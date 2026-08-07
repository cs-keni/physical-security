"""Low-voltage power calculations: PoE budgets, voltage drop, battery sizing.

Derivations in ../../32_Engineering_Math/05_poe.md, 06_voltage_drop.md,
07_battery_ups.md.

SAFETY AND SCOPE
----------------
This module covers LOW-VOLTAGE DC and PoE for security devices. It is a design
aid, not a substitute for an electrical engineer, the NEC as adopted in your
jurisdiction, or the AHJ. Anything touching line voltage, branch circuits,
grounding/bonding, or standby power systems belongs to a licensed EE.

Battery standby minimums for fire alarm and for some access-control and
intrusion applications are CODE-DRIVEN and jurisdiction-specific.
[CODE][VERIFY] -- do not take the defaults here as compliance.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# PoE. [STANDARD] IEEE 802.3af / at / bt. [VERIFY current edition.]
#
# Two numbers matter and people conflate them constantly:
#   * PSE power  = what the switch port must be able to SOURCE (budget against this)
#   * PD power   = what the device may DRAW (datasheets quote this)
# The difference is the worst-case cable loss the standard allows.
# ---------------------------------------------------------------------------
POE_CLASSES: dict[str, dict[str, float | str]] = {
    "af":      {"pse_w": 15.4, "pd_w": 12.95, "std": "802.3af (Type 1)"},
    "at":      {"pse_w": 30.0, "pd_w": 25.5,  "std": "802.3at (Type 2, PoE+)"},
    "bt_t3":   {"pse_w": 60.0, "pd_w": 51.0,  "std": "802.3bt Type 3 (PoE++)"},
    "bt_t4":   {"pse_w": 90.0, "pd_w": 71.3,  "std": "802.3bt Type 4 (PoE++)"},
}

# Copper resistivity, ohm-circular-mil per foot at ~75 C. Using a warm-conductor
# value is the conservative choice: resistance rises with temperature, so a
# calculation at 20 C understates drop on a loaded circuit in a hot ceiling.
K_COPPER_75C = 12.9

# Circular mils by AWG -- the sizes that actually appear in security work.
AWG_CIRCULAR_MILS: dict[str, float] = {
    "24": 404.0,     # Cat5e/Cat6 conductor
    "23": 509.5,     # Cat6/6A conductor
    "22": 640.4,
    "20": 1020.0,
    "18": 1624.0,    # very common for lock power
    "16": 2583.0,
    "14": 4107.0,
    "12": 6530.0,
    "10": 10380.0,
}


# ---------------------------------------------------------------------------
# PoE budgeting
# ---------------------------------------------------------------------------

@dataclass
class PoEDevice:
    name: str
    count: int
    poe_class: str                 # key into POE_CLASSES
    actual_draw_w: float | None = None   # from the datasheet, if known

    def __post_init__(self) -> None:
        if self.poe_class not in POE_CLASSES:
            raise ValueError(
                f"Unknown PoE class {self.poe_class!r}; "
                f"use one of {sorted(POE_CLASSES)}")
        _positive("count", self.count)

    @property
    def budget_w_each(self) -> float:
        """Watts to reserve per device at the switch.

        Uses the class PSE allocation unless a measured/datasheet draw is given.

        WHY THE CLASS VALUE, NOT THE DATASHEET VALUE, IS THE SAFE DEFAULT:
        many switches allocate by CLASS, not by actual consumption, so a 6 W
        camera that classifies as Type 2 can reserve 30 W of the switch budget.
        Whether your switch does static or dynamic allocation is a per-model
        question. [VERIFY per switch datasheet.] Budgeting by class is the
        conservative answer and it is what will keep you out of trouble.
        """
        if self.actual_draw_w is not None:
            return self.actual_draw_w
        return float(POE_CLASSES[self.poe_class]["pse_w"])

    @property
    def total_w(self) -> float:
        return self.budget_w_each * self.count


@dataclass
class PoESwitch:
    name: str
    port_count: int
    poe_budget_w: float
    devices: list[PoEDevice] = field(default_factory=list)
    spare_port_pct: float = 0.20   # [PRACTICE] 20% spare ports is a common minimum

    def add(self, device: PoEDevice) -> "PoESwitch":
        self.devices.append(device)
        return self

    @property
    def ports_used(self) -> int:
        return sum(d.count for d in self.devices)

    @property
    def ports_free(self) -> int:
        return self.port_count - self.ports_used

    @property
    def power_used_w(self) -> float:
        return sum(d.total_w for d in self.devices)

    @property
    def power_headroom_w(self) -> float:
        return self.poe_budget_w - self.power_used_w

    @property
    def power_utilisation_pct(self) -> float:
        return 100.0 * self.power_used_w / self.poe_budget_w

    def check(self) -> list[str]:
        """Return a list of findings. Empty list means it passes."""
        findings: list[str] = []
        if self.ports_used > self.port_count:
            findings.append(
                f"OVERSUBSCRIBED PORTS: {self.ports_used} devices on "
                f"{self.port_count} ports.")
        if self.power_used_w > self.poe_budget_w:
            findings.append(
                f"POE BUDGET EXCEEDED: {self.power_used_w:.1f} W required vs "
                f"{self.poe_budget_w:.1f} W available "
                f"(over by {self.power_used_w - self.poe_budget_w:.1f} W).")
        required_spare = math.ceil(self.port_count * self.spare_port_pct)
        if self.ports_free < required_spare:
            findings.append(
                f"INSUFFICIENT SPARE PORTS: {self.ports_free} free, "
                f"{required_spare} required at {self.spare_port_pct:.0%}.")
        if self.power_utilisation_pct > 80:
            findings.append(
                f"POE BUDGET TIGHT: {self.power_utilisation_pct:.0f}% utilised. "
                f"Adding one more device may fail; check growth plan.")
        return findings

    def summary(self) -> dict:
        return {
            "switch": self.name,
            "ports_used": self.ports_used,
            "ports_total": self.port_count,
            "ports_free": self.ports_free,
            "poe_used_w": round(self.power_used_w, 1),
            "poe_budget_w": round(self.poe_budget_w, 1),
            "poe_headroom_w": round(self.power_headroom_w, 1),
            "poe_utilisation_pct": round(self.power_utilisation_pct, 1),
            "findings": self.check(),
        }


# ---------------------------------------------------------------------------
# Voltage drop
# ---------------------------------------------------------------------------

def voltage_drop_v(current_a: float, length_ft: float, awg: str,
                   *, k: float = K_COPPER_75C) -> float:
    """DC voltage drop over a two-conductor run.

        Vdrop = 2 * K * I * L / CM

    The factor of 2 is the round trip -- current goes out on one conductor and
    back on the other. Forgetting it halves your answer and is the single most
    common error in this calculation.

    ``length_ft`` is the ONE-WAY run length (as you would measure on a plan or
    pull on a cable schedule), not the loop length.
    """
    _positive("current_a", current_a)
    _positive("length_ft", length_ft)
    cm = _circular_mils(awg)
    return 2.0 * k * current_a * length_ft / cm


def voltage_at_load_v(supply_v: float, current_a: float, length_ft: float,
                      awg: str, *, k: float = K_COPPER_75C) -> float:
    return supply_v - voltage_drop_v(current_a, length_ft, awg, k=k)


def voltage_drop_pct(supply_v: float, current_a: float, length_ft: float,
                     awg: str, *, k: float = K_COPPER_75C) -> float:
    _positive("supply_v", supply_v)
    return 100.0 * voltage_drop_v(current_a, length_ft, awg, k=k) / supply_v


def max_run_length_ft(supply_v: float, current_a: float, awg: str,
                      min_device_v: float, *, k: float = K_COPPER_75C) -> float:
    """Longest run that still delivers at least ``min_device_v`` at the load.

    Rearranged from the drop equation:

        L_max = (V_supply - V_min) * CM / (2 * K * I)

    ``min_device_v`` comes from the DEVICE datasheet, not from a rule of thumb.
    A "12 VDC" mag lock may be specified to operate at 10.2-13.8 V; a "12 VDC"
    reader may need 11.0 V. Use the tightest device on the circuit, and remember
    that a battery-backed supply sags toward the low end of its range on
    standby -- so calculate against the LOW supply voltage, not the nominal one.
    """
    _positive("current_a", current_a)
    if min_device_v >= supply_v:
        raise ValueError("min_device_v must be below supply_v")
    cm = _circular_mils(awg)
    return (supply_v - min_device_v) * cm / (2.0 * k * current_a)


def smallest_awg_for_run(supply_v: float, current_a: float, length_ft: float,
                         min_device_v: float, *,
                         k: float = K_COPPER_75C,
                         candidates: list[str] | None = None) -> str:
    """Smallest (highest-gauge-number) conductor that still works."""
    if candidates is None:
        candidates = sorted(AWG_CIRCULAR_MILS, key=lambda a: AWG_CIRCULAR_MILS[a])
    for awg in candidates:
        if voltage_at_load_v(supply_v, current_a, length_ft, awg, k=k) >= min_device_v:
            return awg
    raise ValueError(
        f"No candidate conductor delivers {min_device_v} V at {length_ft} ft "
        f"and {current_a} A. Move the power supply closer, use a higher supply "
        f"voltage, or use local power.")


# ---------------------------------------------------------------------------
# Battery and standby
# ---------------------------------------------------------------------------

@dataclass
class Load:
    name: str
    count: int
    standby_a_each: float
    alarm_a_each: float | None = None   # higher draw during alarm, if applicable

    @property
    def standby_a(self) -> float:
        return self.count * self.standby_a_each

    @property
    def alarm_a(self) -> float:
        each = self.alarm_a_each if self.alarm_a_each is not None else self.standby_a_each
        return self.count * each


def battery_ah_required(loads: list[Load], standby_hours: float,
                        alarm_minutes: float = 0.0,
                        *, derate: float = 1.25,
                        aging_factor: float = 1.25) -> dict:
    """Battery capacity for a required standby duration.

        Ah = (I_standby * H_standby + I_alarm * H_alarm) * derate * aging

    ``derate`` (default 1.25) accounts for the fact that a lead-acid battery
    delivers less than its rated capacity at higher discharge rates and lower
    temperatures (Peukert effect), and that you should not fully discharge it.

    ``aging_factor`` (default 1.25) accounts for capacity loss over service life.
    Sizing a battery to exactly meet requirement on day one means it fails to
    meet it in year two.

    [CODE][VERIFY] Required standby durations for fire alarm and for some
    security applications are set by code and by the AHJ (NFPA 72 sets fire
    alarm secondary power requirements; UL 294 addresses access control system
    standby). The defaults here are engineering practice, NOT a compliance
    determination. Confirm the requirement before you size anything real.
    """
    _nonneg("standby_hours", standby_hours)
    _nonneg("alarm_minutes", alarm_minutes)
    if not loads:
        raise ValueError("no loads supplied")

    i_standby = sum(l.standby_a for l in loads)
    i_alarm = sum(l.alarm_a for l in loads)

    ah_standby = i_standby * standby_hours
    ah_alarm = i_alarm * (alarm_minutes / 60.0)
    ah_raw = ah_standby + ah_alarm
    ah_sized = ah_raw * derate * aging_factor

    return {
        "standby_current_a": round(i_standby, 3),
        "alarm_current_a": round(i_alarm, 3),
        "ah_standby": round(ah_standby, 2),
        "ah_alarm": round(ah_alarm, 2),
        "ah_raw": round(ah_raw, 2),
        "derate": derate,
        "aging_factor": aging_factor,
        "ah_required": round(ah_sized, 2),
        "note": "[CODE][VERIFY] standby duration against NFPA 72 / UL 294 / AHJ",
    }


def runtime_hours(battery_ah: float, load_a: float, *,
                  usable_fraction: float = 0.8) -> float:
    """Approximate runtime for a given battery and constant load.

    ``usable_fraction`` reflects that you should not discharge a lead-acid
    battery to zero. This is a first-order estimate only: real runtime depends
    on discharge rate, temperature, and battery age.
    """
    _positive("battery_ah", battery_ah)
    _positive("load_a", load_a)
    return battery_ah * usable_fraction / load_a


def power_supply_sizing(loads: list[Load], *, headroom: float = 0.25) -> dict:
    """Continuous current a power supply must deliver, with headroom.

    Note the trap: a power supply rated "10 A" is often rated 10 A *peak* with a
    lower continuous rating, and its rating may assume no battery charging. If it
    is also charging a depleted battery, charging current adds to load current.
    [VERIFY per power supply datasheet.]
    """
    if not loads:
        raise ValueError("no loads supplied")
    i_standby = sum(l.standby_a for l in loads)
    i_alarm = sum(l.alarm_a for l in loads)
    i_design = max(i_standby, i_alarm)
    return {
        "standby_current_a": round(i_standby, 3),
        "peak_current_a": round(i_alarm, 3),
        "design_current_a": round(i_design, 3),
        "recommended_supply_a": round(i_design * (1 + headroom), 2),
        "headroom_pct": round(headroom * 100, 1),
        "note": "Does not include battery charging current -- add per datasheet.",
    }


def _circular_mils(awg: str) -> float:
    key = str(awg).strip().upper().replace("AWG", "").strip()
    try:
        return AWG_CIRCULAR_MILS[key]
    except KeyError:
        raise ValueError(
            f"Unknown AWG {awg!r}; known: {sorted(AWG_CIRCULAR_MILS, key=int)}"
        ) from None


def _positive(name: str, value: float) -> None:
    if value is None or value <= 0:
        raise ValueError(f"{name} must be > 0 (got {value!r})")


def _nonneg(name: str, value: float) -> None:
    if value is None or value < 0:
        raise ValueError(f"{name} must be >= 0 (got {value!r})")
