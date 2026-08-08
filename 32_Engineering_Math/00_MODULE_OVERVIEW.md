# Module 32 — Engineering Math

> **Time:** ~18–24 hours over 5–7 weeks for the full module, including the problem sets.
> **Prerequisite:** [`../01_Foundations/`](../01_Foundations/) — the functional chain (`03`) is
> assumed by lesson 08. Lessons 05–07 read better after
> [`../35_Doors_and_Hardware/`](../35_Doors_and_Hardware/) lessons 03–06, which show what these
> numbers do to a real opening.
> **Why this module exists:** [`../28_Calculators/`](../28_Calculators/) already computes all of
> this correctly. This module is the **derivation record** for it. `test_psec.py`'s own docstring
> says *"Expected values are hand-computed in the corresponding 32_Engineering_Math lessons"* —
> so every one of its 68 tests traces to a hand calculation written out here.

## Lessons

| # | Lesson | Core question it answers | Derives |
|---|---|---|---|
| 01 | [Camera Field of View and Focal Length](01_camera_fov.md) | How much scene does this lens actually see, and what lens do I need? | `psec.optics` |
| 02 | [Pixel Density and DORI](02_pixel_density.md) | Is there enough resolution on the subject to do the job I promised? | `psec.optics` |
| 03 | [Video Bandwidth](03_bandwidth.md) | How much network does this camera need, and how much do I trust that figure? | `psec.video` |
| 04 | [Storage and Retention](04_storage.md) | How much disk buys the retention they asked for? | `psec.video` |
| 05 | [PoE Budgets and Switch Capacity](05_poe.md) | Will this switch actually power what I hung off it? | `psec.power` |
| 06 | [Voltage Drop and Conductor Selection](06_voltage_drop.md) | Will the volts survive the trip to the device? | `psec.power` |
| 07 | [Battery and Power Supply Sizing](07_battery_ups.md) | How big a supply, and how big a battery, and why are they sized on different currents? | `psec.power` |
| 08 | [Adversary Path and Timely Detection](08_adversary_path.md) | Does the system detect early enough to matter? | `psec.pps` |

## Assessment and practice

- 🧮 [**The integrated sizing capstone**](_exercises/integrated_sizing.md) — the module capstone.
  One fictional site sized end to end through all eight lessons: cameras → FOV → PPF → bitrate →
  storage → PoE → voltage drop → battery → adversary path. Reference solution in
  [`_solutions/integrated_sizing_reference.md`](_solutions/integrated_sizing_reference.md).
- Every lesson ends with a **problem set**, answered in
  [`_solutions/`](_solutions/). Work them with a calculator and paper before opening the
  solutions — several of them contain deliberate traps that arithmetic alone will walk straight
  past.
- [`../25_Quizzes/quiz_32_engineering_math.md`](../25_Quizzes/quiz_32_engineering_math.md) — 30
  questions. Take it cold, before reading, then again after.
- [`../26_Flashcards/32_engineering_math.csv`](../26_Flashcards/32_engineering_math.csv) —
  Anki-importable. Formulas and the reasoning that selects between them, not just definitions.

## Learning objectives for the module

By the end of this module you can:

1. Derive the field-of-view and pixel-density relationships from the pinhole geometry rather than
   looking them up, and **invert** them — the direction design actually requires.
2. Compute slant range and depression angle, and explain why ignoring them overstates coverage
   for nearly every indoor camera.
3. State where a bitrate figure legitimately comes from, apply frame-rate and codec scaling
   correctly, and distinguish peak from average.
4. Carry a bitrate through to storage with every unit conversion explicit, get the
   decimal/binary distinction right, and present an honest range rather than a false point value.
5. Solve the inverse storage problem — how many days does the disk they already own actually
   buy — and deliver that answer to an owner who believes it is more.
6. Budget a PoE switch against class allocation rather than datasheet draw, and identify which of
   the four independent failure modes binds a given design.
7. Derive `Vd = 2·K·I·L / CM` from Ohm's law, invert it for run length and conductor size, and
   **sum drops across segments of differing gauge**.
8. Size a power supply and a battery from the same load list, and explain why peak current
   governs one and standby current governs the other.
9. State the timeliness inequality, compute the required detection point, and reason about the
   deficit through the four intervention levers.
10. For every calculation above: state its assumptions, name the conditions under which it
    silently stops being true, and communicate the uncertainty alongside the number.

## How to study this module

**Do the arithmetic by hand first, then check it against `psec`.** That order is the entire point.
Running the calculator first and reading the derivation afterward produces the feeling of
understanding without the thing itself. Every worked value in these lessons was produced by
running `psec` and transcribing the result, so your hand calculation and the code should agree to
the digit. When they don't, one of you is wrong and finding out which is the skill.

Lessons **01 and 02** are one continuous derivation. `W = D·w/f` from lesson 01 is load-bearing
for everything in lesson 02; don't start 02 without it.

Lessons **03 and 04** are the same. Read the warning at the top of each. These two produce the
least trustworthy numbers in the module, and the reason they are here is to teach you how to say
so out loud while still giving the client a figure they can build to. The most important sections
in lesson 04 are the two on presenting a range and on the inverse problem — not the arithmetic.

Lessons **05, 06, and 07** are the electrical core, and they are the ones most likely to be tested
by reality on a Tuesday afternoon. Lesson 06 continues
[`../35_Doors_and_Hardware/06_electrified_hardware_power_transfer.md`](../35_Doors_and_Hardware/06_electrified_hardware_power_transfer.md)
directly — same opening, same failure, now with the derivation under it. Note that problem P6.4
**reverses** module 35's conclusion: there the transfer dominated, here the home run does.
"Always check the transfer" is a habit, not a rule, and the problem set exists to break it.

Lesson **08** is different in kind. It is the only lesson whose inputs are estimates of human
behavior rather than properties of hardware, and it is the one where the arithmetic is easy and
the judgment is hard.

Finish with the [integrated sizing capstone](_exercises/integrated_sizing.md). It is where eight
separate calculations become one design, and where you discover that they constrain each other.

## The load-bearing ideas

If you retain eight things from this module:

1. **A calculator you can't derive is a calculator you can't debug.** When two tools disagree by
   30%, only the derivation tells you which one is wrong.
2. **The design direction is the inverse.** Calculators give coverage from a lens, days from a
   disk, drop from a gauge. Designers need the lens, the disk, and the gauge. Learn every formula
   in the direction you will actually use it.
3. **Pixel density falls as `1/D`, not `1/D²`.** Light falls off as the inverse square; resolution
   on target does not. Confusing the two makes camera placement look worse than it is.
4. **A number without its uncertainty is not an engineering answer.** Bitrate and storage figures
   carry genuine 2× disagreement between vendors. Say the range.
5. **Track your units or they will track you.** The one real defect found while writing this
   module was a decimal megabyte divided by 1024 — see below. Dimensional analysis is not
   pedantry; it is the only cheap defect detector you have.
6. **Budget against what the source must supply, not what the load will draw.** True for PoE class
   allocation, true for supply sizing, true anywhere a rating and a measurement disagree.
7. **Peak current sizes the supply; standby current sizes the battery.** The most commonly
   reversed pair in low-voltage design.
8. **Detection is timely or it is decorative.** `T_D + T_A + T_R ≤ T_T` is the whole system in one
   line, and the required detection point is how a detection layer gets located by calculation
   instead of by habit.

## A defect this module found

Writing lesson 04 by hand surfaced a real bug in
[`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py):
`stream_gb_per_day(decimal_gb=False)` divided **decimal** megabytes by 1024. A bitrate is decimal,
so those megabytes are 10⁶ bytes; converting to gibibytes requires dividing by 2³⁰/10⁶ =
1073.741824. The bug reported the decimal/binary gap at TB scale as **4.86%** when the true figure
is **9.95%** — the exact "classic ~10% error" the function's own docstring warned about. The code
contradicted its own comment, and no test caught it, because the only test on that path asserted
`binary < decimal`, which is true either way.

This is worth knowing for two reasons. It is why the module's test count went **66 → 68**
(`test_binary_units_are_true_gibibytes` and
`test_decimal_binary_gap_at_tb_scale_is_about_ten_percent`). And it is the argument for this whole
module in one example: the code was written, reviewed, and tested, and it took working the units
by hand to find it.

## Cross-references

| Module | Relationship |
|---|---|
| [`../28_Calculators/`](../28_Calculators/) | The implementation. This module is its derivation record; `test_psec.py` is the shared ground truth. |
| [`../01_Foundations/03_functional_chain.md`](../01_Foundations/03_functional_chain.md) | Detect / delay / respond conceptually. Lesson 08 derives its arithmetic. |
| [`../03_Video_Surveillance/`](../03_Video_Surveillance/) | Lens selection, resolution, and retention in design context. Lessons 01–04 supply the math. |
| [`../08_Networking/`](../08_Networking/) | Where lesson 03's peak bandwidth becomes a switch uplink and a VLAN. |
| [`../34_Electrical_Power/`](../34_Electrical_Power/) | Power supplies, batteries, and distribution in depth. Lessons 05–07 supply the math. |
| [`../35_Doors_and_Hardware/06_electrified_hardware_power_transfer.md`](../35_Doors_and_Hardware/06_electrified_hardware_power_transfer.md) | Forward-references lesson 06. Same worked opening, carried forward with the multi-segment case. |
| [`../02_Risk_Assessment/`](../02_Risk_Assessment/) | Adversary path analysis and finding the weakest path — the design work lesson 08 measures. |
| [`../16_Automation/data_model/`](../16_Automation/data_model/) | The device register these calculations are ultimately run against. |
| [`../10_Codes_Standards/`](../10_Codes_Standards/) | Determining the adopted edition behind lessons 05 and 07's code-driven minimums. |

## Certification mapping

| Content | APP domain | PSP domain |
|---|---|---|
| Optics, pixel density, DORI | — | D2 Application, Design & Integration |
| Bandwidth, storage, retention | — | D2, D3 Implementation |
| PoE budgets, switch capacity | — | D2, D3 |
| Voltage drop, conductor selection | — | D2, D3 |
| Battery and supply sizing | D4 Security Operations | D2, D3 |
| Adversary path, timely detection | D1 Security Fundamentals | D1 Physical Security Assessment, D2 |

> `[VERIFY]` Domain names and numbering per the current official ASIS Certification Handbook.
> These mappings are **provisional** — see [`../31_References/source_index.md`](../31_References/source_index.md)
> for the confidence note. The APP/PSP tracks are blocked on human verification.

---

> ⚠️ **A standing warning for this module.** These are **design aids**, not compliance
> determinations. Lessons 05, 06, and 07 touch subjects where the NEC as adopted in your
> jurisdiction, NFPA 72, UL 294, and the AHJ have the final word, and where anything at line
> voltage belongs to a licensed electrical engineer. `[CODE][VERIFY]` Every default in these
> lessons and in `psec` is engineering practice. **Sizing something perfectly against the wrong
> requirement is still wrong.** Confirm the requirement first.
