# Solutions — 01 Camera Field of View and Focal Length

> Work the problems before reading. The intermediate values are the point.

---

## P1.1 — Angle of view, 1/3" sensor (4.80 mm wide)

```
   AOV = 2 · arctan( w / 2f )
```

**2.8 mm lens:**
```
   w / 2f      = 4.80 / (2 × 2.8) = 4.80 / 5.6 = 0.857143
   arctan      = 40.6013°
   AOV         = 81.203°
```

**12 mm lens:**
```
   w / 2f      = 4.80 / (2 × 12) = 4.80 / 24 = 0.200000
   arctan      = 11.3099°
   AOV         = 22.620°
```

**The observation worth making:** the focal length went up by a factor of 4.29 (2.8 → 12) and the
angle went down by a factor of 3.59 (81.2 → 22.6). **Not proportional.** Arctan compresses at
large arguments, so wide lenses give up angle slowly and long lenses give it up quickly. This is
why the jump from 2.8 mm to 4 mm changes a scene far less than the jump from 12 mm to 16 mm does.

---

## P1.2 — Scene width vs. distance

```
   w / f  =  4.80 / 6.0  =  0.8      (dimensionless)
```

| Distance D | W = D × 0.8 |
|---|---|
| 15 ft | **12.0 ft** |
| 40 ft | **32.0 ft** |
| 100 ft | **80.0 ft** |

**The relationship is linear** — `W` is directly proportional to `D`, with the constant of
proportionality `w/f`.

**What that means for a coverage diagram:** the covered area is a **triangle** (in plan), not a
cone that flares and then flattens. Two consequences that matter in practice:

1. **You only need one point to draw it.** Compute the width at one distance and the whole wedge
   follows. This is why a coverage overlay in Bluebeam or CAD is a simple triangle primitive.
2. **Pixel density falls as 1/D**, not as 1/D². Lesson 02 does this properly, but note it now: it
   means doubling the distance halves the pixel density, which is a gentler penalty than the
   inverse-square intuition people import from lighting and RF.

---

## P1.3 — Lens selection for a 32 ft storefront at 55 ft

**(a) Required focal length**

```
   f  =  D · w / W  =  55 × 5.37 / 32  =  295.35 / 32  =  9.230 mm
```

**(b) Which lens, and actual coverage**

| Lens | W = 55 × 5.37 / f | vs. 32 ft required |
|---|---|---|
| 6 mm | **49.23 ft** | +17.23 ft — covers it, with a lot of wasted scene |
| 8 mm | **36.92 ft** | +4.92 ft — covers it with margin ✅ |
| 12 mm | **24.61 ft** | **−7.39 ft — misses 23% of the storefront** ❌ |
| 16 mm | **18.46 ft** | −13.54 ft ❌ |

**Specify the 8 mm.** It is the longest lens that still covers the requirement, which means it
delivers the highest pixel density among the options that actually work.

**(c) The consequence, in one sentence**

> Rounding 9.23 mm *up* to 12 mm would have cut 7.4 ft off a 32 ft storefront — a coverage gap of
> nearly a quarter of the scene, invisible on a schedule and obvious the first time something
> happens at the edge of the window.

**The general rule this illustrates:** when the calculated focal length falls between available
sizes, **go shorter**. A shorter lens costs pixel density uniformly across the scene, which you
can quantify and decide about (lesson 02). A longer lens costs you scene entirely, and the part
you lose is the part you never look at until it matters.

---

## P1.4 — Slant range error, camera at 12 ft, face plane at 5 ft

```
   Δh = 12 − 5 = 7 ft
   S  = √(D² + 49)
```

| D (floor) | S (slant) | Error if you use D instead of S |
|---|---|---|
| 5 ft | **8.6023 ft** | **41.9%** |
| 15 ft | **16.5529 ft** | **9.4%** |
| 40 ft | **40.6079 ft** | **1.5%** |

Error computed as `(S − D) / S`, i.e. the fraction of the true distance you are omitting.

**(c) Where the error falls below 1%**

Set `D = 0.99·S`, so `S = D/0.99`:

```
   D² + 49  =  (D / 0.99)²
   D² + 49  =  D² / 0.9801
   49       =  D² (1/0.9801 − 1)  =  D² × 0.020304
   D²       =  2413.3
   D        =  49.13 ft
```

**Beyond about 49 ft, the slant-range correction is under 1%** and you can reasonably ignore it.

**The engineering reading of this table, which is the real answer:**

The error is **worst exactly where you care most.** At 5 ft — a person at the door, the case where
you want identification — using floor distance overstates your effective range by 42%, which
overstates pixel density by the same factor. You would report an "identify"-class opening that is
nothing of the kind.

At 40 ft, where you are doing observation and 1.5% is noise, the correction is irrelevant.

> **So the rule is not "always use slant range" or "it doesn't matter."** It is: *use slant range
> by default, and only simplify when you have checked that the mount height is small relative to
> the distance.* The calculator's `coverage_report` uses slant range unconditionally for exactly
> this reason.

---

## P1.5 — Depression angle, camera at 16 ft, face plane at 5 ft

```
   Δh = 11 ft
   φ  = arctan(11 / D)
```

| D | φ | Identification plausible on geometry? |
|---|---|---|
| 10 ft | **47.73°** | **No.** Severe foreshortening; you are photographing the top of a head. |
| 20 ft | **28.81°** | **Marginal.** Just inside the ~30° heuristic. |
| 40 ft | **15.38°** | **Yes**, on geometry — but check pixel density at 40 ft before celebrating. |

**What this tells you about mounting an identification camera:**

There is a **near limit** as well as a far limit, and the near limit is the one nobody draws.
Every coverage diagram shows the maximum range at which a camera meets a pixel target. Almost none
show the minimum range at which the depression angle stops presenting a face.

For this 16 ft mount, the usable identification band is roughly **20 ft to whatever the pixel math
allows** — and everything closer than 20 ft is a blind spot for identification purposes while
being perfectly good video.

**The design consequence:** an identification camera wants a **low mount and a shallow angle**,
which means roughly 7–8 ft, aimed near-level, close to the point of interest. That is the opposite
of where instinct puts a camera (high, where it is safe from tampering and sees everything). The
two goals are genuinely in conflict, and identification loses unless you decide otherwise
deliberately.

---

## P1.6 — One camera for identification and lobby overview

Model answer (141 words):

> These are two different geometries and one camera can't hold both.
>
> To identify someone at the door, the camera has to be low — about 7 to 8 feet — and aimed
> nearly level at face height, close to the door. Mounted high it looks down at the top of
> people's heads, and past about 30 degrees of downward angle a face stops being usable no matter
> how many pixels land on it.
>
> To see the whole 40-foot lobby, the camera has to be high and wide. A wide lens spreads the
> pixels thin, and a high mount is exactly the angle that kills faces.
>
> So: a low, narrow, near-level camera at the door for identification — something around an 8 to
> 12 mm lens covering just the opening. And a separate high, wide camera for the lobby overview,
> around 2.8 to 4 mm.
>
> Two cameras, and the second one is cheap.

**What makes it work:** it explains the *mechanism* (foreshortening) rather than asserting a rule,
it gives directional numbers so the client can see the two designs are genuinely different, and it
ends by removing the objection — the second camera is not the expensive part of this system.

---

## P1.7 — 🧮 Verifying the model against itself

**Route 1 — similar triangles:**
```
   W = D · w / f  =  50 × 5.37 / 4.0  =  67.125000 ft
```

**Route 2 — via the angle:**
```
   AOV    = 2 · arctan(5.37 / 8)  =  67.742974°
   AOV/2  = 33.871487°
   tan(33.871487°) = 0.671250
   W      = 2 · D · tan(AOV/2)  =  2 × 50 × 0.671250  =  67.125000 ft
```

**They agree exactly.**

**Why they must:** the two routes are the same triangle read in two directions. Route 2 substitutes
route 1's own definition back into itself:

```
   tan(AOV/2)  =  w / 2f            ← from derivation 1

   W = 2 · D · tan(AOV/2)
     = 2 · D · (w / 2f)
     = D · w / f                     ← derivation 2
```

The `2` and the `1/2` cancel. There is only one piece of geometry here, and the angle form and the
ratio form are algebraic rearrangements of each other.

> 🧠 **Why this problem is in the set:** dimensional and self-consistency checks are how you catch
> a formula error without a reference answer. When you derive something new, find a second route
> to the same number. If the routes disagree, one of them is wrong and you have learned that
> before you built anything. This is the same instinct as `test_max_range_is_consistent_with_forward_calc`
> in the test file — a round-trip that proves the inverse really is the inverse.
