# 10 — Retail Case Study: Brannon's Home & Garden

> **This is a case study, not a lecture.** Read it after lessons 01–09, and try to answer each
> question before reading on.
>
> It exists to answer the question every junior asks on their first retail site: **why are there
> four domes clustered over that till?**
>
> **Brannon's Home & Garden is fictional.** Every figure, floor plan, and loss statistic below is
> invented for teaching. Real retail loss figures vary enormously by format, geography, and
> category, and any claim you make on a real project must come from that client's own data.
> `[VERIFY]`

## Learning objectives

- Derive a retail camera design from the store's actual loss profile rather than from a template.
- Explain the four-cameras-over-a-till pattern, camera by camera, from the questions each answers.
- Describe why point-of-sale integration changes the economics of the whole system.
- Distinguish the losses cameras address from the much larger losses they do not.
- Critique a retail design that satisfies a checklist and fails the store.

---

## The site

**Brannon's Home & Garden** — a single-storey big-box retailer, 42,000 ft² of sales floor plus
9,000 ft² of stockroom and a garden centre with an outdoor yard.

```
   ┌──────────────────────────────────────────────────────────┬───────────┐
   │                                                          │  GARDEN   │
   │   ┌────────┐                                             │  CENTRE   │
   │   │STOCK   │        SALES FLOOR                          │  (yard,   │
   │   │ROOM    │        aisles, seasonal, high-value         │  covered) │
   │   │        │        power tools cage                     │           │
   │   └───┬────┘                                             │     ┌─────┤
   │       │ ▒ stock door                                     │     │yard │
   │       │                                                  │     │gate │
   │   ┌───▼──────────────────────────────────────┐           │     └─────┤
   │   │      TILL LANES  1  2  3  4  5  6        │           │           │
   │   └──────────────────────────────────────────┘           │           │
   │        ▒▒▒▒  ENTRANCE / EXIT VESTIBULE ▒▒▒▒              │           │
   └────────────────────────┬─────────────────────────────────┴───────────┘
                    CUSTOMER CAR PARK
   ┌─── staff door (side) ──┘        ┌─── goods-in dock (rear) ───┐
```

**The brief as received:** *"We need cameras. Head office says 60. Our shrink is up."*

That brief contains one useful fact (shrink is up), one instruction that is not a requirement
(60 cameras), and no questions at all. **The design starts by fixing that.**

---

## Step 1 — What is actually being lost, and how?

Before any camera, get the loss profile from the people who handle it: the store manager, the
loss-prevention lead, and the till supervisors.

Brannon's, after that conversation:

| Loss source | Share of shrink | Where it happens | Can video address it? |
|---|---|---|---|
| **External theft** | ~30% | Sales floor → exit; high-value aisles | Partly — at the exit, not the aisle |
| **Internal theft** | ~30% | Tills, stockroom, goods-in, staff door | **Yes, and this is where video earns its cost** |
| **Administrative / paperwork error** | ~20% | Receiving, markdowns, counts | **No.** A process problem |
| **Supplier / delivery shortfall** | ~15% | Goods-in dock | **Yes** — dock capture is high value |
| **Damage and spoilage** | ~5% | Garden centre, seasonal | No |

> 🧠 **Read that table before designing.** **A quarter of the shrink — administrative error and
> most spoilage — is not addressable by cameras at all**, and no camera design will move it. Saying
> so early is one of the most valuable things you can do, because it stops the video system being
> held responsible for a number it cannot influence, and it directs the client toward the process
> fixes that actually would. It also protects you: a system installed against a 100% expectation
> will be judged a failure at 55%.
>
> This is [lesson 01](01_imaging_chain.md)'s prevents-vs-documents conversation, in the specific
> form retail requires.

**The high-value targets, once the table is understood:**

1. **The tills** — internal theft, sweethearting, refund and void fraud. Highest value per camera
   in the store.
2. **The exit** — external theft leaves through it. Everything stolen crosses this line.
3. **Goods-in** — supplier shortfall and internal diversion, at a chokepoint.
4. **The staff door** — internal theft leaves through it.
5. **The high-value cage** (power tools) — concentrated value, defined boundary.

Note that the **sales floor aisles are not on this list.** They are where theft *occurs* but they
are the worst possible place to capture it: long, occluded by racking and displays, with subjects
facing away and moving unpredictably. [Lesson 09](09_camera_placement.md)'s chokepoint principle
applies exactly.

---

## Step 2 — The four domes over the till

**Here is the answer to the question.** A till lane at Brannon's carries four cameras because there
are **four different questions**, and by [lesson 09](09_camera_placement.md)'s rule each needs its
own camera. All figures below computed with `psec.optics`; 4 MP, 2688 px, 1/2.8" sensor.

### Camera 1 — Overhead scan zone

> **Question:** *Was every item that went into the bag actually scanned?*

Mounted in the ceiling at 9.5 ft, looking **straight down** at the scan bed at 3 ft — a working
distance of 6.5 ft.

| Lens | Bed width covered | PPF |
|---|---|---|
| 2.8 mm | 12.47 ft | 216 |
| **4.0 mm** | **8.73 ft** | **308** |
| 6.0 mm | 5.82 ft | 462 |

**4 mm is the choice** — 8.73 ft covers the belt, the scanner, and the bagging area, at 308 ppf,
which resolves individual product barcodes and the operator's hands.

**This camera exists for sweethearting** — an operator passing merchandise around the scanner for a
friend, or scanning a cheap item while bagging an expensive one. That requires seeing **the item and
the scanner together, from above**, where nothing occludes the hands. No other angle answers it.
Note the depression angle is 90°, which would be catastrophic for facial capture and is exactly
right here, **because this camera is not looking at a face.**

### Camera 2 — Customer-facing

> **Question:** *Who was the customer at this transaction, to a standard a stranger could identify?*

Mounted at 8 ft, 7 ft back, aimed at the customer's side of the till.

```
slant range 7.62 ft, depression 23.20°, 4 mm lens
scene width 10.22 ft → 263 ppf → identify, with 3.5× margin
```

Needed for refund fraud, card fraud, and counterfeit currency — all of which require identifying an
**unknown** person, so identify grade ([lesson 04](04_dori_and_pixel_density.md)). The 23° angle is
inside the 30° limit, and the customer is stationary and facing the till: a natural chokepoint.

### Camera 3 — Associate-facing

> **Question:** *Which associate operated this till at this time?*

Mounted at 8.5 ft, 9 ft back, aimed at the operator position.

```
slant range 9.66 ft, depression 21.25°, 4 mm lens
scene width 12.96 ft → 207 ppf
```

The requirement is only **recognise** — staff are known to the reviewer
([lesson 04](04_dori_and_pixel_density.md)) — and the geometry delivers far more, which is fine and
free. It matters because till logins are shared, borrowed, and left open constantly; **the video is
the ground truth about who was physically standing there**, and the till log is not.

### Camera 4 — Lane approach and queue

> **Question:** *What happened in and around the lane — did the customer approach with items that
> never reached the belt, and what did the queue look like?*

Mounted at 12 ft, 2.8 mm lens, covering the approach:

| Distance | Scene width | PPF | Class |
|---|---|---|---|
| 15 ft | 31.7 ft | 85 | identify |
| 25 ft | 49.8 ft | 54 | recognise |
| 35 ft | 68.5 ft | 39 | recognise |

Context and continuity ([lesson 09](09_camera_placement.md)) — it links the sales floor to the
transaction, and it covers the trolley's lower rack, which is where unscanned bulky items ride out.

### So: four questions, four cameras

| Camera | Question | Class needed | Why it cannot be shared |
|---|---|---|---|
| 1 Overhead | Was it scanned? | identify (of the item) | Needs a 90° top-down view |
| 2 Customer | Who was the customer? | identify | Needs a near-frontal view of the customer |
| 3 Associate | Which associate? | recognise | Faces the opposite direction to camera 2 |
| 4 Approach | What led up to it? | observe/recognise | Needs a wide, high view |

**Cameras 2 and 3 face opposite directions. Camera 1 looks straight down. Camera 4 is wide and
high.** There is no single position or lens that serves any two of them — which is the complete
answer to "why four domes," and it is an application of the rule from
[lesson 09](09_camera_placement.md) rather than a retail convention.

> ⚠️ **In practice this is often three, not four**, and knowing when to cut is part of the skill.
> Camera 4's job can sometimes be met by an adjacent lane's camera or a general front-end overview.
> Camera 1 is the one never to cut — it addresses the highest-value, hardest-to-otherwise-detect
> loss. Six lanes × 4 cameras = 24 cameras before anything else in the store, so the question of
> whether every lane needs all four is real. **A common and defensible answer: all four on the
> lanes that handle returns and high-value transactions, three elsewhere.**

---

## Step 3 — The rest of the store

| Zone | Question | Class | Notes |
|---|---|---|---|
| **Entrance / exit vestibule** | Who entered and left, and what were they carrying? | **identify** | The single most important non-till position. 35.37 ft of doorway per camera at identify — a 30 ft vestibule needs one, a 60 ft frontage needs two. Aim **inward** so arrivals are frontal and not silhouetted against daylight ([lesson 03](03_sensors_and_low_light.md)) |
| **Sales floor aisles** | Where did a person go, and when? | **detect / observe** | One camera covers 336 ft at detect, 141.5 ft at observe. Continuity, not identity — identity was established at the entrance |
| **High-value cage** | Who opened the cage and what did they remove? | identify | Chokepoint at the gate, not coverage of the interior |
| **Stockroom door** | Who passed between sales floor and stockroom? | identify | Chokepoint; internal theft route |
| **Goods-in dock** | What was delivered, by whom, and did the count match? | identify + observe | Two cameras, two questions ([lesson 09](09_camera_placement.md) E9.3) |
| **Staff door** | Who left by the staff door and what were they carrying? | identify | Chokepoint |
| **Garden centre yard** | Was stock removed from the yard outside hours? | detect | Large, dark, weather-exposed. Detection, cued — not identification ([lesson 03](03_sensors_and_low_light.md)) |
| **Cash office** | Who accessed the safe and what was the count? | identify | Overhead on the counting surface plus identify at the door |

**What is deliberately not covered:** staff break room, toilets and their approaches, and any view
into neighbouring residential property. These are raised with the client and recorded, never
decided silently ([lesson 09](09_camera_placement.md)).

## Step 4 — Point-of-sale integration

**This is the change that makes the till cameras worth their cost.**

Without it, investigating a suspected void fraud means an operator scrubbing hours of footage. With
POS data overlaid on and searchable against the video, the workflow inverts: query the transaction
log for voids, no-sales, returns without receipt, or manual price overrides on a given till, and
**jump straight to the video of each one.**

| Without POS integration | With POS integration |
|---|---|
| Hours of scrubbing per investigation | Seconds per exception |
| Investigate only when already suspicious | **Routine exception review finds losses nobody suspected** |
| Video is reactive | Video becomes an audit tool |

> 🧠 **The economics change entirely.** An unintegrated till camera is reviewed after a suspicion
> arises, which is rare, so most of its value is never realised. An integrated one supports weekly
> exception review by the loss-prevention team, which finds patterns — one operator with a void
> rate five times the store average — that nobody would ever have suspected. **Recommend POS
> integration on any retail project with till cameras.** It typically costs less than two cameras
> and multiplies the value of twenty-four.

The prerequisites are the same ones from [lesson 08](08_vms_architecture.md): **NTP time
synchronisation** across the VMS and POS, and a consistent naming convention so till 4 in the POS
data is till 4 in the VMS.

## Step 5 — The senior critique

Head office asked for 60 cameras. Here is what a senior engineer says about the design that
results.

**What the store actually got right by asking:** the till coverage. Retail has genuinely converged
on the multi-camera till pattern because the questions are real and the losses are real.

**What is usually wrong in a retail design of this type:**

1. **Too many aisle cameras, too few chokepoint cameras.** Aisles are where theft happens and the
   worst place to record it. The exit is where everything stolen must pass.
2. **The exit camera is aimed outward at the car park**, silhouetting everyone leaving against
   daylight — the exact failure from [lesson 01](01_imaging_chain.md), worked example 1.2. Free to
   fix on the drawing; expensive afterwards.
3. **No POS integration**, so the most expensive cluster in the store operates at a fraction of its
   value.
4. **The garden centre yard is specified with identify-grade cameras** that will deliver nothing at
   night. It needs detection and lighting, not resolution
   ([lesson 04](04_dori_and_pixel_density.md) E4.5's conclusion, in a different setting).
5. **Nobody watches anything live**, and the client believes the system deters. It documents.
6. **Retention is 30 days by habit**, when retail disputes — refund fraud patterns, employment
   matters, supplier claims — routinely surface in months
   ([lesson 07](07_storage_and_retention.md)).

**The recommendation that changes the outcome:** fewer aisle cameras; the exit done properly and
aimed inward; POS integration; lighting in the yard rather than cameras; retention reviewed against
how long Brannon's disputes actually take to surface. **That is very likely fewer than 60 cameras
and a much better system** — the [lesson 09](09_camera_placement.md) E9.5 conversation, in its
natural habitat.

## Common mistakes

⚠️ **Designing retail from a template.** The loss profile differs by format and category; get the
store's own.

⚠️ **Promising shrink reduction.** A quarter of shrink is administrative and no camera touches it.

⚠️ **Covering aisles instead of exits.** Theft happens in aisles and leaves through doors.

⚠️ **Aiming the exit camera outward.** Silhouettes, every day, forever.

⚠️ **Till cameras without POS integration.** Most of the value left unrealised.

⚠️ **Identify-grade cameras on a dark outdoor yard.** Light and detect instead.

⚠️ **Treating the till cluster as a convention rather than four questions.** Then you cannot defend
it, or sensibly reduce it.

## Junior vs. Senior

| | Junior | Senior |
|---|---|---|
| Starts from | "Head office says 60 cameras" | The store's loss profile, from the people who handle losses |
| Explains the four domes as | "That's how retail does tills" | Four questions no single camera can share |
| Handles the shrink expectation by | Agreeing the system will reduce it | Saying which quarter of shrink video cannot touch, before installation |
| Prioritises | Sales floor coverage | Chokepoints — exit, tills, goods-in, staff door, cage |
| Sees POS integration as | An optional extra | The thing that makes the till cluster worth its cost |
| Handles the yard by | Specifying more cameras | Specifying lighting, and detection-grade cameras |
| Delivers 60 cameras because | It was asked for | Only if 60 questions were written |

## Exercises

Work these before opening
[`_solutions/10_retail_case_study_solutions.md`](_solutions/10_retail_case_study_solutions.md).

**E10.1** Brannon's has six till lanes. Using the four-camera pattern, that is 24 cameras.
 (a) The client's budget allows 16 at the front end. Which cameras do you cut, and from which
     lanes?
 (b) Justify each cut by the question it stops answering.
 (c) State what you would put in writing about the residual risk.

**E10.2** The store manager says: *"We put in cameras last year and shrink went up. They don't
work."*
 (a) Give three distinct explanations consistent with both statements being true.
 (b) State what you would ask to distinguish between them.
 (c) Write the reply.

**E10.3** The garden centre yard is 120 ft × 80 ft, unlit, with stock stored outdoors overnight.
The client wants to "identify anyone who comes over the fence."
 (a) Explain why the request as stated will not work.
 (b) Give the design you would propose.
 (c) State what the client gains and gives up.

**E10.4** Design the goods-in dock coverage. State each camera, its question, its class, and its
mounting height, and explain why supplier shortfall needs a different camera from internal
diversion.

**E10.5** 🧠 Brannon's loss-prevention lead wants facial recognition at the entrance to alert on
known offenders.
 (a) State the technical prerequisites and whether the entrance camera as designed meets them.
 (b) Name the three non-technical issues.
 (c) Give your recommendation and the reasoning. There is a defensible answer either way; the
     grading is on whether you engaged with the real difficulties.

## Retrieval check

1. What share of retail shrink is typically not addressable by cameras, and what is it?
2. Name the four till cameras and the question each answers.
3. Which till camera would you never cut, and why?
4. Why are sales floor aisles a poor place to capture theft?
5. Which way should the exit camera be aimed, and why?
6. What does POS integration change about the value of till cameras?
7. What are the two prerequisites for POS integration?

## References

- [`09_camera_placement.md`](09_camera_placement.md) — the rule and the process this case study
  applies throughout.
- [`04_dori_and_pixel_density.md`](04_dori_and_pixel_density.md) — the class assignments here.
- [`08_vms_architecture.md`](08_vms_architecture.md) — time sync and naming, the POS integration
  prerequisites.
- [`../21_Facility_Case_Studies/`](../21_Facility_Case_Studies/) — retail among other facility
  types, in more depth *(not yet written)*.
- [`../36_Human_Factors_Privacy_Ethics/`](../36_Human_Factors_Privacy_Ethics/) — facial
  recognition, staff monitoring, and customer privacy *(not yet written)*.
- `[VERIFY]` **All loss figures in this case study are invented for teaching.** Real shrink
  composition varies widely by retail format, category, and country. Use the client's own data, and
  if they do not have it, that is itself a finding worth reporting.

---

**Next:** [11 — Analytics and Health Monitoring](11_analytics_and_health.md) — what the software
can reliably do, and how you know camera 147 has been showing a wall for six weeks.
