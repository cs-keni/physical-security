# 28 — Calculators

Working, tested Python calculators for physical security engineering. **Pure standard
library** — no `pip install`, so it runs on a locked-down work laptop without asking anyone
for permission.

```bash
python3 28_Calculators/demo.py              # worked examples with interpretation
python3 28_Calculators/tests/test_psec.py   # 68 tests
```

## The rule

> **Work the hand calculation in `32_Engineering_Math/` before you use the matching module
> here.** A calculator you cannot reproduce on paper is a liability, not a tool. The number
> it produces goes into a document with your name on it, and "the spreadsheet said so" is
> not a defense in a design review.

## Modules

| Module | Covers | Math lesson |
|---|---|---|
| `psec.optics` | Angle of view, FOV width, lens selection, slant range, depression angle, pixel density (PPF/PPM), DORI classification, max range for a target class, full camera coverage reports | `32_Engineering_Math/01`, `02` |
| `psec.video` | Bitrate scaling (fps, codec, smart codec), GB/day, storage for retention, camera groups, peak vs. average bandwidth, headroom, honest storage *ranges*, RAID raw capacity, inverse retention | `32_Engineering_Math/03`, `04` |
| `psec.power` | PoE class budgets and switch checks, voltage drop, max run length, conductor selection, battery Ah sizing, runtime, power supply sizing | `32_Engineering_Math/05`, `06`, `07` |
| `psec.pps` | Adversary path timelines, timely detection (`T_A > T_R`), required detection point, intervention comparison | `01_Foundations/03` |

## Design decisions worth knowing about

These are places where the code embeds a judgment. Challenge them rather than inheriting them.

- **PoE is budgeted by class, not by datasheet draw**, by default. Many switches allocate by
  class, so a 6 W camera that classifies Type 2 can reserve 30 W. Pass `actual_draw_w` only
  when you have verified your switch allocates dynamically. `[VERIFY per switch datasheet]`
- **Voltage drop uses K = 12.9 (copper at ~75 °C)**, not the 20 °C value. Resistance rises
  with temperature; calculating cold understates drop on a loaded circuit in a hot ceiling.
- **Frame-rate bitrate scaling is sub-linear** (`ratio ** 0.7`). Halving fps does not halve
  bitrate — I-frames and overhead don't scale, and inter-frame prediction gets *less*
  efficient as frames differ more. This is a modeling choice, documented so you can argue
  with it.
- **Storage is reported as a range**, because bitrate is the dominant uncertainty and you
  don't know it at design time. Two vendor calculators will disagree by 2× on the same
  camera. Present the range; put the point estimate inside it.
- **Battery sizing applies both a discharge derate (1.25) and an aging factor (1.25).** A
  battery sized to exactly meet requirement on day one fails to meet it in year two, and
  nobody tests it until the outage.
- **`slant_range_ft` is used in coverage reports**, not floor distance. Ignoring mount height
  overstates PPF for near targets — which is every indoor camera.
- **`compare_interventions` refuses to emit a negative detection target.** When the response
  deficit exceeds the entire adversary path, it says the detection lever is not achievable
  rather than producing arithmetically-true nonsense.

## What these calculators deliberately do NOT model

Knowing the limits is the point.

- **Optics:** no lens distortion (barrel distortion below ~2.8 mm is significant and
  unmodeled), no fisheye projection, no MTF, no focus error, no motion blur, no compression
  loss. Geometric pixel density is a *necessary, not sufficient* condition for a usable image.
- **Video:** no scene-content modeling, no per-vendor codec behavior, no I-frame interval
  effects, no audio, no metadata/analytics overhead.
- **Power:** no AC-side anything, no inrush, no battery charging current, no temperature
  derating of batteries, no NEC conductor ampacity or fill calculations. This is a design
  aid, not an electrical engineer.
- **PPS:** single linear path only, binary/instantaneous detection (no `P_d` propagation),
  models interruption rather than neutralization, and **does not apply to insiders at all**.

## Extending

Adding a sensor format, an AWG size, or a PoE type is a dict entry. Adding a formula means
adding the derivation to `32_Engineering_Math/` **and** a test whose expected value was
computed by hand. The tests are the record of the derivations — if one fails after you change
a formula, redo the hand calculation before you change the test.
