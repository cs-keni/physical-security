# 08 — Key Management and Mechanical Security

## Learning objectives

- Explain why the mechanical key system is the actual perimeter of a building, regardless of how
  good the electronic access control system is.
- Read and reason about a master key hierarchy, and explain the security cost of each additional
  level.
- Name the events that force a rekey and estimate what each one costs.
- Specify the three controls that do most of the work: a restricted keyway, interchangeable
  cores, and a key control program with an owner.
- Explain construction keying and why the turnover step is the one that gets skipped.
- Decide, deliberately, which openings get **no** mechanical override — and defend it.
- Identify the mechanical attack classes that exist and specify the rated countermeasure for
  each, without needing to know how the attacks are performed.

---

## ELI5

You spent the whole module putting electronic locks on doors. Every one of those locks has a
keyhole in it, because somebody has to get in when the power is dead.

So there is a piece of metal, in somebody's pocket, that opens the door regardless of what your
card system thinks. And there is probably one piece of metal that opens *every* door.

**That key is the real perimeter.** If nobody is managing it — and usually nobody is — then the
access control system is a very expensive logging device.

---

## The uncomfortable framing

Work through what you've built across this module:

- Lesson 03: electrified locksets, exit devices, strikes. All of them have a **mechanical key
  override** by design, because lesson 04's failure mode 2 (battery exhausted) has to have an
  answer.
- Lesson 04: that override is the answer to "what happens when everything is dead."
- Lesson 07: rated openings are fail secure and self-latching, so the override matters more, not
  less.

**Therefore:** every credential decision, every anti-passback rule, every audit trail, and every
alarm you designed is bypassed by a person holding the right key, and the system will record
nothing. Not "record it as suspicious" — **record nothing**, because a mechanical key operation
generates no event at most openings.

> 🧠 **The senior framing to carry into client conversations:** *"Your access control system is
> as strong as your key control program, because every one of these doors also opens with a
> key. Right now I don't know who has master keys and neither do you. That's the cheapest
> significant improvement available to you and it doesn't involve buying anything."*
>
> This is frequently the highest-value recommendation on a project and it reduces your fee,
> because it's a policy fix rather than a hardware purchase. Say it anyway. Lesson 01 of
> Foundations warned you that this job requires saying the uncomfortable thing; this is where
> it shows up most often.

---

## Vocabulary

Get these right; the trade uses them precisely and a keying schedule is unreadable without them.

| Term | Meaning |
|---|---|
| **Change key (CK)** | The individual key for one lock or one small group. The everyday key. |
| **Master key (MK)** | Opens a defined group of locks that each also have their own change key |
| **Grand master key (GMK)** | Opens multiple master key groups |
| **Great grand master (GGMK)** | One level above that. Buildings with this level are rare and should be. |
| **Keyway** | The cross-sectional shape of the keyhole; determines which blanks physically fit |
| **Restricted keyway** | A keyway whose blanks are not commercially available; duplication is controlled |
| **Patented keyway** | Restricted *and* protected by patent, so blanks cannot be legally manufactured by third parties for the patent term |
| **Bitting** | The cut pattern on the key |
| **Differ** | A unique bitting combination. The number available is finite and masterkeying consumes them. |
| **Cylinder** | The lock component the key operates |
| **Core** | A removable cylinder assembly |
| **SFIC / LFIC** | Small / Large Format Interchangeable Core — a core that can be pulled and replaced with a **control key**, without disassembling the lock |
| **Control key** | Removes an interchangeable core. **This is the most sensitive key in the system.** |
| **Construction key / construction core** | A temporary keying arrangement used during construction, voided or replaced at turnover |
| **Keying schedule** | The document mapping every opening to its keying. Usually the AHC's deliverable. |
| **Key control** | The *program* — issuance, records, return, audit |

---

## The hierarchy, and what it costs

```
                        ┌──────────┐
                        │   GMK    │  opens everything below
                        └────┬─────┘
             ┌───────────────┼───────────────┐
        ┌────▼────┐     ┌────▼────┐     ┌────▼────┐
        │  MK-A   │     │  MK-B   │     │  MK-C   │
        │ Floor 1 │     │ Floor 2 │     │  Mech   │
        └────┬────┘     └────┬────┘     └────┬────┘
       ┌─────┼─────┐    ┌────┼────┐     ┌────┼────┐
      CK    CK    CK   CK   CK   CK    CK   CK   CK
     101   102   103  201  202  203   M01  M02  M03
```

**Each level up is a skeleton key for everything beneath it.** That is the entire point and the
entire risk.

**Three costs of depth that juniors don't anticipate:**

1. **Differs are finite and masterkeying consumes them fast.** A keyway has a limited number of
   usable bitting combinations. Every additional masterkey level multiplies the constraints on
   which combinations remain usable, and deep hierarchies burn through the space. On a large
   campus this becomes a real design limit, and the fix is not free.

2. **Masterkeying weakens the individual lock.** A cylinder that must accept two or more keys has
   more shear points than one that accepts a single key. More levels, more shear points. This is
   a known and accepted property, and it is a reason not to add levels you don't need.
   `[VERIFY specifics per cylinder product and platform.]`

3. **The blast radius of a lost key equals the level it sits at.** A lost change key is one
   cylinder. A lost grand master is the building.

> 🧠 **The design guidance: the hierarchy should mirror the responsibility structure, and go no
> deeper.** If nobody's job requires opening every door on floor 2, there should not be a floor 2
> master. Most hierarchies are deeper than the organization that uses them, because they were
> designed once around an org chart that has since changed twice.

---

## Rekeying: the triggers and the cost

**The events that force a rekey:**

| Trigger | Scope forced |
|---|---|
| Change key lost | That opening |
| Master key lost or unreturned | **Every opening in that master's group** |
| Grand master lost | **Everything** |
| **Control key lost** (SFIC systems) | Every core in the system — the control key removes cores, so it is functionally a master key for the entire system's *cylinders* |
| Employee with a master terminated, key not returned | That master's group |
| Contractor turnover at end of construction | Everything the construction key opened |
| Keying records lost or never kept | Everything, because you can no longer reason about it |

**Cost scales with the group, not with the key.** One person loses one key and the invoice covers
every cylinder that key operated, plus every key that has to be reissued to everyone else in
that group, plus the labor.

**This is the argument for interchangeable cores.** With SFIC, rekeying an opening means pulling
a core with a control key and dropping in a new one — minutes, no disassembly, no locksmith at
the door with a lock in pieces. The cores can be rotated from a stock. On a building of any
size, the operational cost difference between SFIC and conventional cylinders over twenty years
is not close.

**The tradeoff, stated honestly:** the control key becomes a single extremely sensitive credential.
An SFIC system with careless control key handling is worse than a conventional system, because
the control key opens the *cylinders*, not just the doors. Whoever holds it can remove and
replace any core in the building, silently.

---

## The three controls that do the work

### 1. A restricted or patented keyway

**The highest-leverage single decision in mechanical security.**

An ordinary keyway means blanks are available at any hardware store and duplication is a
five-dollar, five-minute transaction with no record. "DO NOT DUPLICATE" stamped on the bow is
not a control — it is a request, and it is routinely ignored.

A restricted keyway means the blanks are not commercially available. A patented keyway adds
legal protection against third-party blank manufacture for the patent term. Duplication runs
through an authorized dealer against a signed, recorded authorization list.

**What it actually buys you:** the ability to know how many keys exist. Without it, that number
is unknowable, and every other control in the program is built on sand.

**Cost:** higher per-cylinder cost, and you are tied to a supply channel for the life of the
system. Both are real. Both are usually worth it at any opening that matters.

### 2. Interchangeable cores

Covered above. Makes rekeying cheap enough that it actually happens when it should, rather than
being deferred because it costs too much — which is how buildings end up with keys in
circulation that nobody can account for.

### 3. A key control program with a named owner

The program, minimally:

- **A key control policy**, written, approved, and issued.
- **A named owner.** One person, by role. This is the item that is almost always missing.
- **Issuance records**: who holds which key, since when, authorized by whom, signed for.
- **Return on separation**, integrated with HR offboarding — a terminated employee's key return
  should be on the same checklist as their laptop.
- **Periodic audit**: physically sight the keys against the register. Annually at minimum, and
  for masters and control keys more often.
- **Defined rekey triggers** and a budget line for them, so the decision to rekey isn't a
  budget fight every time.
- **Secure storage**: a key cabinet with its own access control and log. An electronic key
  cabinet that logs issuance and return is a genuinely good investment for master and control
  keys.
- **Records of the keying schedule itself**, held securely — the keying schedule is a map of the
  building's mechanical security and should be treated accordingly.

> ⚠️ **Key management falls between facilities and security and is therefore owned by nobody.**
> It is not glamorous, it involves paperwork, and there is no vendor selling it as a product with
> a sales team pushing it. This is precisely why it degrades. **Name the owner in writing at
> handover**, or in three years the answer to "who has a master?" will be "we're not sure."

---

## Construction keying: the step that gets skipped

During construction the contractor needs access to everything. So the openings are keyed to a
**construction key**, or fitted with temporary **construction cores**.

**At turnover, that access is supposed to be voided:**

- Conventional construction keying: the first use of the permanent change key mechanically
  invalidates the construction key.
- Construction cores: the temporary cores are pulled and the permanent cores installed.

**The failure:** nobody performs the turnover. The cores are never swapped, or they're swapped
at 80% of openings and the remaining 20% are forgotten, or the construction key is never
invalidated because the permanent keys were never distributed.

**The result:** every trade that worked on the building — and everyone they gave a copy to —
retains access, indefinitely, with no record.

**This is extremely common. Assume it has happened until someone shows you otherwise.**

**Your deliverable:** make construction key turnover an explicit, verifiable line item in the
commissioning checklist and the substantial completion criteria — with a **per-opening
verification**, not a blanket sign-off. See `../18_Commissioning/`.

---

## The openings that get no override

A deliberate design decision that most engineers never make consciously.

**The case for no mechanical override at an opening:** the override is a permanent bypass of
every electronic control. At the highest-consequence openings — a vault anteroom, a secure
evidence room, a data hall cage — you may decide the risk of the override exceeds the
operational benefit.

**What you accept when you do this:** if the electronics fail completely, entry requires a
locksmith, a drill, or a documented emergency procedure. That is a real operational cost and a
real delay in an emergency.

**How to make it a decision rather than an accident:**

1. Name the openings.
2. Write down what the emergency access procedure *is*, since it isn't a key. Who is called, what
   is authorized, how long does it take, who approves.
3. Get the owner's explicit acceptance, in writing.
4. Make sure fire service access is addressed separately — **a Knox box or equivalent fire
   department access arrangement is usually a code and AHJ matter and is not yours to trade
   away.** `[CODE][VERIFY]`

> ⚠️ **The Knox box is its own key control problem** and it is routinely ignored. It contains
> keys, it is mounted on the exterior, and the access arrangement belongs to the fire department.
> Know whether one exists on your project, what's in it, and who maintains its contents — because
> the answer to the third question is often "nobody has opened it since 2011 and the keys in it
> are for locks that were replaced."

---

## Mechanical attack classes and their countermeasures

**The correct depth here is: this class of attack exists; here is the rated countermeasure.**
That is what a designer needs. Procedures are not covered and are not necessary.

| Attack class | What it targets | Countermeasure to specify |
|---|---|---|
| **Unauthorized duplication** | The key itself | Restricted or patented keyway; controlled authorization list |
| **Picking and manipulation** | The cylinder's internal mechanism | High-security cylinder rated for pick resistance — ANSI/BHMA A156.30 and UL 437 are the relevant listings `[STANDARD][VERIFY]` |
| **Bumping** | Standard pin tumbler cylinders | Same rated cylinders; the ratings address this class |
| **Drilling** | The cylinder body | Hardened inserts, as covered by the same high-security ratings |
| **Wrenching / pulling the cylinder** | The cylinder's mounting | Protective collar or cylinder guard; a security escutcheon |
| **Latch slipping / loiding** | The latch bolt | Deadlatch, properly seated (lesson 01) — and verify the strike alignment, because a deadlatch that isn't seated isn't working |
| **Attacking the strike or frame** | The frame, not the lock | Frame reinforcement, proper anchorage, dust box, welded frame (lesson 01) |
| **Hinge pin removal** | Out-swinging doors | NRP hinges or security studs (lessons 01, 02) |

**The pattern worth noticing:** four of the eight are addressed by a **rated cylinder**, two by
things you learned in lesson 01 about the frame and the latch, and one — the first, and arguably
the biggest — by a **policy control**, not a product.

**Grades:** ANSI/BHMA A156 grades hardware 1 through 3, with Grade 1 the highest, on durability
and strength criteria. `[STANDARD][VERIFY the criteria per product class.]` Grade 1 at anything
consequential; the delta over Grade 2 is small and the durability difference over twenty years
is not.

Padlocks, hasps, cabinets, cages, safes, and vaults are their own product landscape with their
own rating schemes — see `../38_Products_and_Ratings/`.

---

## What you actually deliver

You are usually not the author of the keying schedule; the AHC is. **Your deliverables are:**

1. **Review of the keying schedule for the security-relevant openings.** Does the hierarchy make
   sense? Are the high-consequence openings on a master they shouldn't be on? Is anything on the
   grand master that doesn't need to be?
2. **A written recommendation on keyway restriction**, with the cost implication stated.
3. **The no-override decision list**, with the owner's written acceptance.
4. **A key control policy recommendation**, including the named owner role.
5. **Construction key turnover as a verified commissioning line item.**
6. **The handover paragraph** naming the ongoing obligation.

Items 3, 4, 5, and 6 are the ones nobody else on the project will produce.

---

## Design tradeoffs

| Tradeoff | The tension | How to resolve |
|---|---|---|
| Deep hierarchy vs. shallow | Depth is operationally convenient; each level is a skeleton key and consumes differs | Mirror the responsibility structure, go no deeper |
| Restricted keyway vs. cost and supply lock-in | Restriction is the highest-leverage control; it costs more and ties you to a channel | Restricted at everything consequential. Justify exceptions, not inclusions. |
| SFIC vs. conventional cylinders | SFIC makes rekeying cheap; the control key becomes critical | SFIC at any building large enough to rekey more than rarely, plus strict control key handling |
| Mechanical override vs. no override | The override guarantees access when all else fails; it permanently bypasses the electronics | Override by default; no-override only at named high-consequence openings with written acceptance |
| Electronic key cabinet vs. a locked box | The cabinet logs and enforces; it costs money | Cabinet for masters and control keys at minimum |

---

## Common mistakes

⚠️ **Designing an access control system and never asking about keys.** The most common omission
in the whole discipline.

⚠️ **Assuming construction keying was turned over.** Verify per opening.

⚠️ **A hierarchy deeper than the organization.**

⚠️ **"DO NOT DUPLICATE" treated as a control.**

⚠️ **No named owner for key control.** Then it is owned by nobody.

⚠️ **Treating the control key as an ordinary key** in an SFIC system.

⚠️ **Putting a high-consequence opening on a broad master** because it was convenient.

⚠️ **Never auditing.** A register that isn't physically verified is a document, not a control.

⚠️ **Forgetting the Knox box.**

⚠️ **Storing the keying schedule where anyone can read it.**

---

## Junior vs. Senior

**Junior:** uses the keying vocabulary correctly; reads a hierarchy; knows a restricted keyway
and interchangeable cores are the two product-level controls; knows construction keying has a
turnover step.

**Senior:** raises key control unprompted on every project, knowing it reduces the hardware scope
and says it anyway; reviews the keying schedule specifically for high-consequence openings
sitting on broad masters; makes the no-override decision explicit and gets it accepted in
writing; puts construction key turnover into the commissioning checklist as a per-opening
verification because they have seen it skipped; names the key control owner in the handover;
and can explain to an executive, without drama, that the $400k access control system is bounded
above by a program that costs nothing and currently doesn't exist.

---

## 🔧 Field exercise

You will not be able to inspect a key system you don't administer, so this exercise is a set of
questions rather than a survey. Ask them about a building you have access to — your own office
is fine. Write down the answers you get, including "nobody knows."

1. Is there a written key control policy? Can someone produce it?
2. Who owns key control, by role?
3. How many master keys exist, and who holds them right now?
4. When was the key register last physically audited against the actual keys?
5. Is the keyway restricted? (Look at a key: does the bow carry a manufacturer's restriction
   marking? Ask whether a hardware store can cut one.)
6. Are the cores interchangeable? (Look at the face of a cylinder — an SFIC core has a
   figure-eight profile.)
7. Was construction keying turned over, and is there a record?
8. Is there a Knox box? What's in it? When was it last checked?

**The pattern of answers is the finding.** In most buildings, questions 3, 4, 7, and 8 have no
answer, and that is worth more to a client than any device recommendation you could make.

---

## Exercises

**E8.1** A 6-story office building. Facilities has 4 technicians who need access to all
mechanical and electrical rooms building-wide. Each floor has a tenant with their own suite.
Security has 2 officers who need access everywhere. Cleaning is a contractor working floors 1–3.
Design the key hierarchy. State every level, what it opens, how many keys of each exist, and
justify each level's existence.

**E8.2** For each event, state the rekey scope and estimate the relative cost:
- (a) A tenant employee loses their suite change key.
- (b) A facilities technician is terminated and does not return their mechanical master.
- (c) The SFIC control key cannot be located.
- (d) The building is 15 years old and no keying records have ever been kept.

**E8.3** You are three weeks from substantial completion on a 200-opening building. Write the
construction key turnover verification procedure: what is verified, per opening or in aggregate,
by whom, what evidence is retained, and what triggers a hold on substantial completion.

**E8.4** A client with a new $400,000 access control system asks what else they should spend
money on to improve security. Write your answer in under 200 words. Note before you start: the
best answer costs them almost nothing and reduces your future scope.

**E8.5** Identify which openings in a data center campus you would specify with **no mechanical
override**, what emergency access procedure replaces the key, and what you would need in writing
from the owner. Include how you would handle fire service access.

**E8.6** A colleague specifies high-security Grade 1 cylinders with a patented keyway at all 61
openings on a project and presents it as a hardened design. The building has no key control
policy and no named owner. Write your review comment.

> Solutions: [`_solutions/08_key_management_solutions.md`](_solutions/08_key_management_solutions.md)

---

## Retrieval check

1. Why is the mechanical key system the real perimeter of an access-controlled building?
2. Define change key, master key, control key, and differ.
3. Name three costs of adding a level to a key hierarchy.
4. What is the rekey scope when a master key is lost? When a control key is lost?
5. What does a restricted keyway actually buy you?
6. What is construction keying, and what is the step that gets skipped?
7. Name the three controls that do most of the work in mechanical security.
8. When would you specify an opening with no mechanical override, and what must you get in
   writing?

---

## References

- ANSI/BHMA A156.5 (auxiliary locks and cylinders), A156.30 (high security cylinders) —
  product standards and grading. `[STANDARD][VERIFY numbering against current editions]`
- UL 437 — key locks; attack resistance listing. `[STANDARD][VERIFY]`
- ALOA and DHI — key system design and key control program practice. `[PRACTICE]`
- ASIS International — *Protection of Assets*, physical security volume, on key control
  programs. `[GUIDELINE]`
- Applicable fire code — fire department access arrangements including key boxes.
  `[CODE][VERIFY]`
- Manufacturer documentation — keyway restriction terms, patent expiry dates, differ capacity.
  `[MFR][VERIFY — patent expiry matters: a patented keyway becomes an unrestricted one when the
  patent lapses, and buildings outlive patents.]`
- `../38_Products_and_Ratings/` — padlocks, hasps, cabinets, safes, and vaults.
- `../19_Operations/` — key control as an operational program.

---

**This is the last lesson in Module 35.** Close the module with:
- 🔧 [The 10-door field exercise](_exercises/10_door_survey.md) — the module's capstone
- [`../25_Quizzes/quiz_35_doors_hardware.md`](../25_Quizzes/quiz_35_doors_hardware.md) — take it cold, then again after
- [`../26_Flashcards/35_doors_hardware.csv`](../26_Flashcards/35_doors_hardware.csv) — import to Anki
