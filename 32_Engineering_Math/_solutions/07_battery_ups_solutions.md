# Solutions — 07 Battery and Power Supply Sizing

---

## P7.1 — Base system

**(a) Total standby current**
```
   14 readers    × 0.09  =  1.26 A
   14 locksets   × 0.30  =  4.20 A
    2 controllers× 0.55  =  1.10 A
   14 REX        × 0.03  =  0.42 A
                            ──────
                            6.98 A
```

**(b) Power supply at 25% headroom**

No alarm-state loads, so `I_peak = I_standby = 6.98 A`.
```
   6.98 × 1.25 = 8.73 A     →  specify ≥ 8.73 A CONTINUOUS
```

**(c) 4-hour battery**
```
   Ah_raw      = 6.98 × 4              =  27.92 Ah
   Ah_required = 27.92 × 1.25 × 1.25   =  43.63 Ah
```

**(d) 8-hour battery**
```
   Ah_raw      = 6.98 × 8              =  55.84 Ah
   Ah_required = 55.84 × 1.5625        =  87.25 Ah
```

**The relationship is exactly 2×**, because `Ah = I × H` is **linear in duration** and both
correction factors are constant multipliers that don't depend on H.

> 🧠 **Why this is worth noticing:** doubling the standby requirement doubles the battery, exactly,
> with no economies of scale. So when someone asks "what would 8 hours cost instead of 4?", the
> answer is "twice the battery" — instantly, no recalculation. It also means that if the standby
> duration is a *code* requirement rather than a preference, there is no clever way to shave it.

---

## P7.2 — Adding one ELR exit device

**(a) Supply**
```
   I_standby = 6.98 + 0.30           =  7.28 A
   I_peak    = 6.98 + 3.50           = 10.48 A
   I_design  = max(7.28, 10.48)      = 10.48 A
   Supply    = 10.48 × 1.25          = 13.10 A
```

**(b) 4-hour battery**
```
   Ah_raw      = 7.28 × 4            = 29.12 Ah
   Ah_required = 29.12 × 1.5625      = 45.50 Ah
```

**(c) Percentage change**

| | Before | After | Change |
|---|---|---|---|
| Supply | 8.73 A | 13.10 A | **+50.1%** |
| Battery | 43.63 Ah | 45.50 Ah | **+4.3%** |

**The asymmetry in one sentence:**

> One device added half again to the power supply requirement and 4% to the battery, because the
> supply must source its 3.5 A peak instantaneously while the battery only ever sees its 0.30 A
> standby draw integrated over four hours.

**The design consequence, which is the real point:** adding a single exit device pushed the supply
from ~9 A to ~13 A. That is very likely a different, larger, more expensive supply — possibly a
different enclosure and a different branch circuit. **One device, one line on a hardware set, a
step change in the power infrastructure.** This is why lesson 05 of module 35 recommends
electrified trim over electric latch retraction unless a requirement specifically demands it.

---

## P7.3 — 40 Ah battery on the P7.1 system

**(a) Realistic runtime**
```
   H = 40 × 0.8 / 6.98 = 4.58 hours
```

**(b) Naive runtime (nameplate)**
```
   H = 40 / 6.98 = 5.73 hours
```

**The usable fraction removes 1.15 hours — 20% of the answer.**

**(c) Does it pass 4 hours?**

**On day one, yes** — 4.58 hours against a 4-hour requirement, a 15% margin.

**In year three, probably not.** The aging factor exists precisely because capacity falls over
service life. At the 1.25 aging factor's implied end-of-life capacity (80% of nameplate):
```
   H = 40 × 0.80 (aging) × 0.8 (usable) / 6.98 = 3.67 hours     ❌
```

**It fails the requirement before the battery reaches the end of its nominal service life.**

**And this is exactly why sizing said 43.63 Ah.** The 40 Ah battery satisfies the naive
calculation (27.92 Ah raw), satisfies the day-one runtime check, and **fails the requirement in
service** — which is the failure the two correction factors exist to prevent. The correctly-sized
battery here is the next standard size up: **55 Ah**.

> ⚠️ **Note how this failure presents:** it is silent. Nobody load-tests a standby battery. The
> system passes commissioning, passes its first annual inspection by inspection rather than test,
> and then delivers 3.7 hours during an outage that lasted five. **If you specify the battery, put
> a periodic load test in the O&M handover** — the same posture module 35 takes toward every other
> recurring obligation.

---

## P7.4 — Multiply, don't add

**What each factor physically represents:**

- **Aging (1.25):** at end of service life the battery holds roughly **80%** of its nameplate
  capacity. `1/0.8 = 1.25`.
- **Discharge derate (1.25):** under a real discharge rate and temperature, and stopping before
  full depletion, you can extract roughly **80%** of whatever capacity the battery currently
  holds. `1/0.8 = 1.25`.

**The two effects compose multiplicatively because the second acts on the output of the first.**
An aged battery holds 80% of nameplate; a fast, cold, partial discharge extracts 80% **of that
80%**:

```
   Usable at end of life  =  0.80 × 0.80  =  0.64  (64% of nameplate)

   Required nameplate     =  Ah_raw / 0.64  =  Ah_raw × 1.5625     ✅
```

**Adding treats them as independent subtractions from the same base**, which would mean the aged
battery loses 20% of nameplate and the discharge loses another 20% *of nameplate*:

```
   Wrong model:  1 − 0.20 − 0.20 = 0.60  →  factor 1/0.6 = 1.667?
```

— except that isn't what "adding the factors" produces either. The common error is
`1 + 0.25 + 0.25 = 1.50`, which is neither model; it just adds the two 25% uplifts.

**Difference for a 30 Ah raw requirement:**

| Method | Factor | Result |
|---|---|---|
| Multiplied (correct) | 1.5625 | **46.875 Ah** |
| Added (wrong) | 1.5000 | **45.000 Ah** |
| Shortfall | | **1.875 Ah — 4.2%** |

**4.2% is small, and it is small in the wrong direction.** It pushes a design toward the next
standard size *down*, and standard battery sizes are spaced 30–50% apart — so a 4.2% arithmetic
error can easily be the difference between specifying 55 Ah and specifying 40 Ah, which is a 27%
real shortfall.

> 🧠 **The general habit: when correction factors compose, ask whether each acts on the original
> quantity or on the output of the previous one.** Sequential proportional effects multiply.
> Independent additive allowances add. Getting this wrong is usually a small percentage and
> occasionally a whole size class.

---

## P7.5 — Does the supply work?

**Datasheet:** 24 VDC, **10 A peak / 6 A continuous**, battery charging **up to 1.5 A**.
**Load:** 6.15 A design current.

**Consideration 1 — Which rating applies?**
The load is continuous, so the **6 A continuous** rating is the relevant one, not the 10 A peak.
**6.15 A > 6 A. The supply is already over its continuous rating on load alone.**

**Consideration 2 — Charging current is additive.**
While recharging a depleted battery the supply must deliver load **plus** charging:
```
   6.15 + 1.5 = 7.65 A     against a 6 A continuous rating
```
**28% over.**

**Consideration 3 — Headroom.**
The 6.15 A figure is the *design* current before the 25% headroom that lesson 07 recommends. With
headroom the target is 7.69 A, and with charging, 9.19 A.

**Consideration 4 — When does the worst case occur?**
Immediately after a power restoration: the battery is depleted and charging hard, the load is
fully active, and any peak loads (an ELR firing as someone badges in) land on top. **The worst
case is the moment the system recovers**, which is also the moment nobody is watching.

**Consideration 5 — What is the 10 A peak rating for?**
Short transients. It does not license sustained operation above 6 A, and relying on it for the
charging period — which lasts hours, not milliseconds — misreads the datasheet.

**Verdict: No. This supply does not work.**

Specify a supply with **≥ 9.2 A continuous** (7.69 A recommended load + 1.5 A charging), or split
the load across two supplies — which also improves the failure domain and shortens the runs
(lesson 06).

> ⚠️ **The trap this problem is built around:** "10 A supply, 6.15 A load" looks like 39% headroom.
> The real comparison is 6 A against 7.65 A, which is a 28% deficit. **Two numbers on the same
> datasheet, and the model number quotes the one that flatters.**

---

## P7.6 — Explaining the asymmetry

Model answer (121 words):

> They're answers to two different questions.
>
> The power supply has to deliver current *at the instant of maximum demand*. When that exit
> device fires, it wants 3.5 amps right then, on top of everything else — so the supply has to be
> able to source it or the latch doesn't pull. That's an instantaneous question.
>
> The battery is an energy question: amp-hours, over four hours. The exit device draws its 3.5
> amps for a few hundred milliseconds at a time. Integrated over four hours that's almost nothing
> — its standby draw of 0.3 amps is what the battery actually sees.
>
> So: **supply sized on peak, battery sized on standby.** Same load list, opposite governing
> numbers. Getting them backwards is the classic error here.

**What makes it work:** it names the two questions before the two numbers, so the asymmetry reads
as inevitable rather than as a rule to memorize. The closing line is the thing worth remembering.

---

## P7.7 — 🧮 4.2 A standby, 4-hour code requirement

**(a) Requirement**
```
   Ah_raw      = 4.2 × 4            = 16.8 Ah
   Ah_required = 16.8 × 1.5625      = 26.25 Ah
```

**(b) What to specify**

Available sizes: 7, 12, 18, 26, 40, 55 Ah.

**26 Ah is 0.25 Ah short.** That is 0.95% — trivially inside the noise of every factor in this
calculation, and it is still *short of the computed requirement*.

**Specify 40 Ah**, or two 18 Ah in parallel (36 Ah).

**Do not specify 26 Ah.** The requirement is code-driven, the calculation already assumes nominal
temperature, and "0.25 Ah short" is not a defensible position in front of an AHJ or after an
incident. **When a computed requirement lands just above a standard size, you go up.** The whole
point of the correction factors is that the margin is not decorative.

**(c) The enclosure fits two 18 Ah batteries maximum**

`2 × 18 = 36 Ah ≥ 26.25 Ah` ✅ — **this works, and it's the answer.**

```
   Runtime check: 36 × 0.8 / 4.2 = 6.86 hours     comfortably over 4
```

**If the enclosure had not accommodated it**, the options in order:

1. **Reduce the standby load.** 4.2 A for an access control floor is high — check for anything
   that could be fail-secure rather than fail-safe (a fail-safe mag lock draws continuously; a
   fail-secure lockset draws only when actuated). This is often available and free, and it is the
   option nobody checks.
2. **Second enclosure with a second supply and battery**, splitting the load. Also shortens runs
   (lesson 06) and improves the failure domain.
3. **Larger enclosure.** Usually a coordination and space problem rather than a cost problem.
4. **Different chemistry** — Li-ion offers far more capacity per unit volume, at higher cost, with
   different derating and different code treatment. `[CODE][VERIFY]` Verify AHJ acceptance before
   proposing it.

> 🧠 **Option 1 is the one to lead with.** A load-reduction review is free, it frequently finds
> 15–20% on an access control floor, and it improves the design on other axes at the same time.
> Reaching for a bigger box first is the reflex; reaching for a smaller load is the engineering.

---

## P7.8 — Raising on degenerate input

**The argument for raising on an empty load list:**

`battery_ah_required([], 4.0)` has no meaningful answer. Returning **0 Ah** would be
*arithmetically* defensible — an empty sum is zero — and **operationally catastrophic**, because
"0 Ah required" reads as a valid design conclusion. A caller who assembled their load list from a
device register that silently returned nothing (a bad filter, a typo'd zone name, an empty CSV
column) gets a number that says "no battery needed" and no indication anything went wrong.

**The asymmetry that decides it:** an exception costs a developer thirty seconds. A plausible-
looking zero costs a building its standby power, and the error is invisible because zero is a
number, not an error message.

**Two other functions where a plausible value for degenerate input would be more dangerous:**

**1. `max_run_length_ft` with an impossible voltage target.**
`test_max_run_rejects_impossible_target` asks for a 12.0 V minimum from a 12.0 V supply — zero
allowable drop. The arithmetic gives `L_max = 0`, or negative for a target above the supply.
Returning 0 would mean "you can run zero feet," which a caller might reasonably interpret as a
boundary condition rather than an error, and returning a **negative** length is meaningless.
Raising forces the caller to notice their voltage budget is impossible before they design around
it. **This one is already correct in the module.**

**2. `retention_days_achievable` with an empty group list, or `raid_raw_capacity_tb` with an
invalid disk count.**
- Empty groups gives a division by zero, or — if guarded by returning 0 — "your storage lasts zero
  days," which looks like a catastrophic finding rather than a bad input, and would send someone
  chasing a storage problem that doesn't exist.
- `raid_raw_capacity_tb(100, "raid5", 2)` is the more interesting case: RAID 5 with 2 disks is
  arithmetically expressible (`efficiency = 1/2`) and **physically meaningless** — RAID 5 requires
  at least 3 disks. Silently returning 200 TB would produce a valid-looking number for a
  configuration that cannot be built. **The module already raises on all three of these**
  (`test_raid_disk_count_validation`), which is the correct call.

> 🧠 **The general principle: a function should raise when the input has no meaningful answer, and
> return when it has one — even an unwelcome one.** The dangerous middle ground is returning a
> value that is arithmetically derivable but semantically void, because the caller has no way to
> distinguish it from a real result.
>
> Note that `psec.pps.compare_interventions` handles exactly this problem well and *without*
> raising: when the required detection point comes out negative, it doesn't emit "move detection
> to −1150 s" — it says **NOT ACHIEVABLE** and redirects the caller to a different lever. That is
> the third option, and it is often the best one: **return a result that names the impossibility
> instead of encoding it in a number.** See lesson 08.
