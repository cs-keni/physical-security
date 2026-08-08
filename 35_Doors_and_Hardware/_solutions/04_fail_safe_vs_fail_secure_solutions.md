# Solutions — 04 Fail Safe vs. Fail Secure

---

## E4.1 — Fail state selection

**(a) Server room, electrified mortise lockset, no panic hardware required.**
**Fail secure.** Egress is mechanical via the inside lever, so nothing is traded away; a power
event must not open the room. Add the mechanical key override and decide who holds it.

**(b) Stair door, floor-to-stair, 90-min rated, re-entry required on alarm.**
**Fail secure latch, with the re-entry function released on fire alarm.**

This opening has two requirements that sound contradictory and aren't. The fire rating requires
the door to be **self-latching** — a fire door that doesn't latch doesn't hold back smoke and
fire. The re-entry requirement means that on alarm, a person in the stair must be able to get
back onto the floor.

The resolution: the *latch* stays mechanical and always latches; the *outside (stair-side)
trim* is what gets released on alarm, so the lever works from the stair without a credential.
The door is still closed and still latched; it is just no longer credential-controlled from the
stair side. `[CODE][VERIFY]`

Getting this distinction right — "release the trim, not the latch" — is the difference between
a compliant stair door and a fire door that has been defeated in the name of life safety.

**(c) All-glass lobby entrance with a magnetic lock.**
**Fail safe** — no choice; the device has no mechanical egress. Plus the full arrangement:
sensor release, manual release device that directly interrupts power, release on power loss,
hardwired fire alarm release, signage. `[CODE][VERIFY]`

**(d) Loading dock personnel door, out-swinging, electric strike retrofit.**
**Fail secure.** Egress mechanical via the inside lever. A dock door is exactly the opening
where a power interruption should *not* produce an unlocked exterior door — it is accessible,
often unobserved, and adjacent to goods.

Also, separately from the fail state: out-swinging means **NRP hinges or security studs**, and
verify the existing lock has no deadbolt function before committing to a strike.

**(e) Cash counting room in a retail back-of-house.**
**Fail secure.** Consequence-driven, and egress is mechanical. Verify whether any
industry-specific or insurer requirement applies — cash-handling spaces sometimes carry
contractual security requirements that exceed code, and those come from the insurer or the
operator, not from the building code. `[VERIFY]`

---

## E4.2 — Responding to "all egress doors should be fail safe"

Model answer (143 words):

> You're right that life safety comes first — that's not negotiable and I'm not arguing with
> it. The conclusion is where it comes apart.
>
> On an electrified lockset or an exit device, egress is already mechanical. The inside lever
> and the push bar are physical linkages; they aren't electrified and they don't care whether
> there's power. Someone inside gets out with the panel dead, the network down, and the
> building on fire. Fail secure controls the *outside* lever only.
>
> So specifying fail safe everywhere doesn't buy any life-safety benefit we don't already have.
> What it does buy is a building that unlocks itself the moment the power drops — including
> when someone drops it deliberately.
>
> The exception is magnetic locks, which have no mechanical egress at all. Those are fail safe
> by necessity, and that's the argument for using fewer of them.

**Why it works:** it opens by agreeing with the principle sincerely, isolates exactly one
factual error, gives the mechanism rather than an assertion, names the cost of the wrong
conclusion, and ends by granting the case where they're right. Nobody has to lose.

---

## E4.3 — API-based fire alarm release

**Failure modes introduced:**

1. **Silent failure of the message path.** Network outage, firewall rule change, VLAN
   reconfiguration, expired certificate, DNS failure, a service that didn't restart after
   patching. Every one of these produces the same observable behavior: nothing. The doors stay
   locked and no one is told.
2. **Dependency on two head-end servers.** Either one being down, mid-reboot, mid-upgrade, or
   mid-database-maintenance breaks the release path. Both servers are general-purpose computers
   with patch cycles.
3. **Dependency on software version compatibility across two vendors, for the life of the
   building.** The integration works on the versions installed at commissioning. In year six,
   one vendor's upgrade changes the API and the integration quietly stops working. Nobody tests
   it, because testing it requires knowing it exists.
4. **Latency and ordering are undefined.** How long between alarm and release? Under what queue
   depth? During the network storm that a real incident produces?
5. **Failure direction is wrong.** A hardwired normally-closed contact fails to *released* — a
   cut wire looks exactly like an alarm. A message-based path fails to *locked*. The
   safe-failure property is inverted.
6. **Not meaningfully testable by the people who will own it.** A facilities tech can pull a
   station and watch a door release. They cannot verify an API integration, and they will not.
7. **Single point of failure with no annunciation.** Nothing on either system says "the release
   path is broken." Compare a supervised circuit, which reports its own failure.
8. **Change control is outside the security team.** An IT change to network segmentation — made
   for good reasons by people who have never heard of this integration — silently disables a
   life-safety function.

**My position, and how I'd state it:**

> The release must be a hardwired path: a dry contact from the fire alarm system that
> physically interrupts power to the locking devices, independent of both head-end systems and
> of the network. `[CODE][VERIFY]`
>
> I'm not against the integration — add it *on top*, for logging and situational awareness.
> That's genuinely useful and it's the part you actually want. But it can't be the release
> path, for the same reason we don't implement a machine's emergency stop in application code:
> the mechanism that has to work when everything else has failed cannot depend on everything
> else working.
>
> On the conduit: I'd rather spend that money than own this failure mode. If the routing is the
> real problem, let's look at where the panels are — there may be a shorter path than the one
> being priced.

**Note the posture.** The person proposing this is trying to solve a real problem (conduit
cost) and offering a real benefit (logging). Take the benefit, refuse the substitution, and
help with the actual constraint.

---

## E4.4 — The hour-5 memo paragraph

Model answer:

> **Extended power outage — what happens after the battery.**
>
> The access control system at [building] is backed by a 4-hour battery. During those four
> hours everything operates normally: badges work, doors lock and unlock on schedule, and
> events are logged. At approximately hour 5 of a total power loss, the battery is exhausted
> and the electrified locks lose power. Because the locks are specified fail secure, every
> access-controlled door **remains locked**. People inside can still leave — the interior levers
> and push bars are mechanical and are unaffected. But nobody can badge in, anywhere, until
> power is restored, and no access events are recorded during that period. Entry during the
> outage would be by mechanical key only, from the [location] key cabinet.
>
> There are two ways to change this outcome. **Option A: extend the battery duration** to cover
> your expected worst-case outage — this is a straightforward capacity increase at the power
> supplies, with a cost and a physical space requirement at each. **Option B: put the access
> control system on the generator**, which makes outage duration irrelevant but requires
> capacity on the generator and a transfer arrangement at each panel.
>
> Which is right depends on how long your realistic worst-case outage is and on what generator
> capacity is already available — both of which are your call and your facilities team's, not
> ours. We're happy to price either.

**What makes it work:** it states what is true rather than what is wrong; it explicitly reminds
the owner that egress is unaffected (the thing they will worry about first); it names the
mechanical key fallback, which is the actual operational answer; it presents two options with
their real constraints; and it does not recommend, because the brief said not to and because
this genuinely is the owner's decision.

---

## E4.5 — Drawing set with no fail-state column

**The correction:**

Add an explicit **fail state** field to the door schedule / device schedule, populated for
every electrified opening with `FAIL SECURE` or `FAIL SAFE` — never blank, never inferred from
the device type.

For every fail-safe opening, add a second field or remark stating the **release trigger(s)**:
power loss, fire alarm, manual release, or a combination.

**Every document it must propagate to:**

| Document | What changes |
|---|---|
| **Security drawings** — door/device schedule | New column, populated for all electrified openings |
| **Security drawings** — riser and point-to-point details | The fire alarm interface and release wiring must be shown for every fail-safe opening |
| **Specification 08 71 00** — hardware sets | Each electrified device line states the fail state explicitly |
| **Specification, Division 28** | Fail state and release requirements described in the access control section |
| **Design narrative** | The reasoning and the code citation for each fail-safe opening `[CODE][VERIFY]` |
| **Device data model** (`../../16_Automation/data_model/`) | `fail_state` populated per device; add a validation rule that flags any electrified device with a blank fail state, and a consistency rule against opening rating and function |
| **Submittal review checklist** | "Fail state matches schedule" becomes an explicit review item |
| **Commissioning test plan** (`../../18_Commissioning/`) | A test per fail-safe opening: interrupt power, confirm release; activate FA, confirm release |
| **O&M handover / operations manual** (`../../19_Operations/`) | Recurring test obligation for release arrangements |

**The thing that makes this a real correction rather than a drawing edit:** the fail state has
to survive from your intent all the way to what the contractor *orders*, and the ordering
happens off the submittal, which is built from the specification, not from your drawing. If the
spec doesn't say it, the drawing column is decoration.

> 🧠 The general lesson: when you find a missing field, trace it forward to the point of
> purchase. A design decision that doesn't reach a purchase order didn't happen.
