# 02 — Optics: Focal Length, FOV, Aperture, and Depth of Field

> **Prerequisite:** [`../32_Engineering_Math/01_camera_fov.md`](../32_Engineering_Math/01_camera_fov.md).
> That lesson derives `W = D·w/f`, its inverse, slant range, and depression angle. **This lesson
> does not re-derive them.** It assumes you can compute a lens and spends its length on the three
> lens properties module 32 does not cover — **aperture, depth of field, and optical quality** —
> and on how they interact with the focal length you already know how to calculate.
>
> Link **[2]** of [the imaging chain](01_imaging_chain.md).

## Learning objectives

- State what aperture controls, in both of its roles: light gathered and depth of field.
- Compute depth of field, and predict how it collapses with focal length.
- Explain why the aperture the camera *chooses* at night is not the aperture you designed for.
- Decide between fixed, varifocal, and motorised-zoom lenses on maintenance grounds, not price.
- Recognise the lens failures that no downstream link repairs, and the three that are free to fix.

---

## The three things a lens controls

Module 32 covers the first. This lesson covers the other two.

| Property | Set by | Controls | Covered in |
|---|---|---|---|
| **How much scene** | Focal length `f` | Field of view, and therefore pixel density | [32/01](../32_Engineering_Math/01_camera_fov.md) |
| **How much light** | Aperture `N` (the f-number) | Exposure, and therefore shutter speed and noise | Here |
| **How much is sharp** | Aperture `N`, focal length `f`, focus distance `s` | Depth of field | Here |

Note that aperture appears twice, pulling in opposite directions. That single fact is most of this
lesson.

## Aperture, the f-number, and why it is a fraction

The **f-number** `N` is the focal length divided by the diameter of the entrance pupil:

```
N = f / D_pupil
```

So `f/1.4` on a 12 mm lens means an opening about 8.6 mm across. Because it is a **ratio**, the
same f-number delivers the same image brightness on any lens — that is the entire reason the
convention exists.

**Light gathered scales as `1/N²`,** because the opening's *area* is what collects photons and
area goes as diameter squared. This is why the standard f-stop series looks strange (1.4, 2, 2.8,
4, 5.6, 8): each step is a factor of √2 in diameter, and therefore exactly **half** the light.

| Aperture | Light relative to f/1.4 | Stops below f/1.4 |
|---|---|---|
| f/1.4 | 1.000× | 0 |
| f/2.0 | 0.490× | 1.0 |
| f/2.8 | 0.250× | 2.0 |
| f/4.0 | 0.122× | 3.0 |
| f/5.6 | 0.062× | 4.0 |
| f/8.0 | 0.031× | 5.0 |

**Read the bottom row against lesson 01.** Going from f/1.4 to f/8 throws away 97% of the light.
To hold the same exposure the camera must find that light somewhere else: a shutter 32× longer
(catastrophic motion blur) or 32× more gain (noise). This is the mechanism behind every night
image failure in this module.

> ⚠️ **A lens's stated f-number is its *maximum* aperture — the best it can do.** A varifocal
> lens's f-number often degrades as it zooms in: a lens marked `f/1.6–2.8` is f/1.6 at its widest
> setting and only f/2.8 at full telephoto, which is **1.6 stops** less light exactly when you
> zoomed in for a distant, poorly lit target. `[MFR][VERIFY]` This is on the datasheet and it is
> routinely missed.

## Depth of field

**Depth of field (DOF)** is the range of distances rendered acceptably sharp. "Acceptably" is a
choice, encoded in the **circle of confusion** `c` — the largest blur spot that still reads as a
point.

For surveillance, tie `c` to the sensor's own pixel pitch rather than to the film-era convention.
A defensible strict choice for identification work is **2 pixels**:

```
pixel pitch = sensor width / horizontal pixels = 5.37 mm / 2688 = 1.998 µm
c = 2 × 1.998 µm = 0.00400 mm
```

The standard thin-lens results (all lengths in the same units):

```
hyperfocal    H   = f² / (N·c) + f

near limit    D_n = s(H − f) / (H + s − 2f)

far  limit    D_f = s(H − f) / (H − s)          → infinite when s ≥ H
```

`s` is the focus distance. **Focus at the hyperfocal distance and everything from `H/2` to
infinity is acceptably sharp** — the deepest DOF available for a given lens and aperture, and the
right default for an overview camera.

> 🧮 **`psec` does not implement depth of field.** Every DOF figure below was produced by an
> explicit script using the formulas above, and the arithmetic is shown so you can check it. See
> [the note on calculator gaps](#a-note-on-two-gaps-in-psec) at the end of this lesson.

### 🧮 Worked example 2.1 — the garage entry lane

**The scenario, which foreshadows [the capstone](_exercises/garage_design.md):** a single camera
at a parking garage entry lane is asked to capture **both** the number plate and the driver's
face. Plate at **25 ft**, face at **32 ft**, camera focused at **30 ft**, 12 mm lens, 1/2.8"
sensor, `c` = 0.004 mm.

```
f/1.4:  H = 84.5 ft   sharp from 22.1 ft to  46.5 ft   (span  24.3 ft)
f/2.8:  H = 42.3 ft   sharp from 17.5 ft to 103.3 ft   (span  85.7 ft)
f/4.0:  H = 29.6 ft   sharp from 14.9 ft to infinity
f/8.0:  H = 14.8 ft   sharp from  9.9 ft to infinity
```

**At 12 mm, both planes are inside the DOF at every aperture, even wide open.** Depth of field is
not the problem here. If you stopped at this example you would conclude that the plate-and-face
camera is fine.

It is not fine, and the reason is lesson 04's: at 12 mm the plate is nowhere near enough pixels to
read. Plate capture needs a **long** lens. Watch what that does.

### 🧮 Worked example 2.2 — the same question with the lens plate capture actually needs

Same sensor, plate at **40 ft**, **50 mm** lens, focused on the plate:

```
f/1.4:  H = 1466 ft   sharp from 38.94 ft to 41.1 ft   → depth  2.2 ft
f/2.0:  H = 1027 ft   sharp from 38.51 ft to 41.6 ft   → depth  3.1 ft
f/2.8:  H =  733 ft   sharp from 37.94 ft to 42.3 ft   → depth  4.4 ft
```

**Two point two feet.** The driver's face, roughly 7 ft behind the plate, is far outside focus at
every aperture. And holding the sharper aperture costs light you do not have at night.

Sweep the focal length at a fixed 30 ft focus to see the collapse directly:

| Lens | DOF at f/1.4 | Plate at 25 ft sharp? | Face at 32 ft sharp? |
|---|---|---|---|
| 12 mm | 22.1 – 46.5 ft | ✅ | ✅ |
| 25 mm | 27.7 – 32.7 ft | ❌ | ✅ |
| 35 mm | 28.8 – 31.3 ft | ❌ | ❌ |
| 50 mm | 29.4 – 30.6 ft | ❌ | ❌ |

**DOF collapses roughly as `1/f²`.** Quadruple the focal length and depth of field falls by about
sixteen. This is the single most important consequence of choosing a long lens, and it is invisible
in the FOV arithmetic of module 32, which is why it lives here.

> 🧠 **The design conclusion, which is a rule you can carry:** *plate capture and facial capture
> are different tasks requiring different cameras.* One camera cannot do both at a vehicle
> entry — not because of resolution, but because the lens that gets the plate cannot hold the face
> in focus, and because the exposure that freezes a moving plate underexposes a face. Every
> experienced designer has had this argument with a client who wants to buy one camera. The
> arithmetic above is how you win it in one page.

### The tension, stated plainly

```
       want deep DOF  ──►  stop down (high N)  ──►  less light  ──►  slower shutter
                                                                    or more gain
                                                                         │
                                                                         ▼
       want sharp motion at night  ◄──  open up (low N)  ◄──  more light │
                    │                                                    │
                    └────────────────  DIRECT CONFLICT  ─────────────────┘
```

You cannot have deep depth of field and a fast shutter in low light from the same lens. Something
must give, and the design act is deciding what — usually by **adding light** (link [1]), which
buys you out of the trade entirely.

## The aperture your camera actually chooses

Here is the part that catches people who have only designed on paper. **On a fixed or varifocal
surveillance lens with an auto-iris, you do not choose the aperture. The camera does, continuously,
based on scene brightness.**

Same 12 mm lens, focused at 30 ft, across a day:

| Condition | Aperture chosen | Resulting DOF |
|---|---|---|
| Bright day | f/8.0 | 9.9 ft → infinity |
| Dusk | f/2.8 | 17.5 → 103.3 ft |
| Night | f/1.4 | 22.1 → 46.5 ft |

**Your depth of field shrinks by a factor of about ten between noon and midnight, without anyone
touching anything.** A design commissioned at 2 p.m. and verified at 2 p.m. will be checked
against its deepest DOF and its most favourable exposure. This is why commissioning must include a
night verification, and why lesson 01 insists the site visit happens after dark.

> ⚠️ The corollary is that **focus set at noon may not be optimal at night**, because the plane of
> best focus shifts slightly with aperture on real lenses, and because focus is often set on a
> daytime scene with abundant contrast. Focus at the aperture and the light level that matter for
> the task — for a night-critical camera, that means focusing at night.

## Choosing a lens: fixed, varifocal, or motorised

| Type | Focal length | Set by | Real argument for it | Real argument against |
|---|---|---|---|---|
| **Fixed** | One value | Manufacture | Cheapest, optically best per dollar, nothing to drift, nothing to misadjust | Wrong by 15% and you are replacing hardware, not turning a ring |
| **Varifocal (manual)** | Range | A technician on a ladder | Absorbs field surprises; one SKU covers many positions | **Requires a ladder to change or re-focus**; drifts; frequently left soft |
| **Motorised zoom / remote focus** | Range | Remotely, from the VMS | Adjust and re-focus without a lift; genuinely valuable at height | Costs more; more to fail; tempts endless fiddling |
| **PTZ** | Wide range | An operator or a tour | Covers large areas, follows events | **Points somewhere else when it matters.** See [lesson 05](05_camera_form_factors.md) |

> 🧠 **The senior's basis for this choice is maintenance access, not optics.** Ask one question:
> *what does it cost to touch this camera again?* A camera at 9 ft over a corridor is a
> step-ladder and five minutes — fixed lenses are fine, and the money saved is real. A camera at
> 28 ft in an atrium, or over a live loading dock, is a lift, a permit, a spotter, and a
> half-day. **Specify remote focus and motorised zoom anywhere the second visit is expensive**,
> and you will recover the premium the first time a lens needs adjusting. Juniors optimise the
> purchase order; the lift rental is not on it.

⚠️ **Every varifocal lens in the field is a lens that was focused once, by hand, possibly badly,
possibly years ago.** On any retrofit survey, assume some fraction are soft and check. It is a
common finding, it is free to fix, and it makes an immediate visible difference that clients
notice — which is worth more to your credibility than most of the design work.

## Optical quality, and the things that are free to fix

Beyond focal length and aperture, real lenses differ in ways no spec sheet compares usefully.

- **Resolving power vs. sensor.** A lens has a finite ability to resolve detail. Pairing a cheap
  lens with an 8 MP sensor produces an 8 MP image of a blurry projection: you pay for pixels,
  storage, and bandwidth to record detail the glass never delivered. `[PRACTICE]` Lens quality
  should scale with sensor resolution, and often does not, because the sensor is the number on the
  quote.
- **IR correction.** Infrared light focuses at a different distance from visible light. An
  IR-corrected (**day/night**) lens holds focus across the day-to-night transition; an uncorrected
  one goes soft at night, exactly when it matters. **Any camera with IR illumination needs an
  IR-corrected lens.** `[MFR][VERIFY]`
- **The dome bubble.** A dome camera shoots through an extra piece of plastic that costs some
  light and some sharpness when new, and much more when scratched, hazed by UV, or dusty. It is
  also the single most-neglected maintenance item in the industry.
- **P-iris / DC-iris.** A P-iris is controlled to a known position and can be held at a mid
  aperture where lenses perform best and DOF is reasonable, instead of swinging wide open at the
  first hint of dusk. Worth specifying where DOF matters.

**The three free fixes**, in order of how often they are the answer on a retrofit:

1. **Clean the dome.** Costs nothing. Frequently the largest single image improvement available.
2. **Re-focus the varifocal.** Costs a ladder.
3. **Re-aim.** Costs a ladder, and fixes more backlight problems than any equipment purchase.

Do all three before quoting anything. It is the fastest credibility you will ever buy, and it
occasionally ends the engagement early — which is the correct outcome and the kind of honesty that
generates referrals.

## Design tradeoffs

| Decision | Buys | Costs | Watch for |
|---|---|---|---|
| Longer focal length | Pixel density at distance | DOF collapses ~1/f²; narrower FOV; more cameras | The plate-and-face trap |
| Wider focal length | Coverage per camera | Pixel density falls; barrel distortion below ~2.8 mm | "One camera covers the whole lobby" |
| Wider aperture (low N) | Light — the binding constraint at night | Shallower DOF; softer corners | Varifocal f-number degrading at zoom |
| Stopping down | DOF, corner sharpness | Light, as `1/N²` — brutal | Auto-iris undoing your choice at dusk |
| Varifocal over fixed | Field adjustability | Drift, soft focus, ladder time | Assume field units are soft until checked |
| Remote focus/zoom | Cheap re-adjustment forever | Purchase premium | Justify on lift cost, not on optics |
| IR-corrected lens | Focus holds into night | Small premium | Mandatory with IR illumination |

## Common mistakes

⚠️ **Specifying a lens from FOV alone.** The focal length that frames the scene may deliver 2 ft
of depth of field. Check DOF whenever `f` exceeds roughly 25 mm on a small sensor.

⚠️ **Asking one camera for plate and face at a vehicle entry.** Worked example 2.2. It is the most
common single-camera-too-few error in the discipline.

⚠️ **Verifying focus only in daylight.** The aperture, and therefore the DOF and often the focus,
are different at night. Commission after dark.

⚠️ **Ignoring f-number drift on varifocal lenses.** `f/1.6–2.8` loses 1.6 stops at full zoom.

⚠️ **Pairing premium sensors with commodity glass.** You cannot record detail the lens did not
pass, but you will pay to store it.

⚠️ **Forgetting IR correction on IR cameras.** Sharp all day, soft all night, and mystifying to
whoever inherits it.

⚠️ **Treating a dirty dome as a maintenance issue rather than an engineering one.** It is a link
[2] optical loss, it is often the biggest one present, and no camera upgrade survives it.

## Junior vs. Senior

| | Junior | Senior |
|---|---|---|
| Picks a lens by | FOV at the target distance | FOV, then DOF, then the aperture the site's night light will force |
| Treats aperture as | A number on the datasheet | The variable the camera changes hourly, and the main night constraint |
| Handles plate + face | One camera, both tasks | Two cameras, and has the DOF arithmetic ready for the objection |
| Chooses varifocal because | It is flexible | The mount is hard to reach — and then specifies **remote** focus |
| Assumes field lenses are | Focused | Soft, until verified — and checks on every survey |
| Quotes a retrofit by | Pricing new cameras | Cleaning, re-focusing, and re-aiming first, then pricing what remains |

## 🔧 Field exercise

1. Find a varifocal camera you can legitimately access. Look at its live image at maximum
   digital zoom on a static high-contrast edge. Judge whether it is truly focused.
2. Note its focal length range and its f-number range from the label or datasheet. Compute the
   light lost between its widest and longest settings.
3. Using the DOF formulas above and the camera's sensor format, compute its DOF at its current
   focal length, focused at the main subject distance, at both f/1.4 and f/8. Compare the spans.
4. Look at the dome bubble. Photograph it. Decide honestly whether it is costing image quality.

## Exercises

Work these before opening
[`_solutions/02_optics_and_lenses_solutions.md`](_solutions/02_optics_and_lenses_solutions.md).

**E2.1** A 1/2.8" camera (2688 × 1520, `c` = 0.004 mm) with a 16 mm lens is focused at 45 ft.
 (a) Compute the hyperfocal distance at f/2.0.
 (b) Compute the near and far limits of DOF at f/2.0.
 (c) The camera also needs to keep a doorway at 20 ft acceptably sharp. Does it?
 (d) If not, name **two** different changes that would fix it, and state the cost of each in terms
     of some other property you lose.

**E2.2** A client's vehicle gate has one camera on a 40 mm lens capturing plates at 35 ft. They
want to add facial capture of drivers "since the camera is already there." Write the three-sentence
reply. Include one number.

**E2.3** A varifocal lens is specified `2.8–12 mm, f/1.4–2.5`.
 (a) How much light is lost between its widest and longest focal length settings, as a ratio and
     in stops?
 (b) A designer computed the required night exposure using f/1.4 but selected 12 mm for the
     required FOV. By what factor is the real exposure short?
 (c) Using the smear reasoning from [lesson 01](01_imaging_chain.md), state the practical
     consequence for a person walking at 3 mph.

**E2.4** Explain, in terms a facilities manager would accept, why a camera that looked fine at
commissioning in July produces unusable images in December. Give two distinct mechanisms from this
lesson. Do not use the word "aperture" — you may describe it.

**E2.5** 🧠 You are reviewing a competitor's design for a 28 ft atrium. Every camera is specified
with a fixed lens, and the bill of materials is 11% cheaper than yours. Write the paragraph, for
the owner, that argues for remote focus and motorised zoom. It must quantify something and must not
disparage the competitor.

## Retrieval check

1. Light gathered scales as what function of the f-number?
2. Depth of field collapses roughly as what function of focal length?
3. Why can one camera not do plate and face at a vehicle entry? Give both reasons.
4. What is the hyperfocal distance, and what is the DOF when you focus there?
5. Why does a design verified at 2 p.m. hide a DOF problem?
6. What are the three free fixes on a retrofit, and in what order?
7. When is an IR-corrected lens mandatory?

## A note on two gaps in `psec`

Writing this module surfaced two calculations that `psec` does **not** implement and that a camera
designer needs routinely:

1. **Motion blur** — `smear_px = subject_speed × exposure_time × PPF`, and the ratio of that smear
   to a facial feature. Used in [lesson 01](01_imaging_chain.md), worked by hand there.
2. **Depth of field** — hyperfocal, near and far limits, from focal length, f-number, and circle
   of confusion. Used throughout this lesson, worked by hand here.

Both are geometric, both are testable against hand calculations, and both belong in `psec.optics`
alongside the FOV and pixel-density functions. They are **not** added here, deliberately: this
repository's architecture is that
[`../32_Engineering_Math/`](../32_Engineering_Math/) derives what
[`../28_Calculators/`](../28_Calculators/) implements, so adding these functions properly means
writing their derivations in module 32 first. That is logged as a follow-on work item rather than
back-doored through a module whose job is application. Until then, the arithmetic in these lessons
is shown in full precisely so it can be checked by hand.

## References

- [`../32_Engineering_Math/01_camera_fov.md`](../32_Engineering_Math/01_camera_fov.md) — focal
  length, FOV, slant range, depression angle. Prerequisite to this lesson.
- `[STANDARD][VERIFY]` **IEC 62676-4** — application guidelines; the DORI framework that
  [lesson 04](04_dori_and_pixel_density.md) applies to lens selection.
- `[PRACTICE]` The 2-pixel circle of confusion used here is a strict choice appropriate to
  identification work. Other defensible conventions exist (sensor diagonal ÷ 1500 is the film-era
  standard and is far more permissive). **State which you used** — DOF figures are not comparable
  across different `c`.
- `[MFR][VERIFY]` F-number ranges, IR correction, and P-iris behaviour are per-product claims.
  Take them from the datasheet of the actual model, and verify IR correction explicitly — it is
  often absent from summary specs.

---

**Next:** [03 — Sensors, Exposure, WDR, and Low Light](03_sensors_and_low_light.md) — link [3],
and the lesson where most real designs are quietly lost.
