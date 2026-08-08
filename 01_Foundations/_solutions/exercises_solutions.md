# Reference Solution — Module 01 Capstone, Ashford Public Library

> For the capstone in [`../exercises.md`](../exercises.md).
> **Do not read this until you have a completed worksheet.**

> **One defensible answer, not the answer.** Parts A2, B6, D2, and all of G admit more than one
> good response. What is not negotiable is the arithmetic in Part B, the failure identified in
> F1, and the obligation to treat the library's mission as a requirement rather than an obstacle.

> **Part B was computed by running
> [`../../28_Calculators/psec/pps.py`](../../28_Calculators/psec/pps.py)**, derived in
> [`../../32_Engineering_Math/08_adversary_path.md`](../../32_Engineering_Math/08_adversary_path.md).

---

## Part A — Framing

### A1 — The four questions, and the asset ranking

**What are we protecting?** In order:

| # | Asset | Owner | Consequence of loss |
|---|---|---|---|
| **1** | **Staff** — 14 people, 2 alone after 1800 | The Library, as employer | Injury; a duty-of-care failure; resignations; inability to staff evenings. **Unbounded and irreversible.** |
| **2** | **Patrons**, including vulnerable users | The Library | Injury; loss of the safe-public-space function that is much of the library's actual value |
| **3** | **Special collections** — appraised $340,000 | The Library and, in a real sense, the community | **Irreplaceable.** Appraised value understates it: money does not restore an 18th-century deed. |
| **4** | **Continuity of service** | The Library | Closure days, which for a branch library is the loss of its whole purpose |
| **5** | **General collection, computers, cash** | The Library | Replaceable, insured, low unit value |
| **6** | **Reputation and public trust** | The Library and the municipality | Slow, diffuse, and it is what a board actually worries about |

**From whom or what?** Staff safety: distressed or intoxicated individuals, people in mental
health crisis, and occasionally a genuinely aggressive person. **Note that most of this
population is not an adversary in the module-02 sense** — there is often no intent to cause harm,
which means deterrence does very little and de-escalation does a great deal. Special collections:
an outsider with hand tools, or a patron with legitimate access. The parking lot: opportunistic.

**What happens if we fail?** For assets 1 and 2, injury and a duty-of-care failure. For asset 3,
permanent loss of community heritage — the appraisal is the insurance number, not the
consequence.

**What are we willing to spend?** $60,000, and — the constraint that actually governs the design —
**no measure that restricts public access or requires identification to enter.** That is not a
preference. It is the library's reason for existing, and it eliminates a large part of the
standard toolkit before you begin.

### A2 — Re-ranking the Director's list

| Director's order | Risk order | Why it moved |
|---|---|---|
| 1. Staff safety | **1. Staff safety** | Agreed, and it is the one thing on the list with an unbounded consequence. Three incidents in a year is a **pattern**, not a coincidence. |
| 2. Break-in | **4. Break-in** | Property loss, insured, low value. **Its importance is as evidence**, not as a risk: it proved the rear door is weak, the intrusion system reaches nobody, and the call list is dead. |
| 3. Special collections | **2. Special collections** | Moves up. **Irreplaceable, unmonitored, protected by one keyed lock at the end of a corridor nobody can see.** The board is right and is being polite about it. |
| 4. East-end lighting | **3. East-end lighting** | Moves up sharply. It is a **staff safety** issue wearing a facilities costume — one of the three incidents involved a staff member being followed to their car. It is also nearly free. |
| 5. Cameras | **6. Cameras** | Moves down. This is a proposed *solution*, not a risk. The existing four are useless and adding more addresses nothing on this list directly. |
| 6. Budget | **Constraint, not a risk** | |
| *(unstated)* | **5. The after-hours call list, dead since 2019** | **The Director did not mention this and it is the single highest-value finding on the site.** The intrusion system worked correctly and the response chain terminated in a disconnected phone number. Cost to fix: zero. |

**What I would need to know to be more confident:** the incident log in full (are the three
incidents related, same individual, same time of day?); whether staff have de-escalation
training and a written procedure; the real discovery interval for anything in special
collections — nobody knows what is missing from an unaudited archive; and the actual measured
police response, since 10 and 15 minutes are published figures, not measurements.

### A3 — Full chains

**Item 1 — Staff safety at the circulation desk**

| Link | Content |
|---|---|
| **Asset** | Staff on duty, especially the 2 working after 1800. Owner: the Library as employer, with a legal duty of care. |
| **Threat / hazard** | Mostly **not a classical threat.** Distressed, intoxicated, or unwell individuals with no formed intent to harm; occasionally a genuinely aggressive person. Capability: physical presence. Intent: usually absent, sometimes impaired rather than malicious. |
| **Vulnerability** | The desk is 45 ft from the entrance **facing away from it**, so staff have no warning of an approach. No barrier, no retreat path, no duress device, no second person after 1800, no sightline to the parking lot, and no written procedure. |
| **Undesired event** | Verbal aggression escalating to physical contact; a staff member followed to a vehicle; an incident with no witness and no way to summon help. |
| **Consequence** | Injury. Trauma and resignation — **the more likely and more expensive outcome**. Inability to staff evening shifts. Duty-of-care exposure. |
| **Countermeasures by function** | **Deter:** visible desk position with a clear sightline; a lit and observed parking lot. **Detect:** the staff member seeing the person coming — the whole finding is that this does not currently happen. **Assess:** staff judgement, which requires training. **Delay:** desk geometry, retreat path, a lockable staff area. **Respond:** duress device, defined procedure, buddy policy for evening closing, escort to vehicles. **Recover:** incident reporting that goes somewhere and gets reviewed. **Non-hardware, and the most effective:** de-escalation training and a written procedure. |
| **Residual risk** | Meaningful and permanent. A public building open to all cannot eliminate this, and no measure compatible with the library's mission comes close. Accept explicitly, at board level. |

**Item 3 — Special collections**

| Link | Content |
|---|---|
| **Asset** | Original maps, photographs, three 18th-century deeds. Appraised $340,000; **irreplaceable**. |
| **Threat** | (a) An after-hours outsider with hand tools — the design-basis adversary in Part B. (b) **A patron with legitimate supervised access**, which is the more likely mechanism and the one nobody plans for. (c) Fire and water — **hazards**, and for an irreplaceable paper archive arguably the larger exposure. |
| **Vulnerability** | One keyed lock. No position monitoring, no intrusion detection on floor 2 at all, no camera, no sightline down the corridor, no item-level audit, and no record of who has been in the room. |
| **Undesired event** | After-hours theft; item-level theft during a supervised visit; fire or water damage. |
| **Consequence** | Permanent loss of community heritage. **For the supervised-visit case, the consequence may never be detected** — an unaudited archive cannot tell you something is missing. |
| **Countermeasures by function** | **Deter:** visible monitoring and a stated supervision policy. **Detect:** door position and intrusion detection on floor 2; camera at the door; **an item-level inventory**, which is the only thing that detects the supervised-visit case at all. **Delay:** a certified safe or cabinet for the highest-value items — see B5. **Respond:** connect floor 2 to a monitored intrusion system with a call list that works. **Recover:** the inventory again, plus appropriate archival storage and environmental protection. **Non-hardware:** a supervision procedure and a signed access log. |
| **Residual risk** | The insider and the supervised-visit cases remain. So does fire. Accept explicitly, and note that an inventory converts an undetectable loss into a detectable one, which is worth more than most hardware here. |

### A4 — The hazard and the solution-masquerading-as-a-requirement

**The hazard:** item 4, the unlit east end of the parking lot. Darkness has no intent. Note the
nuance — the *darkness* is a hazard-like condition, but its consequence is realised through a
threat (a person), and it is best handled as a **CPTED condition** rather than a threat problem.
What changes: you cannot deter darkness, you fix it, and the fix is relamping rather than
security equipment.

> A stronger answer also names fire and water damage to the archive as the genuine hazard on this
> site, and observes that it is absent from the Director's list entirely.

**The solution masquerading as a requirement:** item 5, *"the board is asking about cameras."*
Cameras are a countermeasure, not a risk. What changes: you ask what the board is trying to
accomplish. Almost certainly it is (a) reassurance about staff safety and (b) evidence after the
break-in — and cameras address the second reasonably and the first hardly at all.

### A5 — What to accept, and who accepts it

Recommend explicit acceptance of:

1. **Residual staff-safety risk.** Irreducible in a public building. Accepted by **the Library
   Board**, on the record, with the mitigations documented.
2. **Theft by a patron during supervised access to special collections**, mitigated by inventory
   and procedure rather than prevented. Accepted by **the Board**.
3. **General collection losses.** Ordinary library shrinkage, insured, not worth engineering
   against.
4. **Property loss in a repeat after-hours break-in of the general premises.** Low value,
   insured.

**You do not accept risk. The owner does**, and your obligation is to state it clearly enough
that the acceptance is informed. Put these four in the memo as a numbered list the Board can
formally note.

---

## Part B 🧮 — Timely detection

### B1 — The path as it exists

```
   Task                              delay    start      end
   Approach rear service yard         45 s      0 s      45 s
   Force rear service door           120 s     45 s     165 s
   Cross ground floor to stair        40 s    165 s     205 s   ← lobby motion detects here
   Ascend to floor 2                  25 s    205 s     230 s
   Force special collections door     90 s    230 s     320 s
   Locate and remove items           420 s    320 s     740 s

   T_T  =  740 s
   T_D  =  205 (lobby motion) + 90 (assessment)   =  295 s
   T_A  =  740 − 295                              =  445 s
   T_R  =  600 s  (10 min, verified alarm)

   margin  =  445 − 600  =  −155 s
```

**NOT TIMELY. Short by 155 s.** Against the 60 s required margin, the **deficit is 215 s**.

### B2 — The required detection point

```
   T_D_max  =  T_T − T_R − margin  =  740 − 600 − 60  =  80 s
```

At t = 80 s the adversary is **35 seconds into forcing the rear service door** (that task spans
45–165 s). Detection must occur, *including assessment*, at or before that instant.

Since assessment currently consumes 90 s on its own — more than the entire 80 s budget — **no
sensor anywhere on this path can succeed while the assessment delay stands.** That is the result
that should reorder your recommendations.

### B3 — At the unverified-alarm response of 15 minutes

```
   T_R  =  900 s
   margin  =  445 − 900  =  −455 s

   T_D_max  =  740 − 900 − 60  =  −220 s
```

**The required detection point is negative.** `compare_interventions` reports:

> `NOT ACHIEVABLE on this path.`

**What the sign means:** timeliness would require detecting the adversary 220 seconds *before
they arrive*. Even instantaneous detection at the property line leaves 740 s against a 900 s
response.

**What you should stop doing:** shopping for detection. At the unverified response time the
detection lever is **exhausted, not expensive**, and any proposal built on more sensors is money
spent on a verdict that will not move.

> This also tells you something the client will care about: **video verification is worth 300
> seconds of response time.** That single fact justifies more of the camera budget than any
> argument about image quality.

### B4 — Working the detection lever, at the 10-minute verified response

| | Detection at | Assessment | `T_D` | `T_A` | Margin | Verdict |
|---|---|---|---|---|---|---|
| **Baseline** | Lobby motion (205 s) | 90 s | 295 s | 445 s | −155 s | NOT TIMELY |
| **(a)** | Rear door contact (165 s) | 90 s | 255 s | 485 s | **−115 s** | **NOT TIMELY** |
| **(b)** | Rear door contact (165 s) | 20 s | 185 s | 555 s | **−45 s** | **NOT TIMELY** |
| **(c)** | Service yard (45 s) | 20 s | 65 s | 675 s | **+75 s** | **TIMELY** |

*(For comparison: yard detection with the 90 s assessment retained gives `T_D` = 135 s and a
margin of just +5 s — **MARGINAL**, and treated as not timely.)*

**Why (a) gains so little — this is the question.** Moving detection from the lobby to the rear
door moves it **40 seconds earlier**, because the door-forcing task ends at 165 s and the
ground-floor crossing ends at 205 s. Forty seconds against a 215-second deficit is 19% of the
problem. It feels like a significant intervention — a new sensor on the actual point of entry —
and it is nearly worthless.

**What is really binding is the assessment delay.** The budget is 80 s and assessment consumes 90
of it before any sensor has been chosen. Step (b) attacks that term and gains 70 s, more than the
sensor relocation did. But (b) still fails, because even a door contact firing at 165 s cannot
fit inside an 80 s budget.

**Only (c) works, and it requires both changes at once:** detection moved outside the building
*and* assessment cut to 20 s. Either alone is insufficient. That is the sort of conclusion the
arithmetic produces and intuition does not.

### B5 — The delay lever

Highest-value items into a certified safe inside special collections, raising the removal task
from 420 s to 900 s. **Detection unchanged — lobby motion, 90 s assessment.**

```
   T_T  =  740 − 420 + 900  =  1220 s
   T_D  =  295 s   (unchanged)
   T_A  =  925 s
   margin  =  925 − 600  =  +325 s
```

**TIMELY, with 325 s of margin** — more than four times the margin of B4(c), achieved by changing
nothing about detection, assessment, monitoring, or the alarm company.

### B6 — Comparing B4(c) and B5, and the recommendation

| | **B4(c)** — yard detection + fast assessment | **B5** — a safe |
|---|---|---|
| Margin | +75 s | **+325 s** |
| Cost shape | Exterior detection hardware **plus a recurring monitoring contract change** | One-time capital, low thousands |
| Depends on | A sensor in a public-adjacent yard, a monitoring contract, and an operator being alert | Physics |
| Nuisance alarm exposure | **High** — an exterior sensor in a service yard next to a refuse enclosure, at a public building | None |
| Works at the 15-min unverified response | **No** — B3 showed detection cannot | **Yes**, comfortably |
| Also protects against | Nothing else | **Fire and water**, the hazards nobody listed |
| Also addresses the patron-theft case | No | **Partly** — items are secured between supervised uses |
| Fits the library's mission | Awkwardly. Exterior detection at a public building generates alarms from ordinary human presence | **Completely invisible to the public** |

**Recommendation for this client: B5, the safe.** Decisively.

**Why the answer differs from a warehouse.** In the warehouse case (E3.2, and the module-32
capstone) the delay lever is usually the *worst*-value option: hardening is expensive, the assets
are bulky, and detection plus a fast guard response is cheaper. Here every one of those
assumptions inverts:

- **The asset is small.** Three deeds, some maps and photographs fit in a safe. You cannot put a
  distribution centre's inventory in a safe; you can put this archive in one.
- **Response is external and slow, and you cannot change it.** A warehouse can hire a guard. A
  branch library cannot, and 10 minutes is the *good* case.
- **The mission forbids the detection-heavy answer.** Exterior sensors at a public building
  generate alarms from people who are entitled to be there.
- **The safe is the only option that survives an unverified alarm**, and at a site with a
  2019-vintage call list, unverified is the realistic case.
- **It addresses fire and water**, which for an irreplaceable paper archive may be the larger
  exposure and appears nowhere on the client's list.

> **The general lesson:** the four levers are not ranked in the abstract. Which lever is cheapest
> depends on the size of the asset, who controls the response, and what the institution is
> *for*. A method that produced the same answer at a warehouse and a library would not be a
> method.

### B7 — The two assumptions

1. **The task delay times**, especially 420 s to locate and remove items and 90 s to force the
   collections door. `[PRACTICE][VERIFY]` These are illustrative. If removal is 200 s rather than
   420, B5's margin falls from 325 s to 105 s and the whole analysis tightens.
   **Spend here first.** It is cheap — a supervised timing of the removal task, and a look at the
   actual door construction — and **every other number is downstream of it.**
2. **The 10-minute police response is a published figure, not a measurement**, and it applies to
   a *verified* alarm — which this system currently cannot produce. The realistic figure today is
   the 15-minute unverified one, at which detection is not achievable at all.

> A third, worth stating: the model assumes detection probability is 1.0. The lobby motion
> detector's real `P_D` against someone who has been inside the building as a visitor and knows
> where it is may be considerably lower.

---

## Part C — Zones and boundaries

### C1 — The zone diagram

```
   ZONE 0   Street, sidewalk, public parking apron
     │
   ZONE 1   THE ENTIRE PUBLIC LIBRARY — lobby, stacks, children's, computers,
     │      community room, floor 2 reference and study rooms
     │      boundary: the building envelope.  control: NONE during open hours, by policy
     ▼
   ZONE 2   Staff area, workroom, DVR location
     │      boundary: staff door.  control: keyed
     ▼
   ZONE 3   Special collections
            boundary: room envelope.  control: keyed, staff-escorted
```

**What is unusual:** in almost every other building Zone 1 is a controlled site perimeter. **In a
library, the entire public floor area is Zone 1 and it is deliberately uncontrolled.** The
library's mission places an unrestricted public zone *inside* the building envelope, so the
building envelope is not a security boundary during open hours — it is only a boundary at night.

This has a consequence that governs the whole design: **there are only two real boundaries on
this site**, Zone 1→2 and Zone 2→3 (or 1→3, since special collections is reached from the public
floor). Everything else is public. That is why the answer concentrates so tightly on special
collections and on staff, and why "more cameras in the stacks" addresses nothing.

### C2 — Nine-element integrity check on special collections

| Element | Finding | Confidence |
|---|---|---|
| **Walls** | Not stated. 1994 construction, 2009 renovation — most likely metal stud and gypsum. | **UNKNOWN — survey** |
| **Ceiling** | Not stated. If the partition stops at a suspended grid, the keyed lock is decorative. **The single most important unknown on this list.** | **UNKNOWN — lift a tile** |
| **Floor** | Slab; floor below is public Zone 1 stacks. Penetrations unknown. | UNKNOWN |
| **Doors** | Single leaf, **keyed cylinder only.** No position switch, no monitoring. Frame, hinge, and strike condition unknown. | Partially known |
| **Windows** | Not stated. Floor 2 — check for adjacent roof or canopy access. | **UNKNOWN — survey** |
| **Penetrations** | Not stated. HVAC returns are the usual finding in a 1994 building. | **UNKNOWN — survey** |
| **Roof** | Floor 2 room; roof hatches and skylights unknown. | **UNKNOWN — survey** |
| **Adjacencies** | Study rooms — **public, unobserved, and occupiable for hours at a time.** This is the highest-risk adjacency on the site: an attacker can be legitimately present, alone, adjacent to the boundary, for as long as they like. | Known |
| **Egress hardware** | Not stated. If the room is on any egress path, options narrow considerably. `[CODE][VERIFY]` | UNKNOWN |

**Seven of nine are unknown**, which is the honest output of doing this from a brief rather than
from a site. Write them as survey questions; `UNKNOWN — could not determine from available
information` is data, a blank is indistinguishable from an oversight.

**The finding that emerges anyway:** the study-room adjacency means the room's boundary is
exposed to an unobserved public space for hours at a time, and the only control on it is a keyed
lock. **This is what makes B5's safe the right answer** — it puts a second boundary inside the
one that cannot be made good.

### C3 — Every SPOF

| SPOF | What stops working | Note |
|---|---|---|
| The single DVR in the staff area | All recording — and **it is inside the area an intruder passes through** | It is also the evidence of its own theft |
| One intrusion panel | All detection | |
| **One after-hours call list — dead since 2019** | **The entire response function** | Not equipment |
| One keyed lock on special collections | The only control on the highest-value asset | |
| One staff member on duty after 1800 | Assessment, response, and the ability to summon help | **Also not equipment** |
| One utility feed, no UPS mentioned | Everything | |
| One key system with no stated control | Every mechanical boundary | Who holds keys? Has there ever been a rekey? |

**The one that is not equipment:** the **call list**, and equally the **lone evening staff
member**. The call list is the SPOF that already failed once, in the only real incident this site
has had, and it costs nothing to fix.

### C4 — The propped community room door

**It is a design failure (category 9), presenting as human error (category 6), which creates a
zone integrity failure.** All three are true; the useful classification is the first.

**Defence:** evening events require moving people, equipment, and refreshments through a door
that presumably locks by policy and has no other convenient route. **The propping is a rational
response to a design that did not account for how the room is used.** Classifying it as human
error leads to a memo and a removed doorstop, and it will be propped again within a week.

Classifying it as a design failure leads to the right question — *what does the community room
actually need?* — and the answer is a scheduled unlock during event hours, a position switch with
a held-open alarm outside those hours, and a camera on the door. That is cheap, and it stops
fighting the users.

> This is E5.1's second worked finding and lesson 05's convenience-door problem, in a slightly
> different costume. **Where a door is propped, the design is losing an argument with the work.**

---

## Part D — The environment

### D1 — Six CPTED findings

> Costs are `[VERIFY]` order-of-magnitude placeholders.

> **CPTED-01 — East parking lot, non-functioning fixtures.** Two pole fixtures at the east end
> have been non-functional for over a year, producing a dark zone across approximately 20 spaces.
> Evening staff (2 on duty until 2000, departing after close) will not park there and instead
> use spaces nearer the entrance, displacing patrons. One reported incident involved a staff
> member being followed to a vehicle. The dark zone is not observable from any occupied position.
> **Recommend:** (1) restore both fixtures [**immediate, ~$1,400**]; (2) confirm illuminance and
> uniformity across the full lot after relamping `[VERIFY against IES guidance and any local
> requirement]`; (3) if uniformity remains inadequate at the east end, add one fixture
> [~$6,000].

> **CPTED-02 — Circulation desk orientation.** The desk is set 45 ft back from the entrance and
> faces the stacks, placing the entrance behind the staff member's shoulder. Staff have no
> warning of an approach and no view of who is entering. Three verbal-aggression incidents in
> 12 months. **Recommend:** reorient the desk to face the entrance with the stacks in peripheral
> view, and move it forward to approximately 25 ft [**furniture change, ~$3,000 including
> data/power relocation**]. See D2.

> **CPTED-03 — Special collections corridor, no natural surveillance.** The corridor is a
> dead end past the study rooms with no sightline from any staffed position. A person may remain
> at the collections door indefinitely, unobserved, during open hours. **Recommend:** (1) a
> camera at the corridor end with a view of the door, with recording [~$1,800]; (2) relocate one
> study room's glazing or replace a solid door with a vision panel to create an incidental
> sightline [~$2,500]; (3) **no** access restriction to the corridor — the study rooms are public
> and must remain so.

> **CPTED-04 — Rear service yard, concealment and no observation.** The 6-ft masonry refuse
> enclosure screens the service door from the street, removing the only natural surveillance the
> rear elevation had. The door is unlit, unmonitored, and uncovered by camera. **Recommend:**
> (1) light the service yard [~$2,200]; (2) camera covering the door and yard [~$1,800];
> (3) at the next site works, relocate or lower the refuse enclosure [capital, carry as future].

> **CPTED-05 — Community room door, propped routinely.** See C4. The evening-event route makes
> propping the only practical option. **Recommend:** scheduled unlock during booked event hours,
> position switch with held-open alarm outside them, and a camera [~$2,400]. `[CODE][VERIFY]` any
> egress implications.

> **CPTED-06 — Maintenance and image, general.** Two lights out for over a year is itself the
> most informative observation on this site: it signals that maintenance requests do not result
> in action, which is exactly the mechanism the maintenance/image strategy describes.
> **Recommend:** a documented monthly exterior lighting check with a named owner [**$0**], and
> a standing repair authority so a failed fixture does not require a board decision.

### D2 — The circulation desk, without a checkpoint

**The problem in CPTED terms:** a **natural surveillance** failure caused by orientation, not by
sightline obstruction. The desk has an excellent view — of the wrong thing. Staff cannot see
who is approaching, which removes their ability to assess, prepare, or de-escalate early, and it
removes the deterrent effect of an approaching person knowing they have been seen.

**The fix, and why it is not a checkpoint:**

1. **Rotate the desk to face the entrance**, bringing it forward to roughly 25 ft. Reception
   desks face the door in every building type; this reads as *welcoming*, not as screening. It is
   the single highest-value change on the site and it is a furniture decision.
2. **Keep it open on the public side.** No barrier, no glazing, no raised counter. The finding is
   about *seeing*, not about *separating*, and a screened desk in a library damages the very
   thing the library is for.
3. **Detail the staff side properly**: a solid desk front, an unobstructed retreat path to the
   staff area, and a duress device under the counter. Invisible to the public.
4. **Give staff a sightline to the lot**, or a monitor showing it, so an evening departure is not
   the first time anyone looks outside.

> Note that item 3 is the only *security* item, it is invisible, and it costs a few hundred
> dollars. The rest is furniture layout. **"No" is not a deliverable; a floor plan is.**

### D3 — The east end

**Immediate fix:** relamp both fixtures, **~$1,400, this week.** It is the highest
value-per-dollar item on the entire site.

**Afterwards, `[VERIFY]`:** measure illuminance and the average-to-minimum **uniformity** ratio
across the whole lot against IES guidance and any local requirement, at night, with a meter.
Uniformity matters more than brightness — the eye adapts to the brightest thing in view, so
restoring two fixtures beside a bright entrance canopy may still leave the east end functionally
dark. Also `[VERIFY]` whether the fixtures failed or were switched off, because those imply
different follow-ups.

### D4 — Where CPTED does not help here

1. **The after-hours break-in.** CPTED works by influencing the behaviour of people who can be
   observed by other people. **At 0300 there is nobody to do the observing**, so natural
   surveillance has nothing to operate through. What helps instead: detection, delay, and the
   response chain — Part B.
2. **The distressed or unwell individual at the desk.** CPTED assumes a decision-maker weighing
   the risk of being seen. **Someone in crisis is not performing that calculation**, so
   territorial cues and sightlines do very little. What helps instead: staff training,
   de-escalation procedure, a duress device, staffing levels, and a relationship with local
   social services. **None of that is a security product**, and saying so is part of the job.

---

## Part E — Requirements

### E1 — The requirement set

| ID | Requirement | Type |
|---|---|---|
| LIB-01 | The circulation desk **shall** be positioned such that a staff member seated at it has an unobstructed view of the main entrance and the first 20 ft of the entry path. | Functional |
| LIB-02 | A duress signalling device **shall** be provided at the circulation desk, activating an alarm at a monitored location, and **shall** be testable without generating a dispatch. | Functional |
| LIB-03 | Duress activation **shall** result in a defined response within a documented time, per a written procedure held by staff. | Operational |
| LIB-04 | Not fewer than two staff **shall** be on site from 1800 until the building is secured. | Operational |
| LIB-05 | Exterior illuminance across the parking area **shall** meet [target] with an average-to-minimum uniformity ratio not exceeding [target]. `[VERIFY against IES guidance and local requirement]` | Performance |
| LIB-06 | Exterior lighting **shall** be inspected monthly and non-functioning fixtures restored within 10 working days, per a named owner. | Operational |
| LIB-07 | Items in the special collections designated as high value **shall** be stored, when not in supervised use, in a container rated for not less than [x] minutes of tool attack and [x] hours of fire exposure. `[STANDARD][VERIFY rating basis]` | Performance |
| LIB-08 | The special collections door **shall** be monitored for position, forced-open, and held-open, with alarm annunciation to the monitored location. | Functional |
| LIB-09 | Intrusion detection **shall** cover floor 2 including the special collections corridor. | Functional |
| LIB-10 | An item-level inventory of special collections **shall** be established and audited not less than annually, with the audit recorded. | Operational |
| LIB-11 | Access to special collections **shall** be recorded by date, time, staff supervisor, and visitor identity, for every entry. | Operational |
| LIB-12 | The after-hours response contact list **shall** be verified quarterly, with the verification recorded, and **shall** name not fewer than three reachable contacts. | Operational |
| LIB-13 | Intrusion alarms **shall** be video-verified prior to dispatch. | Functional |
| LIB-14 | Recorded video **shall** be retained not less than 30 days and **shall** be exportable by a trained staff member in under 10 minutes without vendor assistance. | Performance |
| LIB-15 | No measure **shall** restrict public access to the collection or require identification to enter the building. | **Constraint** |
| LIB-16 | Egress from all spaces **shall** remain free at all times. `[CODE][VERIFY]` | Constraint |

**LIB-14's second clause is the one that matters.** The existing DVR probably "retains" footage;
what it has never done is let anyone get it out. A retention requirement without an
**exportability** requirement produces the system they already have.

### E2 — Two pathologies

**"The board is asking about cameras."** — *Solution masquerading as a requirement.*

> **Rewrite:** "Video coverage **shall** be provided at the rear service door, the special
> collections corridor, the community room exterior door, and the main entrance, sufficient to
> **identify** a person at the door plane (≥ 76 PPF horizontal) under design illumination, with
> not less than 30 days of retention and staff-operable export." Plus **LIB-13**, which is where
> the real value is: video verification converts a 15-minute unverified police response into a
> 10-minute verified one — **300 seconds**, which Part B3 showed is the difference between a
> lever that works and one that does not.

**"We had a break-in last spring"** — *not a pathology, but an* **inherited framing** *worth
challenging.* The natural reading is "prevent break-ins," which produces a hardening proposal for
a low-value property loss. The **finding** the break-in actually produced is that the response
chain terminates in a dead phone list, and that is LIB-12 — free, and the highest-value
requirement in the set.

### E3 — RTM rows for the five highest-priority requirements

| Req ID | Requirement (abbrev.) | Traces from | Design element | Test procedure | Status |
|---|---|---|---|---|---|
| LIB-12 | Call list verified quarterly, ≥3 contacts | Break-in RISK-02; **response chain failure** | Procedure + named owner; central station record | CX-OPS-001 — unannounced after-hours test call | Open |
| LIB-01 | Desk sightline to entrance | Staff safety RISK-01 | Desk relocation; furniture plan FP-01 | CX-CP-001 — seated observation test | Open |
| LIB-07 | High-value items in a rated container | Special collections RISK-03 | Safe, [rating] `[VERIFY]`, anchored, in SC room | CX-SC-001 — verify rating label, anchorage, key control | Open |
| LIB-02 | Duress device at the desk | RISK-01 | Fixed duress button, monitored | CX-CP-002 — activation to response, timed | Open |
| LIB-05 | Lot illuminance and uniformity | RISK-01, RISK-04 | Relamp 2 fixtures; verify; add 1 if required | CX-LT-001 — night meter survey, avg:min | Open |

**Note what is at the top of the priority list.** The highest-priority requirement on this site is
a **procedure with a named owner and a test**, not a device. The RTM does not care that it is
free; it cares that it traces to a risk and can be tested.

### E4 — The mission constraint

**LIB-15**, stated above, is the constraint requirement.

**Two otherwise-reasonable countermeasures it eliminates:**

1. **Access control at the main entrance** — credentials, a staffed screening point, or a
   turnstile. Standard practice at almost any other building type, and the single most effective
   thing you could do about the staff-safety risk. **Forbidden**, because a library that asks who
   you are before you come in has stopped being a library.
2. **Restricting the special collections corridor or the study rooms to identified users.** It
   would eliminate the adjacency finding in C2 outright. **Forbidden** for the same reason — the
   study rooms are public amenity space.

> Write the constraint down as a requirement rather than treating it as an obstacle. It is not
> the client being difficult; it is the client's actual mission, and a design that ignores it is
> not a better design that got rejected — it is a worse design, because it fails a requirement.

---

## Part F — Failure

### F1 — Why the 2009 system alarmed and nobody came

**The chain, with the break point marked:**

```
   Physical event: rear door forced                             ✓ occurred
   Transduction:   lobby motion detector activates              ✓ worked
   Local decision: zone armed, alarm classified                 ✓ worked
   Transmission:   panel → central station                      ✓ worked
   Annunciation:   central station operator receives alarm      ✓ worked
   Assessment:     none available — no video, no verification   ✗ ABSENT
   Dispatch:       central station calls the after-hours list   ✗ FAILED — list dead since 2019
   Response:       nobody dispatched, nobody attended           ✗ never occurred
```

**Everything on the equipment side worked exactly as designed.** The failure is entirely in the
last third of the chain.

**Category: 8 — Maintenance failure.** The call list was not maintained. A contact list is a
component of the response function and it decays like any other; nobody replaced its battery for
six years.

There is a strong case for **category 9 — Design failure** as well, and a complete answer names
both: the 2009 design provided detection and annunciation and never specified an **assessment**
capability or a **verified, periodically tested response path**. A design that ends at the central
station has designed half a system.

**Time to detect the failure: never** — until the only night it mattered. That is the defining
property of a silent failure, and it is why the mitigation is *testing* rather than *monitoring*.

**The mitigation costs nothing:** quarterly verification of the call list, with the verification
recorded, plus one unannounced after-hours test call per year. That is LIB-12 and CX-OPS-001.

### F2 — FMEA on the proposed special collections protection

Proposed: a rated safe (LIB-07), door position monitoring (LIB-08), floor 2 intrusion detection
(LIB-09), a corridor camera, and an item-level inventory (LIB-10).

| Failure mode | Effect | Detected by? | Time to detect | Mitigation |
|---|---|---|---|---|
| Safe left unlocked after supervised use | The entire control is absent, invisibly | **Nobody** | **Never** | Closing checklist; a door contact on the safe itself if the value warrants it |
| Safe key/combination shared or never changed after staff departure | Access by a former holder, generating no event | **Nobody** | **Never** | Combination change on staff departure, in the procedure; recorded |
| Position switch on the SC door misaligned or defeated | No alarm on entry | Only with tamper supervision | Never without it | Balanced magnetic switch; walk-test at every PM |
| Floor 2 motion detector masked by stored material | Zone blind | Anti-mask, if specified | Never without it | Specify anti-mask; **housekeeping** — an archive room accumulates boxes |
| Camera view obstructed by later shelving or a fit-out duct | Coverage gap while the camera reports healthy | **Nobody** | **Never** | Quarterly view verification against a reference screenshot |
| Inventory never audited after the first one | Item-level theft becomes undetectable again | Nobody | Never | LIB-10 states *annually*, with the audit recorded — the recording is the control |
| Intrusion zone not armed | Nothing detects anything | Arming report, if read | Days–months | Automatic arming schedule; exception report for zones unarmed by 2100 |
| Central station contract lapses / list decays again | Response function gone | **Nobody** | **Never** | LIB-12 quarterly verification with a named owner |
| Fire or water in the SC room | Loss of the asset with no security failure at all | Building fire alarm | Minutes | **Rated safe with a fire rating**, which is why LIB-07 specifies both attack and fire |

**Five rows say *never*.** Four of the five are procedural, and all four mitigations are free.
This is the recurring result of the exercise: on this site, the failures that matter are not
equipment failures, and the fixes are not purchases.

### F3 — Three failures in the DVR situation

The situation — 4 cameras, 3 fps, 5 days retention, nobody has ever successfully retrieved
footage — contains at least three failures in three different categories:

1. **Category 9, design failure.** *Five days of retention against a discovery interval measured
   in weeks.* The spring break-in was discovered at opening, which was lucky; an item missing from
   special collections might be discovered in a year. **Retention must exceed the time to
   *discover*, not the time to respond**, and nobody made that calculation. 3 fps is a second
   design failure — adequate for presence, useless for a hand movement at a desk or a document
   going into a bag.

2. **Category 8, maintenance failure.** *Nobody has ever retrieved footage successfully.* This is
   not a broken component; it is a capability that was never established, never trained, and never
   tested. The system is, in effect, untested — unknown effectiveness and zero assurance.

3. **Category 6 or 4, human error / software failure.** *Export requires knowledge nobody has* —
   a proprietary player, a codec, a lost password, an expired licence, or simply a UI no staff
   member has been shown. In practice this presents as a staff member trying at 0900 on the
   morning after an incident and giving up.

> A fourth, worth naming: **category 7, malicious** — the DVR is in the staff area, which is on
> the intruder's path. The evidence of the break-in was standing in the room the burglar walked
> through. Recording device location is a design decision, and this one was made by the person
> with a spare shelf.

### F4 — An emergent failure

**The community room door and the intrusion system.**

The community room hosts evening events that run past 2000, when the library is otherwise closed
and the intrusion system is armed. Staff prop the exterior door for load-in. **The intrusion
system, correctly armed on schedule, now covers a building with an open exterior door** — so
either it generates repeated alarms (and gets disarmed, or the zone gets bypassed), or the zone
was bypassed long ago and nobody remembers.

**No component is faulty.** The scheduling is correct. The door hardware works. The propping is a
rational response to how the room is used. The failure lives in the **interface between the
building's *operating schedule* and the security system's *arming schedule*** — two things owned
by different people, neither of whom has seen the other's.

**The tell that this has already happened:** if the community room's exterior door is not on the
2009 intrusion system's zone list, or is on it as a permanently bypassed zone, that is this
failure, already resolved by whoever was on duty the night it first went off.

**Mitigation:** align the arming schedule with the room booking calendar, put a position switch
and a held-open alarm on the door outside event hours, and — the part that matters — make the
bypass state **visible** in a daily report, so a temporary bypass cannot quietly become
permanent.

---

## Part G — The deliverable

### G1 — The $60,000 allocation

| # | Item | Cost | Purpose |
|---|---|---|---|
| 1 | **Verify and maintain the after-hours call list; quarterly, named owner; annual unannounced test call** | **$0** | Restores the response function that failed in the only real incident this site has had |
| 2 | **Relamp the two east-end pole fixtures** | **$1,400** | Restores a control already paid for; addresses the staff-safety-in-the-lot finding |
| 3 | **Reorient and relocate the circulation desk** | **$3,000** | The single highest-value staff safety measure; furniture, not security |
| 4 | **Duress device at the desk + written response procedure + de-escalation training for all staff** | **$6,500** | The measures that actually reduce the staff-safety risk; the training is most of the value |
| 5 | **Rated safe for high-value special collections items, anchored** | **$9,000** | Part B5: takes the path from a 155 s deficit to a 325 s margin, and survives an unverified alarm. Also addresses fire and water. |
| 6 | **Special collections: door position monitoring, floor 2 intrusion detection, corridor camera** | **$8,500** | Detection at the asset; converts an undetectable loss into a detectable one |
| 7 | **Replace the DVR with a recorder: 30-day retention, staff-operable export, video verification to the central station** | **$14,000** | LIB-13/14. **Video verification alone is worth 300 seconds of police response.** |
| 8 | **Cameras: rear service door, community room exterior door, main entrance, special collections corridor (4 new)** | **$7,200** | The four locations where video has a defined job |
| 9 | **Light the rear service yard** | **$2,200** | Removes the concealment created by the refuse enclosure |
| 10 | **Community room: scheduled unlock, position switch, held-open alarm** | **$2,400** | Stops the design fighting the users; closes the propped-door boundary failure |
| 11 | **Item-level inventory of special collections, established and audited annually** | **$4,000** | The only control that detects theft during supervised access |
| 12 | **Commissioning: test every item above, including a timed duress activation and an unannounced call-list test** | **$1,800** | Without it, all of the above is a hypothesis |
| | **Total** | **$60,000** | |

### G2 — What is not funded, and why

- **More cameras in the stacks and public areas.** The board asked for cameras and this proposal
  funds four, all at boundaries. Cameras in a public library's stacks document ordinary library
  use, consume retention, and address nothing on the risk list. **Declined, explicitly.**
- **Exterior detection in the rear service yard.** Part B4(c) showed it works *only* if paired
  with fast assessment, and the safe (item 5) achieves more for less and survives the unverified
  response case. **Declined on value, not on principle.**
- **Hardening the rear service door.** The break-in cost a laptop and petty cash. That delay sits
  *before* the detection point in every variant, so it does not improve timeliness. **Not funded**
  — but note it is a cheap future item if the door needs replacing anyway.
- **A second evening staff member (LIB-04).** This is an **operating** cost, not capital, and it
  is not mine to fund. It goes in the memo as a recommendation to the Board, because it is
  probably the most effective remaining staff-safety measure.
- **Environmental control and archival storage for special collections.** Real, and outside this
  scope. Flag it and name it as someone else's project rather than absorbing it.

### G3 — The memo

---

> **MEMORANDUM**
>
> **To:** Director, Ashford Public Library
> **Re:** Security assessment and recommendations
> **Status:** For your review and for presentation to the Board. Three items need a Board
> decision.

**What we found**

Ashford is a well-used public building with two genuine problems and one that is close to free
to fix. The most serious is that your staff cannot see who is coming — the circulation desk faces
away from the door, which is behind them, and that is the common factor in the incidents of the
last year. The second is the local history archive: it is protected by a single ordinary lock at
the end of a corridor nobody can see, and if someone broke in at night they would be finished and
gone before anyone arrived. The third is that your alarm system worked perfectly during last
spring's break-in and then called a list of phone numbers that has not been updated since 2019.
**Nobody came, and that costs nothing to fix.**

**Staff safety — the first thing we would do**

The desk is 45 feet back from the entrance and faces the stacks, so anyone walking in is behind
your staff member's shoulder until they are already at the counter. Staff get no warning, no time
to read the situation, and no chance to defuse anything early. We recommend turning the desk to
face the door and bringing it forward about twenty feet. **This is a furniture change, not a
security installation** — reception desks face the door in most buildings, and it will read as
more welcoming rather than less. Alongside it: a quiet call button under the counter, a written
procedure for what happens when it is pressed, and de-escalation training for every staff member.

**The training is the part that will make the most difference**, and it is the part that a
security proposal usually leaves out. Most of the difficult situations at a public desk involve
someone unwell or in distress rather than someone dangerous, and no equipment helps with that.

**The archive**

We modelled a night-time break-in aimed at the archive. From the moment someone reaches your rear
yard to the moment they could leave with the deeds is about twelve minutes. Your alarm currently
notices them about three and a half minutes in, and it then takes roughly another minute and a
half to work out whether the alarm is real — so the call goes out at the five-minute mark, after
which police need ten. **They would be finished and gone with about two and a half minutes to
spare.**

The important part is this: **we cannot fix that by adding alarms.** We ran the numbers with a
sensor on the rear door and with sensors in the yard, and unless we *also* make the alarm
verifiable in seconds instead of a minute and a half, none of it arrives in time. And if police
treat the alarm as unverified — which is how it would be treated today — then **no alarm anywhere
on the property could be early enough**, because the whole break-in takes less time than an
unverified response.

**What does work is a good safe.** Putting the deeds, the original maps, and the earliest
photographs into a properly rated, anchored safe means the twelve minutes becomes closer to
twenty, and the response has time to arrive — with room to spare, and without depending on
anyone answering a phone. It also protects the same items from fire and water, which for
irreplaceable paper is a risk nobody has raised and which we think is at least as serious as
theft.

**Where the $60,000 goes**

| | |
|---|---|
| Update and maintain the emergency call list | **$0** — restores the response that failed last spring |
| Relamp the two east-end lot fixtures | $1,400 — staff will use those spaces again |
| Turn and move the circulation desk | $3,000 — staff can see the door |
| Call button, written procedure, de-escalation training | $6,500 |
| Rated safe for the highest-value archive items | $9,000 — the measure that actually protects them |
| Archive room: door alarm, upstairs detection, corridor camera | $8,500 |
| Replace the recorder: 30-day retention, staff can export it, alarms verified by video | $14,000 |
| Four cameras: rear door, community room door, main entrance, archive corridor | $7,200 |
| Light the rear service yard | $2,200 |
| Community room door: unlocks for events, alarms otherwise | $2,400 |
| Item-by-item inventory of the archive, audited annually | $4,000 |
| Testing everything above, including a surprise call-list test | $1,800 |

**What we are not recommending, including something you asked for**

The Board asked about cameras. **We have funded four, and we would advise against more.** Cameras
in the stacks and reading areas would record ordinary library use, would not have prevented any
of the incidents you described, and would sit uneasily with a library's commitment to letting
people read without being watched. The four we propose each have a specific job at a specific
door.

We are also not proposing anything that would control who enters the building or the reading
areas. That would be the most effective single measure available for the staff-safety problem,
and **we think it would cost you more than it is worth** — it is the opposite of what a public
library is for. We have designed around it deliberately, and the Board should know it was a
choice.

**Two things that cost nothing**

1. **Verify the after-hours call list this week**, name someone responsible for it, and check it
   every three months. This is the single highest-value item in this document.
2. **Check the exterior lights once a month** and fix them within two weeks. Two fixtures have
   been out for over a year, and that fact tells anyone paying attention more about this building
   than any camera does.

**For Board decision**

1. **A second staff member on duty after 1800.** An operating cost, not a capital one, so it is
   not in the budget above — but it is probably the most effective remaining measure for staff
   safety.
2. **Formal acceptance of the residual risks** listed in the register below. A building open to
   everyone carries risks that cannot be designed away, and it is appropriate for the Board to
   note that knowingly rather than to assume it has been solved.
3. **Archival environmental conditions** for the collection. Outside our scope, and we think
   someone should own it.

**Assumptions and open items**

| # | Item | Basis | Owner | By |
|---|---|---|---|---|
| 1 | Break-in timings (12 minutes) | Illustrative estimates, **not tested** | Us — to be timed on site | Before the safe is ordered |
| 2 | Police response 10 / 15 minutes | Published figure, never measured here | Library + police liaison | Before Board presentation |
| 3 | Archive appraised at $340,000 | Client-provided | Library | — |
| 4 | Safe rating (attack minutes, fire hours) | To be specified against a recognised standard | Us | With the equipment schedule |
| 5 | Lighting levels and uniformity targets | To be verified against IES guidance and local requirement | Us | After relamping |
| 6 | Archive room construction above the ceiling | **Unknown** — we could not inspect | Us — site visit | Before the room alarm is designed |
| 7 | Egress requirements at the community room and archive | To be confirmed against the adopted code | Us + code official | Before installation |
| 8 | Whether anything is already missing from the archive | **Unknown, and currently unknowable** | Library — inventory | Within 6 months |

> Item 8 is uncomfortable and we would rather say it than not: **without an item-level inventory,
> there is no way to know whether the archive is complete today.** The inventory is in the budget
> for that reason as much as for future protection.

---

## Marking guide

| Part | Full marks looks like |
|---|---|
| A | The Director's ranking challenged with reasons; the dead call list identified as the top finding *despite not being on their list*; staff safety understood as mostly a non-adversary problem |
| B | All four detection variants computed; **why B4(a) gains only 40 s** explained via the assessment term; the negative detection point at 900 s read as *not achievable*; the safe recommended with the warehouse contrast made explicit |
| C | Zone 1 recognised as the entire public floor area and the consequence drawn out; seven of nine integrity items honestly marked unknown; the study-room adjacency identified; the call list named as a non-equipment SPOF |
| D | At least two free findings; the desk fixed without a checkpoint; the two CPTED limits named honestly |
| E | The mission written as a constraint requirement rather than treated as an obstacle; LIB-14's exportability clause present; the top RTM row being a procedure |
| F | The 2009 failure located at *dispatch*, not at the equipment; five FMEA rows saying "never"; the emergent failure found at a schedule interface |
| G | A memo a board could read, with no jargon, one declined request, two free actions, and an honest register including item 8 |

**A weak submission produces a competent security design for a building that happens to contain
books.** The tell is a proposal that controls the entrance.

---

## Where this goes next

- [`../../35_Doors_and_Hardware/`](../../35_Doors_and_Hardware/) — the rear service door and the
  archive door in full depth
- [`../../32_Engineering_Math/`](../../32_Engineering_Math/) — the derivations behind Part B, and
  the pixel-density arithmetic behind the camera requirements
- [`../../02_Risk_Assessment/`](../../02_Risk_Assessment/) — where Part B becomes a full
  multi-path analysis rather than the single path you were handed
- [`../../27_Labs/project_01_secure_one_door/BRIEF.md`](../../27_Labs/project_01_secure_one_door/BRIEF.md)
  — the same reasoning at the scale of one opening
