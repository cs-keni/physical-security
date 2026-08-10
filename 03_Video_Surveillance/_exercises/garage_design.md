# Module 03 Capstone — Cedar Junction Park-and-Ride

> **Budget four to six hours.** Do not open
> [the reference solution](../_solutions/garage_design_reference.md) until you have a complete
> answer written down.
>
> ⚠️ **A warning specific to this exercise.** This module has spent eleven lessons training a set of
> instincts. **Several of them produce the wrong answer here**, and the exercise is built to expose
> that. If your design comes out looking like a slightly larger version of Meridian's, you have
> found the trap rather than avoided it. When something you are confident about does not fit the
> site, that is the exercise working.
>
> **Cedar Junction is fictional.** Every dimension, measurement, and figure is invented for
> teaching.

---

## The brief

Cedar Junction Transit Authority operates a park-and-ride garage adjacent to a commuter rail
station. They have engaged you to design a video surveillance system.

**Their stated requirement, verbatim:**

> *"We've had a spate of break-ins to parked cars — 34 reported incidents in the last twelve
> months, up from 11 the year before. Riders are complaining and two have stopped using the
> station. We want cameras that will identify whoever is doing this. Board has approved capital
> for a system; we'd like coverage of the parking areas."*

## The site

```
  CEDAR JUNCTION PARK-AND-RIDE — typical level (levels 1–4 identical in plan)

  240 ft
  ┌───────────────────────────────────────────────────────────────────────┐
  │ CORE A                                                        CORE B  │  1
  │ ┌──────┐                                                     ┌──────┐ │  2
  │ │STAIR │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │STAIR │ │  0
  │ │ LIFT │  ▓ parking bays▓  ▓ parking bays▓  ▓ parking bays▓  │ LIFT │ │
  │ │LOBBY │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │LOBBY │ │  f
  │ └──┬───┘        aisle            aisle            aisle      └───┬──┘ │  t
  │    │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓      │    │
  │    │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓      │    │
  │  ┌─▼──┐                                                       ┌──▼─┐  │
  │  │PAY │                    ▲ ramp up/down                     │PAY │  │
  │  └────┘                                                       └────┘  │
  └───────────────────────────────────────────────────────────────────────┘
        │                                                             │
        └── to station platform (level 1 only, via bridge) ───────────┘

  LEVEL 1 ONLY:
  ┌───────────────────────────────────────────────────────────────────────┐
  │  ═══════▶ VEHICLE ENTRY (1 lane, barrier, ticket dispenser)           │
  │  ◀═══════ VEHICLE EXIT  (1 lane, barrier, pay-on-exit)                │
  │  ▒▒ pedestrian gate to street (uncontrolled, open 05:00–01:00) ▒▒     │
  └───────────────────────────────────────────────────────────────────────┘
```

**Physical facts:**

| | |
|---|---|
| Levels | 4 (levels 1–3 enclosed, level 4 open deck) |
| Level footprint | 240 ft × 120 ft |
| Spaces | 160 per level, **640 total** |
| Structural soffit clear height | **8 ft 0 in** (levels 1–3); level 4 has light poles at 16 ft |
| Pedestrian cores | 2 (Core A, Core B), each stair + lift + enclosed lobby, all levels |
| Vehicle portal | 1 entry lane, 1 exit lane, both on level 1, barrier-controlled |
| Pedestrian street gate | Uncontrolled, open 05:00–01:00 |
| Payment machines | 2 per level (8 total), in the core lobbies |
| Existing cameras | 6 (all at the vehicle portal), 2005 vintage, analogue |

**Operational facts:**

| | |
|---|---|
| Occupancy pattern | Fills 06:00–09:00, empties 16:00–19:00. **Near-empty 22:00–05:00** |
| Staffing | **None on site.** Station staff are on the platform, not in the garage, and only until 21:00 |
| Monitoring | None. No control room. No plans for one |
| Response | Transit police, dispatched from a district office. **Measured average response 12 minutes; worst case 15** |
| Incident reporting | Riders discover damage **on return, typically 8–11 hours after the event** |
| Lighting | Fluorescent fittings, 1970s, many failed. Measured **2.5 lux average at the deck, max:min uniformity 12:1** |
| Network | Fibre to the station; a spare pair reaches the garage plant room |
| IT | Transit Authority IT will host servers; they run a standard 30-day retention on other systems |

**Incident data supplied by the Authority** (34 incidents, last 12 months):

| Detail | Figure |
|---|---|
| Occurred on levels 3 and 4 | 26 of 34 |
| Occurred between 09:00 and 16:00 | 29 of 34 |
| Entry to vehicle by window break | 21 of 34 |
| Property taken from cabin, not boot | 31 of 34 |
| Offender arrived on foot (no vehicle associated) | **Believed most; not established** |
| Arrests to date | 1 |

---

## Your deliverables

Produce all six. Show your arithmetic; state every assumption.

### 1. Requirements analysis

State, in your own words, what the Authority actually needs — which may not be what they asked for.
Identify the **operational decision** the video must support, and say plainly what the system will
and will not achieve. `[lessons 01, 09]`

### 2. Adversary path and timeliness analysis

Model the break-in as an adversary path. Using
[`../../32_Engineering_Math/08_adversary_path.md`](../../32_Engineering_Math/08_adversary_path.md)
and `psec.pps`:

 (a) State your assumed adversary and task times.
 (b) Compute `T_T`.
 (c) Compute whether **any** detection point produces a timely response given the measured 12-minute
     response time.
 (d) State the conclusion and what it means for the design.

### 3. Zone and target analysis

For every zone, write the **question** the video must answer, assign a DORI class, and justify it.
`[lessons 04, 09]`

### 4. The light problem

 (a) Compute the exposure budget deficit on the decks. `[lesson 03]`
 (b) Give the required illuminance as a specification a lighting designer can build to.
 (c) State what happens to the design if the Authority will not fund lighting.

### 5. The design

 (a) Camera schedule: ID, location, question, class, lens, mount height, illumination requirement.
 (b) Total camera count, with the arithmetic.
 (c) Bandwidth and storage, presented as a range with assumptions. `[lessons 06, 07]`
 (d) VMS architecture with stated failure behaviour. `[lesson 08]`
 (e) Analytics: what, where, and why — with the precision arithmetic. `[lesson 11]`
 (f) Health monitoring and acceptance tests. `[lesson 11]`

### 6. The client conversation

Write what you would say to the Board — no more than 400 words. It must be honest about what the
system will not do, and it must not be defeatist.

---

## Questions to test yourself against

Answer these **before** reading the reference solution. If you disagree with the solution
afterwards, work out whether you were wrong or it was — both happen, and the reasoning matters more
than the verdict.

1. The Authority asked for identify-grade coverage of the parking areas. **How many cameras would
   that actually take**, and would it work?
2. The garage soffit is 8 ft. Is the **depression angle** a problem here? Is that the answer you
   expected?
3. **Where is the chokepoint?** The module has trained you to find one. Is it where you first
   thought?
4. 29 of 34 incidents happened between 09:00 and 16:00 — in **daylight**. Does that change the
   lighting argument? Think carefully; this is the exercise's sharpest question.
5. What does the **12-minute response time** do to the value of detection?
6. What is the single highest-value intervention on this site, and is it a camera?
7. What will you tell a Board that has approved capital for cameras, if cameras are not the answer?

---

## What you are being assessed on

- Whether you **derived** the requirement rather than accepting it.
- Whether you did the **timeliness arithmetic** before designing.
- Whether you located the chokepoint correctly, and can defend the location.
- Whether you handled the daylight-incident data honestly rather than ignoring it.
- Whether your numbers are computed and your assumptions stated.
- Whether you told the client the truth in a way they can act on.

**When you have finished, open the
[reference solution](../_solutions/garage_design_reference.md).**
