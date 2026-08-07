# Quiz 01 — Foundations

**Take this COLD, before reading Module 01.** You will do badly. That is the design — failed
retrieval primes learning far better than confident reading does. Then retake it after the
module and compare.

**Format:** 30 questions. 20 multiple choice / short answer, 6 scenario, 4 calculation.
**Time:** 45 minutes. **Target on retake:** ≥ 80%, and ≥ 90% on the calculations.

Answers and full explanations: [`_answer_keys/quiz_01_answers.md`](_answer_keys/quiz_01_answers.md).
**Write your answers down before you open it.**

---

## Part A — Vocabulary and concepts (1 pt each)

**1.** Which is a *hazard* rather than a *threat*?
- (a) A former employee with a grudge and a retained badge
- (b) A hundred-year flood
- (c) An organized retail theft crew
- (d) An insider diverting inventory

**2.** "The rear door has no position switch and is not visible from any staffed location."
This statement names a:
- (a) Threat  (b) Hazard  (c) Vulnerability  (d) Risk

**3.** Complete: "Security systems do not prevent bad outcomes. They ________ and ________."

**4.** Who accepts residual risk?

**5.** Name the four risk treatment options. Which one does insurance perform, and what does
insurance specifically *not* do?

**6.** Why must a vulnerability always be stated relative to a specific threat?

**7.** A camera that records but is not monitored performs which protection functions?
List all that apply and mark each as primary or secondary.

**8.** State the timely detection inequality using the symbols `T_T`, `T_D`, `T_R`.

**9.** Why is delay that occurs *before* detection nearly worthless?

**10.** Name the three parts of a detection event. What happens if the third is missing?

**11.** A perimeter sensor system has an excellent datasheet `P_d` of 0.95 but generates
40 nuisance alarms per night. What is its *effective* probability of detection after three
months of operation, and why?

**12.** Name three requirements a camera must meet to genuinely perform the *assess* function.

**13.** Distinguish **redundancy** from **diversity**. Which is more valuable against a
thinking adversary, and why?

**14.** What is **graceful degradation**, and why must it be specified at design time rather
than configured later?

**15.** What is **balanced protection**? Give the canonical example of violating it.

**16.** Name the six CPTED strategies.

**17.** Why does CPTED literature list target hardening *last*?

**18.** What is the "convenience door" problem, and why can a door alarm not fix it?

**19.** Name the four requirement types. Which is most often omitted, and what goes wrong
when it is?

**20.** Rewrite as a testable requirement: *"Provide adequate camera coverage of the loading
dock."* State any assumption you need.

---

## Part B — Scenario analysis (3 pts each)

**21.** A client says: *"We've had three laptop thefts in 18 months. All during business
hours. No forced entry. We want cameras."*
- (a) What do the facts most strongly suggest about the threat?
- (b) Give your first three questions.
- (c) Will cameras address this? Answer honestly and completely.

**22.** A 30,000 sq ft office. The server room has a card reader, a solid-core door with a
Grade 1 lock, and partition walls that stop at the suspended ceiling grid. The client wants
to add biometric authentication at the door.
- (a) What principle is being violated?
- (b) Estimate the actual delay this boundary provides against an adversary with no tools.
- (c) What would you recommend instead, and how would you say it to a client who has already
  budgeted for the biometric reader?

**23.** A site installs 40 perimeter fence sensors with no exterior cameras. Response is
police dispatch. Predict, in sequence, what happens over the following six months, and name
the protection function whose absence causes it.

**24.** During design, IT states that all multicast will be blocked network-wide as a matter
of policy. The VMS design uses multicast to feed a video wall.
- (a) What category of failure is this (from the nine-category taxonomy)?
- (b) Why is it classified as *emergent*?
- (c) What should have happened during design to prevent it?

**25.** An access control system enforces anti-passback. A reader fails on an egress door;
users exit through an unread door. Describe what happens the next morning and what it teaches
about the relationship between a correctly functioning control and a security outcome.

**26.** Your design produces 60 exterior cameras with analytics, averaging 8 alerts/day each.
The SOC has one operator per shift. The SOP requires 90 seconds of review per alert.
- (a) Compute the daily alert volume and the operator time required.
- (b) Express that as a fraction of a 24-hour staffed day.
- (c) Is this design viable? Give three fixes and recommend one.

---

## Part C — Calculations (4 pts each)

**27.** 🧮 An adversary path to a cash room:

| Task | Delay (s) |
|---|---|
| Defeat exterior door | 120 |
| Cross lobby | 25 |
| Defeat suite door | 60 |
| Cross office floor | 40 |
| Defeat cash room door | 180 |
| Open safe | 300 |

Detection occurs at completion of the **suite door** task. Assessment takes 25 s. Response
force time is 420 s.
- (a) Compute `T_T`, `T_D`, `T_A`, and the margin.
- (b) Is the system timely?
- (c) What is the latest `T_D` that would still be timely with a 90 s confidence margin?
- (d) Which task is the adversary performing at that time, and what does that tell you about
  where to relocate detection?

**28.** 🧮 Same path. The owner replaces the on-site guard with a contract patrol,
`T_R = 1500 s`.
- (a) Recompute the margin.
- (b) How much *additional delay after the detection point* would be needed for timeliness
  with zero margin?
- (c) Is that achievable? What do you recommend instead, and how do you frame it to the owner?

**29.** 🧮 A boundary has four penetration paths with these delays against your stated
adversary: door 180 s, window 25 s, wall 240 s, ceiling plenum 45 s.
- (a) What is the boundary's actual delay?
- (b) Your timely-detection analysis requires 150 s at this boundary. What is the minimum set
  of changes?
- (c) After fixing those, what is the new boundary delay, and what is the next thing you'd
  spend money on?

**30.** 🧮 A design has 6 zones. Zone 4 (server room) is protected by: badge reader, camera at
the door, DPS, and motion detection inside when unoccupied. The building has one access
control server (no failover), one recording server, one PoE switch per floor, and one MDF.
- (a) List every single point of failure.
- (b) For each, state what stops working.
- (c) Rank your mitigations by cost-effectiveness and justify the top two.

---

## Scoring

| Part | Questions | Points |
|---|---|---|
| A | 1–20 | 20 |
| B | 21–26 | 18 |
| C | 27–30 | 16 |
| **Total** | | **54** |

| Score | Reading |
|---|---|
| < 27 (50%) | Expected on a cold take. Study the module. |
| 27–37 | Vocabulary is landing; reasoning is not yet automatic. Redo the exercises. |
| 38–48 | Working competency. Move on; revisit the missed areas in a month. |
| 49+ | Strong. Make sure the calculations were all correct — those carry the most weight in real work. |

**Whatever you score, read every answer explanation, including for questions you got right.**
Getting the right answer for the wrong reason is the most dangerous outcome in this field, and
it is invisible unless you check.
