# Quiz 35 — Doors and Hardware

**Take this COLD, before reading Module 35.** You will do badly. That is the design — failed
retrieval primes learning far better than confident reading does. Then retake it after the
module and compare.

**Format:** 30 questions. 20 vocabulary and concepts, 6 scenario, 4 calculation.
**Time:** 45 minutes. **Target on retake:** ≥ 80%, and ≥ 90% on the calculations.

Answers and full explanations:
[`_answer_keys/quiz_35_answers.md`](_answer_keys/quiz_35_answers.md).
**Write your answers down before you open it.**

> ⚠️ Several questions touch code requirements. The correct answer to any of them is never a
> number recalled from memory — it is the reasoning plus a statement of what you would look up.
> The answer key scores you on that.

---

## Part A — Vocabulary and concepts (1 pt each)

**1.** What is the "unit of design" at a door, and name its five components.

**2.** A frame is delivered flat in three pieces and snaps onto a finished stud wall. What is it
called, and what is its security consequence?

**3.** What does a **deadlatch** do, and what condition makes it stop working without anything
looking wrong?

**4.** On a pair of doors with an overlapping astragal, what component forces the leaves to close
in the correct order, and what happens without it?

**5.** State the handing convention in one sentence.

**6.** What does "reverse" mean in LHR / RHR?

**7.** Standing in the corridor outside an IT closet, the hinges are on your left and the door
swings into the closet. What is the handing?

**8.** A card reader should be mounted on which side of the opening, and on which jamb? Why the
jamb answer?

**9.** What goes wrong if a request-to-exit motion sensor is mounted on the unsecured side?

**10.** Name the five electrified locking families and state the mechanism by which each provides
free egress.

**11.** Which locking family has no mechanical egress, and name three things its use therefore
requires you to add.

**12.** Which locking families require a power transfer into the leaf?

**13.** What is the "deadbolt trap" with an electric strike?

**14.** Define fail safe and fail secure. What does each word refer to?

**15.** Why does fail secure **not** trap anyone at an electrified lockset?

**16.** Why must a fire alarm release be a hardwired path rather than a software integration
between the fire alarm and access control head-ends? Give two reasons.

**17.** State the free egress principle. What is "one motion" protecting against?

**18.** Free egress is a *one-directional* constraint. What does that let you do, and why does it
resolve most "lock the exit" requests?

**19.** A fire door must positively latch. Name three hardware consequences that follow directly
from that requirement.

**20.** What is a **control key** in an SFIC system, and what is the rekey scope when one is lost?

---

## Part B — Scenario (2 pts each)

**21.** An IT closet has a solid-core wood door, a KD frame, a single-layer drywall partition,
and a suspended ceiling that runs continuously over the wall into the corridor. The facilities
manager wants to install a high-security lock. State the governing weakness, explain why the lock
is not the answer, and give the cheapest intervention that would materially improve the
situation.

**22.** A drawing set specifies magnetic locks at 22 of 61 access-controlled openings. Two are
all-glass lobby entrances. Write the substance of your review comment: what you concede, what you
ask for, and what you require at any opening that remains a mag lock.

**23.** An integrator reports that Door 214 "sometimes doesn't unlock, mostly in the afternoon."
The credential reads, the controller logs a valid grant, and the opening has an electric latch
retraction exit device 180 ft from the panel. Name the three things you check first and say what
each rules in or out. Name one thing you would deliberately **not** check first, and why.

**24.** A retail client is losing merchandise through a rear exit that discharges to an alley.
They want it locked. State the constraint in one sentence, then give three options with what each
does and does not solve.

**25.** Two weeks before turnover you find that six 90-minute rated stair door frames have been
field-drilled to install recessed door position switches. The switches work. State the finding,
why it is worse than a visible violation, and your first two actions.

**26.** A client has just spent $400,000 on an access control system and asks what else they
should buy. Give your answer, and explain the mechanism that makes it the right one.

---

## Part C — Calculation (3 pts each)

**27.** 🧮 A floor has 10 electrified locksets at 0.32 A each, 5 electric strikes at 0.20 A each,
and 1 exit device with electric latch retraction at 0.30 A standby / 3.50 A peak. All 24 VDC.

- (a) Compute standby current and peak current.
- (b) Which one governs the power supply rating, and why?
- (c) Compute the recommended supply at 25% headroom.
- (d) Name one thing this number does **not** include.

**28.** 🧮 Using the same loads, size the battery for a 4-hour standby requirement, using a 1.25
discharge derate and a 1.25 aging factor.

- (a) Compute the required capacity.
- (b) Which current — standby or peak — drives this calculation, and why is it the opposite of
  question 27?
- (c) What is wrong with treating "4 hours" as an engineering choice?

**29.** 🧮 A device draws 2.0 A. The home run from the power supply to the frame is 150 ft. The
power transfer and leaf run add 6 ft of 24 AWG. Supply is 24.0 VDC. Assume the device requires a
minimum of 21.0 V.

- (a) Compute the drop through the 6 ft transfer segment.
- (b) Compute the total drop and the voltage at the device for 18, 16, and 14 AWG home runs.
- (c) Which home run conductor do you specify?
- (d) Would you have reached the same answer if you had stopped your calculation at the frame?
  Show it.

**30.** 🧮 An opening will have an electrified mortise lockset with latch bolt monitoring, an
integral request-to-exit lever switch, and deadbolt monitoring.

- (a) Budget the conductors, showing each function.
- (b) What do you specify, and why is it not the number in (a)?
- (c) A colleague proposes adding a second card reader on the secure side and asks whether the
  transfer needs more conductors. Answer them.

---

## Scoring

| Part | Questions | Points |
|---|---|---|
| A | 1–20 | 20 |
| B | 21–26 | 12 |
| C | 27–30 | 12 |
| | | **44** |

**≥ 80% (36/44)** on the retake means you can be handed an opening and trusted with it.
**≥ 90% on Part C (11/12)** matters more than the total. The calculations are the part that
either works in the building or doesn't.

If you score below 50% cold, that is the expected result and it is doing its job.
