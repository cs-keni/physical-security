# Solutions — 09 Camera Placement Engineering

> Work the exercises in [`../09_camera_placement.md`](../09_camera_placement.md) before reading
> this. Geometry was produced by running
> [`../../28_Calculators/psec/optics.py`](../../28_Calculators/psec/optics.py) and transcribed.

---

## E9.1 — Questions, classes, and mounting heights

**(a) Pharmacy dispensary door, 12 named staff.**

> **Question:** *Which member of dispensary staff opened the dispensary door at a given time?*

**Class: recognise (38 ppf).** The candidate set is 12 people known to the reviewer.
**Mount: 8–9 ft**, at the door — a chokepoint. Aim along the approach so the subject faces the
camera as they arrive.

**Caveat worth raising:** if this could support a criminal matter (controlled substances often
can), the reviewer may be a police officer or a court, and neither knows the staff — which moves it
to **identify**. Raise it; do not decide it. See [lesson 04](../04_dori_and_pixel_density.md) E4.1(b).

**(b) 40-space visitor car park, concern is vehicle damage claims.**

> **Question:** *What was the condition of a vehicle on arrival and departure, and did any vehicle
> or person make contact with it?*

**Class: observe (19 ppf)** for the surface. The decision is about **an event and a vehicle**, not
a person's identity — a damage claim needs to show contact occurred, when, and by what.
**Mount: 12–20 ft** — height is correct here, because the job is coverage and sightline over parked
vehicles.

**Add identify at the entry/exit chokepoint** with plate capture. That is where identity and
vehicle attribution actually become recoverable ([lesson 04](../04_dori_and_pixel_density.md) E4.5).
Note the damage-claim use case is unusual in that **continuity over time** matters more than pixel
density: the value is showing the vehicle was undamaged at 09:00 and damaged at 14:00.

**(c) University library main entrance, public, occasional police requests.**

> **Question:** *Who entered or left the library at a given time, to a standard a stranger could
> identify?*

**Class: identify (76 ppf).** "Unknown person" plus "police request" is the definitional identify
case. **Mount: 8–10 ft**, at the entrance chokepoint, aimed **into** the building so arrivals are
frontal and lit by interior light rather than silhouetted against the entrance glass.

**Privacy note:** a public library carries a genuine tension between access and surveillance —
module 01's Ashford Public Library capstone is built on exactly this. Entrance capture is normally
accepted; camera coverage of reading areas and catalogue terminals raises intellectual-freedom
concerns that must go to the client. `[VERIFY]`

**(d) Warehouse aisle, stock disappearing between pick and dispatch.**

> **Question:** *Which individual removed stock from aisle X, and what did they do with it?*

This is the trap in the set. The instinct is an identify-grade aisle camera — which fails, because
warehouse aisles are long, dark, racked (severe occlusion), and mounted high.

**The correct answer is two things:**
- **Aisle: observe (19 ppf)**, mounted high for sightline, establishing that someone was there,
  when, and in which direction they moved.
- **Identify at the chokepoints** — the aisle entrances, the dispatch door, the personnel doors, the
  yard gate. Stock leaving the building must pass a boundary, and boundaries are where you can
  mount low, light properly, and see faces frontally.

**Mount: aisle 14–20 ft; chokepoints 8–9 ft.** Plus the highest-value recommendation, which is not a
camera at all: correlate video timestamps with the WMS pick records
([lesson 08](../08_vms_architecture.md)), which narrows any investigation from hours of footage to
minutes.

---

## E9.2 — The 18 ft identification camera

**(a) Geometry.**

```
slant range      = √(15.0² + (18.0 − 5.0)²) = √(225 + 169) = 19.85 ft
depression angle = arctan(13.0 / 15.0)      = 40.91°
scene width      = 19.85 × 5.37 / 4          = 26.65 ft
PPF              = 2688 / 26.65              = 100.9 ppf
```

**(b) Does it meet the requirements?**

| Requirement | Result | Verdict |
|---|---|---|
| Identify (≥76 ppf) | 100.9 ppf | ✅ **passes**, with 1.33× margin |
| Depression angle (≤30°) | **40.91°** | ❌ **fails**, by 11 degrees |

> ⚠️ **This is the exercise's whole point.** The pixel arithmetic — the part that gets checked in
> design review — **passes comfortably**. The design is still wrong. At a 41° depression angle the
> camera is looking down at the top of people's heads and foreheads; noses and brows shadow eyes and
> mouths, and the facial geometry an identification depends on is foreshortened away. **You can have
> 100 pixels per foot on a face and not be able to identify it.** Pixel density is necessary, never
> sufficient ([lesson 04](../04_dori_and_pixel_density.md)).

**(c) The corrected design.**

**Drop the mounting height to 9 ft, keeping the 15 ft distance:**

```
slant range      = 15.52 ft
depression angle = 14.93°   ✅
PPF              = 129.0    ✅  (up from 100.9)
```

> **The change in one sentence:** lowering the camera from 18 ft to 9 ft brings the depression angle
> from 41° to 15°, giving a near-frontal view of the face, and — because the slant range shortens —
> it *also* raises pixel density from 101 to 129 ppf, so the design improves on both axes at once.

**Why this is worth internalising:** height and angle are not a trade against pixel density near
the camera; below the envelope's upper edge, **lowering the mount improves both**. The trade only
appears when you pull *back* (as in [lesson 01](../01_imaging_chain.md) E1.3, where distance bought
angle at the cost of density). Height and distance are different variables and they behave
differently.

If the 9 ft mount is genuinely impossible — a high-bay warehouse wall with no low fixing, a
vandalism risk — then the honest options are: mount on the door frame or a dedicated low post; move
the camera closer horizontally so the angle improves; or reclassify to recognise and record the
consequence ([lesson 04](../04_dori_and_pixel_density.md)). Do **not** fit a longer lens and declare
it fixed: that raises PPF and leaves the angle at 41°.

---

## E9.3 — "Why two cameras at the loading dock?"

> They answer two different questions, and neither one can answer the other's.
>
> **C8** answers *"who came in through the dock personnel door?"* It is an identification camera:
> mounted low at 8.5 ft, close to the door, aimed at face height, so it captures a frontal,
> identifiable image of each person passing through — the standard we would need if footage went to
> police. Its field of view is deliberately small, which is what identification costs.
>
> **C9** answers *"was the dock door open outside delivery hours, and what was moved?"* That is an
> observation question about the whole dock area over time — the door state, pallets, vehicles, and
> movement. It is mounted at 12 ft for sightline across the dock, and at that height and coverage it
> could not identify anyone even if we asked it to.
>
> If we delete C9 we keep identification of people through one door and lose all visibility of what
> happens on the dock — including the case that concerns us most, which is material leaving through
> the open roller door rather than a person walking through the personnel door. If we delete C8 we
> can see activity but cannot say who any individual was.
>
> The dock is the building's main goods boundary and is the position where both questions have real
> operational value, so I would keep both. If budget requires one to go, tell me which question
> matters more and I will make that recommendation explicitly and record what we lose.

**What is being graded:** answering with the **questions**, not with coverage diagrams; being
specific about why each camera cannot do the other's job (height and class); naming the failure
case the deletion would create; and ending by putting a genuine choice to the client rather than
either capitulating or refusing. The last move matters — a reviewer asking to cut a camera usually
has a budget constraint, and an engineer who converts that into an informed decision is more useful
than one who simply defends the drawing.

---

## E9.4 — "A camera covering the whole open-plan office"

**(a) Questions to ask before agreeing.**

1. **What decision would someone make from this video?** There have been no incidents, so what
   event is anticipated? Without an answer there is no question, and by the rule, no camera.
2. **What prompted the request now?** There is almost always a specific trigger — a suspicion about
   an individual, a missing item, a complaint, an insurance requirement. The stated reason
   ("general security") is rarely the real one, and the real one determines whether a camera is even
   the right instrument.
3. **Who would have access to the footage, and under what circumstances would it be reviewed?**
4. **Has this been discussed with the staff or their representatives, and does the organisation
   have a policy on workplace monitoring?**
5. **Are there alternatives that address the underlying concern?** Access control on the floor,
   securing specific assets, or a clean-desk policy may address the trigger without monitoring
   people at their desks all day.

**(b) The two non-technical issues.**

1. **Employment and privacy law.** Continuous monitoring of employees at their workstations is
   regulated in many jurisdictions, frequently requiring consultation, notification, a documented
   legitimate purpose, and proportionality. `[VERIFY — this is a legal question and varies
   significantly.]` A camera installed without that process can be unlawful and can render the
   footage unusable in exactly the disciplinary proceeding it was installed for.
2. **Industrial relations.** The workforce is unionised. Workplace monitoring is very commonly a
   matter for consultation under a collective agreement, and installing cameras over desks without
   it can trigger a formal dispute. This is a real organisational risk that is not the engineer's to
   absorb, and it is created the moment the camera goes up.

*(A third: **the effect on the people being watched.** Blanket monitoring of a workforce with no
incident history damages trust and is often noticed as a signal of suspicion. It is a legitimate
consideration and clients frequently have not weighed it.)*

**(c) The recommendation.**

> I would not install this as described, and I want to explain why rather than just decline.
>
> A camera needs a question it answers — something a person would actually decide from the footage.
> "General security" over an open-plan office doesn't give us one, and in practice a camera with no
> specific question is one nobody ever reviews, while still costing a licence, storage, and ten
> years of maintenance. It would also be recording your staff at their desks continuously, which in
> this jurisdiction is likely to require a documented purpose, staff notification, and — given the
> collective agreement — consultation with the union before it is installed. Doing that after
> installation is much worse than doing it before.
>
> So: tell me what actually prompted this. If something specific has happened or is suspected,
> there is usually a targeted answer — covering a particular asset, an entry point to the floor, or
> a store cupboard — that addresses the concern, is far easier to justify to staff and to a
> regulator, and costs less. If the concern is people entering the floor who should not be, that is
> a chokepoint camera at the floor entrance plus access control, not coverage of the desks.
>
> If after that conversation the client still wants area coverage of the office, that is their
> decision to make — but it needs to go through their HR and legal process first, and I would want
> the purpose and the consultation recorded before we install anything.

**What is being graded:** refusing to place a camera with no question, without being obstructive;
identifying the legal and industrial-relations exposure as the client's risk and raising it rather
than absorbing it; **asking what really prompted the request**, which is the move that most often
produces a good design; offering a targeted alternative; and correctly locating the final decision
with the client while insisting on the process that protects them.

---

## E9.5 — 🧠 Eleven cameras with no question, fixed budget

**The recommendation:**

> **Remove or relocate the 11 positions that answer no question, and reinvest the entire saving in
> the positions that do.**

**What to do with the freed budget**, in priority order:

1. **Lighting at the identification positions.** From [lesson 03](../03_sensors_and_low_light.md),
   light is the binding constraint on most designs and the only intervention with no image penalty.
   If the entrance and stair cameras cannot hold 1/125 s at night, they are not identification
   cameras regardless of their specification, and no amount of resolution fixes it. **This is almost
   always the highest-value use of the money.**
2. **Upgrade the genuine chokepoints properly.** Entrances, stair discharges, secure-area doors —
   get these to a real identify grade with margin, correct mounting height, and correct aim, rather
   than the marginal specifications typical of a design that spread its budget evenly.
3. **Close the continuity gaps** found by the route walk. A gap breaks the identification chain that
   the chokepoint cameras establish, so closing them makes every other camera more valuable.
4. **Fix the free things first** — clean domes, re-focus varifocals, re-aim cameras shooting into
   glass ([lesson 02](../02_optics_and_lenses.md)). These cost labour only and often produce the
   most visible improvement, which matters for the conversation in the next section.
5. **Health monitoring** ([lesson 11](../11_analytics_and_health.md)), so the improved system is
   still working in three years.

**How to present it to a client who will hear "less security":**

> I want to be straight about what I am proposing, because on paper it looks like I am reducing
> your system.
>
> I went through all 40 cameras and asked one question of each: what decision would someone make
> from this camera's footage? For 29 of them there is a clear answer. For 11, there isn't — they
> cover space that is already covered, or space where nothing that happens would ever be reviewed.
> Those 11 are not protecting you. They are consuming licences, storage, switch ports, and
> maintenance, and they are producing footage nobody will ever open.
>
> Meanwhile, four of the cameras that matter most — your two entrances, the stair from the car
> park, and the server-room door — cannot currently identify anyone after dark, because there is
> not enough light on the subject for the camera to take a sharp picture of someone walking. Right
> now, if an unknown person came through your front door at 2 a.m., you would have footage of them
> and you would not be able to say who they were. That is the actual gap in this system, and it is
> not a gap that more cameras fix.
>
> What I am proposing is to stop paying for the 11 that answer nothing, and spend it on lighting
> and on doing the four that matter properly. You will end up with fewer cameras and a system that
> can, for the first time, actually identify someone. I would rather hand you 29 cameras that all
> work than 40 where the important ones don't.
>
> If you would like, I will show you the current night footage from the front entrance alongside
> what it looks like with proper lighting — it makes the case better than I can.

**What is being graded:**

- **Reinvesting rather than banking the saving.** The budget is fixed, so this is a
  reallocation, and the recommendation is only credible if the money visibly goes somewhere.
- **Naming light as the priority**, consistent with the whole module.
- Leading the client conversation with **the test applied**, not with the deletion — so the removal
  reads as a finding rather than a cut.
- **A concrete failure scenario** ("2 a.m., front door, you could not say who they were"), which is
  what makes an abstract argument land.
- Offering the **before/after demonstration**. A client who sees the difference agrees in seconds;
  a client who reads an argument negotiates. This is the single most effective move available and
  costs one evening.
- The closing line reframes "fewer cameras" as **more capability**, which is the actual truth of
  the recommendation rather than a spin on it.

---

## Retrieval check — answers

1. **Every camera answers exactly one written question. If you cannot write the question, do not
   place the camera.**
2. **Zones → decisions → questions.** They all involve **no equipment** — and they are the steps
   most often skipped.
3. **None.** At 20 ft, close distances give depression angles of 36–56° and far distances fall
   below 76 ppf. The envelope is empty.
4. Pixel density, depression angle, motion, pose, light, and occlusion.
5. Because **identity is established once at a chokepoint and then carried by continuity** — the
   middle cameras only need to show, without a gap, that it is the same person.
6. **Class rings** — the distance at which the camera meets each DORI class.
7. Any three of: the **question it answers**, DORI class, lens, mounting height, aim direction,
   illumination requirement, retention, privacy note.
