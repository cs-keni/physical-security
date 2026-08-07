# 03 — The Functional Chain: Deter, Detect, Delay, Assess, Respond, Recover

## Learning objectives

- Name the six protection functions and state what each one does that the others cannot.
- Explain why detection *without* assessment is nearly worthless, and why delay *without*
  response is entirely worthless.
- Apply the **Timely Detection** principle: detection must occur early enough that remaining
  delay exceeds response time.
- Compute whether a protection system is timely, given delay and response times.
- Classify any countermeasure by the function(s) it actually performs — including catching
  the common case where a device performs a different function than people assume.

---

## ELI5

Six jobs, in order, like a relay race:

1. **Deter** — make them not want to try. (A big fence and a bright light.)
2. **Detect** — know that someone *is* trying. (An alarm goes off.)
3. **Assess** — find out whether it's a burglar or a raccoon. (Look at the camera.)
4. **Delay** — slow them down while help is coming. (Locked doors, more locked doors.)
5. **Respond** — someone shows up and does something about it.
6. **Recover** — clean up, fix it, learn, and get back to normal.

The trick: **detecting late is the same as not detecting.** If the alarm goes off when the
thief is already walking out the door, you have a very expensive recording of a crime.

---

## The six functions

You will see this called **D3ACR**, or the **Deter–Detect–Delay–Respond** model, or
**PPS** (Physical Protection System) functions of *detect, delay, respond*. The variations
are real but shallow. Here is the complete set with the boundaries that matter.

### 1. Deter — influence the adversary not to attempt

**Mechanism:** the adversary perceives that the attempt will fail, or will be detected, or
that the cost/risk exceeds the reward.

**Critical property: deterrence acts on *perception*, not reality.** A dummy camera deters
exactly as well as a real camera *until the adversary learns it's fake* — after which it
deters worse than nothing, because it has taught them your deterrents are theater.

**Examples:** visible cameras, lighting, signage, fencing, visible guards, active voice
talk-down, well-maintained appearance (see CPTED, lesson 05), reputation.

**Why you cannot design *for* deterrence alone:**
- It is unmeasurable. You cannot count the crimes that didn't happen. Any vendor claiming a
  measured deterrence percentage is selling you something.
- It **does not work on all adversaries.** The determined, the impaired, the ideologically
  motivated, and the insider are all substantially undeterred. Deterrence filters out the
  casual attempt — which is genuinely valuable, since most attempts are casual — but it is
  the layer you must assume fails.
- It can **displace rather than reduce**: the adversary goes to a softer target next door.
  Good for your client, neutral for society. Say this honestly if asked.

> ⚠️ **The deterrence trap:** owners love deterrence because it's cheap and visible. "We put
> up signs and cameras and haven't had an incident since" is a claim with no control group.
> Never let a deterrence argument substitute for detection and response capability.

### 2. Detect — determine that an undesired act is occurring

**A detection event has three parts, and all three must happen:**

```
   SENSOR ACTIVATION  →  SIGNAL TRANSMISSION  →  ANNUNCIATION TO A HUMAN/SYSTEM
   (something trips)     (it gets there)          (someone is actually informed)
```

Break any one and there is no detection. A sensor that trips into an unmonitored panel has
not detected anything. This is why **supervision** (module `04_Access_Control/05`) exists:
the system must detect its own failure to detect.

**Measured by:**
- **Probability of Detection (Pd)** — the chance the sensor detects the intrusion given it
  occurs, for a stated adversary and method. Usually expressed 0–1 or as a percentage. It is
  *never* 1.0 and any datasheet implying otherwise is marketing.
- **Nuisance Alarm Rate (NAR)** — alarms from real, non-threat stimuli (wind, animals, rain,
  a flag). The alarm is *correct*; the cause is benign.
- **False Alarm Rate (FAR)** — alarms with no external cause (equipment fault, noise). In
  practice the industry uses "false alarm" for both; the distinction matters when
  troubleshooting because the fixes differ entirely.
- **Vulnerability to defeat** — how hard is it for a knowledgeable adversary to bypass?
  (Bridging, masking, crawling under, going slowly, going quickly.)

**The Pd/NAR tradeoff is the central tension in detection engineering.** Turn sensitivity up
and Pd rises — and so does NAR. Turn it down and nuisance alarms fall — and so does Pd.
There is no setting that maximizes both. The resolution is *not* to find a magic setting; it
is to use **complementary sensors** whose nuisance sources differ (dual-technology sensors
are exactly this idea), and to design the environment so nuisance sources are removed.

> 🧠 **The operational truth juniors miss:** a system with a high nuisance alarm rate has an
> *effective* Pd approaching zero, because the operator stops believing it. Alarm fatigue is
> not a human weakness to be trained away; it is a rational response to a system that lies.
> **A design that generates alarms nobody believes is a failed design**, regardless of
> its datasheet Pd.

### 3. Assess — determine what actually caused the detection

**This is the function most often missing from bad designs, and its absence is invisible on a
device count.**

Detection tells you *something happened*. Assessment tells you *what*, so you can decide
whether and how to respond. Without assessment:
- Every alarm requires a physical response (expensive, slow, and it desensitizes the guard)
- Or every alarm is ignored (which is what actually happens)

**Assessment is usually performed by video** — a camera whose view is *causally linked* to
the alarm point and which is *automatically presented* to the operator when the alarm occurs.

Three requirements for a camera to actually perform assessment, all frequently violated:

1. **It must cover the detection zone.** Obvious; still missed. A fence sensor on zone 7 and
   a camera that covers zones 6–8 in a wide view at 12 PPF gives you "yes, something is
   moving over there," which is not assessment.
2. **It must be automatically called up on alarm.** If the operator must find the right
   camera among 300, assessment takes 45 seconds you don't have. Alarm-to-video linkage is a
   *design* requirement and a *commissioning test*, not a configuration afterthought.
3. **It must have enough image quality for the decision required.** Assessment usually needs
   *observation*-class imagery (is it a person, an animal, or a bag blowing?) — but if the
   response decision depends on "is that person carrying a weapon," you need better. Tie the
   pixel density target to the *decision*, not to a habit. See `03_Video_Surveillance/04`.

**Assessment can also be human** (a guard who can see the door), **audio** (an intercom to
ask), or **corroborative** (a second, different sensor type confirming). Video is dominant
because it's fast, remote, and recordable.

> ⚠️ **The classic failing design:** perimeter intrusion detection installed with no
> assessment cameras, at a site whose response is a police dispatch. Every gust of wind
> generates a police call. Within three months the site is on a false-alarm penalty list,
> the alarm is disabled during windy weather, and the $400k system protects nothing. This
> happens constantly. **Detection without assessment is not a partial system; it is often a
> net-negative one.**

### 4. Delay — increase the time required for the adversary to reach the asset

**Delay is the only function measured in units you can compute with: seconds.**

Sources of delay: fences, walls, doors, locks, glazing, vaults, cages, distance, procedural
barriers (interlocks, two-person rules), and — importantly — the *sequence* of them.

Key principles:

**(a) Delay only counts if it occurs *after* detection.** A barrier the adversary defeats
before anyone knows they're there has bought nothing. This is the single most important idea
in this lesson, and it's formalized below as Timely Detection.

**(b) Delay times are adversary- and tool-specific.** A hollow metal door is ~3 minutes
against someone with hand tools and ~15 seconds against someone with a battery-powered
angle grinder. Published delay values (from DoD/DOE-lineage references) are always stated
against a defined adversary with defined tools. `[VERIFY — use current references and state
your assumed adversary]`

**(c) Delay is defeated at the weakest element.** Balanced protection again. The delay of a
barrier system is the *minimum* across all penetration paths, not the average, and not the
value of the impressive part.

**(d) Delay in the wrong place is worthless.** Delay *outside* the detection layer helps only
via deterrence. Delay along a path the adversary won't take helps not at all.

**(e) Guards and locks are not equivalent delay.** A guard is response, not delay; a lock is
delay, not response. Owners conflate them when cutting budget.

### 5. Respond — interrupt and neutralize the adversary

**Response is what actually stops things.** Everything else exists to make response possible
and effective.

Response components:
- **Communication** — the responder is told what, where, and what they're facing (this is why
  assessment feeds response)
- **Deployment** — they physically get there
- **Interruption** — they arrive before the adversary completes the act
- **Neutralization** — they actually stop it (or contain, or observe and report, depending
  on the response doctrine)

**Response Force Time (RFT)** is the interval from annunciation to the responder being in a
position to interrupt. Get this number from the *owner*, honestly, and be skeptical:

| Response type | Realistic RFT | Watch out for |
|---|---|---|
| On-site armed force, posted | 1–3 min | Only if actually posted, not roving |
| On-site unarmed guard, roving | 3–10 min | Where are they *actually* at 0300? |
| Off-site contract patrol | 20–45 min | Contractual, not guaranteed |
| Police, alarm-initiated | 10–60+ min | Priority depends on verification; unverified alarms are deprioritized or ignored in many jurisdictions `[VERIFY locally]` |
| Police, verified (video/audio) | Substantially faster | This is the argument for assessment |
| Remote video monitoring + talk-down | Seconds (deterrent effect), then dispatch | Not interruption; it's deterrence at the moment of attack |

> 🧠 **Ask the question nobody asks:** "What is your actual response, at 3 a.m. on a Sunday,
> in the rain?" The answer is often materially worse than the daytime answer, and the design
> must work for the worst case, not the org chart.

### 6. Recover — restore operations and capture the learning

Frequently omitted from the model; it belongs. Includes: incident response, evidence
preservation and chain of custody, forensic review, restoration of the physical barrier and
the system, insurance and legal processes, notification obligations, root-cause analysis, and
design change.

**The engineering relevance:** your design determines whether recovery is possible.
- Is there recorded video with intact metadata and a defensible chain of custody? (module `09_`)
- Are access logs retained long enough and are they trustworthy?
- Can the breached barrier be restored quickly, or is it a 6-week custom order?
- Does the system tell you *what* was compromised, or only that *something* was?

Also: **resilience** — the system's ability to maintain function under degraded conditions
and return to full function afterward. A design where one server failure blinds the whole
site is not resilient regardless of how good it is when healthy.

---

## 🧮 The Timely Detection principle — the core calculation

This is the most important calculation in physical security engineering. Learn it cold.

**Definitions:**
- `T_D` = time from the *start* of the adversary's task sequence to **detection + assessment**
- `T_T` = **total** adversary task time (start → completing the act at the asset)
- `T_R` = **response force time** (annunciation → interruption)
- `T_A` = adversary time **remaining** after detection = `T_T − T_D`

**The system is effective (timely) if and only if:**

```
        T_A  >  T_R
        
   (T_T − T_D)  >  T_R
```

**In words:** the delay remaining *after* you detect must exceed the time it takes to respond.

The margin `T_A − T_R` is your **timely detection margin**. Design for a positive margin with
headroom, because every input is an estimate.

### Why "after detection" is everything

Consider two sites with **identical total delay**:

```
SITE A — detection at the perimeter
                                                     ┌─ asset reached
  ├──fence──┼────yard────┼──door──┼──interior──┼─safe─┤
  │         │            │        │            │      │
  0:00     0:30         1:30     3:00        7:00   9:00   (T_T = 9:00)
  ▲
  DETECT at 0:20 (fence sensor + camera assessment)
  T_D = 0:20,  T_A = 8:40.  Response T_R = 6:00.
  Margin = +2:40  →  EFFECTIVE ✅


SITE B — detection at the safe
  ├──fence──┼────yard────┼──door──┼──interior──┼─safe─┤
  0:00     0:30         1:30     3:00        7:00   9:00   (T_T = 9:00)
                                                ▲
                                     DETECT at 7:00 (safe tamper sensor)
  T_D = 7:00,  T_A = 2:00.  Response T_R = 6:00.
  Margin = −4:00  →  INEFFECTIVE ❌
```

Same barriers. Same total delay. Same response force. **One works and one doesn't**, and the
only difference is *where detection sits in the sequence*.

> **Therefore: detection should be located as early in the adversary path as assessment can
> be reliably supported.** Not as early as possible — as early as you can still *assess*,
> because unassessed early detection is nuisance-alarm hell (see the perimeter example above).
> That tension — detect early, but only where you can assess — is where perimeter design
> lives.

### 🧮 Worked example 1

A warehouse. The adversary path to the tool crib:

| Task | Delay (s) | Cumulative |
|---|---|---|
| Climb chain-link fence | 15 | 15 |
| Cross yard to building | 25 | 40 |
| Force personnel door (hand tools) | 90 | 130 |
| Cross warehouse floor | 45 | 175 |
| Cut tool crib mesh | 120 | 295 |
| Load and remove goods | 180 | 475 |

`T_T = 475 s ≈ 7:55`

**Scenario A:** detection is a motion sensor inside the warehouse floor, tripping at
t = 130 s (just after door entry), with a camera for assessment adding 15 s of operator time.
`T_D = 145 s`. Response is a contract patrol, `T_R = 25 min = 1500 s`.

```
T_A = 475 − 145 = 330 s
330 > 1500 ?  NO.  Margin = −1170 s (−19.5 min)  ❌
```

The system is not timely by a wide margin. **This is the normal situation for most commercial
sites**, and the honest conclusion is: *this system does not interrupt the event; it documents
it.* Say that out loud to the client. It's a legitimate design — evidence and insurance
recovery are real objectives — but it must be a *chosen* objective, not an accident.

**Scenario B:** the owner adds on-site guards, `T_R = 180 s`.
```
T_A = 330 > 180 ?  YES.  Margin = +150 s  ✅
```

**Scenario C:** keep the contract patrol (`T_R = 1500 s`) and instead try to fix it with
hardware. To be timely you'd need `T_T − T_D > 1500`, i.e. over 25 minutes of delay
remaining after detection. You would need to turn the tool crib into a vault. **Cost-
prohibitive.**

> **The lesson, and it's a big one:** *response time is usually the dominant term, and it is
> usually not an engineering variable.* You will frequently find that no achievable amount of
> hardware makes a system timely against a given response posture. When that's true, your
> deliverable is not more hardware — it's a clear statement to the owner that they are
> choosing between (a) changing the response model, (b) accepting a documentation-only system,
> or (c) reducing the consequence by moving or reducing the asset. **Option (c) is the one
> nobody proposes and it is frequently the cheapest.**

### 🧮 Worked example 2 — designing to a required detection point

Given: `T_R = 240 s` (on-site guard). Required margin ≥ 60 s for confidence.
Adversary task time to the asset: `T_T = 600 s`.

Required: `T_T − T_D > T_R + margin` → `600 − T_D > 300` → `T_D < 300 s`.

**Detection must occur within the first 300 seconds of the adversary sequence.** Now walk
the path and find which barrier the adversary reaches at t = 300 s — detection must be at or
before that point, and assessment must be available there. That's how a detection layer gets
*located by calculation* rather than by habit.

> The calculator implementing this is at
> [`../28_Calculators/timely_detection.py`](../28_Calculators/timely_detection.py).
> **Do the arithmetic by hand first.**

### Where this model is honest about its limits

- Delay values are estimates against an assumed adversary and toolset. Change the assumption,
  change the answer. Always state the assumption in writing.
- It assumes a single linear path. Real adversaries pick the *easiest* path — so you must run
  the analysis on the **weakest** path, not the one you designed. Finding that path is
  adversary path analysis (`02_Risk_Assessment/06`).
- It models interruption, not neutralization. Arriving is not the same as stopping.
- It assumes detection is binary and instant. Real detection is probabilistic; a rigorous
  treatment carries Pd through the whole sequence (this is what EASI-type models do).
- **It does not apply to insiders at all.** An authorized insider has `T_D = ∞` for
  barrier-based detection, because they never trip anything. Insider detection is behavioral,
  procedural, and audit-based.

---

## Classifying countermeasures by function

Run this drill until it's automatic. Note how often the *assumed* function is wrong.

| Countermeasure | Deter | Detect | Delay | Assess | Respond | Recover |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Chain-link fence | ● | | ●(low) | | | |
| Fence-mounted vibration sensor | ○ | ● | | | | |
| Camera, recorded only, not monitored | ●(if visible) | | | ○(after the fact) | | ● |
| Camera, monitored + alarm-linked | ● | ○ | | ● | | ● |
| Video analytics tripwire | | ● | | | | |
| Bright, uniform lighting | ● | ○ | | ●(enables) | | |
| Card reader + electric strike | ○ | ●(of unauthorized attempts) | ● | | | ● (log) |
| Mechanical lock, unmonitored | ○ | | ● | | | |
| Door position switch | | ● | | | | ● (log) |
| Bollards | ● | | ● | | | |
| Guard at a post | ● | ● | | ● | ● | |
| Roving guard patrol | ● | ○ | | ○ | ● | |
| Duress button | | ● | | | | |
| Signage | ● | | | | | |
| Visitor escort policy | ● | ● | ● | ● | | |
| Access log audit | ○ | ●(delayed) | | | | ● |
| Turnstile | ● | ● | ● | | | ● |
| Backup power (UPS/generator) | | | | | | ● |

● = primary function ○ = secondary/weak

**Three things this table teaches:**

1. **An unmonitored camera performs almost no protection functions in real time.** It deters
   (if visible and believed) and it supports recovery. It does not detect and it does not
   assess, because assessment requires a human in the loop *now*. Enormous numbers of camera
   systems are sold on the implicit claim that they detect. Be precise about this with clients.

2. **A mechanical lock is delay with no detection.** You will never know it was defeated. This
   is why a door contact costs $40 and changes the character of the opening entirely.

3. **The functions have wildly different costs.** Deter is cheap. Detect is moderate. Delay is
   expensive and gets exponentially more so. **Respond is by far the most expensive**, because
   it's a recurring salary line rather than a capital cost — and it's the one that actually
   stops things. This economic reality explains most of the security industry: everyone sells
   the cheap functions.

---

## Design tradeoffs

| Tradeoff | The tension | How to resolve |
|---|---|---|
| Detect early vs. assess reliably | Early detection is timelier but harder to assess and noisier | Locate detection at the earliest point where assessment is credible |
| Pd vs. NAR | Sensitivity helps one and hurts the other | Complementary sensor technologies; environmental remediation; alarm logic (AND/verified) |
| Delay vs. cost | Delay scales exponentially in cost | Buy delay only where detection precedes it; otherwise buy detection or reduce consequence |
| Delay vs. egress | Barriers that delay adversaries also delay evacuation | **Life safety wins.** Design delay on the *entry* direction only. See `35_Doors_and_Hardware/` |
| Visible vs. covert | Visible deters but is also mapped and defeated | Visible for deterrence at the perimeter; less obvious for assessment inside |
| Response speed vs. cost | On-site staff is the only fast response and costs the most | Be explicit with the owner: this is their decision, not yours |

---

## Common mistakes

⚠️ **Buying delay without detection.** The most expensive way to be insecure. A hardened door
in an unmonitored area is a speed bump the adversary attacks at leisure.

⚠️ **Detection without assessment.** Creates nuisance alarms that destroy the system's
credibility and, eventually, its use.

⚠️ **Assuming the response force.** Design teams routinely assume a response that does not
exist at 3 a.m. Confirm it, in writing, with the owner.

⚠️ **Counting deterrence as a control.** It's real and it's valuable and it cannot be relied on.

⚠️ **Treating the "average" path.** Adversaries take the easiest path. Analyze the weakest.

⚠️ **Forgetting recover.** Retention that's too short, evidence that isn't defensible, a
custom barrier with a 10-week lead time.

---

## Junior vs. Senior

**Junior:** can classify countermeasures by function; can perform the timely detection
calculation given the numbers; knows detection must precede delay.

**Senior:** knows the numbers are estimates and designs margin accordingly; recognizes when
no hardware solution can achieve timeliness and reframes the problem toward response or
consequence; extracts an honest response time from an owner who wants to give the flattering
one; balances Pd against operator credibility rather than against the datasheet; and can tell
a client "the system you're describing documents crimes rather than preventing them" in a way
that leads to a better decision instead of a defensive one.

---

## Exercises

**E3.1** For each, identify which protection function is missing and what the consequence is:
- (a) A gate with a card reader, a strike, and no door position switch.
- (b) 40 perimeter fence sensors, no exterior cameras, response by police dispatch.
- (c) A monitored intrusion system with 30 minutes of guard response and a safe rated for
  5 minutes of attack.
- (d) A server room with badge access, cameras, and a suspended-ceiling wall.
- (e) A campus with excellent cameras, retained for 3 days, and an incident discovered weekly.

**E3.2** 🧮 A distribution center. Adversary path delay: fence 20 s, yard 40 s, dock door
150 s, floor traverse 60 s, cage 200 s, load 240 s. Detection: dock door contact (assume
detection at completion of the dock door task) + 20 s assessment. Response: on-site guard,
`T_R = 300 s`.
- (a) Compute `T_T`, `T_D`, `T_A`, and the margin. Is it timely?
- (b) The owner replaces the guard with a contract patrol, `T_R = 1800 s`. Now?
- (c) Under (b), propose **three** different interventions — one changing detection, one
  changing delay, one changing consequence — and state which you'd recommend and why.

**E3.3** Take the field-exercise building from lesson 01. Map its measures onto the six
functions in a table. Which function is weakest? What is the cheapest intervention that
would most improve overall effectiveness?

**E3.4** Explain to a non-technical facilities director, in under 100 words and no jargon,
why adding a stronger lock to their storage room won't help, given that nobody is monitoring
it and the nearest guard is 25 minutes away.

> Solutions: [`_solutions/03_functional_chain_solutions.md`](_solutions/03_functional_chain_solutions.md)

---

## Retrieval check

1. State the timely detection inequality and define every term.
2. Why must detection precede delay to be useful?
3. What are the three parts of a detection event?
4. Why does a high nuisance alarm rate reduce *effective* Pd to near zero?
5. Name three requirements for a camera to actually perform assessment.
6. Which protection function is most expensive, and why does that shape the industry?
7. Why does this model fail entirely for insider threats?

---

## References

- Garcia, M.L., *The Design and Evaluation of Physical Protection Systems*, 2nd ed. `[PRACTICE]`
  The authoritative treatment of detect/delay/respond and timely detection. Chapters on
  adversary sequence diagrams and EASI are the next step beyond this lesson.
- Garcia, M.L., *Vulnerability Assessment of Physical Protection Systems.* `[PRACTICE]`
- ASIS International — *Protection of Assets*, Physical Security volume. `[GUIDELINE]`
- Sandia National Laboratories physical protection literature (publicly released portions) —
  origin of much of this methodology. `[GUIDELINE]` `[VERIFY availability]`

**Next:** [04 — Defense in Depth and Security Zones](04_defense_in_depth_and_zones.md)
