# Solutions — 08 Key Management and Mechanical Security

---

## E8.1 — Design the hierarchy

**Given:** 6-story office building. 4 facilities technicians needing all mechanical/electrical
rooms building-wide. One tenant per floor with their own suite. 2 security officers needing
access everywhere. Cleaning contractor on floors 1–3.

### The design

```
                        ┌──────────────────┐
                        │       GMK        │   2 keys — security officers
                        │  Grand Master    │   opens everything below
                        └────────┬─────────┘
              ┌──────────────────┼──────────────────┐
     ┌────────▼────────┐ ┌───────▼────────┐ ┌───────▼────────┐
     │      MK-M       │ │     MK-C       │ │  (tenant MKs)  │
     │   Mechanical    │ │   Cleaning     │ │  MK-1 … MK-6   │
     │  & Electrical   │ │  Floors 1-3    │ │  one per floor │
     │   building-wide │ │  common areas  │ │                │
     │    4 keys       │ │    ~6 keys     │ │  held by each  │
     └────────┬────────┘ └───────┬────────┘ │  TENANT, not   │
              │                  │          │  by the owner  │
        CK per room        CK per space      └───────┬────────┘
        M-101, M-201...    (as needed)          CK per door
                                                within the suite
```

| Level | Opens | Keys issued | Justification |
|---|---|---|---|
| **GMK** | Everything | **2** | Security officers need building-wide access. This is the only role that genuinely does. |
| **MK-M** | All mechanical/electrical rooms, all floors | **4** | The stated facilities requirement, exactly. Note it is a *functional* master (all rooms of a type) rather than a *geographic* one. |
| **MK-C** | Floors 1–3 common areas and cleaning closets | **~6** | Contractor scope. Deliberately does **not** include tenant suites — see below. |
| **MK-1..6** | One tenant suite each | Per tenant | Each tenant masters their own suite. |
| **CK** | Individual openings | As needed | |

### The decisions worth defending

**No floor masters for the owner.** There is no stated role that needs "everything on floor 2."
The tenant masters their own suite; facilities needs mechanical rooms, not offices; security has
the GMK. A floor master would be a level that exists because it feels tidy, and lesson 08's rule
is that the hierarchy mirrors the responsibility structure and goes no deeper.

**MK-M is functional, not geographic.** "All mechanical rooms, all floors" matches what the four
technicians actually do. A geographic split would have needed six keys per technician or six
masters, both worse.

**Cleaning does not get tenant suite access on a master.** If a tenant wants their suite cleaned,
that is a tenant decision and it should be a change key issued by the tenant and recorded against
their own register. Putting tenant suites on the cleaning master means a contractor's key loss
rekeys three tenants' suites — and it means the tenants' security depends on a program they
don't control and can't audit.

**Tenant masters are held by the tenant.** This matters legally and operationally: the tenant
controls their own space, and the building owner's liability for a tenant key is not a liability
they want.

### What I would also specify, beyond the hierarchy

- **Restricted keyway** throughout. Without it, the count of existing keys is unknowable and the
  hierarchy is decorative.
- **SFIC**, so that a tenant turnover — which happens on a lease cycle, predictably — is a core
  swap rather than a locksmith visit.
- **GMK and control key in an electronic key cabinet** with logged issuance and return.
- **The cleaning contractor's keys issued to the contracting company against a signed
  register**, returned at contract end, with the rekey cost for non-return written into the
  contract. This is the single most-skipped clause and it's the one that pays.

### The honest note

Total keys at or above master level: 2 GMK + 4 MK-M + ~6 MK-C = **12 keys that open more than
one opening**, plus one control key. Twelve is a number a program can actually audit. A
hierarchy that produces sixty is a hierarchy nobody will audit, and an unauditable program is
not a program.

---

## E8.2 — Rekey scope and relative cost

**(a) A tenant employee loses their suite change key.**
**Scope:** that opening, or that small change-key group.
**Cost: low.** One core, a handful of replacement keys for others holding the same change key.
With SFIC, minutes of labor.
**Judgment call:** if the key was unmarked and lost off-site, the practical risk may be low
enough that the tenant reasonably declines to rekey. That's their decision; make sure it's a
decision and not a shrug.

**(b) A facilities technician terminated, mechanical master not returned.**
**Scope:** every mechanical and electrical room in the building — the whole MK-M group — plus
reissue of the master to the remaining three technicians.
**Cost: moderate to high**, scaling with the room count. On a 6-story building this could be 30+
cylinders.
**The aggravating factor:** mechanical and electrical rooms are exactly where someone with a
grievance can do the most damage, and they are typically unmonitored. This one gets rekeyed,
promptly, and the cost is not the deciding input.

**(c) The SFIC control key cannot be located.**
**Scope: every core in the system.** The control key removes cores. Whoever holds it can pull any
core in the building and replace it with one of their own, silently, leaving a lock that looks
identical and opens to a key you don't know about.
**Cost: the highest on this list.** A full system core replacement plus a new control key plus
reissue of every key at every level.
**Note the asymmetry:** the control key isn't even a *door* key — it opens nothing on its own —
which is exactly why it gets treated casually. Lesson 08's warning about SFIC is this scenario.

**(d) 15-year-old building, no keying records ever kept.**
**Scope: everything, and you cannot scope it any other way**, because scoping requires knowing
what opens what and who holds it. Neither is knowable.
**Cost: the highest in practice**, because it is a full system replacement rather than a rekey,
and it comes with the discovery work of finding every opening first.
**The real finding:** this building has had no mechanical security for some unknown fraction of
15 years, and nobody can say how many keys are in circulation. The correct recommendation is a
full rekey to a restricted keyway with SFIC and a key control program stood up at the same time —
because rekeying without the program just resets the clock on the same failure.

> 🧠 **Ranking these by cost gets the exercise half right. The other half is noticing that (c)
> and (d) are different in kind:** (a) and (b) are incidents a working program handles. (c) and
> (d) are program failures, and rekeying without fixing the program buys you nothing but time.

---

## E8.3 — Construction key turnover verification, 200 openings

**What is verified:** that the construction keying no longer operates, **per opening**, and that
the permanent keying does.

**Aggregate sign-off is not acceptable** and this is the crux of the exercise. "The contractor
confirms all construction cores have been replaced" is the sentence that lets 20% of the
openings stay open forever. A blanket certification is exactly the artifact produced when nobody
walked the building.

**The procedure:**

| Step | What happens | Evidence retained |
|---|---|---|
| 1 | Owner (or owner's rep) takes possession of the permanent cores and permanent keys **before** the exercise begins. Count them against the keying schedule. | Signed receipt; count reconciliation against the schedule |
| 2 | For each of the 200 openings: install/verify the permanent core, or verify the permanent change key has been operated once where conventional construction keying is used. | Per-opening line item, initialled and dated by the person who did it |
| 3 | For each opening: **attempt the construction key.** It must not operate. | Per-opening pass/fail, initialled |
| 4 | For each opening: **operate the permanent change key.** It must operate. | Per-opening pass/fail, initialled |
| 5 | For each opening on a master: **operate the applicable master.** It must operate. | Per-opening pass/fail |
| 6 | Account for the **construction cores** physically — all of them, counted, returned or destroyed. Not "returned to the contractor." | Count reconciliation; disposition record |
| 7 | Account for **construction keys** — every one issued, returned or documented as unrecoverable. | Issuance register with returns |
| 8 | Owner's rep spot-checks **10% of openings independently**, selected by the owner, not by the contractor. | Spot-check record with the openings named |
| 9 | Formal transfer of the permanent keys and the control key to the named key control owner. | Signed transfer, naming the individual and role |

**Who:** step 2–5 by the hardware contractor or locksmith; step 8 by the owner's rep or the
security consultant; step 9 between the contractor and the named key control owner.

**What triggers a hold on substantial completion:**

- **Any opening failing step 3** — a construction key that still operates.
- **Any opening not covered** by a completed per-opening record. Missing is a fail, not a
  pending.
- **Any unaccounted-for construction core or key**, unless the disposition is documented and the
  affected openings have been rekeyed.
- **Any spot-check failure in step 8** — and a spot-check failure triggers re-verification of
  100%, not just the failed opening, because it means the record is not trustworthy.
- **No named key control owner** to receive the keys in step 9. If there is nobody to hand them
  to, the handover has not happened.

**The clause that makes it work, in the substantial completion criteria:**

> Substantial completion is contingent on a completed per-opening construction key turnover
> record for all 200 openings, an owner-selected 10% spot-check with zero failures, full
> accounting of construction cores and keys, and signed transfer of permanent and control keys
> to the owner's named key control representative.

> 🧠 **Why this is worth the friction:** this is the single most reliably-skipped step in
> commercial construction, and its failure mode is silent and permanent. A building whose
> construction key still works has no mechanical security and no way to discover that. The cost
> of the verification is a day of somebody's time. The cost of skipping it is the building.

---

## E8.4 — What else should they spend money on?

Model answer (191 words):

> Honestly? Not much on hardware. The thing that would most improve your security costs almost
> nothing, and it's this: find out who has keys.
>
> Every one of those doors also opens with a mechanical key — that's by design, because somebody
> has to get in when the power's out. Which means a person with the right key walks past the
> entire $400,000 system and it logs nothing. Not a suspicious event. Nothing.
>
> So the question I'd want answered before spending another dollar: how many master keys exist,
> who has them right now, and when was that last physically checked? In most buildings I walk,
> nobody can answer any of the three.
>
> What that looks like in practice: a written key control policy, one named person who owns it,
> a register of who holds what, key return built into your offboarding checklist alongside the
> laptop, and an annual audit where somebody physically sights the masters. If your keyway isn't
> restricted, moving to one is the one purchase I'd make — it's what lets you actually know how
> many keys exist.
>
> That's a policy project, not a procurement. It costs you a few weeks of somebody's attention
> and it's worth more than anything else on your list.

**What makes it work:** answers the question honestly rather than upselling, explains the
mechanism in one sentence so the recommendation isn't just an assertion, gives three concrete
questions the executive can go ask today, and names exactly one purchase. It is deliberately the
answer that reduces the consultant's own scope — which is the point of the exercise and, per
lesson 01 of Foundations, the job.

---

## E8.5 — No-override openings at a data center campus

**Openings I would specify with no mechanical override:**

| Opening | Why |
|---|---|
| Data hall cage / cabinet-level enclosures | Highest consequence; a key override here defeats cabinet-level access logging, which is the whole control |
| Vault or secure media storage room | Consequence tier; the override is a permanent bypass of every electronic control |
| Secure destruction / media handling room | Same |
| Cross-connect / meet-me room, where tenant separation is contractual | A single override key crossing tenant boundaries is a contractual problem as well as a security one |

**Openings I would NOT include, despite the temptation:**

- **Any door on the means of egress.** Egress is mechanical and unaffected by this decision, but
  don't create ambiguity at those openings.
- **Data hall entry doors themselves.** Emergency access to a data hall is an operational
  necessity — hardware failure, environmental event, fire service. The cage inside is the right
  place for the no-override decision, not the hall.
- **Mechanical, electrical, and cooling plant rooms.** An operator who cannot get to a chiller at
  0300 is a bigger risk than the one you're mitigating.

**The emergency access procedure that replaces the key:**

1. **Who is authorized to request** entry, by role, and who approves. Two-person authorization at
   this tier.
2. **The mechanism:** a documented forced-entry procedure — locksmith on retainer with a defined
   response time, or a drill-and-replace procedure with pre-staged replacement hardware on site,
   or a secondary electronic path on independent power and an independent controller.
3. **The realistic time to access**, stated in hours, and confirmed with the owner that it is
   acceptable.
4. **What is logged** and who reviews it afterward.
5. **Pre-staged replacement hardware on site**, so the recovery is same-day.

**What I need in writing from the owner:**

> Acknowledgement that openings `[list]` are specified without mechanical key override; that in
> the event of a total electronic failure, entry to these spaces requires `[procedure]` with an
> expected time to access of `[  ]`; that this delay has been evaluated against the operational
> impact of being unable to enter these spaces; and that the owner accepts it.

Signed by someone with the authority to accept it. This is a residual-risk acceptance, and per
`../../01_Foundations/02_the_risk_vocabulary.md`, residual risk is accepted by the owner, not by
the engineer.

**Fire service access — handled separately and not traded away:**

Fire department access arrangements are a **code and AHJ matter**, not a design preference.
`[CODE][VERIFY]` Address it explicitly:

- Confirm what the AHJ requires for these spaces. A key box (Knox box or equivalent) may be
  required, and its contents are specified by the fire department.
- **A no-override decision does not override a fire service access requirement.** If the AHJ
  requires access to a space, that is the answer, and the no-override list shrinks accordingly.
- Document what is in the key box, who maintains its contents, and when it was last verified.
  Lesson 08's warning applies: the contents are routinely stale.

> 🧠 The exercise is really testing whether you make the no-override call *deliberately and
> narrowly*. A learner who lists every secure door has misread it — the override exists for a
> reason and removing it has a real operational cost. A learner who lists nothing has also
> missed it: at the highest tier, a permanent bypass of every electronic control is a legitimate
> thing to refuse.

---

## E8.6 — Grade 1 patented cylinders with no key control program

**The review comment:**

> **General comment — mechanical security specification.**
>
> The set specifies Grade 1 high-security cylinders with a patented keyway at all 61 openings.
> The hardware selection is sound and I'm not asking for it to change. My concern is that it is
> currently the *only* mechanical security control on the project, and it is the one that does
> the least on its own.
>
> A patented keyway controls **duplication**. It does not control **issuance**. If the building
> has no key control policy, no named owner, no issuance register, and no audit, then within
> three years nobody will be able to say how many keys exist or who holds them — and the
> cylinders will have delivered none of what they were bought for. The keyway is what makes the
> key count *knowable*; the program is what makes it *known*.
>
> **Requested additions to the scope:**
>
> 1. A **key control policy** — issuance, records, return on separation, audit frequency, rekey
>    triggers, and secure storage of the keying schedule itself.
> 2. A **named owner**, by role, in the O&M handover. This is the item most likely to be
>    dropped and it is the one that makes the rest function.
> 3. **Key return integrated with the owner's offboarding process**, so a departing employee's
>    keys are on the same checklist as their laptop.
> 4. **Construction key turnover as a per-opening verified line item** in the commissioning
>    checklist, with a hold on substantial completion. Aggregate certification is not
>    acceptable.
> 5. An **electronic key cabinet** for masters and the control key, with logged issuance.
> 6. Review of the **keying hierarchy** — please provide the keying schedule. At 61 openings I'd
>    expect a shallow hierarchy, and I want to confirm no high-consequence opening is sitting on
>    a broad master for convenience.
>
> Items 1–4 are documentation and process, not procurement. Item 5 is the only cost.
>
> To be clear about the framing: the cylinder selection is the right call and I'd keep it. It's
> just that the cylinders are the part someone was selling, and the program is the part nobody
> was.

**What makes it a good review comment:**

- **Endorses the hardware first, sincerely.** The colleague did something correct and the comment
  says so, which is what allows the criticism to land as engineering rather than as a takedown.
- **Names the precise gap in one sentence:** duplication control vs. issuance control. That
  distinction is the whole finding.
- **Six concrete requests**, four of which cost nothing, so the response can start immediately.
- **Asks for the keying schedule**, which is the document that will reveal whether there's a
  second problem underneath.
- **Closes by naming the structural reason this happens** — hardware has a vendor and a program
  doesn't — which is both true and non-accusatory.
