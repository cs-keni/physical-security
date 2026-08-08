# Solutions — 06, Requirements Engineering

> For the exercises in
> [`../06_requirements_engineering.md`](../06_requirements_engineering.md).
> **Write your answers first.**

> **A note on E6.5.** The exercise refers to "the SEC-001..014 table above," but the lesson's
> RTM shows only four illustrative rows. The full set is **constructed below** so the exercise
> can be worked. Yours will differ; what should not differ is the *method* for cutting it.

> **The pixel-density figures in E6.4 were computed by running
> [`../../28_Calculators/psec/optics.py`](../../28_Calculators/psec/optics.py)**, with the
> derivation in
> [`../../32_Engineering_Math/02_pixel_density.md`](../../32_Engineering_Math/02_pixel_density.md).

---

## E6.1 — Convert each vague statement into ≥3 testable requirements

The rule for every one of these: **state the assumption you had to invent**, because you are
inventing it either way and the only question is whether the client gets to correct you.

### (a) "The loading dock needs to be more secure."

*Assumptions:* one overhead door and one personnel door; deliveries 0600–1400 weekdays; the
asset is palletised finished goods staged on the dock; no current monitoring.

| ID | Requirement | Type |
|---|---|---|
| a1 | The dock personnel door **shall** be monitored for forced-open and held-open conditions, with alarm annunciation at the monitoring position. | Functional |
| a2 | The overhead dock door **shall** report open/closed position to the security system, and an open condition outside the scheduled delivery window **shall** generate an alarm. | Functional |
| a3 | Video coverage of the dock apron **shall** achieve ≥ 38 PPF horizontal across the full width of the apron at the dock face, sufficient to recognise a person, under design nighttime illumination. | Performance |
| a4 | The dock personnel door **shall** permit free egress at all times without a credential, key, or special knowledge. | Constraint `[CODE][VERIFY]` |
| a5 | Delivery drivers **shall** be able to complete a delivery without a credential and without a staff escort into Zone 3. | Operational |
| a6 | Recorded video of the dock **shall** be retained for not less than 30 days. | Performance |

**a5 is the requirement that changes the design**, and it is the one nobody writes. If drivers
need to walk into the building, every locking decision on the dock is different — and a
requirement that ignores how the work is actually done produces a door that gets propped
(lesson 05, E5.1).

### (b) "We want to know who's in the building during an emergency."

*Assumptions:* single building; credential-controlled entry; the driver is fire-drill
mustering, not a regulatory head-count.

| ID | Requirement | Type |
|---|---|---|
| b1 | The access control system **shall** produce a list of credential holders whose most recent transaction was an entry, by area, within 60 seconds of request. | Functional + Performance |
| b2 | The muster report **shall** be obtainable from a location outside the building. | Operational |
| b3 | The report **shall** be obtainable while the building is in fire alarm, including when doors have released. | Operational |
| b4 | Visitors and contractors **shall** appear on the report with a host name and a contact number. | Functional |
| b5 | The report **shall** state its own limitations — specifically that it reflects credential use, not physical presence. | Operational |

**b5 exists because the requirement as stated cannot be met.** An access control system knows
about credential *transactions*. It does not know who tailgated in, who left through a
free-egress door without badging, or who is in the building without a credential. Writing b5
converts a false promise into a stated, bounded capability — and it is the difference between a
tool people use correctly in an emergency and one they trust wrongly.

### (c) "Visitors shouldn't be able to wander."

| ID | Requirement | Type |
|---|---|---|
| c1 | Movement from Zone 2 (public) to Zone 3 (employee) **shall** require a valid credential at every boundary opening. | Functional |
| c2 | Visitor credentials **shall** be valid only for the areas and the time window associated with their visit, and **shall** expire automatically at the end of that window. | Functional |
| c3 | Visitor badges **shall** be visually distinguishable from employee badges at 15 feet. | Performance |
| c4 | Visitor issuance **shall** complete in under 90 seconds per visitor at a peak arrival rate of 12 visitors per 15 minutes. | Performance |
| c5 | An expired visitor credential presented at any Zone 3 boundary **shall** generate an alarm at the monitoring position. | Functional |

**c3 is doing more work than it looks like.** The control that actually stops wandering in most
buildings is an employee noticing an unfamiliar badge, which is natural surveillance (lesson 05)
implemented through a graphic design decision. The readers handle the doors; c3 handles the
corridor.

### (d) "We need better cameras in the parking garage."

| ID | Requirement | Type |
|---|---|---|
| d1 | Video coverage **shall** achieve ≥ 20 PPF horizontal at grade across all pedestrian routes, stair and elevator lobbies, and the full width of drive aisles. | Performance |
| d2 | Video coverage of each vehicle entry and exit lane **shall** achieve ≥ 76 PPF horizontal at the lane plane, sufficient to identify an occupant. | Performance |
| d3 | Cameras **shall** produce usable images under design garage illumination without supplemental lighting, and **shall** maintain the stated pixel density with headlights directly in frame. | Performance |
| d4 | Recorded video **shall** be retained not less than 30 days. | Performance |
| d5 | Camera housings and mounts **shall** be rated for the garage environment, including exhaust deposit, humidity, and washdown. | Constraint |

**d3 is where garage designs actually fail.** Every camera meets its pixel-density number on a
spreadsheet. Half of them produce a white bloom and a silhouette when a car turns the corner
with its lights on, which is a wide-dynamic-range and mounting-angle problem that no resolution
requirement catches.

### (e) "The server room should be locked down."

| ID | Requirement | Type |
|---|---|---|
| e1 | Entry **shall** require two independent authentication factors. | Functional |
| e2 | The room boundary **shall** be continuous slab to slab on all sides, including above any suspended ceiling and through all penetrations larger than 96 in². | **Constraint** `[VERIFY]` |
| e3 | The door **shall** be monitored for position, forced-open, and held-open, with alarm annunciation. | Functional |
| e4 | Video **shall** cover the door approach at ≥ 76 PPF, retained not less than 90 days. | Performance |
| e5 | Access **shall** be granted by named individual, reviewed quarterly, with a record of the review. | Operational |
| e6 | Failure of the access control system **shall not** prevent egress, and **shall not** result in the door becoming unlocked. | Constraint |

**e2 is the only requirement on this list that will actually change the outcome**, and it is the
one a security engineer usually cannot enforce, because the wall belongs to the architect and
the ceiling belongs to the mechanical engineer. Write it anyway, in the security requirements,
and trace it — because when the partition is value-engineered back to grid height, the RTM is
the only artifact that shows what was lost.

---

## E6.2 — Identify the pathology and rewrite

### (a) "Provide a security system that meets industry best practices."

**Pathology: the Unfalsifiable Requirement.** There is no test. "Best practices" is not a
document, has no edition, and no two people will agree on its contents — which means the owner
can allege non-compliance at any time and the contractor can claim compliance at any time.

**Rewrite:** delete it and replace with the specific requirements it was standing in for. If a
reference is genuinely wanted:

> "The system **shall** comply with [named standard], [edition], sections [X–Y]."
> `[STANDARD][VERIFY]` — and you must name a real document with a real edition, or delete it.

### (b) "Install 4K cameras throughout."

**Pathology: the Solution Masquerading as a Requirement.** It specifies a technology, not an
outcome. It is also probably wrong: 4K everywhere multiplies storage and bandwidth (module
`32_Engineering_Math/03` and `04`) while a 4K camera on a 12 mm lens covering a corridor is
enormous overkill and a 4K camera on a 2.8 mm lens covering a 200-foot yard still will not
identify anyone.

**Rewrite:**

> "Video coverage **shall** achieve the pixel density stated per area in the camera schedule
> (Detect ≥ 8 PPF, Observe ≥ 19, Recognise ≥ 38, Identify ≥ 76 horizontal, at the stated target
> plane, under design illumination), measured at commissioning by the method in [test
> procedure]."

That requirement lets the designer pick resolution *and* lens *and* position as a system, which
is the only way any of the three can be chosen correctly.

### (c) "All doors shall have card readers." (200-door building, incl. janitor closets)

**Pathology: the Orphan Requirement** — it traces to no risk — layered over a **Solution
Masquerading as a Requirement**. It is also unaffordable and will be cut, which means it will be
cut *arbitrarily* by whoever is holding the budget rather than deliberately by whoever owns the
risk.

**Rewrite:**

> "Openings forming a boundary between security zones **shall** be access-controlled per the
> door schedule. Zone boundaries and the control at each are defined in [drawing/appendix].
> Openings interior to a single zone **shall not** be access-controlled unless a specific
> requirement is traced to them."

**The second sentence is the valuable one.** A stated default of *no reader* forces every reader
to be justified, which is what converts 200 readers into the 35 that were needed — and it does
so at design time rather than during value engineering.

### (d) "The system shall be scalable and future-proof."

**Pathology: Unfalsifiable.** "Future-proof" is not achievable and not testable; nobody knows
what the future needs. "Scalable" is meaningful only with a stated dimension and a stated bound.

**Rewrite:**

> "The head-end **shall** support expansion to 200 cameras and 150 controlled doors without
> replacement of servers, switches, or licensing tier."
> "Each IDF **shall** be delivered with not less than 20% spare switch ports and not less than
> 20% spare PoE budget at the design device count."
> "The system **shall** support device onboarding via [named open protocol], and **shall not**
> require proprietary licensing for third-party devices conforming to it."

Three testable statements. Note the second is checkable with `psec.power.PoESwitch` at design
review, which is the point of module 32 lesson 05.

### (e) "Per corporate standard, all secure areas require biometric access." (12-person office, one file room)

**Pathology: the Inherited Requirement.** It may be legitimate and binding. It was also almost
certainly written for a data centre or a headquarters, and it is being applied to a satellite
office where the "secure area" is a room with a filing cabinet.

**The rewrite is not a rewrite. It is a documented deviation request**, and this is the whole
teaching point of the exercise — **do not silently comply and do not silently ignore.**

> "**Deviation request DR-001.** Corporate Standard [ref], §[x], requires biometric
> authentication at secure areas. Applied to the [site] file room, this represents approximately
> $[n] of the $[m] project budget. The room contains [asset], with an assessed consequence of
> [x], protected by a stud partition to grid height in a leased suite with landlord key access.
> **Biometric authentication at the door does not address the dominant vulnerability.**
> Recommend: credential-only access at the file room, plus partition extension slab to slab and
> door position monitoring, at approximately $[n/3]. Requesting approval to deviate.
> Decision required by [date]. Owner: [name]."

Three things that does. It **names the person who decides** — you are not entitled to waive a
corporate standard and should not try. It **prices the alternative**, which is what makes the
deviation grantable. And it **states the mechanism**, so the decision-maker can see that the
standard's intent is better served by the deviation than by compliance.

---

## E6.3 — A full requirement set for Project 1

> Project 1 is [`../../27_Labs/project_01_secure_one_door/BRIEF.md`](../../27_Labs/project_01_secure_one_door/BRIEF.md),
> and it has its own reference solution in
> [`../../27_Labs/_solutions/project_01_reference.md`](../../27_Labs/_solutions/project_01_reference.md).
> **Work the project brief itself for the full treatment.** What follows is the shape your
> requirement set should have and the marking criteria.

**Shape: 10–15 requirements across all four types, with no type empty.** A set that is entirely
functional is the commonest failure — it describes what the system does and says nothing about
how well, how it fits the work, or what limits it.

A workable distribution for a single door:

| Type | Count | Typical content |
|---|---|---|
| Functional | 4–6 | Credential required in the secure direction; free egress; position monitoring; forced/held alarms; local annunciation; event logging |
| Performance | 3–4 | Pixel density at the door plane; retention period; alarm-to-video call-up time; standby duration; unlock latency |
| Operational | 2–3 | Who administers credentials; what happens when someone forgets a badge; how a delivery is handled; who responds and from where |
| Constraint | 2–3 | Egress and fire-code limits `[CODE][VERIFY]`; the fail state; landlord or base-building limits; existing head-end compatibility |

### Marking criteria

| Criterion | What good looks like |
|---|---|
| **Every requirement uses "shall"** | Not should, not will, not may. This is a contract convention, not a style preference. |
| **Every requirement is testable** | For each one, name the test. If you cannot, it is not a requirement. |
| **No product names in the requirements** | Basis-of-design products go in the specification, separately. |
| **Every requirement traces to something** | A risk, a code, a client statement, or a design principle. Orphans are either missing links or unnecessary scope. |
| **The fail state is stated explicitly** | Not implied by the hardware selection. It is a requirement and it belongs to the owner. |
| **At least one operational requirement about the failure case** | What happens when it breaks, when someone forgets a badge, when the network is down. |
| **The RTM rows are populated** | Req ID, traces-from, design element, drawing, spec section, test procedure, status. An RTM with empty test-procedure cells is a table, not a traceability matrix. |

**The single most common gap:** no requirement covering **degraded operation**. A door that
works perfectly and has no stated behaviour for a network outage, a power failure, or a fire
alarm is three unwritten requirements away from complete, and all three are the ones that get
argued about on site at 4 p.m. on a Friday.

---

## E6.4 — The submittal that meets resolution and misses pixel density

### The situation

SEC-006 requires **≥ 80 PPF** at the R&D lab door. The RTM's design element is a 4 MP camera
(2688 × 1520, 1/2.8" sensor) with a **4.3 mm** lens at 9'-0" AFF, covering a door at
approximately 26 ft. The contractor has submitted a camera meeting the resolution with a lens
yielding **62 PPF** at the door plane.

Working the numbers (slant range, 5 ft target plane):

| | Lens | Slant range | Scene width | **PPF** | DORI class |
|---|---|---|---|---|---|
| **Specified** | 4.3 mm | 26.3 ft | 32.9 ft | **81.8** | **Identify** |
| **Submitted** | ~3.3 mm | 26.3 ft | 42.8 ft | **62.8** | **Recognise** |

**The submitted camera is 21.5% short, and it crosses a DORI class boundary.** That second fact
is the one that matters and the one to lead with: the specified camera can identify a stranger;
the submitted one can only recognise someone already known to the viewer.

`max_range_ft("identify")` makes the same point from the other side: the specified lens meets
80 PPF out to **26.9 ft**, and the submitted one only to **20.6 ft**. The door is at 26.

### The submittal review comment

> **SEC-006 — REVISE AND RESUBMIT.**
>
> The submitted camera meets the specified sensor resolution but the submitted lens does not
> meet the pixel-density requirement at the design target plane. Calculated horizontal pixel
> density at the door plane is **62.8 PPF against a specified minimum of 80 PPF** (2688 px over
> a 42.8 ft scene width at a 26.3 ft slant range). SEC-006 requires ≥ 80 PPF.
>
> Note that resolution alone does not satisfy this requirement; pixel density is a function of
> sensor pixel count, focal length, and range, and only the first of the three was addressed.
>
> Resubmit with a lens of not less than **4.3 mm** at the design mounting position (calculated
> 81.8 PPF), **or** submit a revised mounting location with supporting pixel-density
> calculations at the door plane. Include the calculation, the assumed target plane, and the
> sensor dimensions used, so that it can be checked.
>
> Field verification of pixel density at the door plane is required at commissioning per
> **CX-VS-019** regardless of the approved submittal.

**Why it is written that way:** it states the number, the requirement, and the gap; it explains
the mechanism in one sentence, because the contractor may genuinely believe resolution is the
whole story; it gives **two** acceptable routes rather than dictating one, because the mounting
position may be cheaper for them to change than the lens; and it demands the calculation, which
prevents the next submittal from being another assertion.

### The two-sentence email to the client

> "The camera the contractor proposed for the R&D lab door meets the resolution we specified but
> uses a wider lens, which drops the detail at the door from the 80 pixels-per-foot we require
> down to about 63 — the practical difference is that we could recognise someone you already
> know, but we could not identify a stranger from the footage. I've marked it revise-and-
> resubmit with two acceptable fixes; neither should carry a cost or schedule impact, and I'll
> flag it immediately if the contractor claims otherwise."

**What that email does:** it translates the number into the **operational consequence** (a
stranger cannot be identified), which is the only part the client can evaluate; it does not use
the words pixel density, DORI, or slant range; and it pre-empts the change-order conversation,
because a contractor whose lens error becomes a cost claim is a problem the client should hear
about from you first.

---

## E6.5 — Cutting $900k to $650k

### The constructed requirement set

| ID | Requirement | Traces from | Est. |
|---|---|---|---|
| SEC-001 | Site perimeter vehicle gate, credentialed | RISK-04 vehicle access | $85k |
| SEC-002 | Exterior video, detect ≥ 8 PPF at perimeter | RISK-04 | $70k |
| SEC-003 | Credential required lobby → employee (Zone 2→3) | RISK-01 tailgating | $120k |
| SEC-004 | Lobby video, identify ≥ 76 PPF at the boundary | RISK-01 | $35k |
| SEC-005 | Two-factor at R&D lab | RISK-02 IP theft | $18k |
| SEC-006 | ≥ 80 PPF at R&D lab door | RISK-02 | $6k |
| SEC-007 | Zone 4 boundary continuous slab to slab | RISK-02 | $45k |
| SEC-008 | Access control on 38 Zone 3 boundary openings | RISK-01, RISK-03 | $190k |
| SEC-009 | Intrusion detection, after-hours, Zones 3–4 | RISK-03 after-hours | $55k |
| SEC-010 | Offline controller decisions + 10k event buffer | Graceful degradation | $12k |
| SEC-011 | 30-day retention, all cameras; 90-day Zone 4 | RISK-01..04, legal hold | $95k |
| SEC-012 | Monitoring workstation + alarm-to-video call-up ≤ 2 s | All | $60k |
| SEC-013 | Standby power, 4 h, all security systems | Availability | $48k |
| SEC-014 | Commissioning and documented test of every requirement | **Assurance** | $61k |
| | | **Total** | **$900k** |

### The cuts, in order, with the risk consequence stated

**Target: remove $250k.**

| Order | Cut | Saves | Risk consequence, stated plainly |
|---|---|---|---|
| 1 | **SEC-008 reduced** from 38 openings to the 14 that are actual zone boundaries | **$120k** | Interior office and storage doors lose electronic access control and audit. **Zone boundary control is unaffected.** Consequence: reduced internal compartmentalisation and no audit trail on 24 interior doors. This is the cut that removes the most money for the least risk, because most of those 38 readers were never traced to a risk. |
| 2 | **SEC-001 deferred** — gate operator and credential, keep the fence and the conduit | **$70k** | Vehicles enter the site uncontrolled. Perimeter *detection* (SEC-002) is retained, so the event is still seen. Conduit and pad are installed now so the retrofit is cheap. Consequence: RISK-04 is detected but not deterred or delayed. |
| 3 | **SEC-011 reduced** from 30 days to 21 days site-wide; **Zone 4 stays at 90** | **$30k** | Any incident discovered more than three weeks later cannot be investigated. **Recommend the client check their own discovery interval before accepting this** — if incidents are typically found monthly, this cut removes the ability to investigate anything. Zone 4's 90 days is regulatory and is not on the table. |
| 4 | **SEC-012 reduced** to one workstation instead of two | **$20k** | No redundant monitoring position. Single point of failure at the monitoring function, and no second operator during peak. |
| 5 | **SEC-009 reduced** to Zone 4 and perimeter openings only | **$10k** | After-hours intrusion into Zone 3 is not detected until it reaches Zone 4. Given SEC-002 and video retention, the event is recorded but not alarmed. |
| | **Total removed** | **$250k** | |

### What is explicitly *not* cut, and why

- **SEC-007 (the slab-to-slab boundary), $45k.** It is the cheapest item that makes SEC-005 and
  SEC-006 mean anything. Cutting it leaves $24k of controls on a boundary that stops at the
  ceiling grid — the E3.1(d) failure, bought deliberately.
- **SEC-014 (commissioning), $61k.** This is the one that always gets cut and it is the one that
  must not. **Uncommissioned, every other requirement on this list is a hypothesis.** Effectiveness
  is unknown and assurance is zero (lesson 02). Cutting commissioning does not save $61k; it
  converts $650k of installed work into $650k of unverified installed work.
- **SEC-010 (offline decisions), $12k.** Trivial cost, and it is the difference between a network
  outage being an inconvenience and being a building that cannot be entered or secured.

### The three-sentence framing to open the meeting

> "I've put together what a $650k version looks like, and I want to be clear up front that this
> isn't me finding efficiencies — every one of these cuts removes a control that was traced to a
> risk you identified, and I'll show you exactly which risk each one is. The good news is that
> the first cut is $120k and it's mostly readers on interior doors that were never traced to a
> risk in the first place, so we get almost half of what we need without touching your zone
> boundaries. The two I'd ask you to look hardest at are the retention reduction — because it
> depends on a number only you know, which is how long it typically takes you to discover an
> incident — and commissioning, which I'm recommending we protect, because without it you'd be
> buying six hundred and fifty thousand dollars of equipment that nobody has proven works."

**Why that framing:** it refuses the "efficiencies" euphemism, which protects you when something
is later found missing; it leads with the *easiest* cut so the meeting starts with agreement; it
hands one decision back to the client on a fact only they possess; and it makes one explicit
recommendation to protect, which is the only way commissioning ever survives.

**This is the RTM's whole payoff.** Without it, a 28% budget cut is a demoralising argument
about which products to delete. With it, it is a documented decision by the person entitled to
make it, with each removed control tied to the risk it was addressing — and that document is
also what protects you afterwards.

---

## The thread through all five

E6.1 turns statements into tests. E6.2 finds the four ways a requirement can be fake. E6.3 builds
the traceability. E6.4 is what the traceability buys you when a submittal arrives. E6.5 is what
it buys you when the budget is cut.

Notice that E6.4 and E6.5 are both **defensive** uses. Requirements engineering is often taught
as a design activity, and it is one — but the reason to do it properly is that six months later
somebody submits the wrong lens, or removes a quarter of the budget, and the RTM is the only
artifact that can tell you what was lost.

> Next: [`07_systems_and_failure_thinking.md`](../07_systems_and_failure_thinking.md) — where
> the requirement "the system shall be reliable" finally gets the treatment it deserves.
