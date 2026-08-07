# 07 — Systems Thinking and Failure Thinking

## Learning objectives

- Trace a signal, a decision, and a human response end-to-end through a security system.
- Enumerate failure modes for any component using a structured taxonomy.
- Perform an informal FMEA on a security subsystem.
- Identify emergent failures that no single component causes.
- Make "what happens if this fails?" an automatic reflex.

---

## The central claim

> A camera is not a camera. A door is not a door. A reader is not a reader.
>
> Each is one node in a chain that ends in a **human decision** and a **human action**. If any
> link is broken, the node at the front is decoration.

Juniors design components. Seniors design chains. This lesson is the transition.

---

## Chain 1 — The video chain

Follow a photon to a conviction:

```
 SCENE           A person is at the loading dock at 0230
   │
   ▼ illumination — is there light? what spectrum? uniform? glare?
 LIGHT reaches the lens
   │
   ▼ optics — focal length, aperture, focus, DOF, IR-corrected?
 IMAGE on the sensor
   │
   ▼ sensor — size, sensitivity, dynamic range, shutter, noise
 RAW SIGNAL
   │
   ▼ ISP — exposure, WDR, noise reduction, white balance, sharpening
 PROCESSED IMAGE
   │
   ▼ encoder — H.264/H.265, bitrate mode, GOP, target quality
 COMPRESSED STREAM
   │
   ▼ network — switch port, PoE, VLAN, uplink, QoS, latency, loss
 STREAM ARRIVES at the recording server
   │
   ▼ recording — codec support, licensing, disk write, retention policy
 STORED VIDEO on disk / array
   │
   ▼ VMS — indexing, timestamps, search, permissions, health monitoring
 RETRIEVABLE VIDEO
   │
   ▼ display — workstation, monitor size/resolution, layout, ambient light
 VIDEO PRESENTED to the operator
   │
   ▼ human — attention, training, alarm queue, fatigue, workload
 OPERATOR PERCEIVES the event
   │
   ▼ decision — SOP, authority, confidence
 OPERATOR DECIDES to act
   │
   ▼ communication — radio, phone, dispatch
 RESPONSE INITIATED
   │
   ▼ evidence — export, format, hashing, chain of custody, retention
 EVIDENCE ADMISSIBLE
```

**Now the point:** ask "what fails here?" at *every* arrow.

| Stage | Representative failures | Who notices? |
|---|---|---|
| Illumination | Lights out; IR reflects off nearby wall; sun in lens at 1700 daily | Nobody, until footage is needed |
| Optics | Focus drifted; dirty dome; spider web; condensation; wrong lens for the distance | Nobody, until footage is needed |
| Sensor | Motion blur at low light (slow shutter); blown highlights; IR-cut filter stuck | Nobody |
| ISP | Over-aggressive noise reduction smears the face you needed | Nobody |
| Encoder | Bitrate cap destroys detail during motion; long GOP loses the key frame | Nobody |
| Network | Port down; PoE budget exceeded; VLAN misconfig; uplink saturated; packet loss | Health monitoring, *if configured* |
| Recording | Server down; license exhausted; disk full; retention silently shortened | Health monitoring, *if configured* |
| Storage | Array degraded; RAID rebuild; silent corruption | Storage alerts, *if monitored* |
| VMS | Wrong timestamp (NTP), permissions block the investigator, index corrupt | The investigator, at the worst moment |
| Display | Too many tiles; operator can't see detail; glare on the monitor | Nobody admits it |
| Human | Fatigue, alarm flood, untrained, on break, distracted, doesn't know the SOP | Post-incident review |
| Decision | No authority to act; unclear SOP; fear of being wrong | Post-incident review |
| Evidence | Export in a proprietary format nobody can play; no hash; broken custody | Legal, months later |

> 🧠 **The lesson to extract:** the majority of video-chain failures are **silent**. Nothing
> alarms. The system reports healthy. You discover the failure at the exact moment you needed
> the video — which is to say, after the incident, when it cannot be fixed.
>
> **This is why health monitoring and periodic image verification are design requirements,
> not operational niceties.** A camera that reports "online" while pointed at a wall, out of
> focus, or with its view blocked by new ductwork is online and useless. Modern VMS platforms
> can detect scene change, defocus, and signal loss — *specify it, configure it, and test it
> in commissioning.*

---

## Chain 2 — The access control chain

Follow a badge to an audit log:

```
 PERSON approaches a door
   │
   ▼ credential — card/mobile/biometric; is it enrolled? valid? not expired?
 CREDENTIAL PRESENTED to the reader
   │
   ▼ read — RF field, range, interference, reader health, card format
 CREDENTIAL DATA read
   │
   ▼ protocol — Wiegand (unauthenticated, one-way) or OSDP (bidirectional, can be encrypted)
 DATA TRANSMITTED to the controller
   │
   ▼ decision — cardholder in DB? access level includes this door? schedule active?
 ACCESS DECISION made  ← *this must work offline*
   │
   ▼ output — relay energizes/de-energizes; wiring; fuse; voltage
 LOCK ACTUATED
   │
   ▼ hardware — strike releases / mag drops / latch retracts; mechanical alignment
 DOOR UNLOCKS
   │
   ▼ human — person pulls the door within the unlock time
 DOOR OPENS  → DPS reports open
   │
   ▼ shunt — DPS alarm suppressed for the programmed time
 DOOR CLOSES → DPS reports closed, relocks
   │
   ▼ event — transaction generated
 EVENT TRANSMITTED to the head-end (or buffered if offline)
   │
   ▼ storage — database write, retention
 AUDIT LOG ENTRY exists and is retrievable
   │
   ▼ correlation — linked to video by time; is time correct on both?
 INVESTIGABLE RECORD
```

**Failure taxonomy for this chain:**

| Stage | Failure | Symptom the client reports |
|---|---|---|
| Credential | Lost, shared, cloned, not revoked after termination | "Someone got in who shouldn't have" |
| Read | Reader dead, RF interference, wrong format, range too short, metal mounting surface | "It doesn't read my card sometimes" |
| Protocol | Wiegand wire tapped/spoofed; OSDP not in secure channel | (silent — this is why OSDP w/ secure channel matters) |
| Decision | Controller offline with no local DB; DB not synced; access level wrong; schedule wrong | "Card accepted but door didn't open" or "worked yesterday" |
| Output | Relay failed, fuse blown, wire broken, voltage drop over a long run | "Beeps green, nothing happens" |
| Lock | Strike misaligned, mag not releasing, latch binding, door warped, closer misadjusted | "Have to push hard" / "door sticks" |
| Human | Person doesn't pull in time, holds door for others (tailgating) | Held-open alarms; unexplained presence |
| DPS | Magnet misaligned, gap too large, contact failed, wire cut | False forced-door alarms, or *no* forced-door alarms |
| Shunt | Too short (nuisance alarms) or too long (real events masked) | Alarm fatigue, or missed propping |
| Event | Buffer full, comm lost, event lost | Gaps in the audit trail |
| Time | Controller clock drift, no NTP, wrong timezone/DST | Video and access events don't line up |

> ⚠️ **"Card accepted but the door doesn't unlock" is the single most common access control
> complaint**, and it can originate at *five different stages*. This is exactly why systematic
> troubleshooting (module `30`, and `04_Access_Control/07`) beats guessing: you bisect the
> chain rather than swapping parts.

---

## The failure taxonomy — nine categories

Use this checklist on any system. It's structured so you can't skip a category by accident.

| # | Category | Ask |
|---|---|---|
| 1 | **Component failure** | What if this device dies? Degrades? Fails intermittently? |
| 2 | **Communication failure** | What if the network, the RS-485 bus, the fiber, the cellular backup drops? For how long is it tolerable? |
| 3 | **Power failure** | Utility loss, UPS depletion, generator failure, a tripped breaker, a blown fuse, voltage drop on a long run |
| 4 | **Software failure** | Server crash, database corruption, license expiry, failed update, memory leak, certificate expiry |
| 5 | **Configuration failure** | Wrong schedule, wrong access level, wrong VLAN, wrong shunt time, default password, wrong timezone |
| 6 | **Human error** | Wrong button, propped door, badge lent, alarm acknowledged without looking, wrong device replaced |
| 7 | **Malicious activity** | Tamper, bypass, credential compromise, network attack, insider misuse, evidence tampering |
| 8 | **Maintenance failure** | Not tested, not cleaned, not calibrated, battery never replaced, firmware never patched, spare parts unobtainable |
| 9 | **Design failure** | Wrong device for the environment, inadequate coverage, unbuildable detail, code violation, no consideration of degraded modes |

**Category 9 is yours.** The other eight happen to your design; this one *is* your design.
It's also the category that's hardest to see from inside, which is why design review
(module `33_`) exists.

> 🧠 **Certificate expiry (category 4) deserves special mention** because it's the modern
> silent killer. A TLS certificate expires on a Saturday and the VMS stops recording, or
> mobile credentials stop working, or the integration between PACS and the identity provider
> silently breaks. Nothing physical failed. Put certificate lifecycle in the O&M manual and
> the maintenance plan.

---

## Informal FMEA for security systems

Full Failure Modes and Effects Analysis is heavyweight. This lightweight version is
proportionate to most security projects and takes about an hour per subsystem.

For each component: list failure modes, effect, detection method, and mitigation.

**Worked example: door controller serving 8 doors**

| Failure mode | Effect | Currently detected by? | Time to detect | Mitigation |
|---|---|---|---|---|
| Loses network to head-end | No real-time monitoring; no credential changes; events buffered | Comm-loss alarm at head-end | Seconds | Local decision DB + 10k transaction buffer; alarm on comm loss; verify buffer depth in commissioning |
| Loses AC power | Runs on battery; then all 8 doors lose electronic control | Power-fail input to panel | Seconds | Battery sized for required standby `[VERIFY code minimum]`; low-battery supervision; documented fail state per door |
| Board failure | All 8 doors offline; fail state per door hardware | Comm loss + no events | Seconds–minutes | Spare board on site; distribute critical doors across panels so no single board serves two doors on the same path |
| Battery end-of-life (silent) | Appears healthy until a power failure, then immediate loss | Only if battery supervision configured **and tested** | Never, without testing | Battery supervision; annual load test; date-label batteries; PM schedule |
| Firmware bug after update | Unpredictable | Testing, if done | Variable | Change control; test on a non-critical panel first; documented rollback; never update the whole site at once |
| Wrong shunt time configured | Nuisance held-open alarms → operator disables the alarm | Alarm volume metrics | Weeks | Commissioning verification per door; review alarm statistics at 30/60/90 days post-occupancy |
| **Two doors on the same egress path on the same panel** | Board failure affects both layers of a two-layer path | **Nobody — this is a design failure** | Never | **Design review**: check panel assignment against zone layering |

That last row is the value of doing this exercise. It is invisible on a device schedule and
obvious in an FMEA.

---

## Emergent failures — nobody's component broke

The hardest failures come from *interactions*. No component is faulty; the system still fails.

**Example 1 — The fire alarm that unlocks the building.**
Fire alarm activates → per code, mag locks release on egress doors `[CODE][VERIFY]` → correct
and required. But: the design also released the mag locks on the *perimeter* doors, which
weren't on the egress path. Now, during an evacuation, the entire building is open, and
during the false alarm at 0200 last Tuesday it was open for 40 minutes with nobody inside.
No component failed. The *interface logic* was wrong.

**Example 2 — The cascade.**
UPS in the MDF fails → core switch drops → all cameras and all controllers lose head-end
comms → controllers go offline-autonomous (good) → but the VMS also loses its NTP source →
and when power restores, controllers and cameras come back with drifted clocks → video and
access events for the outage window cannot be correlated. One failure, four consequences,
none of them the thing you were worried about.

**Example 3 — The anti-passback lockout.**
Anti-passback is enabled. A reader fails on the way out. Users exit through a door with no
reader. Next morning, the system believes they are still inside and denies entry. Now 200
people are queued at the door and someone props it. Anti-passback worked exactly as designed
and produced a security failure.

**Example 4 — Success as a failure mode.**
Analytics are tuned well and start generating 400 accurate alerts/day. The two-person SOC
cannot process them. Within a month, the analytic is disabled. The system worked; the
*sociotechnical system* did not. **Always check that the alarm volume your design produces is
within the operator's capacity.** This is a calculation you should actually do: expected
alarms/hour × handling time per alarm vs. operator hours available.

> **The habit:** after designing each subsystem, ask *"what does this subsystem do to the
> others, and what do they do to it?"* — especially across the fire/security boundary, the
> IT/security boundary, and the design/operations boundary. Those three interfaces produce
> most emergent failures because they're the ones where nobody owns both sides.

---

## The eight questions (make these automatic)

Ask these of **every** design decision. Print them. They are the operational form of
engineering judgment.

1. **What asset does this protect, from whom, against what act?**
2. **Which protection function does it perform** — deter, detect, delay, assess, respond, recover?
3. **What happens if it fails?** Silently or noisily? Who finds out, and how fast?
4. **What happens on power loss?** On network loss? During a fire alarm? During evacuation?
5. **What does the operator have to do because this exists?** Can they actually do it, at 3 a.m.?
6. **How will it be maintained,** by whom, how often, and can they physically reach it?
7. **How will we know it works** — at acceptance, and in year four?
8. **Is there a simpler design that achieves the objective?**

Question 8 is the one that most distinguishes senior engineers. Complexity is easy to add and
nearly impossible to remove. Every device, every integration, every clever piece of logic is
something that can break, must be documented, must be commissioned, must be maintained, and
must be understood by whoever replaces you. **The best design is the simplest one that meets
the requirements** — and "meets the requirements" is the constraint that keeps this from
being an excuse for laziness.

---

## Junior vs. Senior

**Junior:** can trace a chain when prompted; uses the failure taxonomy as a checklist; asks
what happens on power and network loss.

**Senior:** traces chains without prompting; anticipates emergent failures at the fire/IT/ops
interfaces; catches the "success as failure mode" problem by checking alarm volume against
operator capacity; and reflexively looks for the simpler design before defending the clever
one.

---

## Exercises

**E7.1** Trace the full chain for an **intrusion detection** event, from stimulus to response,
in the style of chains 1 and 2. Then build the failure table.

**E7.2** Run the informal FMEA on a **PoE switch serving 24 cameras** in an IDF. At minimum
cover: switch failure, uplink failure, PoE budget exceeded, UPS failure, IDF over-temperature,
firmware update, and a configuration error. Include the "who detects it and how fast" column.

**E7.3** For each, identify the emergent failure and the interface where it originates:
- (a) A security vestibule is interlocked so only one door opens at a time. The fire alarm
  releases both. A visitor is in the vestibule during the alarm.
- (b) IT applies a network-wide policy blocking multicast. The VMS uses multicast for video
  walls.
- (c) The access control system syncs from HR nightly. A terminated employee's badge works
  for up to 24 hours.
- (d) Cameras are on the building's standby generator. The recording server is not.
- (e) A new HVAC duct is installed in a corridor during a later fit-out, directly across
  three camera views. Nobody tells the security team.

**E7.4** Take your Project 1 door design. Apply all nine failure categories. Produce at least
two failure modes per category (some will feel forced — do it anyway; the forced ones are
where the surprises are).

**E7.5** A proposed design has: analytics on 60 exterior cameras, each generating an average
of 8 alerts per day; a SOC staffed by one operator per shift; SOP requires 90 seconds of
review per alert. Compute the operator's alert workload as a fraction of their shift. Is the
design viable? What are three ways to fix it, and which do you recommend?

> Solutions: [`_solutions/07_systems_failure_solutions.md`](_solutions/07_systems_failure_solutions.md)

---

## Retrieval check

1. Name the nine failure categories.
2. Why are most video chain failures silent, and what design requirement follows from that?
3. List five stages at which "card accepted but door doesn't unlock" can originate.
4. What is an emergent failure? Give an example from the fire/security interface.
5. What are the eight questions, and which one is most often skipped?
6. Why is "the analytics work well" a potential failure mode?

---

## References

- Garcia, M.L., *The Design and Evaluation of Physical Protection Systems*, 2nd ed. `[PRACTICE]`
- Leveson, N., *Engineering a Safer World* `[PRACTICE]` — systems-theoretic accident modeling.
  Written for safety, and the most useful book you can read on emergent failure. Highly
  recommended given your background.
- Perrow, C., *Normal Accidents* `[PRACTICE]` — on tight coupling and interactive complexity.
- IEC 60812 — *Failure modes and effects analysis (FMEA and FMECA).* `[STANDARD]`
  `[VERIFY current edition]`
- Dekker, S., *The Field Guide to Understanding 'Human Error'* `[PRACTICE]` — for the human
  links in the chain. Changes how you write SOPs.

---

**Module 01 complete.** Now:
1. Take [Quiz 01](../25_Quizzes/quiz_01_foundations.md) if you haven't.
2. Import [the flashcard deck](../26_Flashcards/01_foundations.csv).
3. Start [Project 1](../27_Labs/project_01_secure_one_door/BRIEF.md).
4. Update [`progress_tracker.md`](../00_Roadmap/progress_tracker.md).
