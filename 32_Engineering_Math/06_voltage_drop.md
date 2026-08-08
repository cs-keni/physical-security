# 06 — Voltage Drop and Conductor Selection

> Derives the voltage-drop functions in
> [`../28_Calculators/psec/power.py`](../28_Calculators/psec/power.py).
>
> **This is the lesson that
> [`../35_Doors_and_Hardware/06_electrified_hardware_power_transfer.md`](../35_Doors_and_Hardware/06_electrified_hardware_power_transfer.md)
> forward-references.** That lesson showed what a voltage-drop failure looks like in a building —
> an "access control software problem" that is actually copper. This one shows where the number
> comes from, and adds the multi-segment case that module 35 established as the one that catches
> people.

> **Scope.** Low-voltage DC for security devices. Line voltage, branch circuits, grounding and
> bonding belong to a licensed EE and the NEC as adopted. `[CODE][VERIFY]`

## Learning objectives

- Derive `Vd = 2·K·I·L / CM` from Ohm's law and conductor resistivity.
- Explain the factor of 2, the choice of `K`, and what a circular mil is.
- Invert the formula for maximum run length and for conductor selection.
- **Sum drops across segments of different gauge**, and explain why a correct home run can still
  fail at the last six feet.
- State what fixes voltage drop and — more usefully — what doesn't.

---

## Derivation — from Ohm's law to the working formula

**Step 1. Ohm's law.**
```
   V = I · R
```
The voltage lost in a conductor is the current through it times its resistance.

**Step 2. Resistance of a conductor.**
```
   R = ρ · L / A
```
Resistance rises with length and falls with cross-sectional area. `ρ` (rho) is resistivity, a
property of the material.

**Step 3. American wire units.** In North American practice, area is measured in **circular
mils** and resistivity is quoted as `K`, in ohm-circular-mils per foot:

```
   R = K · L / CM
```

> **What is a circular mil?** The area of a circle one **mil** (0.001 inch) in diameter. Its
> convenience: `CM = d²` where `d` is the diameter in mils — **no π**. A 40 mil conductor is
> 1,600 circular mils. The factor of π that would appear in a true area calculation is folded
> into `K`, so it never has to be carried through the arithmetic.

**Step 4. The round trip.** Current flows *out* on one conductor and *back* on the other. Both
have resistance. A 200 ft run is 400 ft of copper.

```
   ┌────────────────────────────────┐
   │   Vd  =  2 · K · I · L / CM    │
   └────────────────────────────────┘

   Vd = voltage drop (V)
   K  = 12.9  (copper, ~75 °C, Ω·cmil/ft)
   I  = current (A)
   L  = ONE-WAY run length (ft), as measured on a plan
   CM = conductor area (circular mils)
```

> ⚠️ **Forgetting the 2 halves your answer, and it is the single most common error in this
> calculation.** The result looks plausible — half a volt instead of a volt — and it passes review
> because nobody re-derives it. `L` is the one-way length you would measure on a plan or pull on a
> cable schedule; the formula does the round trip for you.

### Why `K = 12.9` and not `10.4`

Copper's resistivity at 20 °C is about **10.4** Ω·cmil/ft. At 75 °C it is about **12.9**.
`[PRACTICE][VERIFY]`

**Resistance rises with temperature**, so a calculation at room temperature **understates** the
drop on a loaded circuit in a hot ceiling — which is exactly where security cabling lives, and
exactly when the load is highest. Using the warm-conductor value is the conservative choice.

**The magnitude of the choice: 12.9/10.4 = 1.24.** Using the room-temperature figure would give
you 24% less drop than you will actually see on a warm day. That is enough to move a marginal
design from "passes" to "fails," which is precisely the population of designs where it matters.

---

## The conductor table

```
   AWG:     24     23     22     20     18     16     14     12     10
   CM:     404   509.5  640.4  1020   1624   2583   4107   6530  10380
```

**The useful mental rule: circular mils roughly double every 3 AWG sizes.**

```
   24 → 18   is 6 steps:  404 → 1624   =  4.02×   ≈ 2² ✅
   18 → 12   is 6 steps: 1624 → 6530   =  4.02×   ≈ 2² ✅
```

So **dropping 3 AWG sizes halves your voltage drop**, and dropping 6 quarters it. That lets you
estimate a conductor change in your head before reaching for the calculator.

`24` and `23` AWG are in the table because they are Cat5e/Cat6 conductor sizes — relevant when
someone proposes powering a device over spare pairs in a data cable, which is a real and usually
bad idea for anything above a few hundred milliamps.

---

## 🧮 Worked example 6.1 — the test case

0.5 A over a 200 ft run on 18 AWG:

```
   Vd  =  2 × 12.9 × 0.5 × 200 / 1624
       =  2580 / 1624
       =  1.5887 V
```

**1.589 V of drop.** This is `test_voltage_drop_includes_round_trip_factor`.

**Voltage at the load**, from a 24.0 V supply:

```
   V_load = 24.0 − 1.5887 = 22.411 V
```

This is `test_voltage_at_load`.

**Note what the test's name is telling you.** It isn't called `test_voltage_drop`; it's called
`test_voltage_drop_includes_round_trip_factor`. The test exists specifically to pin the factor of
2, because that is the thing that breaks. Naming a test after the failure it prevents is a good
habit — the name is the documentation of *why* the number is 1.589 and not 0.794.

---

## The three linearities

```
   Vd  ∝  I           double the current, double the drop
   Vd  ∝  L           double the length, double the drop
   Vd  ∝  1 / CM      double the copper, halve the drop
```

`test_voltage_drop_scales_linearly_with_length_and_current` pins the first two;
`test_heavier_conductor_drops_less` pins the third's direction.

**These are worth internalizing because they let you reason without computing.** "We moved the
panel twice as far away" immediately means twice the drop. "The device draws three times what we
thought" means three times the drop, and if you were at 1 V you are now at 3 V and probably
failing.

> ⚠️ **The one that isn't linear:** power lost as heat is `P = I²R = I × Vd`, so it goes as the
> **square** of current. At 0.5 A and 1.589 V the loss is 0.79 W — irrelevant. At 3 A over the
> same run the drop is 9.5 V and the loss is 28.6 W, which is both a failed circuit and a warm
> cable. This is the same physics as lesson 05's observation about PoE Type 4.

---

## Inversion 1 — Maximum run length

You have a conductor and a device with a minimum operating voltage. How far can you go?

Solve `V_min = V_supply − 2·K·I·L / CM` for `L`:

```
   ┌──────────────────────────────────────────────────┐
   │   L_max  =  (V_supply − V_min) · CM / (2 · K · I)│
   └──────────────────────────────────────────────────┘
```

### 🧮 Worked example 6.2 — the test case

24.0 V supply, 0.5 A device, 18 AWG, 21.6 V minimum:

```
   Allowable drop = 24.0 − 21.6 = 2.4 V

   L_max = 2.4 × 1624 / (2 × 12.9 × 0.5)
         = 3897.6 / 12.9
         = 302.14 ft
```

**302 ft.** `test_max_run_length_is_self_consistent` confirms the inverse round-trips: feeding
302.14 ft back into `voltage_at_load_v` returns exactly 21.6 V.

**An impossible target raises.** `test_max_run_rejects_impossible_target` asks for 12.0 V minimum
from a 12.0 V supply — zero allowable drop, so no non-zero length works. Returning 0, or a
negative number, would be arithmetically defensible and operationally useless. Raising is right.

---

## Inversion 2 — Conductor selection

The question you actually ask: the run is what it is, so **what wire do I pull?**

```
   Search the conductor table from smallest to largest;
   return the first that delivers ≥ V_min at the load.
```

### 🧮 Worked example 6.3 — the test case

24.0 V supply, 1.0 A, 300 ft, 21.6 V minimum:

| AWG | V at load | Verdict |
|---|---|---|
| 24 | 4.84 V | ❌ |
| 22 | 11.91 V | ❌ |
| 20 | 16.41 V | ❌ |
| 18 | 19.23 V | ❌ |
| 16 | 21.00 V | ❌ (just short) |
| **14** | **22.12 V** | ✅ |

**14 AWG.** This is `test_smallest_awg_selection` — and note what the test actually asserts: not
just that the returned gauge works, but that **every smaller gauge fails.** That is the correct
test for a "smallest that works" function. Asserting only that the answer works would pass an
implementation that always returned 10 AWG.

**Look at 16 AWG: 21.00 V against a 21.6 V requirement.** It misses by 0.6 V. In the field this is
the conductor someone substitutes because it was on the truck, and the failure is intermittent and
temperature-dependent — which is precisely the diagnosis story in module 35 lesson 03.

---

## Multi-segment runs: the case that catches people

**This is the addition module 35 lesson 06 established as necessary.** Real circuits are not one
gauge end to end. A lock circuit is typically:

```
   [Supply] ──── home run, 18–12 AWG ────► [frame] ── transfer, ~24 AWG ──► [lock]
                    100s of feet                        a few feet
```

**Drops in series add.** Total resistance is the sum of segment resistances, so:

```
   ┌───────────────────────────────────────────────────┐
   │   Vd_total  =  Σ  2 · K · I_i · L_i / CM_i        │
   └───────────────────────────────────────────────────┘
```

For a simple series circuit the current is the same in every segment, so:

```
   Vd_total  =  2 · K · I · Σ ( L_i / CM_i )
```

**The bracket is the whole insight: what matters is `L/CM` per segment, summed.** A short segment
of very small conductor can contribute as much as a long segment of large conductor, because the
ratio is what counts.

### 🧮 Worked example 6.4 — module 35's opening, worked properly

An exit device with electric latch retraction drawing **2.8 A**, 200 ft from the supply on
**12 AWG**, then **6 ft of 24 AWG** through the power transfer into the leaf. Supply 24.0 V,
device minimum 21.0 V.

**Segment ratios:**
```
   Home run:  L/CM  =  200 / 6530  =  0.030628
   Transfer:  L/CM  =    6 /  404  =  0.014851
                                      ─────────
   Sum                             =  0.045479
```

**Total drop:**
```
   Vd = 2 × 12.9 × 2.8 × 0.045479  =  3.285 V

   V_load = 24.0 − 3.285 = 20.72 V     ❌  (needs 21.0)
```

**Per segment:**

| Segment | Length | AWG | L/CM | Drop |
|---|---|---|---|---|
| Home run | 200 ft | 12 | 0.030628 | 2.213 V |
| Transfer | 6 ft | 24 | 0.014851 | **1.073 V** |
| **Total** | | | 0.045479 | **3.285 V** |

**Six feet of 24 AWG contributes 33% of the total drop of a 206-foot circuit.**

Its `L/CM` ratio is 0.0149 against the home run's 0.0306 — **half the resistance in 3% of the
length**, because 24 AWG has one sixteenth the copper of 12 AWG.

**And the consequence is decisive:** stopping the calculation at the frame gives 21.79 V, which
passes. Carrying it through the transfer gives 20.72 V, which fails. **The segment everyone omits
is the segment that changes the answer.**

> 🧠 **The general rule: compute `L/CM` for every segment and sum the ratios before multiplying.**
> It makes the relative contribution of each segment visible, which is what tells you *where* to
> spend money. Here, upsizing the home run from 12 to 10 AWG saves 0.82 V; changing the transfer
> from a 24 AWG hinge to an 18 AWG EPT saves 0.86 V — **more, for a fraction of the cost.** You
> cannot see that from a total.

---

## What fixes voltage drop, and what doesn't

| Change | Effect | Why |
|---|---|---|
| **Larger conductor** | ✅ Direct | Reduces `1/CM`. Three AWG sizes halves the drop. |
| **Shorter run** (relocate the supply) | ✅ Direct, often cheapest | Reduces `L`. Also shrinks the failure domain. |
| **Higher supply voltage** | ✅ *if the device tolerates it* | Same drop, bigger budget. Verify the device's maximum. `[MFR][VERIFY]` |
| **Lower-current device** | ✅ Direct | Lesson 03 of module 35: electrified trim instead of latch retraction. |
| **Bigger power supply (more amps)** | ❌ **No effect** | See below |

**Why a bigger supply doesn't help, stated so you can say it in a meeting:**

> Voltage drop is `V = I × R`, and `R` belongs to the wire. The supply sets the voltage at one
> end; the conductor decides how much survives to the other. A supply with more *current capacity*
> at the same output voltage delivers the same voltage at the load.
>
> **"The supply isn't running out of current, the wire is eating the volts. More amps on the shelf
> doesn't put volts back on the door."**

---

## Why PoE doesn't need this

Covered in lesson 05, restated because the question recurs: PoE delivers at 44–57 V, devices are
specified across that range, the **PSE − PD gap is the standard's pre-computed loss budget**, and
the 100 m channel limit keeps real loss inside it. `[STANDARD][VERIFY]`

**This lesson's arithmetic applies where no standard is doing it for you** — dedicated 12/24 V DC
runs to locks, strikes, sirens, and remote power supplies.

---

## Assumptions and limits

| Assumption | Reality |
|---|---|
| DC, steady state | Inrush is higher, sometimes far higher. **Compute at inrush, not running current.** `[MFR][VERIFY]` |
| Copper at ~75 °C | Aluminium and other temperatures need a different `K` |
| Plan length = wire length | Conduit goes up, over, and around. 200 ft on a plan is often 260 ft of pull. |
| Zero connection resistance | Terminations, splices, and connectors each add a little. Assume the calculation is optimistic. |
| Current is the same in every segment | True for a simple series run; not for a shared trunk feeding several devices |
| The device's minimum voltage is known | Get it from the datasheet, not from "it's a 24 V device" |

**The inrush one is the most consequential.** A device that runs at 0.3 A may pull several amps
for a few hundred milliseconds to actuate. That transient is what determines whether it works, and
computing at steady state is how a design passes review and fails in the building — module 35's
lesson 06 problem set works exactly that case.

---

## Common mistakes

⚠️ **Forgetting the factor of 2.**

⚠️ **Using room-temperature `K`.** 24% optimistic.

⚠️ **Computing at running current instead of inrush.**

⚠️ **Stopping the calculation at the frame.** The last few feet of small conductor can dominate.

⚠️ **Using plan distance instead of routed length.**

⚠️ **Believing a larger power supply fixes it.**

⚠️ **Assuming the device tolerates a raised supply voltage** without checking the maximum.

⚠️ **Powering a lock over spare pairs in a data cable.** 24 AWG at any real current is a
non-starter — check the `L/CM` ratio before entertaining it.

---

## Junior vs. Senior

**Junior:** derives and applies `Vd = 2KIL/CM`; inverts for run length and conductor size; knows
the round-trip factor and the warm-conductor constant.

**Senior:** sums `L/CM` across segments and uses the per-segment contribution to decide where to
spend; computes at inrush; asks for routed length rather than plan distance; reaches for
supply relocation before conductor upsizing because it is usually cheaper and improves the failure
domain; recognizes when three rounds of conductor sizing means the *device* was the wrong choice;
and can explain in one sentence why a bigger supply doesn't help.

---

## Problem set

**P6.1** Derive `Vd = 2·K·I·L/CM` from `V = IR` and `R = ρL/A`, stating what each substitution
does and where the 2 comes from.

**P6.2** Compute the voltage drop and voltage at the load for a 24.0 V supply feeding:
- (a) 0.75 A over 150 ft of 18 AWG
- (b) The same load and distance on 14 AWG
- (c) 2.5 A over 150 ft of 18 AWG
- (d) State the ratio between (a) and (c), and between (a) and (b), and explain both from the
  linearities without recomputing.

**P6.3** A device needs at least 21.5 V and draws 1.2 A. The supply is 24.0 V.
- (a) Compute the maximum run length on 18 AWG and on 14 AWG.
- (b) The actual routed run is 240 ft. What is the smallest conductor that works?
- (c) The installer says they only have 16 AWG on the truck. Compute what the device would see
  and state whether you accept it.

**P6.4** 🧮 A lock circuit: 24.0 V supply, device minimum 21.0 V, current 1.8 A. The home run is
180 ft of 16 AWG; the power transfer adds 8 ft of 24 AWG.
- (a) Compute `L/CM` for each segment and their sum.
- (b) Compute the total drop and the voltage at the device.
- (c) Compute each segment's share of the total drop.
- (d) You have budget for exactly one change. Compare upsizing the home run to 14 AWG against
  changing the transfer to 18 AWG. Which do you do, and why?

**P6.5** The same circuit as P6.4, but the manufacturer's data says inrush is 5.5 A for 300 ms.
Recompute. What changes, and what would you do about it?

**P6.6** Explain, in under 120 words to an installer who wants to fix a "flaky" door by fitting a
larger power supply, why that won't work and what will.

**P6.7** A designer proposes powering a 0.4 A electric strike over two spare pairs of a Cat6 cable
(23 AWG) on a 210 ft run from a 12 V supply. The strike needs 10.8 V minimum. Compute it, and
write your response.

**P6.8** `test_smallest_awg_selection` asserts both that the chosen gauge works *and* that every
smaller gauge fails. Explain why the second assertion is necessary, and give an incorrect
implementation that the first assertion alone would pass.

> Answers: [`_solutions/06_voltage_drop_solutions.md`](_solutions/06_voltage_drop_solutions.md)

---

## Retrieval check

1. Derive the working formula from Ohm's law.
2. Where does the factor of 2 come from, and what is `L`?
3. What is a circular mil, and why is it convenient?
4. Why is `K` 12.9 rather than 10.4, and how much does the choice matter?
5. State the three linearities. Which quantity is *not* linear, and why?
6. Write the formula for maximum run length.
7. How do you combine segments of different gauge, and what quantity do you compare?
8. Name three things that fix voltage drop and one thing that doesn't.

---

## References

- [`../28_Calculators/psec/power.py`](../28_Calculators/psec/power.py) — the implementation.
- [`../28_Calculators/tests/test_psec.py`](../28_Calculators/tests/test_psec.py) — `TestPower`.
- NEC as adopted, conductor properties and voltage-drop guidance. `[CODE][VERIFY]`
- [`../35_Doors_and_Hardware/06_electrified_hardware_power_transfer.md`](../35_Doors_and_Hardware/06_electrified_hardware_power_transfer.md)
  — this arithmetic applied at an opening, including the diagnosis of a "software" fault.
- [`../34_Electrical_Power/`](../34_Electrical_Power/) — power distribution in depth *(not yet
  written)*.
- Device datasheets — minimum operating voltage, running current, and **inrush**. `[MFR]`

**Next:** [07 — Battery and Power Supply Sizing](07_battery_ups.md)
