# Solutions — 10 Retail Case Study

> Work the exercises in [`../10_retail_case_study.md`](../10_retail_case_study.md) before reading
> this. Brannon's Home & Garden and all its figures are fictional.

---

## E10.1 — Sixteen front-end cameras instead of twenty-four

**(a) What to cut.**

Six lanes × 4 cameras = 24. The budget allows 16, so eight must go.

**Assume lanes 1 and 2 handle returns and high-value transactions** (this is the normal
arrangement, and if it is not, ask — the answer changes the design).

| Lane | Cameras retained | Cameras cut |
|---|---|---|
| 1 (returns/high value) | Overhead, customer, associate, approach — **all 4** | — |
| 2 (returns/high value) | Overhead, customer, associate, approach — **all 4** | — |
| 3 | Overhead, customer | associate, approach |
| 4 | Overhead, customer | associate, approach |
| 5 | Overhead, customer | associate, approach |
| 6 | Overhead, customer | associate, approach |
| **Total** | **16** | **8** |

**(b) Justifying each cut by the question it stops answering.**

**The approach cameras (4 cut).** These answered *"what led up to the transaction?"* — context and
continuity. This is the cheapest cut because the loss is **partially recoverable elsewhere**: the
front-end overview camera and the exit camera together establish who approached the lanes and who
left, so continuity survives even if the per-lane detail does not. It is the only one of the four
questions with a substitute.

**The associate cameras (4 cut).** These answered *"which associate operated this till?"* The loss
is real but **partially mitigated by the till login record** — imperfect, because logins are shared
and left open, which is precisely why the camera was specified. What we retain is the ability to
answer this question on the two lanes where the highest-value transactions occur.

**What is deliberately not cut, on any lane:**

- **The overhead scan-zone camera.** It addresses sweethearting, which is the highest-value,
  hardest-to-otherwise-detect loss at the front end, and **no other camera angle can substitute** —
  the view must be top-down over the scan bed. Cutting it removes the entire reason the till
  cluster exists.
- **The customer-facing camera.** Refund and card fraud require identifying an **unknown** person,
  and nothing else in the store captures a customer's face at identify grade at the moment of the
  transaction. The exit camera captures them leaving but cannot tie them to a specific transaction.

**(c) The residual risk, in writing.**

> **Front-end coverage — reduced scope, [date].**
>
> **Provided:** overhead scan-zone and customer-facing identification coverage on all six lanes;
> full four-camera coverage on lanes 1 and 2, which handle returns and high-value transactions.
>
> **Not provided, on lanes 3–6:** associate-facing identification, and lane approach coverage.
>
> **Consequence:** on lanes 3 to 6, establishing which associate operated the till at a given time
> will rely on the till login record rather than on video. Where a login has been shared, left
> open, or used by another member of staff, video will not resolve who was physically at the
> till — which is the specific circumstance in which that question usually arises. Lane approach
> context on those lanes will rely on the front-end overview and exit cameras, which will show that
> a person approached the lanes but not the detail of items in a trolley before scanning.
>
> **Compensating measures:** (i) full coverage retained on the two returns lanes, where refund
> fraud concentrates; (ii) POS integration across all six lanes, so exception review remains
> available store-wide and is the primary detection route for till fraud on lanes 3–6; (iii) till
> login discipline recommended as a procedural control, since video no longer backstops it on four
> lanes.
>
> **Accepted by:** [name, role, date]

**What is being graded:** cutting by **question**, not by lane or evenly; identifying which
questions have substitutes (approach, associate) and which do not (overhead, customer); protecting
the returns lanes specifically; and — the mark of the answer being complete — naming **POS
integration as the compensating measure**, since it partly restores detection capability on the
lanes that lost cameras. Cutting one camera from each of eight lanes, or cutting lanes 5 and 6
entirely, are both weaker answers and should be recognised as such.

---

## E10.2 — "We put in cameras last year and shrink went up"

**(a) Three explanations consistent with both statements.**

1. **The cameras are addressing the wrong share of the loss.** If Brannon's shrink is dominated by
   administrative error and supplier shortfall — around 35% combined in the loss profile — a camera
   system aimed at the sales floor cannot move it. Shrink could rise for reasons entirely outside
   what the cameras see, while the cameras work exactly as designed.
2. **Measurement improved, not losses.** Installing cameras frequently coincides with a stock count,
   tighter processes, or a new loss-prevention focus. Losses that were previously invisible are now
   being **recorded** as shrink. The number went up because the counting got better — this is
   extremely common and clients almost never consider it.
3. **The cameras are not working as believed.** Aimed outward at daylight and silhouetting everyone
   leaving; no POS integration so till fraud is undetected; nobody reviewing anything; a misaimed or
   dirty camera on the exit ([lesson 11](../11_analytics_and_health.md)). The system exists,
   documents nothing usable, and deters nobody once staff notice.

*(A fourth, worth credit: **displacement or adaptation** — external theft moved to a different
method or location, and internal theft continued because the cameras were never pointed at the till
or the staff door.)*

**(b) What to ask to distinguish them.**

- **"Can I see the shrink breakdown by category, this year and last?"** Distinguishes explanation
  1 immediately. If administrative error grew, cameras were never the lever.
- **"Did anything change about how you count or record shrink?"** Tests explanation 2. Ask about
  count frequency, method, and whether a new LP process started.
- **"When was the last time anyone reviewed footage, and what were they looking for?"** Tests
  explanation 3. If the answer is "only when something happens," the system is not being used as a
  detection tool at all.
- **"Show me the exit camera's footage from 4 p.m. yesterday."** Ten seconds establishes whether the
  most important camera in the store actually works.

**(c) The reply.**

> That is worth taking seriously, and I would like to understand it before defending anything.
>
> There are a few different things that could produce exactly what you are describing. The most
> common one, honestly, is that cameras get installed alongside better counting — and the shrink
> number goes up because you are now measuring losses that were always happening and never showed
> up. If your count method or frequency changed last year, that alone could explain it.
>
> The second is that a good chunk of retail shrink is not something cameras can address at all.
> Administrative error, markdown mistakes, and supplier shortfalls typically make up a third or
> more, and no camera will move those. If that is where your increase is, the cameras are doing
> their job and the problem is somewhere else entirely.
>
> The third possibility is that the cameras are not delivering what you think they are — that is
> genuinely common, and it is usually the exit camera aimed the wrong way so everyone leaving is a
> silhouette, or till cameras with no link to your POS data so nobody ever reviews them.
>
> Can I see the shrink breakdown by category for both years, and can we look at the exit camera
> footage from yesterday afternoon together? Those two things will tell us which of these it is,
> and it will take about twenty minutes.

**What is being graded:** not defending the system reflexively; offering the measurement explanation
first, because it is both most likely and least accusatory; naming the categories cameras cannot
touch; and ending with two **specific, fast** diagnostic actions rather than a proposal. A reply
that leads with "you need more cameras" is the wrong answer to this question in every respect.

---

## E10.3 — The garden centre yard

**(a) Why the request will not work as stated.**

The yard is 120 ft × 80 ft, **unlit**. "Identify anyone who comes over the fence" fails on three
independent grounds, any one of which is sufficient:

1. **Light.** With no illumination, the exposure budget ([lesson 03](../03_sensors_and_low_light.md))
   cannot support a shutter fast enough to freeze a person climbing or moving. The camera will
   choose a slow shutter and high gain, and produce a smeared, noisy image regardless of resolution.
2. **Coverage geometry.** Identify grade requires roughly 35 ft of scene width per 4 MP camera. The
   fence line alone is 400 ft; covering it at identify would take a dozen cameras, and covering the
   yard surface many more — for a scenario that happens rarely.
3. **Pose and unpredictability.** Someone climbing a fence is not facing a camera, is moving, and is
   at an unpredictable point along 400 ft of boundary. Identification requires a cooperative
   geometry the yard does not provide anywhere.

**(b) The design proposed.**

> - **Detection, not identification, on the boundary.** Thermal or well-configured
>   classification-enabled cameras covering the fence line, tuned to alert on a person crossing
>   ([lesson 11](../11_analytics_and_health.md)). This answers *"is someone in the yard?"*, which is
>   the question that actually has operational value at 2 a.m.
> - **Lighting on the yard**, specified in lux at a named plane. This improves every camera at
>   once, has independent deterrent value for opportunistic theft, and is the only intervention with
>   no image penalty.
> - **Identify-grade capture at the yard gate and at the door between the yard and the store** —
>   the chokepoints. Anyone who takes stock out of the yard has to leave through somewhere, and
>   those points are small, lightable, and give a frontal view.
> - **Detect/observe coverage of the yard surface** for movement and direction, so an incident has
>   a timeline.

**(c) What the client gains and gives up.**

**Gains:** a system that actually alerts when someone is in the yard overnight, which the original
request would not have delivered; identification of anyone using the gate or the store door;
lighting that deters as well as records; and a much lower camera count, freeing budget for the
lighting.

**Gives up:** identification of someone who comes over the fence at an arbitrary point, takes stock,
and leaves back over the fence without using a gate. That case will produce a detection alert, a
timeline, and a description — but not a face.

**Say that explicitly.** It is a real gap and the client should decide about it knowingly. Note the
honest framing: the original design would not have captured that person either, and would have cost
more. **The choice is between a system that fails at this and admits it, and a system that fails at
this and does not.**

---

## E10.4 — Goods-in dock coverage

| Camera | Question | Class | Mount | Notes |
|---|---|---|---|---|
| **D1** | *What was delivered — how many units came off the vehicle, and in what condition?* | **observe (19 ppf)** | 12–14 ft | Wide view of the dock apron and the vehicle tail. Must see the whole unloading operation and the pallet count |
| **D2** | *Who was present at the delivery — driver, and which member of our staff received it?* | **identify (76 ppf)** | 8–9 ft | At the dock personnel door / receiving desk. Chokepoint. Frontal, lit |
| **D3** | *What passed between the dock and the stockroom, and who moved it?* | **identify (76 ppf)** | 8–9 ft | At the stockroom door. The internal diversion route |

**Why supplier shortfall and internal diversion need different cameras:**

They are different events, in different places, requiring different classes.

**Supplier shortfall** is a **counting** question: did 40 cases arrive or 36? The evidence needed is
a wide, continuous view of the unloading operation showing every unit crossing from vehicle to dock
— **observe grade is sufficient**, because nobody's identity is in dispute, and the camera must be
mounted **high** to see over pallets and into the vehicle. It also needs to be continuous and
un-gapped: a count is only defensible if nothing left the frame.

**Internal diversion** is an **identity** question: which individual moved this pallet somewhere it
should not have gone? That needs **identify grade**, mounted **low** for a frontal face at a
chokepoint, covering a doorway rather than an area.

**These requirements are directly opposed** — high/wide/observe versus low/narrow/identify — which
is why one camera cannot serve both, and is the same structural argument as
[lesson 09](../09_camera_placement.md) E9.3. A designer who puts one camera on the dock has chosen
one of these questions without realising the other existed.

> 🧠 **The highest-value addition is not a camera:** correlate D1's footage with the goods-received
> records by timestamp, exactly as the till cameras correlate with POS data. Then a disputed
> delivery goes straight to the relevant three minutes of video instead of an hour of scrubbing,
> and the dock cameras become a routine audit tool rather than an occasional one.

---

## E10.5 — 🧠 Facial recognition at the entrance

**(a) Technical prerequisites, and whether the entrance camera meets them.**

Face recognition needs, at minimum:

| Prerequisite | Status at Brannon's entrance |
|---|---|
| **Sufficient pixels on the face** — typically well above the DORI identify threshold | The entrance camera is specified at identify (76 ppf) across a 35 ft doorway. **Probably marginal** — recognition algorithms generally want more density than a human identification needs, concentrated on the face |
| **Near-frontal pose** | Achievable — the camera is aimed inward at arrivals, who face the direction they walk. **This is met, and it is the reason entrance capture is the standard position** |
| **Controlled, even lighting on the face** | **Not met as designed.** A retail entrance has daylight behind arrivals and interior light in front, varying all day and by season ([lesson 03](../03_sensors_and_low_light.md)). Recognition is far more sensitive to this than human review is |
| **Adequate shutter speed** — no motion blur | Customers walk in at 3 mph. Requires the exposure budget to support ~1/125 s at the darkest hour |
| **A curated gallery** of known offenders with usable images | **Entirely outside the camera system.** Usually the binding constraint in practice |
| **A tuned threshold** | Trades false matches against missed matches; must be set deliberately and reviewed |

**Verdict:** the camera as designed is a reasonable starting point on pose and marginal on density,
and **fails on lighting control** — which is the prerequisite most likely to be the practical
blocker. A dedicated recognition camera, sited to control the light and narrow the field, would be
required.

**(b) The three non-technical issues.**

1. **Legal.** Face recognition is subject to specific and rapidly changing regulation in many
   jurisdictions — some prohibit private-sector use outright, some require explicit notice, a
   documented lawful basis, impact assessments, and retention limits on biometric data. `[VERIFY]`
   Biometric data is typically a special category with heavier obligations than ordinary CCTV.
2. **Accuracy disparities and the consequence of a false match.** Documented accuracy differences
   across demographic groups mean the burden of false matches falls unevenly. `[VERIFY]` A false
   match in a retail setting means a member of the public is approached, challenged, or excluded on
   the basis of a machine error — with a genuine risk of discriminatory outcome, complaint, and
   litigation.
3. **The gallery's provenance and governance.** Who decides a person is a "known offender"? On what
   evidence? Is there a conviction, or a manager's suspicion? How is someone removed? A gallery
   built from staff suspicion is a list of people barred without process, and it is the part of
   these systems that most often fails scrutiny.

**(c) Recommendation and reasoning.**

Either recommendation can be defensible; here is one, argued.

> **I would not recommend deploying face recognition at this site, and I would recommend the
> alternative below instead.**
>
> The technical case is weak: the entrance lighting is uncontrolled and highly variable, which is
> the condition recognition handles worst, so we would be buying a system likely to perform well
> below its demonstration and to degrade seasonally. Fixing that means a dedicated camera and
> controlled lighting at the entrance, which is worth doing on its own merits and should come first
> regardless.
>
> The governance case is the one that decides it. The value of the system depends entirely on the
> quality of the gallery, and building that gallery means your managers deciding which members of
> the public are "known offenders," maintaining that list, and being able to justify each entry and
> each removal. False matches are not a technical inconvenience — they mean approaching a customer
> who has done nothing, and the evidence is that errors do not fall evenly across the population.
> That is a legal and reputational exposure that sits with Brannon's, not with the camera, and it is
> disproportionate to the loss it would prevent.
>
> **What I would do instead:** improve the entrance capture so that when an incident does occur you
> have a genuinely identifiable image — dedicated camera, controlled lighting, proper aim. Then use
> **retrospective search** rather than live alerting: if the same individual is involved in repeat
> incidents, analytics can find them across weeks of footage in seconds
> ([lesson 11](../11_analytics_and_health.md)), and that happens after a human has established there
> was an incident, with no false-alarm cost and none of the live-challenge risk.
>
> If you want to proceed with recognition anyway, it needs to start with your legal team and a
> documented policy on gallery governance, not with a camera specification — and I would want that
> in place before I designed anything.

**What is being graded:** engaging with the **real** difficulties rather than either rejecting the
technology reflexively or treating it as an ordinary product; identifying lighting as the technical
blocker and gallery governance as the actual one; correctly placing the legal decision with the
client while insisting it precedes the engineering; and offering the retrospective-search
alternative, which delivers most of the operational value with almost none of the exposure. An
answer recommending deployment can earn full marks if it addresses all three non-technical issues
concretely and specifies the governance and legal prerequisites as conditions.

---

## Retrieval check — answers

1. Roughly a **quarter** — administrative/paperwork error, plus damage and spoilage. No camera
   design addresses it.
2. **Overhead** (was it scanned?), **customer-facing** (who was the customer?), **associate-facing**
   (which associate?), **approach** (what led up to it?).
3. **The overhead scan-zone camera.** It addresses sweethearting, the highest-value and
   hardest-to-otherwise-detect front-end loss, and no other angle can substitute for a top-down view
   of the scan bed.
4. Long, occluded by racking and displays, subjects facing away and moving unpredictably, and often
   poorly lit. Theft happens there; it is capturable at the exits.
5. **Inward.** Aimed outward, everyone leaving is silhouetted against daylight — and everyone
   leaving is the population of interest.
6. It converts the till cameras from reactive (reviewed only when suspicion already exists) into a
   **routine audit tool** — exception review finds losses nobody suspected.
7. **NTP time synchronisation** between VMS and POS, and a **consistent naming convention** so till
   IDs match across both systems.
