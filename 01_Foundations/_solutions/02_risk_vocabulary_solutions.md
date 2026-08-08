# Solutions — 02, The Risk Vocabulary

> For the practice problems in
> [`../02_the_risk_vocabulary.md`](../02_the_risk_vocabulary.md).
> **Write your answers first.** These are worth almost nothing read cold.

**How these are marked.** Each problem asks for two things: *name the term(s) precisely* and
*state what additional information you'd need.* The second half is the harder one and the one
that matters. A junior engineer classifies the sentence. A senior engineer classifies it **and
knows what question comes next**, because every one of these statements is a client saying
something imprecise and expecting you to run with it.

**The single most common error across all eight:** hearing a sentence and jumping to a
countermeasure. Every problem below has an obvious product answer, and every obvious product
answer is premature.

---

## 1. "Our badge system is old."

**Term: none of them, yet.** This is a **statement about an asset's condition**, not a risk
statement. It contains no threat, no vulnerability, and no consequence.

It is most likely gesturing at a **vulnerability**, but "old" is not a vulnerability. Old
equipment that still performs its function against the relevant threats is not a weakness; it
is depreciated capital. The client has conflated *age* with *inadequacy*, which are correlated
and not the same.

**What you need to know:**

- Old how? Age of the panels, the readers, the credential technology, the software, or the
  support contract? These fail differently.
- **What credential technology?** This is the question that usually matters. A 125 kHz prox
  card is trivially clonable with equipment costing very little `[PRACTICE]`, and that *is* a
  vulnerability with a named threat. A 13.56 MHz card with secure element and diversified keys
  is not old in the way that matters.
- Is it still supported? Are spare parts obtainable? An unsupported system is a **maintenance
  failure** waiting to happen (lesson 07, category 8) — the risk is availability, not breach.
- What is it protecting? Age matters far more at a Zone 4 boundary than an interior office door.
- Has anything actually gone wrong, or is this an aesthetic and confidence judgement?

**The senior move:** ask what prompted the sentence. "Old" is often what a client says when
they mean "I do not trust it and I cannot tell you why," and the underlying reason —
unreliable reads, a badge that worked after termination, no audit trail anyone believes — is
the actual finding.

---

## 2. "There were two car break-ins in the lot last month."

**Term: two undesired events**, which are **evidence for likelihood** and evidence of an
exploited **vulnerability**.

Be careful with the word likelihood. Two events is a very small sample. It tells you the
likelihood is **not negligible**; it does not let you compute a rate with any confidence.
Treating n=2 as a frequency is one of the most common abuses of incident data.

**What you need to know:**

- **Asset and consequence:** what was taken, and whose? Vehicle contents, the vehicles, or
  catalytic converters? These imply different adversaries and different countermeasures.
- **Threat characterization:** opportunistic or targeted? Same MO both times? Time of day?
- Where in the lot, exactly? Two break-ins in the same dark corner is a **CPTED finding**
  (lesson 05). Two break-ins scattered randomly is a different problem.
- What is the base rate? Two in a 400-space lot in a high-crime area may be *below* the
  neighbourhood average. Two in a 20-space lot is alarming. **A number without a denominator
  is not data.**
- Is there a reporting bias? "Two reported" is not "two occurred."
- What is the consequence to the *client*, as opposed to the vehicle owners? Often it is
  employee fear and retention, not property loss — and that changes what a good answer looks
  like.

---

## 3. "If the chiller plant goes down, the whole floor of labs loses samples."

**Term: consequence.** A clearly stated one, which is rarer than it should be. It also names an
**asset** (the samples, and the research they represent) and implies a **dependency**: the
samples depend on the chiller plant, so the chiller plant is itself an asset by derivation.

**Note what is absent: any threat or hazard.** "Goes down" could be mechanical failure (a
hazard), power loss (a hazard), or sabotage (a threat). Those have almost nothing in common as
design problems, and the sentence does not distinguish them.

**What you need to know:**

- **What is the actual consequence?** Cost to replace, or irreplaceable? Multi-year research
  that cannot be repeated is a different order of magnitude, and it changes every downstream
  decision.
- **How long is the ride-through?** Minutes, hours, or days before loss begins? This is the
  single most important number, because it is the `T_R` the whole design has to beat.
- Is there monitoring and alarming on temperature *now*, and does it reach someone who can act
  at 3 a.m. on a Sunday?
- Is this a security problem at all? If the answer is "the chiller fails mechanically twice a
  year," it belongs to facilities and mechanical redundancy, and the security scope is limited
  to the deliberate-act case and to detection.
- Who owns this risk? Frequently nobody, which is why you were told about it.

**The senior move:** say plainly that most of this is not yours. Security engineers who accept
scope for problems they cannot solve end up owning the failure. The security-relevant parts are
(a) deliberate interference with the plant, and (b) detection and notification, which is a real
contribution. Say that, in writing.

---

## 4. "The night cleaning crew has master keys and isn't background-checked."

**Term: vulnerability**, specifically an **insider access** vulnerability — and the sentence
also implicitly characterizes a **threat** (a low-vetting, high-access population) and a
**countermeasure failure** (no screening).

This is the one that should make you sit up. It combines maximum access with minimum vetting
and minimum supervision, at the hour of minimum observation.

Full chain requested — see below.

**What you need to know:**

- What does "master key" actually open? A true grand master, or a floor master? Get the keying
  schedule.
- How many keys, held by whom, and is there a signed record? What happens when a cleaner
  leaves — is there a return procedure, and has a rekey ever happened?
- Is the crew a direct employee or a contracted vendor? If contracted, **what does the contract
  say about screening?** Very often it says something, and nobody has checked compliance.
- Is there any electronic audit trail? Mechanical keys generate no events (module
  `35_Doors_and_Hardware/08`), so the honest answer is usually no.
- What is inside the spaces those keys open, and what would the consequence be?

---

## 5. "We're in a hurricane zone."

**Term: hazard.** Not a threat — a hurricane has no intent, cannot be deterred, and does not
adapt to your countermeasures.

**Why the distinction has engineering consequences**, which is the point of the question:

| | Threat | Hazard |
|---|---|---|
| Responds to deterrence | Yes | No |
| Adapts to your design | Yes | No |
| Probability estimation | Hard, contested, intent-dependent | **Reasonably tractable** — actuarial and meteorological data exist |
| Design approach | Assume it finds the weakest path | Design to a stated return period |
| Concentrates or distributes | Concentrates on one point | Distributes across everything at once |

That last row is the one people miss. A hurricane hits every part of your system
simultaneously, which makes **redundancy far less useful than diversity** (lesson 04) and makes
common-cause failure the dominant concern.

**What you need to know:**

- Which consequences are in scope? Life safety, asset protection, and continuity of operations
  are three different projects.
- What is the design event? Return period, wind speed, and — usually the real problem — flood
  elevation. `[CODE][VERIFY]` The adopted building code and ASCE 7 as adopted govern this, and
  it is not a security engineer's determination.
- **Where is the equipment?** Head-end in a ground-floor room in a flood zone is the finding
  that writes itself.
- What is the post-event scenario? Looting during an extended outage with no police
  availability is a genuine security problem that follows the hazard, and it is routinely
  unplanned for.
- How long must the system run without utility power, and does anyone actually know the answer
  rather than assuming it?

---

## 6. "The CEO wants a panic button."

**Term: a proposed countermeasure**, with no stated asset, threat, vulnerability, or
consequence. This is the **Solution Masquerading as a Requirement** pathology from lesson 06,
arriving from the least contradictable person in the organization.

**What you need to know — and how to ask it:**

- **What happens when it is pressed?** This is the whole question. A button that summons a
  response nobody has defined is a liability that produces false confidence.
- Who responds, from where, in how long? If the honest answer is "reception calls 911," then
  the button's value is the seconds it saves over a phone, which may still be worthwhile — but
  say so.
- What prompted it? An incident, a peer's installation, a news story, or a specific fear?
  These lead to genuinely different designs.
- Duress or medical or both? Fixed or mobile? Silent or audible?
- **How will it be tested, and how often?** An untested panic button has zero assurance, and it
  is the archetypal example of the effectiveness-versus-assurance distinction.
- What is the false-activation plan? They will be pressed by accident, and if that produces an
  armed response the risk you have created may exceed the one you addressed.

**The senior move:** do not fight it. Install the button. Then insist that the **response
procedure** is written, assigned, and tested, because that is the part that actually protects
anyone, and it is the part that will not exist unless you make it a deliverable.

---

## 7. "Anyone can walk from the public lobby to the executive floor without passing a person."

**Term: vulnerability**, and specifically a **defense-in-depth failure** — the boundary between
Zone 1 (public) and a higher zone is not being enforced. It is also, precisely, a **missing
detection function** (lesson 03) rather than a missing barrier.

Note the phrasing: "without passing a person." The speaker is describing the absence of
**natural surveillance** (lesson 05) and the absence of a **control point**, not the absence of
a lock.

Full chain requested — see below.

**What you need to know:**

- What is *on* the executive floor that matters? Very often the honest answer is "people and
  confidential conversations," not property — which points at very different countermeasures.
- What is the path? Elevator, stair, or both? Is the elevator floor-restricted? Are stairs
  free-egress-only in the down direction, and does that create an entry path from below
  (lesson 04's egress-hardware row)?
- Is this actually true, or true only after hours?
- Has it happened? An actual incident changes the funding conversation entirely.
- What throughput and what visitor volume? The answer for 12 visitors a day is not the answer
  for 400.
- **What does the executive population actually want?** They will veto a turnstile in a lobby
  they consider a reception space. Knowing that before you design is the difference between a
  recommendation and a wasted month.

---

## 8. "Our competitor was hit by industrial espionage last year."

**Term: threat intelligence** — evidence about a **threat**'s intent and capability, and
evidence relevant to **likelihood**. It says nothing at all about *your* vulnerability, and
therefore nothing about your risk.

This is the most important distinction in the whole set. **A demonstrated threat plus no
vulnerability equals no risk.** The client has given you half a chain and is feeling the whole
thing.

**What you need to know:**

- What actually happened to the competitor, in mechanism terms? "Industrial espionage" covers
  a bribed employee, a cyber intrusion, a physical break-in, a photograph taken through a
  window, and a departing engineer with a USB drive. **Four of those five are not physical
  security problems.**
- Are you similarly exposed? Same asset type, same access model, same vendor, same building?
- What is your equivalent asset, where does it live, and in what form? Paper, screens,
  prototypes, conversations, or a server?
- Who has legitimate access, and what would it take for one of them to be the mechanism?
- Is there anything to detect? Espionage is characterized by the **absence of a detectable
  event** — nothing is missing afterwards. This is a genuine limit of the whole detect/delay/
  respond model (lesson 03) and it should be said out loud rather than papered over.

**The senior move:** the honest answer here is usually that most of the exposure is
cyber and personnel, not physical, and that the physical contribution is real but bounded.
Saying so costs you scope and buys you credibility, and lesson 01 argued that the trade is
worth it.

---

## The full chain for #4 and #7

### #4 — Cleaning crew with unscreened master key access

| Link | Content |
|---|---|
| **Asset** | Contents of every space the masters open. Requires enumeration — likely to include offices with confidential paper, IT spaces, and possibly a server room. Owner: whoever owns each space, which is part of the problem — nobody owns *the key system*. |
| **Threat** | An unscreened individual with legitimate physical access, unsupervised, during hours of minimum observation. Also the **coerced or recruited** insider, which screening does not fully address. Capability: total, physically. Intent: unknown, and unknowable without screening. |
| **Vulnerability** | (1) No screening, so intent is unassessed. (2) Master keying, so access is not proportionate to task — a cleaner needs to empty bins, not open the network closet. (3) No electronic audit trail, so use is unattributable. (4) Unsupervised hours. (5) Possibly no key return or rekey procedure, so the population with access is unknown. |
| **Undesired event** | Theft of property; theft of information (photographing documents or screens leaves *no trace at all*); unauthorized copying of a key; propping a door for a third party; installation of a device. |
| **Consequence** | Ranges from petty property loss to compromise of confidential information with regulatory or competitive impact. **The information cases have no detectable event**, which means the consequence is unbounded in time — you may never learn it happened. |
| **Countermeasure by function** | **Deter:** screening itself, plus visible logging and stated policy. **Detect:** electronic credentials in place of mechanical keys, giving an audit trail; door position monitoring; alarm on out-of-schedule access to Zone 3+. **Delay:** nothing useful — they have the key. **Respond:** after-hours access to high zones generates a supervised response. **Recover:** rekey procedure on departure; investigation capability from the audit trail. **Non-hardware:** background screening in the vendor contract, key-per-task instead of masters, and supervised cleaning of the highest zones. |
| **Residual risk** | Even with all of the above: a screened individual can still act, screening has finite predictive value, and an audit trail is a *deterrent and an investigative tool*, not a preventive control. Residual risk is meaningful and must be accepted explicitly by the owner. |

**The finding to write:** the cheapest high-value intervention is almost never a security
system. It is **removing the master keys from the cleaning crew** and giving them access only
to what the task requires, plus a screening clause in the vendor contract. Both cost close to
nothing and both reduce your own project scope. Lesson 01's argument that you must sometimes
recommend against your own interest is exactly this case.

### #7 — Public lobby to executive floor with no control point

| Link | Content |
|---|---|
| **Asset** | The executive population (life safety and personal security), confidential conversations and documents, and — usually underrated — the *continuity of executive function*. |
| **Threat** | Spectrum, and it matters that you name which one you are designing for: an opportunistic thief; a disgruntled former employee or terminated staff member; an aggrieved customer; an activist seeking access or disruption; a journalist; a targeted social engineer. Capability is low for most of these, which is the point — **the vulnerability is so cheap to exploit that low capability is sufficient.** |
| **Vulnerability** | No control point and no natural surveillance on the path between Zone 1 and a high zone. The boundary exists on the org chart and not in the building. |
| **Undesired event** | Unauthorized presence on the executive floor; confrontation; theft; observation of confidential material; in the worst case a violence event. |
| **Consequence** | From embarrassment to injury. Note that the *low-consequence* versions are far more likely and are what will actually happen; designing only for the worst case produces a design nobody will fund. |
| **Countermeasure by function** | **Deter:** visible reception presence and a clear boundary — this does most of the work. **Detect:** staffed reception with sightlines; credential-controlled elevator dispatch; door position and forced-door monitoring on stairs; video with assessment capability at the boundary. **Delay:** minimal and mostly beside the point — this is a detection problem, not a delay problem. **Respond:** a defined procedure for reception, which is the deliverable that will be missing. **Recover:** recorded video for investigation. **Non-hardware:** relocating reception so the sightline exists, which is a furniture decision, not a security purchase. |
| **Residual risk** | Tailgating through a controlled point remains possible and is the dominant residual. So does a visitor with a legitimate escort who then wanders. Accept explicitly, and manage with procedure rather than pretending hardware closed it. |

**The finding to write:** the primary control is a **staffed, well-sited reception position with
a sightline to the elevator lobby**, not a turnstile. It is cheaper, the executives will accept
it, it degrades gracefully, and it handles the social cases — the person who *looks* like they
belong — that no reader can. If reception cannot be sited to see the path, that is an
architectural finding and belongs in front of the architect while the drawings are still cheap
to change.

---

## What this practice set was actually testing

Nothing here required a calculation, a product, or a code lookup. Every problem tested whether
you can **hear an imprecise sentence and locate it on the chain** — and then name the missing
link.

Six of the eight statements are missing the same thing: **either a threat with no
vulnerability, or a vulnerability with no consequence.** Neither half is a risk. That is why
the vocabulary is worth the effort, and it is why the correct first response to almost any
client statement is a question rather than a recommendation.

> Next: [`03_functional_chain.md`](../03_functional_chain.md) — where the countermeasures in
> these answers get sorted into six functions, and where you find out that most designs are
> missing the same one.
