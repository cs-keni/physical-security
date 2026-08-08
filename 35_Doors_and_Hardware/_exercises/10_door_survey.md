# 🔧 Field Exercise — The 10-Door Survey

**The capstone for Module 35.** Do it after lesson 08, with all eight lessons behind you.

**Time:** 3–4 hours of field work, 2–3 hours of write-up. Do it over two sessions.
**Prerequisite:** lessons 01–08.
**Deliverable:** a survey record for 10 openings plus a one-page findings memo.

---

## Why this exercise exists

Everything in this module was written to be used standing up. Reading about handing produces
someone who can define it; surveying thirty doors produces someone who determines it in fifteen
seconds without thinking, which is the actual skill.

More importantly: **this is the deliverable.** A door-by-door survey is real work that real
junior engineers are handed in their first month, on retrofit projects, and the difference
between a useful survey and a useless one is entirely in the discipline of the recording.

A useless survey says "Door 12: metal door, card reader." A useful one lets someone who has
never been to the building specify hardware from their desk.

---

## Rules

1. **Ten openings, deliberately varied.** See the selection list below. Do not survey ten
   identical office doors.
2. **Do not touch anything you are not authorized to touch.** Observe, photograph, and operate
   doors only in the normal way a person would. If you need permission, get it first.
3. **Do not report anything as a defect to anyone other than through the proper channel.** If you
   find a genuine life-safety issue — a chained exit, a blocked egress path — report it in
   writing to facilities the same day. That is not part of the exercise; that is a duty.
4. **Record what you observe, not what you infer.** "Frame appears to be KD" is a good record.
   "KD frame" when you couldn't see the joint is not.
5. **Photograph every opening.** Six shots, listed below.
6. **Fill every field.** Where you cannot determine something, write `UNKNOWN — [why]`. A blank
   is indistinguishable from an oversight; `UNKNOWN — could not access hinge side` is data.

---

## Opening selection

Choose ten, covering at least seven of these categories:

| # | Category | Why it's on the list |
|---|---|---|
| 1 | Exterior entrance, glazed | Delay governed by glazing, not hardware (L01) |
| 2 | Exterior personnel/service door | Out-swing, exposed hinges, weather (L02) |
| 3 | Stair door | Rated, re-entry, fire exit hardware (L04, L05, L07) |
| 4 | Mechanical or electrical room | Rated, panic hardware may be required (L03, L07) |
| 5 | IT closet / MDF / IDF | The wall-not-the-door lesson (L01) |
| 6 | Office suite entry off a corridor | The default access-controlled opening (L03) |
| 7 | An opening with a magnetic lock | If you can find one — check its release subsystem (L03, L05) |
| 8 | A pair of doors | Coordinator, astragal, mullion, flush bolts (L01) |
| 9 | An access-controlled opening | Reader side, REX, DPS, transfer (L02, L06) |
| 10 | A restroom or other low-security opening | The control group. Not everything needs securing. |

---

## The record — one per opening

Copy this block ten times.

```
OPENING ______  Location _______________________________  Date _______  Time _______

── IDENTIFICATION ──────────────────────────────────────────────────────────
Building / floor / room served
Door number, if posted
Space on the secure side
Space on the approach side

── GEOMETRY (L01, L02) ─────────────────────────────────────────────────────
Handing                     LH / RH / LHR / RHR
  → SIDE I STOOD ON         ______________________  (mandatory — see L02)
Swing                       in / out, relative to ______________
Leaf count                  single / pair
Leaf size (measured)        ____ w × ____ h × ____ thick
Bevel visible on lock edge  yes / no / not observed

── CONSTRUCTION (L01) ──────────────────────────────────────────────────────
Leaf material               HM / wood solid / wood hollow / aluminum / FRP / glass
Leaf glazing                none / vision lite / half lite / full glass
Frame material
Frame type                  welded / KD / UNKNOWN — why:
Frame throat (measured, if accessible)
Wall construction, visible  masonry / stud+GWB / other
Wall extends to deck?       yes / no / UNKNOWN — why:
Adjacent glazing / sidelite / transom

── HARDWARE (L01, L03) ─────────────────────────────────────────────────────
Hinges                      butt / continuous / pivot;  count ____
  Barrels on which side?    secure / unsecure
  NRP or security studs?    yes / no / not observed
Lock type                   cylindrical / mortise / exit device / other
  Deadbolt present?         yes / no
  Deadlatch seated?         yes / no / not observed
Exit device type            rim / mortise / SVR / CVR / n-a
  Dogging present?          yes / no / n-a
Closer                      surface reg-arm / parallel / top-jamb / concealed / floor / none
Coordinator (pairs)         yes / no / n-a
Astragal / mullion          overlapping / split / fixed mullion / removable / none
Flush bolts (pairs)         manual / automatic / none / n-a
Stop                        wall / floor / overhead / none
Gasketing / seals           smoke / sound / weather / none observed
Threshold / sweep

── ELECTRIFIED (L03, L06) ──────────────────────────────────────────────────
Locking device              strike / mag / electrified lockset / electrified exit / none
  If mag: bond sensor?      yes / no / not observed
Card reader                 present? ____  side: secure/unsecure  jamb: hinge/strike
  Mounting height (approx)
Second reader (in/out)      yes / no
REX                         motion / lever switch / push button / none observed
  → REX on which side?      secure / unsecure
Door position switch        recessed / surface / none observed
Latch monitoring            evident / not evident / cannot determine
Power transfer (L06)        hinge / EPT / door loop / none observed / n-a
  → If none observed but
    the lock is in the leaf: FLAG THIS
Local sounder               yes / no

── FIRE RATING (L07) ───────────────────────────────────────────────────────
Leaf label present?         yes / no / painted over / not found
  Rating stated
  Transcribe label verbatim
Frame label present?        yes / no / not found
Closes and latches from
  ~5 degrees open?          yes / no / did not test — why:
Hold-open present?          listed magnetic / closer-holder / WEDGE OR PROP / none
Unapproved holes observed   describe, or "none observed"

── EGRESS (L05) ────────────────────────────────────────────────────────────
On the means of egress?     yes / no / UNKNOWN — need life safety plan
Opens from inside in ONE
  motion, no key?           yes / no        ← if NO, see rule 3
Panic / fire exit hardware  yes / no / n-a
Delayed egress?             yes / no
  Signage present?          yes / no / n-a
Anything chained, blocked,
  propped, or obstructed?   ← if YES, see rule 3

── ASSESSMENT (the actual exercise) ────────────────────────────────────────
1. Governing weakness of this opening, one sentence:

2. What is this opening's protection function? (deter/detect/delay/assess — L01 Foundations)

3. If I had to add access control here tomorrow, what would the construction force me
   to choose, and what would it cost me?

4. One thing I could not determine from observation, and who I would have to ask:

── PHOTOS ──────────────────────────────────────────────────────────────────
[ ] 1. Full opening from the unsecure side, swing visible
[ ] 2. Full opening from the secure side
[ ] 3. Hinge edge, close
[ ] 4. Strike jamb and strike, close
[ ] 5. Fire label, legible (or a photo of where it should be and isn't)
[ ] 6. Head of frame
[ ] +  Any defect or anomaly, close, with something for scale
```

---

## The findings memo

One page. Not a summary of the table — the table is the data, this is the engineering.

**Required sections:**

1. **Scope.** What you surveyed, when, and what you did not cover.
2. **Method.** How you determined handing, what you measured vs. estimated, what you could not
   access.
3. **The three most significant findings**, ranked. For each: what you observed, why it matters,
   and what you'd do about it. Cost or effort estimate if you can.
4. **Anything reported under rule 3**, and to whom, and when.
5. **What you could not determine and who owns the answer.** Life safety plan, keying schedule,
   as-built drawings, the AHC, the facilities manager.

**The memo is graded on section 3.** Sections 1, 2, 4, and 5 are hygiene.

---

## Self-assessment

Score yourself honestly. This is not a test anyone else is marking.

| | Not yet | Getting there | Solid |
|---|---|---|---|
| **Handing** | Had to think about it each time | Right, with a pause | Fifteen seconds, no hesitation, side recorded every time |
| **Naming components** | Pointed and described | Named most correctly | Named all of them, correctly, without looking anything up |
| **Frame type** | Couldn't tell | Right when the joint was visible | Right, and wrote UNKNOWN honestly when it wasn't |
| **Governing weakness** | Named the lock | Named the door or frame | Named the wall, the glazing, or the closer where that was the answer |
| **Latching test** | Skipped it | Did it on some | Did it on every rated opening and recorded the result |
| **Power transfer** | Didn't look | Looked, found the obvious ones | Found the concealed ones, and flagged the leaf-mounted device with no transfer |
| **Egress** | Recorded the hardware | Checked one-motion operation | Checked it, and knew which openings I couldn't classify without the life safety plan |
| **UNKNOWN discipline** | Left blanks | Wrote UNKNOWN | Wrote UNKNOWN with the reason, every time |
| **Findings memo** | Restated the table | Listed observations | Ranked findings with consequence and recommendation |

**The two rows that predict whether you're actually ready:** *governing weakness* and *UNKNOWN
discipline*. The first is the engineering. The second is the professional habit that makes your
work trustable by someone who wasn't there.

---

## What "good" looks like

A reference set of findings, written against a fictional building, is at
[`../_solutions/10_door_survey_reference.md`](../_solutions/10_door_survey_reference.md).

**Do the survey first.** Reading the reference before you go out will give you its findings
instead of yours, and the whole point is the ones you find.

---

## Where this goes next

The survey record you just built is, structurally, a **device register** — one row per opening,
typed fields, a mix of observed and derived values. That is not a coincidence.

- [`../../16_Automation/data_model/`](../../16_Automation/data_model/) — the 44-field schema this
  record is a hand-built cousin of. Compare your fields to the schema and note what it has that
  you didn't think to record.
- [`../../27_Labs/project_01_secure_one_door/BRIEF.md`](../../27_Labs/project_01_secure_one_door/BRIEF.md) —
  Project 1 takes one opening and designs it fully. You now have ten candidates from real life.
- [`../../33_Design_Review_QA/`](../../33_Design_Review_QA/) — reviewing someone else's survey is
  the next skill.
