# Solutions — 07, Systems and Failure Thinking

> For the exercises in
> [`../07_systems_and_failure_thinking.md`](../07_systems_and_failure_thinking.md).
> **Write your answers first.**

> **The PoE figures in E7.2 and the workload arithmetic in E7.5 were computed**, not estimated
> — E7.2 with [`../../28_Calculators/psec/power.py`](../../28_Calculators/psec/power.py),
> derived in [`../../32_Engineering_Math/05_poe.md`](../../32_Engineering_Math/05_poe.md).

---

## E7.1 — The intrusion detection chain, and its failure table

### The chain, stimulus to response

```
   PHYSICAL EVENT           A person opens a door / crosses a beam / breaks glass
        │
        ▼
   TRANSDUCTION             Sensor converts the physical change into an electrical state
                            (reed switch opens, PIR detects IR differential, acoustic
                            transducer detects the glass signature)
        │
        ▼
   LOCAL DECISION           Sensor or panel input applies its own logic: sensitivity
                            threshold, pulse count, cross-zone, entry delay, and
                            whether the zone is ARMED
        │
        ▼
   SIGNAL TRANSMISSION      Zone → panel over a supervised loop or bus
        │
        ▼
   PANEL DECISION           Panel applies arming state, schedule, partition, and
                            alarm-vs-trouble classification
        │
        ▼
   COMMUNICATION            Panel → central station or head-end, over IP, cellular,
                            or POTS, with a supervision heartbeat
        │
        ▼
   ANNUNCIATION             Alarm presented to a human — central station operator,
                            on-site SOC, or a phone notification
        │
        ▼
   ASSESSMENT               Human determines what actually caused it (video call-up,
                            call list, or a guard walking there)
        │
        ▼
   DISPATCH DECISION        Someone decides to send a response, and to whom
        │
        ▼
   RESPONSE                 Responder travels and arrives.  This is T_R.
```

**The step people leave out of this diagram is ARMING**, and it is where most intrusion systems
actually fail. A perfect sensor on a disarmed zone is a wire.

### The failure table

| Stage | Failure mode | Effect | Detected by? | Time to detect | Mitigation |
|---|---|---|---|---|---|
| Transduction | Magnet gapped, misaligned, or defeated with an external magnet | No alarm on open | Nothing, unless the contact is high-security with tamper | **Never** | High-security balanced magnetic switch where it matters; tamper supervision; physical inspection in PM |
| Transduction | PIR masked, sprayed, or blocked by stored goods | Zone blind | Anti-mask supervision, if fitted and enabled | Never without it | Specify anti-mask; walk-test in PM; **housekeeping** — stacked pallets in front of a PIR is the real-world version |
| Local decision | Sensitivity set too low to avoid nuisance alarms | Detection probability silently reduced | Nobody. Alarm counts go *down*, which reads as improvement | **Never** | Walk-test results recorded at commissioning; treat a falling alarm rate as a question, not a success |
| Local decision | **Zone not armed** | Nothing detects anything | Arming reports, if anyone reads them | Days–months | Automatic arming schedule; exception report for zones not armed by a set time; make this a monitored KPI |
| Transmission | Loop cut or shorted | Zone lost | End-of-line supervision → trouble | Seconds | Supervised loops; treat trouble with the same urgency as alarm |
| Panel | Wrong partition / wrong schedule / wrong entry delay | Alarm suppressed or delayed | Testing only | Never, without testing | Commissioning verification per zone; re-verify after any programming change |
| Panel | Panel power failure, battery end-of-life | Total loss after ride-through | AC-fail and low-battery supervision | Seconds, if configured | Battery sized to the required standby `[CODE][VERIFY]`; **annual load test**, because a battery reports healthy until it is asked to work |
| Communication | IP path down, cellular backup never tested | Alarms never reach the station | Supervision heartbeat, at whatever interval it is set to | Minutes–hours | Dual path; **test the backup path**, do not assume it; verify the supervision interval is short enough to matter |
| Annunciation | Central station on hold / operator overloaded | Delay before anyone looks | Station metrics, rarely shared | Variable | Contractual response time with reporting; audit it |
| Assessment | **No video on the alarming zone** | Cannot determine cause | Nothing | N/A | Video coverage of every alarmed boundary with automatic call-up. This is E3.1(b) again |
| Assessment | Chronic nuisance alarms | Operator acknowledges without looking | Alarm statistics | Weeks | Fix the *source*; review alarm counts at 30/60/90 days post-occupancy |
| Dispatch | Call list is out of date | Nobody reachable | Only during an incident | Never | Quarterly call-list verification, with the verification recorded |
| Response | `T_R` far longer than assumed | Not timely (lesson 03) | Only by measuring | Never, without a test | **Unannounced timed test at 0300 on a Sunday** |

**The pattern to notice:** the "time to detect" column contains the word *never* six times. Six
of these failure modes are silent — the system reports healthy while the function is gone. That
is what the lesson means by saying assurance is a separate property from effectiveness, and it
is why every one of those six rows has *testing* rather than *hardware* in the mitigation
column.

---

## E7.2 — Informal FMEA: a PoE switch serving 24 cameras in an IDF

**First, compute the as-designed state**, because one of the failure modes turns out not to be
hypothetical:

```
   24 cameras × 15.4 W (802.3af PSE class allocation)  =  369.6 W
   Switch PoE budget                                    =  370.0 W
   Utilisation                                          =  99.9 %
   Ports used 24 of 24                                  =  0 free
```

`PoESwitch.check()` returns:

> `INSUFFICIENT SPARE PORTS: 0 free, 5 required at 20%.`
> `POE BUDGET TIGHT: 100% utilised. Adding one more device may fail; check growth plan.`

**This switch is already at its limit on both constraints before anything has failed.** Every
row below is worse than it looks because there is no margin anywhere.

| Failure mode | Effect | Currently detected by? | Time to detect | Mitigation |
|---|---|---|---|---|
| **Switch failure** | All 24 cameras down. If this is one floor of a building, an entire zone loses video simultaneously | Loss of stream at the VMS; SNMP if configured | Seconds–minutes, **if the VMS alarms on stream loss and someone reads it** | Verify the VMS alarms on camera offline and that it reaches a human; cold spare on site; distribute high-value cameras across two switches |
| **Uplink failure** | Same as switch failure from the head-end's perspective — cameras are powered and unreachable. **Edge recording, if fitted, keeps working** | Stream loss | Seconds | Dual uplinks on diverse paths; edge SD recording on the highest-value cameras (diversity, not redundancy) |
| **PoE budget exceeded** | **Not hypothetical — this design is at 99.9%.** Add one camera, or replace one with a heated outdoor unit that classifies 802.3at, and the switch begins denying power. Which port loses power depends on the switch's priority configuration, which nobody has set | Cameras drop offline in an order nobody predicted | Minutes, and it will be **misdiagnosed as a camera fault** | Design to ≤ 80% budget; set per-port PoE priority so the losses are chosen rather than arbitrary; `[VERIFY]` whether the switch allocates by class or by draw |
| **UPS failure or depletion** | Switch down → 24 cameras down. If the recorder is elsewhere on a different UPS, the recorder stays up and records nothing, which looks healthy | UPS supervision, **if configured and monitored** | Seconds if supervised; **never** if not | Supervise the UPS and route the alarm somewhere a human sees; runtime test annually under real load; document required standby duration |
| **IDF over-temperature** | Switch throttles, then shuts down. PoE switches at high load are a significant heat source in a small closet, and this one is at 99.9% of its PoE budget | Environmental monitoring, if fitted — usually it is not | **Never**, typically. Discovered as intermittent, seasonal, afternoon camera dropouts | Temperature sensor in every IDF, alarmed; coordinate IDF cooling with the mechanical engineer at design time; this is a **design failure** (category 9) if the heat load was never given to them |
| **Firmware update** | Unpredictable: PoE behaviour changes, VLAN config lost, extended reboot, or a bug affecting all 24 ports | Testing, if any | Variable | Change control; test on a non-critical switch first; never update the whole site in one window; documented rollback and a known-good config backup |
| **Configuration error** (wrong VLAN, wrong PoE mode, disabled port, wrong QoS) | Cameras unreachable, or reachable with video that stutters under load | Depends entirely on the error. QoS errors are the worst — everything works until the network is busy | Minutes to **months** | Configuration backup and diff; commissioning verification per port; document the intended config in the O&M manual, not just in the switch |
| **Single cable / patch panel damage** | One camera. Trivial by comparison, and the most likely thing on this list to actually happen | Stream loss | Seconds | Labelling and a cable schedule so the fix takes minutes rather than an afternoon |
| **The IDF room itself** — locked, key lost, repurposed as storage, sprinkler above the rack | Everything in it | Nothing | Never, until needed | Access to the IDF in the key plan; **no sprinkler directly over the rack, or a drip shield**; annual walk of every IDF |

**The two rows worth arguing about in a design review** are *PoE budget exceeded* and *IDF
over-temperature*, because both are consequences of the same decision — filling a switch to 100%
— and both present as intermittent camera faults that will be chased at the camera end for
months. Neither is visible on a device schedule. Both are visible in one line of arithmetic.

---

## E7.3 — Emergent failures: nobody's component broke

For each: the failure, and **the interface where it originates**. In every case each subsystem
is behaving exactly as designed and specified.

### (a) Interlocked vestibule, fire alarm releases both doors, visitor inside

**The emergent failure:** the interlock's security function and the fire system's life-safety
function have opposite correct behaviours, and the fire system wins — correctly. During the
alarm, the vestibule is a **wide-open hole in the boundary**, in exactly the conditions where a
building is full of people moving and nobody is watching a screen.

**The interface:** the fire alarm relay to the access control system, and more fundamentally the
**boundary between two design disciplines** — the fire alarm engineer and the security engineer,
who each specified correct behaviour for their own system and never discussed the combination.

**Why it is emergent:** neither behaviour is wrong. Free egress during a fire alarm is
non-negotiable `[CODE][VERIFY]`. Interlocking a vestibule is standard anti-tailgating practice.
The failure exists only in the intersection.

**Mitigation:** accept the release (there is no alternative), and design for the *consequence* —
video coverage of the vestibule with alarm-triggered recording, a stated procedure for a
post-alarm sweep, and a documented recognition that the boundary is unavailable during alarms.
Also worth noting: the visitor *in* the vestibule is the life-safety case the release exists for.

### (b) IT blocks multicast; the VMS uses it for video walls

**The emergent failure:** the video wall stops working. Possibly worse — if the VMS falls back to
unicast, a single stream becomes N streams and the network load multiplies, which can degrade
recording for cameras that were fine.

**The interface:** the boundary between the **security system and the enterprise network**, and
organisationally the boundary between the security team and IT. The security system is a tenant
on somebody else's infrastructure and was not consulted about a policy change.

**Why it is emergent:** the multicast block is good network hygiene. The VMS's multicast use is
good design. Nobody did anything wrong.

**Mitigation:** this is why security systems belong on a documented VLAN with a written
agreement about what is permitted on it, and why the security team has to be on IT's change
advisory board. The technical fix is trivial once the conversation exists; the failure is that
the conversation did not.

### (c) HR sync is nightly; a terminated employee's badge works for up to 24 hours

**The emergent failure:** the single highest-risk access control event — termination — has a
latency of up to a day, in exactly the window when a terminated employee is most likely to act.

**The interface:** the **HR system to access control integration**, and specifically its
*schedule*. The integration works perfectly. It is just periodic.

**Why it is emergent:** nightly batch sync is normal, adequate for onboarding and role changes,
and cheap. It is only wrong for one event type, and that event type is the one that matters.

**Mitigation:** **immediate manual revocation as a documented step in the termination
procedure**, with the badge collected, plus an event-driven trigger for terminations rather than
waiting for the batch. Note that the procedural fix is free and the technical fix is not, and
that the procedural fix is the one that will still be needed even after the technical one is
built. Note also that mechanical keys have this same problem permanently and unfixably (module
`35_Doors_and_Hardware/08`).

### (d) Cameras on the generator; the recording server is not

**The emergent failure:** during a utility outage, every camera stays up and streams happily to
a server that is off. **The system appears healthy from the field and records nothing.**

**The interface:** the **electrical distribution design and the security system architecture** —
specifically, the branch circuit assignments, which are made by the electrical engineer from a
panel schedule that does not say which loads belong to the same functional chain.

**Why it is emergent:** the electrical engineer put cameras on standby because they were listed
as security loads. The server was in an IT room and was picked up on the IT panel schedule. Both
decisions are defensible in isolation.

**Why this one is the most instructive of the five:** it is a **whole-chain failure caused by
partial protection**. Protecting most of a chain and not all of it protects nothing, and the
partial protection actively hides the problem, because the parts you can see are working.

**Mitigation:** the security engineer must produce the list of *every* device in each functional
chain — cameras, switches, servers, storage, monitoring workstations, the network path, the
monitoring position's lighting — and hand it to the electrical engineer as a single power
requirement with a stated duration. Then verify it during commissioning by **actually killing
utility power** and watching what survives. That test finds this every time and nothing else
does.

### (e) A later HVAC duct is installed across three camera views; nobody tells security

**The emergent failure:** three cameras lose their coverage. The requirement they were traced to
silently stops being met. Everything reports healthy — the cameras are online, recording, and
correctly configured.

**The interface:** the boundary between the **original design and later fit-out work**, and
organisationally between the security team and whoever is managing tenant improvements. This is
a **lifecycle** interface rather than a technical one.

**Why it is emergent:** the HVAC contractor routed a duct in an available ceiling space, which
is their job. Nobody had told them a camera sightline was a protected asset.

**Mitigation:** camera sightlines belong in the **record documents as a coordination
constraint**, and any fit-out affecting the ceiling should trigger a security review. Practically,
the reliable mitigation is periodic **view verification** — someone looks at every camera image
against a reference screenshot quarterly. It is unglamorous, it takes an afternoon, and it is the
only thing that catches this class of failure at all.

> **What all five share:** every component met its specification, every discipline did its job,
> and the system failed at the seam. Interfaces are where the failures live, and they are the one
> thing no component-level review ever examines. This is the argument for design review as a
> distinct activity (module `33_Design_Review_QA`).

---

## E7.4 — Nine failure categories applied to the Project 1 door

> Project 1 is [`../../27_Labs/project_01_secure_one_door/BRIEF.md`](../../27_Labs/project_01_secure_one_door/BRIEF.md).
> Work it against your own design. Marking criteria below.

**The instruction says to produce at least two modes per category and warns that some will feel
forced. Do the forced ones.** They are the point of the exercise — a taxonomy's value is that it
makes you look where you would not have looked, and the forced categories are by definition the
ones you were not going to check.

### Marking criteria

| Criterion | What good looks like |
|---|---|
| **All nine categories populated** | Including the ones that feel absurd for a single door. If category 7 (malicious) has nothing, you have not thought about the door being attacked, which is the only reason it exists. |
| **Each mode has a "who detects it and how fast"** | This column is the exercise. A failure mode with no detection answer is an admission, and "never" is a legitimate and valuable entry. |
| **At least three modes detected by "nobody"** | If everything is detected, you are describing an ideal system rather than the one you designed. |
| **Category 9 is honest** | Category 9 is *your* failures. Wrong device for the environment, no degraded-mode consideration, unbuildable detail, coverage gap. A category 9 row that blames someone else is not a category 9 row. |
| **At least one mode is a maintenance mode** | Battery never replaced, closer never adjusted, never tested. Category 8 is the one that kills systems in year three. |
| **The fail state appears** | What the door does on power loss, on network loss, and on fire alarm — three different answers, all of which must be stated. |

### The rows most people miss

- **Category 5, configuration:** wrong shunt time. Set too short and you generate nuisance
  held-open alarms until an operator disables the alarm — at which point you have lost the
  detection function through a purely human mechanism. Detected by: alarm-volume statistics,
  weeks later, if anyone looks.
- **Category 6, human error:** the door is propped, for a legitimate reason, by someone whose job
  is harder because of your design. Detected by: a held-open alarm you may have just disabled.
  See E5.1's second worked finding.
- **Category 8, maintenance:** the door closer falls out of adjustment and the door no longer
  latches reliably. **The lock is fine. The deadlatch is fine. The door simply does not close.**
  Detected by: nobody, until a position switch shows a held-open pattern — and only if someone
  reads it.
- **Category 9, design:** the reader is on the wrong side, the REX covers the wrong area, the
  camera sees the door instead of the face, or the fail state was never explicitly decided and
  the contractor chose it.

---

## E7.5 🧮 — The analytics workload

### The arithmetic

```
   60 cameras × 8 alerts/day                =  480 alerts/day
   480 alerts × 90 s review                 =  43,200 s/day  =  12.0 operator-hours/day

   SOC staffing: 1 operator per shift, 3 shifts × 8 h  =  24 operator-hours/day

   Alert review as a fraction of staffed time  =  12.0 / 24.0  =  50%
   Per shift: 160 alerts × 90 s = 4.0 h of an 8-hour shift    =  50%
```

**The operator spends half of every shift reviewing analytics alerts.**

### Is the design viable? No — and the uniform assumption makes it look better than it is

The 50% figure assumes alerts arrive evenly across 24 hours. **They do not.** These are exterior
analytics; alerts cluster at night, when lighting is marginal, when animals are active, and when
weather moves vegetation. A realistic distribution makes the night shift far worse:

| Share of alerts on the night shift | Alerts | Review time | Fraction of an 8-hour shift |
|---|---|---|---|
| 33% (uniform) | 160 | 4.0 h | **50%** |
| 50% | 240 | 6.0 h | **75%** |
| 60% | 288 | 7.2 h | **90%** |
| 70% | 336 | 8.4 h | **105% — physically impossible** |

**At any plausible distribution the night operator cannot do the job**, and the night shift is
the one that matters.

And the real failure is not the arithmetic. It is what a human does when handed this workload:

1. Review time compresses. 90 seconds becomes 20, then becomes a glance.
2. Alerts are dismissed by pattern rather than by assessment — "that camera is always alerting."
3. The operator is *mid-alert* when a real event arrives, and everything else queues behind it.
4. **Effective probability of detection collapses**, while the system reports 100% availability
   and 480 alerts successfully processed per day.

This is exactly the mechanism from E3.1(b): a nuisance rate high enough to destroy the function
without breaking any component. The difference is that here it was **predictable at design time
with one multiplication**, and nobody did it.

There is also no slack for anything else. The operator's job is not only alerts — it is access
requests, intercom calls, escorting, radio, incident handling, and the reports. Fifty percent
committed means zero percent available.

### Three ways to fix it, and the recommendation

**Fix 1 — Reduce the alert rate at the source.** Target ≤ 20% of a shift on alert review:

```
   0.20 × 8 h × 3600 / 90 s  =  64 alerts/shift  =  192 alerts/day  =  3.2 per camera/day
```

**From 8 to about 3 alerts per camera per day — roughly a 60% reduction.** Achieved by tuning
detection zones and masking irrelevant areas, scheduling analytics by time of day, fixing the
*physical* causes (vegetation in frame, a swinging light, a reflective surface, inadequate or
uneven illumination), re-siting or re-aiming the worst cameras, and using object classification
rather than motion.

**Fix 2 — Reduce the time per alert with triage.** Not every alert needs 90 seconds. With
automatic video call-up showing pre- and post-event roll, most alerts are dismissible in seconds:

```
   80% dismissed at 15 s + 20% reviewed at 90 s
     = 480 × (0.8×15 + 0.2×90) s  =  14,400 s/day  =  4.0 operator-hours/day
     =  16.7% of staffed time
```

**Triage alone takes it from 50% to 16.7%** without reducing the alert count at all. This is
mostly a VMS configuration and SOP change.

**Fix 3 — Add operators.** 12 hours/day of review needs roughly 1.5 additional full-time
equivalents once breaks, leave, and other duties are accounted for. Straightforward, effective,
and by far the most expensive — and recurring, forever.

### Recommendation

**Fix 1 first, then Fix 2, and treat Fix 3 as the fallback if the other two do not land.**

Fix 1 is first because **it addresses the cause rather than the symptom**, and because a high
nuisance rate damages something the other two fixes cannot repair: operator trust. An operator
who has learned that alerts are noise will not respond properly to a real one no matter how fast
the triage interface is. Reducing the alert rate is also mostly free — tuning, masking, and
vegetation management — and it improves the system for everyone downstream, including
investigations.

Fix 2 is second because it is cheap, fast, and multiplies with Fix 1. Both together put the
workload comfortably under 10% of a shift with real margin for the night-shift clustering.

Fix 3 is last because adding staff to absorb a self-inflicted alert rate is paying forever for a
problem that could have been designed out — and because 1.5 FTE of SOC staffing, recurring,
usually exceeds the entire analytics licensing cost that created the problem.

**What to write in the report:** state the 50% figure, state the night-shift figure, and state
that the design is not viable as configured. Then give a **measurable acceptance criterion** —
"analytics shall be tuned such that alert volume does not exceed 3.5 per camera per day averaged
over any 7-day period, verified at 30 and 90 days post-occupancy" — because without a number in
the requirements this gets tuned once at handover and drifts back within a month.

---

## The thread through all five

E7.1 and E7.2 are enumeration: apply a taxonomy and find what you would not have looked for.
E7.3 is the harder skill — the failures that live in interfaces, where no component is faulty.
E7.4 forces the taxonomy onto something small enough that you cannot hide behind complexity.
E7.5 is the one that generalises furthest: **a design can fail on arithmetic nobody did.**

Sixty cameras, eight alerts, ninety seconds. Three numbers, one multiplication, and it says the
system will not work. That calculation costs nothing and it is not in any submittal, any device
schedule, or any drawing — which is precisely why the habit of asking "and then what does the
human do?" is worth more than most of the technical knowledge in this module.

> **Module 01 ends here.** Next: [`../../35_Doors_and_Hardware/`](../../35_Doors_and_Hardware/)
> for the opening in depth, [`../../32_Engineering_Math/`](../../32_Engineering_Math/) for the
> derivations behind every calculation used above, or
> [`../../27_Labs/project_01_secure_one_door/BRIEF.md`](../../27_Labs/project_01_secure_one_door/BRIEF.md)
> to apply all seven lessons to one door.
