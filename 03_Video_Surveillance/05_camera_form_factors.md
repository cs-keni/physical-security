# 05 — Camera Form Factors and Tradeoffs

> The lesson clients think is about picking a shape. It is about **ports, licences, failure
> behaviour, and who climbs the ladder** — none of which appear in the product photograph.
>
> Bitrate figures used here are stated assumptions, flagged `[PRACTICE]`; where they come from and
> how much to trust them is [lesson 06](06_compression_and_bandwidth.md). PoE class and switch
> capacity arithmetic is [32/05](../32_Engineering_Math/05_poe.md).

## Learning objectives

- Name the common form factors and the application each genuinely suits.
- Choose between a multisensor and multiple fixed cameras on the grounds that actually differ.
- Compute a fisheye's pixel density falloff and state honestly what area it covers **to what
  class**.
- Explain the structural problem with a PTZ that no product improvement fixes.
- Read IP, IK, and temperature ratings, and know which ones get specified wrong.
- Evaluate a form factor by its **failure behaviour** and its ten-year maintenance cost.

---

## The form factors

| Form factor | What it is | Genuinely good for | Real weakness |
|---|---|---|---|
| **Fixed dome** | Fixed lens in a dome housing | Indoor general use; discreet; vandal-resistant variants | Bubble costs light and sharpness, and gets dirty; aiming needs a ladder |
| **Turret / "eyeball"** | Ball in a partial housing, no full bubble | **Usually the better indoor choice than a dome** — no bubble, so no IR bounce and less light loss | Less vandal-resistant; more visually obvious |
| **Bullet** | Cylindrical body, integral sunshield | Outdoor runs, long lenses, obvious deterrent presence | Visually intrusive; easier to grab and re-aim; collects spider webs on the shade |
| **Multisensor** | 3–4 independently aimable imagers on one mount, one cable | Corners, intersections, wide areas needing **uniform** density | One device, one failure, several views; heavier; high PoE class; often licensed per imager |
| **Fisheye / panoramic** | One very wide imager, 180° or 360°, dewarped in software | Open areas with **short** radii; retrospective "what happened over there" | Pixel density collapses with radius — see below. Ceiling height dependent |
| **PTZ** | Motorised pan, tilt, and optical zoom | Cued assessment by an operator or an analytic | **Points somewhere else when it matters.** See below |
| **Thermal** | Images emitted heat | Detection over perimeters and dark open areas | Cannot identify anyone ([lesson 03](03_sensors_and_low_light.md)) |
| **Specialty LPR** | Tuned optics, exposure, and often IR for plates | Plate capture, which is its own discipline | Does one job. Not an overview camera ([lesson 02](02_optics_and_lenses.md)) |
| **Corner mount** | Wedge for room corners | Cells, interview rooms, lifts | Application-specific |
| **In-ceiling / recessed** | Flush with the ceiling plane | Aesthetically sensitive lobbies | Limited tilt; ceiling coordination; harder to service |

> 🧠 **The turret point is worth a paragraph, because it is the most common free improvement
> available on an indoor design.** Domes are specified by habit. A turret has no bubble, so it
> loses no light to an extra plastic layer, cannot suffer IR bounce off that layer, and does not
> haze or scratch. Unless you specifically need vandal resistance or the discretion of not showing
> the aim direction, **the turret is the better camera at the same price.** Specify domes where
> vandalism is a real risk; specify turrets elsewhere and take the image quality for free.

---

## 🧮 Worked example 5.1 — four ways to cover one intersection

**The problem:** a four-way corridor intersection in an office building. Requirement is
**recognise (38 ppf)** down all four legs. Assumed bitrates `[PRACTICE]`, 30-day retention,
continuous recording; computed with
[`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py).

| | **A: 4 × fixed 4 MP** | **B: 1 × multisensor (4 × 4 MP)** | **C: 1 × 12 MP fisheye** | **D: 1 × PTZ** |
|---|---|---|---|---|
| Switch ports | **4** | **1** | **1** | **1** |
| Cable drops | 4 | 1 | 1 | 1 |
| PoE class | af/at × 4 | **bt Type 3** | af/at | at/bt |
| Peak bandwidth | 16.0 Mbps | 16.0 Mbps | 12.0 Mbps | 8.0 Mbps |
| Storage, 30 d | 5.18 TB | 5.18 TB | 3.89 TB | 2.59 TB |
| VMS licences | 4 | **1–4 (check!)** | 1 | 1 |
| Recognise achieved | All 4 legs, to 52.7 ft | All 4 legs | **Only to ~16 ft radius** | **One leg at a time** |
| One device fails | Lose 1 leg | **Lose all 4 legs** | Lose everything | Lose everything |
| Re-aim one view | Ladder, 1 camera | Ladder, but all 4 at once | Software only | Software only |

**What the table shows that a product comparison does not:**

- **A and B are identical on bandwidth and storage** — because the same number of imagers at the
  same resolution produce the same data, regardless of how many housings they live in. People
  routinely assume the multisensor is cheaper on infrastructure. It is not; it is cheaper on
  **ports and cabling**, which is a different and usually smaller saving.
- **B's failure mode is four times worse than A's.** One PoE fault, one water ingress, one lightning
  event, and all four corridor legs go dark simultaneously. On a site where the intersection is the
  only route to a secure area, that is a materially different risk from losing one leg.
- **B's PoE class is the trap.** Four imagers with IR on one device commonly needs 802.3bt Type 3
  (60 W PSE). If the switch is 802.3at, the camera will not power up — or worse, will power up and
  brown out under IR load at night. `[VERIFY per datasheet]` See
  [32/05](../32_Engineering_Math/05_poe.md).
- **Licensing is the cost nobody models.** Many VMS platforms licence **per imager**, not per IP
  address. If so, B costs four licences and saves nothing there. **Check before you compare —
  this single line has reversed more form-factor decisions than optics ever has.** `[MFR][VERIFY]`
- **D records one leg.** The PTZ's low bandwidth and storage look attractive right up to the moment
  you notice that the other three corridors were not recorded at all.

**The honest answer for this intersection is A or B**, decided on whether the ports or the failure
concentration matters more at this site. A is right where the intersection is critical; B is right
where cable paths are hard and the risk is tolerable.

---

## The PTZ problem

A PTZ can look anywhere in its range at high zoom. At any given instant it is looking at **one**
place, which means:

> **When something happens where the PTZ is not pointed, it did not record it.**

This is structural. No improvement in optics, speed, or resolution addresses it, because it is a
property of having one imager and one aim direction.

⚠️ **The specific failure that recurs:** an operator zooms in to follow an incident at the north
gate. While zoomed, the *only* recorded view is the north gate. A second event at the south gate is
not recorded at all — not at low resolution, not wide, not at all. Afterwards the client asks for
the south gate footage and there is none, and the recording of the north gate is a tight shot with
no context around it.

**Where a PTZ is genuinely right:**

- **As a cued assessment tool alongside fixed coverage**, never instead of it. Thermal or analytic
  detection cues the PTZ to a location; fixed cameras keep recording everything meanwhile.
- Where a **trained, staffed** console exists to drive it. An unmonitored PTZ on a tour is a fixed
  camera that is pointed wrong most of the time.
- Long-range applications — a large yard, a marine boundary — where the alternative is a great
  many fixed cameras and detection is handled by another sensor.

**Guard tours** deserve a specific warning. A PTZ cycling preset positions sounds like coverage and
is not: it is a fixed camera at each preset for a fraction of the cycle, with gaps between. If the
tour is 6 presets at 10 seconds each, any given location is recorded **1/6 of the time**. Write
that down when someone proposes it, because it sounds thorough and it is worse than a single fixed
camera.

> 🧠 **The rule:** *fixed cameras record; PTZs investigate.* If the design has a PTZ where a fixed
> camera should be, no operator behaviour recovers the missing footage. If it has both, the PTZ
> earns its cost the first time someone drives it.

---

## Fisheye: compute the falloff before you believe the coverage claim

A fisheye's marketing is "one camera covers the whole room." The arithmetic is less generous, and
it is easy.

Pixels are distributed around a circle, so at radius `r` the available pixels are spread over a
circumference of `2πr`. Density therefore falls as **`1/r`** — the same inverse-first-power law as
[32/02](../32_Engineering_Math/02_pixel_density.md), for the same reason.

For a 12 MP fisheye with roughly **4000 px** across the circle:

| Radius | Circumference | PPF | Class met |
|---|---|---|---|
| 5 ft | 31.4 ft | 127.3 | **identify** |
| 10 ft | 62.8 ft | 63.7 | recognise |
| 15 ft | 94.2 ft | 42.4 | recognise |
| **16 ft** | — | **~38** | **recognise floor** |
| 20 ft | 125.7 ft | 31.8 | observe |
| 25 ft | 157.1 ft | 25.5 | observe |
| 30 ft | 188.5 ft | 21.2 | observe |

**A 12 MP fisheye holds recognise to about a 16 ft radius** — roughly a 32 ft diameter circle, or
about 800 ft². That is one modest room, not one floor. Beyond it the camera delivers observe: you
will see that someone walked across the space and what they were doing, and you will not recognise
them.

**When a fisheye is the right answer:**

- Small-to-medium areas where the requirement is genuinely **observe** — a shop floor, an open-plan
  office, a lift lobby — and the value is retrospective context.
- Where you want a permanent wide record **alongside** targeted fixed cameras at the chokepoints.
- Low ceilings. Fisheye performance is strongly ceiling-height dependent: mounted too low, the
  useful radius is tiny; too high, the depression angle over near targets is severe.

⚠️ **Do not accept a fisheye as identification coverage of an area.** Compute the radius at which
it drops below your target class and put that circle on the drawing, exactly as
[lesson 04](04_dori_and_pixel_density.md) requires for every other camera.

⚠️ **Dewarping has a cost.** Client-side dewarping loads the workstation; server-side loads the
server; edge dewarping consumes camera resources and may limit frame rate. And some VMS platforms
handle a given manufacturer's fisheye well and others badly. `[MFR][VERIFY]` Verify the specific
camera-to-VMS combination before specifying it.

---

## Multisensor vs. multiple fixed: the decision, stated properly

Both deliver several views. The differences that matter:

| Factor | Multisensor wins | Multiple fixed wins |
|---|---|---|
| Switch ports and cable | ✅ One drop, one port | |
| Difficult cable paths | ✅ Decisive on retrofits and historic buildings | |
| Uniform mounting and appearance | ✅ | |
| Single mount at height | ✅ One lift visit to install | |
| **Failure concentration** | | ✅ One camera down ≠ all views down |
| **PoE simplicity** | | ✅ Standard af/at rather than bt Type 3 |
| **Licensing cost** | | ✅ Often, if the VMS licenses per imager |
| **Independent placement** | | ✅ Views can be at different heights and distances, each optimal |
| **Independent replacement** | | ✅ Replace or upgrade one view |
| **Per-view lens choice** | | ✅ Different focal length per direction, freely |

> 🧠 **The senior heuristic:** multisensors win on **installation**, fixed cameras win on
> **operation**. Since a system is installed once and operated for ten years, the default should be
> fixed cameras, and the multisensor should be chosen when something specific about the site —
> cable routing, mounting access, a single usable mounting point at a corner — makes installation
> the binding constraint. That is a real and common condition, so multisensors are frequently
> right; but "it's one device instead of four" is an installation argument being used to settle an
> operational question.

**The corner case where a multisensor is clearly correct:** an external building corner where you
need to see along two elevations and out into the car park. One mounting point exists, at height,
requiring a lift. Three imagers aimed independently from that point is exactly the product's
purpose.

---

## Environmental and housing ratings

| Rating | Means | Where it is specified wrong |
|---|---|---|
| **IP** (e.g. IP66, IP67) | Ingress protection: solids digit, then liquids digit | Specifying IP66 for a camera that will be **pressure-washed** — that is IP69K territory. Also: an IP66 camera with an unsealed cable entry is not IP66 `[VERIFY]` |
| **IK** (e.g. IK08, IK10) | Impact resistance in joules | Assuming a "vandal dome" is IK10 — many are IK08. The **bubble** and the **housing** may differ |
| **Operating temperature** | Range the camera functions in | Ignoring **cold start**. A camera rated to −40 °C operating may need a heater to *start* at −40 °C, which needs a higher PoE class `[MFR][VERIFY]` |
| **Corrosion** | Coastal, pool, and chemical environments | Standard housings fail fast near salt water or chlorine. Specify the coated or stainless variant |

⚠️ **The cold-start trap is the one that produces winter callbacks.** The camera worked all
autumn, the site loses power overnight in January, and the camera will not come back up because
the heater and the boot draw together exceed what the switch will deliver. Check the **startup**
power figure, not the operating one, and size the PoE budget on it
([32/05](../32_Engineering_Math/05_poe.md)).

## Design tradeoffs

| Decision | Buys | Costs |
|---|---|---|
| Turret over dome | Light, no IR bounce, no bubble to haze | Vandal resistance, discretion of aim |
| Dome over bullet | Discretion, vandal resistance, less web collection | Bubble light loss and cleaning |
| Multisensor over fixed ×4 | Ports, cable, one mount, one lift visit | Failure concentration, PoE class, often licensing |
| Fisheye over several fixed | One device, full context, software re-aim | Density falls as `1/r`; observe-grade beyond a modest radius |
| PTZ over fixed | Reach and zoom on demand | **Records one place at a time** |
| PTZ **plus** fixed | Assessment without losing coverage | Cost of both |
| Specialty LPR over general camera | Plates that actually read | Does nothing else |
| Higher IP/IK than needed | Margin | Cost, size, sometimes optical penalty |

## Common mistakes

⚠️ **Choosing a form factor before writing the question the camera answers.** Lesson 09's rule
governs this lesson too.

⚠️ **Believing "one fisheye covers the area" without computing the radius.** Do the `1/r`
arithmetic; put the class ring on the drawing.

⚠️ **Using a PTZ as primary coverage.** It records one place. Guard tours make this worse, not
better.

⚠️ **Not checking VMS licensing per imager.** Reverses multisensor economics routinely.

⚠️ **Specifying a multisensor onto an 802.3at switch.** Check the PoE class, and check the
**startup** figure.

⚠️ **Specifying domes reflexively indoors** where a turret would give a better image for the same
money.

⚠️ **Ignoring failure concentration.** Ask what goes dark when this one device fails, and whether
that is acceptable at this location.

⚠️ **Treating IP and IK as marketing numbers.** They are testable claims that get specified
carelessly and matter on the day of the incident or the storm.

## Junior vs. Senior

| | Junior | Senior |
|---|---|---|
| Compares cameras by | Resolution and price | Ports, licences, PoE class, failure behaviour, and lift visits over ten years |
| Sees a multisensor as | Four cameras for the price of one | One failure point serving four views, possibly four licences |
| Sees a fisheye as | Whole-area coverage | Identify to 5 ft, recognise to 16 ft, observe beyond — drawn as rings |
| Uses a PTZ for | Coverage | **Assessment**, always alongside fixed cameras |
| Specifies indoors | A dome, by default | A turret, unless vandal resistance is genuinely needed |
| Checks PoE by | Operating wattage | **Startup** wattage, including heaters, against the switch's per-port and total budget |
| Asks about failure | Whether there is a warranty | What goes dark, and whether the site can tolerate it until someone climbs up |

## 🔧 Field exercise

1. At an accessible site, inventory the form factors present. For each, write the question it
   answers and whether its form factor suits that question.
2. Find any fisheye or panoramic camera. Estimate its resolution, compute its recognise radius,
   and pace out that radius on the floor. Compare it to the area people believe it covers.
3. Find any PTZ. Ask whether anyone drives it, and if it runs a tour, how many presets and at what
   dwell. Compute the fraction of time each preset is recorded.
4. Look for a multisensor. Identify what would be lost if that single device failed, and ask
   whether anyone has considered it.

## Exercises

Work these before opening
[`_solutions/05_camera_form_factors_solutions.md`](_solutions/05_camera_form_factors_solutions.md).

**E5.1** A 20 MP fisheye distributes roughly 5200 px around its circle. It is proposed for an
open-plan office, ceiling 10 ft, to provide **recognise**-grade coverage of a 60 ft × 60 ft area.
 (a) Compute the radius at which it drops below recognise.
 (b) What fraction of the 60 × 60 ft area is covered at recognise or better? State your assumption
     about how the circle sits in the square.
 (c) Write the one-sentence finding for a design review.

**E5.2** A multisensor with four 4 MP imagers is proposed at a building corner to replace three
fixed cameras. The VMS licenses per imager at $180. The multisensor is $2,400; the three fixed
cameras are $520 each. Cable and termination is $340 per drop. The mounting point is at 24 ft and
requires a lift ($480 per visit, one visit covers all installation).
 (a) Compare the installed cost of both options.
 (b) State two non-cost factors that could reverse the decision, and which direction each pushes.
 (c) The site is a distribution centre where this corner is the only camera coverage of the
     hazardous-materials store. Does that change your recommendation? Why?

**E5.3** A client asks for a PTZ at each of four gates "so we can zoom in on anything suspicious."
There is no monitoring station; footage is reviewed after incidents.
 (a) State the problem in one sentence.
 (b) Give the recommendation and the reasoning.
 (c) If they insist on PTZs, name one configuration change that partially mitigates it, and state
     what it still does not fix.

**E5.4** For each, choose a form factor and give one sentence of justification:
 (a) A lift car interior.
 (b) A 300 ft dark perimeter fence line where the requirement is to know someone is approaching.
 (c) A vehicle entry lane where plates must be read.
 (d) An architecturally sensitive hotel lobby, 14 ft ceiling, needing recognise at the reception
     desk and observe across the lounge.
 (e) An exterior corner of a warehouse where two elevations and a yard must be seen, cable path is
     difficult, and the mount is at 26 ft.

**E5.5** 🧠 A colleague proposes replacing 14 fixed cameras in a warehouse with 4 multisensors,
citing a 30% saving on cable and installation. The warehouse runs 24/7 and has no on-site
technician; the nearest service call is four hours away. Write the response. It should agree with
whatever is right in the proposal, and it must engage with the actual saving rather than dismissing
it.

## Retrieval check

1. Why is a turret often a better indoor choice than a dome?
2. Do a multisensor and four equivalent fixed cameras differ in bandwidth or storage? Why?
3. What is the structural problem with a PTZ, and what does a guard tour do to it?
4. Fisheye pixel density falls as what function of radius?
5. Name the two costs that most often reverse a multisensor decision.
6. What is the cold-start trap, and which number do you check to avoid it?
7. Multisensors win on ____; fixed cameras win on ____.

## References

- [`../32_Engineering_Math/05_poe.md`](../32_Engineering_Math/05_poe.md) — PoE class allocation,
  switch budgets, and the four independent failure modes. Essential before specifying a
  multisensor.
- [`../32_Engineering_Math/03_bandwidth.md`](../32_Engineering_Math/03_bandwidth.md) — where the
  bitrate assumptions used in worked example 5.1 come from, and how much to trust them.
- [`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py) — `CameraGroup` and
  `VideoSystem`, used to produce the bandwidth and storage figures here.
- `[MFR][VERIFY]` PoE class, startup power, IP/IK ratings, per-imager licensing, and fisheye
  dewarping support are all per-product and per-VMS claims. Take them from datasheets for the
  actual models, and verify licensing with the VMS vendor in writing before comparing costs.
- `[STANDARD][VERIFY]` IP ratings per IEC 60529; IK ratings per IEC 62262; PoE per IEEE 802.3af /
  at / bt. Verify current editions.

---

**Next:** [06 — Compression, Bitrate, and Bandwidth](06_compression_and_bandwidth.md) — where the
numbers in this lesson's comparison table actually come from, and why two vendors will give you
two of them.
