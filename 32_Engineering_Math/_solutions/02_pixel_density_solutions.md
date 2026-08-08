# Solutions — 02 Pixel Density and DORI

---

## P2.1 — 4 MP camera, 1/1.8" sensor, 6 mm lens

2688 × 1520 px, `w` = 7.20 mm, `f` = 6 mm.

**(a) At 25 ft**
```
   W    = 25 × 7.20 / 6.0  =  30.000 ft
   PPF  = 2688 / 30.0      =  89.600 px/ft
```
89.6 PPF — comfortably **identify** class (≥ 76).

**(b) Maximum range per class**

```
   D_max = px · f / (PPF · w)  =  2688 × 6 / (PPF × 7.20)  =  16128 / (7.2 · PPF)
```

| Class | PPF | D_max |
|---|---|---|
| Detect | 8 | **280.0 ft** |
| Observe | 19 | **117.9 ft** |
| Recognise | 38 | **58.9 ft** |
| Identify | 76 | **29.5 ft** |

**(c) The halving pattern**

| Step | Ratio |
|---|---|
| Detect → Observe | 280.0 / 117.9 = **2.375** |
| Observe → Recognise | 117.9 / 58.9 = **2.000** |
| Recognise → Identify | 58.9 / 29.5 = **2.000** |

The last two are **exactly** 2.000, because `D_max ∝ 1/PPF` and the table values are exactly
double each other: 19 → 38 → 76.

**The first step is 2.375, not 2.5, and the reason is the rounding.** In the IEC px/m figures the
ratio is 62.5 / 25 = **2.5**. The calculator's per-foot table rounds detect *up* (7.62 → 8.0) and
observe *down* (19.05 → 19.0), which compresses that first step to 19/8 = 2.375.

So the answer to "where does it not hold exactly, and why" is: **the detect→observe step, because
the rounding in `DORI_PPF` is not uniform in direction.** Everything else is exact by construction.
Hold that thought for P2.7.

---

## P2.2 — Deriving `D_max`

```
   Start:        PPF = px / W                              (definition)
   Substitute:   W   = D · w / f                            (lesson 01)

                 PPF = px / (D · w / f)
                     = px · f / (D · w)                     ← combined form

   Solve for D:  PPF · D · w = px · f
                 D = px · f / (PPF · w)                     ← D_max
```

**Verification, 1920 px, 76 PPF, 5.37 mm, 4 mm:**

```
   D_max = (1920 × 4.0) / (76.0 × 5.37)
         = 7680 / 408.12
         = 18.818 ft
```

**Forward check:**
```
   W   = 18.818 × 5.37 / 4.0  =  25.263 ft
   PPF = 1920 / 25.263        =  76.000  ✅
```

Exact round-trip. This is the pattern `test_max_range_is_consistent_with_forward_calc` encodes:
an inverse that doesn't round-trip isn't an inverse.

---

## P2.3 — Recognise at 60 ft with a 2 MP camera

**(a) Required focal length**

Rearranging `D_max = px·f/(PPF·w)` for `f`:

```
   f  =  PPF · w · D / px
      =  38.0 × 5.37 × 60 / 1920
      =  12243.6 / 1920
      =  6.377 mm
```

**(b) Scene width at 60 ft with that lens**

```
   W  =  60 × 5.37 / 6.377  =  50.53 ft
```

Cross-check: `1920 / 50.53 = 38.0 PPF` ✅

**(c) Does it work for a 40 ft scene?**

**No, and it fails in the direction people don't expect.** The lens that delivers exactly 38 PPF at
60 ft covers **50.5 ft** of scene — that is 10.5 ft *more* than you need. You aren't short of
coverage; you're **wasting pixels on scene you don't care about.**

Realistically you'd fit an available lens. Options at 60 ft:

| Lens | Scene width at 60 ft | PPF at 60 ft | Recognise range |
|---|---|---|---|
| 6 mm | 53.70 ft | **35.75** ❌ | 56.5 ft |
| 8 mm | 40.28 ft | **47.67** ✅ | 75.3 ft |
| 12 mm | 26.85 ft | **71.51** ✅ | 112.9 ft |

**Option 1 — the 8 mm lens.** Covers 40.28 ft, which matches the 40 ft requirement almost exactly,
and delivers 47.7 PPF, comfortably above the 38 needed. **This is the answer.**
*Cost:* none. It is simply the right lens, and the fact that the "required" 6.377 mm figure sat
between available sizes was never the real constraint — the 40 ft scene width was.

**Option 2 — the 6 mm lens.** Covers the scene with room to spare but delivers only 35.75 PPF,
**below the recognise threshold.** It would be classified "observe."
*Cost:* you miss the requirement by 6%, which is close enough to be argued about and far enough to
be wrong. Don't.

> 🧠 **The lesson buried in this problem:** the question gave you a *range* requirement and a
> *scene width* requirement, and they interact. Solving for the range requirement alone produced a
> lens that was wrong for the scene. **Always solve both, then pick the lens that satisfies the
> binding one** — here, scene width. Lesson 01's P1.3 made the same point from the other
> direction.

---

## P2.4 — Identification at a gate 40 ft away

**What they have:** 2 MP (1920 px), 4 mm, 1/2.8" (5.37 mm).

```
   W@40   = 40 × 5.37 / 4.0    =  53.7 ft
   PPF@40 = 1920 / 53.7        =  35.75 px/ft   →  class: recognise (barely)
```

**What they need:** 76 PPF for identify.

```
   Identify range with current setup:  D_max = 7680 / 408.12 = 18.8 ft
```

**They are asking for identification at 40 ft from a camera that stops identifying at 18.8 ft.**
They have less than half the range they need, and they're currently getting *recognise* — which
sounds close and is a factor of 2 away.

**Three options:**

**Option A — Change the lens. `f = 76 × 5.37 × 40 / 1920 = 8.50 mm`.**
Fit an 8 mm lens (giving 71.5 PPF, just under) or a 12 mm (107 PPF, comfortable).
*Consequence:* the scene narrows hard. At 40 ft, a 12 mm lens sees **26.85 ft**, down from 53.7 ft.
You have converted a wide gate overview into a narrow identification shot. If the gate is 30 ft
wide, this no longer covers it, and you have traded one problem for another.
*Cost:* a lens. Cheapest option by far if the narrow view is acceptable.

**Option B — Add pixels. `px = 76 × 40 × 5.37 / 4.0 = 4081 px` horizontal.**
That is a 4K camera (3840 px) and still slightly short; 4K gets you 71.5 PPF at 40 ft, essentially
the same as the 8 mm option but *keeping the wide view*.
*Consequence:* roughly 3× the bandwidth and storage (lesson 03), higher camera cost, and smaller
photosites — worse low-light performance at a gate that probably matters most at night.
*Cost:* the camera, plus recurring storage.

**Option C — Move the camera, buy no hardware.**
`D_max` for identify is 18.8 ft. If a mounting point exists within ~18 ft of where people actually
present themselves — a gate pedestal, a call box, an existing pole closer to the lane — the
current camera identifies there today.
*Consequence:* requires a mounting location and a conduit run; may need a second camera to retain
the wide view. But it costs no camera and no bandwidth, and it is the option that most often turns
out to be available once someone actually walks the site.

**Recommendation:** walk the site for Option C first, then A if the narrow view is acceptable,
then B. The order is deliberate: **the cheapest fix for a range problem is usually to shorten the
range**, and it is the one nobody proposes because it isn't on a price list.

---

## P2.5 — "200 ft range" vs. "19 ft"

Model answer (138 words):

> Both numbers are right; they're answering different questions.
>
> A camera doesn't have a range — it has a range *per task*. The vendor's 200 feet is the distance
> at which the camera can tell you *something is there*: a person-shaped object moving across the
> lot. That's a real and useful capability, and it's the biggest number available, so it's the one
> that goes on the datasheet.
>
> My 19 feet is the distance at which the image carries enough detail to **identify** someone —
> meaning a person who has never met them could say who it is from the video, in front of a jury.
> That takes about ten times the pixels on the subject.
>
> Same camera, same lens. Detect at 200 feet, recognise at 38, identify at 19.
>
> So the question to ask any vendor is: "at what task?"

**What makes it work:** it doesn't accuse the vendor of lying, because they aren't. It names the
mechanism (pixels on subject), gives the evidentiary framing for why identify is the bar that
matters, and hands the director a question they can use on the next vendor call — which is worth
more than the explanation.

---

## P2.6 — 🧮 Coverage table, camera at 14 ft

1920 px, 4 mm, 5.37 mm sensor, target plane 5 ft, so `Δh = 9 ft`.

| Floor D | Slant S | Scene W | PPF | Class | Depression φ |
|---|---|---|---|---|---|
| 8 ft | 12.042 ft | 16.166 ft | **118.77** | identify | **48.37°** |
| 20 ft | 21.932 ft | 29.443 ft | **65.21** | recognise | 24.23° |
| 50 ft | 50.804 ft | 68.204 ft | **28.15** | observe | 10.20° |

Working, first row:
```
   S   = √(8² + 9²) = √145 = 12.042 ft
   W   = 12.042 × 5.37 / 4.0 = 16.166 ft
   PPF = 1920 / 16.166 = 118.77
   φ   = arctan(9/8) = 48.37°
```

**One sentence per row — what the camera can actually be relied on to do:**

**At 8 ft:** *Nothing that needs a face.* The arithmetic says identify at 118.8 PPF, and the
depression angle is 48°, well past the ~30° heuristic — this camera is photographing the top of
someone's head with excellent resolution. **This row is the trap in the whole problem set:** the
PPF column and the class column both look outstanding, and the geometry has already thrown away
the feature you needed.

**At 20 ft:** *Recognition of someone already known, plausibly.* 65 PPF is solidly recognise, and
24° depression is inside the heuristic. This is the row where the camera is doing real work.

**At 50 ft:** *Observation only — what someone is doing, not who they are.* 28 PPF, and the
shallow 10° angle is fine but irrelevant, because there aren't enough pixels for a face regardless.

> 🧠 **The point of this problem:** the PPF column read alone says the camera is best at 8 ft and
> worst at 50 ft, which is true and useless. Read with the depression column, the camera's usable
> identification band starts somewhere past 15 ft and ends before the pixels run out around 19 ft
> — **a narrow window that neither column reveals on its own.** This is why
> `coverage_report` emits both, and why a coverage diagram with only range rings is an incomplete
> deliverable.

---

## P2.7 — Should `DORI_PPF` round uniformly?

**The situation.** Exact conversions: 7.62, 19.05, 38.10, 76.20. The table: 8.0, 19.0, 38.0, 76.0.
Detect rounds up by 0.38; the rest round down by 0.05, 0.10, 0.20.

**The case for making them uniform (round all down, or use exact values):**

1. **The class ratios break.** As P2.1 showed, the exact px/m criteria are spaced exactly 2.5×,
   2×, 2× — and the current table makes detect→observe 2.375×. Anyone reasoning from "each class
   is roughly double" gets a slightly wrong answer at the one boundary where the rounding is
   largest.
2. **Detect is rounded in the *conservative* direction while the others are rounded in the
   *permissive* direction.** That's an inconsistency in posture, not just in arithmetic: the table
   makes detect harder to achieve than the standard requires and the other three marginally
   easier.
3. **Uniform rules are easier to defend** when someone asks where the numbers came from.

**The case for leaving it (which is what the code does):**

1. **8 is what practice uses.** The rounded per-foot values are the figures that appear in real
   design conversations, and matching them means the calculator agrees with the room. A tool that
   reports 7.62 invites an argument about a number nobody cares about.
2. **The precision is false anyway.** All four figures are threshold criteria for human visual
   tasks under "good conditions." The difference between 7.62 and 8.0 PPF is far inside the
   uncertainty of the underlying criterion, and pretending otherwise is the actual error.
3. **The 0.38 discrepancy at detect is 5%** — real, but detect is the class where nothing important
   turns on the boundary. You do not build an evidentiary case on detect-class imagery.

**My position:** leave it, and **document the asymmetry in the table comment** so the next reader
doesn't discover it by getting 2.375 and wondering what they did wrong. The code already flags the
values as converted-and-rounded-to-practice; adding one line noting that the rounding direction
differs would close the gap. That's a comment change, not a code change.

**What I'd change in the test if I changed the table:**

`test_dori_table_matches_iec_conversion` currently asserts `|DORI_PPF[k] − DORI_PPM[k]/3.28084| < 0.5`.
The 0.5 tolerance exists precisely to permit the current rounding.

- **If I moved to exact conversions**, the assertion should become an equality to within floating
  point (`assertAlmostEqual(..., places=6)`), and the test would then be verifying a pure unit
  conversion — which is close to testing that division works, so I'd also want a separate test
  pinning the px/m source values against the standard.
- **If I moved to uniform downward rounding** (7.6, 19.0, 38.1, 76.2 → or 7, 19, 38, 76), I would
  **tighten the tolerance to 0.15** so that the test actually constrains the rounding rather than
  permitting anything within half a pixel. A tolerance loose enough to admit any plausible value
  isn't testing much.
- Either way I would **add a test asserting the class ratios**, since P2.1 showed that's the
  property a designer actually reasons with and nothing currently protects it.

> 🧠 The general habit: **when a test's tolerance is doing real work, know what it is permitting.**
> The 0.5 here is not sloppiness — it is a deliberate statement that the table may deviate from
> the exact conversion by up to half a pixel per foot. Changing the table means revisiting that
> statement, not just the numbers.
