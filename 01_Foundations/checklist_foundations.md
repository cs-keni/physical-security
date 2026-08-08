# The Foundations Checklist

**The reasoning checklist you will use forever.**

This is the whole module compressed into questions. Not facts — **questions**, because what
Module 01 actually teaches is a sequence of things to ask, in an order that stops you from
solving the wrong problem.

Print it. Put it in the front of the notebook you take to site. Run it on every project, every
survey, and every drawing set you are handed, until you stop needing it.

> **The single most common failure this checklist prevents:** hearing a request and reaching for
> a product. Every section below is upstream of the product decision, and skipping to the end is
> what produces buildings full of equipment that addresses nothing.

---

## 0 — Before you do anything

- [ ] **What am I actually being asked for?** A design, an opinion, a number, a second opinion,
      or cover for a decision already made? These are different jobs.
- [ ] **Who is the client, and who is the user?** They are frequently not the same person and
      their interests differ.
- [ ] **What decision will my work inform, and who makes it?** If nobody will decide anything
      differently because of your output, find out why before you produce it.
- [ ] **What has already been decided?** Budget, product standard, architect's design, a
      committed schedule. Constraints discovered late are expensive.
- [ ] **What is my scope, and what is adjacent to it?** Say out loud what is *not* yours,
      early and in writing.

---

## 1 — The four questions (lesson 01)

Every physical security problem starts here. If you cannot answer all four, you are not ready
to design anything.

- [ ] **What are we protecting?** The asset, its owner, and its form (people, property,
      information, reputation, continuity).
- [ ] **From whom, or from what?** Threat (with intent and capability) or hazard (with neither).
      Characterize them; do not just name them.
- [ ] **What happens if we fail?** The consequence, stated in the client's terms — dollars,
      downtime, injury, penalty, headline.
- [ ] **What are we willing to spend?** Money, inconvenience, aesthetics, staff time, and
      throughput. All four are currencies and clients will spend some and not others.

**Check:** can you write one paragraph containing all four? If not, ask more questions before
you draw anything.

---

## 2 — The risk chain (lesson 02)

- [ ] Can I trace **asset → threat/hazard → vulnerability → event → consequence → likelihood →
      risk → countermeasure → residual risk** for every recommendation I am making?
- [ ] Have I distinguished **threat from hazard**? (Intent — and it changes the whole design
      approach.)
- [ ] Is every vulnerability stated **relative to a specific threat**?
- [ ] Am I using the risk equation for its **structure** rather than for a number?
- [ ] For each risk, which of the four **treatments** applies: avoid, reduce, transfer, accept?
- [ ] Have I stated the **residual risk**, and does the owner know they are accepting it?
- [ ] Have I distinguished **effectiveness** from **assurance** — and is there a test plan?

**The question that catches the most:** *is this a threat with no vulnerability, or a
vulnerability with no consequence?* Neither is a risk, and most client statements are one of
the two.

---

## 3 — The functional chain (lesson 03)

- [ ] Have I classified every existing and proposed countermeasure by **function** —
      deter, detect, assess, delay, respond, recover?
- [ ] **Which function is missing?** (In most buildings: assess, then respond.)
- [ ] For every detection: does it have all **three parts** — sensor activation, signal
      transmission, and annunciation **to a human who acts**?
- [ ] Can that alarm be **assessed**, within seconds, by someone who is already there?
- [ ] What is the **nuisance alarm rate**, and what will it do to effective P_D in six months?
- [ ] Is the system **supervised** — will it tell me when it has stopped being able to detect?

### The timely detection check

- [ ] Have I computed `T_T`, `T_D` (**including assessment**), `T_A`, and `T_R`?
- [ ] Is `T_A > T_R`, and with how much margin?
- [ ] Is `T_R` **measured** or quoted? (Quoted numbers are optimistic. Test at 0300 on a Sunday.)
- [ ] Have I computed the **required detection point**, and does the detection layer sit at or
      before it?
- [ ] Is any delay I am proposing **after** the detection point? (Before it, it buys nothing.)
- [ ] If it is not timely, have I shown **all four levers** — detect earlier, delay after
      detection, faster response, **reduce the consequence** — rather than only the one I sell?

**Check:** if the required detection point comes out **negative**, say *not achievable* and go to
the response or consequence lever. Do not go shopping for sensors.

---

## 4 — Layers and boundaries (lesson 04)

- [ ] Have I drawn the **zone diagram**, with zones as volumes and a named control at every
      boundary?
- [ ] Are my layers **independent, sequential, and individually meaningful**? (Three locks on
      one door is one layer bought three times.)
- [ ] For every high-value zone, have I run the **nine-element integrity check** — walls,
      ceiling, floor, doors, windows, penetrations, roof, adjacencies, egress hardware?
- [ ] **Does the boundary go slab to slab?** (Ask it out loud. It is the most-missed question in
      the discipline.)
- [ ] What is on the **other side of every wall**, and who has access to *that* space?
- [ ] Does the required **egress path from within** create an entry path from without?
- [ ] **Balanced protection:** is the path I am strengthening still the weakest one? If not,
      stop spending on it.
- [ ] Have I enumerated the **SPOFs** — including the room, the UPS, the licence, the
      certificate, and the one administrator?
- [ ] Where I have redundancy, would **diversity** be better? (Against a thinking adversary or a
      common cause: yes.)
- [ ] Is **graceful degradation** specified, or am I hoping for it?

**Check:** if every weak boundary on your list is a door, you have not run the check.

---

## 5 — The environment (lesson 05)

- [ ] Have I walked the site as **each user type** — visitor, early-shift employee, delivery
      driver, contractor, and someone with no legitimate business?
- [ ] Have I mapped **sightlines** from every occupied position, and marked the vulnerable areas
      covered by none?
- [ ] Have I inventoried **concealment** within 20 ft of every entry and path?
- [ ] Have I surveyed the lighting **at night**, for **uniformity** rather than brightness?
- [ ] At each transition, **would a stranger know they were entering more private space?**
- [ ] Have I done the **maintenance walk** — and specifically, **where are the propped doors?**
      (They mark exactly where the access concept is fighting how people move.)
- [ ] Is there a **free or cheap** answer here — trimming, relamping, signage, moving furniture,
      changing a schedule — before I propose hardware?
- [ ] Is every finding written with **location, affected users, mechanism, and a cost**?

**Check:** if none of your findings costs under $2,000, you are looking for products rather than
conditions.

---

## 6 — Requirements (lesson 06)

- [ ] Is every requirement **testable**? For each one, can I name the test?
- [ ] Does every requirement use **"shall"**?
- [ ] Do I have all four **types** — functional, performance, operational, constraint — with
      none empty?
- [ ] Have I written the **operational** requirements about how people actually work, including
      the failure cases: forgotten badge, delivery, network down, fire alarm?
- [ ] Does every requirement **trace** to a risk, a code, a client statement, or a principle?
- [ ] Have I checked for the four **pathologies** — solution-as-requirement, inherited,
      unfalsifiable, orphan?
- [ ] Are **requirements separated from specifications**? (What must be achieved vs. one way to
      achieve it.)
- [ ] Is the **RTM** populated, including the test-procedure column?
- [ ] Is the **fail state** of every controlled opening explicitly stated rather than implied by
      the hardware selection?

**Check:** if the budget were cut 30% tomorrow, could you show which risks are being dropped?
If not, the RTM is not finished, and the cut will be made arbitrarily.

---

## 7 — Failure (lesson 07)

- [ ] Have I traced the **full chain** for each subsystem, from physical stimulus to human
      response?
- [ ] Have I run the **nine categories** — component, communication, power, software,
      configuration, human error, malicious, maintenance, **design**?
- [ ] For every failure mode: **who detects it, and how fast?** (How many say *never*?)
- [ ] What happens at the **interfaces** — between subsystems, between disciplines, and between
      this design and later fit-out work?
- [ ] Is **every device in each functional chain** on the same power source, or have I protected
      half a chain?
- [ ] What is the behaviour on **power loss, network loss, and fire alarm**? (Three different
      answers, all required.)
- [ ] Have I done the **"and then what does the human do?"** arithmetic — alerts per day × time
      per alert, against staffed hours?
- [ ] Is there a **maintenance** obligation I am creating, and does the owner know about it?

**Check:** if nothing in your failure table is detected by "nobody," you are describing an ideal
system rather than the one you designed.

---

## 8 — Before you issue

- [ ] Is every **code or standard claim** tagged and verified against the **adopted** edition,
      or explicitly flagged as unverified? `[CODE][VERIFY]`
- [ ] Have I stated my **assumptions** in a register, with an owner and a due date against each?
- [ ] Have I said the **uncomfortable thing** — the finding that costs me scope, the
      recommendation the client will not like, the limitation of my own analysis?
- [ ] Are numbers presented as **ranges** where the underlying figure is a range, and as point
      values only where it is not?
- [ ] Would a **contractor** be able to build this from what I have issued? Would a **commissioning
      agent** be able to test it?
- [ ] Would this survive being **read back to me after an incident**?

---

## The five questions that catch the most

If you only carry five things out of this module, carry these. They are ordered by how often
they find something.

1. **"Does the boundary go slab to slab?"**
   Finds the $3,000 door on the $0 wall. Ask it about every high-value room, every time.

2. **"Who assesses that alarm, and how fast?"**
   Finds the missing function in most designs. An alarm nobody can assess is an alarm nobody
   will dispatch on.

3. **"Is that response time measured or quoted?"**
   `T_R` is usually the largest term in the inequality and it is almost never measured. It is
   also usually decided by someone who has never seen your calculation.

4. **"Is that delay before or after the detection point?"**
   Finds money about to be wasted on barriers that cannot help.

5. **"And then what does the human do?"**
   Finds the alert workload, the alarm fatigue, the propped door, and the procedure that does
   not exist. It is the question that generalises furthest beyond this discipline.

---

> **The meta-check.** Every section above is a set of questions, and none of them is a product.
> That is the actual claim of Module 01: this discipline is a way of reasoning about risk that
> occasionally results in equipment, and the engineers who are worth hiring are the ones who
> can tell you when it should not.

**Related:** [`vocabulary.md`](vocabulary.md) for the terms ·
[`exercises.md`](exercises.md) for practice ·
[`../27_Labs/project_01_secure_one_door/BRIEF.md`](../27_Labs/project_01_secure_one_door/BRIEF.md)
to run all seven lessons against one door.
