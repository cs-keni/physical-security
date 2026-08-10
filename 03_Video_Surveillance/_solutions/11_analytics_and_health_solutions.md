# Solutions — 11 Analytics and Health Monitoring

> Work the exercises in [`../11_analytics_and_health.md`](../11_analytics_and_health.md) before
> reading this.

---

## E11.1 — 35 perimeter cameras, live alarm response

**(a) Alarms per year and precision.**

```
true events = 3 in 2 years = 1.5 per year
alarms/day   = 35 cameras × 1.0 = 35
alarms/year  = 35 × 365 = 12,775
precision    = 1.5 / (12,775 + 1.5) = 0.0117%
```

**About one alarm in 8,500 is real.**

**(b) False alarms per true event.**

```
12,775 / 1.5 = 8,517 false alarms per genuine intrusion
```

At 30 seconds of assessment each, that is **18 minutes per day**, or **106 operator-hours per
year**, spent almost entirely on nothing.

**(c) What will happen, and over what timescale.**

Predictably, and in this order:

- **Weeks 1–2.** Operators assess alarms conscientiously. Everyone notices the volume. Someone asks
  whether it can be tuned.
- **Weeks 3–8.** Assessment becomes cursory — alarms are acknowledged and cleared without the
  operator genuinely looking, because 60 consecutive false alarms have taught them, correctly, what
  the next one is. **This is rational adaptation, not negligence.**
- **Months 2–6.** Alarms are muted at night, or the noisiest cameras are excluded from the analytic,
  or notification is routed to a mailbox nobody opens.
- **Months 6–18.** The analytic is disabled or ignored entirely. It remains on the as-built drawings
  and in the client's understanding of what they own.

**The end state is the dangerous one:** the client believes they have analytics-driven perimeter
detection, and they have nothing — and nobody made a decision to remove it. That is worse than never
having installed it, because it displaced a control that would have worked.

**(d) The recommendation.**

> Do not deploy this as a live alarm system. The arithmetic says it cannot work: with roughly 1.5
> genuine intrusions a year against 12,775 false alarms, about one alarm in 8,500 is real, and no
> operator can sustain attention against that. Even if the vendor improved the analytic by 99%, it
> would still be about one alarm in 100.
>
> **What I would do instead:**
>
> 1. **Enable object classification** (person vs. vehicle vs. animal), which removes most weather,
>    foliage, and animal triggers and is the single largest real-world reduction available.
> 2. **Constrain the geometry** — tripwires set in from the fence line, perpendicular to travel,
>    away from frame edges, on cameras chosen for the analytic rather than for viewing.
> 3. **Use the analytics for retrospective search, not live alerting.** "Show me every person who
>    crossed this line overnight" turns an investigation from hours into seconds, and a false
>    positive costs one second to dismiss rather than eroding an operator's trust.
> 4. **If live detection at the perimeter is genuinely required**, the correct instrument is a
>    dedicated detection sensor — thermal, fence-mounted detection, or a beam — cueing a camera for
>    human assessment. Cameras plus analytics are the wrong tool for a low-base-rate live alarm.
> 5. **Budget a tuning period** of several weeks with a written false-alarm acceptance threshold
>    before handover, whatever is deployed.

---

## E11.2 — Would you trust it?

**(a) Person vs. vehicle classification on a car park camera.**
**Yes, with verification.** This is squarely in the reliable category — a geometric, well-defined
distinction that modern classifiers handle well. **Require:** a site trial across a full weather
cycle including rain and night, confirmation the camera's pixel density on target supports the
classifier's minimum object size, and a measured false-classification rate. It is also the single
most valuable thing you can enable to reduce false alarms.

**(b) "Aggression detection" in a hospital waiting area.**
**No.** Aggression is a matter of interpretation, not a geometric event, and there is no stable,
generalisable definition for a classifier to learn. In a hospital the failure modes are severe and
biased: distress, intoxication, dementia, autism, pain, and cultural differences in gesture and
volume will all trigger it, and the people flagged will disproportionately be those already
vulnerable. **Before I would consider it:** independent evidence of performance in a comparable
setting, a measured false-positive rate, a clear statement of what staff do on an alert, and a
review of the harm a false positive causes. In practice this bar is not met. **Recommend instead:**
a staff-operated duress button, which has near-perfect precision because a human decides.

**(c) People counting at a single entrance turnstile.**
**Yes.** This is the best case for counting — a chokepoint, one person at a time, constrained
geometry, consistent scale. **Require:** confirmation of behaviour at tailgating and with
pushchairs/wheelchairs, and a manual count over a busy hour to establish the error rate. Counting
across an open area would be a different and much weaker answer.

**(d) Object-left-behind in a busy airport concourse.**
**Cautiously, and not as a primary control.** The analytic is moderate at best, and a busy concourse
is its worst environment: constant occlusion, people setting bags down legitimately for minutes at a
time, and lighting that changes. Expect a high false-positive rate. **Require:** a realistic trial
at peak, an agreed dwell threshold, and — critically — a defined response that is proportionate to
the precision (dispatch someone to look, not evacuate). Useful as a cue to a human; not as a trigger
for action.

**(e) LPR on the existing overview camera at a gate.**
**No.** Plate capture is its own discipline ([lesson 02](../02_optics_and_lenses.md)): it needs a
long lens, a short exposure to freeze a moving plate, often dedicated IR, and a narrow field aimed
at plate height. An overview camera is chosen for the opposite of all four. It will read plates in
good light on stationary vehicles and fail at night, in rain, and on anything moving — which is when
it is needed. **Require:** a dedicated LPR camera, and if the client wants both plate and overview,
that is two cameras (worked example 2.2).

---

## E11.3 — 90 cameras, 14 misaimed or obstructed, client unaware

**(a) What it implies about the health monitoring.**

**15.6% of the estate was compromised and invisible**, which tells us the monitoring in place
detects only **hard failures** — device offline, stream lost. Every one of these 14 cameras was
online, streaming, recording, and showing green on the dashboard while pointing at a wall or looking
through an obstruction.

It further implies **no manual verification regime**, since a human comparing views against
references would have found them, and **no reference images** from commissioning, since without them
there is no objective standard to compare against. The client's belief that they were covered was
never tested at any point in three years.

**(b) The monitoring regime that would have caught them.**

**Automated:**

| Check | Catches |
|---|---|
| **Scene-change detection** against a stored reference frame | **Misaiming and obstruction — the primary gap here.** The single most valuable non-standard check |
| Focus/sharpness metric trended over time | Varifocal drift, condensation, dirty domes, hazed bubbles |
| Mean luminance overnight vs. baseline | Failed lighting, failed IR emitters |
| Frame rate / bitrate deviation from commissioned baseline | Firmware regressions, config drift, network problems |
| Recording verification (not just streaming) | Recorder-side failures |
| Retention achieved per camera vs. specification | Under-sizing, bitrate drift |
| NTP offset | Time sync loss |
| **Alert delivery to a named role, tested** | The failure that disables all of the above |

**Manual:**

- **Quarterly view verification** — every camera's live view compared against its dated reference
  image, by a named person, with findings logged.
- **Annual physical inspection** — dome cleaning, mounting security, cable condition, sunshade and
  housing check.
- **Reference image refresh** whenever a camera is legitimately re-aimed, so the baseline stays true.

**(c) Annual manual verification cost.**

```
90 cameras × 5 min = 450 min = 7.5 hours per quarter
× 4 quarters       = 30 hours per year
```

**30 hours per year** — under four working days, for a 90-camera estate. Against three years in
which 14 cameras recorded nothing useful, this is trivially justified.

**(d) The finding, for the report.**

> **Finding: 14 of 90 cameras (15.6%) are significantly misaimed or obstructed, and the condition
> was not detected.**
>
> These cameras have been online and recording throughout, and appear healthy on the system's
> monitoring dashboard, because the monitoring in place detects only loss of device connectivity.
> It does not detect a camera that is streaming normally while pointing somewhere other than its
> designed view. The affected positions include [list], of which [n] are identification positions at
> chokepoints.
>
> **Consequence:** for the period these cameras have been in their current state, the coverage shown
> on the as-built drawings has not existed. Any incident in the affected areas during that period
> will not have been recorded as designed, and the system's own records give no indication of when
> each camera moved. Because no reference images were captured at commissioning, the date each
> camera was displaced cannot be established.
>
> **Recommendation:** (i) re-aim and re-focus all 14 positions and capture dated reference images
> for the full estate; (ii) implement scene-change monitoring against those references, with alerts
> to a named role rather than an individual; (iii) institute quarterly manual view verification,
> approximately 30 hours per year for this estate; (iv) verify the recipient of all system alerts
> and test alert delivery.

**What is being graded:** distinguishing hard failures from silent ones and explaining why the
dashboard was green; noting that **the absence of reference images means the duration cannot be
established**, which is the finding within the finding; quantifying the manual cost so the
recommendation is actionable; and specifying alerts to a **role**, not a person.

---

## E11.4 — Acceptance test specification for Meridian camera C1

> **Acceptance test — C1, main vestibule identification camera**
>
> **Design intent:** identify any person entering through the main vestibule, to a standard
> sufficient for a viewer who has never met them. Target: identify class, ≥76 ppf at the inner
> vestibule door, depression angle ≤30°.
>
> **T1 — Geometry and pixel density (daylight).**
> *Method:* a test subject of known height (record it) stands at the inner vestibule door, on the
> marked design position. Capture a still from the recorded stream. Measure the subject's height in
> pixels and derive delivered PPF. Record the measured mounting height and horizontal distance.
> *Pass:* delivered ≥76 ppf at the design position, and computed depression angle ≤30°.
> *Expected:* ~160 ppf at 12.50 ft slant range, 16.26° — a design margin of 2.11×.
> *Fail action:* re-aim, re-lens, or reposition; retest.
>
> **T2 — Night verification, walking subject.** *(The test that matters most.)*
> *Method:* repeat T1 after dark, with all normal night lighting in its normal state and no
> temporary lighting. The subject **walks** through the vestibule at a normal pace (~3 mph) three
> times. Export the recording — do not assess the live view.
> *Pass:* the subject's face is identifiable from the **exported recording** by an assessor who has
> not met them, on at least two of three passes. Record the camera's actual shutter speed and gain
> at the time of test.
> *Fail action:* measure illuminance at the face plane; compare against the specified 12.5 lux
> minimum; remediate lighting or cap the maximum exposure time. **Retest at night.**
>
> **T3 — Illumination.**
> *Method:* measure illuminance with a calibrated meter at 5 ft above finished floor, facing the
> camera, at the design position and at three points across the vestibule, at night.
> *Pass:* ≥12.5 lux at every measured point, and a max:min uniformity ratio no worse than 4:1.
>
> **T4 — Backlight behaviour.**
> *Method:* repeat T1 at midday with full sun on the north elevation, the worst-case backlight
> condition for this position.
> *Pass:* the subject's face remains identifiable and is not rendered as a silhouette.
>
> **T5 — Recording, retention, and export.**
> *Method:* confirm the camera is recording at the specified bitrate, codec, and frame rate.
> Export a 60-second clip; open it on a machine without the VMS client.
> *Pass:* export opens and plays; native timestamp and camera identity are present; hash or
> signature verifies; export completes in under 5 minutes.
>
> **T6 — Reference image capture.**
> *Method:* capture and date a reference still of the commissioned view; file with the as-built
> documentation and load as the baseline for scene-change monitoring.
> *Pass:* image filed and monitoring baseline configured.
>
> **Witnessed by:** [engineer], [client representative], [installer]. **Date:** ______
> **All tests to be witnessed. T2 and T3 to be conducted after full darkness — not at dusk.**

**What is being graded:** including **night testing with a walking subject** and assessing the
**exported recording** rather than the live view; measuring illuminance as a separate pass/fail
rather than assuming it; testing the worst-case backlight; specifying **who** witnesses; and
capturing the reference image as part of acceptance. A specification that tests only daylight pixel
density accepts the system under the conditions it performs best in, which is how systems come to be
signed off and then found wanting.

---

## E11.5 — 🧠 Replacing two overnight officers with analytics

**(a) What the analytics would have to achieve.**

Assume ~12 cameras covering the 1,800 ft perimeter (one per ~150 ft), against **4 genuine incidents
per year**:

| False alarms/camera/day | Alarms/year | Precision |
|---|---|---|
| 1.0 | 4,380 | 0.091% |
| 0.5 | 2,190 | 0.182% |
| 0.1 | 438 | **0.905%** |

Even at an excellent **0.1 false alarms per camera per day**, fewer than 1 alarm in 100 is real.

To reach even **10% precision** — still nine false alarms for every real one — total alarms must fall
to **36 per year**, which across 12 cameras is **one false alarm per camera every 122 days.**

**For an outdoor perimeter, in weather, with vegetation and wildlife, that is not achievable.** State
it plainly: the required performance is not a stretch target, it is outside what the technology
does.

**(b) What the officers do that analytics do not.**

This is the heart of the answer, and it is where the cost argument is actually won or lost.

1. **Assess and decide.** An officer distinguishes a fox from an intruder from a lost delivery driver
   in one second, with context no classifier has.
2. **Respond physically.** They approach, challenge, lock a door, escort someone off site. Detection
   without response contributes nothing to [the timeliness inequality](../01_imaging_chain.md) —
   `T_R` is the officer.
3. **Deter by presence.** A patrolling officer is visible and unpredictable, which prevents events
   rather than recording them. Analytics deter nobody.
4. **Notice what nobody specified.** A propped fire door, a water leak, a smell of burning, a vehicle
   parked oddly, a contractor who should not be there. **This is routinely the largest real value of
   overnight staff and it never appears in the business case**, because it prevents incidents that
   are therefore never counted.
5. **Life safety and first response.** Medical emergencies, fire alarm investigation, letting the
   fire service in, accounting for people.
6. **Operate under failure.** When the network drops, the analytics stop. The officer does not.

**(c) Recommendation, engaging with the cost argument.**

> Two officers overnight is roughly **7,300 officer-hours a year**, and I understand entirely why
> that is the line being looked at. I want to give you a straight answer rather than a defensive
> one.
>
> **The proposal as framed will not work.** With four genuine incidents a year across this
> perimeter, even excellent analytics would generate several hundred alarms a year, meaning fewer
> than one alarm in a hundred is real. A remote monitoring centre facing that ratio will, entirely
> reasonably, stop treating alarms as urgent within a couple of months — that is what always
> happens, and the end state is that you are paying for monitoring that nobody acts on while
> believing the perimeter is covered.
>
> **The deeper issue is that this compares the wrong things.** Analytics can detect. Your officers
> detect, assess, decide, respond, deter by being visible, and — the part that never shows up in the
> business case — notice the propped fire door, the leak, the contractor who should not be on site.
> Removing them does not just change how detection happens; it removes response entirely. A
> detection with no response does not prevent anything, it documents it.
>
> **What I would propose instead**, if the cost needs to come down:
>
> - **Reduce, don't replace.** One officer overnight instead of two, with analytics and better
>   lighting extending their reach so one person can cover what two did. That is roughly a 50%
>   saving with response capability retained.
> - **Use analytics to cue the officer, not a remote centre.** At 1% precision an alarm is a poor
>   basis for dispatching a response team and a perfectly good basis for telling an officer already
>   on site which camera to glance at. Precision matters far less when assessment is instant and
>   free.
> - **Spend part of the saving on lighting and on the perimeter itself.** Lighting deters, improves
>   every camera, and costs nothing to operate. Delay at the fence buys response time and is what
>   makes any detection timely.
> - **If the officers must go entirely**, then be clear that the site is accepting a documentation
>   system rather than a prevention one overnight, and that response becomes a police call with
>   whatever response time that carries. That may be an acceptable business decision — but it should
>   be made knowingly, in writing, not as a by-product of a technology substitution.

**What is being graded:** doing the precision arithmetic and stating plainly that the required
performance is unachievable rather than merely difficult; enumerating the officer functions that
analytics do not replace, especially the **unspecified-noticing** one; **taking the cost pressure
seriously** and offering a genuine 50% option instead of simply defending headcount; and correctly
placing the final decision with the client while insisting it be made explicitly. An answer that
only says "analytics can't replace guards" is right and useless.

---

## Retrieval check — answers

1. Reliable analytics detect **geometric, well-defined events** (something crossed this line, this
   is a person). Unreliable ones require **interpretation** (suspicious behaviour, aggression) —
   things with no stable definition.
2. **Precision** is the fraction of alarms that are real. For 20 cameras × 3 FA/day = 21,900
   alarms/year against 2 true events: **0.009%.**
3. **No.** A 99% reduction gives 219 alarms/year and precision of **0.905%** — still fewer than 1 in
   100 real. The base rate, not the detector, is the constraint.
4. **Retrospective search and filtering.** Precision does not matter because a human is already
   searching and a false positive costs one second to dismiss — there is no trust to erode.
5. Any four of: misaimed, out of focus, obscured by web/dust/condensation, physically blocked,
   recording at reduced resolution after a firmware change, frozen frame, stuck in night mode.
6. **Scene-change detection** against a stored reference frame — it catches misaiming, obstruction,
   and tampering, none of which appear as offline.
7. **Night verification with a walking subject; retention actually achieved; failover test; health
   alert delivery test; reference image capture.**
8. **A dated reference image of every camera's intended view**, filed with the as-built
   documentation.
