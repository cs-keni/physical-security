# 09 — Camera Placement Engineering

> Everything in lessons 01–08 exists to serve this one. This is where a floor plan becomes a
> design, and it is — with [lesson 03](03_sensors_and_low_light.md) — where most real designs are
> lost.
>
> Not to bad math. To cameras placed to cover **area** instead of to answer **questions**.

## Learning objectives

- Apply the governing rule: **every camera answers one written question.**
- Run the placement process from zones and decisions rather than from a floor plan and a budget.
- Compute the mounting-height envelope in which identification is actually achievable.
- Design chokepoints, and explain why they beat adding cameras.
- Draw coverage as **class rings**, and design continuity and handoff between views.
- Produce a camera schedule that survives review, construction, and ten years of operation.

---

## The rule

> **Every camera answers exactly one written question. If you cannot write the question, do not
> place the camera.**

"Cover the lobby" is not a question. These are:

- *Who passed through the north vestibule between 22:00 and 06:00, to a standard a stranger could
  identify?*
- *Did the loading dock door stand open outside scheduled delivery hours, and for how long?*
- *Which of the twelve pharmacy staff opened the controlled-substance cabinet at 14:32?*
- *Which vehicle occupied bay 14 between 09:00 and 17:00, by plate?*

Each of those determines the pixel target, the lens, the mounting height, the aim, the lighting,
the shutter, the retention, and whether the camera needs to be monitored. **The question is the
specification.** Everything else is derived from it.

⚠️ **The test that finds dead cameras in any existing design:** go camera by camera and write its
question. The ones you cannot write a question for are cameras nobody will ever look at — and they
still cost a licence, a port, PoE, bandwidth, storage, and ten years of maintenance. On most
retrofit surveys this exercise finds between 10% and 30% of the estate. Removing them funds the
lighting that makes the rest work.

---

## The placement process

Work in this order. Reversing it is the single most common cause of a design that satisfies a
drawing review and fails in service.

```
 1. ZONES         from 01_Foundations/04 — what are the security zones?
        │
 2. DECISIONS     what decision must someone make from video, per zone?
        │
 3. QUESTIONS     write the question each decision needs answered
        │
 4. TARGETS       DORI class per question  (lesson 04)
        │
 5. CONSTRAINTS   light (lesson 03), motion, angle, occlusion, privacy
        │
 6. POSITIONS     mounting points that satisfy 4 and 5 — geometry last
        │
 7. EQUIPMENT     lens, form factor, illumination  (lessons 02, 05)
        │
 8. VERIFY        compute delivered PPF at slant range; check the angle;
                  check the night exposure budget; walk it at night
```

**Steps 1–3 involve no equipment at all**, and they are the steps that get skipped. A designer who
starts at step 6 with a floor plan and a camera count produces coverage; a designer who starts at
step 1 produces evidence.

## The mounting-height envelope

The tension identified in [lesson 01](01_imaging_chain.md) — pull back for a better viewing angle,
lose pixel density; mount higher for coverage and protection, ruin the angle — has an exact
solution space.

For an identification camera (4 mm lens, 2688 px, 1/2.8" sensor, face plane 5.0 ft), requiring
**both** ≥76 ppf **and** a depression angle ≤30° `[PRACTICE]`:

| Mount height | Distances that satisfy **both** | Window width |
|---|---|---|
| 8 ft | 8 – 26 ft | **18 ft** |
| 9 ft | 8 – 26 ft | 18 ft |
| 10 ft | 10 – 24 ft | 14 ft |
| 12 ft | 14 – 24 ft | 10 ft |
| 14 ft | 16 – 24 ft | 8 ft |
| 16 ft | 20 – 22 ft | **2 ft** |
| 20 ft | **none** | **0** |

**Read the last row.** At a 20 ft mounting height there is **no distance at all** at which this
camera both resolves a face and sees it at a usable angle. Close in, the depression angle is
36–56°; far out, the pixel density has fallen below identify. This is the arithmetic behind lesson
01's claim that a 20 ft pole camera will never identify anyone — and it is not a limitation of that
camera. Fitting a longer lens raises PPF at distance but does nothing about the angle; the geometry
is the constraint.

> 🧠 **The rules that fall out of this table, and they are worth memorising:**
> 1. **Identification cameras mount low — 8 to 10 ft — and look nearly level.** Accept that they
>    cover a small area. That is what identification costs.
> 2. **Height buys coverage and vandal resistance, and spends the angle.** Above roughly 14 ft,
>    identification becomes a narrow window; above 16–18 ft it is gone.
> 3. **Overview and identification are different cameras**, because they want opposite mounting
>    heights. Trying to get both from one position is the same error as the plate-and-face camera
>    in [lesson 02](02_optics_and_lenses.md), arriving from a different direction.

## Chokepoints: the highest-leverage move available

A **chokepoint** is a place a person must pass, slowly, in a predictable direction, where you can
control the light.

Doors, vestibules, turnstiles, gates, lift lobbies, stair discharges, and queue lines are natural
chokepoints. They solve, simultaneously, every constraint that defeats identification elsewhere:

| Constraint | How a chokepoint fixes it |
|---|---|
| **Pixel density** | The subject is close and the field of view is narrow |
| **Depression angle** | You can mount low; a door frame is 7 ft, not 20 |
| **Motion** | A door slows people to near-zero and a turnstile stops them |
| **Pose** | People face the direction they are travelling — toward the camera |
| **Light** | A small area is cheap to light properly and to control |
| **Occlusion** | One person at a time |

⚠️ **Compare the alternatives honestly.** Adding pixels to a corridor addresses one of those six
constraints. Designing the capture at a chokepoint addresses all six, usually with **one** camera
where area coverage would need several.

> 🧠 **Chokepoint design is where a security engineer earns their fee, and it is often
> architectural rather than electronic.** Recommending that a second door be added to form a
> vestibule, that a turnstile line be re-ordered, or that a service corridor gain a door is a
> higher-value recommendation than any camera specification — and it frequently *reduces* the
> camera count. It also requires you to be in the conversation early, which is the argument for
> being involved at design development rather than being handed a plan at tender.

**The pattern that generalises to almost every site:** **identify at the chokepoints, observe or
detect in the areas between.** [Lesson 04](04_dori_and_pixel_density.md)'s E4.5 reached the same
conclusion for a car park by a different route, and the module capstone tests whether you reach it
unprompted.

## 🧮 Worked example 9.1 — Meridian Building 2, ground floor

```
                                NORTH  (parking lot, lit by pole lights)
   ┌──────────────────────────────────────────────────────────────────────┐
   │                                                                      │
   │    ░░░░░ GLASS CURTAIN WALL ░░░░░                                    │
   │   ┌────────────────┐                                                 │
   │   │   VESTIBULE    │ ◄── C1 identify, 8.5 ft mount, 12 ft back       │
   │   │  outer   inner │     aimed at INNER door, back to the glass      │
   │   │   ▒▒      ▒▒   │                                                 │
   │   └───┬────────┬───┘                                                 │
   │       │        │                                                     │
   │   ┌───▼────────▼──────────────────┐                                  │
   │   │                               │                                  │
   │   │         LOBBY / ATRIUM        │ ◄── C2 overview, 14 ft, observe  │
   │   │      (double height, glass)   │                                  │
   │   │   ┌──────────┐                │                                  │
   │   │   │ RECEPTION│                │ ◄── C3 recognise at the desk     │
   │   │   └──────────┘                │     9 ft mount, 14 ft back       │
   │   └────┬──────────────────┬───────┘                                  │
   │        │                  │                                          │
   │   ┌────▼─────┐      ┌─────▼──────┐                                   │
   │   │ LIFT     │      │  STAIR 1   │ ◄── C4 identify at stair          │
   │   │ LOBBY    │      │            │     discharge (chokepoint)        │
   │   └────┬─────┘      └────────────┘                                   │
   │        │                                                             │
   │   ═════╪═══════════════════════════════════  CORRIDOR  ══════════    │
   │        │        ▲                    ▲                               │
   │        │        C5                   C6      (recognise, 9 ft)       │
   │        │                                                             │
   │   ┌────▼──────────┐                        ┌───────────────────┐     │
   │   │  SERVER ROOM  │ ◄── C7 identify at     │   LOADING DOCK    │     │
   │   │               │     the door only      │                   │     │
   │   └───────────────┘     (chokepoint)       └────────┬──────────┘     │
   │                                                     │                │
   │                                            C8 ─────►│ identify at    │
   │                                            C9 ─────►│ dock personnel │
   │                                                     │ door; observe  │
   └─────────────────────────────────────────────────────┴────────────────┘
                                SOUTH  (service yard)
```

**The camera schedule, with the question each answers:**

| ID | Question it answers | Class | Mount | Notes |
|---|---|---|---|---|
| **C1** | Who entered through the main vestibule, to a standard a stranger could identify? | identify | 8.5 ft | **Aimed at the inner door with its back to the glass** — subjects are lit from the front by lobby light, not silhouetted against the curtain wall ([lesson 03](03_sensors_and_low_light.md)) |
| **C2** | What happened in the lobby, and where did people go? | observe | 14 ft | Context and continuity, not identity. High mount is correct **because** its job is coverage |
| **C3** | Who spoke to reception, and was the visitor process followed? | recognise | 9 ft | Reception knows regular visitors; the viewer supplies familiarity |
| **C4** | Who used stair 1 outside business hours? | identify | 8 ft | **Chokepoint.** Stair discharge is a door — slow, frontal, small, easy to light |
| **C5, C6** | Who moved along the ground-floor corridor and in which direction? | recognise | 9 ft | Continuity between C2 and the secure areas |
| **C7** | Which individual opened the server room door? | identify | 8 ft | **Chokepoint at the door, not coverage of the room.** Correlates with the access-control record |
| **C8** | Who entered via the dock personnel door? | identify | 8.5 ft | Chokepoint |
| **C9** | Was the dock door open outside delivery hours, and what was moved? | observe | 12 ft | A different question, so a different camera |

**Note four things about this schedule:**

1. **C7 covers a door, not a room.** The question is *which individual opened it* — answerable at
   the door with one camera, at identify grade, cheaply. Covering the room's interior at identify
   would take several cameras and answer a question nobody asked.
2. **C8 and C9 look at the same dock and are not redundant**, because they answer different
   questions and therefore need different classes, heights, and aims. When a reviewer asks why
   there are two, the questions are the answer.
3. **C1's aim is a lighting decision, not a coverage decision.** Pointed the other way it would
   frame the same doorway and produce silhouettes all day. This single choice is worth more than
   any equipment upgrade at that position.
4. **There is no camera in the lift car or the toilets corridor.** Lift car coverage is a separate
   decision (and usually a corner-mount camera owned by the lift package); the toilet approach is a
   privacy question that must be raised, decided by the client, and recorded — never decided
   silently by an engineer.

**Verification for C1** (from [lesson 01](01_imaging_chain.md)): slant range 12.50 ft, depression
angle 16.26°, scene width 16.78 ft, **160.2 ppf — 2.11× the identify threshold**, at an angle
comfortably inside 30°. And from [lesson 03](03_sensors_and_low_light.md): the night exposure
budget must be checked, because the geometry passing is not the design passing.

---

## Continuity and handoff

A person walking from the car park to the server room should be **trackable without gaps**. This is
what makes an investigation possible, and it is a property of the design as a whole rather than of
any camera.

```
   car park ──► vestibule ──► lobby ──► corridor ──► server room door
     C-park      C1            C2        C5, C6       C7
    (detect)   (IDENTIFY)   (observe)  (recognise)  (IDENTIFY)
                    ▲                                     ▲
                    └──── identity established here ──────┘
                          and re-confirmed here
```

**Identity is established once, at a chokepoint, and then *carried* by continuity.** The corridor
cameras do not need to identify anyone — they need to show, without a gap, that the person
identified at C1 is the same person who reached C7. That is why the middle of the chain can be
recognise or observe, and why breaking continuity is far more damaging than a slightly low pixel
count.

⚠️ **Gaps are where investigations die.** A person who disappears from coverage for eight seconds
and reappears is a person whose chain of identification is broken, and a competent defence will say
so. Walk the route on the drawing and mark every point where nobody is watching.

⚠️ **Overlap deliberately, not accidentally.** The ~15% overlap allowance used in
[lesson 04](04_dori_and_pixel_density.md)'s arithmetic exists for this. Two cameras that just touch
at their nominal edges have a gap in practice, because the edge of a field of view is where
distortion and falloff are worst.

## Environmental and site constraints

**Sun path.** An east-facing exterior camera looks into the sunrise; west-facing into the sunset.
Both blind the camera for a period every day, and the period is predictable in advance from the
building orientation. `[PRACTICE]` **Check the aim against sun angles before committing**, and
prefer aiming north where the choice exists.

**Backlight indoors.** Any camera aimed at a glass entrance, an atrium, or a roller door is aimed
at the brightest thing in the building. Re-aim first ([lesson 02](02_optics_and_lenses.md)'s free
fixes); use WDR only when the geometry cannot be fixed.

**Occlusion changes.** A clear sightline at design becomes a stack of pallets, a seasonal display,
a new partition, or a tree in leaf. Ask what the space looks like at its busiest and in every
season, and prefer sightlines that cannot be casually blocked.

**Mounting reality.** Is there structure to fix to? Is there a cable path? Is it reachable for
service without a lift ([lesson 02](02_optics_and_lenses.md))? Will the ceiling contractor accept
the penetration? Many elegant paper positions are not buildable, and finding out on site is
expensive.

**Privacy.** Restrooms, changing areas, and medical treatment spaces are categorically excluded.
Break rooms, prayer rooms, union workplaces, desks, and views into neighbouring residential
property are jurisdiction-dependent and frequently contested. `[VERIFY]` **Raise it, document the
decision, and get it accepted by the client** — an engineer who quietly aims a camera at a
neighbour's garden has created a legal problem for their client. Privacy masking is available on
most cameras and should be specified where a sightline unavoidably includes protected areas.

## The deliverable

A camera placement design is not a set of dots on a plan. It is:

1. **A plan showing camera positions, aim direction, and mounting height.**
2. **Class rings, not cones** — the distance at which each camera meets each DORI class
   ([lesson 04](04_dori_and_pixel_density.md)). This is the single change that most improves a
   coverage drawing.
3. **A camera schedule**: ID, location, question answered, class, lens, mount height, aim,
   illumination requirement, retention, and any privacy note.
4. **Per-zone targets and any documented lower-target decisions**
   ([lesson 04](04_dori_and_pixel_density.md)).
5. **Illumination requirements in lux at a named plane**
   ([lesson 03](03_sensors_and_low_light.md)).
6. **A continuity review** — the route walk showing no gaps.

The schedule is also the input to
[`../16_Automation/data_model/`](../16_Automation/data_model/), which projects it into the drawing
schedule, the IP plan, the cable schedule, and the commissioning tracker. **Name devices once,
consistently, and everything downstream works** ([lesson 08](08_vms_architecture.md)).

## Common mistakes

⚠️ **Placing cameras to cover area rather than to answer questions.** The root error; everything
else follows.

⚠️ **One camera for two questions.** Overview and identification want opposite mounting heights.

⚠️ **Mounting identification cameras high.** Above ~16 ft the envelope closes; at 20 ft it does not
exist.

⚠️ **Aiming at the glass.** Free to fix on the drawing, expensive to fix after installation.

⚠️ **Covering rooms when the question is about a door.** Chokepoints are cheaper and better.

⚠️ **Leaving continuity gaps.** Breaks the identification chain that the chokepoint camera
established.

⚠️ **Ignoring the sun path.** Predictable, and predictably blinding.

⚠️ **Deciding privacy questions silently.** They belong to the client, in writing.

⚠️ **Drawing cones instead of class rings.** Implies uniform capability that does not exist.

⚠️ **Verifying with floor distance instead of slant range.** Overstates every indoor camera.

## Junior vs. Senior

| | Junior | Senior |
|---|---|---|
| Starts from | The floor plan and a camera count | Zones, decisions, and written questions |
| Justifies a camera by | The area it covers | The question it answers |
| Reviews a design by | Checking for uncovered areas | Writing the question for each camera and finding those with none |
| Places identification cameras | Wherever there is a mounting point | Low, near, level, at a chokepoint |
| Improves identification by | Specifying more pixels | Designing a chokepoint, then checking light and angle |
| Handles a bright entrance by | Enabling WDR | Re-aiming so the light is behind the camera |
| Delivers | Dots on a plan | Plan, class rings, schedule with questions, lux targets, continuity review |
| Treats privacy as | Not their problem | A documented client decision they are responsible for raising |

## 🔧 Field exercise

1. Get a floor plan of a building you can access. Mark the zones.
2. Without looking at the existing cameras, write the question for each zone and assign a class.
3. Place your own positions. Compute delivered PPF at slant range for each identification camera,
   and check the depression angle.
4. Now compare with the cameras actually installed. For each existing camera, write its question.
   Count how many have none.
5. Walk the main route through the building and mark every continuity gap.
6. Do steps 3–5 again after dark.

## Exercises

Work these before opening
[`_solutions/09_camera_placement_solutions.md`](_solutions/09_camera_placement_solutions.md).

**E9.1** For each, write the question the camera should answer, assign a class, and state the
mounting height range you would target:
 (a) A pharmacy dispensary door used by 12 named staff.
 (b) A 40-space visitor car park where the concern is vehicle damage claims.
 (c) A university library main entrance, open to the public, where police occasionally request
     footage.
 (d) A warehouse aisle where the concern is stock disappearing between pick and dispatch.

**E9.2** A designer proposes a single identification camera at 18 ft on a warehouse wall, 15 ft
horizontally from a personnel door, 4 mm lens, 2688 px, 1/2.8" sensor.
 (a) Compute the slant range, depression angle, and PPF.
 (b) State whether it meets identify, and whether it meets the angle guidance.
 (c) Give the corrected design and explain the change in one sentence.

**E9.3** Using the Meridian ground-floor plan, a reviewer asks: "Why are there two cameras at the
loading dock? Delete one." Write the response.

**E9.4** A client wants to add a camera "covering the whole open-plan office" for
"general security." There have been no incidents. The staff are unionised.
 (a) State the questions you would ask before agreeing.
 (b) Name the two non-technical issues.
 (c) Give the recommendation.

**E9.5** 🧠 You are reviewing an existing 40-camera design for a three-storey office. Applying the
question test, 11 cameras have no answerable question. The client's budget for the refresh is
fixed. Write the recommendation, including what you would do with the freed budget, and how you
would present the removal of 11 cameras to a client who will hear "less security."

## Retrieval check

1. State the governing rule of camera placement.
2. What are the first three steps of the placement process, and what do they have in common?
3. At a 20 ft mounting height, which distances satisfy both identify and the 30° angle guidance?
4. Name the six constraints a chokepoint fixes at once.
5. Why can the middle of a continuity chain be recognise rather than identify?
6. What does a coverage drawing show instead of cones?
7. Name three things in a camera schedule beyond ID and location.

## References

- [`../01_Foundations/04_defense_in_depth_and_zones.md`](../01_Foundations/04_defense_in_depth_and_zones.md)
  — the zone model that step 1 works from.
- [`../01_Foundations/03_functional_chain.md`](../01_Foundations/03_functional_chain.md) — detect,
  delay, respond; the reason a chokepoint is a security intervention and not just a camera position.
- [`../32_Engineering_Math/01_camera_fov.md`](../32_Engineering_Math/01_camera_fov.md) and
  [`02_pixel_density.md`](../32_Engineering_Math/02_pixel_density.md) — slant range, depression
  angle, PPF. All verification arithmetic here is theirs.
- [`../16_Automation/data_model/`](../16_Automation/data_model/) — where the camera schedule
  becomes every other document.
- `[PRACTICE]` The 30° depression-angle guidance, the 8–10 ft identification mounting range, and
  the 15% overlap allowance are engineering practice, not standards.
- `[VERIFY]` Privacy constraints on camera placement vary enormously by jurisdiction, by space
  type, and by employment law. Raise them; do not decide them.

---

**Next:** [10 — Retail Case Study](10_retail_case_study.md) — the whole module applied to one site,
and an answer to the question everyone asks.
