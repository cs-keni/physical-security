# 🧮 Capstone — Integrated Sizing: One Site, All Eight Lessons

**The capstone for Module 32.** Do it after lesson 08, with all eight lessons behind you.

**Time:** 4–6 hours. Do it over two sessions; Part F benefits from sleeping on it.
**Prerequisite:** lessons 01–08 and their problem sets.
**Deliverable:** a completed design worksheet plus a two-page **basis of design** memo.
**Reference solution:** [`../_solutions/integrated_sizing_reference.md`](../_solutions/integrated_sizing_reference.md)

---

## Why this exercise exists

Every lesson in this module taught one calculation in isolation. Real design is not eight
separate calculations — it is one design in which **each calculation constrains the next**. The
lens you pick sets the pixel density, which sets whether you need more cameras, which sets the
bitrate total, which sets the storage, which sets the PoE budget, which sets how many switches
you need, which sets where the IDF goes, which sets the cable run length, which sets the
conductor. Change the lens and you may change the conductor.

That chain is the thing this exercise teaches, and it is not visible from any single lesson.

There is a second thing. **This design fails on the first pass.** Four times, in four different
places, for four different reasons. That is not a trick — it is what design actually looks like,
and the skill being tested is not "compute correctly" but **"notice that the answer is
unacceptable and know which knob to turn."** A student who sails through this exercise without
re-specifying anything has made an arithmetic error somewhere.

---

## Rules

1. **Hand-calculate first, then check with `psec`.** Every part below can be done with a
   calculator and the formulas from the lessons. Do that. Then run the code. If they disagree,
   find out why before moving on — that disagreement is the most valuable thing this exercise
   can give you.
2. **Show the units at every step.** Half the traps in this exercise are unit traps.
3. **State every assumption you make.** Where the brief is silent, you must decide, and the
   decision must be written down. An unstated assumption is a defect.
4. **Tag every claim that depends on code or a standard** with `[CODE][VERIFY]` and name what
   you would have to look up. You are not expected to have the adopted code text. You *are*
   expected to know that you need it.
5. **When a calculation fails, do not quietly change an input to make it pass.** Record the
   failure, then record the fix and its cost. The failures are the deliverable.
6. **Present ranges where the underlying figure is a range.** Especially in Part B.

---

## The site

**Meridian Cold Chain — Building 4, a third-party logistics (3PL) distribution centre.**
Single-storey tilt-up warehouse on a fenced 6-acre parcel in a light-industrial park. Operates
two shifts, five days; unoccupied nights and weekends except for a roving contract patrol.

Inside the warehouse is a **caged vault room** holding controlled pharmaceutical inventory
(Schedule II). The cage is expanded metal over a steel frame, floor to deck, with one gate.
It is the asset. Everything else on this site is either a path to it or an alibi.

```
                              N
   ┌───────────────────────────────────────────────────────────────┐
   │   8 ft chain link fabric, 3-strand barbed outrigger           │
   │                                                               │
   │            ┌──────────────────────────────────────┐           │
   │            │                                      │           │
   │            │      WAREHOUSE 300 ft x 200 ft       │           │
   │   yard     │                                      │   yard    │
   │  (paved)   │              ┌──────────┐            │  (paved)  │
   │            │              │  VAULT   │            │           │
   │            │              │   CAGE   │  40 x 30   │           │
   │            │              │   [G]    │            │           │
   │            │              └──────────┘            │           │
   │            │                                      │           │
   │            │  [P]                                 │           │
   │            └───┬──────────────────────────────┬───┘           │
   │                │  DOCK APRON  4 dock doors    │  ┌─────────┐  │
   │                └──────────────────────────────┘  │ OFFICE  │  │
   │                        truck court                │ + LOBBY │  │
   │                                                   └────┬────┘  │
   └─────────────────────[ VEHICLE GATE ]───────────────────┴───────┘
                                 │
                          public road

   [G] cage gate      [P] dock personnel door (man-door beside dock 4)

   Distances you will need:
     Vehicle gate to gatehouse camera mast .................  60 ft
     Fence line to nearest camera mast, longest span ....... 200 ft
     Dock apron, furthest point from dock camera ...........  55 ft
     Warehouse floor, furthest point from an overview cam ..  80 ft
     Cage gate to the camera covering it ...................  12 ft
     Lobby door to lobby camera ............................  15 ft
     IDF-1 (office) to cage gate hardware, cable route .....  250 ft
     Cage gate frame to lock through the power transfer ....    8 ft
```

---

## Given data

### Client requirements

| # | Requirement | Source |
|---|---|---|
| R1 | Identify any driver at the vehicle gate | Client, written |
| R2 | Recognise persons anywhere on the dock apron | Client, written |
| R3 | Detect a person crossing the fence line at any point | Client, written |
| R4 | Identify any person entering the vault cage | Regulatory, per client counsel `[VERIFY]` |
| R5 | Identify any person entering the lobby | Client, written |
| R6 | Observe general activity on the warehouse floor | Client, verbal |
| R7 | 30-day retention, all cameras | Client, written |
| R8 | 90-day retention, vault cage camera | Regulatory, per client counsel `[VERIFY]` |
| R9 | Access control on 6 openings; 4 h standby minimum | Client + `[CODE][VERIFY]` |
| R10 | Detection must be timely against the design-basis adversary | Yours to defend |

### Camera platform (the client has standardised on one model)

```
   4 MP fixed dome / bullet, 2688 x 1520, 1/2.8" sensor (5.37 x 3.02 mm)
   Lens options stocked:  2.8 mm   4 mm   6 mm   9 mm   12 mm
   Outdoor variants have integral heaters and classify as 802.3at
   Indoor variants classify as 802.3af
```

### Draft camera schedule (the previous designer's first pass — audit it)

| Tag | Qty | Location | Lens | Mount ht | Design distance | Task required |
|---|---|---|---|---|---|---|
| FENCE-01..04 | 4 | Fence line masts | 6 mm | 16 ft | 200 ft | Detect (R3) |
| GATE-01 | 1 | Gate mast | 4 mm | 14 ft | 60 ft | Identify driver (R1) |
| DOCK-01..04 | 4 | Dock canopy | 6 mm | 16 ft | 55 ft | Recognise (R2) |
| WHSE-01..06 | 6 | Warehouse deck | 2.8 mm | 24 ft | 80 ft | Observe (R6) |
| CAGE-01 | 1 | Above cage gate | 4 mm | 12 ft | 12 ft | Identify (R4) |
| LOBBY-01..02 | 2 | Lobby ceiling | 6 mm | 10 ft | 15 ft | Identify (R5) |
| | **18** | | | | **as drafted** |

Assume a 5 ft target height (eye/face plane) throughout.

### Recording parameters (the previous designer's first pass — audit these too)

| Group | Codec | Frame rate | Recording | Retention |
|---|---|---|---|---|
| Fence line | H.265 | 15 fps | Motion, 35% duty cycle | 30 d |
| Vehicle gate | H.265 | 30 fps | Continuous | 30 d |
| Dock apron | H.265 | 15 fps | Continuous | 30 d |
| Warehouse floor | H.265 | 10 fps | Motion, 50% duty cycle | 30 d |
| Vault cage | H.265 | 30 fps | Continuous | 90 d |
| Lobby | H.265 | 15 fps | Continuous | 30 d |

Use the module's reference bitrate for 4 MP at 30 fps H.264 as the starting point.

### Network and power

```
   IDF-1  office IDF        24-port PoE+ switch, 370 W PoE budget
   IDF-2  yard/gatehouse    24-port PoE+ switch, 370 W PoE budget
   Both switches: 20% spare-port policy [PRACTICE]
```

### Access control (6 openings, all on one panel in IDF-1)

| Load | Qty | Standby (A ea) | Alarm/active (A ea) |
|---|---|---|---|
| Access controller + power board | 1 | 0.250 | 0.250 |
| Card readers | 6 | 0.120 | 0.200 |
| Electrified locks, fail secure | 6 | 0.030 | 0.450 |
| Door position switch + REX | 6 | 0.008 | 0.008 |
| Local sounder | 1 | ~0 | 0.300 |

Cage gate lock: **12 VDC nominal, 0.45 A, minimum operating voltage 10.2 V** `[MFR][VERIFY]`.
Supply is a battery-backed 12 VDC unit; **calculate against 12.0 V**, not 13.8 V, because a
battery-backed supply sags toward the low end of its range on standby.
Cage gate home run as drawn: **250 ft of 18 AWG**. Power transfer and door loop: **8 ft of 22 AWG**.

### Design-basis adversary (for Part F)

> Two outsiders, no insider aid. Cordless angle grinder, bolt cutters, hand tools. Box truck
> staged off-site. Motivated by resale value of the controlled inventory; willing to work for
> roughly 20 minutes; not willing to confront a responder.

| Task | Delay |
|---|---|
| Cut and spread fence fabric | 90 s |
| Cross yard to building | 45 s |
| Force dock personnel door `[P]` | 180 s |
| Cross warehouse floor to cage | 60 s |
| Cut cage mesh and enter | 240 s |
| Load product to hand truck | 300 s |

Detection as drawn: **door position switch on the dock personnel door**, at task completion.
Assessment delay: **60 s** (patrol supervisor must reach a monitor and call up video).
Response: **contract patrol, 11 minutes (660 s)** from alarm to arrival at the fence line.
Required confidence margin: **120 s.**

> These delay values are **illustrative**, not authoritative. Real task times come from tested
> penetration data for the specific construction. `[PRACTICE][VERIFY]` Treat the numbers as given
> for the exercise and say so in your memo.

---

## Part A — Optics and pixel density (lessons 01, 02)

**A1.** For each row of the draft camera schedule, compute the horizontal angle of view, the
scene width at the design distance, and the pixel density. Use the **slant range**, not the floor
distance. State the depression angle for each.

**A2.** Compare each result against the task required by the matching client requirement. **Two
rows fail** — one badly, one narrowly. Identify both and state the shortfall as a percentage of
the requirement.

**A3.** For the row that fails badly, compute the focal length that would meet the requirement at
the stated distance. Then compute the angle of view that lens gives you, and say what you have
just given up.

**A4.** That failure therefore **cannot be fixed by changing the lens alone** — the client asked
for something the corrected lens can no longer deliver. Say what, propose the fix, and state the
added cost in devices, ports, and watts. You will need those three numbers in Part C.

**A5.** For the row that fails narrowly, compute the **maximum floor distance** at which the
drawn lens still meets its task. (Careful: `max_range_ft` returns a slant range. Convert it.)
Given a 300 ft × 200 ft floor and six drawn positions at 80 ft, state roughly how many positions
that distance implies, and by what reasoning. Then propose the fix and its cost in devices,
ports, and watts.

**A6.** Someone suggests fixing A5 with a 4 mm lens at the same six positions instead of adding
cameras. Compute the pixel density that gives at 80 ft. It passes. Explain why you would still
not do it.

**A7.** For the fence line: at what slant range does FENCE-01 stop meeting "detect"? Given a
200 ft longest span, does the mast spacing work? What happens to your answer if the client later
upgrades R3 from "detect" to "observe"?

**A8.** State three things pixel density does **not** tell you about whether these cameras will
actually satisfy R1–R6.

---

## Part B — Bandwidth and storage (lessons 03, 04)

**B1.** Compute the per-camera bitrate for each group from the reference figure, applying frame
rate scaling and the codec factor in the correct order. Show the intermediate value.

**B2.** Compute peak and average aggregate bandwidth for the whole system, and for each of the
two switches separately once you have decided the split in Part C. Say which number you would
put on a network riser and why.

**B3.** Compute raw storage for the retention table, then apply headroom. Then compute the same
figure in **TiB**. State the percentage gap between the two and explain where it comes from.

**B4.** Present the storage answer as an **honest range**, not a point value. Write the single
sentence you would say to the client alongside that range.

**B5.** Size the array. The client wants RAID 6. Compute raw disk capacity required for
8-disk and 12-disk groups. State plainly what RAID 6 does and does not protect against here.

**B6.** *The inverse problem.* Meridian has an existing NVR in another building: **96 TB usable**,
30 cameras, 8 MP, H.264, 30 fps, continuous, 24 h/day. The facilities manager believes it holds
30 days and has told an auditor so. Compute the actual retention. Then compute what it would take
to reach 30 days two different ways — buy disk, or change encoding — and give the numbers for
both.

**B7.** Your Part A fixes changed the camera count. Redo B2 and B3 with the corrected schedule.
State the delta in peak bandwidth, average bandwidth, and storage-with-headroom, and attribute
each delta to the specific optics decision that caused it.

---

## Part C — PoE budget and switch capacity (lessons 05)

**C1.** Budget both switches for the corrected camera count. Use **class allocation**, not
datasheet draw, and justify that choice in one sentence.

**C2.** First try putting every camera on one switch. Report ports used, power used, utilisation,
and every finding. State which of the two constraints binds and by how much.

**C3.** Now split the cameras across IDF-1 and IDF-2 on a **geographic** basis. Report both
switches. One of them raises a finding even though it passes. Explain what that finding is
protecting you from.

**C4.** For the switch in C3 that is tightest: you have free ports and free watts. Compute how
many additional **outdoor** cameras you could add before the switch fails, and how many
additional **indoor** cameras. Explain to a client, in one sentence, why "we have 14 spare ports"
is a misleading thing to say.

**C5.** Re-budget the single-switch case using **datasheet draw** figures instead of class
allocation (assume 16.5 W outdoor, 7.2 W indoor). The power finding disappears. Note that one
finding does **not** disappear, and say why that is significant. Then explain in three sentences
why you would still not build the single-switch design, and what you would have to `[VERIFY]` to
change your mind.

**C6.** Why does none of this require the voltage-drop calculation from lesson 06?

---

## Part D — Voltage drop (lesson 06)

**D1.** Compute the voltage at the cage gate lock as drawn: 250 ft of 18 AWG home run plus 8 ft
of 22 AWG through the power transfer. Show both segments separately. Does it pass?

**D2.** State what fraction of the total drop each segment contributes. Compare this with the
conclusion of `35_Doors_and_Hardware/06`. What general rule does the comparison destroy?

**D3.** Someone on your team runs `smallest_awg_for_run` against the **home run only**, gets an
answer, and specifies it. Show that this answer is wrong, and show by how little. Then do it
correctly by budgeting the drop across both segments.

**D4.** Compute the maximum run length for 18 AWG and for your corrected gauge at this load.
State the design margin your corrected answer leaves.

**D5.** The supply's battery sags to 11.6 V near the end of standby. Recheck your corrected
conductor at 11.6 V. Does it still pass? If your answer changes, say what you would do.

**D6.** Give one alternative that fixes this without changing the conductor at all, and state its
tradeoff.

---

## Part E — Battery and power supply (lesson 07)

**E1.** Build the load list. Compute total standby current and total alarm current separately.

**E2.** Size the battery for the 4 h standby requirement with a 5-minute alarm. Show the raw
amp-hours, then the derate and aging factors, then the sized figure. Select a real battery.

**E3.** Size the power supply. State which current governs the battery and which governs the
supply, and give the physical reason.

**E4.** Compute realistic runtime for your selected battery. Compare it against the 4 h
requirement and state the margin.

**E5.** The AHJ turns out to require **24 h** standby `[CODE][VERIFY]`. Recompute. What changes
about the enclosure, the supply, and the charging circuit — and which of those three does the
calculator not tell you?

**E6.** A colleague sizes the battery by **adding** the derate and aging factors (1.0 + 0.25 +
0.25 = 1.5) instead of multiplying them. Compute the exact percentage by which this under-sizes
the battery, and say whether it matters here.

**E7.** Name the one current that is missing from `power_supply_sizing`'s answer and say where you
would find it.

---

## Part F — Adversary path and timely detection (lesson 08)

**F1.** Build the path. Compute `T_T`, `T_D`, and `T_A`. Evaluate against the 660 s response and
the 120 s margin. State the verdict and the deficit.

**F2.** Compute the **required detection point**. Identify which task the adversary is executing
at that instant. State in one sentence what that result is telling you to build.

**F3.** *The obvious fix.* Move detection to the fence — an exterior detection layer that alarms
at completion of the fence cut. Keep the 60 s assessment delay. Re-evaluate. **It does not
work.** Explain precisely why, in terms of the inequality.

**F4.** Fix F3 without adding any hardware to the path. Show the calculation that proves it works,
and state exactly what operational change you are asking the owner to make.

**F5.** Evaluate the delay lever instead: keep the original door detection and harden the cage
(CMU infill plus expanded metal, raising the cage task to 600 s). Does it work? Compare it with
your F4 answer on grounds other than arithmetic.

**F6.** Evaluate the response lever: what response time exactly hits the boundary? Show that the
boundary value is reported as **marginal**, not timely, and defend that behaviour as a design
choice in the calculator.

**F7.** State the fourth lever, apply it to this site concretely, and estimate what it would cost
relative to the other three.

**F8.** Name three assumptions in this path model that would change the verdict if wrong, and say
which one you would spend money to reduce first.

---

## Part G — The integration

This is the part that cannot be done from any single lesson.

**G1.** Draw the dependency chain for this design: which Part's output was an input to which other
Part. Mark every place where a decision in an earlier Part changed a number in a later one.

**G2.** Take the **single** camera added by your A4 fix — the gate identification camera. Trace
that one device all the way through: peak bandwidth, average bandwidth, 30-day storage, RAID 6
raw capacity, switch port, switch watts, and whether it changed the switch split or the growth
limit from C4. Give the number at each step. Then do the same for **one** camera added by A5 and
explain why the two cameras cost different amounts.

**G3.** Suppose the client cuts the budget and asks you to drop the vault cage retention from 90
days to 30. Compute the storage saving. Then state, in one sentence, why you would push back
anyway.

**G4.** Of every calculation in this exercise, **which single number is your design most sensitive
to, and which are you least confident in?** They are not the same number. Say what you would do
about the gap between them.

**G5.** Write the **basis of design memo** — two pages, addressed to the client's project manager,
who is not an engineer.

It must contain:

1. What the system does, in requirement terms, in one paragraph.
2. The camera schedule as corrected, with the two failures from Part A stated plainly and the
   fix for each.
3. The storage figure as a **range**, with the sentence from B4.
4. The switch arrangement and the growth limit from C4, stated in cameras rather than watts.
5. The one conductor change from Part D, with the sentence you would put on the drawing so a
   contractor does not value-engineer it back out.
6. The battery and supply selection, with the `[CODE][VERIFY]` standby duration flagged as an
   open item and named as a decision the client must close.
7. The timeliness finding and your recommendation, including the option you did **not**
   recommend but the client will probably want.
8. A list of every assumption you made and every item you tagged `[VERIFY]`, as a numbered
   register with an owner against each.

**No number in this memo may appear without its units or, where relevant, its range.**

---

## What good looks like

A strong submission is recognisable by four things:

1. **The failures are foregrounded, not buried.** The two optics failures, the switch overrun,
   the conductor, and the timeliness gap appear in the memo's first page, not in an appendix.
2. **Ranges where ranges are honest, point values where they are not.** Storage gets a range.
   A conductor gauge does not.
3. **The `[VERIFY]` register is real.** It names the document, the edition, and the person who
   has to close it — not "verify with AHJ."
4. **The dependency chain in G1 is right.** This is the actual test. Anyone can run the
   calculator; the engineer is the one who knows that the lens change moved the storage number.

A weak submission computes all thirty-something values correctly, presents them as a table, and
never notices that the design does not work.

---

## Where this goes next

- [`../../27_Labs/`](../../27_Labs/) — the projects that build on this
- [`../../02_Risk_Assessment/`](../../02_Risk_Assessment/) — where Part F becomes a full path
  analysis across multiple paths, not just the one you were handed
- [`../../17_Construction_Documents/`](../../17_Construction_Documents/) — where the memo in G5
  becomes a basis-of-design section in a real submittal
- [`../../16_Automation/data_model/`](../../16_Automation/data_model/) — where the device
  schedule becomes a validated register

> Answers and full worked reference:
> [`../_solutions/integrated_sizing_reference.md`](../_solutions/integrated_sizing_reference.md).
> Do not open it until you have a completed worksheet. The reference is worth far more as a
> comparison than as a source.
