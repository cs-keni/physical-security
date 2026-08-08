# Solutions — 08 Adversary Path and Timely Detection

---

## P8.1 — The distribution centre

**(a) The three quantities**

```
   T_T  =  45 + 55 + 120 + 80 + 90 + 420          =  810 s

   T_D  =  (45 + 55 + 120)  +  30 assessment      =  250 s

   T_A  =  810 − 250                              =  560 s
```

**(b) On-site guard, `T_R = 420 s`, zero margin**

```
   margin = 560 − 420 = +140 s        →   TIMELY ✅
```

**(c) Police dispatch, `T_R = 900 s`, 120 s margin**

```
   margin = 560 − 900 = −340 s        →   NOT TIMELY ❌  (short by 340 s)
```

**(d) Deficit and required detection point for (c)**

```
   deficit = T_R + margin − T_A  =  900 + 120 − 560  =  460 s

   T_D_max = T_T − T_R − margin  =  810 − 900 − 120  =  −210 s
```

**A negative required detection point.** Hold that for P8.2 and P8.3.

---

## P8.2 — Timeline and locating the detection point

**The timeline:**

| Task | Start | End | Detected |
|---|---|---|---|
| Cut perimeter fence | 0 | 45 | |
| Cross yard | 45 | 100 | |
| Force personnel door | 100 | **220** | ✅ |
| Cross warehouse floor | 220 | 300 | |
| Force office door | 300 | 390 | |
| Open safe | 390 | 810 | |

*(Detection at t = 220 plus 30 s assessment gives `T_D` = 250 s.)*

**Posture (b) — on-site guard, `T_R = 420 s`, zero margin**

```
   T_D_max = 810 − 420 − 0 = 390 s
```

**t = 390 s falls exactly on the boundary** between "force office door" (ends 390) and "open safe"
(starts 390). So detection must occur **no later than the completion of forcing the office door.**

Current detection is at t = 250 s — the personnel door — which is **140 s earlier than required.**
The system is timely with margin, and there is nothing to fix.

> Note the boundary case is worth reading carefully: detection *at* 390 s means detecting at the
> instant the safe attack begins, which gives exactly zero margin. The convention of detecting at
> task **completion** means "detect at the office door" is the last acceptable placement — and it
> only works with zero confidence margin, which is not a design you'd sign.

**Posture (c) — police dispatch, `T_R = 900 s`, 120 s margin**

```
   T_D_max = −210 s
```

**There is no such task, and that is the finding.**

A negative required detection point means timeliness would demand detection **before the adversary
sequence begins.** Even instantaneous detection at the property line — `T_D` = 0 — leaves 810 s of
total path against a 900 s response plus 120 s margin. **You are 210 s short before you have
placed a single sensor.**

**What I conclude:** the detection lever does not exist on this path against this response posture.
No sensor placement, no technology, no budget fixes it. Continuing to shop for detection here
would be spending money to move a number that cannot reach the target.

**Where the answer exists (posture b), what constraint might prevent placing detection there:**

Detection at the office door would be *timely*, but pushing detection **later** is never the goal —
you would place it as early as you can **assess**. The binding constraint on moving it earlier is
assessment, not detection: a fence sensor at t = 45 s detects beautifully and, without a camera
that covers that zone and is automatically called up on alarm, produces nuisance alarms that
destroy the system's credibility. See
[`../01_Foundations/03_functional_chain.md`](../01_Foundations/03_functional_chain.md).

**So the real constraint is: detect as early as you can assess, and no earlier.**

---

## P8.3 — Contract patrol at `T_R = 2400 s`

**(a) Required detection point**
```
   T_D_max = 810 − 2400 − 120 = −1710 s
```

**(b) Is the detection lever feasible?**
```
   cutoff = −1710  ≤  0    →   NOT FEASIBLE
```

**The check is simply whether the cutoff is positive.** It isn't, by a wide margin: even
instantaneous detection at t = 0 leaves 810 s against a 2520 s requirement. The deficit is
```
   deficit = 2400 + 120 − 560 = 1960 s
```
— nearly 33 minutes, against a total adversary path of 13.5 minutes.

**(c) The paragraph for the owner**

> **North perimeter path — timeliness assessment**
>
> Against the assumed adversary (one person with hand tools) the total time from the fence to
> having the safe open is about **13.5 minutes**. Your current detection is the personnel door
> contact, which — including the time for an operator to check the camera and confirm — gives you
> about **4 minutes** of warning. With a contract patrol responding in around **40 minutes**, the
> adversary finishes and leaves roughly **33 minutes** before anyone arrives.
>
> **This system does not interrupt the event. It documents it.** That is a legitimate objective —
> evidence, insurance, and prosecution all have value — but it should be a decision you make
> rather than an assumption, so here are the four ways to change the outcome:
>
> **1. Earlier detection — not available on this path.** Even if we detected the instant someone
> touched the fence, the whole path is 13.5 minutes against a 40-minute response. There is no
> sensor placement that makes this timely, and I would not recommend spending money on detection
> in the hope that it helps timeliness. *(It would still improve evidence and assessment quality,
> which is a different and real benefit.)*
>
> **2. More delay after the detection point — technically possible, expensive.** You would need to
> add roughly 33 minutes of additional delay *after* the personnel door. That means turning the
> office and safe area into something close to a vault. Delay cost rises steeply and this is the
> most expensive item on this list.
>
> **3. Faster response — the dominant term, and your decision.** Response time is by far the
> largest number in this analysis. Moving from a 40-minute contract patrol to an on-site guard
> would make the system timely with margin. It is also a recurring salary rather than a capital
> cost, which is why it is a business decision rather than an engineering one.
>
> **4. Reduce the consequence — the cheapest option and the one nobody proposes.** Move the
> contents of the safe. Reduce what is held on site overnight. Bank cash daily. If a successful
> attack costs you very little, the timeliness question stops mattering. I would look at this
> first.
>
> My recommendation is to start with **4**, evaluate **3** on business grounds, and treat the
> current system as a documentation and evidence system in the meantime — and to say so in
> writing, so that nobody later believes it was intended to prevent anything.

**What makes it work:** it gives the honest verdict in the second paragraph without hedging, it
frames "documents rather than prevents" as a legitimate choice rather than a failure, it is
explicit that lever 1 is unavailable (rather than quietly omitting it), and it leads the
recommendation with the cheapest option — which is also the one an engineer has no financial
incentive to propose.

---

## P8.4 — The undetected path

**What the model returns:**

```
   T_T  = 90 s
   T_D  = None
   T_A  = None
   margin = None
   timely = False
   verdict = "NO DETECTION ON THIS PATH. The system cannot interrupt; it can
              only document after the fact."
```

**Why `None` beats 0 and beats infinity:**

**Against 0:** `T_D = 0` means "detection at the instant the sequence begins" — the *best possible*
detection. It is the opposite of the truth. Worse, it is arithmetically usable: `T_A = 90 − 0 = 90`,
margin `= 90 − 60 = +30`, and the model would report the path as **TIMELY**. A missing sensor
would be scored as a perfect one.

**Against infinity:** `T_D = ∞` gives `T_A = 90 − ∞ = −∞`, and a margin of `−∞`. Directionally
right, but it propagates into every downstream calculation as a non-number, and any table or
report containing it becomes unreadable. It also implies detection happens *eventually*, which is
not what "no detection on this path" means — it means the mechanism does not exist.

**`None` is the honest encoding: the quantity does not exist.** It cannot be silently arithmetic'd
into a wrong answer, it forces any consumer to handle the case explicitly, and **the meaning is
carried by the verdict string instead of by a number.**

> 🧠 **This is the same design decision as lesson 07's P7.8 and this lesson's NOT ACHIEVABLE
> case, in a third form.** When a quantity is undefined, the options are: raise, return a
> sentinel that cannot be misused, or return a result that names the situation in words. All
> three are better than returning a number that is arithmetically derivable and semantically
> void. `pps` uses the second and third together — `None` for the number, prose for the meaning.

---

## P8.5 — Modelling a shock sensor at task start

**The effect on the analysis:** it credits the entire 150 s door-forcing task as post-detection
delay. `T_D` falls by 150 s and `T_A` rises by 150 s, improving the margin by 150 s. On a marginal
system that is easily the difference between "not timely" and "timely."

**Are they right?** **Partly — the physics is right and the modelling is wrong.**

A shock or vibration sensor genuinely does detect the *attempt*, not the completion. That is the
whole reason such sensors exist and it is a real advantage over a door contact. Your colleague is
not wrong about the sensor.

**But changing where detection sits within a task breaks the convention**, and the convention is
what makes analyses comparable. If some tasks are detected at start and some at completion,
depending on what sensor happens to be there, no two analyses on the project can be compared and
nobody reviewing it can tell which convention any given row used.

**How to model it properly: split the task.**

| Original | Split |
|---|---|
| Force personnel door — 120 s, detected at completion | **Approach and set up — 15 s, DETECTED** (shock sensor fires on first impact) |
| | **Force door — 105 s**, not separately detected |

Now the convention is intact — detection is still at the *completion* of the task it is attached
to — and the analysis correctly credits the ~105 s of remaining door delay as post-detection.

**Two things to be honest about when you do this:**

1. **The split is an estimate.** How long between the first blow and the sensor annunciating? Not
   zero, and it depends on sensitivity settings. Be conservative.
2. **Sensitivity is a `P_d` / nuisance-alarm tradeoff.** A shock sensor set sensitive enough to
   catch the first impact is also sensitive enough to fire on a slammed door, weather, or a
   delivery truck. If it gets turned down or ignored, its effective detection reverts to
   something much later — or to nothing. The 15 s figure is only real if the sensor is believed.

> 🧠 **The general rule: don't bend the model to fit the device — change the task list.** The
> convention exists so that two analyses mean the same thing. When reality doesn't fit, the fix
> is almost always to describe reality in more detail, not to redefine the terms.

---

## P8.6 — Three questions before entering 300 s

**Question 1: "What is the response at 3 a.m. on a Sunday, in the rain?"**
*Protects against:* the daytime answer. Owners quote the org chart, which describes a fully-staffed
weekday. The overnight, weekend, and holiday posture is frequently different — a roving guard
instead of a posted one, or nobody on site at all. **The design has to work for the worst case,
not the average one.**

**Question 2: "Is that person posted, or roving? Where are they actually standing at 3 a.m., and
how do they get here?"**
*Protects against:* confusing presence with availability. A guard on site is not a guard *at this
door*. If they are roving a 400,000 sq ft campus, the response time is the walk from the far end,
plus whatever they were doing. Ask for the route and the distance, not the headcount.

**Question 3: "Has that been measured, and by whom? Can we test it?"**
*Protects against:* an estimate presented as a fact. A response time that has never been timed is
an aspiration. **The follow-up is the real one: "can we run a drill?"** — a timed test converts the
dominant term in the whole analysis from a guess into data, and it is nearly free.

**Two more worth having in reserve:**

- *"Is the response contractual or best-effort?"* Contract patrols quote response windows that are
  service targets, not guarantees, and unverified alarms are deprioritised or ignored in many
  jurisdictions. `[VERIFY locally]`
- *"What is the responder authorised to do on arrival?"* — this doesn't change `T_R`, but it
  determines whether interruption becomes neutralisation, and the owner should be clear about it.

> 🧠 **Why this matters more than any other input:** response time is usually the **dominant term**
> in the inequality and it is usually **not an engineering variable.** An error of 10 minutes in
> `T_R` swamps every hardware decision on the project. Spend your uncertainty budget here.

---

## P8.7 — 🧮 Comparing four levers on cost

**The deficit is 400 s.** Each option closes it; they cost very differently.

| Lever | Option | Capital | Recurring | Closes the deficit? |
|---|---|---|---|---|
| **2. More delay** | 400 s barrier after the detection point | **$85,000** | — | ✅ |
| **1. Earlier detection** | Move detection 400 s earlier | $30,000 | — | ⚠️ **only with** assessment |
| | *plus required assessment cameras* | **+$45,000 = $75,000** | — | ✅ |
| **3. Faster response** | On-site guard, −400 s | — | **$190,000/yr** | ✅ |
| **4. Reduce consequence** | Relocate the asset to an interior vault | **$12,000** | — | ✅ (dissolves the problem) |

**Recommendation: lever 4 — relocate the asset. $12,000.**

**Justification:**

It is **6× cheaper than the next best option** and it doesn't merely close the deficit — it
removes the exposure. Once the asset is behind an interior vault, the original path no longer
reaches anything worth reaching, and the timeliness question on that path stops being load-bearing.
Every other option leaves the asset exactly where it is and buys time around it.

It also has no recurring cost, no ongoing testing obligation, no additional devices to maintain,
and no new failure modes. Levers 1 and 2 each add hardware that must work in ten years; lever 3
adds a salary line that must survive every future budget cycle.

**Second choice: lever 1 at $75,000**, not $30,000 — and this is the trap in the numbers.
**Detection without assessment is not a partial system; it is often a net-negative one.** Moving
detection earlier without the cameras produces alarms nobody can evaluate, which produces nuisance
alarms, which produces a disabled system. The honest price of lever 1 is $75,000 and anyone
quoting $30,000 has omitted the part that makes it work.

**What I would tell the owner about the option they will probably want:**

> You will likely be drawn to the **$30,000 detection option**, because it is the cheapest number
> on the page. I need to be direct that **$30,000 does not buy a working system here.**
>
> Detection without assessment means the alarm fires and nobody can tell whether it is an intruder
> or weather. In practice that means every alarm either triggers a physical response — expensive,
> slow, and it desensitises the responder — or gets ignored, which is what actually happens.
> Within a few months the system is on a false-alarm list or switched off during bad weather, and
> you have spent $30,000 to protect nothing.
>
> The real price of that option is **$75,000**, and at that price it is still five times the cost
> of moving the asset and it leaves the asset where it is.
>
> If the vault relocation is genuinely impossible for operational reasons, tell me why and I will
> price the alternatives properly. But I would not spend $30,000 on this.

**What the problem is testing:** whether you notice that the cheapest line item is conditional,
whether you price the condition, and whether you lead with the option that reduces your own scope.

---

## P8.8 — Why "NOT ACHIEVABLE" beats a negative number

**The case for it:**

A negative required detection point is **arithmetically valid and physically meaningless.**
"Detect at t = −1150 s" is a correct solution to the equation and describes nothing that can be
built.

Three specific problems with emitting it:

1. **It looks like an answer.** A number in a results field reads as guidance. Someone would try
   to act on it, or would present it in a report, or would feed it into a spreadsheet that
   compares detection points across paths and produce a ranking in which the most hopeless path
   scores "earliest."
2. **It points at the wrong lever.** The caller's next question is *"what do I do?"* and the
   negative number implicitly answers "work on detection," which is exactly the lever that cannot
   help. The prose version redirects: *"go to the response or consequence lever."*
3. **The distinction it hides is qualitative, not quantitative.** Feasible-but-hard (cutoff = 150 s,
   move detection 80 s earlier) and impossible (cutoff = −1150 s) are different *kinds* of
   situation, and expressing both as numbers on the same scale implies they differ only in degree.

The module also exposes `detection_lever_feasible` as a boolean alongside the prose, so a program
can branch on it without parsing text — which is the right way to serve both audiences.

**Another calculation in this module where the same pattern would be an improvement:**

**`smallest_awg_for_run` (lesson 06) when no conductor in the table works.** It currently raises
`ValueError` (`test_smallest_awg_raises_when_impossible`), which is correct and safe — but the
raise tells the caller only *that* it failed, not *what to do*.

A designer hitting that raise is in the same position as one hitting a negative detection point:
the lever they reached for doesn't exist on this problem, and there are other levers. A result
object could say:

> **NOT ACHIEVABLE with available conductors.** 300 ft at 5.0 A from 12.0 V needs a conductor
> larger than 10 AWG to hold 11.0 V at the load. Options: relocate the supply closer (a 60 ft run
> works on 12 AWG), raise the supply voltage if the device permits, or select a lower-current
> device.

That is exactly the redirect `compare_interventions` performs, and it converts a dead end into a
decision — which is what a design aid should do.

**A second candidate: `max_run_length_ft` with an impossible voltage target.** It raises, which is
right, but "you asked for a 12.0 V minimum from a 12.0 V supply, which allows zero drop" is more
useful than a generic error, and it names the input that is wrong.

> 🧠 **The generalisable pattern: for a calculation whose consumer is a *designer* rather than a
> *program*, an impossible result should name the impossibility and point at the next lever.**
> Raising is correct when the input is malformed; naming is better when the input is well-formed
> and the answer is "not this way."
