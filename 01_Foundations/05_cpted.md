# 05 — CPTED: Crime Prevention Through Environmental Design

## Learning objectives

- State the CPTED strategies and explain the behavioral mechanism behind each.
- Apply CPTED analysis to a site and produce recommendations that cost little or nothing.
- Explain why CPTED is usually the highest risk-reduction-per-dollar available.
- Recognize the tension between CPTED and hardening, and resolve it.
- Know CPTED's limits and where it does not apply.

---

## ELI5

Two convenience stores. Same neighborhood, same hours, same merchandise.

**Store A:** windows covered with sale posters, the register tucked behind a tall aisle at the
back, a dark parking lot, an alley entrance with a dumpster next to it, weeds, and graffiti
nobody removed.

**Store B:** clear sightlines from the street to the register, the register visible from
outside, well-lit lot, one clearly marked entrance, trimmed landscaping, and everything
clean.

Store A gets robbed. Store B doesn't. Neither one bought a security system.

The *design of the place itself* changed the behavior of the people in it. That's CPTED.

---

## What CPTED is, and why an engineer should care

**CPTED** (usually pronounced "sep-ted") is the practice of designing the built environment to
reduce the opportunity for and fear of crime, by influencing the behavior of both legitimate
users and potential offenders.

It originates in criminology — Jane Jacobs's observations about "eyes on the street," Oscar
Newman's *defensible space*, and C. Ray Jeffery's 1971 book that gave it the name. `[PRACTICE]`
Modern practice distinguishes "first generation" CPTED (the physical strategies below) from
"second generation" CPTED (social cohesion, community capacity — outside an engineer's scope
but worth knowing exists).

**Why it matters to you specifically:**

1. **It is nearly free if applied early.** Moving a reception desk on a schematic-design plan
   costs nothing. Moving it after construction costs $40,000. Your leverage over CPTED is
   greatest at exactly the phase when juniors are usually not in the room — so learn to speak
   up in SD.

2. **It reduces the number of devices you need.** Every sightline you create is a camera you
   don't buy, power, license, and maintain for 10 years.

3. **It's what the architect can actually act on.** An architect cannot install your card
   reader, but they absolutely can move a door, change a window, adjust a grade, or reposition
   a desk. CPTED is the vocabulary that makes you useful to the design team rather than the
   person who shows up late with a device schedule.

4. **Some jurisdictions require CPTED review** for certain project types `[VERIFY locally]`,
   and many police departments offer CPTED assessments.

---

## The strategies

Different sources organize these as three, four, five, or six strategies. The substance is
stable; the count varies. Here is the full set with the mechanism behind each.

### 1. Natural Surveillance — "see and be seen"

**Goal:** maximize the chance that an offender is observed, and their *perception* of that
chance.

**Mechanism:** offenders avoid being seen. Visibility raises perceived risk of apprehension
even when nobody is actually watching.

**Design moves:**
- Sightlines from occupied spaces to vulnerable areas (lobby to parking, office to entry)
- Window placement and *not* covering the windows you paid for
- Lighting — uniform, glare-free, at the right height (see below)
- Landscaping: **the 3-foot / 6-foot rule** — shrubs trimmed below ~3 ft, tree canopies raised
  above ~6–8 ft, preserving a clear visual band at human height. `[GUIDELINE]`
- Avoid recessed entries, blind corners, alcoves, and stair returns that create concealment
- Elevator lobbies visible from occupied areas; elevator cabs with a view or a mirror
- Parking layout: perpendicular parking with sightlines beats angled rows behind screening
- Transparent stair enclosures where code and fire rating permit `[CODE][VERIFY]`

**Lighting is the highest-leverage natural surveillance tool, and it's usually done badly:**
- **Uniformity beats brightness.** A lot with one very bright pole and deep shadows is worse
  than a uniformly moderate lot. Deep shadows adjacent to bright areas destroy both human and
  camera vision (the eye and the sensor both adapt to the bright area). Specify average-to-
  minimum uniformity ratios, not just footcandles `[GUIDELINE — see IES recommendations,
  VERIFY current]`.
- **Glare is a security failure.** A light that shines in a guard's or camera's eyes creates
  a dark zone behind it. Full-cutoff fixtures.
- **Color rendering matters** for suspect description. Low-pressure sodium (monochromatic
  yellow) makes "blue jacket" impossible. LED with decent CRI is the modern default.
- **Light where people are, not where the fixture is convenient.** Vertical illuminance on
  faces is what identifies people; horizontal illuminance on pavement is what gets specified.

### 2. Natural Access Control — guide people where you want them

**Goal:** channel movement to controlled, observable routes and make unauthorized routes feel
wrong.

**Mechanism:** most people follow designed paths. Offenders seeking an unobserved route find
fewer options, and using one is conspicuous.

**Design moves:**
- **One clearly dominant public entrance.** A building with five equally plausible entrances
  has no reception function, no matter how good the receptionist is.
- Paths, paving changes, and landscaping that direct pedestrians
- Low walls, planters, bollards, and grade changes as symbolic (not physical) barriers
- Reception positioned so the *only* natural route inward passes it
- Doors that are for egress-only clearly not-an-entrance in appearance
- Parking layout that puts visitors where you want them, near observation
- Fencing and gates that make the intended route obvious

> ⚠️ **The most common CPTED failure in commercial buildings:** the "convenience" door.
> An employee side entrance near the parking lot, added because walking around is annoying.
> It becomes the *de facto* main entrance, bypasses reception entirely, is propped daily, and
> undoes the entire access control concept. This is a design problem that manifests as a
> behavior problem. You cannot fix it with a door alarm — you fix it by understanding walking
> patterns during design and putting the controlled entrance where people actually want to
> walk.

### 3. Territorial Reinforcement — signal ownership

**Goal:** make it obvious that a space is owned, cared for, and watched — so an intruder feels
conspicuous and legitimate users feel responsible.

**Mechanism:** offenders read environmental cues about whether behavior will be challenged.
Ambiguous, unowned-looking space invites use. Clearly owned space feels risky to loiter in.

**Design moves:**
- Clear transitions from public → semi-public → private (paving changes, thresholds, gateways,
  signage, landscaping)
- Property line definition even where a fence isn't warranted
- Signage that communicates ownership and expectations
- Consistent, well-maintained appearance
- Personalization of space by occupants (a workspace people care about gets watched)
- Eliminating ambiguous leftover space (the gap between two buildings that belongs to nobody)

### 4. Maintenance / Image — the broken windows effect

**Goal:** signal that the environment is monitored and deviations are noticed.

**Mechanism:** visible disorder (graffiti, broken lights, litter, damaged fencing, dead
landscaping) signals that nobody is paying attention and that misbehavior has no consequence.

**Design moves:**
- **Specify for maintainability.** Graffiti-resistant coatings, vandal-resistant fixtures,
  accessible fixtures (a light nobody can reach won't get relamped), durable finishes.
- Rapid-repair policy: graffiti removed within 24–48 hours, lights replaced promptly, fence
  damage fixed immediately.
- Design out the things that break: bollard-protect what vehicles hit, avoid finishes that
  show wear, avoid landscaping that requires irrigation nobody will maintain.

> 🧠 **The engineer's angle on maintenance:** you influence this through *specification*, and
> it is one of the most durable contributions you can make. A vandal-resistant, easily
> relamped, accessible fixture keeps working for 15 years. A beautiful, unreachable one is
> dark within 18 months and dark forever.

### 5. Activity Support — put legitimate activity in vulnerable places

**Goal:** increase the presence of legitimate users in areas that would otherwise be empty and
unobserved.

**Mechanism:** natural surveillance requires someone to do the surveilling. Occupied space
is self-policing.

**Design moves:**
- Locate break rooms, café seating, or workstations to overlook parking or entries
- Program plazas and courtyards with actual uses, not just paving
- Route high-traffic circulation past areas needing observation
- Avoid creating dead zones: service corridors, unused mezzanines, over-provisioned lobbies
- Schedule activity into otherwise-empty hours where practical

### 6. Target Hardening — the last resort, not the first

Physical strengthening: locks, bars, safes, glazing, barriers.

CPTED literature traditionally lists this *last and reluctantly*, because hardening can
undermine the other strategies. Bars on windows destroy natural surveillance and signal a
dangerous area — which reduces legitimate activity, which reduces surveillance, which
increases crime. The "fortress effect."

**The correct sequence:** apply strategies 1–5 first, then harden the residual. This is not
CPTED ideology; it's cost engineering. Hardening is the most expensive risk reduction per
dollar, and the strategies above are the cheapest.

---

## 🔧 CPTED site analysis method

A repeatable procedure you can run in 60–90 minutes.

**Preparation:** get a site plan and a floor plan. Note the hours of operation, staffing,
and any incident history.

**Step 1 — Approach as each user type.** Walk the site as: a first-time visitor, an employee
arriving at 0600 in the dark, a delivery driver, a contractor, and someone with no legitimate
business. *Where does each naturally go?* Note every point where the intended path is unclear.

**Step 2 — Sightline mapping.** From each occupied position (reception, workstations, guard
post), mark on the plan what can actually be seen. Then mark every vulnerable area (entries,
parking, service areas, secluded spots). **The vulnerable areas not covered by any sightline
are your findings.**

**Step 3 — Concealment inventory.** Walk the site looking specifically for places a person
could stand unobserved within 20 feet of an entry or path: alcoves, landscaping, dumpsters,
mechanical screening, column recesses, stair returns, vehicle screening walls, blind corners.
Photograph each.

**Step 4 — Lighting survey.** At night, with a light meter if you have one. Record: dark
zones, glare sources, non-functioning fixtures, uniformity by eye (can you see a face at
30 feet?), and whether the lighting supports the cameras that exist.

**Step 5 — Territorial reading.** At each transition (property line, plaza to building, lobby
to office), ask: *would a stranger know they were crossing into more private space?* If not,
that's a finding.

**Step 6 — Maintenance walk.** Graffiti, broken fixtures, damaged fencing, dead landscaping,
overgrowth, litter, propped doors, defeated hardware. Photograph everything. The propped doors
are the most informative finding on any site — they tell you exactly where your access control
concept is fighting how people actually move.

**Step 7 — Write findings as observations + mechanisms + recommendations.**

Bad finding: *"Lighting is poor in the east lot."*
Good finding: *"The east lot (approx. 40 spaces, used by second-shift staff departing after
2300) has three non-functioning pole fixtures, producing dark zones of approximately 60 ft
diameter at the northeast corner adjacent to the perimeter landscaping. Employees walking to
these spaces cannot be observed from any occupied position, and the adjacent 6-ft-tall
untrimmed shrubs provide concealment within 10 ft of the walking path. Recommend: (1) restore
the three fixtures [immediate, ~$1,200]; (2) trim shrubs to 3 ft and maintain [immediate,
~$800/yr]; (3) verify average:minimum illuminance uniformity meets target after relamping
[VERIFY target against IES guidance and any local requirement]; (4) if uniformity remains
inadequate, add two fixtures [~$9,000]."*

The second one gets funded. It states what, where, who's affected, why it matters, and what
it costs.

---

## Tradeoffs and tensions

| Tension | Resolution |
|---|---|
| **Natural surveillance vs. privacy** | Glazing gives sightlines and also exposes occupants and screens. Use height, glazing type, and layout — you can have visibility of the *path* without visibility of the *desk*. |
| **Natural surveillance vs. energy code / solar gain** | Glazing has thermal cost. Coordinate with the architect early; shading devices can preserve sightlines if designed for it. |
| **Access control vs. accessibility** | The accessible route must be a *dignified, primary* route, not a back door. And it is often the easiest adversary route. Control it properly rather than treating it as an exception. |
| **Territorial reinforcement vs. welcoming design** | Retail, healthcare, and civic buildings want to feel open. Use subtle cues (materials, level changes, lighting) rather than fences. |
| **Hardening vs. the fortress effect** | Harden the least-visible layer. A hardened door in an interior corridor doesn't signal danger; bars on the street-facing window do. |
| **CPTED vs. an existing building** | Retrofit CPTED is mostly landscaping, lighting, signage, furniture, and locking policy. Still cheap, still effective, just less powerful. |

---

## Limits — where CPTED does not help

Be honest about this; over-claiming CPTED is a credibility risk.

- **Insiders.** CPTED works on people who don't belong. It does nothing about an authorized
  employee.
- **Determined and prepared adversaries.** Someone who has surveilled the site and accepts
  the risk of being seen is not deterred by sightlines.
- **Impaired or irrational offenders.** The mechanism is risk-perception; if risk isn't being
  perceived, the mechanism doesn't engage.
- **Remote or unoccupied sites.** Natural surveillance requires someone to surveil. A remote
  substation at 3 a.m. has no eyes; that's a detection and response problem.
- **High-consequence, low-frequency events.** You do not counter a vehicle-borne attack with
  landscaping. Standoff and barriers are the answer there.
- **Evidence base.** CPTED's effectiveness is supported but the research is uneven across
  strategies and contexts, and effects can include displacement rather than reduction.
  `[PRACTICE]` Claim it as good practice, not as a guaranteed percentage.

---

## Junior vs. Senior

**Junior:** knows the strategies; can identify concealment and sightline problems on a walk;
writes findings with specific locations.

**Senior:** raises CPTED issues in schematic design when they're free to fix; can persuade an
architect to move a reception desk without making it a turf fight; anticipates the
"convenience door" problem before the building is occupied; knows which CPTED recommendations
the client will actually maintain (and doesn't recommend landscaping to a client with no
grounds budget); and distinguishes clearly between what CPTED will and won't do so the
security concept doesn't rest on it.

---

## Exercises

**E5.1** Run the full 7-step CPTED analysis on a site you can legally observe. Produce at
least eight findings in the "good finding" format, each with location, affected users,
mechanism, and a costed recommendation.

**E5.2** For each condition, name the CPTED strategy violated and give a low-cost and a
high-cost remedy:
- (a) A parking garage stair tower with solid concrete walls and no windows.
- (b) A retail store with the entire storefront covered in promotional posters.
- (c) An office building with four unlocked entrances, all equally prominent.
- (d) A campus courtyard with dense 8-ft hedges along the main walking path.
- (e) A loading dock with a dumpster enclosure adjacent to the personnel door.
- (f) A plaza with no seating, no shade, and no reason for anyone to be there.

**E5.3** An architect proposes a dramatic two-story glass lobby with the reception desk set
back 60 feet from the entrance, positioned facing the elevator bank. Identify the CPTED
problems and propose a solution that preserves the architect's design intent. (This matters:
"no" is not a deliverable — "yes, and here's how" is.)

**E5.4** You have $15,000 and a shopping-center site with: dark rear service alley, overgrown
landscaping at the front entrances, graffiti on the east wall, three burned-out lights, no
signage at the property line, and a vacant unit with papered windows. Allocate the money and
justify the order.

> Solutions: [`_solutions/05_cpted_solutions.md`](_solutions/05_cpted_solutions.md)

---

## Retrieval check

1. Name the six CPTED strategies and the behavioral mechanism behind each.
2. What is the 3-foot/6-foot rule and what strategy does it serve?
3. Why is lighting uniformity more important than lighting brightness?
4. Why does CPTED literature list target hardening last?
5. What is the "convenience door" problem and why can't a door alarm fix it?
6. Name four situations where CPTED provides little or no benefit.
7. What makes a written CPTED finding fundable?

---

## References

- Newman, O., *Defensible Space* (1972). `[PRACTICE]` The foundational text.
- Jeffery, C.R., *Crime Prevention Through Environmental Design* (1971). `[PRACTICE]`
- Crowe, T.D. / Fennelly, L.J., *Crime Prevention Through Environmental Design*, current ed.
  `[PRACTICE]` The standard practitioner reference.
- ASIS International — *Protection of Assets*, Physical Security volume, CPTED sections.
  `[GUIDELINE]`
- Illuminating Engineering Society (IES) — recommended practices for exterior and parking
  facility lighting. `[GUIDELINE]` `[VERIFY current documents and values]`
- International CPTED Association (ICA) — practitioner resources. `[PRACTICE]`
- Your local police department's crime prevention unit — many perform free CPTED assessments
  and it is worth attending one.

**Next:** [06 — Requirements Engineering](06_requirements_engineering.md)
