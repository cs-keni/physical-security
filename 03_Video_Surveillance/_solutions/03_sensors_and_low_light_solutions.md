# Solutions — 03 Sensors, Exposure, WDR, and Low Light

> Work the exercises in [`../03_sensors_and_low_light.md`](../03_sensors_and_low_light.md) before
> reading this. All arithmetic below was produced by running the exposure-budget script and
> transcribed. The method — **work in stops** — needs no vendor data and is the thing to carry
> away, not the specific numbers.

Constants: walking 3 mph = **4.4 ft/s**; interpupillary distance **2.5 in**; smear budget
**25% of eye-to-eye = 0.625 in** `[PRACTICE]`.

---

## E3.1 — Parking structure ramp, 1.5 lux, f/1.6, camera settles at 1/25 s

**(a) Shutter required for pedestrians (3 mph).**

```
smear budget = 0.25 × 2.5 in = 0.625 in = 0.05208 ft
t ≤ 0.05208 ft ÷ 4.4 ft/s = 11.84 ms = 1/84 s
```

Nearest standard step, rounding **toward faster**: **1/125 s**.

**(b) Shutter to hold the same absolute smear on a 10 mph vehicle.**

```
10 mph = 10 × 5280 / 3600 = 14.67 ft/s
t ≤ 0.05208 ft ÷ 14.67 ft/s = 3.55 ms = 1/282 s
```

Nearest standard step: **1/500 s**.

Note the vehicle is 3.33× faster than the pedestrian and so demands a 3.33× shorter exposure —
the relationship is linear in speed, which makes it easy to carry in your head.

**(c) Exposure budget shortfall for the pedestrian requirement.**

```
have  1/25 s
need  1/125 s
ratio = (1/25) ÷ (1/125) = 5.00×
stops = log₂(5.00) = 2.32 stops short
```

**(d) Required illuminance and the specification.**

```
required = 1.5 lux × 5.00 = 7.50 lux at the face plane
```

> **Specification:** *"Provide a minimum maintained illuminance of 7.5 lux at 5 ft above finished
> floor, measured vertically facing the camera, throughout the ramp travel path."*

**The part most people miss:** the vehicle requirement is on the **same ramp**, and it is far
harsher:

```
have 1/25 s, need 1/500 s → ratio 11.26× → 3.49 stops
required = 1.5 lux × 11.26 = 16.90 lux
```

So the ramp actually needs **16.9 lux** if the design must capture vehicles as well as pedestrians
at the same smear budget — **2.25× the pedestrian figure.** A designer who computes only the
pedestrian case will specify 7.5 lux, install it, and then discover that vehicles are still
smeared.

> 🧠 **Always identify the fastest thing you must capture in the scene, and design to it** — or
> explicitly decide you are not capturing it and record that decision. A ramp is a mixed-traffic
> scene and mixed-traffic scenes are where this error lives. The alternative, and often the better
> answer, is to design the *chokepoint*: capture vehicles where they are stopped at the gate, not
> where they are moving on the ramp.

---

## E3.2 — The 2 MP → 8 MP proposal, quantified

**(a) Change in light per photosite.**

1/2.8" sensor, 5.37 mm wide:

```
2 MP: pitch = 5.37/1920 = 2.797 µm → photosite area 7.82 µm²
8 MP: pitch = 5.37/3840 = 1.398 µm → photosite area 1.96 µm²

ratio = 1.96 / 7.82 = 0.250×  →  log₂(0.250) = −2.00 stops
```

**The upgrade loses exactly two stops.**

**(b) Net position.**

```
needed:            +2.00 stops
upgrade delivers:  −2.00 stops
net:                4.00 stops short
```

The site was 2 stops short. After the upgrade it is **4 stops short** — twice as far from working,
in stops, and **four times** as far in linear light.

**(c) Effect on required scene illuminance.**

```
before upgrade: 2^2.00 =  4.00× the current illuminance
after upgrade:  2^4.00 = 16.00× the current illuminance
```

**The lighting required to rescue the scene quadruples.** If the original fix was "get from 3 lux
to 12 lux," after the upgrade it becomes "get from 3 lux to 48 lux" — which is a different order
of lighting project, and on many sites is not achievable at all without objections about light
spill.

**(d) The two-sentence response.**

> Moving from 2 MP to 8 MP on the same size sensor makes each pixel a quarter of the area, so
> each one collects a quarter of the light — that is a two-stop loss, and since we are already
> about two stops short of the shutter speed we need to stop motion blur, the upgrade would leave
> us four stops short instead of two and roughly quadruple the lighting we'd need to fix it.
> The change that actually solves this is raising the light at the scene to about 12 lux at head
> height; if we do that first, the cameras you already own will meet the requirement, and we can
> revisit resolution afterwards if the geometry turns out to be short anywhere.

**What is being graded:** the −2.00 stops; recognising the losses **add** so the position is 4
stops short, not 0; the illuminance quadrupling; and proposing the intervention at the binding
link. Also — do not accuse the vendor of dishonesty. The claim that more pixels capture more
detail is true *in good light*. It is wrong here because of the specific condition, and that is
the argument to make.

---

## E3.3 — Identification at a rear service door, no visible light, colour wanted

**(a) The conflict, precisely.**

Clothing colour requires the sensor to receive **visible** light, because colour information comes
from the red, green, and blue filters over the photosites. At night the camera has three
possibilities: run in colour mode (needs visible light, which is prohibited), switch to monochrome
with IR illumination (works, but IR carries **no colour information at all**), or run in colour
mode at very low light (which forces a slow shutter and high gain — smeared, noisy, and still not
reliably colour-accurate).

So: **"no visible light" and "clothing colour at night" are mutually exclusive.** This is not a
budget or product problem; it is a physical one, and no camera resolves it.

**(b) Three options.**

| Option | Delivers | Gives up |
|---|---|---|
| **1. IR illumination, monochrome at night** | Reliable identification-grade facial capture at night, invisible to neighbours, low cost | **All colour information.** Clothing described only by shade and pattern |
| **2. Low-level visible light, shielded and aimed** | Colour retained; identification retained; some deterrent value | Requires neighbour and possibly planning acceptance `[VERIFY]`; risk of complaints; higher cost. Full cut-off shielded fixtures aimed down at the door apron often survive objections that floodlights do not |
| **3. White-light illuminator triggered on detection** | Dark most of the time, colour at the moment that matters, strong deterrent | Only captures **after** the trigger fires — the approach is lost; false triggers annoy neighbours; the moment of activation may be the moment the subject turns away |

*(A fourth, sometimes correct: accept monochrome at the door and place a colour camera further
inside where light is permitted, capturing the subject after entry.)*

**(c) Recommendation and what goes in writing.**

Recommend **option 1**, with option 3 as a priced alternate.

> The rear door will be monochrome at night. We are using infrared illumination because visible
> light is not permitted at this elevation, and infrared images carry no colour — a witness
> description like "red jacket" cannot be confirmed or contradicted from this camera's night
> footage. Facial identification is unaffected and will meet the requirement. If clothing colour
> at night is important to you, the options are low-level shielded visible lighting at the door
> apron, which would need neighbour agreement, or a detection-triggered white light, which gives
> colour only from the moment it fires. Please confirm which you would like us to carry.

**What is being graded:** naming the conflict as physical rather than commercial; giving genuinely
distinct options rather than three flavours of one; and — the real point — **putting the loss in
writing and asking for a decision**. The failure mode this exercise trains against is delivering
an IR system and letting the client discover the monochrome limitation after an incident.

---

## E3.4 — Why "0.002 lux" may beat "0.05 lux" on paper and lose on site

**Three ways the ratings can differ** (any three of these earn credit):

1. **Video level.** One vendor quotes the illuminance producing 50% video level, another 30%. The
   30% figure yields a much lower — better-sounding — lux number for the identical sensor.
2. **IR cut filter in or out.** With the filter removed the sensor also collects near-infrared,
   dramatically improving the number, at the cost of being **monochrome**. A colour-mode rating and
   a monochrome rating are not comparable quantities.
3. **Shutter speed.** A rating taken at 1/4 s collects 30× the light of one taken at 1/125 s. A
   camera "rated" at a shutter that smears every moving subject is rated at a setting you can
   never use.
4. **Gain.** Maximum gain with heavy noise reduction produces a bright, smooth, detail-free image
   that satisfies a "usable video" criterion.
5. **Target reflectance.** A high-reflectance test chart returns far more light than a person in
   dark clothing.
6. **Lens aperture.** The rating is quoted with a specific lens at a specific f-number, often the
   fastest available; your installed lens may be two stops slower.

**What to do instead:**

- Design with the **exposure budget in stops** — self-consistent, no vendor input required.
- Write a **testable** requirement: *"shall produce an identification-grade facial image of a
  subject walking at 3 mph, in colour, at 1/125 s, at the design illuminance of X lux."* Every
  term is measurable at handover.
- **Run a site shootout.** Candidate cameras, on the real scene, at night, with a person walking.
  One evening. It is the only evidence that answers the question, and it changes the answer often
  enough to justify itself every time.

---

## E3.5 — 🧠 The "washed out, grey, flat" retail entrance

**(a) Most likely cause.**

**Multi-exposure WDR enabled by default, on a scene with high dynamic range** (a retail entrance
has daylight through the doors against interior lighting), combined with aggressive noise reduction
and tone mapping on the higher-resolution camera. WDR is compressing the scene's very wide
brightness range into the display range, which by construction reduces local contrast everywhere.
The higher-resolution sensor's smaller photosites also mean more gain for the same interior light,
and the resulting noise reduction smooths remaining texture.

**(b) Why the old cameras looked better while capturing less.**

The old cameras had **narrower dynamic range and no WDR**, so they simply clipped: the doorway
blew out to white and the interior shadows crushed to black. That produces a **high-contrast,
"punchy," subjectively sharp-looking image** — because contrast is what the eye reads as sharpness.
But the clipped regions contain *no data at all*. Anyone standing in the bright doorway was a pure
white silhouette; anyone in the shadow was pure black.

The new cameras are retaining detail across the whole range, which necessarily means no part of the
image uses the full black-to-white span, which reads as flat and grey. **They capture strictly more
information and look worse.** This is the general and counter-intuitive lesson: subjective image
appeal and evidentiary information content are different quantities, and they routinely move in
opposite directions.

**(c) What to change, and what to measure.**

*Change, in order of preference:*

1. **Fix the scene geometry first.** Re-aim so the glass doors are not directly in frame behind
   the subject, or move the camera to shoot across the entrance rather than into it. This reduces
   the dynamic range the camera has to span and is free.
2. **Tune WDR down rather than off.** Default WDR is usually set aggressively. Reducing the level
   restores contrast while keeping the highlight retention that matters. Turning it fully off
   returns to clipping, which is not an improvement even if the client prefers the look.
3. **Add interior light near the entrance** to lift the shadow end toward the daylight end,
   shrinking the range at source. This is the intervention with no image penalty.
4. **Review noise reduction and sharpening** settings, which are frequently the actual source of
   the "smeared" quality distinct from the flatness.

*Measure, to confirm:*

- **Walk a test subject** through the entrance at the worst hour and evaluate the **recording**,
  not the live view — can you identify them, in both the doorway and the interior?
- Measure illuminance inside and at the doorway to quantify the actual dynamic range you are
  asking the camera to span.
- Compare before/after on the **same subject in the same positions**, because the client's
  complaint is comparative and your evidence must be too.

> 🧠 **The conversation to have.** The client is describing a real perception accurately and
> drawing the wrong conclusion from it. Do not tell them the image is fine — it is not what they
> want. Show them a subject standing in the doorway on both systems: on the old one the person is
> a white silhouette, on the new one they are identifiable and flat. That single comparison makes
> the case in five seconds and no amount of explanation does it as well.

---

## Retrieval check — answers

1. **`√N`** — signal-to-noise scales with the square root of photon count, so 4× the photons is
   2× the SNR.
2. **No.** Gain amplifies signal and noise equally. It changes brightness, not information.
3. **Exactly 2.00 stops**, lost.
4. From the **motion in the scene**: pick a smear budget (25% of eye-to-eye is a defensible one),
   convert to feet, divide by subject speed. Speed sets the shutter.
5. **Adding light to the scene.** Every other source of stops costs depth of field, noise, or
   pixel density.
6. **Identify anyone.** Thermal detects presence and movement; it carries no facial detail, colour,
   text, or plate.
7. **All colour information.** IR images are monochrome.
8. Because the conditions are chosen by the vendor — video level, IR cut filter in/out, shutter
   speed, gain, target reflectance, and lens aperture all differ between datasheets.
9. **Maximum gain** and **slowest shutter (maximum exposure time).** Uncapped, the camera will
   choose a bright, smeared, noisy image over a dark, sharp one — and a dark sharp image can be
   brightened in review, while a smeared one can never be unsmeared.
