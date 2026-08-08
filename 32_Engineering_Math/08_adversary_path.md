# 08 — Adversary Path and Timely Detection

> Derives [`../28_Calculators/psec/pps.py`](../28_Calculators/psec/pps.py), which implements the
> model taught conceptually in
> [`../01_Foundations/03_functional_chain.md`](../01_Foundations/03_functional_chain.md).
>
> **Read that lesson first if you haven't.** This one assumes you know *why* detection must
> precede delay; it derives the arithmetic that tells you *where*.

## Learning objectives

- Define `T_T`, `T_D`, `T_A`, and `T_R` precisely, and state the timeliness inequality.
- Explain why detection is placed at task **completion** rather than at task start, and why that
  is the conservative choice.
- Invert the inequality to compute the **required detection point** — how a detection layer gets
  located by calculation rather than by habit.
- Explain the three verdicts (timely / marginal / not timely) and why marginal is treated as not
  timely.
- Compute the deficit and reason about the four intervention levers, including why the fourth one
  is not a term in the equation.
- State the model's limits precisely enough to know when not to use it.

---

## The four quantities

```
   T_T   TOTAL TASK TIME
         From the start of the adversary's sequence to completing the act at the asset.
         The sum of all task delays on the path.

   T_D   DETECTION TIME
         From sequence start to detection AND ASSESSMENT.
         Detection alone is not enough — somebody has to know what it was
         before a response can be initiated.

   T_A   ADVERSARY TIME REMAINING  =  T_T − T_D
         The delay left after you know they're there. This is the only delay
         that does any work.

   T_R   RESPONSE FORCE TIME
         From annunciation to the responder being in a position to interrupt.
```

```
   ┌──────────────────────────────────────────────────┐
   │   The system is TIMELY  ⟺   T_A  >  T_R          │
   │                                                    │
   │   equivalently:   (T_T − T_D)  >  T_R             │
   └──────────────────────────────────────────────────┘
```

**In words: the delay remaining after you detect must exceed the time it takes to respond.**

```
   t=0                    T_D                                    T_T
    │                      │                                      │
    ├──────────────────────┼──────────────────────────────────────┤
    │   before detection   │        T_A  (remaining delay)        │
    │   (buys nothing)     │                                      │
                           ├──────────────────┤
                           │   T_R (response) │  margin = T_A − T_R
                           └──────────────────┘
```

**Everything to the left of `T_D` is delay you paid for and did not use.** That single geometric
fact is the whole model.

---

## Derivation 1 — The quantities from a task list

An adversary path is an ordered list of tasks, each with a delay. Detection is marked on the task
at whose **completion** it occurs.

```
   T_T  =  Σ delay_i                                    over all tasks

   T_D  =  Σ delay_i  (up to and including the detected task)  +  assessment_delay

   T_A  =  T_T − T_D
```

### Why detection at task completion, not task start

**This is a deliberate conservative choice and it is worth understanding.**

A door position switch reports when the door **opens** — that is, when the task "force the dock
door" is *complete* — not when the adversary first puts a pry bar on it. Placing detection at
completion assumes you learn about the intrusion as late as the sensor could plausibly tell you.

Placing it at task start would credit you with the entire duration of the task as post-detection
delay, which for a 150-second door is a large and unearned gift.

> 🧠 **Where the choice would be wrong:** a sensor that genuinely detects the *attempt* — a
> vibration or shock sensor on the door, a video analytic on approach — does detect at or near
> task start. If you have one, model it by splitting the task: an "approach and set up" task that
> is detected, followed by the "force" task that isn't. **Don't change the convention; change the
> task list.** The convention is what makes different analyses comparable.

### Why assessment is added to `T_D`

Detection tells you *something happened*. Assessment tells you *what*, and until someone knows
what, nobody dispatches. The operator's time to pull up the camera, look, and decide is real and
it is on the critical path.

**It is also the term people omit**, because it isn't a device with a price. Twenty seconds sounds
trivial; in worked example 8.1 it is 4% of the entire post-detection budget, and on a fast path it
can be most of it.

---

## 🧮 Worked example 8.1 — the reference case

A warehouse, north dock. Adversary: **two persons, hand tools, willing to be seen briefly.**
Assessment delay: **20 s.**

| # | Task | Delay | Cumulative | Detected? |
|---|---|---|---|---|
| 1 | Climb fence | 20 s | 20 | |
| 2 | Cross yard | 40 s | 60 | |
| 3 | Force dock door | 150 s | 210 | ✅ DPS + camera |
| 4 | Traverse floor | 60 s | 270 | |
| 5 | Cut cage | 200 s | 470 | |
| 6 | Load goods | 240 s | 710 | |

```
   T_T  =  20+40+150+60+200+240           =  710 s
   T_D  =  (20+40+150)  +  20 assessment  =  230 s
   T_A  =  710 − 230                      =  480 s
```

These are `test_total_task_time`, `test_detection_time_includes_assessment`, and
`test_time_remaining`.

**Now evaluate against three response postures:**

| Response | `T_R` | Margin = `T_A − T_R` | Verdict |
|---|---|---|---|
| On-site guard | 300 s | **+180 s** | ✅ **TIMELY** |
| Contract patrol | 1800 s | **−1320 s** | ❌ **NOT TIMELY** — short by 22 minutes |
| Guard, but requiring 120 s confidence margin | 420 s | +60 s | ⚠️ **MARGINAL** — treated as not timely |

These are `test_timely_with_onsite_guard`, `test_not_timely_with_contract_patrol`, and
`test_marginal_is_treated_as_not_timely`.

> ⚠️ **The contract patrol result is the normal situation for most commercial sites**, and the
> honest conclusion is: *this system does not interrupt the event; it documents it.* That is a
> legitimate design — evidence and insurance recovery are real objectives — but it must be a
> **chosen** objective, stated out loud, not an accident discovered after a loss.

---

## Derivation 2 — The three verdicts

```
   timely   ⟺   margin > required_margin

   if timely:              "TIMELY"
   elif margin > 0:        "MARGINAL"     ← still treated as NOT timely
   else:                   "NOT TIMELY"
```

**Why `required_margin_s` exists.** Every input to this model is an estimate: delay values are
assumed, response times are self-reported, assessment time is a guess. **Designing to a zero
margin means designing to fail half the time.** Ask for a margin proportionate to your
uncertainty.

**Why marginal is a separate verdict rather than just "not timely."** The distinction carries
information for the reader: *"you have 60 seconds of real margin but I asked for 120, so I am not
willing to call this effective"* is a different message from *"you are 22 minutes short."* The
first is a conversation about confidence; the second is a conversation about strategy.

The verdict strings say so explicitly — the marginal case ends with **"Treat as not timely."**

### The undetected path

If no task is marked detected, `T_D` is `None` and so are `T_A` and the margin.

```
   "NO DETECTION ON THIS PATH. The system cannot interrupt; it can only
    document after the fact."
```

This is `test_no_detection_path`. **Note that it returns `None` rather than infinity or zero.**
`None` is the honest encoding: the quantity does not exist, and any number would invite arithmetic
that means nothing. The verdict string carries the meaning instead.

---

## Derivation 3 — The required detection point

**This is the design direction**, and it is the most useful thing in the lesson.

Rearrange the inequality for `T_D`:

```
   T_A > T_R + margin
   T_T − T_D > T_R + margin

   ┌──────────────────────────────────────────────┐
   │   T_D_max  =  T_T − T_R − margin             │
   └──────────────────────────────────────────────┘
```

### 🧮 Worked example 8.2 — the test case

The warehouse path, on-site guard (`T_R = 300 s`), requiring a 60 s confidence margin:

```
   T_D_max = 710 − 300 − 60 = 350 s
```

This is `test_required_detection_point`.

**Detection must occur within the first 350 seconds of the adversary sequence.** Now walk the
timeline and find which task the adversary is executing at t = 350 s:

| Task | Start | End |
|---|---|---|
| Climb fence | 0 | 20 |
| Cross yard | 20 | 60 |
| Force dock door | 60 | **210** |
| Traverse floor | 210 | 270 |
| **Cut cage** | **270** | **470** ← t = 350 falls here |
| Load goods | 470 | 710 |

**At t = 350 s the adversary is cutting the cage.** So detection must be at or before the cage —
and the existing detection at the dock door (t = 230) is comfortably earlier.

`test_detection_before_required_point_is_timely` asserts exactly this relationship: `T_D < cutoff`
implies `timely`.

> 🧠 **This is how a detection layer gets located by calculation instead of by habit.** Not "put
> sensors on the perimeter because that's where sensors go," but: *compute the latest detection
> point that still works, walk the path to find which barrier the adversary reaches at that time,
> and place detection at or before it — subject to the constraint that you must be able to
> **assess** there.* That constraint is what stops the answer from always being "the property
> line."

The `timeline()` function exists to support exactly this walk: cumulative start and end times per
task, contiguous by construction (`test_timeline_is_cumulative_and_complete` asserts every task's
end equals the next task's start, and that the last ends at `T_T`).

---

## Derivation 4 — The deficit and the four levers

When a path is not timely, **how much are you short?**

```
   deficit  =  T_R + margin  −  T_A
```

### 🧮 Worked example 8.3 — the test case

Warehouse path, contract patrol (`T_R = 1800 s`), zero margin:

```
   deficit = 1800 + 0 − 480 = 1320 s
```

This is `test_compare_interventions_offers_all_four_levers`.

### The four levers

Three of them move a term in the inequality. The fourth doesn't, and it is the important one.

| Lever | What it changes | The catch |
|---|---|---|
| **1. Earlier detection** | Reduces `T_D`, raising `T_A` | **Detection is only useful where you can assess it.** Moving detection to the property line without assessment produces nuisance-alarm hell — see the functional chain lesson. |
| **2. More delay after detection** | Raises `T_T` and hence `T_A` | **Delay added *before* the detection point buys nothing.** And delay cost rises steeply — check it against the other levers before recommending it. |
| **3. Faster response** | Reduces `T_R` | Usually **the dominant term** and usually an **owner decision**, not an engineering one. |
| **4. Reduce the consequence** | **Nothing — it isn't in the equation** | Move, reduce, or eliminate the asset so a successful attack matters less. **Frequently the cheapest option available, and the one nobody proposes.** |

**Lever 4 is not a timeliness lever.** It does not appear in `T_A > T_R`. It is included because
when the arithmetic says no achievable design is timely, the right engineering response is to
stop solving the stated problem and question it — and that option needs to be on the table
explicitly, or nobody will raise it.

### The infeasibility check

Here is the part worth studying as engineering, not just arithmetic.

```
   cutoff = T_T − T_R − margin

   if cutoff <= 0:
       → detection cannot fix this path at any placement
```

### 🧮 Worked example 8.4 — when the lever doesn't exist

Warehouse path, contract patrol, 60 s margin:

```
   cutoff = 710 − 1800 − 60 = −1150 s
```

**A negative required detection point.** Arithmetically it says "detect 1150 seconds before the
adversary arrives." That is **true and useless**.

The module detects this and says so:

> **NOT ACHIEVABLE on this path.** Timeliness would require detection at t ≤ −1150 s, i.e. before
> the adversary sequence begins. Even instantaneous detection at the property line leaves only
> 710 s against an 1800 s response. Detection alone cannot fix this — go to the response or
> consequence lever.

This is `test_compare_flags_infeasible_detection_lever`.

**Compare the feasible case** (`T_R = 500 s`, margin 60):

```
   cutoff = 710 − 500 − 60 = 150 s      ← positive, and earlier than the current T_D of 230 s
   deficit = 500 + 60 − 480 = 80 s
```

> **Move detection at least 80 s earlier in the path (T_D from 230 s to ≤ 150 s). Constraint:
> detection is only useful where you can ASSESS it.**

This is `test_compare_gives_actionable_detection_target_when_feasible`.

> 🧠 **Why this matters beyond this module.** The naive implementation emits "move detection to
> −1150 s" and is not wrong — it is just unusable, and worse, it *looks* like an answer. Somebody
> would try to act on it.
>
> **A calculation that produces an arithmetically valid but physically meaningless result should
> say so, and redirect.** That is a third option alongside "return a number" and "raise an
> exception": **return a result that names the impossibility.** It is the right choice here
> because the caller is a designer who needs to know *which lever to pull next*, not a program
> that needs an error code.
>
> This function was fixed during the initial build for exactly this reason — it originally emitted
> the negative number. See `docs/ENGINEERING_LOG.md`.

**Also note the short circuit:** if the path is already timely, `compare_interventions` returns
`{"already_timely": True, ...}` and computes no levers (`test_compare_short_circuits_when_already_timely`).
There is nothing to fix, and offering interventions anyway would imply there is.

---

## Limits of the model

**Read these before using it on anything real.** They are in the module docstring for the same
reason.

| Limit | Consequence |
|---|---|
| **Delay values are estimates against an ASSUMED adversary with ASSUMED tools** | Change the assumption, change the answer. **State it in writing, always.** A hollow metal door is ~3 minutes against hand tools and ~15 seconds against a battery angle grinder. |
| **It assumes a single linear path** | Real adversaries take the **easiest** path. Run this against the weakest path you can find, not the one you designed. Finding that path is adversary path analysis. |
| **Detection is modelled as binary and instantaneous** | Real detection is probabilistic. A rigorous treatment carries `P_d` through the whole sequence — that is what EASI-type models do. |
| **It models INTERRUPTION, not neutralisation** | Arriving is not stopping. |
| **It does not apply to insiders at all** | An authorised insider trips nothing. `T_D` is effectively infinite for barrier-based detection. Insider detection is behavioural, procedural, and audit-based. |

> ⚠️ **The single-path limit is the one that bites in practice.** A beautiful analysis of the front
> door is worthless if the roof hatch is unalarmed. The model's answer is only as good as the
> path you fed it, and choosing that path is judgment, not arithmetic.

---

## Common mistakes

⚠️ **Omitting the assessment delay.** It is on the critical path and it has no price tag.

⚠️ **Modelling detection at task start.** Credits you with delay you haven't earned.

⚠️ **Designing to a zero margin.** Every input is an estimate.

⚠️ **Treating "marginal" as a pass.**

⚠️ **Analysing the path you designed** instead of the weakest path.

⚠️ **Accepting a self-reported response time.** Ask what happens at 3 a.m. on a Sunday, in the
rain.

⚠️ **Reaching for the delay lever first.** It is usually the most expensive of the three, and
delay added before the detection point buys nothing.

⚠️ **Never mentioning lever 4.**

⚠️ **Applying the model to insider threat.**

---

## Junior vs. Senior

**Junior:** computes `T_T`, `T_D`, `T_A`, and the margin from a task list; states the inequality;
computes the required detection point and locates it on the timeline.

**Senior:** states the assumed adversary and toolset in writing alongside every result; runs the
analysis on the weakest path rather than the designed one; extracts an honest response time from
an owner who wants to give the flattering one; recognizes when no achievable design is timely and
reframes toward response posture or consequence instead of iterating on hardware; presents all
four levers so the conversation becomes a decision about strategy rather than an argument about
products; and can say "this system documents crimes rather than preventing them" in a way that
leads to a better decision instead of a defensive one.

---

## Problem set

**P8.1** A distribution centre. Adversary: one person, hand tools. Assessment delay 30 s.

| Task | Delay |
|---|---|
| Cut perimeter fence | 45 s |
| Cross yard | 55 s |
| Force personnel door | 120 s ← **detected here** (DPS) |
| Cross warehouse floor | 80 s |
| Force office door | 90 s |
| Open safe | 420 s |

- (a) Compute `T_T`, `T_D`, and `T_A`.
- (b) Evaluate against an on-site guard at `T_R = 420 s` with zero margin.
- (c) Evaluate against a police dispatch at `T_R = 900 s` with a 120 s margin.
- (d) For (c), compute the deficit and the required detection point.

**P8.2** Produce the timeline table for P8.1's path. Then, for **each** of the two response
postures in P8.1(b) and P8.1(c), identify which task the adversary is executing at the required
detection point — **if any** — and say what you conclude. Where the answer exists, state what
constraint might prevent you placing detection there.

**P8.3** The same site, but the owner replaces the guard with a contract patrol at `T_R = 2400 s`.
- (a) Compute the required detection point.
- (b) Is the detection lever feasible? Show the check.
- (c) Write the paragraph you would give the owner, covering all four levers.

**P8.4** An adversary path has no detection at all: walk in 30 s, take it 60 s, `T_R = 60 s`.
Explain what the model returns and why `None` is a better answer than 0 or infinity for `T_A`.

**P8.5** A colleague models a shock sensor on a door as detecting at the *start* of the "force
door" task, which is 150 seconds long. Explain the effect on the analysis, whether they are right,
and how you would model it properly.

**P8.6** An owner tells you response time is "about 5 minutes." Write the three questions you ask
before putting 300 s into the model, and say what each one is protecting against.

**P8.7** 🧮 A site is not timely by 400 s. Compare the four levers quantitatively where you can:
the site could add a 400 s barrier after the detection point for $85,000; move detection 400 s
earlier for $30,000 but only if assessment cameras costing $45,000 are added; reduce response time
by 400 s by adding an on-site guard at $190,000/year; or relocate the asset to an interior vault
for $12,000. Make a recommendation and justify it, including what you would tell the owner about
the option you did *not* recommend but they will probably want.

**P8.8** Explain why `compare_interventions` returning "NOT ACHIEVABLE" is better engineering than
returning a negative detection time, and give one other calculation in this module where the same
pattern would be an improvement.

> Answers: [`_solutions/08_adversary_path_solutions.md`](_solutions/08_adversary_path_solutions.md)

---

## Retrieval check

1. Define `T_T`, `T_D`, `T_A`, `T_R`, and state the timeliness inequality.
2. Why is assessment time added to `T_D`?
3. Why is detection modelled at task completion rather than task start?
4. Write the required detection point formula and say what you do with it.
5. Why is "marginal" treated as not timely?
6. Name the four levers. Which one is not a term in the inequality, and why is it included?
7. What does a negative required detection point mean, and what should a calculation do about it?
8. Name the five limits of the model. Which one bites most often in practice?

---

## References

- Garcia, M.L., *The Design and Evaluation of Physical Protection Systems*, 2nd ed. `[PRACTICE]`
  The authoritative treatment of detect/delay/respond and timely detection.
- Garcia, M.L., *Vulnerability Assessment of Physical Protection Systems.* `[PRACTICE]`
- Sandia National Laboratories physical protection literature (publicly released portions) —
  origin of much of this methodology, including EASI. `[GUIDELINE][VERIFY availability]`
- [`../28_Calculators/psec/pps.py`](../28_Calculators/psec/pps.py) — the implementation.
- [`../28_Calculators/tests/test_psec.py`](../28_Calculators/tests/test_psec.py) — `TestPPS`.
- [`../01_Foundations/03_functional_chain.md`](../01_Foundations/03_functional_chain.md) — the
  conceptual treatment this lesson derives.
- [`../02_Risk_Assessment/`](../02_Risk_Assessment/) — adversary path analysis and finding the
  weakest path *(not yet written — see [`../COURSE_PROGRESS.md`](../COURSE_PROGRESS.md))*.

---

**This is the last lesson in Module 32.** Close the module with:
- 🧮 [The integrated sizing capstone](_exercises/integrated_sizing.md) — one site, all eight lessons
- [`../25_Quizzes/quiz_32_engineering_math.md`](../25_Quizzes/quiz_32_engineering_math.md)
- [`../26_Flashcards/32_engineering_math.csv`](../26_Flashcards/32_engineering_math.csv)
