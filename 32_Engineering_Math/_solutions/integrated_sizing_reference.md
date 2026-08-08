# Reference Solution — Integrated Sizing Capstone

> Worked reference for
> [`../_exercises/integrated_sizing.md`](../_exercises/integrated_sizing.md). **Do not read this
> until you have a completed worksheet.** Its value is as a comparison, not as a source.
>
> Every numeric value below was produced by running `psec` and transcribing the result. If your
> hand calculation disagrees with a figure here, work out which of you is wrong before assuming
> it is you. That is the entire point of the module.

> **This is one defensible answer, not the answer.** Parts A4, A6, D5, D6, F5, F7, and all of
> Part G admit more than one good response. What is *not* negotiable is the arithmetic, the
> failures it exposes, and the obligation to state your assumptions.

---

## Part A — Optics and pixel density

### A1 — Audit of the draft schedule

Computed with `CameraSpec.coverage_report()`, which uses **slant range**, not floor distance.
Sensor 5.37 × 3.02 mm, 2688 × 1520 px, 5 ft target height.

| Tag | Lens | Mount | Floor dist | HFOV | Slant | Scene W | PPF | Required | Depression | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| FENCE-01..04 | 6 mm | 16 ft | 200 ft | 48.22° | 200.3 ft | 179.3 ft | **15.0** | 8 (detect) | 3.1° | PASS |
| GATE-01 | 4 mm | 14 ft | 60 ft | 67.74° | 60.7 ft | 81.5 ft | **33.0** | 76 (identify) | 8.5° | **FAIL** |
| DOCK-01..04 | 6 mm | 16 ft | 55 ft | 48.22° | 56.1 ft | 50.2 ft | **53.5** | 38 (recognise) | 11.3° | PASS |
| WHSE-01..06 | 2.8 mm | 24 ft | 80 ft | 87.60° | 82.2 ft | 157.7 ft | **17.0** | 19 (observe) | 13.4° | **FAIL** |
| CAGE-01 | 4 mm | 12 ft | 12 ft | 67.74° | 13.9 ft | 18.7 ft | **144.1** | 76 (identify) | 30.3° | PASS |
| LOBBY-01..02 | 6 mm | 10 ft | 15 ft | 48.22° | 15.8 ft | 14.2 ft | **189.9** | 76 (identify) | 18.4° | PASS |

Worked by hand for GATE-01, to show the chain:

```
   HFOV  = 2 · arctan( 5.37 / (2 × 4) )        = 2 × 33.87°   = 67.74°
   slant = sqrt( 60² + (14 − 5)² )             = sqrt(3681)   = 60.67 ft
   W     = 60.67 × 5.37 / 4                    = 81.45 ft
   PPF   = 2688 / 81.45                        = 33.0 px/ft
   depression = arctan( (14 − 5) / 60 )        = 8.5°
```

**Note the effect of using slant range.** At the floor distance of 60 ft, `fov_width_ft` gives
80.55 ft and 33.4 PPF. The slant correction costs 0.4 PPF here because the camera is far relative
to its mount height. At CAGE-01 the same correction takes PPF from 188.4 (at 8 ft) down through
144.1 (at 12 ft) — for close, high-mounted cameras the correction is large, which is exactly the
lesson-01 warning.

### A2 — The two failures

| Tag | Achieved | Required | Shortfall |
|---|---|---|---|
| GATE-01 | 33.0 PPF (**observe**) | 76 PPF (identify) | **56.6% short** |
| WHSE-01..06 | 17.0 PPF (**detect**) | 19 PPF (observe) | **10.5% short** |

GATE-01 misses by two whole DORI classes. It was specified to identify a driver and it will
produce footage in which you can tell a person is at the gate and nothing else. This is the most
common and most expensive failure in video design: a camera that satisfies everyone at the design
review and nobody at the incident.

WHSE fails narrowly. 10.5% is inside the honest error of this model — MTF, focus, motion blur, and
compression all sit below the geometric calculation. **That is an argument for treating it as a
worse failure, not a lesser one.** The geometric number is a ceiling; the real number is below it.

### A3 — The lens GATE-01 actually needs

Invert the pixel-density relation:

```
   W_required = px / PPF_required   = 2688 / 76      = 35.368 ft
   f          = D · w / W           = 60 × 5.37 / 35.368 = 9.110 mm
```

The stocked lens list has a **9 mm**. Round down to it and check:

```
   9 mm @ 60 ft floor → slant 60.2 ft, W 35.9 ft, PPF 74.8  →  classifies "recognise"
```

**It still fails**, by 1.2 PPF (1.6%). Two things caused that:

1. The inverse was computed at the **floor** distance (60 ft), but the light travels the **slant**
   path (60.2 ft). Redo it at the slant distance and the requirement is 9.140 mm.
2. Rounding a computed focal length **down** to the nearest stocked size always loses pixel
   density. Round **up**.

`max_range_ft("identify")` for the 9 mm confirms it: **59.28 ft**. The gate is at 60 ft. You miss
by nine inches of standoff.

The next stocked size up is **12 mm**:

```
   12 mm @ 60 ft floor → slant 60.2 ft, W 26.9 ft, PPF 99.8  →  identify ✓
   max_range_ft("identify") = 79.0 ft  →  19 ft of design margin
```

**What you gave up:** the horizontal angle of view collapses from **67.74° to 25.22°**, and the
scene width at the gate from **81.5 ft to 26.9 ft**. A 26.9 ft view covers the driver's window and
a lane. It does not cover the gate, the approach, a second vehicle, or anyone walking in beside
the truck.

### A4 — Why the gate needs two cameras

R1 says "identify any driver at the vehicle gate." But the reason a gate camera exists is also to
show *what happened at the gate* — tailgating, a second occupant, someone on foot using the
vehicle as cover. The draft's single 4 mm camera delivered the wide view and no identification.
The corrected 12 mm delivers identification and no context. **Neither camera can be both, because
angle of view and pixel density trade against each other directly at a fixed pixel count.**

**Fix: two cameras at the gate.**

| Tag | Role | Lens | Result |
|---|---|---|---|
| GATE-01 | Scene context, approach, tailgating | 4 mm (unchanged) | 33.0 PPF, observe |
| GATE-02 | Driver identification | 12 mm | 99.8 PPF, identify |

**Added cost: +1 camera, +1 switch port, +30 W** (outdoor, heated, 802.3at class allocation).
Carry those three numbers to Part C.

> An equally defensible alternative: mount a 9 mm at 45 ft from the stop line instead of on the
> 60 ft mast — `coverage_report` gives 99.5 PPF, identify, with a 6.3° depression angle. It saves
> a lens size and costs a mounting position. Either answer is correct if you show the calculation.
> What is **not** correct is specifying the 9 mm on the 60 ft mast.

### A5 — How far the 2.8 mm warehouse lens actually reaches

```
   max_range_ft("observe") for 2.8 mm, 2688 px   =  73.77 ft   ← this is a SLANT range
   vertical offset = 24 − 5 = 19 ft
   max FLOOR distance = sqrt( 73.77² − 19² ) = sqrt(5081.2)     =  71.28 ft
```

Check it: at 71 ft floor distance, `coverage_report` gives slant 73.5 ft, W 141.0 ft, **19.1 PPF**
— just over the 19 PPF threshold, and classified "observe."

The drawn design used **80 ft**. Coverage area scales with the square of distance, so the position
count scales the same way:

```
   6 positions × (80 / 71.28)²  =  6 × 1.2596  =  7.56  →  8 positions
```

**Fix: 8 warehouse cameras at 2.8 mm instead of 6, design distance reduced to ≤ 71 ft.**
**Added cost: +2 cameras, +2 switch ports, +30.8 W** (indoor, 802.3af).

> Designing to exactly 71 ft leaves 0.5% of margin on a figure the model already overstates. In
> real work, design to ~68 ft and note it. The exercise accepts 8 positions as the answer.

### A6 — Why the "cheaper" 4 mm fix is worse

```
   4 mm @ 80 ft floor → slant 82.2 ft, W 110.4 ft, PPF 24.4  →  observe ✓
```

It passes the pixel-density test at the original 80 ft, with no added cameras. It is still the
wrong answer, because **scene width fell from 157.7 ft to 110.4 ft — a 30% loss per camera.** Six
cameras at 2.8 mm covered 6 × 157.7 = 946 ft of scene width. To cover the same width at 110.4 ft:

```
   946 / 110.4  =  8.57  →  9 positions
```

So the "no new cameras" fix needs **nine** cameras, against **eight** for keeping the 2.8 mm and
tightening the spacing. The cheap-looking option is more expensive.

**The general lesson:** pixel density and coverage are not independent knobs. Fixing a density
failure by narrowing the lens moves the problem into the coverage budget, where it usually costs
more. Check both before you claim a lens change is free.

### A7 — The fence line

```
   max_range_ft("detect")   for 6 mm  =  375.4 ft (slant)
   max_range_ft("observe")  for 6 mm  =  158.1 ft (slant)
   at 200 ft floor: slant 200.3 ft, W 179.3 ft, PPF 15.0  →  detect ✓ (87% margin over 8 PPF)
```

The 200 ft longest span works comfortably for R3 as written. **It fails immediately if R3 is
upgraded to "observe"** — the 6 mm meets observe only to 158 ft slant, so a 200 ft span would need
either a 7.6 mm-equivalent lens or a mast added to every long run. Flag this in the memo as a
scope-change trigger, because "can we also see what they're doing" is the single most common
post-award request on a fence line.

### A8 — What pixel density does not tell you

1. **Whether there is any light.** PPF is a geometric quantity. It is identical at noon and at
   2 a.m. Every one of these outdoor cameras is a night-time device most of the hours it matters.
2. **Whether the image is sharp.** Lens MTF, focus error, motion blur, and compression all destroy
   detail the geometry says is present. Geometric PPF is necessary, never sufficient.
3. **Whether the face is pointed at the camera.** GATE-02 at 4.8° depression sees a face; a
   30.3° depression like CAGE-01 sees a forehead and a hat. Lesson 02's problem P2.6 is exactly
   this trap.
4. **Whether the subject is in frame at all.** A 26.9 ft-wide identification view is unforgiving of
   a truck stopping three feet further forward than assumed.

---

## Part B — Bandwidth and storage

### B1 — Per-camera bitrates

Reference: 4 MP, 30 fps, H.264 = **10.0 Mbps** `[PRACTICE]`. Frame-rate scaling is
`(to_fps / from_fps)^0.7`, applied **before** the codec factor. H.265 factor 0.5.

| Group | fps | Ratio | `ratio^0.7` | H.264 intermediate | × 0.5 (H.265) |
|---|---|---|---|---|---|
| Vehicle gate, Vault cage | 30 | 1.000 | 1.00000 | 10.0000 Mbps | **5.0000 Mbps** |
| Fence, Dock, Lobby | 15 | 0.500 | 0.61557 | 6.1557 Mbps | **3.0779 Mbps** |
| Warehouse | 10 | 0.333 | 0.46346 | 4.6346 Mbps | **2.3173 Mbps** |

Note the sub-linear scaling doing its job: halving the frame rate from 30 to 15 cuts bitrate by
38%, not 50%. I-frames and overhead do not scale, and inter-frame prediction gets *less* efficient
as successive frames diverge. This is a **documented modelling choice** `[PRACTICE]`, not a law —
challenge it against a pilot stream if the storage number is load-bearing on a bid.

### B2 — Aggregate bandwidth (corrected 21-camera schedule)

| Group | Qty | Bitrate | Duty | Peak | Average |
|---|---|---|---|---|---|
| Fence line | 4 | 3.0779 | 0.35 | 12.311 | 4.309 |
| Vehicle gate | 2 | 5.0000 | 1.00 | 10.000 | 10.000 |
| Dock apron | 4 | 3.0779 | 1.00 | 12.311 | 12.311 |
| Warehouse floor | 8 | 2.3173 | 0.50 | 18.539 | 9.269 |
| Vault cage | 1 | 5.0000 | 1.00 | 5.000 | 5.000 |
| Lobby | 2 | 3.0779 | 1.00 | 6.156 | 6.156 |
| **System** | **21** | | | **64.3 Mbps** | **47.0 Mbps** |

Split by switch, using the Part C geography:

```
   IDF-2 (yard: fence + gate + dock, 10 cameras)   peak 34.6 Mbps
   IDF-1 (core: warehouse + cage + lobby, 11 cams) peak 29.7 Mbps
```

**Put the peak on the riser.** Motion events correlate — a vehicle entering the yard triggers the
gate, the fence, and two dock cameras within seconds of each other, which is precisely when you
need the bandwidth. Sizing to the 47.0 Mbps average would be sizing for the hours when nothing is
happening. Both switch uplinks fit a 1 Gb link with an order of magnitude spare, so nothing binds
here — but say the number, because on a 100 Mb legacy uplink it would have.

### B3 — Storage

Raw, per the retention table:

| Group | Qty | Effective h/day | Retention | TB | TiB |
|---|---|---|---|---|---|
| Fence line | 4 | 8.40 | 30 d | 1.396 | 1.270 |
| Vehicle gate | 2 | 24.00 | 30 d | 3.240 | 2.947 |
| Dock apron | 4 | 24.00 | 30 d | 3.989 | 3.628 |
| Warehouse floor | 8 | 12.00 | 30 d | 3.003 | 2.731 |
| Vault cage | 1 | 24.00 | **90 d** | 4.860 | 4.420 |
| Lobby | 2 | 24.00 | 30 d | 1.994 | 1.814 |
| **Raw total** | | | | **18.483 TB** | **16.810 TiB** |
| **With 20% headroom** | | | | **22.179 TB** | **20.172 TiB** |

Worked by hand for one vault cage camera, showing every conversion:

```
   5.0 Mbps × 3600 s/h × 24 h        =  432,000 megabits/day
                        ÷ 8          =   54,000 megabytes/day
                        ÷ 1000       =       54.0 GB/day   (decimal)
   × 90 days ÷ 1000                  =        4.860 TB
```

And the same figure in binary units:

```
   54,000 megabytes ÷ (2³⁰ / 10⁶)    =   54,000 / 1073.741824  =  50.291 GiB/day
   × 90 ÷ 1024                       =        4.420 TiB
```

**The gap is 9.051%,** and it is constant across the whole system because it is a pure unit
conversion, not a modelling choice. It comes from the fact that a bitrate is **decimal** — 5.0
Mbps is 5 × 10⁶ bits per second, so the intermediate megabytes are 10⁶ bytes. Converting those to
gibibytes divides by 2³⁰/10⁶ = 1073.741824, not by 1024. Dividing by 1024 is the classic error;
it reports the gap as roughly half its true size. `psec` had exactly this bug until this module
was written — see the note in [`../00_MODULE_OVERVIEW.md`](../00_MODULE_OVERVIEW.md).

**Why this matters commercially:** the client buys disk labelled in decimal TB and their operating
system reports capacity in TiB. A 22.2 TB array shows up as roughly 20.2 TiB. If nobody explains
the 9% in advance, it is discovered as a shortfall at handover.

### B4 — The honest range

```
   storage_range_tb()  →  15.53 TB  to  35.49 TB
   point estimate with headroom      22.18 TB
```

The bounds are 0.7× and 1.6× the headroom figure `[PRACTICE]`. They are not statistical confidence
intervals; they are the observed spread between an optimistic smart-codec estimate on a static
scene and a busy, noisy, low-light one.

> **The sentence to say to the client:**
> "We're sizing the array at **22 TB** to hold 30 days, but the true figure depends on how busy
> your scenes are and could land anywhere between **16 and 36 TB** — so we're specifying a chassis
> with expansion bays, and we'll measure real bitrate in the first week and tell you where you
> actually landed."

That sentence does three things a point estimate cannot: it gives them a number to budget against,
it makes the uncertainty theirs to see rather than yours to absorb, and it commits you to closing
it with data instead of argument.

### B5 — RAID sizing

```
   RAID 6, 8-disk group  → efficiency (8−2)/8 = 0.75  →  22.179 / 0.75  =  29.57 TB raw
   RAID 6, 12-disk group → efficiency (12−2)/12 = 0.833 → 22.179 / 0.833 = 26.62 TB raw
```

**What RAID 6 protects against here:** the loss of any two disks in a group, without data loss and
without taking the array offline.

**What it does not protect against, and what you must say out loud:** controller failure, chassis
loss, fire, water, theft of the recorder, ransomware, accidental or malicious deletion, or a
configuration error that stops recording. It is not a backup. During a rebuild — which on
high-capacity drives runs for many hours — the array is slower and its remaining redundancy is
reduced. For an asset whose 90-day retention is a **regulatory** obligation (R8), a single RAID 6
array in a single room is a single point of failure with a compliance consequence, and that
belongs in the memo as a named risk, not a footnote.

### B6 — The inverse problem: the existing 96 TB NVR

30 cameras, 8 MP, H.264, 30 fps, continuous, 24 h/day. Reference bitrate **18.0 Mbps**.

```
   per camera:  18.0 × 3600 × 24 / 8 / 1000   =  194.4 GB/day   (181.049 GiB/day)
   30 cameras:                                  5.832 TB/day
   retention  =  96 TB / 5.832 TB/day         =  16.46 days
```

**The facilities manager told an auditor it holds 30 days. It holds 16.** If the NVR reports in
TiB and the "96" was read off the OS, the answer is 18.10 days — still not 30.

Two routes to 30 days:

| Route | Calculation | Result |
|---|---|---|
| **Buy disk** | 18.0 Mbps × 30 d × 30 cams | **174.96 TB** required → buy ~79 TB more |
| **Change encoding** to H.265 @ 15 fps | 18.0 × 0.61557 × 0.5 = **5.5401 Mbps** | 96 TB now buys **53.5 days** |

The encoding change is roughly free and overshoots the requirement by 78%. It costs frame rate and
depends on the cameras supporting H.265 `[VERIFY per camera model]` — and on someone accepting
that 15 fps is enough, which is a conversation about what the footage is *for*, not a technical
question. Note the asymmetry that makes this worth raising: buying 79 TB of disk fixes the number;
re-encoding fixes the number *and* leaves 23 days of margin for the next camera they add.

### B7 — What the Part A fixes cost

| | Draft (18 cams) | Corrected (21 cams) | Delta |
|---|---|---|---|
| Peak bandwidth | 54.7 Mbps | 64.3 Mbps | **+9.635 Mbps** |
| Average bandwidth | 39.7 Mbps | 47.0 Mbps | **+7.317 Mbps** |
| Raw storage | 16.112 TB | 18.483 TB | **+2.371 TB** |
| With headroom | 19.334 TB | 22.179 TB | **+2.845 TB** |

Attribution:

- **GATE-02** (A4 fix, 1 camera): +5.000 Mbps peak, **+1.620 TB** raw
- **WHSE-07, -08** (A5 fix, 2 cameras): +4.635 Mbps peak, **+0.751 TB** raw (2 × 0.375)

One gate camera costs **more than twice** the storage of two warehouse cameras, because it records
continuously at 30 fps while they record at 10 fps on a 50% duty cycle. Camera *count* is a poor
proxy for storage; camera *duty* is the real driver.

---

## Part C — PoE budget and switch capacity

Corrected schedule: **10 outdoor** (fence 4, gate 2, dock 4), heated, 802.3at →
**30.0 W PSE each**. **11 indoor** (warehouse 8, cage 1, lobby 2), 802.3af →
**15.4 W PSE each**.

### C1 — Class allocation, not datasheet draw

Budget against **class**: 10 × 30.0 + 11 × 15.4 = **469.4 W**.

The one-sentence justification: many switches reserve power by the class the device negotiates,
not by what it consumes, so a 6 W camera that classifies as Type 2 can hold 30 W of the switch
budget hostage — and whether *your* switch does static or dynamic allocation is a per-model
question you have not yet answered `[VERIFY per switch datasheet]`.

### C2 — Everything on one switch

```
   ports:  21 used / 24        3 free
   power:  469.4 W / 370.0 W   126.9% utilised
```

Findings from `PoESwitch.check()`:

- `POE BUDGET EXCEEDED: 469.4 W required vs 370.0 W available (over by 99.4 W).`
- `INSUFFICIENT SPARE PORTS: 3 free, 5 required at 20%.`
- `POE BUDGET TIGHT: 127% utilised.`

**Both constraints bind, and they bind independently.** Power is over by 99.4 W (26.9%). Ports are
over by 2 against the spare-port policy — the switch physically holds all 21 devices, but leaves
no room for the growth the policy exists to reserve. Note that adding ports would not fix power
and adding power would not fix ports. That independence is the whole point of lesson 05.

### C3 — Geographic split

| | IDF-2 (yard/gatehouse) | IDF-1 (office core) |
|---|---|---|
| Devices | 10 outdoor | 11 indoor |
| Ports | 10 / 24, **14 free** | 11 / 24, **13 free** |
| Power | **300.0 W** / 370.0 W | **169.4 W** / 370.0 W |
| Utilisation | **81.1%** | **45.8%** |
| Findings | `POE BUDGET TIGHT: 81% utilised` | *(none)* |

IDF-2 passes and still raises a finding. **What the finding protects you from is the gap between
"it fits today" and "it fits the next change order."** At 81% you have 70 W of headroom on a
switch with 14 empty ports. The next person to look at that switch will see the empty ports, not
the watts, and will assume there is room for fourteen more cameras.

### C4 — The growth limit, stated correctly

```
   IDF-2 headroom  =  370.0 − 300.0  =  70.0 W
     → additional OUTDOOR cameras (30.0 W each):   70.0 // 30.0   =  2
     → additional INDOOR  cameras (15.4 W each):   70.0 // 15.4   =  4
   IDF-2 free ports                                              = 14
```

> **The sentence for the client:** "The yard switch has fourteen empty ports but only enough power
> for **two** more outdoor cameras. If you add a third, we replace the switch."

Saying "we have 14 spare ports" is misleading because it names the constraint that is *not*
binding. It is true, it is measurable, and it will cause someone to make a commitment you cannot
keep. Quote the binding constraint, in the units the client thinks in — cameras, not watts.

### C5 — Re-budgeting on datasheet draw

```
   10 × 16.5 W + 11 × 7.2 W  =  244.2 W  /  370.0 W  =  66.0%
```

The power findings vanish. **One finding does not:**
`INSUFFICIENT SPARE PORTS: 3 free, 5 required at 20%.`

That is significant because the port count is a physical fact and the power figure is a modelling
assumption. Changing which power model you believe made two of the three findings disappear and
left the third untouched — which tells you the port finding is the more robust of the two and the
one you should trust when they disagree.

Three reasons not to build the single-switch design anyway:

1. Static class allocation would reserve 469.4 W regardless of what the cameras actually draw, and
   the switch would refuse power to devices while its own utilisation meter reads 66%.
2. Datasheet draw is a nominal figure at room temperature. These are **heated** outdoor cameras;
   their draw rises exactly when it is coldest, which is exactly when every one of them rises
   together.
3. One switch means every camera on site shares one failure domain, one firmware upgrade, and one
   power cord.

To change my mind I would have to `[VERIFY]` from the switch datasheet that it does **dynamic**
allocation, and `[VERIFY]` the heater-on draw from the camera manufacturer at the site's design
low temperature — and I would still keep the geographic split for the failure-domain reason.

### C6 — Why PoE needs no voltage-drop calculation

Because PoE solves it inside the standard. A PSE sources 44–57 V into a link whose maximum
resistance is bounded by the cable specification and whose length is bounded to 100 m, and the PD
contains a converter that accepts the whole input range. The 802.3af/at/bt gap between PSE power
and PD power (15.4 vs 12.95, 30.0 vs 25.5) **is the cable loss allowance**, already paid for. Your
lesson-06 arithmetic is done for you by the standards body.

That protection ends the moment you leave PoE. The cage gate lock in Part D is a 12 V DC load on
copper you chose, at a length you chose, and nothing bounds the drop except you.

---

## Part D — Voltage drop at the cage gate

Given: 12.0 V supply (calculated at the low end, not 13.8 V), 0.45 A, minimum device voltage
10.2 V `[MFR][VERIFY]`, K = 12.9 Ω·cmil/ft at 75 °C.

### D1 — As drawn

```
   Segment 1  home run, 250 ft, 18 AWG (1624 cmil):
       Vd = 2 × 12.9 × 0.45 × 250 / 1624   =  2902.5 / 1624   =  1.7873 V   (14.894%)

   Segment 2  power transfer + door loop, 8 ft, 22 AWG (640.4 cmil):
       Vd = 2 × 12.9 × 0.45 × 8 / 640.4    =    92.88 / 640.4 =  0.1450 V

   Total drop                                                 =  1.9323 V
   Voltage at the lock  =  12.0 − 1.9323                      = 10.0677 V
```

**FAIL.** The lock needs 10.2 V and gets 10.068 V — short by **0.1323 V**.

This is the failure mode module 35 described in the building: the lock buzzes, sometimes releases,
releases reliably in the morning and intermittently at 3 p.m. when the ceiling is warm, and gets
logged as an access control software problem for eight months.

### D2 — Which segment dominates, and the rule it destroys

```
   home run  1.7873 / 1.9323  =  92.49%
   transfer  0.1450 / 1.9323  =   7.51%
```

`35_Doors_and_Hardware/06` showed a case where the **last six feet** through the power transfer
dominated the total, and concluded that the transfer is what people forget. Here the home run
dominates it 12 to 1.

**The rule this destroys is "always check the transfer."** Neither segment is inherently the
culprit. Drop is `2·K·I·L / CM` — it scales with length *and* inversely with circular mils, and
which segment wins depends entirely on the ratio `L/CM` for each. Module 35's case had a short,
very thin transfer against a short, fat home run. This one has a long home run against a short
transfer. **Compute both. Every time. The habit is the defect.**

### D3 — The trap: sizing the home run in isolation

Run `smallest_awg_for_run(12.0, 0.45, 250, 10.2)` and it returns **18 AWG**. Specify that and you
have specified the conductor that fails.

It is wrong by very little, which is what makes it dangerous:

```
   max_run_length_ft(12.0, 0.45, "18", 10.2)  =  251.78 ft
```

The home run alone would work — with 1.78 ft to spare, or **0.7% of margin**. The 8 ft of 22 AWG
transfer consumes 0.1450 V and the design goes under.

Doing it correctly means **budgeting the drop across both segments** before sizing either. Work
backwards from the load:

```
   The lock needs                             ≥ 10.2000 V
   The transfer will take                        0.1450 V
   ∴ the home run must deliver                 ≥ 10.3450 V at the frame junction

   smallest_awg_for_run(12.0, 0.45, 250, 10.345)  →  16 AWG
```

Check the whole circuit at 16 AWG (2583 cmil):

```
   Segment 1:  2902.5 / 2583   =  1.1237 V
   Segment 2:                     0.1450 V
   Total                          1.2687 V   →  V at lock = 10.7313 V   ✓
   Design margin over 10.2 V                              =  0.5313 V
```

### D4 — Maximum run lengths and the margin

```
   max_run_length_ft(12.0, 0.45, "18", 10.200)  =  251.78 ft   ← ignores the transfer
   max_run_length_ft(12.0, 0.45, "18", 10.345)  =  231.50 ft   ← honest limit for 18 AWG
   max_run_length_ft(12.0, 0.45, "16", 10.200)  =  400.47 ft
```

At 250 ft the corrected 16 AWG has **0.5313 V** of margin, and the run could grow to **368 ft**
(allowing for the transfer) before it binds. That is real margin against the thing that
actually happens on site: the cable route measured on the plan is not the cable route the
installer pulls.

### D5 — Rechecking at a sagging supply

A battery-backed supply near the end of its standby period sits well below nominal. At **11.6 V**:

```
   16 AWG + 22 AWG:  11.6 − 1.2687  =  10.3313 V   ✓ passes, margin 0.1313 V
   14 AWG + 22 AWG:  11.6 − 0.8518  =  10.7482 V   ✓ passes, margin 0.5482 V
```

16 AWG still passes, on **0.13 V**. That is the same order as the shortfall that failed the
original design, and it appears precisely during a power outage — when the lock most needs to
work and nobody is available to diagnose it.

**Recommendation: specify 14 AWG for the home run.** The upgrade from 16 to 14 costs a few dollars
of copper on a 250 ft pull and converts a 0.13 V margin into 0.55 V. This is the cheapest
insurance in the entire design, and it is the line item most likely to be value-engineered out by
someone reading only the 12.0 V calculation.

### D6 — Fixing it without touching the conductor

**Move the power supply.** Put a local 12 V supply in the warehouse near the cage instead of
feeding from IDF-1 in the office. A 30 ft run of 18 AWG at 0.45 A drops 0.2145 V; the whole
problem disappears.

Tradeoff: a second supply means a second battery, a second enclosure, a second AC circuit, a
second thing to inspect, and a second thing that can be missing from the maintenance schedule.
You have traded a copper problem for an asset-management problem. On a site with one remote
opening that is usually a bad trade; on a site with a dozen, it is the right architecture.

> A second option: run the lock at **24 VDC**. Same power at half the current — 0.225 A over 250 ft
> of 18 AWG drops 0.8936 V, delivering 23.11 V against a 20.4 V minimum. Voltage drop as a
> *percentage* is what matters, and doubling the supply voltage halves the current and therefore
> halves the drop. Tradeoff: a different lock SKU, and 24 V hardware is not always available in the
> function you need `[MFR][VERIFY]`.

---

## Part E — Battery and power supply

### E1 — The load list

| Load | Qty | Standby (A ea) | Standby total | Alarm (A ea) | Alarm total |
|---|---|---|---|---|---|
| Access controller + power board | 1 | 0.250 | 0.250 | 0.250 | 0.250 |
| Card readers | 6 | 0.120 | 0.720 | 0.200 | 1.200 |
| Electrified locks, fail secure | 6 | 0.030 | 0.180 | 0.450 | 2.700 |
| Door position switch + REX | 6 | 0.008 | 0.048 | 0.008 | 0.048 |
| Local sounder | 1 | ~0 | ~0 | 0.300 | 0.300 |
| | | | **1.198 A** | | **4.498 A** |

The locks are 15% of standby current and **60% of alarm current**. Fail-secure hardware is
de-energised at rest and draws only when released — which is why it barely touches the battery and
dominates the supply.

### E2 — Battery for 4 h standby

```
   Ah_standby =  1.198 A × 4 h                  =  4.79 Ah
   Ah_alarm   =  4.498 A × (5/60) h             =  0.37 Ah
   Ah_raw                                       =  5.17 Ah
   Ah_required = 5.17 × 1.25 (derate) × 1.25 (aging)  =  8.07 Ah
```

The alarm component is **7% of the total**. Five minutes at 4.5 A is a small amount of energy; the
same 4.5 A is what forces the supply selection in E3. This is the pair people reverse.

**Selection: 12 V 12 Ah sealed lead-acid.** The next standard size down is 7 Ah, which is below
the 8.07 Ah requirement.

`[CODE][VERIFY]` The 4 h duration is the client's stated requirement. UL 294 addresses access
control standby and NFPA 72 governs anything tied to fire alarm; the adopted edition and the AHJ
decide. Sizing perfectly against the wrong duration is still wrong.

### E3 — Supply sizing

```
   design current = max(standby 1.198, alarm 4.498)  =  4.498 A
   recommended    = 4.498 × 1.25                     =  5.62 A
```

**Selection: 6 A continuous 12 VDC supply**, minimum.

**Peak current governs the supply; standby current governs the battery**, and the physical reason
is that they are answering different questions. The supply must deliver the worst instantaneous
demand without its output collapsing — six locks releasing at once during an evacuation is 2.7 A
by itself. The battery must deliver *energy over time*, and that worst instant lasts seconds, so
it contributes almost nothing to amp-hours. One is a power question; the other is an energy
question.

### E4 — Realistic runtime

```
   runtime_hours(12.0 Ah, 1.198 A, usable_fraction=0.8)  =  8.01 h
```

Against a 4 h requirement, **2.0× margin**. The `usable_fraction` of 0.8 reflects that discharging
a sealed lead-acid battery to zero destroys it; the honest capacity is what you can take out
without ruining the asset.

For comparison, a 7 Ah battery gives 4.67 h — which *looks* like it meets the 4 h requirement.
It does not, because that figure has not been derated or aged. Your own sizing calculation
already said 8.07 Ah. Trust the sizing calculation over the runtime check; the runtime function
is a sanity test, not a selection tool.

### E5 — When the AHJ says 24 hours

```
   Ah_standby =  1.198 × 24                     =  28.75 Ah
   Ah_alarm   =                                     0.37 Ah
   Ah_raw                                       =  29.13 Ah
   Ah_required = 29.13 × 1.5625                 =  45.51 Ah
```

A 5.6× jump. **Selection: 2 × 12 V 26 Ah in parallel (52 Ah), or a single 55 Ah.**

Three things change, and the calculator tells you **none** of them:

1. **Enclosure.** Two 26 Ah batteries do not fit a standard access-control can. You need a larger
   or separate battery enclosure, which needs wall space, which needs to be coordinated on a
   drawing with a trade that has already laid out that wall.
2. **Charging circuit.** Access control supplies typically charge at 0.5–1.5 A. Recharging 52 Ah
   from deep discharge at 1 A takes on the order of two days. If the adopted code specifies a
   maximum recharge time `[CODE][VERIFY]`, the standard supply cannot comply regardless of its
   output rating.
3. **Charging current adds to load current.** A supply sized at 6 A for the load is not sized for
   6 A of load *plus* charging. `power_supply_sizing` says so in its own return value and does not
   compute it, because the figure comes from the supply datasheet.

The pattern worth taking away: the calculator answers the energy question and hands you three
questions it cannot answer. Notice when a computed result has just changed the *category* of the
problem.

### E6 — Adding the derate factors instead of multiplying

```
   correct:  1.25 × 1.25   =  1.5625     →  5.17 × 1.5625  =  8.078 Ah
   wrong:    1 + 0.25 + 0.25 = 1.5       →  5.17 × 1.5     =  7.755 Ah

   under-sizing = (1.5625 − 1.5) / 1.5   =  4.167%
```

**At this site it does not matter.** Both figures round up to the same 12 Ah battery, because 7 Ah
is below both and 12 Ah is above both. Say that explicitly rather than implying a 4% error is
always harmless.

Where it *would* matter is anywhere the correct and incorrect figures straddle a standard battery
size — and at 24 h standby the same 4.167% is 1.9 Ah, which is the difference between selecting
two 26 Ah batteries and getting away with a 44 Ah. The factors multiply because they describe
*independent* reductions in delivered capacity: aging removes a fraction of what remains after the
discharge-rate derate, not a fraction of the original.

### E7 — The missing current

**Battery charging current.** `power_supply_sizing` returns
`"Does not include battery charging current -- add per datasheet."` It comes from the **power
supply** datasheet (the charger's rated output), not the battery's, and it must be added to the
design current before you select the supply. `[VERIFY per power supply datasheet]`

---

## Part F — Adversary path and timely detection

### F1 — Baseline

```
   Task                              delay    start      end
   Cut and spread fence fabric        90 s      0 s      90 s
   Cross yard to building             45 s     90 s     135 s
   Force dock personnel door         180 s    135 s     315 s   ← detection (DPS)
   Cross warehouse floor to cage      60 s    315 s     375 s
   Cut cage mesh and enter           240 s    375 s     615 s
   Load product to hand truck        300 s    615 s     915 s

   T_T  total task time                              =  915 s
   T_D  detection + assessment  =  315 + 60          =  375 s
   T_A  time remaining          =  915 − 375         =  540 s
   T_R  response                                     =  660 s
   margin  =  T_A − T_R         =  540 − 660         = −120 s
```

**Verdict: `NOT TIMELY. Short by 120 s.`** The adversary finishes loading and leaves 120 seconds
before the patrol arrives at the fence.

`compare_interventions` reports a **deficit of 240 s** — the 120 s shortfall plus the 120 s of
confidence margin the design was supposed to carry.

### F2 — The required detection point

```
   T_D_max  =  T_T − T_R − margin  =  915 − 660 − 120  =  135 s
```

At t = 135 s the adversary has finished crossing the yard and is starting on the dock personnel
door. **135 s is exactly the completion of task 2.**

What that result is telling you to build: detection must be **outside the building**, on the yard
or the fence, not on the door. The door contact is 240 s too late no matter how good it is.

> Without the confidence margin, `T_D_max` = 255 s, which falls in the middle of forcing the door.
> The margin is what pushes the requirement out past the building envelope — which is a good
> illustration of why the margin is a design input and not a rounding courtesy.

### F3 — The obvious fix, and why it fails

Move detection to a fence-line layer alarming at completion of the fence cut. Keep the 60 s
assessment delay.

```
   T_D  =  90 (fence cut complete) + 60 (assessment)  =  150 s
   T_A  =  915 − 150                                  =  765 s
   margin  =  765 − 660                               =  105 s
```

**Verdict: `MARGINAL. 105 s remaining but 120 s of confidence margin was required.`** Treated as
not timely.

Precisely why, in terms of the inequality: the budget is `T_D ≤ 135 s`, and `T_D` is
**detection time plus assessment time**. The 60 s assessment consumes 60 of the 135 s, leaving
only **75 s** of raw path time in which detection must occur. The fence cut does not complete
until 90 s. **There is no point on this path where a completion-triggered detection can fire early
enough**, because the very first task ends 15 s past the budget.

This is the most important result in the exercise. The obvious answer — spend money on a new
detection layer at the outermost boundary — buys 225 s of `T_A` and still fails, because a term
that has nothing to do with hardware is eating the budget.

### F4 — Fixing it with no hardware

**Reduce the assessment delay from 60 s to 30 s.**

```
   T_D  =  90 + 30    =  120 s      ≤ 135 s  ✓
   T_A  =  915 − 120  =  795 s
   margin  =  795 − 660  =  135 s   >  120 s required
```

**Verdict: `TIMELY. 135 s of margin beyond the 120 s required.`**

The operational change: alarms from the fence layer must **auto-call up the associated camera at a
continuously staffed monitoring position**. The 60 s figure was a patrol supervisor walking to a
monitor and finding the right view. The 30 s figure is a monitoring operator who is already
looking at a screen when the video appears on it.

That is a **monitoring contract change and a VMS configuration change** — no devices, no
construction, no conduit. It is the cheapest item in this entire design and it is the one that
makes the system work.

### F5 — The delay lever

Keep the original door detection. Harden the cage: CMU infill and expanded metal, raising the cage
breach task from 240 s to 600 s.

```
   T_T  =  1275 s          (915 + 360)
   T_D  =   375 s          (unchanged — still the door contact)
   T_A  =   900 s
   margin  =  900 − 660  =  240 s   >  120 s required
```

**Verdict: `TIMELY. 240 s of margin.`** It works, with twice the margin of F4.

**Comparing them on grounds other than arithmetic:**

| | F4 (assessment) | F5 (cage hardening) |
|---|---|---|
| Cost shape | Recurring (monitoring contract) | Capital, one-time |
| Depends on | Sustained human performance, every shift, forever | Physics |
| Degrades when | An operator is distracted, sick, or new | Never, until someone cuts a hole for a conduit |
| Detection occurs | At the fence, t = 120 s — **outside** | At the door, t = 375 s — **inside** |
| Responder arrives to find | An adversary in the yard | An adversary in the building |
| Fails how | Quietly, and you find out during the incident | Visibly, when someone removes the mesh |

F4 is cheaper and it moves detection **outward**, which is worth more than the margin arithmetic
shows: it gives the responder the option of an exterior intervention and it gives the operator
video of an approach rather than video of an entry. F5 is more robust, because it does not depend
on a human being awake.

**Recommend both if the budget allows.** If only one, take F4 first — but write down explicitly
that it converts a physical property into an operational commitment, and that nobody will
re-verify it in year three unless it is in a test procedure. Hand it to
[`../../18_Commissioning/`](../../18_Commissioning/) as a recurring test, not a one-time
acceptance item.

### F6 — The response lever and the boundary

```
   break-even  T_R  =  T_A − margin  =  540 − 120  =  420 s   (7 minutes)
```

Evaluate at exactly 420 s:

```
   margin  =  540 − 420  =  120 s
   verdict:  MARGINAL. 120 s remaining but 120 s of confidence margin was required.
```

`evaluate` uses `timely = margin > required_margin_s` — a **strict** inequality. Landing exactly
on your margin is reported as marginal, and marginal is treated as not timely.

**Defending that as a design choice:** the confidence margin exists because every input is an
estimate. A design that lands exactly on it has consumed the entire allowance for being wrong and
has nothing left. If the calculator reported that as timely, a designer could claim compliance at
the precise point where any error in any of six estimated task times makes the claim false. A
tool that answers a yes/no question about whether people get hurt should round toward the
uncomfortable answer.

### F7 — The fourth lever

**Reduce the consequence.** It is not a term in the timeliness inequality, which is exactly why
nobody proposes it — it does not appear on the diagram everybody is looking at.

Concretely at Meridian:

1. **Reduce on-hand inventory.** More frequent, smaller deliveries. The cage still gets breached
   in 240 s; there is a fraction as much in it. Cost: a logistics conversation, roughly zero
   capital.
2. **A certified safe inside the cage** for the highest-value SKUs. This adds delay *and* reduces
   what is reachable in one attempt. On the order of a few thousand dollars.
3. **Relocate the controlled inventory** to a facility that already has the response time.

Relative cost, order of magnitude: consequence reduction at ~$1–5k, versus cage hardening in the
tens of thousands, versus an on-site guard at roughly $190k/year. **And it is the only lever that
still helps after the system has failed** — the other three change the probability of interruption;
this one changes what an interruption failure costs.

The reason to put it in the memo even though the client will not choose it: it reframes the
meeting from "which product do we buy" to "how much loss are we buying down, and at what rate."
That is the conversation you want to be in.

### F8 — Three assumptions that would flip the verdict

1. **The task delay estimates**, especially 240 s to cut the cage mesh with a cordless angle
   grinder. `[PRACTICE][VERIFY]` These are illustrative. Real values come from tested penetration
   data for the specific construction, and a factor-of-two error here moves every result in Part
   F. **This is the one to spend money on first** — it is cheap (published penetration data, or a
   single supervised test on a sample panel), it is one-time, and *every other number in the
   analysis is downstream of it.* Reducing uncertainty at the root beats padding margins at the
   leaves.
2. **The 660 s response time is a contract figure, not a measurement.** It should be validated by
   unannounced timed tests, several of them, at the hours that matter — 3 a.m. on a Sunday, not
   2 p.m. on a Tuesday. Free to test, and contract figures are routinely optimistic.
3. **Detection probability is assumed to be 1.0.** The model has no `P_D` term at all. A fence
   sensor with a real-world `P_D` of 0.6, or a door contact that has been defeated with a magnet,
   silently invalidates the entire calculation while every number in it stays the same. This is
   the model's most dangerous limit, because nothing in the output hints that the assumption was
   made.

> A fourth, worth stating even though the exercise did not ask: **this is one path.** The adversary
> picks the weakest path, not the one you analysed. The roof, the dock doors during operating
> hours, and the office wing after hours are all separate analyses. A timely result on one path is
> not a timely system. See [`../../02_Risk_Assessment/`](../../02_Risk_Assessment/).

---

## Part G — The integration

### G1 — The dependency chain

```
   ┌──────────────────────────────────────────────────────────────────────┐
   │  A  optics                                                           │
   │     lens choice ──► pixel density ──► PASS/FAIL ──► CAMERA COUNT     │
   └──────────────────────────────┬───────────────────────────────────────┘
                                  │ 18 → 21 cameras
              ┌───────────────────┴──────────────────┐
              ▼                                      ▼
   ┌──────────────────────────┐          ┌───────────────────────────────┐
   │  B  bitrate & storage    │          │  C  PoE budget & ports        │
   │     count × duty × days  │          │     count × class allocation  │
   │     ──► TB ──► RAID raw  │          │     ──► SWITCH SPLIT          │
   └──────────────────────────┘          └───────────────┬───────────────┘
                                                         │ IDF location
                                                         ▼
                                          ┌───────────────────────────────┐
                                          │  D  voltage drop              │
                                          │     run length ──► CONDUCTOR  │
                                          └───────────────┬───────────────┘
                                                          │ same panel
                                                          ▼
                                          ┌───────────────────────────────┐
                                          │  E  battery & supply          │
                                          │     load list ──► Ah, A       │
                                          └───────────────────────────────┘

   ┌──────────────────────────────────────────────────────────────────────┐
   │  F  adversary path — the only part that does NOT take an input from  │
   │     A–E, and the only part that can invalidate all of them.          │
   └──────────────────────────────────────────────────────────────────────┘
```

Every place an earlier decision changed a later number:

| Decision in… | Changed in… | The change |
|---|---|---|
| A4: gate needs 2 cameras | B2 | peak +5.000 Mbps |
| A4 | B3 | raw storage +1.620 TB |
| A4 | C3 | IDF-2 from 270 W (73.0%) to 300 W (**81.1%**) — crossed the "tight" threshold |
| A4 | C4 | outdoor growth headroom from 3 cameras to **2** |
| A5: warehouse 6 → 8 | B2 | peak +4.635 Mbps |
| A5 | B3 | raw storage +0.751 TB |
| A5 | C3 | IDF-1 from 138.6 W to 169.4 W |
| B3+B5 | procurement | RAID 6 raw from 25.78 TB to **29.57 TB** |
| C3: IDF-1 stays in the office | D1 | 250 ft run to the cage — the cause of the conductor failure |
| E5: 24 h standby (if imposed) | enclosure, supply, charger | changes the *category* of the problem |

**Note the last row of the diagram.** Part F takes no input from Parts A–E, and yet an F verdict of
"not timely" means the video system is documenting a loss rather than preventing one. It is
possible to get every number in A–E right and build the wrong system. Run Part F **first** on the
next project.

### G2 — Tracing one camera through the whole design

**GATE-02**, the identification camera added by A4 — 30 fps, continuous, 24 h, 30 d, outdoor:

| Step | Value |
|---|---|
| Peak bandwidth | **+5.0000 Mbps** |
| Average bandwidth | **+5.0000 Mbps** (continuous, duty 1.0) |
| Raw storage, 30 d | **+1.6200 TB** |
| With 20% headroom | **+1.9440 TB** |
| RAID 6 raw, 8-disk | **+2.5920 TB** |
| Switch port | +1 on IDF-2 (10 of 24) |
| Switch power | **+30.0 W** (802.3at class) → IDF-2 from 270.0 W to 300.0 W |
| Switch split | Unchanged, but **utilisation crossed 73.0% → 81.1%**, raising the `POE BUDGET TIGHT` finding |
| C4 growth limit | Outdoor headroom fell from 100 W (3 cameras) to **70 W (2 cameras)** |

**WHSE-07**, one camera added by A5 — 10 fps, 50% duty, 30 d, indoor:

| Step | Value |
|---|---|
| Peak bandwidth | **+2.3173 Mbps** |
| Average bandwidth | **+1.1587 Mbps** |
| Raw storage, 30 d | **+0.3754 TB** |
| With 20% headroom | **+0.4505 TB** |
| RAID 6 raw, 8-disk | **+0.6006 TB** |
| Switch port | +1 on IDF-1 |
| Switch power | **+15.4 W** (802.3af) |
| Switch split | Unchanged, IDF-1 still at 45.8% |

**Why they cost differently:** GATE-02 costs **4.3× the storage** and **1.9× the switch power** of
WHSE-07. Storage, because it records continuously at 30 fps while the warehouse camera records at
10 fps on a 50% duty cycle — 5.0 Mbps × 24 h against 2.3173 Mbps × 12 h. Power, because it is a
heated outdoor unit that classifies 802.3at against an indoor unit at 802.3af.

**One camera is not one camera.** A schedule that prices by device count is wrong about both the
recorder and the switch, and the error is not small.

### G3 — Cutting the cage retention from 90 days to 30

```
   raw saving              =  4.860 − 1.620  =  3.240 TB
   with 20% headroom                          =  3.888 TB
   RAID 6, 8-disk, raw disk                   =  5.184 TB
   as a fraction of raw system storage        =  17.53%
```

Real money — 17.5% of the array for one camera's retention.

**Push back anyway:** R8 is a **regulatory** requirement per the client's own counsel `[VERIFY]`.
The saving is a one-time capital number in the low thousands. The exposure is a compliance finding
on controlled-substance inventory, which is not a security cost, is not bounded by the value of the
disk, and lands on the client's licence rather than on the security budget. Take the position in
writing, note it in the assumption register with the client's counsel named as owner, and let them
overrule you on the record if they choose to.

### G4 — Sensitivity versus confidence

**The number the design is most sensitive to:** the **task delay estimates in Part F**. They
determine a binary verdict — the system either interrupts the adversary or documents the loss —
and a 25% error in the cage breach time flips **both** recommended fixes on its own. Take 25% off
the hardened cage in F5 (600 s → 450 s) and the margin falls from 240 s to 90 s: marginal, treated
as not timely. Take the same 25% off the unhardened cage in F4 (240 s → 180 s) and its 135 s
margin falls to 75 s: also marginal. One estimate, made from illustrative data, is holding up
every conclusion in Part F.

**The number I am least confident in:** the **assumed bitrate**, 10.0 Mbps for 4 MP at 30 fps
H.264. `[PRACTICE]` Lesson 03 says it plainly: two vendors' calculators disagree by 2× on the same
camera, and this figure is scaled and multiplied through every storage number in Part B.

**They are not the same number, and the gap between them needs two different treatments:**

- The bitrate uncertainty is **presented, then retired**. Give the client the 15.5–35.5 TB range,
  specify a chassis with expansion bays so the architecture absorbs being wrong, and measure real
  bitrate in the first week of operation. Storage is continuous, so it can be sized as a range and
  corrected later without redesigning anything.
- The task-delay uncertainty **cannot be presented as a range**, because the output is a yes/no.
  "The system is 60% likely to be timely" is not something a client can act on. It must either be
  **reduced** — get tested penetration data for the actual cage construction — or **absorbed** by
  raising the confidence margin above 120 s, which costs real money in whichever lever you pick.

The general principle: **uncertainty in a continuous output can be carried; uncertainty in a
binary output must be retired.** Spend the investigation budget on the second kind. Most designers
do the reverse, because the continuous number is the one on the invoice.

### G5 — The basis of design memo

---

> **MEMORANDUM**
>
> **To:** Project Manager, Meridian Cold Chain
> **Re:** Building 4 security systems — basis of design and open items
> **Status:** For review. Three items below need your decision before we can issue for
> construction.

**1. What the system does**

Building 4 gets 21 cameras, access control on six openings, and an exterior detection layer at the
fence. The cameras cover the fence line, the vehicle gate, the dock apron, the warehouse floor, the
vault cage, and the lobby, each sized to the specific task you asked for — identifying a driver is
a different camera from watching the gate, and this design now reflects that. Recording is held 30
days for the site and 90 days for the vault cage. The access control system holds all six openings
locked through a four-hour power outage. The exterior detection layer exists so that a break-in is
detected while the intruder is still in the yard rather than after they are inside the building.

**2. Camera schedule — two corrections to the earlier drawing**

The draft schedule had two cameras specified to do jobs their lenses cannot do. Both are corrected
below at a total of three added cameras.

| | Issue | Correction |
|---|---|---|
| **Vehicle gate** | The single wide camera resolves about **33 pixels per foot** at the gate. Identifying a driver needs **76**. It would have shown that someone was there and nothing more. | Keep the wide camera for context and **add a second camera with a 12 mm lens** for driver identification (99.8 px/ft). One camera cannot do both jobs — a lens wide enough to see the gate cannot resolve a face at 60 ft. |
| **Warehouse floor** | Six cameras at 80 ft spacing give **17 px/ft**; the "observe activity" standard is **19**. | **Two additional cameras**, reducing spacing to 71 ft. Cheaper than the alternative of narrower lenses, which would have needed nine cameras, not eight. |

**3. Recording storage**

We are sizing the array at **22 TB** to hold 30 days, but the true figure depends on how busy your
scenes are and could land anywhere between **16 and 36 TB** — so we are specifying a chassis with
expansion bays, and we will measure real bitrate in the first week and tell you where you actually
landed.

At RAID 6 in an 8-disk group, 22 TB usable requires **29.6 TB of raw disk**.

Two things to know. First, disk is sold in decimal terabytes and your operating system will report
about **9% less** than the label — a 22 TB array shows as roughly 20 TiB. That is arithmetic, not a
shortfall. Second, **RAID is not a backup.** It survives two disk failures. It does not survive
fire, theft of the recorder, ransomware, or someone deleting footage. For the vault cage's 90-day
regulatory retention we recommend discussing an off-site copy as a separate item.

**4. Network switches and what "spare capacity" means**

Two 24-port PoE switches, split by geography: yard devices on the gatehouse switch, interior
devices on the office switch. A single switch does not work — the 21 cameras need 469 W and one
switch supplies 370 W.

> **The yard switch has fourteen empty ports but only enough power for two more outdoor cameras.
> If you add a third, we replace the switch.**

Please use that sentence rather than the port count when scoping future additions. Outdoor cameras
have heaters and reserve twice the power of an indoor camera.

**5. Cage gate wiring**

The cage gate lock is 250 ft of cable from the panel. At the drawn 18 AWG the lock receives
**10.07 V** against a **10.2 V minimum** — it would have worked intermittently and been diagnosed
as a software fault. We have specified **14 AWG** for that run.

> **On the drawing:** *"Cage gate lock home run: 14 AWG minimum. Sized for voltage drop over 250 ft
> at 0.45 A with the supply at its standby low of 11.6 V. Do not substitute a smaller conductor.
> Confirm actual routed length before pulling; re-calculate if it exceeds 440 ft."*

That note exists because this is the line item most likely to be substituted on site by someone
who reads the nominal 12 V and not the calculation.

**6. Power supply and battery** — *decision needed*

Selected: a **6 A** 12 VDC supply and a **12 Ah** battery, giving **8.0 hours** of standby against
your stated 4-hour requirement.

> **⚠ OPEN ITEM.** The four-hour figure is your requirement, not a code determination. If the AHJ
> requires **24 hours**, the battery goes to **46 Ah** — which changes the enclosure, may exceed
> the supply's charging capability, and needs coordination with the electrical contractor. **We
> need this closed before the enclosure is ordered.** `[CODE][VERIFY]`

**7. Detection timing — the finding that matters most** — *decision needed*

Against a defined two-person adversary with power tools, **the system as drawn does not detect
early enough to interrupt them.** The door contact alarms 375 seconds into a 915-second attack;
your patrol takes 660 seconds to arrive. **They finish and leave two minutes before anyone gets
there.**

Adding fence detection is the obvious fix and **it is not sufficient**. The binding constraint is
not the sensor — it is the 60 seconds it currently takes for a supervisor to reach a monitor and
assess the alarm. That 60 seconds is more than half the available detection budget.

> **Recommendation: change the monitoring arrangement so fence alarms call up video automatically
> at a continuously staffed position, cutting assessment to 30 seconds.** This makes the system
> timely with 135 seconds of margin. It requires no new hardware and no construction — it is a
> monitoring contract and a VMS configuration.

*The option we did not recommend, which you will probably want:* **hardening the cage** (CMU infill
and expanded metal, raising breach time to 600 seconds) also works, with more margin. It is
capital rather than recurring, and it does not depend on an operator being alert. We did not lead
with it because it costs an order of magnitude more and it leaves detection where it is — inside
the building, with the intruder already past the dock. **If the budget allows, do both.** If you
do only the monitoring change, note that it converts a physical protection into an operational
promise, and it needs to be on a recurring test schedule or it will quietly stop being true.

*A third option nobody proposes:* reduce what is in the cage. Smaller, more frequent deliveries, or
a certified safe inside the cage for the highest-value SKUs, costs a fraction of either option
above and is the only measure that still helps if the system fails.

**8. Assumption and verification register**

| # | Item | Basis | Owner | Needed by |
|---|---|---|---|---|
| 1 | Battery standby duration: 4 h vs 24 h | Client requirement; **not** a code determination. UL 294 / NFPA 72 as adopted | Meridian facilities + AHJ | Before enclosure order |
| 2 | 90-day vault retention | Client counsel, verbal | Meridian counsel | Before array purchase |
| 3 | Camera bitrate, 10.0 Mbps @ 4 MP 30 fps H.264 | Industry practice figure; vendors disagree by 2× | Design team — measure in week 1 | 30 days after cutover |
| 4 | Cage lock 10.2 V minimum, 0.45 A | Manufacturer datasheet, to be attached | Design team | With submittal |
| 5 | Switch PoE allocation: static or dynamic | Not yet confirmed from datasheet | Design team | Before switch order |
| 6 | Camera heater draw at design low temperature | Not yet confirmed from manufacturer | Design team | Before switch order |
| 7 | Adversary task delay times | **Illustrative**, not tested penetration data | Meridian security + design team | Before Item 7 decision |
| 8 | Patrol response time, 660 s | Contract figure, never measured | Meridian security | Before Item 7 decision |
| 9 | Detection probability assumed 1.0 | Model limitation — no P_D term | Design team, to state in report | With final report |
| 10 | Single adversary path analysed | Roof, dock doors in hours, office wing not yet analysed | Design team | Phase 2 |
| 11 | Sensor dimensions 5.37 × 3.02 mm | Typical for format; confirm per datasheet | Design team | With submittal |
| 12 | Adopted code edition and AHJ | Not yet determined | Meridian + design team | Before IFC |

> Items **1, 2, and 7** need your decision. Items 5, 6, 7 (verification), 8, and 12 are ours to
> close and are scheduled. Items 9 and 10 are limitations we are stating, not closing.

---

## Marking guide

| Part | Full marks looks like |
|---|---|
| A | Both failures found, GATE quantified at 56.6%, the 9 mm rounding trap caught, WHSE floor-vs-slant conversion done correctly, and A6's "cheap fix is more expensive" reasoning shown |
| B | Correct order of operations on bitrate, storage presented as a range with the client sentence, 9.051% gap explained as a unit conversion, 96 TB → 16.5 days |
| C | Both constraints identified as independent in C2, growth stated in cameras not watts in C4, C5's surviving port finding noticed |
| D | Both segments computed separately, the `smallest_awg_for_run` trap caught, the drop budgeted backwards from the load, 11.6 V recheck driving the 14 AWG recommendation |
| E | Peak-vs-standby pair explained physically, E5's three non-calculable consequences named, E6 answered "it does not matter here" with the reason |
| F | F3's failure explained via the assessment term, F4 found without hardware, F6's strict inequality defended, F8 prioritising the task-delay data |
| G | The dependency table populated, G2's two cameras compared with numbers, G4 distinguishing sensitivity from confidence, and a memo an actual PM could act on |

A submission that computes every value correctly and never states that the design does not work
has missed the exercise.

---

## Verification

Every figure above was produced by:

```bash
python3 28_Calculators/tests/test_psec.py      # 68 tests, all passing
python3 28_Calculators/demo.py                 # 8 worked examples
```

with the site model built from `psec.optics`, `psec.video`, `psec.power`, and `psec.pps` directly.
If you rebuild it and get different numbers, the disagreement is worth more than the agreement —
find it.
