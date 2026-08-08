# Solutions — 06 Voltage Drop and Conductor Selection

---

## P6.1 — The derivation

```
   1.  V = I · R                     Ohm's law: voltage lost = current × resistance

   2.  R = ρ · L / A                 Resistance of a conductor: rises with length,
                                     falls with cross-sectional area

   3.  R = K · L / CM                Same relation in American wire units. Area is in
                                     CIRCULAR MILS (the area of a circle 1 mil across,
                                     so CM = d² in mils — no π), and K is resistivity
                                     in Ω·cmil/ft, which absorbs the π and the unit
                                     conversions. K = 12.9 for copper at ~75 °C.

   4.  R_circuit = K · (2L) / CM     THE ROUND TRIP. Current leaves on one conductor
                                     and returns on the other, so the circuit contains
                                     2L feet of copper. L is the ONE-WAY length as
                                     measured on a plan.

   5.  Vd = I · R_circuit
          = 2 · K · I · L / CM       Substituting 4 into 1.
```

**What each substitution does:** step 2 turns an abstract resistance into a property of a physical
conductor. Step 3 changes the unit system so the numbers are the ones on a wire spool and the
geometry constant disappears. Step 4 accounts for the fact that a circuit is a loop, not a
one-way trip.

---

## P6.2 — Drop and load voltage, 24.0 V supply

| | Current | Length | AWG | Drop | V at load |
|---|---|---|---|---|---|
| (a) | 0.75 A | 150 ft | 18 | **1.7873 V** | **22.213 V** |
| (b) | 0.75 A | 150 ft | 14 | **0.7067 V** | **23.293 V** |
| (c) | 2.5 A | 150 ft | 18 | **5.9575 V** | **18.043 V** |

Working for (a):
```
   Vd = 2 × 12.9 × 0.75 × 150 / 1624 = 2902.5 / 1624 = 1.7873 V
```

**(d) The ratios, explained without recomputing**

```
   c / a  =  5.9575 / 1.7873  =  3.3333  =  2.5 / 0.75
```
**Exactly the current ratio.** `Vd ∝ I` with everything else held constant. Tripling the current
triples the drop, and nothing else in the formula moved.

```
   a / b  =  1.7873 / 0.7067  =  2.5289  =  4107 / 1624
```
**Exactly the circular-mil ratio.** `Vd ∝ 1/CM`. Going from 18 to 14 AWG multiplies the copper by
2.529, so it divides the drop by 2.529.

Note this is close to the "double every 3 AWG" rule — 18 to 14 is four steps, which the rule
predicts as `2^(4/3) = 2.52`. The rule is accurate to better than 1% here.

> 🧠 **The reason this sub-question exists:** once you can read a ratio off the formula, you stop
> recomputing. "We're going from 18 to 14" is a 2.5× improvement, instantly, in a meeting, without
> a calculator.

---

## P6.3 — 1.2 A device, 21.5 V minimum, 24.0 V supply

**(a) Maximum run length**

Allowable drop = 24.0 − 21.5 = **2.5 V**

```
   L_max = Vd_allowed × CM / (2 · K · I)

   18 AWG:  2.5 × 1624 / (2 × 12.9 × 1.2)  =  4060 / 30.96  =  131.14 ft
   14 AWG:  2.5 × 4107 / 30.96             = 10267.5 / 30.96 =  331.64 ft
```

**(b) Smallest conductor for a 240 ft routed run**

| AWG | V at load | Verdict |
|---|---|---|
| 18 | 19.425 V | ❌ |
| 16 | 21.123 V | ❌ (short by 0.38 V) |
| **14** | **22.191 V** | ✅ |
| 12 | 22.862 V | ✅ (more than needed) |

**14 AWG.**

**(c) The installer's 16 AWG**

```
   V at load = 21.123 V   against a 21.5 V requirement   →  short by 0.377 V
```

**No — and here is how to say it without a fight:**

> That's 21.12 volts at the device and it needs 21.5. It'll probably work on the bench and on a
> cool morning, and it'll be the door that "acts up sometimes" for the next ten years — because
> copper resistance rises with temperature, so it gets worse exactly when the building is warm and
> busy.
>
> It's 0.4 volts short, which sounds like nothing and is the difference between a circuit with
> margin and a circuit with none. Can we get 14 on site tomorrow?

**Why this matters more than the 0.38 V suggests:** the calculation already assumes 75 °C copper
and **zero** connection resistance. Every termination adds a little. A design that is 0.38 V short
on paper is further short in the building, and the failure will be intermittent —
which, per module 35 lesson 03, will be misdiagnosed as software for months.

---

## P6.4 — 🧮 Multi-segment: 1.8 A, 180 ft of 16 AWG + 8 ft of 24 AWG

**(a) Segment ratios**
```
   Home run:  L/CM = 180 / 2583 = 0.069686
   Transfer:  L/CM =   8 /  404 = 0.019802
                                  ─────────
   Sum                          = 0.089488
```

**(b) Total drop and load voltage**
```
   Vd = 2 × 12.9 × 1.8 × 0.089488 = 4.1558 V

   V_load = 24.0 − 4.156 = 19.844 V     ❌  (needs 21.0 — short by 1.16 V)
```

**(c) Share of the total**

| Segment | Drop | Share |
|---|---|---|
| Home run, 180 ft / 16 AWG | 3.2362 V | **77.9%** |
| Transfer, 8 ft / 24 AWG | 0.9196 V | **22.1%** |

**(d) One change: home run to 14 AWG, or transfer to 18 AWG?**

| Option | New sum of L/CM | Total drop | V at load | Verdict |
|---|---|---|---|---|
| **A — home run → 14 AWG** | 180/4107 + 8/404 = 0.063632 | 2.955 V | **21.045 V** | ✅ passes, just |
| **B — transfer → 18 AWG** | 180/2583 + 8/1624 = 0.074613 | 3.465 V | **20.535 V** | ❌ still fails |

**Do option A — upsize the home run.**

**And note that this is the opposite conclusion to module 35's example**, which is the point of the
problem. There, six feet of 24 AWG contributed 33% of the drop and changing the transfer was the
efficient fix. Here the same transfer contributes only 22%, because the home run is 16 AWG rather
than 12 — a smaller conductor, so it dominates.

> 🧠 **There is no rule of thumb here, and that is the lesson.** "Always check the transfer" and
> "always upsize the home run" are both wrong. **Compute `L/CM` per segment, look at the shares,
> and spend where the share is.** The ratio table takes thirty seconds and it tells you which
> change is worth making — which a total never does.
>
> Also worth noticing: option A passes by 0.045 V. That is not a design, it is a coin flip against
> connection resistance and temperature. The honest answer to (d) is "A, **and I'd want the
> transfer upsized too**, or the supply moved" — see P6.5, which forces exactly that.

---

## P6.5 — The same circuit at 5.5 A inrush

```
   Vd = 2 × 12.9 × 5.5 × 0.089488 = 12.698 V

   V_load = 24.0 − 12.698 = 11.302 V     ❌❌
```

**11.3 V on a 24 V circuit. The device will not actuate.**

**What changes: everything.** At 1.8 A the circuit was 1.16 V short and one conductor change away
from working. At 5.5 A it is **9.7 V short** and no combination of conductor changes rescues it:

| Configuration | V at load |
|---|---|
| As designed (16 AWG home, 24 AWG transfer) | 11.30 V ❌ |
| Both upsized (14 AWG home, 18 AWG transfer) | 17.08 V ❌ |
| Aggressive (12 AWG home, 18 AWG transfer) | 19.39 V ❌ |

**What I would do about it — in order:**

**1. Verify the inrush figure and its duration with the manufacturer.** 5.5 A for 300 ms is a real
transient, but some devices tolerate a substantial sag during it as long as the voltage recovers.
The device's **minimum operating voltage during actuation** is the number that decides this, and
it is not always the same as its steady-state minimum. `[MFR][VERIFY]` This question is free and
it sometimes ends the problem.

**2. Relocate the power supply.** A local supply 30 ft away on 14 AWG, with an 18 AWG transfer:
```
   2 × 12.9 × 5.5 × (30/4107 + 8/1624) = 1.735 V   →   22.26 V   ✅
```
**Comfortable, with margin, using smaller conductors than any of the failed options.** It also
shrinks the failure domain — one supply failure now affects a few openings rather than a floor.
This is almost always the right answer when inrush is the binding constraint.

**3. Change the device.** Per module 35 lesson 03: **electrified trim instead of electric latch
retraction** draws a fraction of the current and deletes the problem. If three rounds of conductor
sizing haven't fixed it, the device selection is what's wrong.

> 🧠 **The meta-lesson, and it is the one worth carrying:** when the arithmetic gets ugly, stop
> iterating on the conductor. Two design changes — *where the power comes from* and *what the
> device is* — dominate anything you can do with copper, and both are usually cheaper.

---

## P6.6 — To an installer who wants a bigger power supply

Model answer (114 words):

> A bigger supply won't touch it, and here's why.
>
> Voltage drop is current times the resistance of the wire. The supply sets the voltage at its
> end; the wire decides how much survives to the door. A supply rated for more *amps* at the same
> *volts* delivers exactly the same voltage down there. It isn't running out of current — the wire
> is eating the volts.
>
> Three things actually fix it: bigger wire, a shorter run, or a device that draws less.
>
> Cheapest here is usually a shorter run — put a small supply in the closet near the door instead
> of feeding it from the panel. Costs less than the copper and it means one supply failure doesn't
> take out the floor.

**What makes it work:** one sentence of mechanism, one memorable line ("the wire is eating the
volts"), then straight to what *does* work — with the cheapest option named and a second benefit
attached so it doesn't sound like a consolation prize.

---

## P6.7 — Powering a strike over spare Cat6 pairs

```
   0.4 A, 210 ft, 23 AWG (509.5 CM), 12.0 V supply, 10.8 V minimum

   Vd = 2 × 12.9 × 0.4 × 210 / 509.5  =  2167.2 / 509.5  =  4.254 V

   V_load = 12.0 − 4.254 = 7.746 V        ❌  (needs 10.8 — short by 3.05 V)

   Maximum run on 23 AWG for this load:  1.2 × 509.5 / (2 × 12.9 × 0.4) = 59.2 ft
```

**The proposal exceeds its own limit by a factor of 3.5.**

**The response:**

> This won't work — it's not marginal, it's about three and a half times over.
>
> At 0.4 A over 210 ft of 23 AWG the drop is 4.25 V, so the strike sees **7.7 V** against a 10.8 V
> minimum. The maximum run for this load on Cat6 conductor is about **59 ft**.
>
> The problem is the conductor size. 23 AWG has roughly an eighth the copper of 18 AWG, and
> voltage drop scales inversely with copper, so it eats the budget very quickly. A 12 V supply
> makes it worse — there's only 1.2 V of headroom to spend before the device drops out, where a
> 24 V circuit would have had 13.
>
> Options, cheapest first: **pull a dedicated 18 AWG pair** for the lock power (18 AWG at 210 ft
> and 0.4 A drops 1.33 V — comfortable); or **put a local supply near the door**; or **use a 24 V
> device and supply**, which multiplies the available headroom by an order of magnitude.
>
> Worth adding: even if this had computed as marginal, running lock power over spare pairs in a
> data cable is worth avoiding — it couples a switching inductive load into the same jacket as the
> network, and it makes the cable's purpose ambiguous to whoever troubleshoots it in five years.

**Note the second-order point.** The arithmetic settles it, but the *practice* argument matters
too and a good response includes it — the design is bad even at 50 ft.

---

## P6.8 — Why the "every smaller gauge fails" assertion is necessary

**The test:**
```python
awg = power.smallest_awg_for_run(24.0, 1.0, 300, 21.6)
self.assertGreaterEqual(power.voltage_at_load_v(24.0, 1.0, 300, awg), 21.6)   # it works
smaller = [a for a in AWG_CIRCULAR_MILS if CM[a] < CM[awg]]
for a in smaller:
    self.assertLess(power.voltage_at_load_v(24.0, 1.0, 300, a), 21.6)          # nothing smaller works
```

**Why the second assertion is necessary:** the function's contract has two halves — *sufficient*
("this conductor works") and *minimal* ("no cheaper conductor does"). The first assertion only
tests sufficiency. **Minimality is the entire reason the function exists** — if you only needed a
conductor that works, you would specify 10 AWG everywhere and never call it.

**An incorrect implementation the first assertion alone would pass:**

```python
def smallest_awg_for_run(supply_v, current_a, length_ft, min_device_v, *, k=K_COPPER_75C):
    return "10"      # always returns the largest conductor in the table
```

This passes `assertGreaterEqual(voltage_at_load_v(...,"10"), 21.6)` — 10 AWG delivers 23.28 V,
comfortably over the threshold — while being useless and expensive. Every call would over-specify
copper, on every run, forever, and nothing in a sufficiency-only test would notice.

**Subtler wrong implementations it also catches:**

- **Iterating the table in dictionary order rather than by circular mils.** Python dicts preserve
  insertion order, and the table happens to be written largest-CM-last, so it works by accident.
  Reorder the literal and a sufficiency-only test still passes while the function starts returning
  whichever adequate gauge it hits first.
- **An off-by-one that skips the true smallest** — returning 14 when 16 would have worked.
  Sufficiency passes; the design costs more copper than it needs on every run.
- **A `>` instead of `>=` at the threshold**, which would reject a conductor landing exactly on the
  minimum and return the next size up.

> 🧠 **The general principle, and it generalizes past this function:** when a function's name
> contains a superlative — *smallest*, *cheapest*, *fastest*, *first* — the test must assert the
> superlative, not just the property. Asserting "the answer satisfies the constraint" tests half
> the contract, and it is the half that a lazy implementation satisfies for free.
>
> This is the same failure class as lesson 04's binary-units defect, where
> `assertLess(binary, decimal)` tested a direction instead of a value. **Both are tests that
> constrain the answer to an infinite family rather than to a point.**
