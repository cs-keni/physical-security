# Vocabulary — Module 01 Foundations

**The full term list for the module, with precise definitions.**

This is a reference, not a lesson. The terms are defined where they are taught — this file
collects them so you can look one up without rereading, and so you can test yourself against a
list rather than against your memory of a list.

> **Precision here is not pedantry.** These words appear in contracts, in reports that inform
> spending decisions, and in the sentence a lawyer reads back to you after an incident. Using
> "threat" when you mean "vulnerability" is not a style error; it produces a design that
> addresses the wrong thing.

**How to use this:** cover the right column and work down. Any term you cannot state in one
sentence, go back to the lesson in the third column.

**Jump to:** [Risk](#risk-vocabulary-lesson-02) · [Functions](#the-functional-chain-lesson-03) ·
[Timely detection](#timely-detection-lesson-03) · [Zones](#defense-in-depth-and-zones-lesson-04)
· [CPTED](#cpted-lesson-05) · [Requirements](#requirements-engineering-lesson-06) ·
[Failure](#systems-and-failure-lesson-07)

---

## Risk vocabulary (lesson 02)

The chain these hang on: **asset → threat/hazard → vulnerability → undesired event →
consequence → (with likelihood) risk → countermeasure → residual risk → compared to tolerance.**

| Term | Definition | Where |
|---|---|---|
| **Asset** | Something of value, with an owner and a consequence of loss. People, property, information, reputation, and continuity of operations all qualify. If you cannot name the owner, you have not identified an asset. | [02](02_the_risk_vocabulary.md) |
| **Threat** | An actor with **intent and capability** to cause an undesired event. Both are required. A capable actor with no intent is not a threat to you; a motivated actor with no capability is not either. | [02](02_the_risk_vocabulary.md) |
| **Hazard** | A source of harm with **no intent** — flood, fire, earthquake, equipment failure. Cannot be deterred and does not adapt to your countermeasures, which is why the distinction has engineering consequences. | [02](02_the_risk_vocabulary.md) |
| **Vulnerability** | A weakness in protection that a **specific threat can actually exploit**. Always relative to a threat: a wall vulnerable to a vehicle is not vulnerable to a pedestrian. | [02](02_the_risk_vocabulary.md) |
| **Likelihood** | How probable an undesired event is. In security this is rarely actuarial — for deliberate acts it depends on adversary intent, which is unobservable. Treat stated likelihoods as judgements, not measurements. | [02](02_the_risk_vocabulary.md) |
| **Consequence / Impact** | The outcome if the event occurs: loss, injury, downtime, penalty, reputational harm. The one factor in the risk equation you can usually estimate honestly. | [02](02_the_risk_vocabulary.md) |
| **Risk** | A measure of the potential for loss, as a function of threat, vulnerability, and consequence: `R = f(T, V, C)`, often written `R = T × V × C`. **Use the structure; distrust the product** — three estimates each uncertain by an order of magnitude give an answer uncertain by three. | [02](02_the_risk_vocabulary.md) |
| **ALE / SLE / ARO** | Annualized Loss Expectancy = Single Loss Expectancy × Annual Rate of Occurrence. Useful with actuarial data (retail shrink, cargo theft); useless for events that have never occurred at a six-year-old facility. | [02](02_the_risk_vocabulary.md) |
| **Countermeasure / Control / Mitigation** | A measure that reduces risk by reducing **threat, vulnerability, or consequence**. The three targets are worth remembering — most designers only ever attack vulnerability. | [02](02_the_risk_vocabulary.md) |
| **Residual risk** | What remains after countermeasures. Never zero. **The owner accepts it, not you** — your obligation is to state it clearly enough that the acceptance is informed. | [02](02_the_risk_vocabulary.md) |
| **Risk tolerance / appetite** | How much residual risk the organization will knowingly bear. An organizational property, not a technical one, and the thing residual risk is compared against to answer "is this enough?" | [02](02_the_risk_vocabulary.md) |
| **Risk treatment** | The four options, exactly one per identified risk: **Avoid** (stop doing the thing), **Reduce/Mitigate** (countermeasures), **Transfer/Share** (insurance, contractual shift), **Accept** (bear it knowingly). | [02](02_the_risk_vocabulary.md) |
| **Transfer ≠ prevention** | Insurance moves the **financial consequence**, not the event. It does not prevent the fire, restore the data, or return your reputation. Clients confuse this constantly. | [02](02_the_risk_vocabulary.md) |
| **Effectiveness** | Does the countermeasure work? | [02](02_the_risk_vocabulary.md) |
| **Assurance** | **How confident are we that it works, and how do we know?** An untested system has unknown effectiveness and *zero* assurance. This distinction is the entire justification for commissioning. | [02](02_the_risk_vocabulary.md) |

---

## The functional chain (lesson 03)

Six functions. Countermeasures are classified by which one they perform, because a device
schedule cannot show a missing function and a function table can.

| Term | Definition | Where |
|---|---|---|
| **Deter** | Influence the adversary not to attempt. Unmeasurable, works only on the deterrable, and routinely over-credited. | [03](03_functional_chain.md) |
| **Detect** | Determine that an undesired act is occurring. **Three parts, all required: sensor activation → signal transmission → annunciation to a human or system.** Break any one and there is no detection. | [03](03_functional_chain.md) |
| **Assess** | Determine what actually caused the detection. Without it you have an alarm, not information — and no basis for dispatching a response. The most commonly absent function. | [03](03_functional_chain.md) |
| **Delay** | Increase the time required to reach the asset. **Only the delay occurring after the detection point counts.** | [03](03_functional_chain.md) |
| **Respond** | Interrupt and neutralize. Usually the most expensive function, which is why the industry sells the other five. | [03](03_functional_chain.md) |
| **Recover** | Restore operations and capture the learning: evidence retention, investigation, spares, procedures, insurance claim. | [03](03_functional_chain.md) |
| **Probability of detection (P_D)** | The chance a sensor detects the intrusion given it occurs, for a **stated adversary and method**. Never 1.0; any datasheet implying otherwise is marketing. | [03](03_functional_chain.md) |
| **Nuisance alarm** | An alarm from a real stimulus that is not an intrusion — wind, animals, vegetation. Distinct from a false alarm (no stimulus at all). | [03](03_functional_chain.md) |
| **Effective P_D** | What detection probability becomes after operators learn to ignore the sensor. A high nuisance rate drives effective P_D toward zero **while every component keeps working perfectly.** | [03](03_functional_chain.md) |
| **Supervision** | The system detecting its own failure to detect — end-of-line resistors, heartbeats, comm-loss alarms, tamper. Without it, a dead sensor and a quiet sensor look identical. | [03](03_functional_chain.md) |

### Timely detection (lesson 03)

The most important calculation in the discipline.

| Symbol | Meaning |
|---|---|
| `T_T` | **Total task time** — start of the adversary sequence to completing the act at the asset |
| `T_D` | Time from the start of the sequence to **detection *plus* assessment** |
| `T_A` | Adversary time **remaining** after detection = `T_T − T_D` |
| `T_R` | **Response force time** — annunciation to interruption |

```
   The system is timely if and only if      T_A  >  T_R
                                       (T_T − T_D)  >  T_R
```

| Term | Definition |
|---|---|
| **Timely detection margin** | `T_A − T_R`. Design for a positive margin **with headroom**, because every input is an estimate. |
| **Required detection point** | `T_D_max = T_T − T_R − margin`. The latest detection can occur and still be timely. Walk the path, find which task the adversary is executing at that instant, and place detection at or before it. **This is how a detection layer gets located by calculation rather than by habit.** |
| **Marginal** | A positive margin that is below the required confidence margin. Treated as **not timely** — landing exactly on your allowance for being wrong means you have none left. |
| **The four levers** | When a path is not timely: detect earlier, add delay **after** the detection point, reduce response time, or **reduce the consequence**. The fourth is not a term in the inequality, which is why nobody proposes it and why it is often cheapest. |

> Implemented in [`../28_Calculators/psec/pps.py`](../28_Calculators/psec/pps.py); derived in
> [`../32_Engineering_Math/08_adversary_path.md`](../32_Engineering_Math/08_adversary_path.md).

---

## Defense in depth and zones (lesson 04)

| Term | Definition | Where |
|---|---|---|
| **Defense in depth** | Multiple layers that are **independent, sequential, and each individually meaningful**. Three locks on one door is not depth; it is one layer bought three times. | [04](04_defense_in_depth_and_zones.md) |
| **Security zone** | A **volume** with a defined boundary and a defined control at every crossing of it. Zones are spaces, not devices. | [04](04_defense_in_depth_and_zones.md) |
| **Zone integrity** | The rule people break constantly: **a boundary must be continuous in three dimensions** — walls, doors, windows, floor, ceiling, and every penetration. The boundary is the entire enclosing surface, not the door. | [04](04_defense_in_depth_and_zones.md) |
| **The nine integrity elements** | Walls · Ceiling · Floor · Doors · Windows · Penetrations · Roof · Adjacencies · Egress hardware. | [04](04_defense_in_depth_and_zones.md) |
| **Balanced protection** | Every path to the asset should offer comparable resistance. **The stopping rule: stop strengthening a path when it is no longer the weakest one.** The canonical violation is a $3,000 door in a wall that stops at the ceiling grid. | [04](04_defense_in_depth_and_zones.md) |
| **Redundancy** | A second **identical** thing. Protects against random failure of that thing; does not protect against the common cause that takes both. | [04](04_defense_in_depth_and_zones.md) |
| **Diversity** | A second **different** thing achieving the same function. **Better against a thinking adversary and against common-cause failure**, because it fails for different reasons. | [04](04_defense_in_depth_and_zones.md) |
| **Graceful degradation** | The system loses capability progressively rather than totally. **Must be specified at design time** — it never emerges by accident. | [04](04_defense_in_depth_and_zones.md) |
| **Single point of failure (SPOF)** | Any element whose failure takes down a whole function. Includes the unglamorous ones: a room, a UPS, a software licence, a certificate, one administrator. | [04](04_defense_in_depth_and_zones.md) |

---

## CPTED (lesson 05)

**Crime Prevention Through Environmental Design** — influencing behaviour through the design of
the physical environment. The cheapest tool in the discipline and the one most often dismissed.

| Strategy | Mechanism | Where |
|---|---|---|
| **Natural surveillance** | See and be seen. Offenders avoid places where they are likely to be observed. Sightlines, glazing, lighting, and the position of occupied spaces. | [05](05_cpted.md) |
| **Natural access control** | Guide people where you want them using layout, planting, level changes, and entrance hierarchy — before resorting to locks. | [05](05_cpted.md) |
| **Territorial reinforcement** | Signal ownership. Clear transitions and evident care tell a stranger that this space belongs to someone who is paying attention. | [05](05_cpted.md) |
| **Maintenance / image** | The broken-windows effect. Visible disrepair signals that nobody is watching, and it compounds. | [05](05_cpted.md) |
| **Activity support** | Put legitimate activity into vulnerable places. Informal guardianship by ordinary users is more effective than surveillance of an empty space. | [05](05_cpted.md) |
| **Target hardening** | Locks, bars, barriers. **Listed last deliberately** — it is the last resort, not the first move, and it carries the fortress-effect cost. | [05](05_cpted.md) |

| Term | Definition |
|---|---|
| **The 3-foot/6-foot rule** | Keep shrubs below 3 ft and tree canopies above 6 ft, so the sightline between them stays open. Serves natural surveillance. |
| **Uniformity vs. brightness** | Uniformity matters more. The eye adapts to the brightest thing in view, so a bright light beside a dark zone is worse than moderate even light — it manufactures the shadow it hides someone in. |
| **The convenience door problem** | A door propped because the access concept is fighting the shortest legitimate path. **A design problem, not a discipline problem**, and a door alarm does not fix it. |
| **The fortress effect** | Visible hardening that signals danger, reduces legitimate use, and thereby removes the informal guardianship that was protecting the place. |
| **A fundable finding** | Location, affected users, mechanism, and a costed recommendation. "Lighting is poor in the east lot" is not a finding. |

---

## Requirements engineering (lesson 06)

| Term | Definition | Where |
|---|---|---|
| **Functional requirement** | What the system must **do**. | [06](06_requirements_engineering.md) |
| **Performance requirement** | **How well** it must do it. Measurable, with units, a value, a condition, and a measurement method. | [06](06_requirements_engineering.md) |
| **Operational requirement** | How it must fit **the way people actually work**. The most commonly omitted type, and the one whose absence produces propped doors. | [06](06_requirements_engineering.md) |
| **Constraint** | What **limits** the solution: code, budget, existing infrastructure, landlord, corporate standard. | [06](06_requirements_engineering.md) |
| **"Shall"** | Mandatory. Not *should* (recommendation), not *will* (statement of fact), not *may* (permission). Universal in specification writing, and violating it creates contractual ambiguity. | [06](06_requirements_engineering.md) |
| **RTM** | **Requirements Traceability Matrix.** Req ID → traces-from → design element → drawing → spec section → test procedure → status. Answers "why is this here?" for every device on every drawing. | [06](06_requirements_engineering.md) |
| **Requirement vs. specification** | A requirement states **what must be achieved**; a specification states **one acceptable way** to achieve it. Keep them separate, because the product will be discontinued mid-project. | [06](06_requirements_engineering.md) |
| **Basis of design** | The named product that sets the quality level, stated *alongside* the requirement rather than in place of it. | [06](06_requirements_engineering.md) |

### The four requirement pathologies

| Pathology | Shape | Fix |
|---|---|---|
| **Solution masquerading as a requirement** | "We need a mantrap." | Ask what it would accomplish; write *that*; evaluate their idea as one candidate. |
| **Inherited requirement** | "It's in our corporate standard." | Ask what it is for. If it does not fit, raise a **documented deviation request** — never silently comply, never silently ignore. |
| **Unfalsifiable requirement** | "Comprehensive security." | If you cannot write a test, it is not a requirement. Delete it or make it testable. |
| **Orphan requirement** | Traces to no risk and no driver. | Either a missing traceability link (fix it) or unnecessary scope (delete it and save the money). |

---

## Systems and failure (lesson 07)

| Term | Definition | Where |
|---|---|---|
| **Functional chain** | The full sequence from physical stimulus to human response. **A chain fails at its weakest link, and most reviews examine only the components.** | [07](07_systems_and_failure_thinking.md) |
| **Informal FMEA** | Lightweight Failure Modes and Effects Analysis: for each component, list failure modes, effect, **detection method and time to detect**, and mitigation. About an hour per subsystem. | [07](07_systems_and_failure_thinking.md) |
| **Silent failure** | A failure the system does not report. The "time to detect" column reading *never*. The reason assurance requires testing rather than monitoring. | [07](07_systems_and_failure_thinking.md) |
| **Emergent failure** | The system fails while **no component is faulty**. Originates at an interface — between subsystems, between disciplines, or between the design and later work. | [07](07_systems_and_failure_thinking.md) |

### The nine failure categories

Structured so you cannot skip one by accident.

| # | Category | Ask |
|---|---|---|
| 1 | **Component** | What if this device dies? Degrades? Fails intermittently? |
| 2 | **Communication** | Network, bus, fiber, cellular backup. For how long is loss tolerable? |
| 3 | **Power** | Utility, UPS depletion, generator, breaker, fuse, voltage drop on a long run |
| 4 | **Software** | Crash, database corruption, licence expiry, failed update, **certificate expiry** |
| 5 | **Configuration** | Wrong schedule, access level, VLAN, shunt time, timezone, default password |
| 6 | **Human error** | Wrong button, propped door, badge lent, alarm acknowledged without looking |
| 7 | **Malicious** | Tamper, bypass, credential compromise, insider misuse, evidence tampering |
| 8 | **Maintenance** | Not tested, not cleaned, not calibrated, battery never replaced, spares unobtainable |
| 9 | **Design** | Wrong device for the environment, coverage gap, unbuildable detail, no degraded-mode consideration |

> **Category 9 is yours.** The other eight happen to your design; this one **is** your design.
> It is also the hardest to see from inside, which is why design review exists as a separate
> activity.

---

## Terms that are routinely confused

The disambiguation drill. If you can do this table cold, the vocabulary has landed.

| These get confused | The distinction that matters |
|---|---|
| Threat vs. hazard | **Intent.** A threat adapts to your design and can be deterred; a hazard does neither, hits everything at once, and is actuarially tractable. |
| Threat vs. vulnerability | A threat is an **actor**; a vulnerability is a **weakness**. A demonstrated threat with no vulnerability is no risk — and vice versa. |
| Vulnerability vs. risk | A vulnerability is one **factor**. Risk needs a consequence and a likelihood too. |
| Detect vs. assess | Detection says *something happened*. Assessment says *what*. Only the second justifies a dispatch. |
| Delay vs. delay-after-detection | Only the second is in the inequality. **Delay added before the detection point buys nothing.** |
| Redundancy vs. diversity | Identical vs. different. Only diversity survives a common cause or a thinking adversary. |
| Effectiveness vs. assurance | Does it work, vs. how do you know. Testing provides the second, and nothing else does. |
| Requirement vs. specification | What must be achieved vs. one acceptable way to achieve it. |
| Peak vs. average | Links are sized on peak; storage on average. Reversing them is a design failure in both directions. |
| Nuisance vs. false alarm | Nuisance: a real stimulus that is not an intrusion. False: no stimulus at all. Different fixes. |

---

## Where the terms go next

| Term family | Deepened in |
|---|---|
| Timely detection, adversary path | [`../32_Engineering_Math/08_adversary_path.md`](../32_Engineering_Math/08_adversary_path.md) · [`../02_Risk_Assessment/`](../02_Risk_Assessment/) |
| Pixel density, PPF, DORI | [`../32_Engineering_Math/02_pixel_density.md`](../32_Engineering_Math/02_pixel_density.md) · [`../03_Video_Surveillance/`](../03_Video_Surveillance/) |
| Zone integrity at an opening | [`../35_Doors_and_Hardware/01_door_anatomy.md`](../35_Doors_and_Hardware/01_door_anatomy.md) |
| Fail safe / fail secure | [`../35_Doors_and_Hardware/04_fail_safe_vs_fail_secure.md`](../35_Doors_and_Hardware/04_fail_safe_vs_fail_secure.md) |
| Supervision, offline behaviour | [`../04_Access_Control/`](../04_Access_Control/) |
| Assurance and testing | [`../18_Commissioning/`](../18_Commissioning/) |
| RTM and specification writing | [`../11_Division_28/`](../11_Division_28/) · [`../17_Construction_Documents/`](../17_Construction_Documents/) |
| Tag discipline and `[VERIFY]` | [`../31_References/source_index.md`](../31_References/source_index.md) |

> Cards for this vocabulary: [`../26_Flashcards/01_foundations.csv`](../26_Flashcards/01_foundations.csv).
