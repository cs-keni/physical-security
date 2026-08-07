# 06 — Requirements Engineering: "Make It Secure" → Testable Requirements

## Learning objectives

- Convert a vague client statement into a set of traceable, testable requirements.
- Distinguish functional, performance, operational, and constraint requirements.
- Write a requirement that a contractor can build to and a commissioning agent can test.
- Build a requirements traceability matrix linking risk → requirement → design → test.
- Recognize and neutralize the four requirement pathologies.

---

## Why this lesson may be the most immediately useful one in the module

You have a software background, so you already know the shape of this: a requirement that
can't be tested isn't a requirement, it's a hope. Physical security engineering has exactly
the same disease as software, with an added complication — **the artifact that expresses
the requirement is a drawing and a specification, and it becomes a legal contract document.**
Ambiguity in it doesn't produce a bug report; it produces a change order, a delay claim, or a
system that fails acceptance.

This is also where your background gives you a visible edge on day one. Most physical
security engineers were never taught requirements engineering formally. You were.

---

## The problem

The client says:

> "We need this building to be secure."

This is not a requirement. It's a feeling. You cannot design to it, price it, build it, test
it, or ever be judged to have satisfied it. Worse, it's *unfalsifiable* — after an incident,
you will be told the building wasn't secure, and you will have no defense.

Your job is to convert it into statements that are:

| Property | Meaning | Test |
|---|---|---|
| **Specific** | Names the location, asset, or system | Can you point at it? |
| **Testable** | A pass/fail can be determined | Could a commissioning agent write a test script? |
| **Traceable** | Links back to a risk or a client objective | Can you answer "why is this here?" |
| **Achievable** | Physically and economically possible | Would a contractor bid it? |
| **Unambiguous** | One reading only | Would two contractors price it the same? |
| **Necessary** | Removing it would matter | What breaks if you delete it? |

---

## The elicitation funnel

You get from feeling to requirement through structured questioning. Here is the funnel,
with the actual questions.

```
   "Make it secure"
          │
          ▼  ── WHY NOW? ─────────────────────────────────────
   What triggered this project? (incident, audit, insurer,
   customer, lease, new construction, an executive's anxiety)
   → tells you the real success criterion
          │
          ▼  ── WHAT MATTERS? ─────────────────────────────────
   Assets, owners, consequence of loss (lesson 01, Q1 & Q4)
          │
          ▼  ── FROM WHOM? ────────────────────────────────────
   Threats, characterized (lesson 01, Q2 & Q3)
          │
          ▼  ── WHAT MUST NOT HAPPEN? ─────────────────────────
   Undesired events, ranked by consequence
          │
          ▼  ── WHAT MUST STILL WORK? ───────────────────────────
   Operational requirements: throughput, hours, staffing,
   visitor volume, deliveries, accessibility, tenant experience
          │
          ▼  ── WHAT ARE THE LIMITS? ──────────────────────────
   Budget, schedule, code, landlord, union, aesthetic,
   existing systems, IT policy, corporate standards
          │
          ▼
   REQUIREMENTS
```

### The questions that actually produce answers

Clients cannot answer "what are your assets?" — it's an abstraction they've never had to
articulate. These work better:

- **"Walk me through what happens if I show up at 6 a.m. and want to get to [X]."**
  Elicits actual operations, not the policy fiction.
- **"What's the worst day you've had here?"** Elicits incident history and real fear.
- **"What would you have to tell your CEO about?"** Elicits consequence thresholds.
- **"What are you required to do by someone else?"** Elicits regulatory, contractual, and
  insurer drivers — the ones that actually have budget attached.
- **"What do people complain about today?"** Elicits the operational constraints that will
  kill your design if you ignore them.
- **"Who has keys? All of them? Are you sure?"** Elicits the truth, usually after a pause.
- **"What did the last consultant recommend, and why didn't you do it?"** Elicits the real
  constraints, and saves you from re-proposing something already rejected.
- **"If you had to give up one of these, which?"** Elicits actual priority ranking, which
  nobody volunteers.

> 🧠 **The single most valuable question in this profession:** *"What happens at 3 a.m.?"*
> Almost every security design is validated against the daytime, staffed, everything-working
> case. Ask about nights, weekends, holidays, outages, and the day the guard called in sick.

---

## The four requirement types

Every security requirement is one of these. Mixing them up produces documents nobody can act on.

### 1. Functional — *what the system must do*
> "The system shall detect and annunciate the opening of Door 112 at any time the door is in
> a secured state."

Verb-driven. Describes behavior, not product.

### 2. Performance — *how well it must do it*
> "Video coverage of the main entrance vestibule shall achieve a minimum of 60 pixels per
> foot horizontal across the full width of the door opening at the door plane, under design
> illumination conditions."

Numeric, measurable, with stated conditions. **The conditions clause is what juniors omit and
what makes the requirement testable.** "60 PPF" without "at the door plane, across the full
opening, under design illumination" is not testable — it's true somewhere in every camera's
field of view.

### 3. Operational — *how it must fit the way people work*
> "Employee ingress at the north entrance shall accommodate a peak flow of 300 persons within
> the 15-minute period beginning at 0745 without a queue exceeding 6 persons."

This is the category most often skipped, and skipping it produces designs that get defeated
by their own users. A security vestibule that can't handle shift change will be propped open
within a week — permanently.

### 4. Constraint — *what limits the solution*
> "No modification to the exterior facade is permitted (landlord restriction, lease §7.3)."
> "All network devices shall reside on VLANs managed by the Owner's IT department per
> corporate standard IT-SEC-004."
> "Total installed cost for Division 28 scope shall not exceed $1.4M."

Constraints are requirements too, and unstated constraints are the number one source of
late-stage redesign. Ask for them explicitly.

---

## From vague to testable — worked conversion

**Client statement:** *"We need this building to be secure."*

**After elicitation, you learn:** it's a 5-story, 90,000 sq ft corporate HQ; the driver is a
customer security audit that flagged "inadequate access controls" and threatens a contract;
assets are people (450 employees), a data room, an R&D lab with prototypes, and continuity of
operations; the threats of concern are opportunistic theft (three laptop thefts in 18 months,
all during business hours, no forced entry — **so: tailgating or insider**), and unauthorized
access to R&D by competitors or visitors; there is a receptionist 0800–1700 and no guards;
response is police, ~15 min; the building is leased and the facade cannot be modified;
budget is roughly $900k; IT owns all networking; the customer audit must be satisfied within
9 months.

**Now the requirements write themselves.** Note that each has an ID and a traceability link.

| ID | Type | Requirement | Traces to |
|---|---|---|---|
| SEC-001 | Functional | All perimeter doors shall be monitored for position and shall annunciate forced-open and held-open conditions to the monitoring workstation and to a mobile notification. | RISK-03 unauthorized entry |
| SEC-002 | Performance | Held-open annunciation shall occur no more than 30 seconds after the programmed shunt expires; forced-open within 3 seconds. | RISK-03; enables timely detection |
| SEC-003 | Functional | Access from the Zone-2 lobby to Zone-3 employee areas shall require an authenticated credential presented at a reader, on every elevator and stair path. | RISK-01 laptop theft (tailgating) |
| SEC-004 | Operational | Lobby-to-employee-area access shall accommodate 300 persons in the 15-minute 0745 peak with a queue not exceeding 6 persons at any turnstile lane. | Ops constraint; prevents propping |
| SEC-005 | Functional | The R&D lab (Zone 4) shall require two authentication factors for entry and shall log all entries and exits. | RISK-02 R&D access |
| SEC-006 | Performance | Video at the R&D lab door shall achieve ≥ 80 PPF horizontal at the door plane, sufficient for identification of a known individual, under all operating illumination. | RISK-02; supports investigation |
| SEC-007 | Functional | The R&D lab shall be equipped with volumetric intrusion detection, armed automatically outside published operating hours. | RISK-02 after-hours access |
| SEC-008 | Performance | Recorded video shall be retained for not less than 30 days for all cameras, with the R&D lab and data room cameras retained for 90 days. | Customer audit requirement CA-11 |
| SEC-009 | Functional | Access control shall integrate with the Owner's identity system such that termination in HR revokes physical access within 4 hours. | RISK-04 insider / audit CA-07 |
| SEC-010 | Functional | Door controllers shall continue to make access decisions from a locally cached credential database and buffer not fewer than 10,000 transactions during loss of communication to the head-end. | Graceful degradation |
| SEC-011 | Constraint | No penetrations or attachments to the building facade. | Lease §7.3 |
| SEC-012 | Constraint | All IP devices shall reside on Owner-managed VLANs per IT-SEC-004; the security system shall not require inbound internet access. | Owner IT policy |
| SEC-013 | Operational | Free egress shall be maintained at all times from all occupied spaces without the use of a credential, key, or special knowledge. | `[CODE]` life safety `[VERIFY with AHJ]` |
| SEC-014 | Performance | Total installed cost of Division 28 scope shall not exceed $900,000 including all labor, materials, licensing, and first-year warranty. | Budget |

**Look at what just happened.** "Make it secure" became 14 statements, each of which:
- a contractor can bid,
- a commissioning agent can test,
- you can defend in a design review,
- and which trace back to a specific risk or driver.

**And note SEC-013.** It's a requirement that constrains all the others, it's non-negotiable,
and it must appear explicitly — because if it doesn't, someone will propose a mag lock on a
required exit and it will get built.

---

## Writing a good requirement: the grammar

Use **"shall"** for mandatory. Not "should" (recommendation), not "will" (statement of fact),
not "may" (permission). This convention is universal in specification writing and violating
it creates real contractual ambiguity.

**Template for functional:**
> [Subject] **shall** [verb] [object] [under conditions] [within performance bound].

**Template for performance:**
> [Measurable property] **shall** be [comparison] [value] [units] [at/under stated conditions],
> [measured by method].

**Bad → Good:**

| Bad | Why it's bad | Good |
|---|---|---|
| "Provide adequate camera coverage of the parking lot." | "Adequate" is untestable | "Video coverage of the parking area shall achieve ≥ 20 PPF horizontal at grade across all pedestrian walkways and the full width of vehicle drive aisles, sufficient for detection of a person, under design nighttime illumination." |
| "Cameras shall be high quality." | Meaningless | Specify resolution, sensitivity, WDR range, frame rate, codec, and the pixel-density target driven by the operational use |
| "The system shall be reliable." | Untestable | "The video management system shall be configured such that failure of any single recording server results in loss of recording for no more than 16 cameras and for no more than 60 seconds." |
| "Doors shall be secure." | Undefined | Specify locking type, monitoring, alarm conditions, and fail state per door in the door schedule |
| "Install a Brand-X 5MP dome at each entrance." | Product, not requirement; forecloses alternatives and hides the *why* | State the performance requirement; name the basis-of-design product separately if you need to set a quality level |
| "Response time shall be fast." | No metric, no measurement point | "Time from alarm annunciation to display of the associated camera on the monitoring workstation shall not exceed 2 seconds." |

> ⚠️ **The product-vs-requirement trap.** Writing "provide a Model 1234" is easy and feels
> definitive. It is a *specification* decision, not a *requirement*. Requirements state what
> must be achieved; specifications state one acceptable way to achieve it. Keep them separate,
> because when Model 1234 is discontinued mid-project — and it will be — the requirement tells
> you what an acceptable substitute must do. This is the entire logic of "basis of design"
> specification writing (module `11_Division_28/`).

---

## The Requirements Traceability Matrix (RTM)

This is the artifact that ties the whole project together, and it's the single most
software-engineer-shaped tool in the discipline. It answers "why is this here?" for every
device on every drawing.

| Req ID | Requirement (abbrev.) | Traces from | Design element | Drawing | Spec section | Test procedure | Status |
|---|---|---|---|---|---|---|---|
| SEC-003 | Credential required lobby→employee | RISK-01 | 4 optical turnstile lanes + 1 accessible gate, ACS-1 | SE-101, SE-501 | 28 13 00 | CX-AC-004 | Verified |
| SEC-005 | 2FA at R&D lab | RISK-02 | Reader + keypad, door 4-118 | SE-104 | 28 13 00 | CX-AC-011 | Verified |
| SEC-006 | ≥80 PPF at R&D door | RISK-02 | CAM-4-118, 4MP, 4.3mm, 9'-0" AFF | SE-104, SE-601 | 28 23 00 | CX-VS-019 | Open |
| SEC-010 | Offline decisions + 10k buffer | Grace. degr. | ACP-1..6 w/ local DB | SE-701 riser | 28 13 00 §2.4 | CX-AC-022 | Verified |

**Why build this:**
- **Design reviews become trivial.** "Why is this camera here?" → point at the row.
- **Value engineering becomes rational.** When the owner cuts 20%, you can show exactly which
  requirements — and therefore which risks — are being dropped. This converts a demoralizing
  budget fight into an informed decision by the person entitled to make it.
- **Commissioning writes itself.** Every requirement with a test procedure ID becomes a test.
- **Scope creep becomes visible.** A device with no requirement traced to it is either an
  omission in your RTM or a device nobody needs. Both are worth knowing.
- **It protects you.** After an incident, "the design met requirements SEC-001 through
  SEC-014, which were derived from the risk assessment dated X and approved by the Owner on
  Y" is a categorically different position than "we did what seemed right."

**Build it in Excel or a CSV in your device dataset** (module `16_Automation/data_model/`).
It's a join table. You know what to do with it.

---

## The four requirement pathologies

**1. The Solution Masquerading as a Requirement.**
> "We need a mantrap at the front entrance."

That's a solution. The requirement underneath might be "prevent tailgating into Zone 3," which
could also be met by turnstiles, a staffed post, tailgate detection analytics, or an
anti-passback policy — each with different cost, throughput, and aesthetics. Always ask:
*what would this accomplish?* Then write **that** as the requirement, and evaluate the
client's proposed solution as one candidate. Do this gently; the client is often attached to
their idea, and the goal is a better outcome, not a demonstration that you're cleverer.

**2. The Inherited Requirement.**
> "It's in our corporate standard."

Sometimes legitimate and binding. Sometimes a 2009 decision nobody remembers, being applied
to a facility it was never meant for. Ask what it's for. If it doesn't fit, escalate it as a
documented deviation request rather than silently complying or silently ignoring.

**3. The Unfalsifiable Requirement.**
> "The system shall provide comprehensive security."

Delete it or make it testable. If you cannot write a test, it is not a requirement, and
leaving it in a contract document means the owner can claim non-compliance at will.

**4. The Orphan Requirement.**
A requirement that traces to no risk and no driver. Often a leftover from a template, a
previous project, or an enthusiastic vendor. Every orphan is either a missing traceability
link (fix it) or unnecessary scope (delete it and save the money).

---

## Junior vs. Senior

**Junior:** can write testable functional and performance requirements from a given risk
assessment; maintains the RTM; catches "adequate" and "high quality" in draft documents.

**Senior:** elicits requirements from a client who doesn't know what they want, in one
meeting, without it feeling like an interrogation; recognizes the solution-masquerading-as-
requirement immediately and reframes it without embarrassing anyone; knows which requirements
the client will fail to fund and sequences the conversation accordingly; writes the
operational requirements that keep the design from being defeated by its own users; and uses
the RTM as a negotiating instrument during value engineering rather than as documentation
after the fact.

---

## Exercises

**E6.1** Convert each into at least three testable requirements. State any assumption you
need, and label each requirement's type.
- (a) "The loading dock needs to be more secure."
- (b) "We want to know who's in the building during an emergency."
- (c) "Visitors shouldn't be able to wander."
- (d) "We need better cameras in the parking garage."
- (e) "The server room should be locked down."

**E6.2** Identify the pathology in each and rewrite:
- (a) "Provide a security system that meets industry best practices."
- (b) "Install 4K cameras throughout."
- (c) "All doors shall have card readers." (applied to a 200-door building including
  janitor closets and interior office doors)
- (d) "The system shall be scalable and future-proof."
- (e) "Per corporate standard, all secure areas require biometric access." (applied to a
  12-person satellite office with one file room)

**E6.3** Take Project 1 (`27_Labs/project_01_secure_one_door/`) and write a complete
requirement set (aim for 10–15 requirements across all four types), plus the RTM rows.

**E6.4** You wrote SEC-006 (≥80 PPF at the R&D lab door). The contractor submits a camera
that meets the resolution but with a lens that yields 62 PPF at the door plane. Write the
submittal review comment. Then write the two-sentence email to the client explaining the
issue and its consequence.

**E6.5** The owner cuts the budget from $900k to $650k. Using the SEC-001..014 table above,
propose what to cut, in order, with the risk consequence of each cut stated plainly. Then
write the three-sentence framing you'd open the meeting with.

> Solutions: [`_solutions/06_requirements_solutions.md`](_solutions/06_requirements_solutions.md)

---

## Retrieval check

1. Name the six properties of a good requirement.
2. What are the four requirement types, and which one is most often omitted?
3. Why must a performance requirement include a conditions clause?
4. What is the difference between a requirement and a specification, and why keep them separate?
5. What does an RTM let you do during value engineering that you otherwise couldn't?
6. Name the four requirement pathologies and how you'd address each.
7. What is the single most valuable elicitation question, and why?

---

## References

- ISO/IEC/IEEE 29148 — *Requirements engineering.* `[STANDARD]` Software-oriented; the
  requirement quality criteria transfer directly and it's a fast read for you.
- ASIS International — *Protection of Assets*, Security Management volume, on program
  development. `[GUIDELINE]`
- CSI — *Project Delivery Practice Guide* and *Construction Specifications Practice Guide.*
  `[GUIDELINE]` How requirements become specifications in the AEC world. Relevant to module `11_`.
- ASHRAE Guideline 0 / commissioning literature — the *Owner's Project Requirements* (OPR)
  concept, which is the AEC industry's name for exactly this artifact. `[GUIDELINE]`
  `[VERIFY current edition]` Worth knowing: if a project has a commissioning agent, an OPR
  probably already exists and your requirements should align to it.

**Next:** [07 — Systems Thinking and Failure Thinking](07_systems_and_failure_thinking.md)
