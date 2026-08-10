# Solutions — 05 Camera Form Factors and Tradeoffs

> Work the exercises in [`../05_camera_form_factors.md`](../05_camera_form_factors.md) before
> reading this. Pixel-density values were produced by running
> [`../../28_Calculators/psec/optics.py`](../../28_Calculators/psec/optics.py); the fisheye
> falloff uses `PPF = px_around_circle / (2πr)`, the same `1/r` law derived in
> [32/02](../../32_Engineering_Math/02_pixel_density.md).

---

## E5.1 — 20 MP fisheye over a 60 × 60 ft open-plan office

**(a) Radius at which it drops below recognise (38 ppf).**

```
PPF = px / (2πr)   →   r = px / (2π · PPF)
r = 5200 / (2π × 38) = 21.78 ft
```

**Recognise holds to a radius of 21.78 ft.**

| Radius | PPF | Class |
|---|---|---|
| 5 ft | 165.5 | identify |
| 10 ft | 82.8 | identify |
| 15 ft | 55.2 | recognise |
| 20 ft | 41.4 | recognise |
| **21.78 ft** | **38.0** | **recognise floor** |
| 25 ft | 33.1 | observe |
| 30 ft | 27.6 | observe |

**(b) Fraction of the 60 × 60 ft area covered at recognise or better.**

*Assumption, stated:* the camera is mounted at the centre of the room, and the recognise circle
sits wholly inside the square (21.78 ft < 30 ft, so it does).

```
recognise circle area = π × 21.78² = 1490 ft²
room area             = 60 × 60    = 3600 ft²
fraction              = 1490 / 3600 = 41.4%
```

**41.4%.**

And the corners are worse than "observe" sounds:

```
centre to corner = √(30² + 30²) = 42.43 ft
PPF at the corner = 5200 / (2π × 42.43) = 19.5 ppf
```

**19.5 ppf against an observe threshold of 19.0** — the room corners scrape the *bottom* class by
half a pixel per foot. A person standing in a corner of this office is at the very edge of "what
is it doing?" and nowhere near "who is that?"

**(c) One-sentence design review finding.**

> A single 20 MP fisheye at the centre of this space delivers recognise-grade coverage over a
> 21.8 ft radius — 41% of the floor area — with the room corners at 19.5 ppf, marginally at
> observe; if recognise is required across the space, this needs either supplementary fixed
> cameras at the perimeter or the target reclassified and the consequence recorded.

> 🧠 **The generalisable check:** a fisheye's useful radius is `px / (2π · target_PPF)`, and its
> useful **area** goes as the square of that — so halving the target class quadruples the covered
> area. That steep relationship is why fisheye claims are always made without naming a class.
> Ask "at what class?" and the conversation becomes concrete immediately.

---

## E5.2 — Multisensor vs. three fixed at a building corner

**(a) Installed cost comparison.**

| | Multisensor | 3 × fixed |
|---|---|---|
| Camera(s) | $2,400 | 3 × $520 = $1,560 |
| VMS licences | 4 imagers × $180 = **$720** | 3 × $180 = $540 |
| Cable drops | 1 × $340 = $340 | 3 × $340 = $1,020 |
| Lift | $480 | $480 |
| **Total** | **$3,940** | **$3,600** |

**The three fixed cameras are $340 cheaper.**

> ⚠️ **This is the result the exercise exists to produce.** The multisensor saves $680 on cable —
> a real and visible saving — and loses it, plus more, on the camera price and on **licensing a
> fourth imager the design does not need**. The device has four imagers whether or not the corner
> requires four views, and per-imager licensing charges for all of them. Anyone comparing on
> "one drop instead of three" reaches the opposite conclusion and is wrong by $340 before
> operations are considered at all.

**(b) Two non-cost factors that could reverse it.**

1. **Cable path difficulty → pushes toward the multisensor.** The $340-per-drop figure assumes
   three routable paths exist. On a retrofit, in a historic structure, or where the corner is
   reached by a single conduit, two of those three drops may be impossible or cost multiples of the
   estimate. Where cable routing is the binding constraint, the multisensor wins decisively and the
   licence premium is trivial against it.
2. **Failure concentration → pushes toward fixed cameras.** One multisensor failure removes all
   three views at once; one fixed camera failure removes one. On a 24/7 site with slow service
   response, the difference is hours of total blindness at that corner versus degraded coverage.

*(Also creditable: independent aiming heights and lens choices per view — pushes toward fixed;
single mounting point available at height — pushes toward multisensor; PoE class availability at
the switch — usually pushes toward fixed.)*

**(c) Does the hazardous-materials store change the recommendation?**

**Yes — decisively, toward the three fixed cameras.**

The corner is the *only* coverage of a hazardous-materials store, which makes this a
**single-point-of-failure** question rather than a cost question. With the multisensor, one PoE
fault, one water ingress, one failed device leaves the HAZMAT store with **no coverage at all**
until someone brings a lift out. With three fixed cameras, a single failure degrades coverage and
leaves two views recording.

There are two further reasons specific to this scenario:

- A HAZMAT store is likely to carry regulatory, insurance, or permit obligations regarding
  monitoring `[VERIFY — jurisdiction and material dependent]`. A total coverage outage may be a
  **compliance** event and not merely an operational one, and the duration of that outage is now
  bounded by the lift schedule.
- The fixed option is also the cheaper option here, so there is no tension to resolve. **Say so
  plainly** — when the more robust option is also cheaper, the recommendation writes itself and you
  should not dress it up as a difficult trade.

> **The recommendation as written:** *"Three fixed cameras — $340 less, and a single device failure
> at this corner would otherwise leave the HAZMAT store with no coverage until a lift can be
> mobilised. If cable routing to the second and third positions turns out to be impractical, come
> back to me: the multisensor becomes the right answer, and we should then discuss a spare on the
> shelf."*

---

## E5.3 — Four PTZs, no monitoring station

**(a) The problem, in one sentence.**

> A PTZ records only where it is currently pointed, so with nobody driving it, three of the four
> gates — and often all four — are simply not recorded during the event you will later be asked
> about.

**(b) Recommendation and reasoning.**

**Specify fixed cameras at all four gates, sized to the required pixel density.**

The client's stated want is "zoom in on anything suspicious." Unpack it: with no monitoring
station, nobody is watching anything live, so there is no one to *do* the zooming. What they
actually need is that **when they review footage after an incident, the recording contains enough
detail** — which is a pixel-density-at-capture requirement, not a zoom requirement. That is exactly
what a correctly specified fixed camera delivers, and what a PTZ parked at its home position does
not.

Digital zoom into a well-specified fixed recording gives them the "zoom in" experience they are
describing, on **recorded** footage, at every gate simultaneously, forever. That is a better answer
to their actual question, and it costs less.

If assessment reach is genuinely wanted later, the upgrade path is monitoring plus a PTZ **added
to** the fixed coverage — never replacing it.

**(c) If they insist: one partial mitigation, and what it does not fix.**

**Mitigation:** configure each PTZ to **return automatically to a wide home preset** after a short
idle timeout (typically 30–60 seconds), and set that home position to the widest useful view of the
gate. Then at least the default recorded state is the full gate rather than wherever it was last
left pointing.

**What it still does not fix:**

- The PTZ still covers **one gate**, and each gate has its own camera here, so the cross-gate
  problem is solved by having four — but each camera still records only *its* gate's home view,
  which is now just a fixed camera with motors, at higher cost and with more to fail.
- During the timeout window after any movement, and during any tour, the recording is a partial
  view.
- **The home preset is wide**, so its pixel density is the *lowest* the camera offers — which means
  the recorded default is the least detailed image the device can produce. If that wide view does
  not meet the required class, the mitigation is cosmetic.

**The honest framing:** a PTZ configured to sit at a wide home preset is a fixed camera that costs
more, fails more, and drifts. If that is where you end up, say so, and let the client decide with
that on the table.

---

## E5.4 — Form factor selection

**(a) Lift car interior.**
**Corner mount.** A lift car is a small box where a ceiling-centre camera looks straight down at
heads; a corner wedge gets a near-frontal view of everyone facing the doors, which is where faces
point. Vandal resistance matters, and the corner form factor takes the mounting geometry out of the
problem.

**(b) 300 ft dark perimeter fence, requirement is to know someone is approaching.**
**Thermal.** The requirement is explicitly **detection**, not identification, over a long, dark
run. Thermal needs no illumination, works in fog and total darkness, and covers long ranges — this
is the application it is genuinely best at. Pair it with a cued PTZ or fixed camera at the likely
approach points if assessment is also needed, and be explicit that thermal will never say who it
was ([lesson 03](../03_sensors_and_low_light.md)).

**(c) Vehicle entry lane, plates must be read.**
**Specialty LPR camera.** Plate capture needs its own optics, its own short exposure, and usually
its own IR illumination, and it does not double as an overview camera
([lesson 02](../02_optics_and_lenses.md), worked example 2.2). Specify a **second** camera for
lane overview and occupants — that is not scope creep, it is the correct design.

**(d) Architecturally sensitive hotel lobby, 14 ft ceiling, recognise at reception, observe across
the lounge.**
**Two form factors, because there are two requirements.** A discreet **in-ceiling or small fixed
dome/turret** aimed at the reception desk, sized for recognise at the desk position; and a
**fisheye** over the lounge for observe-grade context, which suits both the requirement class and
the aesthetic constraint (one small device instead of several). The 14 ft ceiling is workable for
the fisheye; compute the observe radius and confirm it covers the lounge before committing.

**(e) Warehouse exterior corner, two elevations plus yard, difficult cable, mount at 26 ft.**
**Multisensor.** This is the textbook case: a single mounting point at height, a difficult cable
path, three distinct directions needing independent aiming, and one lift visit to install. All the
multisensor's advantages apply and its main disadvantages (licensing, failure concentration) are
the acceptable side of the trade — **unless** this corner is the sole coverage of something
critical, per E5.2(c). Confirm the PoE class the switch can deliver, including startup, before
specifying it.

---

## E5.5 — 🧠 14 fixed cameras → 4 multisensors in a 24/7 warehouse

A model response:

> The 30% saving on cable and installation is real, and on a warehouse it is probably
> understated — the drops in that building are long, some of them are over racking, and every one
> we delete is a cable tray run we do not have to coordinate. So I want to be clear that the
> instinct is sound and I would reach for multisensors on a site like this too.
>
> Two things need checking before we commit, and one of them may reverse it.
>
> First, licensing. Four multisensors is 12 to 16 imagers depending on the model, against 14
> cameras today. If our VMS licenses per imager — and ours does — we may be buying more licences
> than we are deleting, which eats a meaningful part of the saving before we start. That is a
> phone call to the vendor and I would want it in writing.
>
> Second, and this is the one that concerns me: the site runs 24/7 with no on-site technician and a
> four-hour service response. Today a camera failure costs us one view. With four multisensors, a
> single failure costs us a quarter of the entire system for at least four hours, and the failure
> modes that take out a multisensor — the PoE port, the single cable, water in the one gland,
> the device itself — are exactly the ones that were previously spread across three or four
> independent devices. We would be concentrating the risk at the same time as we lengthen the
> time to fix it.
>
> What I would propose: use multisensors where the cable saving is largest and the coverage is not
> critical — the general floor and the yard elevations — and keep fixed cameras on the positions
> where a four-hour blind spot actually matters: the dock doors, the high-value cage, and the two
> personnel entrances. We keep most of the installation saving, and we stop a single failure from
> taking out anything we would have to shut down the shift over. I would also budget one spare
> multisensor on the shelf, because with a four-hour response and a lift required, the spare is
> what actually determines the outage length.

**What is being graded:**

- **It agrees with what is right.** The saving is real and the response says so first, without
  irony. A reply that opens by listing objections loses the colleague immediately and is usually
  also wrong, since multisensors *are* frequently correct on warehouses.
- **It engages with the actual number** rather than waving at "hidden costs" — naming per-imager
  licensing as a specific, checkable item, with a specific action (get it in writing).
- **It identifies the site-specific factor that dominates**: 24/7 operation, no technician, four-hour
  response. The same proposal in a staffed building with a technician on site would be an easy yes.
- **It proposes a hybrid**, which is the actual engineering answer — the choice is per-position, not
  per-site, and treating it as a single decision is the error underneath the original proposal.
- **It names the spare.** With a lift and a four-hour response, mean time to repair is dominated by
  parts availability, and a spare on the shelf is a cheaper intervention than any design change.

A response that simply says "multisensors concentrate failure, don't do it" is technically true
and professionally useless: it ignores a real saving, offers no alternative, and would be overruled
by anyone holding the budget.

---

## Retrieval check — answers

1. **No bubble.** A turret loses no light to an extra plastic layer, cannot suffer IR bounce off
   it, and has nothing to haze or scratch — better image for the same money, unless vandal
   resistance or aim discretion is needed.
2. **No.** Same imager count at the same resolution produces the same data regardless of housing.
   Multisensors save **ports and cable**, not bandwidth or storage.
3. It records **one place at a time**, structurally. A guard tour makes it worse: 6 presets at 10 s
   each means any location is recorded 1/6 of the time, while sounding thorough.
4. **`1/r`** — pixels spread around a circumference of `2πr`.
5. **Per-imager VMS licensing** and **failure concentration** (with PoE class a close third).
6. A camera may need more power to **start** in cold than to run — heaters plus boot draw. Check
   the **startup** power figure against the PoE budget, not the operating figure.
7. Multisensors win on **installation**; fixed cameras win on **operation**.
