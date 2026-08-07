# Project 1 — Secure One Office Door

> **The whole discipline, at the smallest possible scale.** Every idea you will use on a
> data center campus is present in one door. Do this properly and Project 8 is the same
> reasoning, repeated.

**Effort:** 3–5 hours. **Prerequisites:** `01_Foundations/` lessons 01–07,
`35_Doors_and_Hardware/` 01–04 (or work from this brief and backfill).
**Do not open [`_solutions/`](../_solutions/project_01_reference.md) until you submit.**

---

## The scenario

**Meridian Analytics** leases the 4th floor of a 6-story multi-tenant office building.
Standard commercial construction, sprinklered, fully occupied. Their space is 11,000 sq ft
with 62 employees.

Inside their suite is **Room 412, "Data & Records."** It contains:

- A small server rack (2 physical servers, a NAS, and network gear) — the company's primary
  file storage and their client project archive.
- Three lateral filing cabinets holding **signed client contracts and personnel files**.
- A wall safe holding backup tapes and the company's original corporate documents.

**The room today:** a standard 3'-0" × 7'-0" hollow metal door in a hollow metal frame, with
a mechanical lockset keyed to the office master. No monitoring of any kind. The door swings
**into** the room. There is a suspended acoustical ceiling at 9'-0" AFF in both the room and
the adjacent corridor; the deck above is at 13'-6". Interior partitions are metal stud with
one layer of gypsum board each side, terminating at 10'-0" — **above the ceiling grid but
below the deck.** One 24" × 24" return air transfer grille penetrates the wall to the corridor
at 8'-6" AFF.

### Who has access today

| Group | Count | Notes |
|---|---|---|
| IT manager | 1 | Legitimate daily need |
| Office manager | 1 | Legitimate need (records) |
| Two principals | 2 | Legitimate |
| Everyone with an office master key | **~14** | Includes 3 people who left in the past year; keys not returned |
| Building janitorial contractor | unknown | Has building master; unescorted, nightly, ~2200–0100 |
| Building engineering | unknown | Has building master; enters for HVAC/sprinkler |

### Operating context

- Suite hours 0700–1900 weekdays. Employees badge into the *suite* entry door already (an
  existing, functioning access control system with spare controller capacity in the suite's
  IDF, 90 ft away).
- No guards. No SOC. Alarm response would be a keyholder callout — realistically **45+
  minutes** at night, and the two people on the callout list live 20 and 35 minutes away.
- The building has a lobby attendant 0700–1800 only. After hours, tenants badge in at the
  building's main entry with a building-issued credential.
- Meridian's IT manager checks system health "when something seems wrong."
- Budget for this scope: **$4,000–$6,000**, and the principals are skeptical about spending
  more. They asked for "a card reader on the data room."

### What triggered this

A client's vendor-security questionnaire asked whether physical access to systems holding
their data is "controlled, monitored, and auditable." Meridian answered *yes*. The office
manager, filling in the form, then realized she wasn't sure that was true and raised it.

---

## Your deliverable

A short design package. Aim for **4–8 pages**. Quality of reasoning beats volume — a
two-page document that answers everything is better than eight pages of padding.

### 1. Risk basis (½–1 page)
- Asset register: each asset, its owner, and its **consequence of loss** across all six
  consequence categories (life safety, financial, operational, regulatory/legal,
  reputational, environmental). Note which category actually justifies the budget.
- Threat characterization: at least **three** distinct threats, each with motivation,
  capability, knowledge, access, and risk aversion.
- Vulnerability findings: written as *exploitable weaknesses*, not as missing devices.

### 2. Requirements (½ page)
- 8–12 requirements, each tagged **F / P / O / C** (functional, performance, operational,
  constraint), each traced to a risk or driver, each testable.

### 3. Design narrative (1–2 pages)
For each device or measure you propose: what it is, where it goes, **which protection
function it performs**, and what happens if it fails.

Cover at minimum:
- Door hardware — and whether the existing door and frame are adequate
- The locking method, with **fail safe vs. fail secure** decided and justified
- Credential and reader (technology and why)
- Door position switch — type and mounting
- Request-to-exit — or a defensible argument that none is needed
- Whether video is warranted; if so, where, with what pixel-density target and why
- Whether intrusion detection is warranted
- The **zone boundary** — and what you're doing about the ceiling and the transfer grille
- The mechanical key system
- Anything procedural

### 4. Sequence of operation (½–1 page)
Write it as numbered steps a contractor can build from and a commissioning agent can test.
Cover **all** of:
- Valid credential presented, door opened and closed normally
- Invalid/expired credential presented
- Door forced open
- Door held open beyond the shunt period
- Egress from inside
- **Loss of network to the head-end**
- **Loss of AC power**
- **Fire alarm activation**
- Controller failure

### 5. Calculations (½ page)
- 🧮 Power: current draw of everything you added, power supply sizing, and battery Ah for a
  4-hour standby. Use `28_Calculators/psec/power.py` — but **do the arithmetic by hand first
  and show it.**
- 🧮 Voltage drop for the lock power run from the IDF (90 ft cable route — but justify the
  actual routed length you use, which is not 90 ft).
- 🧮 If you specified a camera: FOV, pixel density at the door plane, and the max range at
  which your target class holds.
- 🧮 **Timely detection:** build the adversary path to the safe, place your detection, and
  compute whether the system is timely against the 45-minute response. Then state honestly
  what the system is actually *for*.

### 6. Residual risk statement (¼ page)
What remains after your design. Written for the **principals**, not for an engineer. Plain
language, no jargon, and specific enough that they can genuinely accept or reject it.

### 7. Test plan (½ page)
The commissioning tests that prove each requirement is met. One row per test: test ID,
requirement it verifies, procedure, expected result, pass/fail.

---

## The ambiguities (deliberate — resolve them, don't ignore them)

A real brief is never complete. These are the gaps. **State your assumption for each one in
writing and proceed** — that's the professional behavior, and it's what's being assessed.

1. **Is the door frame anchored to the deck or only to the partition?** Not stated. It
   changes your answer about the boundary. What would you do about not knowing?
2. **What is above the ceiling — is the plenum continuous to the corridor?** The wall stops
   at 10'-0" and the deck is at 13'-6". Draw the conclusion.
3. **Does the return air transfer grille need to stay?** It's an HVAC requirement, not a
   security one. Who do you have to talk to, and what do you ask for?
4. **Is there an existing camera in the corridor outside 412?** Not stated. What do you do
   when you don't know — assume, or find out, and how does that change the schedule?
5. **Does the suite's existing access control system support the credential technology you
   want?** If it's legacy 125 kHz prox, what do you recommend, and does that change the
   budget conversation?
6. **The janitorial contractor.** Nobody controls this and nobody wants to talk about it.
   It is arguably your most significant finding. How do you raise it?
7. **The budget doesn't cover the right answer.** Decide what you do about that.

---

## The trap in this project

The client asked for "a card reader on the data room." A card reader on this door, by itself,
**does almost nothing** — and figuring out precisely why, then saying so constructively, is
the actual exercise.

Before you write anything, answer these three:
- What is the **weakest penetration path** into Room 412, and how long does it take?
- How many people can open that door **today**, and does the client know the number?
- If someone takes the contents of the safe at 0200 on a Saturday, **when would anyone find
  out?**

If your design doesn't change the answers to those three questions, it hasn't accomplished
anything, regardless of how many devices it contains.

---

## Self-assessment before you look at the solution

Score yourself honestly:

- [ ] I identified the **ceiling plenum** as a penetration path and addressed it
- [ ] I identified the **transfer grille** and said something about it
- [ ] I addressed the **mechanical key system** (this is the highest-value, lowest-cost finding)
- [ ] I addressed the **janitorial/building-engineering access** problem
- [ ] I decided fail safe vs. fail secure **and justified it against life safety**
- [ ] I stated whether a REX is required and **why** — including what happens if the door
      swings *into* the room
- [ ] My sequence of operation covers **fire alarm, power loss, and network loss**
- [ ] I computed timely detection and **stated honestly what the system is actually for**
- [ ] I wrote a residual risk statement a non-engineer could act on
- [ ] Every device I specified traces to a requirement, and every requirement traces to a risk
- [ ] I recommended at least one **procedural** control (they're cheaper and I should have
      considered them first)
- [ ] I said something about **what I would do differently if the budget were larger** — and
      about whether the budget should be larger

**If you checked fewer than 8, go back before reading the solution.** The learning is in the
attempt, not in the comparison.

---

## Then

1. Read [`_solutions/project_01_reference.md`](../_solutions/project_01_reference.md).
2. Write a **gap list** — what the reference caught that you didn't, and *why* you missed it.
   The "why" matters more than the "what."
3. Log the gaps in your decision journal.
4. Update [`progress_tracker.md`](../../00_Roadmap/progress_tracker.md).
