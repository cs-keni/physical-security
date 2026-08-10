# Reference Solution — Cedar Junction Park-and-Ride Capstone

> Do not read this before attempting
> [the brief](../_exercises/garage_design.md). All values were produced by running
> [`../../28_Calculators/psec/`](../../28_Calculators/psec/) and transcribed.
>
> **This is a reference solution, not the only correct one.** Several decisions below are
> defensible in more than one direction. What is not negotiable is the *order* of the reasoning:
> requirement, then timeliness, then constraints, then cameras.

---

## The three traps

Before the solution, the three places this site defeats the instincts the module trained.

**Trap 1 — "Identify at the point of the incident."** The Authority asked for it and lessons 04 and
09 will have you reaching for it. It takes **128 cameras**, and it still fails. The incident happens
between parked cars, where the offender is occluded, crouching, facing away, and unpredictable in
location across 115,200 ft².

**Trap 2 — "Light is the binding constraint."** Lesson 03 hammers this, and it is usually right.
Here, **29 of 34 incidents occurred between 09:00 and 16:00.** If you proposed lighting as the
headline fix on the grounds that the garage is dark at night, you applied the module's reflex to a
site whose incidents happen in daylight. Lighting still matters — but for a different and more
specific reason, worked below, and it is **not** the top recommendation.

**Trap 3 — "Find the chokepoint."** Lesson 09's highest-leverage move. Most people find the
**vehicle portal**, because it is barrier-controlled, it is where the existing cameras are, and it
looks like a chokepoint. It is the wrong one: the offenders arrive **on foot**.

---

## 1. Requirements analysis

**What they asked for:** cameras covering the parking areas that will identify whoever is breaking
into cars.

**What they actually need**, derived from their own data:

The Authority has three distinct problems bundled into one request:

1. **An investigative problem** — 34 incidents, 1 arrest. They cannot attribute incidents to
   individuals.
2. **A recurrence problem** — the rate tripled in a year. Something changed and nobody knows what.
3. **A rider-confidence problem** — two riders have stopped using the station. This is a revenue and
   reputational problem, and it is arguably the one the Board actually cares about.

**Video addresses (1) well, (2) partially, and (3) only indirectly.**

**The operational decision the video must support:**

> *Who entered the garage on foot during the period an incident occurred, to a standard that would
> support identification and prosecution of a person unknown to the reviewer — and can repeat
> offenders be linked across incidents?*

Note what that is **not**. It is not "capture the break-in." It is identification of **people
entering and leaving the garage on foot**, correlated to a time window. The break-in itself, captured
at observe grade, establishes the time window; the cores establish who was present.

**What the system will and will not achieve — state this before designing:**

| Will | Will not |
|---|---|
| Identify every person entering or leaving on foot | Identify an offender from footage of the bay itself |
| Establish the time window of an incident to within minutes | Prevent the incident |
| Link repeat offenders across incidents | Produce a response while the incident is in progress |
| Capture the plate of every vehicle entering and leaving | Attribute an on-foot offender to a vehicle |
| Support prosecution with identify-grade images | Recover property |

---

## 2. Adversary path and timeliness

**(a) Assumed adversary and task times** `[PRACTICE — stated so they can be challenged]`:

A single opportunist on foot, carrying a hand tool (spring punch or similar), targeting visible
property in vehicle cabins. Not a determined or equipped adversary; consistent with 21 of 34 entries
being window breaks and 31 of 34 takes being from the cabin.

| Task | Delay (s) |
|---|---|
| Approach vehicle on foot, scan cabin | 20 |
| Force window or door | 25 |
| Remove property from cabin | 40 |
| Walk to stair core and exit | 45 |

**(b) `T_T` — total task time: 130 seconds.**

**(c) Timeliness.** Assume the best possible detection — an analytic on the deck detecting the
approach, with a 60-second assessment allowance (generous, given there is **no one to assess**):

```
T_D (detection + assessment) =  80 s
T_R (measured response)       = 720 s   (12 min; worst case 900 s)

T_D + T_R = 800 s     vs.     T_T = 130 s
deficit   = 670 s  (11.2 minutes)
```

Now the decisive test. Assume **instant detection and zero assessment** — a physically impossible
best case:

```
T_R alone = 720 s     vs.     T_T = 130 s
deficit   = 590 s  (9.8 minutes)
```

**(d) The conclusion.**

> **No detection point anywhere on this site can produce a timely response.** The response time
> alone exceeds the adversary's entire task time by a factor of **5.5×**. The offender completes
> the act and leaves the structure roughly ten minutes before anyone could arrive, even with a
> perfect detector and an operator who does not exist.

**What that means for the design, and it governs everything downstream:**

- **Detection has no interruption value here.** Do not design for it, do not sell it, and do not
  deploy live analytics hoping for it ([lesson 11](../11_analytics_and_health.md)).
- **The system is a documentation and attribution system.** That is a legitimate and valuable thing
  to be ([lesson 01](../01_imaging_chain.md)) — it supports investigation, prosecution, and pattern
  analysis, which is exactly what a site with 34 incidents and 1 arrest needs.
- **The remaining levers are deterrence and delay**, not detection. This is where the highest-value
  recommendation comes from — see section 7.

> 🧠 **Why this is the right first calculation.** Doing it before any camera work reframes the whole
> project honestly, and it takes fifteen minutes. A designer who skips it will spend the budget
> chasing detection and deliver a system that the Authority believes will stop break-ins.

---

## 3. Zone and target analysis

| Zone | Question | Class | Reasoning |
|---|---|---|---|
| **Core lobby doors** (2 cores × 4 levels + 2 at grade = 10) | *Who entered or left the garage on foot, to a standard a stranger could identify?* | **identify (76)** | **The critical zone.** Everyone on foot passes a core. Enclosed, small, lightable, frontal, slow — every constraint favourable |
| **Core interiors / stair landings** (8) | *Which level did this person go to, and when did they return?* | **recognise (38)** | Continuity between the identified entry and the deck. Identity established at the door is *carried* here ([lesson 09](../09_camera_placement.md)) |
| **Parking decks** (16) | *When and where did an incident occur, and which direction did the person come from and go?* | **observe (19)** | Establishes the **time window** and the movement, not the identity. This is the reclassification the whole design turns on |
| **Vehicle portal — plate** (2) | *Which vehicles entered and left, by plate?* | **LPR (dedicated)** | Its own discipline ([lesson 02](../02_optics_and_lenses.md)); not a DORI class |
| **Vehicle portal — occupants** (2) | *Who was in the vehicle at entry and exit?* | **identify (76)** | Separate camera from the LPR; different lens and exposure |
| **Payment machines** (4, at grade + level 1) | *Who used this machine at this transaction?* | **identify (76)** | Transaction correlation, and a natural chokepoint. Only where machines are on likely routes |
| **Pedestrian street gate** | *Who entered from the street?* | **identify (76)** | Covered by the grade-level core cameras; see design note |

**The reclassification of the decks from identify to observe is the single most important decision
in this design.** Justification:

```
identify on the decks:  30.06 ft effective per camera → 32 cameras/level → 128 total
recognise:              60.13 ft                      →  8 cameras/level →  32 total
observe:               120.25 ft                      →  2 cameras/level →   8 total
```

**128 cameras versus 16** (we use 4 per level rather than the geometric minimum of 2, for sightlines
around structural columns). And the 128 would *still* not identify anyone, because of occlusion
between vehicles, pose, and crouching. **We are not accepting a lower standard to save money; we
are declining to buy a capability that does not exist at any price on this geometry.**

---

## 4. The light problem — and the trap in it

**(a) Exposure budget deficit on the decks.**

Measured: **2.5 lux average, 12:1 max:min uniformity.** In that light the camera settles at
**1/15 s** at f/1.4.

```
required shutter for a walking subject (25% eye-to-eye smear budget) = 1/84 s → 1/125 s standard
stops short = log₂((1/15) ÷ (1/125)) = log₂(8.33) = 3.06 stops
required illuminance = 2.5 × 8.33 = 20.8 lux
```

Smear at the shutter the camera actually chooses:

| Shutter | Smear | % of eye-to-eye |
|---|---|---|
| **1/15 s (actual)** | 3.52 in | **141%** |
| 1/30 s | 1.76 in | 70% |
| 1/125 s (required) | 0.42 in | 17% |

At 1/15 s the motion smear **exceeds the entire eye-to-eye distance**. Nobody is identifiable, at
any pixel density.

**(b) The specification.**

> Provide a minimum maintained illuminance of **21 lux** at 5 ft above the deck slab, measured
> vertically, throughout all parking and circulation areas, with a maximum-to-minimum uniformity
> ratio no worse than **4:1**. `[VERIFY against the applicable lighting standard and any transit
> authority requirement.]`

**(c) — and here is the trap.**

**29 of 34 incidents occurred between 09:00 and 16:00.** So does the lighting argument survive?

**Partly, and you must be precise about why — a general "the garage is dark" argument is wrong
here.**

- **Level 4 is an open deck.** In daylight it has ample natural light. Lighting improvements there
  do nothing for the 09:00–16:00 incidents. They matter only for the ~5 out-of-hours incidents.
- **Levels 1–3 are enclosed.** They measure **2.5 lux at noon** as well as at midnight, because the
  1970s fluorescent fittings are the only light source and many have failed. **The daylight
  incidents on level 3 happened in a 2.5 lux environment.** For those, the exposure budget applies
  in full.
- 26 of 34 incidents were on **levels 3 and 4** — a mix of the two cases.

**Correct conclusion:** lighting is a **real and necessary** intervention on levels 1–3, justified
by the enclosed levels being dark at all hours, and it is **not** justified on level 4 by the
incident data. And because the core lobbies are enclosed and small, **lighting them properly is
cheap and is where the identification actually happens** — so core lighting is the highest-priority
lighting spend, not deck lighting.

> 🧠 **What this trap teaches.** Lesson 03's rule — measure the light, compute the budget — is
> right. The reflex that grew out of it — *"the problem is always that it's dark at night"* — is a
> habit, not a rule. The incident data was in the brief, and it says the offenders work in daylight.
> **A designer who did not reconcile their lighting argument against the incident timing was
> designing from the module rather than from the site.** Module 32's problem set does the same thing
> deliberately, reversing a conclusion from module 35.

**(d) If the Authority will not fund lighting:**

The core cameras still work, because the lobbies are enclosed spaces where a single fitting delivers
the required illuminance for very little money — and the cores are where identification happens. The
deck cameras degrade to establishing that *something* happened and roughly when, which is still
enough to define the time window the core footage is then searched against. **The design degrades
gracefully, which is a property worth engineering for deliberately.** Say so, and price the core
lighting separately and small so it is not lost in a value-engineering exercise.

---

## 5. The design

### (a) Camera schedule

| ID | Location | Question | Class | Lens | Mount | Illumination |
|---|---|---|---|---|---|---|
| C-A1…A4, B1…B4 (8) | Core lobby doors, levels 1–4 | Who passed through, identifiable to a stranger? | identify | 4 mm | **8.0 ft** | 30 lux at face plane |
| C-A0, B0 (2) | Core lobby doors at grade | As above, street entry | identify | 4 mm | 8.0 ft | 30 lux |
| C-SA1…4, SB1…4 (8) | Stair landings / core interiors | Which level, and when did they return? | recognise | 2.8 mm | 8.0 ft | 20 lux |
| C-D1…D16 (16) | Parking decks, 4 per level | When and where, and direction of travel? | observe | 2.8 mm | 7.5 ft (soffit) | 21 lux (levels 1–3) |
| C-LPRi, C-LPRo (2) | Vehicle entry/exit lanes | Which vehicles, by plate? | LPR | dedicated | 4.5 ft | dedicated IR |
| C-Pi, C-Po (2) | Vehicle entry/exit lanes | Who was in the vehicle? | identify | 6 mm | 8.0 ft | 30 lux |
| C-M1…M4 (4) | Payment machines, grade + level 1 | Who used this machine? | identify | 4 mm | 8.0 ft | 30 lux |

**Verification of the core door cameras** (4 MP, 2688 px, 1/2.8", 4 mm, 8.0 ft mount, face plane
5 ft):

| Distance back | Slant | Depression | PPF | Class |
|---|---|---|---|---|
| 8 ft | 8.54 ft | 20.56° | **234.3** | identify |
| 10 ft | 10.44 ft | 16.70° | **191.8** | identify |
| 12 ft | 12.37 ft | 14.04° | **161.9** | identify |

All three comfortably exceed 76 ppf with large margin, at angles well inside 30°. **Specify 10 ft
where lobby depth allows** — 2.5× margin, and margin is the tolerance budget for everything not
modelled ([lesson 04](04_dori_and_pixel_density.md) E4.3).

**On the 8 ft soffit — the answer to brief question 2.** The depression angle is **not** a problem
here, and that surprises people. A low soffit forces a low mount, and a low mount is exactly what
identification wants ([lesson 09](../09_camera_placement.md)). At 7.5 ft mount and 20 ft distance
the depression angle is **7.13°** — nearly level. The garage's most awkward physical constraint is
an advantage for this design. **Vandal resistance, not angle, is the real consequence of a low
mount**, so specify IK10 vandal-resistant housings throughout `[VERIFY rating per product]`.

### (b) Camera count

| Group | Count |
|---|---|
| Core lobby doors (identify) | 10 |
| Core interiors / stair landings (recognise) | 8 |
| Deck coverage (observe) | 16 |
| Vehicle portal LPR | 2 |
| Vehicle portal occupants | 2 |
| Payment machines | 4 |
| **Total** | **42** |

**42 cameras, against 128 for identify-everywhere on the decks alone** — and the 42 delivers
identification, which the 128 does not.

### (c) Bandwidth and storage

Computed with `psec.video`, 30-day retention, continuous recording:

| Case | Peak bandwidth | 30-day storage |
|---|---|---|
| Nominal | 246.0 Mbps | 79.70 TB |
| **Nominal + 20% headroom** | **295.2 Mbps** | **95.64 TB** |
| Deck cameras at the high band (14 Mbps) | 342.0 Mbps | 110.81 TB |

**Basis of estimate:**

> Estimated peak bandwidth **246 Mbps nominal**, range **246–342 Mbps**. Estimated 30-day storage
> **79.7 TB nominal**, range **79.7–110.8 TB**. Assumptions: H.264, continuous recording, 30-day
> retention, **no smart-codec saving assumed**. The **deck cameras carry by far the widest
> uncertainty** — an open level 4 with weather, headlights, and moving shadows is the worst case for
> temporal compression ([lesson 06](../06_compression_and_bandwidth.md)). Provision at nominal +20%
> (**95.6 TB**), with the array able to reach the high case without chassis replacement. Bitrates to
> be measured per group in the first 30 days and provision reviewed.

**On retention:** the Authority's standard is 30 days, but **riders report damage 8–11 hours after
the event** and — more importantly — **investigating a pattern of 34 incidents requires looking
across months, not days.** Recommend **90 days on the core cameras** (the identification set, 18
cameras), keeping 30 days elsewhere. Per-zone retention
([lesson 07](../07_storage_and_retention.md)) makes this cheap, and it is what makes cross-incident
offender linking possible at all.

### (d) VMS architecture

- **Two recording servers**, splitting the failure domain (~21 cameras each), in the garage plant
  room. RAID 6 with hot spare.
- **Management server** hosted by Transit Authority IT on their existing virtual infrastructure,
  under their backup regime.
- **Substreams enabled** — there is no monitoring station, but investigators reviewing footage
  remotely over the station fibre will otherwise saturate it.
- **Recording is local, management is central** ([lesson 08](../08_vms_architecture.md)).

> **Failure behaviour.** One recording server fails: ~21 cameras stop recording until repaired;
> already-recorded video remains retrievable. Estimated 4–24 h. **Cameras are split so that each
> core's cameras are divided across both servers** — a single server failure never removes
> identification coverage of both cores at once. Management server fails: recording continues;
> remote review unavailable until restored. Network to station fails: recording continues locally.
> Storage degrades: hot spare rebuilds automatically; alerts to a named Transit Authority role.

**That camera-to-server split is a design decision worth calling out.** The naive split is by
level; the correct split is by **core**, so that the failure of either server still leaves every
level's on-foot traffic captured at one core.

### (e) Analytics

**Do the precision arithmetic first** ([lesson 11](../11_analytics_and_health.md)). With detection
established as having no interruption value, **live alarms are not proposed at all** — there is
nobody to receive them and no response that would be timely.

**What is proposed:**

- **Retrospective search on the core cameras** — person detection and appearance search. This is the
  highest-value analytic on the site by a wide margin: given a deck incident time window, it turns
  "who entered on foot in the preceding hour" into a handful of clips in seconds, across 90 days of
  footage. **This is what will link repeat offenders across the 34 incidents.**
- **LPR list matching** at the portal, for vehicle attribution and for flagging repeat plates.
- **Object classification** on the deck cameras, to make retrospective search on the decks usable.

**Not proposed:** live intrusion alarms, loitering alerts to a remote centre, or anything relying on
an operator. The precision would be near-zero and there is no response at the end of it.

### (f) Health monitoring and acceptance

**Health monitoring:** device online, recording verification, retention achieved per group, **scene
change against dated reference images** (a garage is full of ladders, contractors, and delivery
vehicles that knock cameras out of aim), focus metric, overnight luminance (catches failed
lighting — directly relevant here), NTP offset. **Alerts to a named Transit Authority role**, tested
at commissioning.

**Acceptance tests:** pixel density verification at every core door with a known-height subject;
**night verification with a walking subject at every core and on level 4**; illuminance measurement
against the 21 lux / 30 lux specifications; continuity walk from street gate through a core to a
level 3 bay; LPR read-rate test at night and in rain; retention verification after 30 days;
recorder failover test; export test; health alert test; **reference image capture for all 42
cameras**.

---

## 6. The client conversation

> **Cedar Junction Park-and-Ride — video surveillance, summary for the Board**
>
> You asked for cameras that identify whoever is breaking into cars. I want to be straight about
> what is achievable, because the honest answer changes the design and I think it gets you a better
> outcome.
>
> **We cannot identify someone at the car.** Covering 640 bays across four levels to
> identification standard would take around 128 cameras, and it would still fail — between parked
> cars people are hidden, crouching, and facing away. That is a limit of the geometry, not of the
> budget.
>
> **We can identify everyone who walks in and out.** Every person who reaches a parked car arrives
> and leaves on foot through one of your two stair and lift cores. Those lobbies are small,
> enclosed, and easy to light, and a camera there gets a clear, front-on view of every person who
> passes. Cameras on the decks then establish when and where an incident happened, and we search the
> core footage for that window. That is how you go from 34 incidents and one arrest to identifying
> repeat offenders — and your own data suggests these are repeat offenders.
>
> **The system will not stop a break-in, and I want that on the record.** Your measured police
> response is twelve minutes. A break-in takes just over two. Even with a perfect detector and
> someone watching around the clock, the offender is gone roughly ten minutes before anyone
> arrives. Anyone who tells you cameras will stop this is selling you something. What this system
> does is let you identify, prosecute, and — once word gets round that this garage produces arrests
> — deter.
>
> **Two things matter more than the cameras.** First, the pedestrian gate from the street is
> uncontrolled and open twenty hours a day, which is how offenders are getting in on foot. Putting
> that gate and the core doors behind a rider credential would remove most of the opportunity, and
> I would spend money there before I spent it on my own scope. Second, levels 1 to 3 measure 2.5 lux
> at noon — your enclosed levels are dark all day, and that is where most incidents are. The
> lighting needs replacing regardless of what we do with cameras.
>
> **Forty-two cameras, not the coverage you were quoted for.** Fewer cameras, better placed, plus
> lighting and gate control. I would rather give you a system that identifies people than one that
> covers ground.

*(392 words.)*

---

## 7. The recommendation that reduces your fee

**The highest-value intervention on this site is not a camera and not lighting. It is controlling
the uncontrolled pedestrian street gate and the core doors.**

The offenders arrive on foot. The garage has a pedestrian gate open from 05:00 to 01:00 with no
control at all, and core doors that anyone can use. **Putting the street gate and the core lobby
doors behind a rider credential** — a transit card tap, which riders already carry — does three
things video cannot:

1. **It removes the opportunity** rather than recording its exercise. A person with no transit
   credential cannot get to the decks.
2. **It creates a transaction record** for every entry, which correlates with the video and turns
   "who is this person" into "which credential was used" — dramatically stronger attribution than
   video alone ([lesson 08](../08_vms_architecture.md)).
3. **It supplies delay and deterrence**, which are the only levers the timeliness analysis left
   available.

It is also outside the scope you were engaged for, and recommending it reduces the size of the video
job.

> 🧠 **Say it anyway, and say it first.** [`AI_CONTEXT.md`](../../docs/AI_CONTEXT.md) names this as
> the discipline's defining act: *"the highest-value recommendation is outside your scope and
> reduces your fee."* A Board that has approved capital for cameras and is told by the camera
> engineer that access control matters more will believe it, precisely because it costs the person
> saying it. That is the credibility that generates the next engagement.

---

## Assessment: how did you do?

| Did you... | Why it matters |
|---|---|
| Compute the timeliness deficit **before** designing? | It reframes the entire project. Skipping it produces a detection system that cannot detect in time |
| Reclassify the decks from identify to observe, with the 128-vs-16 arithmetic? | The core engineering judgment of the exercise |
| Locate the chokepoint at the **pedestrian cores**, not the vehicle portal? | Trap 3. The offenders arrive on foot |
| Notice that the 8 ft soffit **helps**? | Tests whether you apply the mounting-height envelope or recite it |
| Reconcile your lighting argument against **29 of 34 incidents in daylight**? | Trap 2, and the sharpest question in the brief |
| Distinguish enclosed levels 1–3 (2.5 lux at noon) from open level 4? | The precise version of the lighting argument |
| Recommend **per-zone retention**, 90 days on the cores? | Cross-incident linking is the actual investigative need |
| Split recorders **by core** rather than by level? | Failure-domain thinking applied to the specific site |
| Decline live analytics on precision grounds? | Lesson 11 applied rather than recited |
| Recommend the **access control** intervention that shrinks your own scope? | The professional act the whole academy is pointed at |

**If you produced a 42-camera design with identification at the cores, observe on the decks, and an
honest timeliness statement — you have done the exercise.** If you also told the Board to spend
money on the gate before spending it on you, you have done it as a senior engineer would.

---

## Cross-references

- [`../../32_Engineering_Math/08_adversary_path.md`](../../32_Engineering_Math/08_adversary_path.md)
  — the timeliness arithmetic in section 2.
- [`../../01_Foundations/03_functional_chain.md`](../../01_Foundations/03_functional_chain.md) —
  detect / delay / respond, and why deterrence and delay are the remaining levers.
- [`../../01_Foundations/exercises.md`](../../01_Foundations/exercises.md) — the Ashford Public
  Library capstone reaches a structurally similar conclusion (detection cannot be made timely) by a
  different route, and lands on **delay** where this site lands on **deterrence and access
  control**. Comparing the two is worthwhile.
- [`../../32_Engineering_Math/_exercises/integrated_sizing.md`](../../32_Engineering_Math/_exercises/integrated_sizing.md)
  — the module 32 capstone, which sizes a system correctly; this one decides what to size.
