# 02 — Pixel Density and DORI

> Derives the pixel-density half of
> [`../28_Calculators/psec/optics.py`](../28_Calculators/psec/optics.py). Continues directly from
> [lesson 01](01_camera_fov.md) — you need `W = D·w/f` before anything here makes sense.

## Learning objectives

- Derive pixel density from the FOV width, and then derive the combined form that skips it.
- Explain why pixel density falls as `1/D` and not as `1/D²`, and why that distinction is not
  pedantic.
- Invert the relationship to get the maximum range at which a camera meets a stated task.
- Explain what DORI is, where the numbers come from, and why the per-foot table in the calculator
  is deliberately **not** the exact metric conversion.
- Recognize that `D_max ∝ px · f` — so resolution and focal length trade against each other for
  range, and *not* for coverage.
- State what pixel density does not tell you.

---

## Derivation 1 — Pixel density

Pixel density is a rate: how many horizontal pixels land on each foot of scene.

```
   ┌────────────────────────────┐
   │   PPF  =  px  /  W         │
   └────────────────────────────┘

   px = horizontal pixel count of the sensor
   W  = scene width in feet at the target distance
```

That's it. The whole formula.

### 🧮 Worked example 2.1 — the test case

The lesson 01 camera: 1920 horizontal pixels, 1/2.8" sensor (5.37 mm), 4 mm lens, target at 50 ft.

From lesson 01, `W = 67.125 ft`.

```
   PPF  =  1920 / 67.125  =  28.603 px/ft
```

**28.60 PPF.** This is `test_pixel_density`.

---

## Derivation 2 — The combined form

Substituting lesson 01's `W = D·w/f`:

```
   PPF  =  px / W
        =  px / (D · w / f)
        =  px · f / (D · w)

   ┌────────────────────────────────┐
   │   PPF  =  ( px · f ) / (D · w) │
   └────────────────────────────────┘
```

**Read what this says.** Pixel density is:

| Proportional to | Inversely proportional to |
|---|---|
| **px** — sensor resolution | **D** — distance to target |
| **f** — focal length | **w** — sensor width |

Two of those are counterintuitive:

**A *bigger* sensor gives *lower* pixel density, all else equal.** Because a bigger sensor sees a
wider scene through the same lens, spreading the same pixels over more feet. Sensor size buys you
light-gathering, not detail. People assume the opposite constantly.

**Density falls as `1/D`, not `1/D²`.** See below — this one matters enough to have its own
section.

---

## Why `1/D` and not `1/D²`

Everyone arrives here with inverse-square intuition from lighting and RF. It is wrong for pixel
density, and knowing *why* is what keeps you from misapplying it.

```
   Pixels per square foot   →  falls as 1/D²   (an AREA measure)
   Pixels per foot          →  falls as 1/D    (a LINEAR measure)
```

Doubling the distance doubles both the width and the height of the scene, so the *area* covered
quadruples and pixels-per-area drops by four. But **DORI is a linear criterion.** What determines
whether you can recognise a face is how many pixels span it horizontally — a linear dimension. So
the relevant rate is pixels per foot, and that halves.

**The practical consequence:** range degrades more gently than people expect. Doubling the
distance costs you one DORI class (roughly — the classes are spaced about 2× apart), not two.
That is a useful thing to know when someone proposes moving a camera back 20 ft to make a sightline
work.

> ⚠️ **The corollary that catches people:** because the classes are spaced roughly 2× apart in PPF
> and density falls as `1/D`, **each DORI class boundary is roughly half the range of the one
> below it.** Identify range is about half of recognise range, which is about half of observe
> range. See worked example 2.3 — the numbers fall out almost exactly that way, and you can use it
> as a mental check on any coverage table someone hands you.

---

## Derivation 3 — Maximum range for a task

The design direction. You know the task, so you know the PPF you need. What you want is the
distance beyond which the camera stops delivering it.

Solve `PPF = px·f / (D·w)` for `D`:

```
   ┌──────────────────────────────────────┐
   │   D_max  =  ( px · f ) / (PPF · w)   │
   └──────────────────────────────────────┘
```

### 🧮 Worked example 2.2 — the test case

1920 px, target 38 PPF (recognise), 5.37 mm sensor, 4 mm lens.

```
   D_max  =  (1920 × 4.0) / (38.0 × 5.37)
          =  7680 / 204.06
          =  37.636 ft
```

**Beyond 37.6 ft this camera no longer supports recognition.** This is `test_max_range_for_ppf`.

**Check it round-trips** — this is `test_max_range_is_consistent_with_forward_calc`:

```
   W    = 37.636 × 5.37 / 4.0  =  50.526 ft
   PPF  = 1920 / 50.526        =  38.000  ✅
```

**This is the number to put on a coverage diagram.** Not the camera's "range" — cameras don't have
a range, they have a range *per task*.

### 🧮 Worked example 2.3 — the four ranges of one camera

Same 2 MP camera, 4 mm lens, 1/2.8" sensor:

| Task | PPF target | D_max = 1920 × 4 / (PPF × 5.37) |
|---|---|---|
| Detect | 8 | **178.8 ft** |
| Observe | 19 | **75.3 ft** |
| Recognise | 38 | **37.6 ft** |
| Identify | 76 | **18.8 ft** |

**One camera, four different ranges.** Note the halving: 178.8 → 75.3 → 37.6 → 18.8. Each class
costs you roughly half your range, exactly as the `1/D` relationship predicts.

> 🧠 **This table is the single most useful artifact in camera design, and it is why "how far does
> this camera see?" is not an answerable question.** When a client or a vendor states a camera's
> range as one number, the first question is *"at what task?"* The answer is almost always
> "detect," because it's the biggest number.

---

## The `px · f` insight

Look at `D_max = px·f / (PPF·w)` again. **Resolution and focal length enter the same way — as a
product.** So for range purposes they are interchangeable:

```
   1920 px @ 4 mm  →  identify at 18.8 ft
   3840 px @ 4 mm  →  identify at 37.6 ft     (double the pixels)
   1920 px @ 8 mm  →  identify at 37.6 ft     (double the focal length)
```

**Identical range. Completely different designs.**

| | 4K at 4 mm | 2 MP at 8 mm |
|---|---|---|
| Identify range | 37.6 ft | 37.6 ft |
| Scene width at 37.6 ft | **50.5 ft** | **25.3 ft** |
| Horizontal AOV | 67.7° | 36.9° |
| Cost | Higher camera cost | Higher camera count |
| Bandwidth and storage | ~3× (lesson 03) | Baseline |
| Low light | Worse — smaller pixels on the same sensor | Better |

**More pixels buys range *and keeps the wide view*. More focal length buys range *by giving up the
wide view*.** They are not substitutes; they are opposite trades that happen to produce the same
number in this one equation.

> 🧠 **The senior read:** "just use 4K" is a real answer and it is not free — it costs roughly 3×
> the bandwidth and storage (lesson 03), and it puts smaller photosites on the sensor, which costs
> low-light performance exactly where security video matters most. The right question is not which
> is better but which constraint is binding: **if you're short on range, add pixels; if you're
> short on pixels-on-target for a narrow scene, add focal length; if you're short on both, add a
> camera.**

---

## DORI: where the numbers come from

`[STANDARD]` **IEC 62676-4** defines four operational criteria in **pixels per metre**:

| Class | px/m | The question it answers |
|---|---|---|
| **D**etect | 25 | "Is something there?" |
| **O**bserve | 62.5 | "What is it doing?" |
| **R**ecognise | 125 | "Is that someone I know?" |
| **I**dentify | 250 | "Who is that, to a viewer who has never met them?" |

`[VERIFY current edition]`

**Note the distinction between recognise and identify**, because it is the one that gets blurred in
sales conversations. *Recognise* means a viewer who already knows the person can pick them out.
*Identify* means a stranger — a juror, an investigator — can establish who it is from the image
alone. That is a much higher bar and it is the one that matters for evidence.

### Converting to pixels per foot

```
   1 m  =  3.280839895 ft

   px/ft  =  px/m  /  3.280839895
```

| Class | px/m | Exact px/ft | `DORI_PPF` in the calculator |
|---|---|---|---|
| Detect | 25 | 7.620 | **8.0** |
| Observe | 62.5 | 19.050 | **19.0** |
| Recognise | 125 | 38.100 | **38.0** |
| Identify | 250 | 76.200 | **76.0** |

**The table is rounded, deliberately, and not always in the same direction.** Detect rounds *up*
from 7.62 to 8; the other three round *down*. These are the values used in common practice, and
`test_dori_table_matches_iec_conversion` asserts only that each is within 0.5 of the exact
conversion.

**Why round at all, and why is a loose tolerance the right test?**

Because the precision is false. These are threshold criteria for human visual tasks under
"good conditions," derived from testing, and the real boundary between recognising someone and not
is not a sharp line at 125.0 px/m. Carrying 38.1 px/ft through a design implies a confidence the
underlying criterion does not have. **A test that demanded exact conversion would be encoding
precision that isn't in the source.**

> 🧠 This is a general habit worth taking from this lesson: **match your significant figures to
> your weakest input.** If the criterion is soft, the derived number is soft, and reporting
> "identify range: 18.82 ft" invites a client to believe something about foot 18.8 that isn't
> true. Report 19 ft, or "roughly 19 ft," and say what it rests on.

### Classification boundaries

`classify_ppf` returns the **highest class met**, using `>=`:

```
   ppf ≥ 76  →  "identify"
   ppf ≥ 38  →  "recognise"
   ppf ≥ 19  →  "observe"
   ppf ≥ 8   →  "detect"
   otherwise →  "below detect"
```

`test_classify_ppf_boundaries` pins the edges: 76 → identify, **75.9 → recognise**, 38 → recognise,
19 → observe, 8 → detect, **7.9 → below detect**.

The `>=` semantics matter: the DORI figures are **minima for the stated task**, so meeting the
number exactly counts as meeting it. And "below detect" is a real, named category rather than an
error — a camera can absolutely be pointed at something it cannot resolve at all, and the report
should say so plainly.

---

## Putting it together: the coverage report

`CameraSpec.coverage_report` chains everything from both lessons: slant range → FOV width → pixel
density → class, plus the depression angle.

### 🧮 Worked example 2.4 — the test case

`CameraSpec("CAM-1", 1920×1080, "1/2.8", 4.0 mm, mount 9.0 ft)`, target plane 5 ft.

**Megapixels:** `1920 × 1080 / 1,000,000 = 2.0736 MP` — this is `test_camera_spec_report`.

At a floor distance of 10 ft:

```
   Δh   = 9 − 5 = 4 ft
   S    = √(10² + 4²) = √116 = 10.770 ft
   W    = 10.770 × 5.37 / 4.0 = 14.46 ft
   PPF  = 1920 / 14.46 = 132.8
   φ    = arctan(4/10) = 21.8°
   class = identify
```

The full table:

| Floor D | Slant S | Scene W | PPF | px/m | Class | Depression |
|---|---|---|---|---|---|---|
| 10 ft | 10.8 ft | 14.5 ft | **132.8** | 435.7 | identify | 21.8° |
| 30 ft | 30.3 ft | 40.6 ft | **47.3** | 155.0 | recognise | 7.6° |
| 60 ft | 60.1 ft | 80.7 ft | **23.8** | 78.0 | observe | 3.8° |

**PPF falls monotonically with distance** — `test_camera_spec_report` asserts exactly this, and it
is the cheapest possible sanity check on any coverage table. If density ever *rises* with
distance, something is inverted.

**Read the depression column too.** At 10 ft the geometry is 21.8°, inside the 30° heuristic from
lesson 01, so the "identify" classification is geometrically plausible. Had the camera been at
16 ft instead of 9 ft, the depression at 10 ft would be 47.7° and the identify classification would
be arithmetically true and practically worthless. **The PPF column and the depression column have
to be read together.**

---

## What pixel density does not tell you

`[PRACTICE]` Pixel density is a **necessary condition, not a sufficient one.** The geometric pixel
count is an upper bound on usable detail. Everything below reduces it, and none of it appears in
the arithmetic:

| Factor | What it costs you |
|---|---|
| **Lighting** | The dominant one. A camera meeting 80 PPF in daylight may resolve nothing at 2 lux. |
| **Lens MTF** | Cheap optics don't deliver the sensor's resolution to the sensor |
| **Focus error** | Especially on varifocal lenses adjusted once, on a ladder, in daylight |
| **Motion blur** | A walking subject at a slow shutter smears across several pixels |
| **Compression** | The codec throws away detail, and it throws away *more* in exactly the noisy low-light scenes where you had least to spare (lesson 03) |
| **Depression angle** | Lesson 01 — geometry can remove the feature entirely |
| **WDR / backlight** | A silhouetted subject against a bright door has pixels and no information |

> ⚠️ **The failure this produces:** a coverage diagram showing green "identify" zones, signed off
> by everyone, over a system that identifies nobody at night. The diagram was not wrong. It was
> answering a narrower question than the client thought it was answering. **Label your coverage
> diagrams with their assumptions** — "geometric pixel density, daylight, static subject" — and
> the conversation changes.

---

## Common mistakes

⚠️ **Applying inverse-square intuition.** PPF falls as `1/D`.

⚠️ **Quoting a camera's "range" as one number.** Range is per task.

⚠️ **Assuming a bigger sensor means more pixel density.** It means less, all else equal.

⚠️ **Treating recognise and identify as synonyms.** Identify is the evidentiary bar and it is 2×
the pixels.

⚠️ **Reporting derived figures to more significant digits than the criterion supports.**

⚠️ **Using floor distance instead of slant range** (lesson 01) — inflates PPF worst at short range.

⚠️ **Reading the PPF column without the depression column.**

⚠️ **Presenting geometric pixel density as a performance guarantee.**

---

## Junior vs. Senior

**Junior:** derives PPF and `D_max`; produces a four-class range table for a camera; knows the DORI
figures and that they are minima; uses slant range.

**Senior:** knows `D_max ∝ px·f` and can therefore reason about whether a range problem should be
solved with resolution, focal length, or another camera — and knows those three have different
bandwidth, cost, and low-light consequences; rounds derived numbers to the precision the criterion
actually supports; reads PPF and depression together; labels every coverage diagram with the
conditions it assumes; and says out loud that the diagram describes daylight geometry, not
performance.

---

## Problem set

**P2.1** A 4 MP camera (2688 × 1520) on a 1/1.8" sensor (7.20 mm) with a 6 mm lens.
- (a) Compute the scene width and PPF at 25 ft.
- (b) Compute the maximum range for each DORI class.
- (c) Verify the halving pattern between classes. Where does it not hold exactly, and why?

**P2.2** Derive `D_max = px·f / (PPF·w)` from `PPF = px/W` and `W = D·w/f`, showing every step.
Then verify your result for 1920 px, 76 PPF, 5.37 mm, 4 mm by computing `D_max` and then working
forward to confirm the PPF at that distance.

**P2.3** You need **recognise** class (38 PPF) at 60 ft with a 2 MP camera (1920 px) on a 1/2.8"
sensor.
- (a) What focal length is required?
- (b) What is the scene width at 60 ft with that lens?
- (c) The scene you must cover is 40 ft wide. Does this work? If not, state your two options and
  the cost of each.

**P2.4** A client has 2 MP cameras with 4 mm lenses and wants identification at the property gate,
40 ft from the nearest mounting point. Compute what they have and what they need, then give three
distinct engineering options with their consequences. One of your options must not involve buying
a camera.

**P2.5** Explain, in under 150 words to a facilities director, why the camera vendor's claim of
"200 ft range" and your report's claim of "19 ft" are both true.

**P2.6** 🧮 A camera is mounted at 14 ft. Compute PPF at floor distances of 8, 20, and 50 ft for a
1920 px camera with a 4 mm lens on a 5.37 mm sensor, using slant range and a 5 ft target plane.
Then compute the depression angle at each. Produce the coverage table, classify each row, and
write one sentence per row saying what the camera can actually be relied on to do there.

**P2.7** The `DORI_PPF` table rounds detect *up* (7.62 → 8.0) and the others *down*. Argue for or
against making all four round the same direction. What would you change in the test if you changed
the table?

> Answers: [`_solutions/02_pixel_density_solutions.md`](_solutions/02_pixel_density_solutions.md)

---

## Retrieval check

1. Write both forms of the pixel density equation.
2. Why does PPF fall as `1/D` rather than `1/D²`?
3. Write `D_max` and say what you use it for.
4. State the four DORI classes and their px/m figures.
5. What is the difference between recognise and identify, and why does it matter for evidence?
6. Why is the calculator's per-foot table not the exact metric conversion?
7. What does `D_max ∝ px·f` let you trade, and what does it *not* let you trade?
8. Name four things that reduce usable detail below the geometric pixel count.

---

## References

- IEC 62676-4 — video surveillance systems, application guidelines; the source of DORI.
  `[STANDARD][VERIFY current edition]`
- [`../28_Calculators/psec/optics.py`](../28_Calculators/psec/optics.py) — the implementation.
- [`../28_Calculators/tests/test_psec.py`](../28_Calculators/tests/test_psec.py) — `TestOptics`.
- [`01_camera_fov.md`](01_camera_fov.md) — the geometry this lesson builds on.
- [`../03_Video_Surveillance/`](../03_Video_Surveillance/) — application, including when to design
  above the DORI minima and why *(not yet written — see
  [`../COURSE_PROGRESS.md`](../COURSE_PROGRESS.md))*.

**Next:** [03 — Video Bandwidth](03_bandwidth.md)
