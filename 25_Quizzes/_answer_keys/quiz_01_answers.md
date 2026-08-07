# Quiz 01 — Answer Key and Explanations

> **Stop.** If you have not written your answers down, go back. Reading these first will make
> you feel like you understood the material and will not teach you anything.

Read the explanation for **every** question, including the ones you got right. The
explanations contain material the questions don't.

---

## Part A

**1. (b) A hundred-year flood.**
A hazard has no intent. The engineering consequence is not academic: **hazards don't adapt.**
A flood will not notice you moved the generator and pick a different route. An adversary
will. This is why security design assumes the adversary knows the design — the same reasoning
as Kerckhoffs's principle in cryptography.

**2. (c) Vulnerability.** A weakness a threat could exploit. Note it is stated well: it names
*what is missing* (position switch) and *why it matters* (not observed), rather than just
"no camera at the rear door," which would be a shopping list item.

**3. "…buy time and produce information."**
Test every device against this. A fence buys a little time. A monitored camera produces
information. A mechanical lock buys time and produces *nothing* — which is why an unmonitored
lock is a weaker control than it appears.

**4. The owner** — the person accountable for the assets. **Not you.** Your obligation is to
identify it, characterize it as best you can, present it clearly in language the owner
understands, recommend, and **document the acceptance**. This is a professional boundary that
protects both of you.

**5. Avoid, Reduce/Mitigate, Transfer/Share, Accept.** Insurance performs **transfer**. It
moves the *financial consequence* to another party. It does **not** prevent the event, restore
operations, protect people, or repair reputation. Clients conflate "we're insured" with "we're
protected" constantly.

**6.** Because "adequate" is meaningless without an adversary. A 6-ft fence is not a
vulnerability against a shoplifter and is a vulnerability against a fit, determined,
tool-equipped intruder. **"Is this fence adequate?" is unanswerable.** "Is this fence adequate
against an unequipped individual attempting entry unobserved at night?" is answerable.

**7. Deter (secondary — only if visible and *believed*), Recover (primary).**
It does **not** detect and does **not** assess, because both require a human in the loop in
real time. Enormous numbers of camera systems are sold on the implicit claim that they detect.
Be precise about this with clients — it is one of the fastest ways to establish that you are
an engineer rather than a salesperson.

**8. `(T_T − T_D) > T_R`**, i.e. `T_A > T_R`. Total adversary task time minus time-to-
detection-and-assessment must exceed response force time.

**9.** Because the delay is consumed while nobody knows the adversary is there. They work at
leisure. A hardened door in an unmonitored area is a speed bump attacked without time
pressure. **Delay only counts after detection** — this is the single most important idea in
the functional chain.

**10. Sensor activation → signal transmission → annunciation to a human or system.**
If annunciation is missing, there is no detection at all — a sensor tripping into an
unmonitored panel has detected nothing. This is exactly why **supervision** exists: the system
must be able to detect its own failure to detect.

**11. Effectively near zero.** Not because the sensor stopped working, but because the
operator stopped believing it. Alarm fatigue is not a human weakness to be trained away; it is
a *rational* response to a system that lies 40 times a night. Within weeks the alarms are
acknowledged without assessment, and eventually the zone is bypassed "temporarily."
**A design generating alarms nobody believes is a failed design regardless of datasheet `P_d`.**

**12.** (i) It must actually **cover the detection zone** — not the general area. (ii) It must
be **automatically called up on alarm** — if the operator hunts for it among 300 cameras,
assessment costs 45 seconds you don't have. (iii) It must have **enough image quality for the
decision required** — tie the pixel-density target to the decision (person vs. animal? weapon
or not?), not to habit.

**13. Redundancy** = a second *identical* thing (two servers). **Diversity** = a second
*different* thing achieving the same function (PIR + microwave). **Diversity is more valuable
against a thinking adversary**, because an adversary who knows how to defeat one technology
usually cannot defeat a different one simultaneously — and because diversity also survives
common-mode failures and environmental conditions that defeat one technology entirely. Rule of
thumb: **redundancy against failure, diversity against defeat and environment.**

**14.** The system loses capability *progressively* rather than totally. Example: on loss of
network, controllers keep making access decisions from a locally cached database, buffer
transactions, maintain locking, and alarm locally — degraded but functional, versus a brittle
design that simply stops.
**It must be specified at design time** because it is a *purchasing* decision (does the
controller have local decision-making and adequate buffer depth?) and a *configuration*
decision. It is cheap at design and effectively impossible to retrofit.

**15. Balanced protection:** all penetration paths through a boundary should present roughly
equal delay, and the boundary's real delay is the **minimum** across paths, not the average.
**Canonical violation:** a vault door in a drywall partition — or, in real buildings, a
hardened server room door in walls that stop at the ceiling grid.

**16.** Natural Surveillance, Natural Access Control, Territorial Reinforcement,
Maintenance/Image, Activity Support, Target Hardening.

**17.** Because hardening can *undermine* the other five. Bars on windows destroy natural
surveillance and signal a dangerous area, which reduces legitimate activity, which reduces
surveillance, which increases crime — the "fortress effect." It is also the most expensive
risk reduction per dollar. Apply 1–5 first; harden the residual.

**18.** An employee side entrance added for convenience becomes the de-facto main entrance,
bypasses reception entirely, and is propped daily.
**A door alarm cannot fix it** because the problem is not the door — it is that the controlled
entrance is not where people want to walk. You are asking hundreds of people to accept a daily
inconvenience, and they won't. The fix is understanding circulation during design and putting
the controlled entrance on the natural path. *Design problems that manifest as behavior
problems cannot be solved with hardware.*

**19. Functional, Performance, Operational, Constraint.**
**Operational is most often omitted.** When it is, you get designs that are defeated by their
own users — a security vestibule that can't handle shift change is propped open within a week,
permanently.

**20.** Example: *"Video coverage of the loading dock apron shall achieve a minimum of 40 PPF
horizontal at the plane of the dock doors across the full width of all four dock positions,
and a minimum of 20 PPF horizontal at grade across the full truck maneuvering area, under
design illumination conditions."* Assumptions to state: number of dock positions, whether the
operational need is recognition of persons (justifying 40) or only detection, and what design
illumination is.
The key move is adding the **conditions clause** — "40 PPF" alone is true somewhere in every
camera's field of view and therefore untestable.

---

## Part B

**21.**
- **(a)** Business hours + no forced entry = the person had **access**. Either an insider, or
  an outsider who walked in unchallenged (tailgating or an uncontrolled entrance). The absence
  of forced entry is the most informative fact and it points away from the perimeter entirely.
- **(b)** Three good ones: *"Walk me through what happens when someone the receptionist
  doesn't recognize walks in at 2 p.m."* / *"Were the laptops in occupied areas or empty
  offices, and were they secured?"* / *"Who has access to those areas, and how do you know?"*
- **(c)** **Partially, and probably not the way they expect.** Cameras support *recovery*
  (investigation, evidence) and weak *deterrence*. They do not detect or prevent this. If the
  actor is an insider, cameras document an authorized person doing an authorized-looking
  thing. The likely higher-value interventions are access control at the suite boundary,
  visitor escort policy, and a laptop-securing policy — all cheaper than a camera system.
  **Say this.** The client may still buy cameras; they'll buy them for a defensible reason,
  and they will remember that you told them the truth.

**22.**
- **(a)** **Balanced protection.** The boundary's delay is its minimum path, and the ceiling
  plenum path is the minimum.
- **(b)** Roughly **30–60 seconds**: stand on furniture, push up a ceiling tile, climb over the
  partition. No tools required. The Grade 1 lock and the biometric reader are irrelevant to
  this path.
- **(c)** Recommend extending the walls **slab to slab** (or installing security mesh above
  the wall line) *before* spending anything on the reader. Framing that works: *"The biometric
  reader is a good control and I'd like you to have it — but right now it protects a door that
  an intruder can walk around in about 40 seconds by lifting a ceiling tile. If we close the
  wall first, the reader you've already budgeted becomes the actual boundary instead of a
  formality. Same money, ordered differently."* You've validated their decision, named the
  problem concretely, and given them a sequence rather than a refusal.

**23.** Predictable sequence: (1) Wind, rain, and animals generate nightly alarms. (2) Every
alarm triggers a police dispatch because there is no way to verify it. (3) Police respond to
repeated unverified alarms; within weeks the site is deprioritized, fined, or placed on a
non-response list (jurisdiction-dependent `[VERIFY]`). (4) Staff begin bypassing zones "during
windy weather." (5) Within 3–6 months the system is effectively off, and a $400k investment
protects nothing.
**The missing function is ASSESS.** Detection without assessment is frequently not a partial
system but a net-negative one, because it consumes the credibility that response depends on.

**24.**
- **(a)** **Configuration failure** at the design level — arguably category 9, design failure,
  since the interface was never coordinated.
- **(b)** It is emergent because **no component failed.** The network works as IT designed it;
  the VMS works as the vendor designed it. The failure lives in the *interaction*, and it is at
  the IT/security boundary — one of the three interfaces (fire/security, IT/security,
  design/operations) that produce most emergent failures, because nobody owns both sides.
- **(c)** The IT/security interface should have been explicitly coordinated during design:
  a written requirement stating the network services the security system depends on
  (multicast, QoS, NTP, VLANs, port counts, PoE, inter-VLAN rules), reviewed and signed by IT.
  This belongs in the Basis of Design and as constraint-type requirements.

**25.** The system believes those users are still inside. The next morning it denies them
entry. Two hundred people queue at the door; someone props it; the propped door defeats both
anti-passback and the access boundary for the rest of the day. **Anti-passback functioned
exactly as designed and produced a security failure.** The lesson: a correctly functioning
control is not the same as a security outcome. Controls that punish users for the *system's*
faults will be defeated by users, and the defeat is usually worse than the risk the control
addressed. Mitigations: soft anti-passback, timed reset, reader supervision with alarm on
failure, and an operational procedure for bulk reset.

**26.**
- **(a)** 60 × 8 = **480 alerts/day**. × 90 s = 43,200 s = **12.0 hours** of review.
- **(b)** Against a 24-hour staffed day: **50% of the operator's *entire* shift time**, doing
  nothing but alert review — no patrols, no calls, no visitors, no breaks, no incidents.
- **(c)** **Not viable.** Realistically, an operator has perhaps 20–30% of their time
  available for alert handling. Three fixes: (i) **tune the analytics** — filter by zone,
  time, direction, object class, and size to cut volume, accepting some reduction in `P_d`;
  (ii) **reduce scope** — apply analytics only to the cameras where a real-time response is
  actually possible and warranted, and leave the rest as forensic-only; (iii) **change the
  response model** — add staff, or route low-priority alerts to a queue reviewed in batch
  rather than in real time.
  **Recommend (i) + (ii) together.** Adding staff is the owner's decision and the most
  expensive option; tuning and scoping are engineering decisions you can make, and they
  address the actual problem — that you designed an alarm volume exceeding operator capacity.
  This is "success as a failure mode": the analytics working well is what breaks the system.

---

## Part C

**27.**
- **(a)** `T_T` = 120+25+60+40+180+300 = **725 s**.
  Detection at completion of the suite door task = 120+25+60 = 205 s, plus 25 s assessment →
  `T_D` = **230 s**. `T_A` = 725 − 230 = **495 s**. Margin = 495 − 420 = **+75 s**.
- **(b)** **Yes, timely** — but only just. 75 s of margin on inputs that are all estimates is
  thin. If the safe takes 200 s instead of 300, or response is 480 s instead of 420, it fails.
  Report it as *marginal* and recommend margin.
- **(c)** `T_D_max` = `T_T − T_R − margin` = 725 − 420 − 90 = **215 s**.
- **(d)** At t = 215 s the adversary is **crossing the office floor** (that task runs
  205 → 245 s). So detection must occur no later than about 10 s into that traverse. Current
  detection lands at 230 s — 15 s too late. **The fix is not more hardware; it's moving
  detection one layer earlier** (e.g. detect at the *exterior* door rather than the suite
  door, or reduce assessment time by pre-linking the camera to the alarm so the operator isn't
  hunting). That's a configuration change worth 25 seconds and costing nothing, which is a
  much better answer than a stronger safe.

**28.**
- **(a)** Margin = 495 − 1500 = **−1005 s** (short by nearly 17 minutes).
- **(b)** You'd need `T_A > 1500`, so `T_A` must increase from 495 to 1500 → **1005 s
  (≈ 17 minutes) of additional delay after the detection point.**
- **(c)** **Not achievable.** That means turning the cash room into a vault and the safe into
  a substantially higher-rated unit — likely well past the value of what's inside, and past
  what the structure will accept. Recommend instead, in this order: (i) **reduce the
  consequence** — reduce cash on hand, increase deposit frequency, use a time-delay safe
  (which converts the problem: a robber who can't open it quickly is a different threat model
  entirely); (ii) **change the response model** if the asset value justifies it; (iii)
  **accept a documentation-only posture** for after-hours and design deliberately for evidence
  quality and recovery.
  Framing for the owner: *"With a 25-minute response, no amount of hardware we can reasonably
  build will let anyone interrupt this. That's not a criticism of the budget — it's just
  arithmetic. So the real choice is whether to reduce what's here, change who responds, or
  accept that the system's job after hours is evidence rather than prevention. All three are
  legitimate; I just don't want you to think you're buying the first one when you're buying
  the third."*

**29.**
- **(a)** **25 s** — the window. The boundary is its weakest path, not its average, and the
  240 s wall contributes nothing to the boundary's rating.
- **(b)** To reach 150 s you must fix **both** sub-150 paths: the window (25 s) and the ceiling
  plenum (45 s). Minimum set: upgrade the glazing (security film, laminated glazing, or a
  grille — each with different cost, appearance, and egress implications) **and** close the
  plenum (extend the wall slab to slab, or install security mesh above the wall line).
  The door at 180 s and the wall at 240 s already exceed the requirement and need **nothing**.
- **(c)** New boundary delay = **150 s**, set by whichever of the two fixes lands lowest —
  by design, right at your requirement.
  **What to spend on next: nothing on this boundary.** That is the discipline. Once a boundary
  meets the requirement derived from your timely-detection analysis, further hardening buys
  nothing measurable. The next dollar goes to whichever *other* boundary or function is now
  the weakest link — most likely detection coverage or assessment, since you've just
  demonstrated you can compute what delay you actually need.

**30.**
- **(a) and (b):**

| SPOF | What stops working |
|---|---|
| Access control server (no failover) | Real-time monitoring, credential changes, reporting, alarm annunciation. **Doors keep working *only if* controllers make decisions locally** — verify this, don't assume it |
| Recording server | All video recording. Live view may survive; evidence does not |
| PoE switch per floor | Every camera and IP device on that floor goes dark, including the Zone 4 door camera if it's on that floor |
| MDF (single room) | Fire, flood, or loss of cooling there takes the entire system |
| Single UPS (implied) | Everything drops together, including the "redundant" things sharing it |
| Single network path/conduit | One cable strike isolates a floor or the building |
| Zone 4 detection: motion armed only when unoccupied | An authorized person who stays past occupancy, or an intruder entering while occupied, is undetected — a *logic* SPOF |
| One administrator account (implied) | Compromise or departure = total loss of control |
| One person who knows the system (implied) | The most common real-world SPOF, and mitigated by *your* deliverables: as-builts, O&M manuals, device schedules |

- **(c)** Ranked by cost-effectiveness:
  1. **Controllers with local decision-making + adequate transaction buffer.** Near-zero
     incremental cost at design time, converts total access-control failure into graceful
     degradation, and is impossible to retrofit. Highest return in the list by a wide margin.
  2. **Documentation and as-builts** (mitigating the bus-factor SPOF). Costs your time, not
     capital, and it is the difference between a system that survives staff turnover and one
     that becomes unmaintainable in year three.
  3. Recording server failover / N+1 — real capital cost, but evidence loss is often the
     consequence that actually matters to the owner.
  4. Distributing critical devices across switches — cheap if planned at design, expensive
     later.
  5. Secondary head-end location — expensive; justified only by consequence.

  The top two are the answer because **they cost almost nothing at design time and cannot be
  added later.** That asymmetry — cheap now, impossible later — is the thing to look for
  whenever you're prioritizing.

---

## After the quiz

1. For every miss, find the lesson section and re-read *just that section*.
2. Add your missed items to your flashcard deck as cards in your own words.
3. Write in your decision journal: which answer surprised you most, and why?
4. Update [`progress_tracker.md`](../../00_Roadmap/progress_tracker.md) with your score.
