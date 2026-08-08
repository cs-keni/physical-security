# Exercises — Module 01 Foundations

Two things live here: an **index** of the exercises embedded in each lesson, and the **module
capstone** — one site that requires all seven lessons at once.

Do the per-lesson exercises as you go. Do the capstone last.

---

## Per-lesson exercises

| Lesson | Exercises | Solutions |
|---|---|---|
| [01 — What PSE is](01_what_is_physical_security_engineering.md) | 🔧 Field exercise: one asset, six questions, on a real site. Plus the retrieval check. | *(Field exercise — no key. Keep the write-up; you redo it in month 6.)* |
| [02 — The Risk Vocabulary](02_the_risk_vocabulary.md) | 8 practice problems: name the term, state what you'd need. Then the full chain for two of them. | [`_solutions/02_risk_vocabulary_solutions.md`](_solutions/02_risk_vocabulary_solutions.md) |
| [03 — The Functional Chain](03_functional_chain.md) | E3.1 missing-function diagnosis (5 cases) · **E3.2 🧮 timely detection** · E3.3 function mapping · E3.4 the 100-word explanation | [`_solutions/03_functional_chain_solutions.md`](_solutions/03_functional_chain_solutions.md) |
| [04 — Defense in Depth and Zones](04_defense_in_depth_and_zones.md) | E4.1 zone diagram · E4.2 integrity checklist · E4.3 SPOF enumeration · E4.4 the $50k door | [`_solutions/04_zones_solutions.md`](_solutions/04_zones_solutions.md) |
| [05 — CPTED](05_cpted.md) | E5.1 full 7-step analysis · E5.2 six conditions · E5.3 the glass lobby · E5.4 allocate $15,000 | [`_solutions/05_cpted_solutions.md`](_solutions/05_cpted_solutions.md) |
| [06 — Requirements Engineering](06_requirements_engineering.md) | E6.1 vague → testable · E6.2 four pathologies · E6.3 Project 1 requirement set · E6.4 the submittal · E6.5 the budget cut | [`_solutions/06_requirements_solutions.md`](_solutions/06_requirements_solutions.md) |
| [07 — Systems and Failure Thinking](07_systems_and_failure_thinking.md) | E7.1 intrusion chain · E7.2 PoE switch FMEA · E7.3 five emergent failures · E7.4 nine categories on one door · **E7.5 🧮 the analytics workload** | [`_solutions/07_systems_failure_solutions.md`](_solutions/07_systems_failure_solutions.md) |
| **Capstone (below)** | One site, all seven lessons, Parts A–G | [`_solutions/exercises_solutions.md`](_solutions/exercises_solutions.md) |

**Also:** [`../25_Quizzes/quiz_01_foundations.md`](../25_Quizzes/quiz_01_foundations.md) — 30
questions, with an isolated key. Take it cold, then again after.

---

# 🔧 Capstone — Ashford Public Library

**Time:** 3–4 hours. **Prerequisite:** lessons 01–07.
**Deliverable:** a completed worksheet plus a two-page memo to a non-technical client.
**Reference solution:** [`_solutions/exercises_solutions.md`](_solutions/exercises_solutions.md)

## Why this site

Every worked example in this module has been a warehouse, an office, or a server room — places
where hardening is culturally acceptable and the assets are property.

**A library is the opposite of all of that**, and it is a much better test. Its mission is
unrestricted public access. Its most valuable asset is its staff, not its collection. Its
users include people with nowhere else to go. Almost every instinct this module has given you
produces the wrong answer here, and the exercise is finding out which instincts survive.

> The site is **synthetic**. It is a composite written to exercise the module, not a description
> of a real facility.

---

## The site

**Ashford Public Library** — a 2-storey branch, 24,000 sq ft, built 1994, renovated 2009.
Open 0900–2000 weekdays, 0900–1700 Saturday, closed Sunday. Staff of 14, typically 5 on duty,
2 after 1800.

```
                              N
   ┌──────────────────────────────────────────────────────────────┐
   │  Rear service yard  (loading, refuse enclosure, staff door)  │
   │        ┌───────────────────────────────────────────┐         │
   │        │  FLOOR 2   Reference · Study rooms ·       │         │
   │        │            SPECIAL COLLECTIONS [SC]        │         │
   │        ├───────────────────────────────────────────┤         │
   │        │  FLOOR 1   Lobby · Circulation desk [CD] · │         │
   │        │            Stacks · Children's · Computers │         │
   │        │            Community room · Staff area     │         │
   │        └───────────────┬───────────────────────────┘         │
   │                     main entrance                            │
   │  ┌────────────────────────────────────────────────────────┐  │
   │  │            PARKING  — 60 spaces, unlit east end        │  │
   │  └────────────────────────────────────────────────────────┘  │
   └──────────────────────────────────────────────────────────────┘

   [CD] circulation desk — set 45 ft back from the entrance, facing the stacks
   [SC] special collections — local history archive, floor 2, at the end of a
        dead-end corridor past the study rooms
```

### What the client has told you

The Library Director has asked for "a security assessment and a proposal." In the kickoff
meeting you were told, in this order:

1. *"Staff don't feel safe at the desk anymore."* Three verbal-aggression incidents in the last
   year; one where a staff member was followed to their car. No injuries. The desk is 45 ft from
   the entrance, facing the stacks, with the entrance behind the staff member's shoulder.
2. *"We had a break-in last spring."* Rear service door forced overnight; a laptop and petty
   cash taken. Discovered at opening. The 2009 intrusion system did alarm; the central station
   called the after-hours list and reached nobody.
3. *"The special collections room worries our board."* A local-history archive: original maps,
   photographs, and three 18th-century deeds. **Irreplaceable, and appraised at $340,000.** The
   room has a keyed lock and no monitoring. It is opened on request by a staff member.
4. *"Evening staff won't park at the east end."* The east end of the lot is unlit; two pole
   fixtures have been out for over a year.
5. *"The board is asking about cameras."* There are four, installed 2009, recording to a DVR in
   the staff area at 3 fps with 5 days of retention. Nobody has retrieved footage successfully.
6. *"We have about $60,000, and it has to last."*

### Additional facts from your site visit

- The rear service door has a keyed cylinder, no position switch, no camera, and a worn strike.
  It opens onto a service yard screened from the street by a 6-ft masonry refuse enclosure.
- The stair from floor 1 to floor 2 is open and unmonitored.
- The special collections corridor has no sightline from any staffed position.
- The community room has its own exterior door, used for evening events, propped routinely.
- The 2009 intrusion system covers the lobby and the staff area with motion detectors. Nothing
  covers floor 2.
- The after-hours call list has not been updated since 2019.
- Police response to this address, per the department's published figure, is **10 minutes** for
  a verified alarm and **15 minutes** for an unverified one. `[VERIFY — this is a quoted figure]`
- Library policy prohibits any measure that would restrict public access to the collection or
  require identification to enter.

### Design-basis adversary, for Part B

> Two outsiders, hand tools, prior familiarity with the building as ordinary visitors. Targeting
> special collections after hours. Willing to work about 15 minutes.

| Task | Delay |
|---|---|
| Approach rear service yard | 45 s |
| Force rear service door | 120 s |
| Cross ground floor to stair | 40 s |
| Ascend to floor 2 | 25 s |
| Force special collections door | 90 s |
| Locate and remove items | 420 s |

Detection as it exists: **lobby motion detector**, at completion of the ground-floor crossing.
Assessment: **90 s** (central station calls the after-hours list). Required confidence margin:
**60 s**.

> These task times are **illustrative**, not tested penetration data. `[PRACTICE][VERIFY]` Treat
> them as given and say so in your memo.

---

## Part A — Frame the problem (lessons 01, 02)

**A1.** Answer the four questions for this site. There is more than one asset; rank them and
justify the ranking.

**A2.** The Director listed six items. **Re-rank them by risk**, and explain every place your
ranking differs from theirs. Name what you would need to know to be more confident.

**A3.** For item 1 (staff safety) and item 3 (special collections), trace the full chain: asset →
threat/hazard → vulnerability → event → consequence → countermeasure by function → residual risk.

**A4.** One of the six items is a **hazard**, not a threat, and one is a **solution masquerading
as a requirement**. Identify both and say what changes as a result.

**A5.** State which risks you would recommend **accepting**, and say who accepts them.

---

## Part B 🧮 — Timely detection (lesson 03)

**B1.** Compute `T_T`, `T_D`, and `T_A` for the path as it exists. Evaluate against the 10-minute
verified-alarm response and the 60 s margin. State the verdict and the shortfall.

**B2.** Compute the **required detection point**. Which task is the adversary executing at that
instant?

**B3.** Now evaluate the response at **15 minutes** (unverified alarm). Compute the required
detection point again. What does the sign of that number tell you, and what should you stop
doing as a result?

**B4.** Work the detection lever in three steps, keeping the 10-minute response throughout:

- (a) Move detection to a **contact on the rear service door**, keeping the 90 s assessment.
- (b) Same contact, with assessment reduced to **20 s** (video verification at the central
  station).
- (c) Move detection to the **service yard**, with 20 s assessment.

Report the verdict at each step. Two of the three fail. **State precisely why (a) gains so
little**, and what that says about which term is really binding.

**B5.** Now ignore detection entirely and work the **delay** lever: the highest-value items go
into a certified safe inside the special collections room, raising the removal task from 420 s to
900 s. Keep the original lobby detection and the 90 s assessment. Evaluate.

**B6.** Compare B4(c) and B5 on grounds other than arithmetic. Which do you recommend for **this
client**, and why does the answer differ from what you would recommend for a warehouse?

**B7.** Name the two assumptions in this analysis that would change the verdict if wrong, and say
which you would spend money to reduce first.

---

## Part C — Zones and boundaries (lesson 04)

**C1.** Draw the zone diagram. A library's Zone 1 is unusual — say what it is and why.

**C2.** Run the nine-element integrity check on **special collections**. Mark every item you
cannot answer from the information given; those are survey questions.

**C3.** Identify every SPOF in the existing system. One of them is not equipment.

**C4.** The community room's exterior door is propped routinely. Classify this: is it a zone
integrity failure, a human error, or a design failure? Defend your answer.

---

## Part D — The environment (lesson 05)

**D1.** Apply the six CPTED strategies to this site. Produce at least six findings in the
required format (location, affected users, mechanism, costed recommendation).

**D2.** The circulation desk is 45 ft back from the entrance, facing the stacks. State the
problem in CPTED terms and propose a fix. **Constraint: the library will not accept anything
that reads as a security checkpoint.**

**D3.** The east end of the lot is unlit. Give the immediate fix and its cost, and state what you
would `[VERIFY]` afterwards.

**D4.** Name two conditions on this site where CPTED provides **little or no benefit**, and say
what does.

---

## Part E — Requirements (lesson 06)

**E1.** Convert the Director's six statements into a testable requirement set. Aim for 12–16
requirements across all four types, with none empty.

**E2.** Two of the Director's statements contain requirement pathologies. Identify and rewrite
them.

**E3.** Write the RTM rows for your five highest-priority requirements, including the
test-procedure column.

**E4.** Library policy prohibits any measure restricting public access to the collection. Express
this as a **constraint requirement**, and name two otherwise-reasonable countermeasures it
eliminates.

---

## Part F — Failure (lesson 07)

**F1.** The 2009 intrusion system alarmed correctly and nobody came. Trace the full chain and
identify **exactly** where it failed. Which of the nine categories is it?

**F2.** Run the informal FMEA on your proposed special collections protection. Include the
"who detects it and how fast" column, and make sure at least two rows say *never*.

**F3.** The DVR records at 3 fps with 5 days of retention, and nobody has ever retrieved footage
successfully. Name **three separate failures** here, in three different categories.

**F4.** Identify one **emergent failure** on this site — where no component is faulty and the
system still fails — and name the interface it originates at.

---

## Part G — The deliverable

**G1.** Allocate the **$60,000**. Itemize, sequence, and state the risk consequence of everything
you chose not to fund.

**G2.** State plainly which of the Director's six concerns your proposal does **not** address,
and why.

**G3.** Write the **two-page memo** to the Director, who is not an engineer and who has to
present it to a board.

It must contain:

1. What you found, in order of risk, in one paragraph.
2. The staff safety finding first, with a fix, in language a board will fund.
3. The special collections finding, with the arithmetic translated into plain English — including
   the fact that **detection alone cannot solve it**.
4. The $60,000 allocation, with each item's purpose in one clause.
5. What you are **not** recommending, and why. Include at least one thing they asked for.
6. What they must do that costs nothing.
7. Your assumption and `[VERIFY]` register, with an owner and a date against each.

**No number in the memo may appear without its units or, where relevant, its range. No jargon
from this module may appear at all.**

---

## What good looks like

1. **The Director's ranking is challenged, respectfully and with reasons.** Their list opens with
   staff safety and ends with money; the risk ranking is not the same list, and saying so is the
   job.
2. **At least one recommendation costs nothing.** Updating the after-hours call list is free and
   is arguably the single highest-value item on the entire site.
3. **At least one thing they asked for is declined.** They asked about cameras. A strong answer
   funds very few of them and explains why.
4. **The library's mission constrains the design, and it is treated as a requirement rather than
   an obstacle.** An answer that recommends restricting access has failed, however sound the
   security reasoning.
5. **The memo is readable by a board.** No PPF, no `T_R`, no "defense in depth."

A weak submission produces a competent security design for a building that happens to contain
books.

> Reference solution: [`_solutions/exercises_solutions.md`](_solutions/exercises_solutions.md).
> Do not open it until you have a completed worksheet.
