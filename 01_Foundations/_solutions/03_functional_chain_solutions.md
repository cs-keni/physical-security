# Solutions — 03, The Functional Chain

> For the exercises in [`../03_functional_chain.md`](../03_functional_chain.md).
> **Write your answers first.**

> **E3.2's numbers were computed by running
> [`../../28_Calculators/psec/pps.py`](../../28_Calculators/psec/pps.py)**, not by hand.
> The derivation behind that module is
> [`../../32_Engineering_Math/08_adversary_path.md`](../../32_Engineering_Math/08_adversary_path.md).
> If your hand calculation disagrees with a figure here, find out which of you is wrong.

---

## E3.1 — Which function is missing?

The exercise is designed so that each case is missing exactly one function, and the consequence
in each case is that **the other five stop paying off**. That is the whole argument of the
lesson: the functions are a chain, not a menu.

### (a) A gate with a card reader, a strike, and no door position switch

**Missing: DETECT.**

There is access *control* and no access *monitoring*. The system knows about valid credential
presentations and nothing else. Specifically it cannot tell you:

- that the gate was forced
- that the gate was propped or left standing open
- that someone followed a valid user through
- that the gate opened with no credential at all

**The consequence:** the only events in the log are the legitimate ones. **The log is a record
of compliance, not of security**, and it will be produced after an incident as proof that
nothing happened. A door with a reader and no position switch is arguably worse than no
system, because it manufactures confidence.

Cheap fix, and it should be on every controlled opening as a default: a door position switch,
plus forced-door and held-open alarms with the shunt time actually verified in commissioning
(lesson 07's FMEA finds this one).

### (b) 40 perimeter fence sensors, no exterior cameras, response by police dispatch

**Missing: ASSESS.**

Detection without assessment is not detection in any useful sense — the lesson's three-part
definition of a detection event (sensor activation, signal transmission, **and assessment**) is
not satisfied. Nobody can determine what caused any of the 40 sensors to alarm.

**The consequence is a cascade, and it is worth tracing in full:**

1. Fence sensors have high nuisance alarm rates — wind, animals, vegetation, vehicles, ice.
2. Every alarm requires a dispatch, because nothing can distinguish them.
3. Police response degrades to low priority, then to no response.
4. Operators begin acknowledging alarms without action.
5. **Effective probability of detection collapses toward zero** while the sensors keep working
   perfectly and the system keeps reporting 100% availability.

This is the lesson's point that a high nuisance rate destroys effective `P_D`. The sensors are
not broken. The *function* is broken.

Fix: exterior cameras with automatic call-up on alarm, sited and illuminated for assessment
rather than for evidence. Also revisit the sensor technology and the vegetation management,
because assessment capability lets you finally *measure* the nuisance rate instead of guessing.

### (c) Monitored intrusion, 30 minutes of guard response, a safe rated for 5 minutes of attack

**Missing: DELAY** — or, stated more precisely, **the timeliness inequality fails.**

```
   T_A (delay after detection) ≈ 300 s   vs   T_R = 1800 s
   Deficit ≈ 1500 s
```

Detection works. Response exists. **They are simply not connected in time.** The adversary
finishes the job with twenty-five minutes to spare and leaves before anyone arrives.

**The consequence:** the system documents the loss. Every component performs to specification,
the incident report is complete, and the asset is gone. This is the archetypal "everything
worked and we lost anyway" design, and it is more common than any of the outright failures.

Note that the fix is not necessarily a better safe. A UL-rated attack time is quoted against a
specified tool set for a specified duration `[STANDARD][VERIFY rating and test basis]`, and
buying from a 5-minute to a 30-minute rating is expensive. The four levers are all available
here, and the delay lever is usually the worst-value one.

### (d) A server room with badge access, cameras, and a suspended-ceiling wall

**Missing: DELAY, via a zone-integrity failure** — the boundary is not continuous in three
dimensions (lesson 04).

The controls are all on the door. The wall stops at the ceiling grid and the plenum runs
continuously to the corridor. **Total delay via the ceiling: on the order of forty seconds, and
it generates no event**, because the door contact never changes state and the camera is pointed
at the door.

**The consequence:** you have specified a $3,000 door on a $0 wall — the lesson's canonical
balanced-protection violation. Worse, the *detection* is also defeated, because everything that
detects is attached to the path that is no longer being used.

This is the case where the correct finding costs almost nothing: extend the partition slab to
slab, or install a physical barrier in the plenum, and the whole rest of the design starts
working. It is also the finding that is impossible to make after the ceiling is closed, which
is why lesson 04 insists on the zone-integrity checklist during design.

### (e) A campus with excellent cameras, retained 3 days, incidents discovered weekly

**Missing: RECOVER** — specifically the evidence-retention part of it.

Every other function may be performing. But if the detection latency of the *organization* is
seven days and the retention is three, then **at the moment anyone goes looking, the footage
does not exist.** The system is, in practice, a very expensive live-view display.

**The consequence:** no investigation is possible, no learning is captured, no pattern is
detected across incidents, and no prosecution is supported. The client will conclude that the
cameras are useless, and they will be right — for reasons that have nothing to do with the
cameras.

Fix, in order of value: (1) find out **why** discovery takes a week and shorten it, because
that is the real defect; (2) extend retention past the discovery interval with margin —
retention must exceed the time to *discover*, not the time to *respond*; (3) verify the actual
retention rather than the configured one, because storage over-subscription silently shortens
it (module `32_Engineering_Math/04_storage.md`).

> **The pattern across all five.** Every case has substantial working equipment and one absent
> function, and in every case the absent function makes the rest of the spend worthless. This
> is why the lesson insists you classify countermeasures by function rather than by product
> category: a device schedule cannot show you a missing function, and a function table can.

---

## E3.2 🧮 — The distribution center

### Given

| Task | Delay | Cumulative |
|---|---|---|
| Fence | 20 s | 20 s |
| Yard | 40 s | 60 s |
| Dock door | 150 s | **210 s ← detection here** |
| Floor traverse | 60 s | 270 s |
| Cage | 200 s | 470 s |
| Load | 240 s | **710 s** |

Assessment delay: 20 s.

### (a) On-site guard, `T_R = 300 s`

```
   T_T  =  20 + 40 + 150 + 60 + 200 + 240        =  710 s
   T_D  =  210 (dock door complete) + 20 (assess) =  230 s
   T_A  =  710 − 230                              =  480 s

   margin  =  T_A − T_R  =  480 − 300             =  +180 s
```

**TIMELY. 180 s of margin.**

Note what is doing the work: 440 of the 710 seconds of task time sit *after* the detection
point, and the cage plus the loading time — the two slowest tasks — are both after it. The
design is timely because the detection layer happens to be positioned early relative to the
expensive delay, which is what a working design looks like.

Worth stating in a report: with a 60 s confidence margin required, this still passes (180 > 60).
With a 200 s margin it would not. **Whether it is timely depends on how much you trust your own
task-time estimates**, and the honest way to express that is a required margin, not a point
value.

### (b) Contract patrol, `T_R = 1800 s`

```
   T_A  =  480 s      (unchanged — nothing about the path moved)
   T_R  =  1800 s

   margin  =  480 − 1800  =  −1320 s
```

**NOT TIMELY. Short by 1320 s (22 minutes).**

One procurement decision — replacing an on-site guard with a contract patrol — moved a design
from 180 s of margin to a 1320 s deficit. **No hardware changed.** No drawing changed. Nothing
in the security system got worse.

This is the single most important thing in the exercise. `T_R` is usually the **largest term in
the inequality**, it is usually decided by someone who has never seen your calculation, and it
is usually decided on operating cost. If you do not put this arithmetic in front of the owner
*before* they make the decision, you will be asked to fix it afterward with hardware, at
several times the cost.

**Now compute the required detection point:**

```
   T_D_max  =  T_T − T_R − margin  =  710 − 1800 − 0  =  −1090 s
```

**Negative.** `compare_interventions` returns:

> `NOT ACHIEVABLE on this path. Timeliness would require detection at t <= -1090 s, i.e.
> before the adversary sequence begins. Even instantaneous detection at the property line
> leaves only 710 s against a 1800 s response. Detection alone cannot fix this -- go to the
> response or consequence lever.`

Read that carefully, because it is the most useful result in the exercise. **The detection lever
is not expensive here — it is exhausted.** Even a sensor that fires the instant the adversary
touches the fence, with zero assessment delay, leaves 710 s against an 1800 s response. You
could spend the entire security budget on detection and not move the verdict.

A calculator that returned "move detection 1320 s earlier" would be arithmetically correct and
would send someone shopping for perimeter sensors that cannot help.

### (c) Three interventions, and a recommendation

**Deficit to close: 1320 s.**

**Intervention 1 — change DETECTION.** *Not viable on this path, and that is the finding.*

The only version of this lever that does anything is detecting the adversary **before task 1
begins** — approach detection outside the fence line, video analytics on the approach road, or
intelligence-based warning. Even then you are buying seconds against a 22-minute deficit. Report
this as **not achievable**, with the arithmetic, so nobody spends money discovering it.

**Intervention 2 — change DELAY.** Add ≥ 1320 s *after* the detection point.

Concretely: harden the cage from 200 s to something on the order of 1500 s — a
substantial construction change, likely CMU or a certified enclosure — or add an inner barrier
between the floor traverse and the cage.

Two cautions. First, **delay added before the detection point buys nothing**; fence upgrades and
a better dock door increase `T_T` and `T_D` by the same amount and leave `T_A` untouched. This is
the most commonly wasted money in this whole model. Second, the cost curve for delay is steep
and it is capital — going from 200 s to 1500 s is not seven times the price of the original
cage, it is a different kind of construction.

**Intervention 3 — change CONSEQUENCE.** Reduce what is reachable.

Concretely: reduce on-hand high-value inventory through more frequent, smaller deliveries;
move the highest-value SKUs into a certified safe inside the cage (which also adds delay, so it
plays both levers); or relocate the high-value line to a facility that has response.

**What I would recommend, and why.**

**Reduce the consequence first, then re-run the analysis.** It is almost certainly the cheapest
option on this list, it is the only one that still helps *after* the system fails, and it
converts the meeting from "which product do we buy" into "how much loss are we buying down."

But the recommendation that matters is the one about `T_R`. **The honest report says that the
patrol decision created this problem and that reversing it fixes it completely for less than the
capital cost of the delay option.** Run the numbers both ways and put them side by side:

```
   Contract patrol      T_R = 1800 s   →  deficit 1320 s, plus ~$X of cage hardening
   On-site guard        T_R =  300 s   →  timely, 180 s margin, no capital
```

That is not a security-system recommendation and the owner may still choose the patrol for
sound business reasons. **Your job is to make sure they choose it knowing what it costs**, not
to solve with hardware a problem that was created by an operating budget. Lesson 01's framing —
you inform decisions, you do not make them — is exactly this.

> If they hold the patrol decision *and* will not fund the cage: say so plainly, in writing,
> and recommend the consequence lever. A design that cannot be timely should be documented as
> a **detection-and-documentation system**, so nobody believes it will interrupt anything.

---

## E3.3 — Mapping your field-exercise building onto the six functions

There is no single right answer; there is a right *shape*. Use this table format, and fill the
"who/what/how fast" column honestly — that column is where the exercise does its work.

| Function | Measures present | Actually performing? | Weakness |
|---|---|---|---|
| **Deter** | Signage, visible cameras, lighting, staffed reception, fencing | Deterrence is unmeasurable and works only on the deterrable. Do not credit it heavily. | Typically over-credited |
| **Detect** | Door contacts, motion, glassbreak, staffed observation, alarm monitoring | **Detect *what*, and does the signal reach a human who acts?** | Usually the weak one |
| **Assess** | Cameras with call-up, sightlines, staffed position | Can someone determine the cause **within seconds**, or must they walk there? | Usually absent as a designed capability |
| **Delay** | Walls, doors, locks, glazing, distance, barriers | Measured **after** the detection point only | Usually over-invested |
| **Respond** | Guard, police, key holder, procedure | **Time, in seconds, measured not quoted.** Who, from where, and at 3 a.m.? | Usually unmeasured |
| **Recover** | Video retention, backups, spares, procedures, insurance | Does retention exceed the *discovery* interval? | Usually forgotten |

**In most ordinary buildings the weakest function is ASSESS, followed closely by RESPOND**, and
the most over-invested is DELAY. If your table says otherwise, check it — that is a real
finding, not a mistake.

**The cheapest high-value intervention is almost always one of these three**, none of which is a
product:

1. **Automatic camera call-up on alarm.** Usually a configuration change in a system that is
   already installed. It converts existing detection into detection-plus-assessment, which is
   the difference between an alarm and information.
2. **Measuring the actual response time** with an unannounced test at 3 a.m. on a Sunday. Free.
   Frequently reveals that the design basis is fiction.
3. **Extending video retention past the discovery interval.** Cheap relative to any hardware,
   and it is the one that determines whether an investigation is possible at all.

Write your answer with a cost against the recommendation. A finding without a cost is an
opinion (lesson 05).

---

## E3.4 — Explain it in under 100 words, no jargon

> Locks buy time. Time only helps if somebody is coming, and right now nobody is watching that
> room and the nearest guard is twenty-five minutes away. A better lock might take someone four
> minutes to beat instead of one. They still have twenty-one minutes alone in the room, and
> we'd never know they were there. Spend the money on knowing — a sensor on the door and a
> camera that pops up on a screen when it opens. Then the lock's minutes start being worth
> something.
>
> *(93 words)*

**What that answer is doing, and what to check yours against:**

- **It never says "delay," "detection," "timely," or "T_R."** The jargon constraint is not
  decoration. Clients who are handed vocabulary stop listening; clients who are handed
  arithmetic they can check start participating.
- **It uses their numbers.** Twenty-five minutes is *their* fact, so the conclusion is theirs
  too. This is far more persuasive than any framework.
- **It does not say the lock is worthless.** It says the lock's value is *contingent*, and it
  names the condition. Telling a facilities director their existing spend was wasted is both
  unhelpful and usually inaccurate.
- **It ends with a specific, cheap thing to do next.** "Reprioritize toward detection" is not a
  deliverable. "A door sensor and a camera that pops up on a screen" is.
- **It is honest about what the fix does.** It does not promise the intrusion is prevented. It
  promises you will know.

Common failure modes in answers to this one: explaining the model instead of the situation;
using "delay" and thinking it counts as plain English because it is a short word; and
recommending a guard, which is the correct engineering answer and is not available for the
budget implied by the question.

---

## Where these answers came from

E3.2 was computed with:

```python
from psec import pps
p = pps.AdversaryPath(name="Distribution center", assessment_delay_s=20.0)
for name, delay, det in [("Fence", 20, False), ("Yard", 40, False),
                         ("Dock door", 150, True), ("Floor traverse", 60, False),
                         ("Cage", 200, False), ("Load", 240, False)]:
    p.add(pps.Task(name, float(delay), detected_here=det))

p.evaluate(300.0)                    # timely, +180 s
p.evaluate(1800.0)                   # not timely, short by 1320 s
p.required_detection_point_s(1800.0) # -1090 s  →  NOT ACHIEVABLE
pps.compare_interventions(p, 1800.0)
```

The derivation of every one of those formulas is
[`../../32_Engineering_Math/08_adversary_path.md`](../../32_Engineering_Math/08_adversary_path.md).
Do the arithmetic by hand before you trust the module — that is the entire argument for module
32 existing.

> Next: [`04_defense_in_depth_and_zones.md`](../04_defense_in_depth_and_zones.md) — where the
> "$3,000 door on a $0 wall" from E3.1(d) becomes a checklist you run on every boundary.
