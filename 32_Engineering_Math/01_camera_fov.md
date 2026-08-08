# 01 — Camera Field of View and Focal Length

> **This lesson derives what [`../28_Calculators/psec/optics.py`](../28_Calculators/psec/optics.py)
> implements.** Every expected value in `TestOptics`
> ([`../28_Calculators/tests/test_psec.py`](../28_Calculators/tests/test_psec.py)) is worked here
> by hand. **If a test ever fails after a formula change, redo the hand calculation — do not
> change the test.** The test is the record of the derivation and this lesson is its prose.

## Learning objectives

- Derive the angle-of-view formula from the pinhole geometry, rather than looking it up.
- Derive the field-of-view width formula from similar triangles, and explain why an equation
  mixing millimetres and feet is dimensionally sound.
- Invert the FOV equation to get the lens you actually need — the direction you use in design.
- Compute slant range and depression angle, and explain why ignoring them overstates coverage
  for every indoor camera.
- State the assumptions the model rests on and name the situations where it silently stops being
  true.

---

## Why derive it at all

You already have a working calculator. Three reasons to do this anyway:

1. **A calculator you can't derive is a calculator you can't debug.** When a vendor's tool
   disagrees with yours by 30%, you need to know which one is wrong, and the only way is to know
   what the formula is doing.
2. **The design direction is the inverse.** The calculator gives you coverage from a lens; a
   designer needs the lens from required coverage. That inversion is trivial once you can see the
   equation and impossible to remember as a lookup.
3. **The assumptions are where the money is.** Every formula here is exactly true for an idealized
   lens and approximately true for a real one. Knowing *which* approximation you're standing on
   tells you when to stop trusting the number.

---

## The model: a pinhole

Treat the lens as a single point. Light from the scene passes through it and lands on the sensor.
That is the **thin-lens** or **pinhole** model, and it is the whole basis of the arithmetic.

```
        SENSOR                LENS                    SCENE
       (w mm wide)          (pinhole)             at distance D
            │                   │                       │
       ┌────┼────┐              │                  ┌────┼────┐
       │    │    │              │                  │    │    │
       │    ·────┼──────────────●──────────────────┼────·    │
       │    │    │             ╱ ╲                 │    │    │
       └────┼────┘            ╱   ╲                │    │    │
            │                ╱     ╲               └────┼────┘
            │◄──── f ──────►│       │◄────── D ────────►│
            │   (focal      │       │                   │
            │    length)    │       │                   │
                                                   W (scene width)

   Two similar triangles, sharing the apex at the lens:
     • small triangle:  half-sensor (w/2) at distance f
     • large triangle:  half-scene  (W/2) at distance D
```

Everything in this lesson falls out of that picture.

---

## Derivation 1 — Angle of view

Look at the small triangle. Half the sensor is `w/2` from the optical axis, and the sensor sits
`f` from the lens. The half-angle `θ/2` satisfies:

```
   tan(θ/2) = (w/2) / f  =  w / (2f)
```

So:

```
   ┌──────────────────────────────────┐
   │   AOV  =  2 · arctan( w / 2f )   │
   └──────────────────────────────────┘

   w = sensor dimension (mm) — WIDTH for horizontal AOV, HEIGHT for vertical
   f = focal length (mm)
```

**Both terms are in millimetres, so the ratio is dimensionless and the result is an angle.**
Angle of view depends only on the *ratio* of sensor size to focal length — not on distance, not
on resolution, not on the scene.

### 🧮 Worked example 1.1 — the test case

A 1/2.8" sensor (5.37 mm wide) with a 4 mm lens.

```
   w / 2f  =  5.37 / (2 × 4.0)  =  5.37 / 8.0  =  0.67125

   arctan(0.67125)  =  33.8715°          ← half-angle

   AOV = 2 × 33.8715  =  67.743°
```

**Horizontal AOV ≈ 67.74°.** This is `test_angle_of_view_known_case`.

Vertical, using the sensor *height* of 3.02 mm:

```
   3.02 / 8.0 = 0.3775  →  arctan = 20.6815°  →  AOV = 41.363°
```

**Vertical AOV ≈ 41.36°.** Note it is *not* 67.74 × (3.02/5.37) = 38.1°. **Angle of view does not
scale linearly with sensor dimension**, because arctan is not linear. Juniors who scale angles
proportionally get answers that are close enough to look right and wrong enough to matter at the
edges.

> ⚠️ **Sensor format designations lie.** "1/2.8 inch" is a legacy vidicon tube convention and does
> **not** equal the diagonal in inches. 5.37 mm is about 0.21", nowhere near 1/2.8" = 0.357". The
> numbers in `SENSOR_FORMATS_MM` are typical industry figures and **vary between manufacturers**.
> `[VERIFY per datasheet]` — for a real design, take the imager dimensions from the camera's
> datasheet, not from the format name.

---

## Derivation 2 — Field of view width

Now the large triangle. It is similar to the small one, so corresponding sides are in proportion:

```
   (W/2) / D  =  (w/2) / f

   W / D      =  w / f

   ┌──────────────────────┐
   │   W  =  D · w / f    │
   └──────────────────────┘
```

### The units question that trips everyone

`D` is in feet. `w` and `f` are in millimetres. The answer comes out in feet. **Is that legal?**

Yes, and here is exactly why:

```
   W  =  D  ×  (w / f)
         ↑       ↑
      feet    mm/mm = DIMENSIONLESS
```

`w/f` is a ratio of two lengths in the same unit, so it is a pure number — 1.3425 in the example
below. `W` therefore inherits whatever unit `D` carries. **You may use any distance unit you like
for `D` and `W`, as long as you use the same one for both, and as long as `w` and `f` share a unit
with each other.**

This is worth internalizing rather than memorizing, because it is the single most common source of
"my number is off by a factor of 25.4."

### 🧮 Worked example 1.2 — the test case

Same camera, target at 50 ft.

```
   w / f  =  5.37 / 4.0  =  1.3425      (dimensionless)

   W  =  50 ft × 1.3425  =  67.125 ft
```

**Scene width at 50 ft = 67.125 ft.** This is `test_fov_width_similar_triangles`.

Sanity-check it against the angle: a 67.74° horizontal AOV at 50 ft should span
`2 × 50 × tan(33.8715°) = 2 × 50 × 0.67125 = 67.125 ft`. ✅ The two derivations agree, as they
must — they are the same triangle read two ways.

> **What `D` actually measures.** `W = D·w/f` gives the width on a plane **perpendicular to the
> optical axis** at distance `D` along that axis. For a camera aimed level at a target directly
> ahead, that is the floor distance. For a **tilted** camera it is the **slant range**, and using
> floor distance instead will overstate your pixel density. See derivation 4.

---

## Derivation 3 — The inverse: choosing a lens

This is the one you use. You know the scene you must cover and the distance you can mount at. You
need the lens.

Rearrange `W = D·w/f` for `f`:

```
   ┌──────────────────────┐
   │   f  =  D · w / W    │
   └──────────────────────┘
```

### 🧮 Worked example 1.3 — the test case

What lens covers 67.125 ft at 50 ft on a 5.37 mm sensor?

```
   f  =  50 × 5.37 / 67.125  =  268.5 / 67.125  =  4.0 mm
```

**4.0 mm** — which is where we started, so the inversion round-trips. This is
`test_focal_length_inverts_fov_width`.

### 🧮 Worked example 1.4 — a real design question

You must cover a 24 ft wide loading dock from a camera 40 ft away, on a 1/2.8" sensor.

```
   f  =  40 × 5.37 / 24  =  214.8 / 24  =  8.95 mm
```

**You need ≈ 8.95 mm.** Now the engineering starts:

- **Lenses come in discrete sizes.** You will not buy an 8.95 mm lens. Common fixed focal lengths
  are 2.8, 4, 6, 8, 12, 16 mm. A varifocal 8–12 mm covers it with room to adjust.
- **Which way do you round?** A *longer* lens narrows the view — you cover less than 24 ft and
  miss the edges. A *shorter* lens widens it — you cover more than 24 ft and every foot of scene
  gets fewer pixels. **Round to the longer lens only if you can verify the coverage loss is
  acceptable; otherwise go shorter and accept the pixel cost.** Lesson 02 quantifies that cost.
- If you pick 8 mm: `W = 40 × 5.37/8 = 26.85 ft`. You cover the dock with 2.85 ft of margin.
- If you pick 12 mm: `W = 40 × 5.37/12 = 17.9 ft`. You have missed 6 ft of the dock.

> 🧠 **The senior habit: always compute the coverage of the lens you can actually buy, not the
> lens you calculated.** The calculated focal length is an intermediate value, never a
> specification. Half the coverage gaps in as-built systems are a rounding decision nobody wrote
> down.

---

## Derivation 4 — Slant range and depression angle

A camera is mounted above head height and aimed down. The distance the optics care about is not
the distance along the floor.

```
                 ● camera, mount height h_m
                 │╲
                 │ ╲
                 │  ╲   slant range S  (what the LENS sees)
      h_m − h_t  │   ╲
        = Δh     │    ╲
                 │     ╲
                 │  ┌───● target feature plane, height h_t
                 │  │
        ─────────┴──┴──────────────────  floor
                 │◄─ D ─►│
                  horizontal distance
```

**Pythagoras gives the slant range:**

```
   ┌────────────────────────────────┐
   │   S  =  √( D² + (h_m − h_t)² ) │
   └────────────────────────────────┘
```

**Basic trigonometry gives the depression angle:**

```
   ┌──────────────────────────────────────┐
   │   φ  =  arctan( (h_m − h_t) / D )    │
   └──────────────────────────────────────┘
```

`h_t` defaults to **5.0 ft** in the calculator — roughly face height for a standing adult, which
is the plane that matters for recognition and identification. Use `0.0` for a target at grade,
such as a licence plate.

### 🧮 Worked example 1.5 — the test cases

Camera at 9 ft, target face plane at 5 ft, 30 ft away horizontally:

```
   Δh  =  9 − 5  =  4 ft
   S   =  √(30² + 4²)  =  √(900 + 16)  =  √916  =  30.2655 ft
```

**Slant range = 30.27 ft.** This is `test_slant_range`.

Camera at 20 ft (a parking lot pole), same 5 ft target plane, 30 ft away:

```
   Δh  =  20 − 5  =  15 ft
   φ   =  arctan(15 / 30)  =  arctan(0.5)  =  26.565°
```

**Depression angle = 26.57°.** This is `test_depression_angle`.

### Two properties worth checking, because the tests do

**Slant range is never less than horizontal distance.** `S = √(D² + Δh²) ≥ √(D²) = D`, with
equality only when `Δh = 0`. This is `test_slant_range_never_less_than_horizontal`, and it is a
useful sanity check on any coverage table: if a slant range comes out smaller than the floor
distance, you have a sign error.

**Directly below the camera, depression is 90°.** At `D = 0` the arctan expression divides by
zero; the geometry says the camera is looking straight down, so the function returns 90.0
explicitly. This is `test_depression_directly_below_is_90`. A guard clause in place of a limit is
the right engineering choice here — the limit is unambiguous and the code should not raise on a
physically meaningful input.

### Why the depression angle matters more than juniors expect

```
   DESIGN HEURISTIC [PRACTICE] — not a rule, not a standard

   φ ≲ 30°   faces remain usable for identification
   φ ≳ 30°   increasing foreshortening; identification degrades regardless
             of how many pixels are on target
```

**Pixels are necessary, not sufficient.** A 20 ft pole camera looking down at someone standing
beneath it can have enormous pixel density on the top of their head and identify nobody. The
geometry has thrown away the face.

This is why:
- **Identification cameras at doors are mounted low and aimed near-level.** Roughly 7–8 ft, aimed
  at face height across the opening.
- **Overview cameras go high**, because their job is observation and situational awareness, and
  foreshortening doesn't hurt that.
- **A camera cannot do both jobs.** Owners ask for one camera that identifies at the door and
  watches the lobby. The geometry says no. Say so early, and propose two cameras.

> 🧠 The general principle behind the heuristic: **a coverage calculation gives you a necessary
> condition, never a sufficient one.** Lesson 02 adds pixel density; you still have to check
> lighting, focus, motion blur, compression, and — as here — whether the geometry presents the
> feature you need at all.

---

## Assumptions, and where they break

| Assumption | Where it stops being true | Consequence |
|---|---|---|
| **Thin-lens, rectilinear projection** | Wide-angle lenses below roughly 2.8 mm on a 1/2.8" sensor show barrel distortion | Real coverage at the frame edge differs from the calculation; edges are stretched and lower-density than the model says |
| **Fisheye is just a very wide lens** | **False.** Fisheye uses a different projection entirely | These functions must not be used on fisheye lenses at all. Use the manufacturer's coverage tool. |
| **Target plane is perpendicular to the optical axis** | Real scenes are oblique — a person walking toward the camera crosses many distances | Compute per target distance, not once per camera |
| **Geometric pixels equal usable detail** | Always an overstatement | No allowance for lens MTF, focus error, motion blur, or compression loss. All reduce usable detail below the geometric count. |
| **Sensor dimensions match the format name** | Format designations are legacy convention and vary by manufacturer | `[VERIFY per datasheet]` |

**The honest summary:** this model gives you the *best case* the geometry permits. Everything real
subtracts from it.

---

## Common mistakes

⚠️ **Scaling angle of view linearly with sensor dimension.** Arctan is not linear. Compute each
axis separately.

⚠️ **Using floor distance where the formula wants slant range.** Overstates pixel density, and the
error is worst at short range — which is exactly where you were counting on identification.

⚠️ **Specifying the calculated focal length.** Compute the coverage of a lens you can buy.

⚠️ **Mixing sensor units.** `w` and `f` must share a unit; `D` and `W` must share a unit. The two
pairs need not match each other.

⚠️ **Applying these formulas to a fisheye lens.**

⚠️ **Treating the 30° depression heuristic as a code requirement.** It is `[PRACTICE]`. It is also
right often enough to design by.

⚠️ **Trusting the sensor format name instead of the datasheet.**

---

## Junior vs. Senior

**Junior:** derives AOV and FOV width from the geometry; inverts for focal length; computes slant
range and depression angle; knows the format name isn't the diagonal.

**Senior:** computes coverage for the lens that can actually be purchased and records the rounding
decision; uses slant range by default and only simplifies when the error is demonstrably
negligible; recognizes when a single camera is being asked to satisfy two incompatible geometries
and proposes two; and states the assumption set alongside the number, because the number without
the assumptions is not an engineering result.

---

## Problem set

Work these by hand. Show the intermediate values, not just the answer — the intermediate values
are where the mistakes live.

**P1.1** A 1/3" sensor is 4.80 mm wide. Compute the horizontal angle of view for a 2.8 mm lens
and for a 12 mm lens.

**P1.2** Same 1/3" sensor, 6 mm lens. Compute the scene width at 15 ft, 40 ft, and 100 ft. What
kind of relationship is width vs. distance, and what does that mean for a coverage diagram?

**P1.3** You must cover a 32 ft wide storefront from a camera mounted 55 ft away on a 1/2.8"
sensor (5.37 mm).
- (a) Compute the required focal length.
- (b) Available fixed lenses are 6, 8, 12, and 16 mm. Which do you specify, and what is the actual
  coverage?
- (c) State the consequence of the rounding decision in one sentence.

**P1.4** A camera is mounted at 12 ft. A target's face plane is at 5 ft.
- (a) Compute the slant range at horizontal distances of 5, 15, and 40 ft.
- (b) Compute the percentage error you would make by using floor distance instead, at each.
- (c) At what horizontal distance does the error fall below 1%?

**P1.5** Compute the depression angle for a camera at 16 ft looking at a 5 ft face plane, at
horizontal distances of 10, 20, and 40 ft. At which of these is identification plausible on
geometry alone, and what does that tell you about where to mount an identification camera?

**P1.6** A client wants one camera at the main entrance that both identifies people entering and
provides an overview of the 40 ft wide lobby behind them. Using only the material in this lesson,
explain in under 150 words why this is two cameras, and what each one's mounting and lens would be
directionally.

**P1.7** 🧮 Verify the model against itself: for the 1/2.8" sensor with a 4 mm lens, compute the
scene width at 50 ft two ways — once with `W = D·w/f`, and once as `2·D·tan(AOV/2)`. Show that
they agree, and explain why they must.

> Answers: [`_solutions/01_camera_fov_solutions.md`](_solutions/01_camera_fov_solutions.md)

---

## Retrieval check

1. Derive `AOV = 2·arctan(w/2f)` from the pinhole geometry in two lines.
2. Derive `W = D·w/f` from similar triangles.
3. Why is it dimensionally legal for `W` to come out in feet when `w` and `f` are in millimetres?
4. Write the inverse and say when you use it.
5. What distance does `D` actually measure, and when is it not the floor distance?
6. Write the slant range and depression angle formulas.
7. Why is a 20 ft pole camera unable to identify someone standing beneath it, even with unlimited
   pixels?
8. Name three things this model does not account for.

---

## References

- IEC 62676-4 — video surveillance system application guidelines; source of the DORI criteria used
  in lesson 02. `[STANDARD][VERIFY current edition]`
- Any undergraduate optics text, thin-lens chapter — the geometry here is standard and unchanged
  for a century. `[PRACTICE]`
- Camera manufacturer datasheets — the only authority on a specific imager's dimensions. `[MFR]`
- [`../28_Calculators/psec/optics.py`](../28_Calculators/psec/optics.py) — the implementation.
- [`../28_Calculators/tests/test_psec.py`](../28_Calculators/tests/test_psec.py) — `TestOptics`,
  the record of these derivations.
- [`../03_Video_Surveillance/`](../03_Video_Surveillance/) — the application of this math to
  system design *(not yet written — see [`../COURSE_PROGRESS.md`](../COURSE_PROGRESS.md))*.

**Next:** [02 — Pixel Density and DORI](02_pixel_density.md)
