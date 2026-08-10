# Answer Key — Quiz 03, Video Surveillance

> Do not open until you have written your answers to
> [`../quiz_03_video_surveillance.md`](../quiz_03_video_surveillance.md).
>
> Calculation values were produced by running
> [`../../28_Calculators/psec/`](../../28_Calculators/psec/) and transcribed.

---

## Part A — Concept and judgment (1 pt each)

**A1.** Scene/light → lens → sensor → ISP → encoder → network → recorder → display/operator.

**A2.** Binding: **link [1], light.** Bought: **link [3], sensor resolution.**

**A3.** Link [1]: photons that never arrived — gain amplifies noise with signal, it does not create
signal. Link [3]: motion blur, clipped highlights, and noise. Link [5]: detail discarded by the
encoder. None is recoverable downstream.

**A4.** **Recognise** means a viewer **who already knows the person** can say it is them — the
viewer supplies most of the information. **Identify** means a viewer who has **never met them** can
pick them out; the image must carry the information alone. It matters legally because evidence is
normally assessed by people who did not know the subject, so a recognise-grade image can be
sufficient for an employer's conversation with a named employee and insufficient to support
prosecution of a stranger. `[VERIFY — evidentiary sufficiency is jurisdiction-dependent.]`

**A5.** Light scales as **1/N²** (aperture *area* collects photons). Depth of field collapses as
roughly **1/f²**.

**A6.** **No.** Gain amplifies signal and noise equally — it changes brightness, not information.

**A7.** (i) The long lens plate capture requires has a depth of field of only a few feet, so the
face plane falls outside focus; (ii) the short exposure needed to freeze a moving plate
underexposes a face. Independent — either alone defeats the single-camera design.

**A8.** Because temporal compression encodes **change between frames**, and bitrate follows how
much the scene changes. A windy car park has constantly moving foliage, weather, headlights, and
shifting light; a corridor is empty and static most of the time. Scene content dominates resolution.

**A9.** CBR protects **predictable network and storage planning**. It fails by degrading image
quality when the scene becomes busy — i.e. **during the incident**, which is the only condition the
footage will ever be reviewed under.

**A10.** **No.** When motion triggers, the camera streams at full rate, so peak is unchanged. Only
storage and *average* bandwidth fall, both linearly with duty cycle.

**A11.** RAID protects against **disk failure**, and nothing else. It does not protect against fire,
flood, theft of the recorder, ransomware, accidental or deliberate deletion, or corruption
propagated by the controller. (Any three.)

**A12.** **Every camera answers exactly one written question. If you cannot write the question, do
not place the camera.**

**A13.** Any four of: misaimed; out of focus (varifocal drift); obscured by spider web, dust, or
condensation; physically blocked by stock, a vehicle, or vegetation; recording at reduced resolution
after a firmware update; frozen frame; stuck in night mode from a failed IR cut filter.

**A14.** Reliable analytics detect **geometric, well-defined events** — something crossed this line,
this object is a person. Unreliable ones require **interpretation** — "suspicious behaviour,"
"aggression" — for which no stable, generalisable definition exists.

---

## Part B — Scenario (2 pts each)

**B1.** **Cause: light (link [1]), delivered through the sensor and ISP.** At low illuminance the
camera selects a slow shutter; a subject walking at 3 mph smears across a large fraction of the
facial detail regardless of pixel density. **Cheapest fix:** raise illuminance at the face plane
enough that the camera selects 1/125 s or faster, and cap the maximum exposure time so it cannot
choose a slower one. (1 pt for identifying light/motion blur; 1 pt for the fix being lighting plus
an exposure cap rather than a camera upgrade.)

**B2.** Photosite area falls to **0.250×** — a loss of exactly **2.00 stops**. A client already 2
stops short becomes **4 stops short**, and the illuminance needed to rescue the scene rises from 4×
to **16×** current levels. The upgrade moves them further from working, not closer.

**B3.** (i) **No distance is stated** — PPF falls as 1/D, so "80 ppf" is a number that is true
somewhere, not a specification. (ii) It almost certainly uses **floor distance rather than slant
range**; at a 14 ft mount with a 5 ft face plane the true optical path is longer, so the delivered
density is overstated. *(Also creditable: no depression angle stated.)*

**B4.** The flat rate over-estimated the interiors (2.2 actual vs 3.0 assumed) and under-estimated
the exteriors by more than 3× (9.8 vs 3.0). Because the interior over-estimate **partially masked**
the exterior under-estimate, the site-wide total was only moderately wrong rather than obviously
wrong — so nothing looked anomalous at design review. The error is applying a **single bitrate to a
mixed system**. (1 pt for the flat-rate root cause; 1 pt for the masking explanation.)

**B5.** Any three of: *"Redundant against which components specifically?"* — a non-decomposing
answer usually means "the storage is RAID." *"How many seconds of video are lost at failover?"* —
"none" is not credible; a specific range signals honesty. *"Is pre-failover video still retrievable
afterwards?"* — hesitation reveals the orphaned-footage gap. *"Is the standby's own health
monitored?"* — an unmonitored standby is a coin flip. *"What is the documented test procedure?"* —
reluctance to test means it has not been tested. *"Does recording continue if the licence server is
unreachable?"* — catches the commercial failure mode.

**B6.** **Problem:** everyone leaving is silhouetted against daylight, and everyone leaving is the
population of interest — the exact population the exit camera exists to capture. **Cost of the
fix:** free at design time (aim it inward); a ladder afterwards. **Why it is a design failure:** the
aim direction is a decision made on the drawing against a known lighting condition, not an
installation error — nothing about the site was unknown when the aim was chosen.

**B7.** It implies the monitoring detects only **hard failures** (device offline, stream lost) —
every one of those 14 cameras was online, streaming, and green. It also implies no manual
verification regime and, critically, **no reference images from commissioning**, so the date each
camera moved cannot now be established. **The single most valuable automated check: scene-change
detection against a stored reference frame.**

**B8.** Any three of: **assess** (distinguish a fox from an intruder instantly, with context);
**respond physically** (approach, challenge, lock, escort — analytics contribute nothing to `T_R`);
**deter by visible presence**; **notice what nobody specified** (propped fire door, leak, smell of
burning, unexpected contractor) — routinely the largest real value and never in the business case;
**life safety and first response**; **operate when the network is down**.

---

## Part C — Calculation (3 pts each)

**C1.** 9 ft mount, 20 ft floor distance, face plane 5 ft, 4 mm, 2688 px, 1/2.8" (w = 5.37 mm).

```
(a) slant = √(20² + (9−5)²) = √(400 + 16) = √416 = 20.40 ft
(b) W   = 20.40 × 5.37 / 4 = 27.38 ft
    PPF = 2688 / 27.38 = 98.2 ppf
(c) identify (≥76 ppf), with 1.29× margin. Depression angle 11.31° — well inside 30°.
```

**C2.**

```
D_max = (px × f) / (PPF × w) = (2688 × 4) / (76 × 5.37) = 26.35 ft
```

**C3.**

```
(a) smear = 4.4 ft/s × (1/30) s = 0.1467 ft = 1.76 in
            0.1467 ft × 120 ppf = 17.60 px
(b) eye-to-eye = 2.5 in = 0.2083 ft → 0.2083 × 120 = 25.00 px
(c) ratio = 17.60 / 25.00 = 0.704
```

**Doubling the resolution does not change the ratio at all.** Both the smear and the facial feature
are physical lengths in the scene, so multiplying by pixel density scales both equally and the ratio
cancels: `(s × PPF)/(e × PPF) = s/e`. **Motion blur relative to facial detail is invariant under
every change of resolution, lens, or distance** — it can only be fixed by a faster shutter (which
needs light) or a slower subject (which needs a chokepoint). *(1 pt for each of (a) and (b); 1 pt
for the invariance and its explanation — this is the most important single result in the module.)*

**C4.**

```
(a) stops = log₂((1/25) ÷ (1/125)) = log₂(5.00) = 2.32 stops
(b) required = 4 lux × 5.00 = 20.0 lux
(c) Adding light to the scene — every other source of stops costs depth of field
    (wider aperture), noise (gain), or pixel density (lower resolution).
```

**C5.** 16 mm, f/2.0, c = 0.00400 mm, focused at 45 ft.

```
(a) H = f²/(N·c) + f = 256/(2.0 × 0.004) + 16 = 32,016 mm = 105.04 ft
(b) D_n = s(H−f)/(H+s−2f), s = 45 ft = 13,716 mm  →  31.51 ft
    (far limit for reference: 78.69 ft)
(c) NO — the doorway at 20 ft is 11.5 ft closer than the near limit of 31.51 ft.
```

**One fix and its cost** (any one):
- **Stop down to f/8** → near limit 16.60 ft, doorway sharp. **Cost: 93.8% of the light** (4 stops)
  — usually fatal at night.
- **Refocus to 20 ft** → 16.81–24.68 ft sharp. **Cost: the 45 ft subject leaves the DOF entirely.**
- **Fit an 8 mm lens** → 16.60 ft to infinity. **Cost: half the pixel density everywhere.**

*(Note: focusing at the hyperfocal distance is the reflex answer and it **fails** — it pushes the
near limit out to 52.58 ft.)*

**C6.** 110 ft elevation, 15% overlap (effective = raw × 0.85).

```
(a) recognise, 4 MP: 2688/38 = 70.74 ft → 60.13 ft effective → ceil(110/60.13) = 2 cameras
(b) identify,  4 MP: 2688/76 = 35.37 ft → 30.06 ft effective → ceil(110/30.06) = 4 cameras
(c) identify,  8 MP: 3840/76 = 50.53 ft → 42.95 ft effective → ceil(110/42.95) = 3 cameras
```

**Comment:** the 8 MP option saves **one** camera, not the two you might expect from 43% more
coverage width — because camera count is a **ceiling function** and extra pixels only convert into
fewer cameras when they cross an integer boundary. Against that single-camera saving, 8 MP costs
1.03 stops of light on the same sensor size, plus higher bitrate and storage. **On a night-critical
elevation the 4 MP option is very likely the better engineering choice despite needing one more
camera.**

**C7.** 12 MP fisheye, ~4000 px around the circle. `PPF = px / (2πr)`.

```
(a) r = 4000 / (2π × 38) = 16.75 ft
(b) area = π × 16.75² = 882 ft²
```

**(c) Assessing the 50 ft × 50 ft claim:**

```
room area = 2500 ft²;  recognise circle = 882 ft²  →  35.3% of the floor
centre-to-corner = √(25² + 25²) = 35.36 ft  →  PPF = 4000/(2π × 35.36) = 18.0 ppf
```

**The claim fails on two counts.** Only **35%** of the room reaches recognise, and the room corners
sit at **18.0 ppf — below the observe threshold of 19**, so they do not even meet the lowest useful
class. The camera does "cover" the room in the sense of having it in frame, and covers roughly a
third of it usefully. **Always ask "at what class?"** — the claim is made without one precisely
because naming one defeats it.

**C8.** 25 cameras, 2 false alarms/camera/day, 2 true events/year.

```
(a) alarms/year = 25 × 2 × 365 = 18,250
    precision   = 2 / (18,250 + 2) = 0.0110%
(b) 18,250 / 2 = 9,125 false alarms per true event
(c) 95% reduction → 912 alarms/year → precision = 2/(912+2) = 0.219%
```

**Does it change the recommendation? No.** At 0.219%, roughly **one alarm in 457 is real**. An
operator cannot sustain attention against that, and will — entirely rationally — stop responding
within months. **The base rate, not the detector, is the constraint:** with only 2 true events a
year, no achievable false-alarm rate produces a usable live alarm stream. The correct recommendation
is unchanged — use the analytics for **retrospective search**, where a false positive costs one
second to dismiss and precision does not matter, and if live perimeter detection is genuinely
required, use a dedicated detection sensor cueing human assessment.

*(1 pt for (a), 1 for (b), 1 for correctly concluding the upgrade does **not** change the
recommendation. An answer that computes 0.219% and calls it an improvement worth buying scores 2 of
3 — the arithmetic is right and the engineering judgment is the point of the question.)*

---

## Scoring notes

**The pattern that matters:** losses concentrated in **Part B** rather than Part C. The arithmetic
in this module is the easy half — `psec` performs all of it, and the module exists because
performing it is not the same as knowing what to compute or what to do with the answer.

Three questions carry the module's core ideas, and getting them right matters more than the total:

- **C3(c)** — the invariance of blur-to-detail under pixel density. If this is not solid, the whole
  "buy more resolution" conversation cannot be won.
- **C8(c)** — that a 95% improvement does not rescue a low-base-rate alarm system.
- **A12** — the placement rule, which governs every design decision in the module.

**Next:** [the park-and-ride garage capstone](../03_Video_Surveillance/_exercises/garage_design.md),
which is built to make several of the instincts this quiz rewards produce the wrong answer.
