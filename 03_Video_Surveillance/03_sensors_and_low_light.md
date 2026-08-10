# 03 — Sensors, Exposure, WDR, and Low Light

> Link **[3]** of [the imaging chain](01_imaging_chain.md), plus the part of link [4] that
> matters most.
>
> **This is the lesson where real designs are lost.** Not in the geometry — the geometry is easy
> and [`../28_Calculators/psec/optics.py`](../28_Calculators/psec/optics.py) already does it.
> Designs fail because the light was never measured, and because nobody computed what the camera
> would be forced to do with the light that was there. Everything here is arithmetic a junior can
> do in ten minutes, and it is skipped on most projects.

## Learning objectives

- Explain what a sensor actually measures, and why **area** matters more than pixel count.
- Derive the shutter speed a scene requires from the motion in it, not from preference.
- Build an **exposure budget in stops** — the vendor-independent tool for arguing about low light.
- State the four places extra stops can come from and what each one costs.
- Describe what WDR does, what it costs, and when it makes an image worse.
- Specify IR and thermal honestly, including what each one categorically cannot deliver.
- Give an illumination target that a lighting designer or electrician can actually build to.

---

## What a sensor does

A sensor is a grid of buckets that count photons. Each photosite accumulates charge while the
shutter is open; that charge is read out and digitised. Everything that makes a night image bad
follows from one fact: **at low light levels, the number of photons arriving is small enough that
its own randomness is visible.**

Two noise sources matter:

- **Shot noise** — the irreducible randomness of photon arrival. If you expect `N` photons you
  actually get about `N ± √N`. The signal-to-noise ratio is therefore roughly `√N`. **Collect four
  times the photons and the image gets twice as clean.** No processing improves on this; it is
  physics, not engineering.
- **Read noise** — added by the electronics on readout. Fixed per frame, so it dominates when the
  signal is very small — which is exactly the night case.

The design consequence is immediate: **the only real fix for a noisy image is more photons.** They
can come from a longer exposure (costs motion blur), a wider aperture (costs depth of field), a
bigger bucket (costs money), or more light in the scene (costs a fixture). Gain is not on that
list — gain multiplies the signal *and* the noise, changing brightness without changing SNR.

> 🧠 A software analogy that holds: gain is turning up the volume on a bad recording. It does not
> add information, and past a point it makes the noise floor obvious. What people call
> "low-light performance" in marketing is mostly aggressive gain plus aggressive noise reduction —
> a brighter, smoother picture containing no more information and often visibly less detail.

## Why sensor area beats megapixels

Photosite area is what collects photons, and on a fixed sensor size adding pixels makes each one
smaller. Compute it for the common 1/2.8" format (5.37 × 3.02 mm):

| Resolution | Pixel pitch | Photosite area | Light per photosite | Stops vs 2 MP |
|---|---|---|---|---|
| 2 MP (1920 px) | 2.797 µm | 7.82 µm² | 1.000× | 0.00 |
| 4 MP (2688 px) | 1.998 µm | 3.99 µm² | 0.510× | **−0.97** |
| 8 MP (3840 px) | 1.398 µm | 1.96 µm² | 0.250× | **−2.00** |

**Going from 2 MP to 8 MP on the same sensor costs exactly two stops of light per photosite.**

And across sensor formats at fixed resolution:

| Sensor | Area | Photosite area at 2688 px | vs 1/2.8" |
|---|---|---|---|
| 1/2.8" | 16.22 mm² | 3.99 µm² | — |
| 1/1.8" | 38.88 mm² | 7.17 µm² | **+0.85 stops** |
| 1/1.2" | 64.02 mm² | 15.76 µm² | **+1.98 stops** |

> ⚠️ **The rule to carry:** *on a fixed sensor size, resolution and low-light performance are
> directly traded against each other.* Buying resolution to fix a night image is not merely
> ineffective, as [lesson 01](01_imaging_chain.md) showed — it actively spends the resource you
> were short of. This is the arithmetic behind that lesson's warning, and E3.2 makes it exact.

---

## The exposure budget, in stops

Here is the tool. It is vendor-independent, it needs no sensor sensitivity data, and it settles
most low-light arguments in a page.

**A stop is a factor of 2 in light.** Shutter, aperture, gain, sensor area, and scene illuminance
all convert into stops, so they can be added and subtracted on one line. Work the budget in three
steps.

### Step 1 — Derive the shutter the scene requires

The shutter is set by the **motion in the scene**, not by preference. From
[lesson 01](01_imaging_chain.md): a person walking at 3 mph covers 4.4 ft/s, and adult
interpupillary distance is about 2.5 in `[PRACTICE]`.

| Shutter | Smear | % of eye-to-eye | Verdict |
|---|---|---|---|
| 1/15 s | 3.52 in | 141% | unusable for ID |
| 1/30 s | 1.76 in | 70% | unusable for ID |
| 1/60 s | 0.88 in | 35% | marginal |
| **1/125 s** | **0.42 in** | **17%** | **good** |
| 1/250 s | 0.21 in | 8% | good |
| 1/500 s | 0.11 in | 4% | good |

Setting a design target of **smear ≤ 25% of eye-to-eye** gives 0.625 in, which requires a shutter
no slower than 11.84 ms — **1/84 s** — so the nearest standard step is **1/125 s**.

That is your requirement. Write it in the basis of design: *"identification cameras shall be
capable of 1/125 s at the design illuminance."* It is checkable at commissioning, unlike
"good low-light performance."

> 🧠 **Faster motion moves the target hard.** A person running is ~15 ft/s (3.4× a walk) and
> demands ~1/500 s for the same smear budget. A vehicle at 15 mph is 22 ft/s and demands faster
> still — which, combined with [lesson 02](02_optics_and_lenses.md)'s depth-of-field collapse, is
> the second reason plate cameras are their own discipline. **Always ask how fast the subject is
> moving where the camera is looking**, then design the chokepoint that slows them down. A door,
> a turnstile, or a speed table is an image-quality intervention.

### Step 2 — Compare against what the site gives you

🧮 **Worked example 3.1 — the Meridian loading dock.**

Night survey of the loading dock at Meridian Building 2 measures **3.0 lux** at the face plane
`[PRACTICE]`. In that light, at f/1.4, the camera settles on **1/30 s**.

```
have:   1/30 s
need:   1/125 s
ratio = (1/30) / (1/125) = 4.17×
stops = log₂(4.17) = 2.06 stops short
```

Converting the shortfall into an illumination requirement:

```
required = 3.0 lux × 4.17 = 12.5 lux at the face plane
shortfall = 9.5 lux
```

**That is a specification.** "Provide 12.5 lux minimum at the face plane at the dock apron"
is something a lighting designer, an electrician, or a landlord can act on and you can verify with
a meter at handover. Compare it to what usually gets written — *"provide adequate lighting"* —
which is unbuildable and unverifiable.

### Step 3 — Decide where the stops come from

You need 2.06. Every source has a price:

| Source of stops | Buys | Costs |
|---|---|---|
| **Add light: 3.0 → 12.5 lux** | **2.06** | Fixture, power, possibly permits `[VERIFY]`. **The only source with no image penalty.** |
| Open f/2.0 → f/1.4 | 1.03 | Shallower DOF ([lesson 02](02_optics_and_lenses.md)) |
| Open f/2.8 → f/1.4 | 2.00 | Much shallower DOF; often not available anyway |
| +6 dB gain | 1.00 | Noise up; NR then smears detail; bitrate up |
| +12 dB gain | 2.00 | Noise badly up; the image looks "brighter" and identifies nobody |
| Larger sensor 1/2.8" → 1/1.8" | 1.26 | Camera cost, housing size, lens cost |
| Drop 4 MP → 2 MP, same sensor | 0.98 | **Half the pixel density** — check it still meets the target |

Note the last row. **Reducing resolution is a legitimate low-light intervention**, and it is
almost never proposed, because it looks like going backwards on a quote. Where the geometry has
margin — as the Meridian vestibule did at 2.11× — trading a stop of resolution for a stop of light
is straightforwardly the right engineering call.

> ⚠️ **The commonest wrong answer is gain**, because it is free and instant and the picture gets
> brighter on the monitor at 2 p.m. when the client is watching. It buys nothing. The second
> commonest is a resolution upgrade, which by the table above *costs* two stops.

---

## Dynamic range and WDR

**Dynamic range** is the ratio between the brightest and darkest parts of a scene a sensor can
record simultaneously, usually quoted in dB. When scene dynamic range exceeds sensor dynamic
range, something clips: highlights blow to white, shadows crush to black, or both.

Security scenes are unusually brutal here — a glass lobby at noon, a garage portal at midday, a
loading door with sun outside and shade inside. These routinely exceed what any single exposure
can hold.

**Wide Dynamic Range (WDR)** addresses it two ways, and the difference matters:

| Approach | How | Strength | Cost |
|---|---|---|---|
| **True / multi-exposure WDR** | Captures 2+ exposures per frame and blends them | Genuinely extends captured range | **Motion artefacts** — the exposures are taken at different instants, so moving subjects ghost or tear. Effective frame rate and low-light performance may drop. |
| **Tone mapping / "digital WDR"** | Single exposure, locally remapped contrast | No motion artefacts; free | **Adds no information.** It redistributes what was captured. Crushed shadows stay crushed. |

> ⚠️ **WDR is not free and is not always on-by-default correct.** Aggressive WDR produces the
> characteristic flat, grey, low-contrast surveillance image — everything visible, nothing
> identifiable. It is the visual signature of a camera trying to satisfy a scene it should never
> have been asked to cover. And multi-exposure WDR ghosting appears **exactly on moving subjects**,
> which are the ones you care about.

**The better fix is nearly always geometric.** Re-aim so the bright source is not in frame. Move
the camera to the other side of the vestibule so it shoots *with* the light rather than into it.
Add light on the subject side to lift the shadows toward the highlights, reducing the range the
sensor has to span. **WDR is what you use when you could not fix the geometry** — and on a
retrofit, re-aiming is free (one of [lesson 02](02_optics_and_lenses.md)'s three free fixes).

## IR illumination

Infrared gives a usable night image with no visible light. It is genuinely useful and it is
routinely oversold.

- **850 nm** — more efficient, better range, emits a **faint visible red glow** from the emitter.
- **940 nm** — effectively invisible, but **roughly half the effective range** for the same power
  `[MFR][VERIFY]`, because sensor sensitivity falls off that far into the infrared.

**What IR categorically cannot deliver:**

⚠️ **Colour.** An IR-illuminated image is monochrome. *"Suspect wore a red jacket"* is not
available from it — the single most common descriptor in a witness statement and a BOLO. This is a
real evidentiary loss and it must be a stated, accepted decision, not a surprise. Where colour at
night matters, you need **visible** light, and the design conversation is about lighting, not
cameras.

**Failure modes to design around:**

- **Range claims.** Manufacturer IR distances assume a high-reflectance target under ideal
  conditions `[MFR][VERIFY]`. A person in dark clothing at the stated range will be far darker
  than the marketing image. **Derate substantially and verify on site.**
- **Hotspot and falloff.** IR from a point source obeys the inverse square law: a subject at 10 ft
  is blown out white while one at 40 ft is invisible, in the same frame. Integrated ring
  illuminators around a lens are the worst offenders. **Separately-mounted IR illuminators, aimed
  independently, are markedly better** and are how you fix this.
- **Retroreflection.** Retroreflective materials — safety vests, road signs, plate faces — return
  IR intensely and bloom into white. A high-vis vest can white out the wearer's torso and defeat
  the camera's exposure metering for the whole frame.
- **Dome bounce.** IR emitters inside the same dome as the lens reflect off the bubble straight
  into the sensor, washing the image out. It is worst when the bubble is dirty or scratched — and
  it is a common cause of "the camera worked when new."
- **Spiders and insects.** IR emitters attract insects, which attract spiders, which build webs
  directly in front of the lens. This sounds like a joke and is one of the most frequent real
  causes of degraded night images in the field.

## Thermal

Thermal cameras image emitted heat rather than reflected light. They need **no illumination at
all** and see through smoke, light fog, and total darkness.

**What they are excellent at:** detecting that a warm object is present and moving, at long range,
in conditions where nothing else works. As a **detection** sensor over a perimeter or a large dark
yard, thermal is often the correct and most cost-effective answer.

⚠️ **What they cannot do: identify anyone.** A thermal image has no facial detail, no colour, no
text, no plate. It answers *"is something there and where is it going?"* and never *"who is it?"*

**The standard, and correct, pattern is to pair them:** thermal detects and cues; a visible-light
camera — often a PTZ, often with illumination — is directed to the location for assessment and
identification. Specifying thermal alone where the requirement is identification is a
requirements failure that no amount of thermal resolution repairs.

## Lux ratings, and why you should not trust them

Every camera datasheet carries a minimum illumination figure. Treat it as marketing until proven
otherwise. `[MFR][VERIFY]` It is quoted under conditions the vendor chooses, and vendors choose
differently: 50% or 30% video level, IR cut filter in or out (out is monochrome), shutter as slow
as 1/4 s, maximum gain, high-reflectance target. **A "0.001 lux" camera achieving that figure at
1/4 s with the filter removed is telling you nothing about whether it can capture a walking person
at 1/125 s in colour.**

**What to do instead:**

1. Design with the **exposure budget in stops**. It is self-consistent and needs no vendor claims.
2. Specify the requirement in terms you can test: *"shall produce an identifiable facial image of
   a subject walking at 3 mph at 1/125 s at the design illuminance."*
3. **Demand a site shootout** for any significant project. Put the two or three candidate cameras
   on the actual scene, at night, and walk a person through. It takes an evening and it is the
   only evidence that answers the question. It also, reliably, changes the answer.

## Design tradeoffs

| Decision | Buys | Costs | When it is right |
|---|---|---|---|
| Add scene lighting | Stops, with no image penalty | Fixture, power, permits, light pollution | **Almost always the first move** |
| Larger sensor format | ~1–2 stops | Cost, size, lens cost | Night-critical, no lighting possible |
| Lower resolution | ~1 stop per halving | Pixel density | Where geometry has margin — underused |
| Longer exposure | Stops, linearly | Motion blur — usually total loss | Static scenes only |
| Higher gain | Brightness | **No SNR gain**; noise; bitrate | Last resort, deliberately capped |
| Multi-exposure WDR | Captured dynamic range | Motion artefacts, frame rate, low light | High-contrast, low-motion scenes |
| Re-aim to avoid backlight | Dynamic range, free | Coverage geometry changes | **Try before any WDR setting** |
| IR illumination | Night image with no visible light | **All colour information** | Where covertness or light pollution rules |
| Visible white light | Colour at night, deterrence | Cost, neighbours, permits `[VERIFY]` | Where colour is evidentially needed |
| Thermal | Detection in any conditions | **Cannot identify** | Perimeter/large-area detection, cued to a visible camera |

## Common mistakes

⚠️ **Never measuring the light.** A $200 light meter and one night visit is the highest
return-on-cost activity in this discipline. Designs are routinely built on a guess.

⚠️ **Specifying "adequate lighting."** Unbuildable, unverifiable, and unarguable at handover.
Specify lux at a named plane.

⚠️ **Believing datasheet lux figures.** See above. Different vendors, different conditions,
uncomparable.

⚠️ **Fixing low light with resolution.** Costs two stops going 2 MP → 8 MP on the same sensor.

⚠️ **Leaving gain uncapped.** The camera will choose brightness over detail every time, and the
result looks acceptable on a monitor and identifies nobody. Cap it deliberately.

⚠️ **Leaving the maximum exposure time uncapped.** This is the same error, in the other direction,
and it is the direct cause of worked example 1.2. **Cap the slowest shutter** on any camera whose
job is identification — accept a darker image over a smeared one, because a dark sharp image can
be brightened in review and a smeared one cannot be unsmeared.

⚠️ **Turning WDR on everywhere by default.** It costs motion performance and low-light
performance, and it is the wrong tool when re-aiming would fix the scene.

⚠️ **Promising colour and delivering IR.** Write down which cameras go monochrome at night, and
have the client acknowledge it.

⚠️ **Specifying thermal for identification.** It is a requirements failure, not a product problem.

## Junior vs. Senior

| | Junior | Senior |
|---|---|---|
| Assesses low light by | The camera's lux rating | An exposure budget in stops, from a measured site reading |
| Site survey | Daytime | **Night, with a light meter, at the face plane** |
| Specifies lighting as | "Adequate" | "12.5 lux minimum at the face plane," verifiable at handover |
| Fixes a night image with | A better camera | Light — then, if needed, a bigger sensor or *fewer* pixels |
| Treats gain as | Free performance | Brightness without information; caps it |
| Treats shutter as | Whatever the camera picks | A **requirement derived from subject speed**, capped in configuration |
| Uses WDR | On, everywhere | After trying to re-aim; knowing it costs motion and low light |
| Selects cameras by | Datasheet comparison | **Site shootout on the actual scene at night** |
| Handles IR | Specifies it | Specifies it *and* gets the loss of colour acknowledged in writing |

## 🔧 Field exercise

Borrow or buy a light meter (a phone app is not adequate for design, but it is fine for learning
the magnitudes).

1. Measure illuminance at head height, facing the camera, at three locations you care about, at
   the darkest hour they are normally used. Record lux and the time.
2. For each, compute the shutter required for a walking subject at a 25%-of-eye-to-eye smear
   budget.
3. Look at the camera's actual configured shutter and gain, if you can see them. Compute the
   exposure budget shortfall in stops.
4. Write the one-line lighting specification each location would need. Compare that to what is
   installed.
5. Walk through each scene and look at the **recording**. Confirm your arithmetic predicted what
   you see.

## Exercises

Work these before opening
[`_solutions/03_sensors_and_low_light_solutions.md`](_solutions/03_sensors_and_low_light_solutions.md).

**E3.1** A parking structure ramp measures **1.5 lux** at the face plane at night. The camera is
at f/1.6 and settles on 1/25 s. Vehicles move through at roughly 10 mph; pedestrians walk at 3 mph.
 (a) Compute the shutter required for the pedestrians at a 25%-of-eye-to-eye smear budget.
 (b) Compute the shutter required to hold the same *absolute* smear on a 10 mph vehicle.
 (c) State the exposure budget shortfall in stops for the pedestrian requirement.
 (d) Give the required illuminance, and write the one-line specification.

**E3.2** A client's night images are poor. A vendor proposes replacing the 2 MP cameras (1/2.8"
sensor) with 8 MP cameras (same 1/2.8" sensor), stating the higher resolution will "capture more
detail in low light."
 (a) Compute the change in light collected per photosite, in stops.
 (b) The site needs 2.0 stops *more* light to reach an acceptable shutter. What is the net
     position after the upgrade?
 (c) Compute what the upgrade does to the required scene illuminance.
 (d) Write the two-sentence response.

**E3.3** A design calls for a camera to identify people at a rear service door at night with **no
visible light permitted** (residential neighbours). The client also wants clothing colour.
 (a) State the conflict precisely.
 (b) Give three options, with what each delivers and what each gives up.
 (c) Say which you would recommend and what you would put in writing.

**E3.4** Explain why a camera with a "0.002 lux" rating may perform worse on your site than one
rated "0.05 lux." Name at least three specific ways the ratings could differ, and state what you
would do instead of comparing them.

**E3.5** 🧠 A retail client reports that their new cameras produce "washed out, grey, flat" images
at the entrance all day, though the old ones looked "contrasty and sharp." The new cameras are
higher resolution and have WDR enabled by default. Nobody has changed the lighting.
 (a) Give the most likely cause.
 (b) Explain why the old cameras looked better while capturing *less* information.
 (c) State what you would change, and what you would measure to confirm it.

## Retrieval check

1. Signal-to-noise ratio scales as what function of photon count?
2. Does gain improve SNR? What does it actually do?
3. How many stops does 2 MP → 8 MP cost on a fixed sensor size?
4. How do you derive the required shutter speed for a scene?
5. Name the only source of extra stops with no image penalty.
6. What can a thermal camera never do?
7. What does an IR-illuminated image categorically lack?
8. Why is a datasheet lux rating not comparable between manufacturers?
9. Which two camera settings should be **capped** on an identification camera, and why?

## References

- `[STANDARD][VERIFY]` **IEC 62676-4** — application guidelines, including guidance on
  illumination for the DORI classes. Verify the current edition.
- `[GUIDELINE][VERIFY]` **IES RP series** — illuminance recommendations by application; the
  reference a lighting designer will work from when you hand them a lux target. Treated properly
  in [`../06_Perimeter_Security/`](../06_Perimeter_Security/) *(not yet written)*.
- `[PRACTICE]` Walking speed, interpupillary distance, the 25%-of-eye-to-eye smear budget, and the
  measured lux values in this lesson are engineering practice and a fictional site, not standards.
  They are stated explicitly so you can substitute your own and redo the arithmetic.
- `[MFR][VERIFY]` Minimum-illumination ratings, IR range claims, and WDR dB figures are
  per-product marketing claims measured under conditions the vendor selects. Verify by site
  shootout.
- [`02_optics_and_lenses.md`](02_optics_and_lenses.md) — the aperture side of the exposure budget,
  and the depth-of-field cost of buying stops by opening up.

---

**Next:** [04 — DORI and Pixel Density in Practice](04_dori_and_pixel_density.md) — where the
target class comes from, and what choosing the wrong one costs.
