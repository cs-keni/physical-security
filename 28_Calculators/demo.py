#!/usr/bin/env python3
"""Worked examples for every psec calculator.

    python3 28_Calculators/demo.py

Read the OUTPUT alongside the corresponding 32_Engineering_Math lesson. Each
section prints the inputs, the result, and the engineering interpretation --
because the interpretation is the part that matters and the part a spreadsheet
never gives you.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from psec import optics, power, pps, video


def rule(title: str) -> None:
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def table(rows: list[dict]) -> None:
    if not rows:
        return
    cols = list(rows[0])
    widths = {c: max(len(c), max(len(str(r[c])) for r in rows)) for c in cols}
    print("  " + " | ".join(c.ljust(widths[c]) for c in cols))
    print("  " + "-+-".join("-" * widths[c] for c in cols))
    for r in rows:
        print("  " + " | ".join(str(r[c]).ljust(widths[c]) for c in cols))


# ---------------------------------------------------------------------------
rule("1. CAMERA OPTICS -- entrance lobby, identification required")

cam = optics.CameraSpec(
    name="CAM-1-101 (lobby entry)",
    horizontal_pixels=1920, vertical_pixels=1080,
    sensor_format="1/2.8", focal_length_mm=6.0, mount_height_ft=9.0,
)
print(f"  {cam.name}: {cam.megapixels:.1f} MP, {cam.sensor_format}\" sensor, "
      f"{cam.focal_length_mm} mm lens at {cam.mount_height_ft} ft AFF")
print(f"  Horizontal AOV: {cam.hfov_deg:.1f} deg   Vertical AOV: {cam.vfov_deg:.1f} deg")
print()
table(cam.coverage_report([8.0, 15.0, 25.0, 40.0, 60.0]))
print(f"\n  Max range for IDENTIFY (76 PPF): {cam.max_range_ft('identify'):.1f} ft")
print(f"  Max range for RECOGNISE (38 PPF): {cam.max_range_ft('recognise'):.1f} ft")
print(f"  Max range for DETECT (8 PPF):     {cam.max_range_ft('detect'):.1f} ft")
print("""
  INTERPRETATION
  This camera identifies only within about 28 ft, and recognises to about 57 ft.
  If the design intent is "identify everyone who enters", the door must sit
  inside 28 ft -- and note the depression column: past ~30 deg (which happens
  close to the camera) the face is foreshortened and
  the geometric pixel count overstates what you will actually get. Mount lower
  and aim flatter for identification, or accept recognition instead and say so
  in the Basis of Design.""")

# ---------------------------------------------------------------------------
rule("2. LENS SELECTION -- inverse problem, the one you actually use")

for dist, width in ((30, 20), (60, 25), (100, 40)):
    f = optics.focal_length_for_width_mm(dist, width, 5.37)
    ppf = optics.pixel_density_ppf(1920, width)
    print(f"  Cover {width} ft wide at {dist} ft -> {f:5.1f} mm lens "
          f"-> {ppf:5.1f} PPF ({optics.classify_ppf(ppf)})")
print("""
  INTERPRETATION
  Lens comes from geometry, not preference. Pick the scene you must cover and
  the distance you can mount at; the lens falls out. Then check the resulting
  PPF against the task -- if it is short, you need more pixels, a narrower view,
  a closer mount, or a relaxed requirement. Those are the only four options.""")

# ---------------------------------------------------------------------------
rule("3. VIDEO STORAGE AND BANDWIDTH -- 200-camera facility")

sysm = video.VideoSystem(headroom=0.20)
sysm.add(video.CameraGroup("Interior fixed 4 MP",  count=120,
                           bitrate_mbps=video.scale_bitrate_mbps(10.0, codec="h265"),
                           retention_days=30))
sysm.add(video.CameraGroup("Exterior 4 MP, motion", count=60,
                           bitrate_mbps=video.scale_bitrate_mbps(10.0, codec="h265"),
                           motion_duty_cycle=0.40, retention_days=30))
sysm.add(video.CameraGroup("Critical 8 MP, 90 day", count=20,
                           bitrate_mbps=video.scale_bitrate_mbps(18.0, codec="h265"),
                           retention_days=90))

s = sysm.summary()
for k, v in s.items():
    print(f"  {k:28s}: {v}")
print(f"\n  Raw disk for RAID 6 (12-disk groups): "
      f"{sysm.raid_raw_capacity_tb(s['storage_with_headroom_tb'], 'raid6', 12):.0f} TB")
print("""
  INTERPRETATION
  Report the RANGE, not the point estimate. Bitrate is the dominant uncertainty
  and you do not know it at design time. Size the network on PEAK, not average:
  motion events correlate, so the averaging you hoped for disappears exactly
  when it matters. And note the 90-day group -- 20 cameras consume as much as
  the 120-camera group. Retention, not camera count, drives storage cost.""")

# ---------------------------------------------------------------------------
rule("4. RETENTION -- the retrofit question")

groups = [video.CameraGroup("existing", 85, 6.0)]
print(f"  Client has 60 TB of usable storage and 85 cameras at 6 Mbps continuous.")
print(f"  Achievable retention: "
      f"{video.retention_days_achievable(60, groups):.1f} days")
print("""
  INTERPRETATION
  They believe they have 30 days. Ask what their retention POLICY says, then
  measure what the system actually holds. The gap between the two is one of the
  most common and most consequential findings in an existing-conditions survey,
  because it is usually discovered during a legal request.""")

# ---------------------------------------------------------------------------
rule("5. POE BUDGET -- IDF switch check")

sw = power.PoESwitch("IDF-2 SW-1", port_count=48, poe_budget_w=740.0,
                     spare_port_pct=0.20)
sw.add(power.PoEDevice("Fixed dome (Type 1)", 22, "af"))
sw.add(power.PoEDevice("Multisensor (Type 2)", 6, "at"))
sw.add(power.PoEDevice("PTZ w/ heater (Type 3)", 4, "bt_t3"))
sw.add(power.PoEDevice("Intercom (Type 1)", 2, "af"))

for k, v in sw.summary().items():
    if k != "findings":
        print(f"  {k:24s}: {v}")
for f in sw.summary()["findings"]:
    print(f"  !! {f}")
print("""
  INTERPRETATION
  Budget by CLASS, not by datasheet draw, unless you have verified the switch
  allocates dynamically. A 6 W camera that classifies as Type 2 can reserve 30 W.
  Discovering this in the field means a switch swap, a change order, and an
  awkward conversation.""")

# ---------------------------------------------------------------------------
rule("6. VOLTAGE DROP -- lock power run")

supply_v, current_a, run_ft, min_v = 24.0, 0.6, 250.0, 21.6
for awg in ("18", "16", "14"):
    vd = power.voltage_drop_v(current_a, run_ft, awg)
    vl = supply_v - vd
    ok = "OK " if vl >= min_v else "FAIL"
    print(f"  {awg} AWG: drop {vd:5.2f} V -> {vl:5.2f} V at the lock  [{ok}]")

chosen = power.smallest_awg_for_run(supply_v, current_a, run_ft, min_v)
print(f"\n  Smallest acceptable conductor: {chosen} AWG")
print(f"  Max run on 18 AWG at this current: "
      f"{power.max_run_length_ft(supply_v, current_a, '18', min_v):.0f} ft")
print("""
  INTERPRETATION
  The factor of 2 for the round trip is the most-missed term in this formula.
  Also: calculate against the LOW end of the supply's output range, not nominal
  -- a battery-backed supply sags on standby, which is precisely when you need
  the lock to work.""")

# ---------------------------------------------------------------------------
rule("7. BATTERY SIZING -- 12-door access control panel")

loads = [
    power.Load("Readers", 12, 0.100),
    power.Load("Electric strikes (standby 0, alarm 0.35 A)", 12, 0.0, alarm_a_each=0.35),
    power.Load("Controller boards", 2, 0.250),
]
r = power.battery_ah_required(loads, standby_hours=4.0, alarm_minutes=5.0)
for k, v in r.items():
    print(f"  {k:22s}: {v}")
print(f"\n  Power supply: {power.power_supply_sizing(loads)}")
print("""
  INTERPRETATION
  Standby duration is frequently CODE-DRIVEN and jurisdiction-specific --
  [VERIFY] against NFPA 72, UL 294, and the AHJ before sizing anything real.
  The aging factor matters: a battery sized to exactly meet requirement on day
  one fails to meet it in year two, and nobody tests it until the outage.""")

# ---------------------------------------------------------------------------
rule("8. TIMELY DETECTION -- does the system actually interrupt?")

path = pps.AdversaryPath(
    "North dock -> tool crib",
    assessment_delay_s=20.0,
    adversary_description="2 persons, hand tools, unwilling to be observed for long",
)
path.add(pps.Task("Climb perimeter fence", 20))
path.add(pps.Task("Cross yard to building", 40))
path.add(pps.Task("Force dock personnel door", 150,
                  detected_here=True, detection_note="DPS + assessment camera"))
path.add(pps.Task("Traverse warehouse floor", 60))
path.add(pps.Task("Cut tool crib mesh", 200))
path.add(pps.Task("Load and remove goods", 240))

table(path.timeline())
print()
for rft, label in ((300.0, "on-site guard"), (1800.0, "contract patrol")):
    res = path.evaluate(rft, required_margin_s=60.0)
    print(f"  Response = {label} ({rft:.0f} s): {res['verdict']}")

print("\n  If not timely, the levers are:")
cmp_ = pps.compare_interventions(path, 1800.0, required_margin_s=60.0)
if not cmp_["already_timely"]:
    print(f"  Deficit: {cmp_['deficit_s']:.0f} s")
    for name, text in cmp_["levers"].items():
        print(f"\n  - {name.upper()}:\n      {text}")
print("""
  INTERPRETATION
  Response time is usually the dominant term and usually NOT an engineering
  variable. When no achievable amount of hardware makes a system timely, the
  deliverable is not more hardware -- it is a clear statement that the owner is
  choosing between changing the response model, accepting a documentation-only
  system, or reducing the consequence. That last option is the one nobody
  proposes and it is frequently the cheapest.""")

print("\n" + "=" * 78)
print("Now do these by hand. See 32_Engineering_Math/ for derivations and")
print("problem sets. A calculator you cannot reproduce on paper is a liability.")
print("=" * 78)
