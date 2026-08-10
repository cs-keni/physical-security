# 04 — DORI and Pixel Density in Practice

> **Prerequisite:** [`../32_Engineering_Math/02_pixel_density.md`](../32_Engineering_Math/02_pixel_density.md).
> That lesson derives `PPF = px / W`, the `1/D` falloff, `D_max = (px·f)/(PPF·w)`, and the
> conversion between px/ft and px/m. **This lesson does not re-derive any of it.**
>
> The math answers *what pixel density does this camera deliver*. This lesson answers the question
> that actually governs the design: **which class does this scene need, who decides, and what does
> choosing wrong cost?**
>
> This file is referenced by name from
> [`../28_Calculators/psec/optics.py`](../28_Calculators/psec/optics.py) — the `DORI_PPF` table's
> comment points here for when to exceed the minima and why.

## Learning objectives

- State the four DORI classes and, more importantly, the **operational question** each answers.
- Distinguish **recognise** from **identify** precisely, and explain why the difference is legal
  as much as technical.
- Derive a per-zone pixel target from the decision the video must support.
- Quantify what raising a target one class costs in cameras — it is not linear in the way people
  expect.
- Name the six conditions under which DORI minima **understate** the requirement.
- Defend a lower target in writing, with the consequence recorded.

---

## The classes, briefly

`[STANDARD][VERIFY]` IEC 62676-4 defines four criteria in pixels per metre. The per-foot values
used in this academy and in `psec` are those figures converted (1 m = 3.28084 ft) and rounded to
values in common practice:

| Class | px/m (standard) | px/ft (`psec`) | The question it answers |
|---|---|---|---|
| **Detect** | 25 | 8 | *Is something there?* |
| **Observe** | 62.5 | 19 | *What is it doing?* |
| **Recognise** | 125 | 38 | *Is that someone I already know?* |
| **Identify** | 250 | 76 | *Who is that, to someone who has never met them?* |

Converting back confirms the rounding is honest: 8 ppf = 26.2 ppm, 19 ppf = 62.3 ppm, 38 ppf =
124.7 ppm, 76 ppf = 249.3 ppm. Close enough that the class boundaries hold; **state which unit
system you designed in**, because a reviewer working in px/m and finding your px/ft figures will
otherwise assume an error.

> ⚠️ **These are minima under good conditions, not design targets.** The standard's figures assume
> a cooperative subject, adequate light, a reasonable viewing angle, and an image not degraded by
> motion or compression. Every one of those assumptions fails somewhere on a real site. The whole
> rest of this lesson is about the gap between the minimum and the target.

## Recognise vs. identify: the distinction that matters most

This is the most consequential and most misused pair in the discipline.

**Recognise (38 ppf)** means a viewer **who already knows the person** can say that is them. The
viewer supplies most of the information — gait, build, habitual clothing, the fact that only six
people have access to that corridor. This is the right target for insider scenarios: *which of our
staff opened that cabinet?*

**Identify (76 ppf)** means a viewer **who has never met the person** can pick them out — from a
photograph, a line-up, or a database. The image must carry the information by itself.

**Why the difference is legal, not just technical.** Evidence in a criminal matter is normally
assessed by people who did not know the subject. A "recognise"-grade image can be entirely
sufficient for an employer to have a conversation with a named employee, and entirely insufficient
to support a prosecution of a stranger. `[VERIFY — evidentiary standards vary by jurisdiction and
are a legal question, not an engineering one.]`

> 🧠 **The question to ask the client, in these words:** *"If this ends up in front of someone who
> has never met the person on the screen, does the image need to stand on its own?"* Their answer
> selects the class. It is a better question than "do you want to identify people?", which always
> gets a yes.

## Deriving the target from the decision

**Every pixel target traces to a decision someone will make from the video.** Work it backwards.

| The decision to be supported | Class | Why |
|---|---|---|
| Dispatch a guard to a zone; know a person is in the yard | **Detect** | Position and presence is all that is needed |
| Confirm whether the loading door is open, whether a queue formed, whether someone fell | **Observe** | Behaviour, not identity |
| Determine which of ~40 known staff entered the server room | **Recognise** | The viewer knows the candidate set |
| Support a prosecution of an unknown intruder; confirm a badge photo against the person who used it | **Identify** | The image must stand alone |
| Read a number plate | **Special case** | Not a DORI class. Plate capture has its own pixel-per-character requirement, its own lens, and its own exposure — see [lesson 02](02_optics_and_lenses.md) |

**Zones inherit targets, cameras deliver them.** Set the target per zone
([`../01_Foundations/04_defense_in_depth_and_zones.md`](../01_Foundations/04_defense_in_depth_and_zones.md)),
then design cameras to meet it. Do not set targets per camera — that is how a design ends up with
an identify-grade camera on a car park and a detect-grade camera on the cash office.

## 🧮 Worked example 4.1 — what a class upgrade actually costs

A 4 MP camera has **2688** horizontal pixels. The scene width one camera can hold at each class
follows directly from `PPF = px / W`:

| Class | Target PPF | Max scene width per camera |
|---|---|---|
| Detect | 8.0 | **336.00 ft** |
| Observe | 19.0 | **141.47 ft** |
| Recognise | 38.0 | **70.74 ft** |
| Identify | 76.0 | **35.37 ft** |

Now apply it to a **120 ft retail frontage**, with a realistic 15% overlap allowance for continuity
of coverage:

| Class | Effective width per camera | Cameras required |
|---|---|---|
| Detect | 285.60 ft | **1** |
| Observe | 120.25 ft | **1** |
| Recognise | 60.13 ft | **2** |
| Identify | 30.06 ft | **4** |

**Each step up the DORI ladder doubles the pixel requirement and therefore doubles the camera
count.** Detect to identify is a factor of **9.5× in pixel density** and **4× in cameras** on this
frontage — and each of those cameras also brings a licence, a switch port, PoE budget, bandwidth,
storage, and a maintenance obligation for ten years.

> 🧠 **This table is the most useful thing in the lesson to have in your head during a client
> meeting.** When someone says "let's just make them all identify," you can answer in one
> sentence: *"That takes this elevation from one camera to four, and the same multiplier applies
> across the site."* The conversation immediately becomes what it should have been — **which zones
> genuinely need identify** — instead of a blanket setting nobody costed.

The same relationship expressed as range, for the Meridian lobby camera (4 mm lens, 1/2.8" sensor,
2688 px):

| Class | Maximum range still meeting it |
|---|---|
| Detect | 250.3 ft |
| Observe | 105.4 ft |
| Recognise | 52.7 ft |
| Identify | **26.3 ft** |

Put these numbers on the coverage drawing as **rings**, not as a single cone. A camera does not
"cover" an area; it covers different areas to different standards, and the drawing should say so.
This is the single change that most improves a camera coverage plan, and it is what
[lesson 09](09_camera_placement.md) builds on.

## The six conditions where DORI minima understate the requirement

The standard's numbers assume near-ideal conditions. Design **above** the minimum when any of
these apply — and most real scenes carry at least two.

1. **Motion.** [Lesson 01](01_imaging_chain.md) showed motion smear consumes facial detail
   independently of pixel density, and the smear-to-detail ratio is invariant under PPF. A subject
   moving at speed needs either faster shutter (light) or a chokepoint — **not more pixels.**
   Meeting 76 ppf on a running subject at 1/30 s identifies nobody.
2. **Depression angle.** Beyond roughly 30°, faces foreshorten and identification degrades no
   matter how many pixels are on target `[PRACTICE]`. A high mount can meet identify numerically
   and fail it in practice. See [32/01](../32_Engineering_Math/01_camera_fov.md).
3. **Compression.** DORI is a **geometric** measure taken before the encoder. A heavily compressed
   stream, or a smart codec deprioritising a moving subject, delivers fewer usable pixels than the
   geometry promises. See [lesson 06](06_compression_and_bandwidth.md).
4. **Light.** Every class assumes an adequately exposed image. At the noise levels typical of an
   underlit scene, real discriminable detail is well below the geometric pixel count.
   See [lesson 03](03_sensors_and_low_light.md).
5. **Occlusion and pose.** Hoods, hats, masks, sunglasses, and simply looking away defeat facial
   identification at any density. Design the **capture point** where the subject must face the
   camera — a door they pull open, a turnstile, a queue — rather than adding pixels to a corridor.
6. **The viewer's task.** Cross-racial identification, identification from a still rather than
   video, and identification by someone examining hundreds of frames are all harder than the
   standard's implied case. `[VERIFY]` This is a human-factors question, treated in
   [`../36_Human_Factors_Privacy_Ethics/`](../36_Human_Factors_Privacy_Ethics/) *(not yet written)*.

> ⚠️ **The synthesis, and the sentence to remember:** *pixel density is a necessary condition, never
> a sufficient one.* A design that meets 76 ppf and ignores angle, light, motion, and pose has
> satisfied the arithmetic and not the requirement. The arithmetic is the part that gets checked in
> review, which is exactly why the rest gets missed.

## Choosing wrong, in both directions

**Too low** is the failure everybody anticipates: the incident happens, the footage exists, and
nobody can say who it was. The cost is borne years later by someone who was not in the design
meeting.

**Too high is also a failure**, and it is the one engineers commit:

- Cameras multiply, as worked example 4.1 shows, and with them licences, ports, PoE, bandwidth,
  storage, and a decade of maintenance.
- The budget is finite, so **money spent over-specifying one zone is money not spent on the zone
  that needed it** — very often the lighting that would have made the existing cameras work.
- Systems that cost more than the risk justifies get value-engineered by someone with no security
  background, late, badly, and uniformly across the site.

> 🧠 **The senior move is to be the person who proposes the reduction.** Walking into a review and
> saying "three of these eleven identify-grade positions should be recognise, and here is the
> reasoning, and here is what I want to spend the saving on" is the single most credibility-building
> act available to you. It also protects the zones that genuinely need identify, because you have
> shown the targets were reasoned rather than reflexive.

## Defending a lower target in writing

Sometimes the budget will not carry the correct target. This is legitimate — it is the owner's risk
to accept — **provided the consequence is recorded**. The pattern:

> **Zone:** East car park, rows 4–7.
> **Recommended target:** Recognise (38 ppf) at the aisle centreline.
> **Target adopted:** Detect (8 ppf), per budget direction of [date].
> **Consequence:** Video from this zone will establish that a person or vehicle was present and
> where it moved. It will **not** support identification of an unknown individual, and will not
> reliably support recognition of a known one. Incidents in this zone requiring identification
> will depend on the identify-grade cameras at the two entry points, which capture everyone
> entering and leaving on foot.
> **Compensating measure:** Entry/exit choke cameras at identify grade, retained 90 days.
> **Accepted by:** [name, role, date]

Three things this does. It records the engineering recommendation, so the decision is visible as a
decision. It states the consequence in **operational** terms the owner can evaluate, not in
pixels. And it names the compensating measure — which is the part that turns a compromise into a
design rather than a gap.

## Design tradeoffs

| Decision | Buys | Costs | Note |
|---|---|---|---|
| Raise one DORI class | 2× pixel density | **2× cameras** on a given frontage, plus everything each camera drags with it | The multiplier compounds site-wide |
| Higher-resolution camera instead of more cameras | Density without more positions | Low light (2 stops for 2 MP → 8 MP), bitrate, storage | Only where light is ample — [lesson 03](03_sensors_and_low_light.md) |
| Longer lens instead of more cameras | Density at range | Narrower FOV; **DOF collapses ~1/f²** | [Lesson 02](02_optics_and_lenses.md) |
| Move the camera closer | Density, and a shallower depression angle | Coverage area; may need more positions | Usually the cheapest real fix |
| Design a chokepoint | Identification at one point instead of everywhere | Architectural change; client cooperation | **The highest-leverage move available** |
| Accept a lower class, document it | Budget for the zone that needs it | Capability, knowingly | Only with the written consequence above |

## Common mistakes

⚠️ **Setting one pixel target for the whole site.** Either you have over-specified the car park or
under-specified the cash office. Targets are per zone.

⚠️ **Confusing recognise with identify.** They differ by 2× in density and by a great deal more in
what the footage can be used for.

⚠️ **Quoting a camera's pixel density without stating the distance.** PPF falls as `1/D`
([32/02](../32_Engineering_Math/02_pixel_density.md)). "This camera does 90 ppf" is meaningless.
"90 ppf at 22 ft" is a specification.

⚠️ **Drawing coverage cones instead of class rings.** A cone implies uniform capability across an
area that in reality drops from identify to detect within its own footprint.

⚠️ **Treating the geometric number as the delivered number.** Light, motion, angle, pose, and
compression all sit between them.

⚠️ **Using floor distance instead of slant range.** Overstates PPF for every indoor camera; see
[32/01](../32_Engineering_Math/01_camera_fov.md).

⚠️ **Specifying identify everywhere because it is safer.** It is not safer. It consumes the budget
that the binding constraints — light, and the zones that genuinely need identify — were going to
need.

## Junior vs. Senior

| | Junior | Senior |
|---|---|---|
| Sets targets | Per camera, or one for the site | **Per zone, from the decision the video must support** |
| Asked "do you want to identify people?" | Takes the yes | Asks whether the image must stand alone for a stranger |
| Presents coverage as | A cone per camera | **Class rings** — identify to X ft, recognise to Y ft |
| Reports pixel density as | "90 ppf" | "90 ppf at 22 ft slant, at a 9° depression angle" |
| Treats DORI minima as | The target | The floor, then adds margin for motion, angle, light, and compression |
| Handles a budget cut by | Reducing camera count uniformly | Proposing specific class reductions with written consequences and a compensating measure |
| Sees an identification problem and | Specifies more pixels | Asks whether a chokepoint could make the subject stop and face the camera |

## 🔧 Field exercise

1. At a site you can access, list every distinct zone and write the **decision** someone would
   need to make from video in that zone. One sentence each. If you cannot write one, note that —
   it is a finding.
2. Assign a DORI class to each zone from the decision, not from the equipment present.
3. For two zones, compute the actual delivered PPF of the installed camera at the distance that
   matters, using `psec.optics` and the real mounting geometry.
4. Compare assigned to delivered. Note every zone that is over-specified as well as under —
   both are findings and the over-specified ones are the more interesting conversation.

## Exercises

Work these before opening
[`_solutions/04_dori_and_pixel_density_solutions.md`](_solutions/04_dori_and_pixel_density_solutions.md).

**E4.1** For each, state the DORI class and one sentence of justification:
 (a) A warehouse yard where the requirement is to dispatch a patrol to the right quadrant.
 (b) A pharmacy controlled-substance cabinet accessed by 12 named staff.
 (c) A public library entrance where police may later request footage of an unknown person.
 (d) A production line where the question is whether operators are wearing eye protection.
 (e) A data hall aisle where the requirement is to confirm which contractor opened a cabinet, from
     a pool of contractors who change weekly and are not known by sight to the reviewer.

**E4.2** A 90 ft warehouse dock elevation must be covered at **recognise**. Available cameras are
4 MP (2688 px).
 (a) How many cameras, with a 15% overlap allowance?
 (b) The client asks what identify would cost instead. Answer with a number.
 (c) An 8 MP (3840 px) option is offered. Recompute (a) and (b) for it.
 (d) Given [lesson 03](03_sensors_and_low_light.md), state the condition under which the 8 MP
     option is the wrong answer even though it needs fewer cameras.

**E4.3** A camera is specified as delivering "80 ppf, meets identify." On the drawing it is
mounted at 14 ft, and the subject of interest is at 30 ft floor distance.
 (a) Name two things wrong with the specification as written.
 (b) Compute the slant range and the depression angle.
 (c) State whether you would accept the claim, and what you would ask for.

**E4.4** Write the documented-consequence block (using the pattern in this lesson) for the
following: a self-storage facility's interior corridors are specified at **detect** rather than the
recommended **recognise**, on budget grounds, with identify-grade cameras retained at the two
building entrances.

**E4.5** 🧠 A client insists on identify-grade coverage across a 400-space open car park. Their
stated reason is vehicle break-ins. Using worked example 4.1's reasoning plus anything from lessons
01–03:
 (a) Estimate the order of magnitude of the camera count. State your assumptions.
 (b) Give the two strongest technical reasons the design would still fail at night.
 (c) Propose an alternative design that addresses the actual stated risk, and explain why it is
     better rather than merely cheaper.

## Retrieval check

1. Name the four classes and the question each answers.
2. What exactly distinguishes recognise from identify, and why does it matter legally?
3. Raising one DORI class multiplies pixel density by what, and camera count on a fixed frontage
   by what?
4. Name four of the six conditions under which DORI minima understate the requirement.
5. Why is "this camera delivers 90 ppf" not a specification?
6. What are the three components of a documented lower-target decision?
7. What is the highest-leverage intervention for identification, and why is it not more pixels?

## References

- [`../32_Engineering_Math/02_pixel_density.md`](../32_Engineering_Math/02_pixel_density.md) — the
  derivation of everything numeric in this lesson. Prerequisite.
- `[STANDARD][VERIFY]` **IEC 62676-4** — the source of the DORI criteria. Verify the current
  edition and its exact wording before quoting it in a specification; see
  [`../31_References/source_index.md`](../31_References/source_index.md).
- [`../28_Calculators/psec/optics.py`](../28_Calculators/psec/optics.py) — `DORI_PPF`, `DORI_PPM`,
  `classify_ppf`, `max_range_for_ppf_ft`. Its `DORI_PPF` comment references this lesson by name.
- `[PRACTICE]` The 30° depression-angle limit, the 15% overlap allowance, and the guidance to
  design above the minima are engineering practice, not standards.
- `[VERIFY]` Evidentiary sufficiency is a legal question that varies by jurisdiction. Engineers
  specify image quality; they do not determine admissibility.

---

**Next:** [05 — Camera Form Factors and Tradeoffs](05_camera_form_factors.md) — multisensor, PTZ,
fisheye, or four fixed domes, and the real basis for deciding.
