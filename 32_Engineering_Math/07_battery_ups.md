# 07 — Battery and Power Supply Sizing

> Derives the battery and supply-sizing functions in
> [`../28_Calculators/psec/power.py`](../28_Calculators/psec/power.py).

> ⚠️ **Battery standby minimums for fire alarm and for some access-control and intrusion
> applications are CODE-DRIVEN and jurisdiction-specific.** `[CODE][VERIFY]` NFPA 72 sets fire
> alarm secondary power requirements; UL 294 addresses access control system standby. **The
> defaults in this lesson and in the calculator are engineering practice, not a compliance
> determination.** Confirm the required duration before you size anything real. Sizing a battery
> perfectly against the wrong duration is still wrong.

## Learning objectives

- Derive amp-hour capacity from a load list and a required duration.
- Explain the discharge derate and the aging factor, and why both are multiplied rather than
  added.
- Handle the alarm-current component and explain why it barely affects the battery while
  dominating the supply.
- Size a power supply, and explain why **peak current governs the supply while standby current
  governs the battery** — the most commonly reversed pair in this subject.
- Compute realistic runtime and explain the usable-fraction adjustment.

---

## Derivation 1 — Amp-hours from a load list

A battery's capacity is quoted in **amp-hours**: current × time.

```
   Ah  =  I × H
```

For a system with a standby load and, optionally, a higher alarm load for part of the time:

```
   ┌──────────────────────────────────────────────────────────────────┐
   │   Ah_raw  =  I_standby × H_standby  +  I_alarm × (M_alarm / 60)  │
   └──────────────────────────────────────────────────────────────────┘
```

The `/60` converts alarm **minutes** to hours, because alarm durations are specified in minutes
and standby durations in hours.

### Two correction factors, both multiplied

```
   ┌────────────────────────────────────────────────────────┐
   │   Ah_required  =  Ah_raw × derate × aging               │
   │                                                          │
   │   derate = 1.25    discharge rate + temperature          │
   │   aging  = 1.25    capacity loss over service life       │
   └────────────────────────────────────────────────────────┘
```

**Discharge derate (1.25).** A lead-acid battery does not deliver its rated capacity at every
discharge rate. Rated capacity is quoted at a slow reference rate; draw it faster and you get less
(the **Peukert effect**). Cold temperatures reduce it further. And you should not fully discharge
a lead-acid battery — doing so damages it and shortens its life.

**Aging factor (1.25).** A battery loses capacity over its service life. **Sizing a battery to
exactly meet the requirement on day one means it fails to meet it in year two** — and it fails
silently, because nobody load-tests standby batteries until the outage.

**Why multiplied, not added:** they are independent proportional effects on the same quantity. A
battery at 80% of rated capacity from age, delivering 80% of *that* under a fast cold discharge,
gives you 0.8 × 0.8 = 64% — not 60%. Multiplying the reciprocals (1.25 × 1.25 = **1.5625**) is the
correct compensation. Adding them (1 + 0.25 + 0.25 = 1.50) under-sizes by **4.2%**.

> 🧠 **Together they mean you buy roughly 1.56× the arithmetic answer.** That feels like a lot
> until you remember what the failure looks like: the battery that "should" last four hours lasts
> two and a half, at year three, during the outage, and nobody knew.

---

## 🧮 Worked example 7.1 — the test case

8 readers at 0.10 A and 8 locks at 0.25 A, 4-hour standby:

```
   I_standby  =  8(0.10) + 8(0.25)
              =    0.80  +   2.00     =  2.80 A

   Ah_raw     =  2.80 × 4             =  11.20 Ah

   Ah_required = 11.20 × 1.25 × 1.25  =  17.50 Ah
```

**17.5 Ah minimum — specify the next standard size up.** This is `test_battery_sizing`.

Batteries come in standard capacities (7, 12, 18, 26, 40 Ah…), so 17.5 means an **18 Ah** battery.
Note that landing just under a standard size is lucky; landing just over 18 would mean buying 26,
and at that point revisiting the load list or the duration is worth ten minutes.

---

## 🧮 Worked example 7.2 — the alarm component

2 horns drawing 0.05 A standby and **0.90 A in alarm**, 24-hour standby with 5 alarm minutes:

```
   I_standby  =  2 × 0.05  =  0.10 A
   I_alarm    =  2 × 0.90  =  1.80 A

   Ah_standby =  0.10 × 24           =  2.40 Ah
   Ah_alarm   =  1.80 × (5/60)       =  0.15 Ah
                                        ───────
   Ah_raw                            =  2.55 Ah

   Ah_required = 2.55 × 1.5625       =  3.98 Ah
```

This is `test_battery_alarm_component`.

**Look at the proportions.** The alarm load is **18× the standby load** in current, and it
contributes **6% of the amp-hours** — 0.15 of 2.55. Five minutes is 0.35% of 24 hours, and that
ratio dominates.

> 🧠 **This is the key structural insight of the lesson, and it sets up the next section:**
> **amp-hours are dominated by the long, quiet load. Instantaneous current is dominated by the
> short, loud one.** These are different questions with different governing terms, and the same
> load list answers them differently.

---

## Derivation 2 — Power supply sizing

The supply must deliver current at the moment of maximum demand.

```
   ┌────────────────────────────────────────────────────────┐
   │   I_design      =  max( I_standby , I_alarm )          │
   │   I_recommended =  I_design × (1 + headroom)           │
   └────────────────────────────────────────────────────────┘

   headroom = 0.25 by default
```

### 🧮 Worked example 7.3 — the test case

10 locks at 0.25 A standby, 0.50 A in alarm:

```
   I_standby =  10 × 0.25  =  2.50 A
   I_alarm   =  10 × 0.50  =  5.00 A

   I_design  =  max(2.50, 5.00)  =  5.00 A
   Recommended = 5.00 × 1.25     =  6.25 A
```

This is `test_power_supply_sizing_uses_worst_case`.

### ⚠️ Two things this number does not include

**1. Battery charging current.** A supply that is simultaneously running the load *and* recharging
a depleted battery is doing both jobs at once. Charging current adds to load current and it comes
from the supply's datasheet. `[MFR][VERIFY]`

**2. The peak-vs-continuous rating trap.** A supply advertised as "10 A" is frequently 10 A
**peak** with a lower continuous rating, and that rating often assumes it is not charging a
battery. **Read the datasheet, not the model number.**

---

## The pair everyone reverses

```
   ┌──────────────────────────────────────────────────────────────┐
   │   POWER SUPPLY  is governed by  PEAK current                 │
   │   BATTERY       is governed by  STANDBY current              │
   └──────────────────────────────────────────────────────────────┘
```

**Why:** the supply must source current *instantaneously* at the worst moment. The battery must
supply *energy over time*, and a load that lasts 300 ms contributes essentially nothing to
amp-hours no matter how large it is.

### 🧮 Worked example 7.4 — the same load list, both answers

The 12-opening floor from
[`../35_Doors_and_Hardware/03_locking_hardware_families.md`](../35_Doors_and_Hardware/03_locking_hardware_families.md):
8 electrified locksets at 0.30 A, 3 electric strikes at 0.25 A, 1 ELR exit device at 0.30 A
standby / 3.00 A peak.

```
   I_standby = 2.40 + 0.75 + 0.30 = 3.45 A       ← battery is sized on THIS
   I_peak    = 2.40 + 0.75 + 3.00 = 6.15 A       ← supply is sized on THIS

   Supply:   6.15 × 1.25              =  7.69 A
   Battery:  3.45 × 4 × 1.5625        = 21.56 Ah   (4-hour standby)
```

**The ELR device is 49% of the supply requirement and about 4% of the battery requirement.** One
device, two completely different levels of importance, depending on which question you are asking.

> ⚠️ **Getting these backwards is the most common sizing error in low-voltage design**, and both
> directions fail badly:
>
> - **Supply sized on standby (3.45 A):** the latch does not retract when the ELR fires. The door
>   does not open. Intermittently, because it depends on what else is drawing at that instant.
> - **Battery sized on peak (6.15 A):** you buy a 38 Ah battery instead of a 26 Ah one. Wasteful,
>   physically larger, and it may not fit the enclosure — but nothing breaks.
>
> **One error costs money, the other costs a door.** Know which is which.

---

## Derivation 3 — Runtime

The inverse question: given a battery you already have, how long does it last?

```
   ┌──────────────────────────────────────────────────┐
   │   H  =  Ah × usable_fraction / I                 │
   │                                                   │
   │   usable_fraction = 0.8                          │
   └──────────────────────────────────────────────────┘
```

**The 0.8 reflects that you should not discharge a lead-acid battery to zero.** Doing so damages
the cells and sharply shortens service life, so only about 80% of nameplate capacity is usable in
practice.

### 🧮 Worked example 7.5 — the test case

A 12 Ah battery on a 2 A load:

```
   H = 12 × 0.8 / 2.0 = 4.8 hours
```

This is `test_runtime_uses_usable_fraction`. **Note the naive answer is 6 hours** — the usable
fraction removes 1.2 hours, which is the difference between meeting a 5-hour requirement and not.

**This is a first-order estimate only.** Real runtime depends on discharge rate, temperature, and
battery age — the same effects the 1.25 derate compensates for when sizing. **Runtime and sizing
are not exact inverses of each other**, and they shouldn't be: sizing is conservative (buy more),
runtime is realistic (expect less). Both err on the safe side of their respective questions.

---

## Assumptions and limits

| Assumption | Reality |
|---|---|
| Lead-acid chemistry | The 1.25 derate and 0.8 usable fraction are lead-acid conventions. Li-ion behaves differently. `[VERIFY]` |
| Loads are constant | Real loads vary with occupancy, temperature, and time of day |
| The standby duration is an engineering choice | **It is frequently code.** `[CODE][VERIFY]` |
| One battery, one supply | Distributed supplies change the arithmetic and improve the failure domain |
| Charging current is somebody else's problem | It is additive and it is yours |
| Temperature is nominal | Cold reduces capacity; a battery in an unheated space delivers less |
| Simultaneous peaks | Sizing assumes all peak loads can coincide. Justify any assumption that they can't — "they probably won't" is not a justification; shift change and drills exist. |

---

## Common mistakes

⚠️ **Sizing the supply on standby current.** Doors fail to unlock, intermittently.

⚠️ **Sizing the battery on peak current.** Wasteful; may not fit.

⚠️ **Adding the derate and aging factors instead of multiplying.** Under-sizes by 4.2%.

⚠️ **Treating the standby duration as an engineering choice.** It is often code. `[CODE][VERIFY]`

⚠️ **Omitting battery charging current from the supply sizing.**

⚠️ **Reading a supply's peak rating as its continuous rating.**

⚠️ **Using nameplate capacity for runtime** instead of the usable fraction.

⚠️ **Sizing a battery to exactly meet requirement on day one.** It fails in year two, silently.

⚠️ **Assuming multiple peak loads cannot coincide** without demonstrating it.

---

## Junior vs. Senior

**Junior:** computes Ah from a load list with both correction factors; sizes a supply on peak
current; knows the usable fraction; knows the standby duration comes from somewhere else.

**Senior:** states which current governs which component and why, out loud, because the reversal is
so common; confirms the required standby duration against the adopted standard and the AHJ before
sizing anything; adds charging current and checks continuous vs. peak ratings on the datasheet;
considers distributing supplies rather than centralizing them, for both voltage drop (lesson 06)
and failure domain; and tells the owner what is true after the battery is exhausted — module 35
lesson 04's failure mode 2, which nobody asks about.

---

## Problem set

**P7.1** A floor has 14 card readers at 0.09 A, 14 electrified locksets at 0.30 A, 2 door
controllers at 0.55 A, and 14 REX sensors at 0.03 A. All 24 VDC, all continuous, no alarm-state
loads.
- (a) Compute the total standby current.
- (b) Size the power supply at 25% headroom.
- (c) Size the battery for 4-hour standby.
- (d) Size it for 8-hour standby. What is the relationship, and why is it exactly that?

**P7.2** Take P7.1's system and add one ELR exit device: 0.30 A standby, 3.5 A peak.
- (a) Recompute the supply requirement.
- (b) Recompute the 4-hour battery requirement.
- (c) State the percentage change in each and explain the asymmetry in one sentence.

**P7.3** A 40 Ah battery is installed on P7.1's system.
- (a) Compute the realistic runtime.
- (b) Compute the naive runtime using nameplate capacity.
- (c) The specification requires 4 hours. Does it pass? Would it pass in year three?

**P7.4** Show that multiplying the derate and aging factors is correct and adding them is not, by
working through what each factor physically represents. Compute the difference for a 30 Ah raw
requirement.

**P7.5** A supply datasheet says: "Output: 24 VDC, 10 A peak / 6 A continuous. Battery charging:
up to 1.5 A." Your load list needs 6.15 A design current. Does this supply work? Show every
consideration.

**P7.6** Explain, in under 130 words to a colleague, why the ELR exit device dominates the power
supply sizing and barely affects the battery sizing.

**P7.7** 🧮 A system draws 4.2 A standby. Code requires 4 hours of standby. Available battery
sizes are 7, 12, 18, 26, 40, and 55 Ah, and batteries can be paralleled.
- (a) Compute the requirement.
- (b) What do you specify?
- (c) The enclosure fits two 18 Ah batteries maximum. What are your options?

**P7.8** `test_battery_requires_loads` asserts that an empty load list raises rather than returning
zero. Argue for that choice, then name two other functions in `psec` where returning a plausible
value for degenerate input would be more dangerous than raising.

> Answers: [`_solutions/07_battery_ups_solutions.md`](_solutions/07_battery_ups_solutions.md)

---

## Retrieval check

1. Write the amp-hour formula including the alarm component.
2. What does the 1.25 discharge derate compensate for? The 1.25 aging factor?
3. Why are they multiplied rather than added?
4. Which current governs the power supply? Which governs the battery? Why?
5. Which of those two errors costs money and which costs a door?
6. Write the runtime formula and explain the 0.8.
7. Name two things a supply-sizing figure does not include.
8. Where does the required standby duration come from?

---

## References

- NFPA 72 — fire alarm secondary power requirements. `[STANDARD][VERIFY]`
- UL 294 — Access Control System Units, including standby requirements. `[STANDARD][VERIFY]`
- [`../28_Calculators/psec/power.py`](../28_Calculators/psec/power.py) — the implementation.
- [`../28_Calculators/tests/test_psec.py`](../28_Calculators/tests/test_psec.py) — `TestPower`.
- Battery manufacturer data — capacity at rate, temperature curves, service life. `[MFR]`
- [`../35_Doors_and_Hardware/04_fail_safe_vs_fail_secure.md`](../35_Doors_and_Hardware/04_fail_safe_vs_fail_secure.md)
  — what is true after the battery is exhausted, and why it is the owner's decision.
- [`../34_Electrical_Power/`](../34_Electrical_Power/) — power systems in depth *(not yet
  written)*.

**Next:** [08 — Adversary Path and Timely Detection](08_adversary_path.md)
