# Solutions — 04 DORI and Pixel Density in Practice

> Work the exercises in [`../04_dori_and_pixel_density.md`](../04_dori_and_pixel_density.md) before
> reading this. All numeric values were produced by running
> [`../../28_Calculators/psec/optics.py`](../../28_Calculators/psec/optics.py) and transcribed.

Targets used: detect **8 ppf**, observe **19 ppf**, recognise **38 ppf**, identify **76 ppf**.
Overlap allowance **15%** (effective width = raw × 0.85) `[PRACTICE]`.

---

## E4.1 — Assign the class

**(a) Warehouse yard, dispatch a patrol to the right quadrant.**
**Detect (8 ppf).** The decision is *where do I send someone*, which needs position and presence
only. Anything above detect here is money that belongs in the zones where identity matters.

**(b) Pharmacy controlled-substance cabinet, 12 named staff.**
**Recognise (38 ppf).** The candidate set is 12 people known to the reviewer, so the viewer
supplies most of the identifying information. Note the caveat: if the footage might support a
criminal prosecution — and with controlled substances it well might — the client should be asked
the standalone question, because a diversion investigation can end up in front of people who do
not know the staff. **This is the case where the engineering answer and the legal answer can
differ, and the right move is to raise it rather than decide it.** `[VERIFY]`

**(c) Public library entrance, police may request footage of an unknown person.**
**Identify (76 ppf).** "Unknown person" and "police request" together mean the image must stand
alone for a viewer who has never met the subject. This is the definitional identify case.

**(d) Production line, checking eye protection.**
**Observe (19 ppf).** The question is behaviour and state, not identity — *are they wearing it*,
not *who is not wearing it*. If the requirement became disciplinary action against a named
individual, it would move to recognise, and that is a different requirement worth confirming
before designing.

**(e) Data hall aisle, contractors changing weekly, not known by sight.**
**Identify (76 ppf).** This is the trap in the set. The phrase "confirm which contractor" sounds
like recognise, and the pool is even bounded. But **the reviewer does not know them by sight and
the pool changes weekly**, so the image cannot lean on viewer familiarity — it must carry the
information itself, which is identify. **Recognise vs. identify is decided by what the viewer
brings, not by how small the candidate set is.**

---

## E4.2 — 90 ft dock elevation

**(a) Recognise with 4 MP (2688 px).**

```
raw width per camera       = 2688 / 38.0 = 70.74 ft
effective (15% overlap)    = 70.74 × 0.85 = 60.13 ft
cameras                    = ceil(90 / 60.13) = 2
```

**Two cameras.**

**(b) Identify instead.**

```
raw width       = 2688 / 76.0 = 35.37 ft
effective       = 30.06 ft
cameras         = ceil(90 / 30.06) = 3
```

**Three cameras** — one more, a 50% increase for this elevation. (Note it is *not* the clean 2×
of worked example 4.1: at 90 ft the ceiling function rounds in the client's favour. On a 120 ft
frontage the same step is 2 → 4.)

**(c) The 8 MP (3840 px) option.**

```
recognise: raw 101.05 ft → effective 85.89 ft → ceil(90/85.89) = 2 cameras
identify:  raw  50.53 ft → effective 42.95 ft → ceil(90/42.95) = 3 cameras
```

| | 4 MP | 8 MP |
|---|---|---|
| Recognise | 2 | **2** |
| Identify | 3 | **3** |

**The 8 MP option buys nothing on this elevation.** Identical camera counts at both classes.

> 🧠 **This is the most valuable result in the exercise, and it generalises.** Camera count is a
> **ceiling function**, so resolution gains only convert into fewer cameras when they cross an
> integer boundary. Here, 85.89 ft of effective coverage is not enough to cover 90 ft with one
> camera, so the extra pixels are entirely wasted — while still costing more per camera, doubling
> the bitrate and storage, and losing two stops of light. **Always compute the count before
> accepting a resolution upgrade as a saving.** Vendors quote coverage width, which is continuous
> and always looks better; you buy cameras, which are integers.

**(d) When 8 MP is the wrong answer even with fewer cameras.**

Whenever the dock is **light-limited at night**. From [lesson 03](../03_sensors_and_low_light.md),
2 MP → 8 MP on a fixed sensor costs exactly **2.00 stops**, and 4 MP → 8 MP costs **1.03 stops**.
A dock apron is an outdoor, poorly lit, high-motion scene — vehicles and people moving, often at
speed, often at night — which is the exact profile where the exposure budget binds. Trading a stop
of light for pixel density that the ceiling function throws away is the worst available deal.

The general condition: **8 MP is wrong wherever the exposure budget is already short and the
geometry has margin.** Check the light before the pixels.

---

## E4.3 — The "80 ppf, meets identify" claim

**(a) Two things wrong with the specification as written.**

1. **No distance is stated.** PPF falls as `1/D`
   ([32/02](../../32_Engineering_Math/02_pixel_density.md)), so "80 ppf" without a distance is not
   a specification. It is a number that is true somewhere.
2. **It almost certainly uses floor distance rather than slant range.** The camera is at 14 ft and
   the face plane is at 5 ft, so the actual optical path is longer than the 30 ft plan dimension.
   A claim computed from the drawing dimension overstates the delivered density.

*(A third, also creditable: no depression angle is stated, and at 14 ft mounting height it needs
checking.)*

**(b) Slant range and depression angle.**

```
D_slant = √(30.0² + (14.0 − 5.0)²) = √(900 + 81) = √981 = 31.32 ft
θ       = arctan(9.0 / 30.0) = 16.70°
```

**(c) Do you accept the claim?**

Correcting for slant range:

```
slant / floor  = 31.32 / 30.00 = 1.0440   → PPF overstated by 4.40%
corrected PPF  = 80 / 1.0440 = 76.63 ppf
```

**The claim survives — 76.63 ppf against a 76 ppf threshold — by 0.8%.**

**Do not accept it as written.** It is technically true and practically worthless, because the
entire design margin has been consumed by an error the designer did not know they were making. At
0.8% margin, the class is lost by any of: a subject standing 1 ft further back, a lens 5% off its
nominal focal length `[MFR][VERIFY]`, a shorter person whose face plane is below 5.0 ft, or a
sensor whose actual imaging width differs slightly from the format table.

**What to ask for:**

> Please restate the pixel density at the **slant range** to the 5 ft face plane, with the distance
> and the mounting height shown, and confirm the depression angle. Our check makes it 76.6 ppf at
> 31.3 ft, which meets identify with under 1% margin — that is too thin to build on. Either move
> the camera closer, go one step longer on the lens, or reclassify the zone to recognise and record
> the decision.

The depression angle at 16.70° is fine — comfortably inside the ~30° practice limit — so that part
of the design is sound and should be said so.

> 🧠 **The transferable habit:** when a claimed value lands within a few percent of a threshold,
> treat that as a *finding*, not a pass. Designs that just barely meet a target usually meet it by
> accident, and the accident is normally a missing correction.

---

## E4.4 — Documented consequence block, self-storage corridors

> **Zone:** Interior storage corridors, Buildings A–D, all levels.
>
> **Recommended target:** Recognise (38 ppf) at the corridor centreline, 5 ft above finished
> floor.
>
> **Target adopted:** Detect (8 ppf), per budget direction of [date].
>
> **Consequence:** Video from the interior corridors will establish that a person was present, the
> time, the direction of travel, and which unit ranges they approached. It will **not** support
> identification of an unknown individual, and will not reliably support recognition of a known
> tenant or member of staff. Where an incident occurs inside a corridor and the person's identity
> is in question, the investigation will depend entirely on correlating corridor timestamps
> against the building entrance cameras and the access-control record for that period. If a
> subject entered on a tenant's credential and the corridor footage cannot confirm they were that
> tenant, the record will show only which credential was used.
>
> **Compensating measures:** (i) Identify-grade cameras at both building entrances, capturing every
> person entering and leaving, retained 90 days. (ii) Access-control transaction logging retained
> for the same period, time-synchronised to the video system via NTP so corridor timestamps can be
> correlated. (iii) Corridor cameras positioned to capture direction of travel and unit range
> unambiguously, so the entrance capture can be tied to a location.
>
> **Residual risk accepted by:** [name, role, date]

**What is being graded:**

- The consequence is written in **operational** terms (what an investigation will and will not be
  able to conclude), not in pixels. The person signing must be able to evaluate it.
- It names the **specific failure case** — a subject using someone else's credential — because
  that is the realistic incident and the one where detect-grade corridors actually bite.
- The compensating measures are real and connected: entrance capture is only useful if the
  timestamps correlate, which is why **NTP synchronisation is listed as a compensating measure**
  rather than assumed. Correlation is the entire mechanism by which the compromise works.
- It is signed by a named person in a named role. An unsigned block is a note to yourself.

---

## E4.5 — 🧠 Identify-grade coverage of a 400-space car park

**(a) Order of magnitude.**

Assumptions, stated: double-loaded aisles at 40 spaces each → **10 aisles**; 9 ft space width, 20
spaces per side → each aisle **180 ft** long; 4 MP cameras; 15% overlap; coverage of the aisle
centreline only.

```
identify:  effective width 30.06 ft → ceil(180/30.06) = 6 cameras per aisle → 60 cameras
recognise: effective width 60.13 ft → 3 per aisle → 30 cameras
detect:    effective width 285.60 ft → 1 per aisle → 10 cameras
```

**Roughly 60 cameras** for identify, against **10** for detect — a **6× multiplier**, before
counting perimeter, entries, or overlap between aisles.

And that 60 covers only the **aisle centreline**. A person standing between two parked vehicles is
occluded from an aisle-aligned camera regardless of pixel density, so genuine identify-grade
coverage of the whole surface is materially worse than 60 — plausibly double. **The honest answer
to the client is "somewhere between 60 and 120 cameras, and I am not confident the upper figure
achieves it either."**

**(b) The two strongest reasons it still fails at night.**

1. **The exposure budget.** An open car park at night is a low-light, high-dynamic-range scene:
   pools of light under poles, deep shadow between them, and headlights sweeping through. From
   [lesson 03](../03_sensors_and_low_light.md), holding 1/125 s for a walking subject requires an
   illuminance most car parks do not have, and uniformly across 400 spaces at that. The cameras
   will settle on slow shutters and high gain, and the geometric 76 ppf will not deliver an
   identifiable face. **60 cameras that all meet the pixel target and none of which identify
   anyone is the realistic outcome.**
2. **Pose and occlusion.** People in a car park face wherever they are going, which is rarely the
   camera; they bend into boots and door wells; they are screened by vehicles, pillars, and each
   other. Identification requires a cooperative or at least forward-facing subject, and a car park
   surface is the least cooperative geometry there is. Pixel density does nothing about the back of
   a head.

*(Also creditable: depression angle. Pole-mounted cameras at 20–25 ft produce steep angles over
nearby spaces — [lesson 01](../01_imaging_chain.md)'s point that a 20 ft pole camera will never
identify anyone directly beneath it.)*

**(c) The alternative design, and why it is better rather than cheaper.**

**Start from the actual stated risk: vehicle break-ins.** That risk has a specific structure —
offenders must enter the lot, move through it, and leave, usually on foot or in a vehicle, and
almost always through a small number of entry and exit points.

> **Proposed design.**
> - **Identify-grade capture at the entry and exit chokepoints**, on foot and vehicular, where
>   subjects are moving slowly, facing a predictable direction, and can be lit properly and
>   cheaply because the area is small. Plus dedicated plate capture on the vehicle lanes, with its
>   own lens and exposure ([lesson 02](../02_optics_and_lenses.md)). Roughly **4–6 cameras.**
> - **Detect-grade area coverage across the aisles** — about **10 cameras** — to establish
>   presence, movement, and timeline, and to direct a patrol to the right quadrant.
> - **Lighting brought to a uniform, verified level** across the surface, specified in lux at a
>   named plane per [lesson 03](../03_sensors_and_low_light.md).
> - The saving from ~60 cameras to ~16 spent on the lighting and on the chokepoint cameras being
>   genuinely good ones.

**Why it is better, not merely cheaper:**

- **It captures identity where identity is capturable.** Chokepoints give a slow, forward-facing,
  well-lit subject. That is where an identifiable image comes from. The 60-camera design spends
  everything on the surface, which is where identification is *hardest*, and captures identity
  nowhere.
- **It matches the investigative narrative.** An investigator asks: who came in, when, in what
  vehicle, where did they go, when did they leave. Chokepoint identify plus surface detect answers
  all five. Sixty identify-grade aisle cameras answer "who" badly and the rest not at all.
- **The lighting improves every camera at once, and deters independently.** `[PRACTICE]` Lighting
  is the one intervention with no image penalty, and it is a recognised deterrent for opportunistic
  vehicle crime in its own right — which is the client's actual goal, and something no amount of
  recording achieves ([lesson 01](../01_imaging_chain.md): prevents vs. documents).
- **It is maintainable.** Sixty cameras across an open lot is a decade of aiming drift, dirty
  domes, spider webs, and PoE faults, monitored by nobody. Sixteen is a system that can actually
  be kept working — see [lesson 11](../11_analytics_and_health.md).

**How to present it:** do not open with the cost. Open with *"identify-grade coverage of an open
surface lot does not work at night even when you buy it, and here is why"* — then show the 60-camera
figure, then the alternative. The client's objection is that you are cutting scope; the answer is
that the scope they asked for does not deliver what they want, and this one does.

---

## Retrieval check — answers

1. **Detect** (8 ppf) — is something there? **Observe** (19) — what is it doing? **Recognise**
   (38) — is that someone I know? **Identify** (76) — who is that, to a stranger?
2. **What the viewer brings.** Recognise relies on the viewer already knowing the person; identify
   requires the image to stand alone. It matters legally because evidence is usually assessed by
   people who did not know the subject.
3. Pixel density **× 2**; camera count on a fixed frontage **× 2** (subject to ceiling effects —
   see E4.2(c)).
4. Any four of: motion, depression angle, compression, light, occlusion/pose, and the viewer's
   task (cross-racial identification, stills, fatigue).
5. Because PPF falls as `1/D`, so the figure is meaningless without the distance — and the
   distance must be the **slant range**, not the plan dimension.
6. The **recommendation**, the **consequence in operational terms**, and the **compensating
   measure** — plus a named person accepting it.
7. **A chokepoint.** More pixels cannot fix pose, motion, or light; making the subject slow down
   and face a well-lit camera fixes all three at once.
