# Answer Key — Quiz 32, Engineering Math

> For [`../quiz_32_engineering_math.md`](../quiz_32_engineering_math.md).
> **Write your answers before opening this.** Every numeric answer here was produced by running
> `psec` and transcribing it. If your hand calculation disagrees, find out which of you is wrong
> — that is worth more than the mark.

**52 points.** Part A 16 × 1, Part B 6 × 2, Part C 8 × 3.

---

## Part A — Derivations and concepts

**1.** *(1 pt)*

```
   AOV = 2 · arctan( sensor_dimension / (2 · f) )
```

From the **thin-lens pinhole model**: the sensor sits at the focal plane, the lens is a point, and
half the sensor dimension over the focal length is the tangent of the half-angle. Doubling gives
the full angle.

> Full marks needs both the formula and "pinhole / thin lens." Half marks for the formula alone.
> The model is what tells you when the formula stops being true — fisheye lenses use a different
> projection entirely and must not be modelled with it.

**2.** *(1 pt)*

```
   W = D · w / f      W scene width (ft), D distance (ft), w sensor width (mm), f focal (mm)
```

From **similar triangles**: the scene at distance `D` and the sensor at distance `f` subtend the
same angle, so `W/D = w/f`.

It is dimensionally sound because `w/f` is a **ratio of two lengths in the same unit** — it is
dimensionless. The millimetres cancel before the feet ever meet them. `W` inherits its unit
entirely from `D`.

**3.** *(1 pt)*

```
   f = D · w / W_required
```

A calculator gives you coverage from a lens you already chose. A designer starts from a coverage
requirement — "I must see this 30 ft doorway from that column" — and needs the lens. **The
requirement comes first and the hardware comes second**, so the inverse is the form you actually
type.

**4.** *(1 pt)* **Slant range** is the true optical path from the lens to the target, accounting
for the mount height above the target plane: `sqrt(D² + (h_mount − h_target)²)`.

Worst for **indoor cameras**, and more generally for any camera where mount height is a meaningful
fraction of target distance. A camera 12 ft up looking at a face 8 ft away has a slant range of
10.6 ft — 33% further than the floor distance. Ignoring it **overstates** PPF, because it computes
the scene width at a distance shorter than the light actually travels.

**5.** *(1 pt)*

```
   PPF = px / W                  and     PPF = px · f / (D · w)
```

The second is the first with `W = D·w/f` substituted in. Use it when you do not care about the
scene width itself.

**6.** *(1 pt)* **Illuminance** falls as `1/D²` — the inverse square law for light from a point
source.

Pixel density falls as `1/D` because it is a **linear** density: pixels per foot of a
one-dimensional scene width, and scene width grows linearly with distance. (Pixels per square foot
would fall as `1/D²`, but nobody specifies that.)

The bad decision it causes: assuming that doubling the distance quarters your usable resolution.
It halves it. That mistake makes people add cameras or reject viable mounting positions that would
have worked.

**7.** *(1 pt)* Resolution and focal length trade against each other **for range** — you can reach
the same `D_max` with more pixels or a longer lens.

They explicitly do **not** trade against each other for **coverage**. More pixels widen the range
at fixed coverage; a longer lens narrows coverage to buy range. Substituting one for the other
changes what the camera sees, not just how far.

**8.** *(1 pt)* `[STANDARD]` IEC 62676-4 defines DORI in pixels per metre (25 / 62.5 / 125 / 250).
`[VERIFY current edition]` The exact conversions are 7.62, 19.05, 38.10, 76.20 ppf. The table uses
8, 19, 38, 76 — **rounded to the values used in common practice**, so that a designer's numbers
match the numbers on a vendor datasheet and in a room full of people who all say "76 PPF."

Chasing 0.2 PPF of conversion precision on a figure that is itself a minimum under good conditions
is false precision. The rounding is documented so you can undo it, which is the point.

**9.** *(1 pt)*

1. **A measured stream from a pilot** of the actual camera in the actual scene. Nothing beats it.
2. **The camera manufacturer's datasheet** for the specific model, codec, and profile.
3. **A vendor bandwidth calculator** for that manufacturer's cameras.
4. **A generic reference table** like `TYPICAL_H264_MBPS`. `[PRACTICE]` A starting point, and the
   one you must caveat.

**10.** *(1 pt)* Two physical reasons frame-rate scaling is sub-linear:

1. **I-frames and container overhead do not scale** with frame rate. A fixed cost per GOP stays
   fixed.
2. **Inter-frame prediction gets less efficient** as frame rate falls, because successive frames
   differ more, so each P-frame carries more residual.

A documented modelling choice (`ratio^0.7`, `[PRACTICE]`) beats an undocumented one because it can
be **challenged, tested, and replaced**. An undocumented one gets inherited silently by everyone
downstream and is indistinguishable from a fact.

**11.** *(1 pt)* Storage accumulates over time, so it integrates the *average* — a camera that
records half the time fills half the disk. A network link must carry whatever arrives *right now*,
so it must survive the *peak*.

And the peaks **correlate**: a vehicle entering a yard triggers the gate camera, two fence cameras,
and a dock camera within seconds. The statistical smoothing you might hope for evaporates exactly
when you need it.

**12.** *(1 pt)* A duty cycle below 1.0 assumes the motion detection **fires on every event that
matters**. Motion recording that misses the event produces nothing, and poorly tuned motion
detection misses events routinely — while producing hours of footage of a flag, a shadow, or rain.

So the storage saving is real and the risk is real, and they are not the same person's problem.
Book it as a saving and you have quietly transferred a technical risk to the owner without telling
them. **Name it, quantify what it saves, and let them accept it.**

**13.** *(1 pt)*

```
   PSE power  =  what the switch port must SOURCE   ← budget against THIS
   PD power   =  what the device may DRAW           ← datasheets quote THIS
```

The difference is the **worst-case cable loss the standard allows**. `[STANDARD]` 802.3af 15.4 /
12.95 W, at 30.0 / 25.5 W, bt Type 3 60 / 51 W, Type 4 90 / 71.3 W. `[VERIFY current edition]`

Budget against **PSE**, because many switches allocate by the class the device negotiates, not by
what it draws.

**14.** *(1 pt)*

1. **Port count exceeded** — more devices than ports.
2. **Power budget exceeded** — total class allocation over the switch's PoE budget.
3. **Insufficient spare ports** against the growth policy — it fits, with no room to change.
4. **Budget tight** (over ~80% utilised) — it fits today and the next device fails.

They are **independent**. Adding ports does not add watts; adding watts does not add ports.

**15.** *(1 pt)*

```
   Step 1   Ohm's law                      V  = I · R
   Step 2   Conductor resistance           R  = K · L_total / CM
   Step 3   Round trip: L_total = 2·L      Vd = 2 · K · I · L / CM
```

**The factor of 2** is the round trip. Current leaves on one conductor and returns on the other,
and both have resistance. Forgetting it halves your answer and is the single most common error in
this calculation.

**A circular mil** is the area of a circle one thousandth of an inch in diameter — so area in
circular mils is simply `(diameter in mils)²`, with no π. It exists precisely to make this formula
arithmetic instead of geometry.

**16.** *(1 pt)* **Peak (alarm) current governs the power supply. Standby current governs the
battery.**

They differ because they answer different questions. The supply must deliver the worst
*instantaneous* demand without its output collapsing — a **power** question. The battery must
deliver *energy over time*, and the worst instant lasts seconds, so it contributes almost nothing
to amp-hours — an **energy** question. This is the most commonly reversed pair in low-voltage
design.

---

## Part B — Scenario

**17.** *(2 pts)* **How both are right:** bitrate at design time is an estimate built on assumed
scene content, motion, noise, lighting, codec implementation, and encoder tuning — none of which
anyone knows yet. A 2× spread between two vendors' calculators on the same camera is normal and
reflects genuine uncertainty, not an error in either tool. They are also likely using different
codec factors, different frame-rate models, and possibly decimal versus binary units.

**What goes in the proposal:** a **range**, with the point estimate inside it, plus the mechanism
for closing it. "We're sizing at 7.9 TB; the true figure depends on scene activity and could land
between roughly 5.5 and 12.6 TB, so we're specifying expansion bays and we'll measure real bitrate
in week one."

> 1 pt for explaining the uncertainty. 1 pt for the range **and** a commitment to measure. An
> answer that just picks one number, however well argued, does not get the second point.

**18.** *(2 pts)* **What you need to know:** the PoE **class** of the cameras they want to add
(indoor vs outdoor/heated is roughly 15.4 W vs 30 W), the switch's **PoE budget and current
draw**, whether it allocates **statically by class or dynamically** `[VERIFY per datasheet]`, and
their **spare-port policy**.

**The shape of the answer:** state the **binding** constraint in **cameras**, not watts. "You have
16 free ports but power for four more outdoor cameras. The fifth needs a new switch." Quoting the
port count alone is technically true and will cause someone to make a commitment you cannot keep.

**19.** *(2 pts)* **First hypothesis: voltage drop.** The device is receiving less than its minimum
operating voltage and the margin is marginal, not absent.

**Two measurements:** (a) voltage **at the lock**, measured *while it is energised*, not at the
power supply and not at rest — the drop only exists under load; (b) actual current draw at the
device, compared with the datasheet figure used to size the conductor.

**Why time-of-day dependent:** **copper resistance rises with temperature.** A conductor in a
ceiling plenum that is cool at 7 a.m. and warm by 3 p.m. has measurably higher resistance in the
afternoon, so the drop grows and a design sitting 0.1 V above the minimum crosses below it. This
is why `psec` uses `K = 12.9` at 75 °C rather than a 20 °C value — the warm-conductor figure is the
conservative one.

> Full marks requires the temperature reason. Naming voltage drop alone is 1 pt.

**20.** *(2 pts)* In eighteen months:

1. **The battery no longer holds its rated capacity.** Lead-acid loses capacity over service life.
   Addressed by the **aging factor** (1.25).
2. **It never delivered its rated capacity in the first place** at the actual discharge rate and
   temperature, and it should not be run to full discharge. Addressed by the **derate** (1.25).

They **multiply**, not add — 1.5625, not 1.5 — because they describe *independent* reductions:
aging removes a fraction of what remains after the discharge derate, not a fraction of the
original. Adding instead of multiplying under-sizes by **4.167%**.

`[CODE][VERIFY]` And the 4-hour requirement itself is not necessarily yours to choose — UL 294 and
NFPA 72 as adopted, plus the AHJ, may set it.

**21.** *(2 pts)* **Why it may buy nothing:** delay added **before the detection point** buys
nothing at all. The timeliness inequality is about `T_A = T_T − T_D`, the time remaining *after*
detection. Adding 600 s at the site perimeter, when detection happens at a door well inside it,
increases `T_T` and `T_D` by the same 600 s. `T_A` is unchanged. The verdict does not move.

**The condition under which it works:** the barrier must sit **after** the detection point on the
path. Put detection at the perimeter as well — or move the barrier inward past the existing
detection layer — and the same 600 s becomes fully effective.

> This is the single most common misapplication of the model. Full marks needs "delay before
> detection buys nothing" stated as the principle, not just as a fact about this case.

**22.** *(2 pts)* **Interpretation:** timeliness would require detecting the adversary **240
seconds before they begin**. No placement of detection anywhere on this path can succeed. Even
instantaneous detection at the property line leaves less time than the response needs. The
detection lever is **exhausted**, not merely expensive.

**What a good calculator returns:** an explicit `NOT ACHIEVABLE` verdict that says so in words,
names the arithmetic, and redirects to the levers that can still work — response time or
consequence reduction. `psec.compare_interventions` does exactly this when the cutoff is ≤ 0.

**Why:** "move detection to −240 s" is arithmetically true and operationally meaningless. A number
that cannot be acted on, presented as if it can, is worse than no answer — someone will try to
build it.

---

## Part C — Calculation

### 23 — Angle of view, scene width, pixel density *(3 pts)*

```
   AOV  =  2 · arctan( 5.37 / (2 × 6) )  =  2 · arctan(0.4475)  =  2 × 24.109°  =  48.22°

   W    =  40 × 5.37 / 6                 =  214.8 / 6            =  35.80 ft

   PPF  =  2688 / 35.80                                          =  75.08 px/ft
```

**Class: recognise** (38 ≤ 75.08 < 76).

> **The trap.** 75.08 is 0.92 PPF short of identify — **1.2% short**. It is not "basically
> identify." If the requirement is identification, this camera fails, and rounding it up in a
> design review is how a system gets built that cannot do the thing it was bought for.
>
> 1 pt AOV, 1 pt W, 1 pt PPF **with the correct class**. Naming "identify" loses the third point.

### 24 — Focal length from required coverage *(3 pts)*

```
   f  =  D · w / W  =  75 × 5.37 / 30  =  402.75 / 30  =  13.425 mm
```

Stocked sizes are 9, 12, 16 mm. **Specify 16 mm.**

**Why that direction:** rounding a computed focal length **down** widens the field of view beyond
the requirement and **reduces** pixel density — you fail the requirement you just computed. Check
both candidates:

```
   12 mm @ 75 ft  →  W = 33.56 ft   (30 ft required — too wide, misses coverage spec)
   16 mm @ 75 ft  →  W = 25.17 ft   (narrower than required — meets it with margin)
```

**Always round focal length up to the next stocked size**, then verify that the narrower field
still covers what you need. If it does not, you need a different mounting position or a second
camera — which is a real finding, not a rounding problem.

> 1 pt for 13.425 mm. 1 pt for choosing 16. 1 pt for the "round up, then re-verify coverage"
> reasoning. Choosing 12 mm because it is closer scores 1.

### 25 — Maximum range for a DORI class *(3 pts)*

```
   W_max  =  px / PPF_target  =  2688 / 38     =  70.74 ft
   D_max  =  W_max · f / w    =  70.74 × 4 / 5.37  =  52.69 ft
```

**52.69 ft** for recognise.

With an 8 MP camera (3840 px) on the same lens and sensor:

```
   D_max  =  52.69 × (3840 / 2688)  =  52.69 × 1.4286  =  75.27 ft
```

**Range scales linearly with pixel count**, because `D_max ∝ px · f`. A 43% increase in horizontal
pixels buys a 43% increase in range — **not** a 43% increase in area covered, and not a 43%
increase in anything at a fixed distance except pixel density.

> 1 pt for 52.69 ft, 1 pt for 75.27 ft, 1 pt for stating the linearity explicitly. A common wrong
> answer computes the megapixel ratio (8/4 = 2×) instead of the horizontal-pixel ratio; that scores
> zero on the third point because it misidentifies which quantity drives range.

### 26 — Storage and the decimal/binary gap *(3 pts)*

```
   6.0 Mbps × 3600 s/h × 18 h   =   388,800 megabits/day
                        ÷ 8     =    48,600 megabytes/day
                        ÷ 1000  =        48.6 GB/day        (decimal)

   × 45 days ÷ 1000             =         2.187 TB
```

In binary units:

```
   48,600 megabytes ÷ (2³⁰ / 10⁶)  =  48,600 / 1073.741824  =  45.262 GiB/day
   × 45 ÷ 1024                                              =   1.989 TiB
```

**Gap: 6.868%** at the GB/GiB step.

**Where it comes from:** a bitrate is **decimal** — 6.0 Mbps is 6 × 10⁶ bits per second — so the
intermediate megabytes are 10⁶ bytes. Converting those to gibibytes divides by
**2³⁰ / 10⁶ = 1073.741824**, not by 1024. Dividing by 1024 reports roughly half the true gap.

> The classic error. `psec.video` contained exactly this bug until Module 32 was written — see
> [`../../32_Engineering_Math/00_MODULE_OVERVIEW.md`](../../32_Engineering_Math/00_MODULE_OVERVIEW.md).
>
> Note the gap is **6.868%** here and **9.051%** at the TB/TiB scale, because the TB figure applies
> the mismatch twice (once at GB, once at TB) while GiB→TiB is a clean 1024. Full marks needs the
> decimal-bitrate reason, not just the number.
>
> 1 pt GB/day + TB, 1 pt GiB/day, 1 pt the reason.

### 27 — PoE switch *(3 pts)*

```
   ports used   =  12 / 24                             12 free
   power used   =  12 × 30.0 W (802.3at PSE)  =  360.0 W
   utilisation  =  360.0 / 240.0              =  150.0%
```

Findings:

- `POE BUDGET EXCEEDED: 360.0 W required vs 240.0 W available (over by 120.0 W).`
- `POE BUDGET TIGHT: 150% utilised.`

**Power binds. Ports do not** — 12 free ports comfortably satisfies a 20% spare policy (5
required). The switch has half its ports empty and cannot power what is already plugged in.

The fix is not more ports. It is a higher-budget switch, a second switch, or non-PoE power for
some devices.

> 1 pt for 360 W, 1 pt for 150% and both findings, 1 pt for identifying power as the binding
> constraint **and** noting ports are fine. This is the whole lesson: two independent constraints.

### 28 — Voltage drop *(3 pts)*

```
   Vd  =  2 × 12.9 × 0.25 × 175 / 640.4  =  1128.75 / 640.4  =  1.7626 V

   V at device  =  12.0 − 1.7626                             =  10.2374 V
   Drop         =  1.7626 / 12.0                             =  14.688%
```

**FAIL.** The device needs 10.5 V and receives 10.237 V — short by **0.263 V**.

Maximum length for 22 AWG at this load:

```
   L_max  =  (12.0 − 10.5) × 640.4 / (2 × 12.9 × 0.25)  =  960.6 / 6.45  =  148.93 ft
```

Smallest conductor that works at 175 ft: **20 AWG** (1020 cmil).

```
   check:  2 × 12.9 × 0.25 × 175 / 1020  =  1.1066 V  →  10.893 V at the device  ✓
```

> 1 pt drop + voltage, 1 pt the fail verdict with the percentage, 1 pt L_max **and** 20 AWG.
>
> A 14.7% drop should trigger suspicion before you finish the arithmetic. Rules of thumb like
> "keep it under 10%" are useful as an alarm, never as the calculation — the only figure that
> decides is the **device's** minimum operating voltage `[MFR][VERIFY]`, and a "12 VDC" device may
> specify anything from 10.2 to 11.5 V.

### 29 — Battery and supply *(3 pts)*

```
   Ah_standby   =  0.8 A × 6 h                     =   4.80 Ah
   Ah_alarm     =  2.5 A × (10/60) h               =   0.42 Ah
   Ah_raw                                          =   5.22 Ah

   Ah_required  =  5.22 × 1.25 × 1.25              =   8.15 Ah

   Supply: design current = max(0.8, 2.5) = 2.5 A
           recommended    = 2.5 × 1.25            =   3.12 A
```

**Select: 12 Ah battery, 3.5 A (or next standard up) supply.**

**If you had used the alarm current for the battery:**

```
   2.5 A × 6 h = 15.0 Ah raw  →  × 1.5625  =  24.09 Ah
```

Nearly **three times** the correct figure. You would specify a 26 Ah battery and the enclosure to
hold it, at several times the cost and space, for a load that draws 2.5 A for ten minutes a year.

The alarm current contributes **0.42 of 5.22 Ah — 8%** of the battery, and **100%** of the supply
selection. Same two numbers, opposite roles.

> 1 pt raw + sized Ah, 1 pt supply current, 1 pt the wrong-way figure with the point about which
> current does what.
>
> `[CODE][VERIFY]` The 6-hour duration is a given here. In real work it is set by the adopted code
> and the AHJ, and getting it from a previous project is how you inherit someone else's mistake.
> Also missing from `power_supply_sizing`: **battery charging current**, which comes from the
> supply datasheet and must be added before selection.

### 30 — Adversary path *(3 pts)*

```
   T_T  =  200 + 180 + 220                       =  600 s
   T_D  =  200 (detection at task 1 completion) + 45 (assessment)  =  245 s
   T_A  =  600 − 245                             =  355 s

   margin  =  T_A − T_R  =  355 − 400            =  −45 s
```

**Verdict: `NOT TIMELY. Short by 45 s.`** The adversary completes the act 45 seconds before the
response arrives. Against the 60 s required confidence margin, the total **deficit is 105 s**.

Required detection point:

```
   T_D_max  =  T_T − T_R − margin  =  600 − 400 − 60  =  140 s
```

**What it means:** detection must occur — **including assessment** — no later than 140 s into the
sequence. Detection currently occurs at 245 s. Since the 45 s assessment delay is part of `T_D`,
the *sensor* must fire by **95 s** of raw path time, which falls **inside task 1** (0–200 s).

So detection cannot stay at the completion of task 1. It must move to a point **partway through
it** — an earlier layer covering the approach or the start of that task, not the end of it — or
the assessment delay must come down, or both.

> 1 pt for T_T/T_D/T_A, 1 pt for the verdict with the shortfall, 1 pt for the required detection
> point **and** the observation that assessment delay eats into it.
>
> That last point is the one most people miss. `T_D` is detection **plus** assessment, so a 45 s
> assessment delay consumes 45 s of a 140 s budget before any sensor has to be chosen. It is the
> cheapest term in the whole inequality to improve and the one nobody looks at.

---

## Scoring

| Range | Reading |
|---|---|
| 47–52 | You can derive this module. Go do the capstone. |
| 39–46 | Solid. Re-read the lesson behind whichever Part C question you lost points on. |
| 26–38 | The concepts are there and the arithmetic is not. Work every problem set. |
| < 26 | Expected on a cold take. Read the module. |

**Score Part C separately.** Part A high and Part C low means you have read the module rather than
done it — which is precisely the failure mode this module exists to prevent. Go back and work the
problem sets in [`../../32_Engineering_Math/_solutions/`](../../32_Engineering_Math/_solutions/)
with a calculator and paper.

---

## Where each question came from

| Q | Lesson |
|---|---|
| 1–4, 23–25 | [`01_camera_fov.md`](../../32_Engineering_Math/01_camera_fov.md) |
| 5–8, 25 | [`02_pixel_density.md`](../../32_Engineering_Math/02_pixel_density.md) |
| 9–12, 17 | [`03_bandwidth.md`](../../32_Engineering_Math/03_bandwidth.md) |
| 26 | [`04_storage.md`](../../32_Engineering_Math/04_storage.md) |
| 13, 14, 18, 27 | [`05_poe.md`](../../32_Engineering_Math/05_poe.md) |
| 15, 19, 28 | [`06_voltage_drop.md`](../../32_Engineering_Math/06_voltage_drop.md) |
| 16, 20, 29 | [`07_battery_ups.md`](../../32_Engineering_Math/07_battery_ups.md) |
| 21, 22, 30 | [`08_adversary_path.md`](../../32_Engineering_Math/08_adversary_path.md) |
