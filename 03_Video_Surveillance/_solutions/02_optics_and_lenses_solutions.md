# Solutions — 02 Optics: Focal Length, FOV, Aperture, and Depth of Field

> Work the exercises in [`../02_optics_and_lenses.md`](../02_optics_and_lenses.md) before reading
> this. FOV and pixel-density values were produced by running
> [`../../28_Calculators/psec/optics.py`](../../28_Calculators/psec/optics.py). DOF values were
> produced by an explicit script using the thin-lens formulas in the lesson — `psec` does not
> implement DOF; see the note at the end of the lesson.

Constants used throughout: 1/2.8" sensor, **w = 5.37 mm**, **2688 px** horizontal, pixel pitch
1.998 µm, **c = 0.00400 mm** (2-pixel circle of confusion).

---

## E2.1 — 16 mm lens, focused at 45 ft

**(a) Hyperfocal distance at f/2.0.**

```
H = f² / (N·c) + f
  = 16² / (2.0 × 0.00400) + 16
  = 256 / 0.008 + 16
  = 32000 + 16 = 32016 mm
  = 32016 / 304.8 = 105.04 ft   →  105.16 ft carrying full precision
```

**H ≈ 105.16 ft.**

**(b) Near and far limits at f/2.0, focused at 45 ft.**

With `s` = 45 ft = 13716 mm:

```
D_n = s(H − f) / (H + s − 2f) = 13716(32016 − 16) / (32016 + 13716 − 32)  →  31.52 ft
D_f = s(H − f) / (H − s)      = 13716(32016 − 16) / (32016 − 13716)       →  78.62 ft
```

**Sharp from 31.52 ft to 78.62 ft** — a span of 47.1 ft. Note that `s` (45 ft) is well below `H`
(105 ft), so the far limit is finite, as expected.

**(c) Is the doorway at 20 ft acceptably sharp?**

**No.** The near limit is **31.52 ft**. The doorway at 20 ft is 11.5 ft closer than the nearest
sharp plane — not marginally out, comfortably out. At a 2-pixel circle of confusion it will be
visibly soft, and softness at 20 ft is exactly where you would have wanted the most detail.

**(d) Two fixes, and what each costs.**

There are four defensible options. Any two, correctly costed, earns full credit — but notice that
**none of them is free**, which is the point of the exercise.

| Fix | Result | What it costs |
|---|---|---|
| **1. Stop down to f/8** | near limit 16.60 ft → **20 ft is in** | **93.8% of the light** (0.062× of f/2.0, 4 stops). At night this is fatal: the shutter must go ~16× longer, and by [lesson 01](../01_imaging_chain.md)'s arithmetic the subject smears beyond use. Viable **only** if the scene is reliably bright. |
| **2. Re-focus to 20 ft** | 16.81 → 24.68 ft, **20 ft is in** | **The 45 ft subject leaves the DOF entirely** (far limit 24.68 ft). You have swapped which target is sharp, not gained both. |
| **3. Swap to an 8 mm lens, keep f/2.0 and 45 ft focus** | 16.60 ft → **infinity**; both planes sharp | **Half the pixel density everywhere.** At 45 ft, PPF falls 178.0 → **89.0**; at 20 ft, 400.4 → **200.2**. Both still clear the 76 ppf identify threshold here, so in *this* case it is the best option — but it is a real loss of margin, and on a longer shot it would break the requirement. |
| **4. Focus at the hyperfocal distance (105.16 ft)** | sharp from **52.58 ft** to infinity | **Fails.** It maximises DOF *toward infinity*, which is the wrong direction — it pushes the near limit further away, from 31.52 ft to 52.58 ft. Included because reaching for "hyperfocal = maximum DOF" without checking the near limit is a standard reflex error. |

Intermediate stops do **not** rescue it: f/2.8 gives a near limit of 28.15 ft, f/4.0 gives 24.25 ft,
and f/5.6 gives 20.48 ft — still short of 20 ft. Only f/8 reaches.

> 🧠 **The transferable lesson.** Two targets at 20 ft and 45 ft is a **2.25:1 distance ratio**, and
> that ratio is what the optics have to span. The comfortable engineering answer is usually the one
> people resist: **two cameras.** Every single-camera fix above trades away something real, and on a
> site where light is scarce or the pixel target is tighter, all four run out at once.

---

## E2.2 — The 40 mm plate camera asked to also capture faces

A model reply, three sentences with a number:

> The gate camera is on a 40 mm lens focused at the plate, which gives it a depth of field of about
> **2.6 ft** — from roughly 33.8 to 36.4 ft — so a driver's face, sitting several feet behind the
> plate, falls outside the focus zone no matter how we adjust it. On top of that, the exposure that
> freezes a moving plate is far too short to capture a face through windscreen glass at night, so
> the two tasks pull the camera in opposite directions. If facial capture at the gate matters, the
> reliable answer is a second camera aimed and exposed for the driver, and I can price that.

**What is being graded:**

- The 2.6 ft DOF figure (at f/1.4; f/2.0 gives 3.7 ft and f/2.8 gives 5.2 ft — any of the three,
  correctly attributed to an aperture, is fine).
- Naming **both** independent reasons — focus depth *and* exposure conflict. A reply that gives
  only one is half the answer, because a client can argue around either alone.
- Offering the second camera rather than just refusing.
- Not blaming the client for asking. It is a reasonable-sounding request.

Note that pixel density is **not** the objection here: at 40 mm the plate sits at 572 ppf and even
a face 7 ft further back would be at 477 ppf, far above any threshold. **The camera has plenty of
pixels and still cannot do the job** — the same lesson as worked example 1.2, arriving by a
different route.

---

## E2.3 — Varifocal `2.8–12 mm, f/1.4–2.5`

**(a) Light lost between the widest and longest settings.**

```
relative light = (N_wide / N_long)² = (1.4 / 2.5)² = 0.314
stops = 2 · log₂(2.5 / 1.4) = 1.67 stops
```

At full telephoto the lens passes **31.4% of the light** it passes at its widest setting — a loss
of **1.67 stops**, or a factor of **3.19×**.

**(b) By what factor is the exposure short?**

The designer budgeted for f/1.4 and is actually getting f/2.5, so the scene is delivering
**1/0.314 = 3.19× less light** than assumed. To hold the same image brightness the camera must
lengthen the exposure by **3.19×** (or raise gain equivalently, trading blur for noise).

**(c) Practical consequence for a person walking at 3 mph (4.4 ft/s).**

| Intended shutter | Actual shutter after the 3.19× shortfall | Smear at 3 mph |
|---|---|---|
| 1/60 s | ≈ **1/19 s** | **2.81 in** |
| 1/125 s | ≈ **1/39 s** | **1.35 in** |

Against an eye-to-eye distance of ~2.5 in, a **2.81 in** smear exceeds the entire interpupillary
distance: the face is destroyed, not degraded. Even the 1/125 s case degrades to a 1.35 in smear,
over half the eye-to-eye distance and well past usable for identification.

> ⚠️ **The trap this exercise sets.** The designer did nothing obviously wrong — they read
> `f/1.4` off the datasheet and computed with it. The f-number range is right there in the model
> number, and the failure is entirely one of not noticing that **the f-number they budgeted with
> and the focal length they selected cannot coexist.** Whenever you zoom a varifocal in, re-check
> the exposure budget at the *long* end's f-number.

---

## E2.4 — Why July looked fine and December does not

Two distinct mechanisms, in language a facilities manager will accept without a lecture:

**Mechanism 1 — the camera's automatic light control opens up, and less of the scene stays in
focus.**

> The camera adjusts itself to the light, the same way your eye does. In bright conditions it
> works with a small opening, and when the opening is small a wide range of distances stays sharp
> at once. As the light drops, it has to open up to keep the picture bright enough, and the side
> effect is that only a narrow band of distances stays sharp. In July we were seeing the widest
> version of that band; in December we are seeing the narrowest. Nothing has moved and nothing has
> broken — the camera is making a different trade because the conditions changed.

**Mechanism 2 — the camera holds the picture open for longer, so anything moving is smeared.**

> To get a bright enough image in the dark, the camera also has to collect light for longer on
> each frame. Anyone walking through during that time is recorded as a blur rather than a person.
> It is the same effect as a phone photo taken indoors at night without a flash. This is why we
> can look at the December footage and see plainly that *someone* was there, but not who — the
> detail was never captured, so there is nothing to enhance later.

Both end with the correct conclusion for the manager: **the fix is light on the scene, not a
better camera.**

*(A third acceptable mechanism: a lens without IR correction going soft when the camera switches
to night mode. Credit for it if stated as a distinct cause rather than a restatement of
mechanism 1.)*

---

## E2.5 — 🧠 The remote-focus argument at 11% more

A model paragraph:

> Both designs put the right image on the right scene on day one. Where they differ is what
> happens on day 400. Every camera in the atrium sits at roughly 28 ft, which means any adjustment
> — a lens that has drifted soft, a view that needs re-aiming after the tenant fit-out, a focus
> that was set in daylight and turns out to be wrong at night — requires a lift, a permit, and a
> spotter, and realistically a half-day of building disruption per visit. Our design specifies
> remote focus and motorised zoom on the atrium positions, so those adjustments happen from the
> security office in minutes. The premium is 11% of the camera package, and it is recovered the
> first or second time a lift would otherwise have been needed; on a ten-year system it will not
> be the first or second time. The other design is a sound design, and if these cameras were at 9
> ft over a corridor I would specify fixed lenses too and pocket the difference — the
> recommendation here is driven by the mounting height, not by the optics.

**What is being graded:**

- **Quantifies something** — the lift/half-day cost against the 11%, and the "recovered in one or
  two visits" comparison.
- Names the specific mechanism (drift, re-aim after fit-out, day-vs-night focus) rather than
  waving at "flexibility."
- **Does not disparage the competitor.** It explicitly calls their design sound and concedes the
  case where they would be right. This is both honest and far more persuasive to an owner, who has
  usually already noticed the price difference and is listening for whether you will be straight
  with them.
- Ties the recommendation to the site condition — **mounting height, not optics** — which is the
  senior framing from the lesson.

A common weak answer argues on image quality. It is the wrong argument: at commissioning both
designs deliver the same image, the owner can see that, and an argument the owner can disprove by
looking costs you the rest of the conversation.

---

## Retrieval check — answers

1. **`1/N²`.** Light scales with the *area* of the aperture, so each √2 step in f-number halves it.
2. **Roughly `1/f²`.** Quadrupling focal length cuts depth of field by about sixteen.
3. **(i)** The long lens needed for plate pixel density has a DOF of only a few feet, so the face
   plane falls outside focus; **(ii)** the short exposure needed to freeze a moving plate
   underexposes a face. Independent reasons — either alone defeats the single-camera design.
4. **Hyperfocal `H = f²/(N·c) + f`.** Focus there and everything from **H/2 to infinity** is
   acceptably sharp — the deepest available DOF for that lens and aperture.
5. Because at 2 p.m. the auto-iris is stopped well down, giving the **deepest** DOF the camera
   will ever show. The night aperture can shrink the sharp zone by a factor of ten.
6. **Clean the dome, re-focus the varifocal, re-aim** — in that order, cheapest first.
7. **Whenever the camera uses IR illumination.** IR focuses at a different distance from visible
   light, so an uncorrected lens goes soft precisely at night.
