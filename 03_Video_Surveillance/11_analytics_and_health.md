# 11 — Analytics and Health Monitoring

> Two subjects in one lesson because they are the same subject: **whether the system is still doing
> what you designed it to do, a year after you left.**
>
> Analytics is where the industry's claims are loosest. Health monitoring is where its silence is
> loudest. Together they decide whether the design in lessons 01–10 is still true in 2029.
>
> Link **[8]** of [the imaging chain](01_imaging_chain.md) — and the feedback loop back to link [1].

## Learning objectives

- Separate analytics that work reliably from analytics that are sold as though they do.
- Compute the **precision** of an alarm system and predict operator behaviour from it.
- Explain why reducing false alarms by 99% can still leave a useless alarm system.
- Design analytics for the job they are actually good at.
- Specify health monitoring that detects the failures nobody notices.
- Build acceptance and periodic verification into the design rather than hoping.

---

## What analytics reliably do

Ordered by how much I would trust them on a real project. `[PRACTICE]` — this ordering is
engineering judgment, and the boundary moves as the technology improves. Verify against the
specific product on the specific site.

| Analytic | Reliability | Notes |
|---|---|---|
| **Line crossing / tripwire** | **Good** | With correct geometry and a well-chosen line. The workhorse |
| **Intrusion into a defined zone** | **Good** | Same caveats |
| **Object classification (person vs. vehicle vs. animal)** | **Good and improving** | The single biggest reducer of false alarms — it eliminates most weather and animal triggers |
| **People counting** | **Good** at a chokepoint | Poor across an open area |
| **Loitering / dwell time** | **Moderate** | Needs a defined zone and a sensible threshold |
| **Object left behind / removed** | **Moderate** | Sensitive to lighting change and busy scenes |
| **Licence plate recognition** | **Good with dedicated hardware** | A discipline of its own ([lesson 02](02_optics_and_lenses.md)); poor with a general camera |
| **Directional flow / wrong way** | **Moderate** | Good at chokepoints |
| **Face recognition** | **Highly variable** | Depends on capture conditions, gallery quality, and threshold. Carries the heaviest legal and ethical load `[VERIFY]` |
| **"Suspicious behaviour" detection** | **Treat as marketing** | There is no reliable, generalisable definition of suspicious behaviour. Be sceptical of anything claiming to detect intent |
| **Aggression / violence detection** | **Treat as marketing** | Same |
| **Weapon detection** | **Highly variable** | Improving; verify on site, with the actual failure modes, before relying on it |

> 🧠 **The pattern is worth naming.** Analytics are reliable when they detect **geometric,
> well-defined events** — something crossed this line, something is in this zone, this is a person
> not a fox. They become unreliable as the thing being detected becomes a matter of **interpretation**.
> "A person crossed the fence line" is a fact. "A person is behaving suspiciously" is a judgment, and
> a system claiming to make it is claiming something nobody has a stable definition for. Apply that
> test to any analytic you are shown.

⚠️ **Analytics need different camera placement than viewing does.** A line-crossing analytic wants
the subject crossing the frame perpendicular to the camera axis, at consistent scale, with the line
away from the frame edge. An identification camera wants the subject frontal and close. **These are
different cameras**, and a design that bolts analytics onto cameras chosen for viewing will produce
poor detection and blame the software. Decide which cameras carry analytics **during**
[lesson 09](09_camera_placement.md)'s placement process, not afterwards.

---

## 🧮 Worked example 11.1 — why your alarm system is ignored

**The arithmetic every designer should be able to do and almost none do.**

A perimeter with **20 cameras** running line-crossing analytics. The site experiences **2 genuine
intrusion events per year**. Assume 30 seconds of operator time to assess each alarm.

| False alarms per camera per day | Alarms/day | Alarms/year | **Precision** | Operator time/day |
|---|---|---|---|---|
| 0.05 | 1.0 | 365 | **0.545%** | 0.5 min |
| 0.20 | 4.0 | 1,460 | 0.137% | 2.0 min |
| 1.00 | 20.0 | 7,300 | 0.027% | 10.0 min |
| **3.00** | **60.0** | **21,900** | **0.009%** | **30.0 min** |
| 10.00 | 200.0 | 73,000 | 0.003% | 100.0 min |

**Precision** is the fraction of alarms that are real. At a very ordinary 3 false alarms per camera
per day, an operator assesses **10,950 false alarms for every true one.**

Now watch what improving the analytic buys:

| Improvement from the 3/day baseline | Alarms/year | Precision |
|---|---|---|
| 50% reduction | 10,950 | 0.018% |
| 90% reduction | 2,190 | 0.091% |
| **99% reduction** | **219** | **0.905%** |

> ⚠️ **Even a 99% reduction in false alarms leaves fewer than 1 alarm in 100 being real.** This is
> the base-rate problem, and it is not solvable by improving the detector. When true events are
> genuinely rare — 2 a year — no achievable false-alarm rate produces an alarm stream a human will
> keep taking seriously.

**What actually happens, predictably:** operators stop responding. Not through negligence — through
entirely rational adaptation to a signal that is almost never real. The alarms get acknowledged
without assessment, then muted, then the analytic is disabled, and eighteen months later nobody
remembers it was specified. **This is the normal life cycle of a badly-conceived analytics
deployment**, and it is a design failure, not an operations failure.

### What to do instead

**1. Use analytics for search and filtering, not live alarms.** This is the highest-value and most
under-sold application. "Show me every person who crossed this line between 22:00 and 06:00 last
Tuesday" turns eight hours of footage into six clips. There is **no false-alarm cost** in
retrospective search — a false positive is a clip you dismiss in one second — and it makes every
investigation dramatically faster. Precision does not matter when a human is already searching.

**2. Raise the base rate before deploying live alarms.** Analytics work as an alarm source where
genuine events are common enough to sustain attention, or where the alarm gates something
consequential (a gate opening, a door releasing). If true events are twice a year, do not build a
live alarm around them.

**3. Use object classification.** Filtering to "person" eliminates most weather, foliage, and
animal triggers — the single most effective real-world false-alarm reduction available.

**4. Cue, don't decide.** Analytics that direct a PTZ or bring a camera onto a monitor for a human
to assess are useful at far lower precision than analytics expected to trigger a response.

**5. Constrain the geometry.** A tripwire 3 ft inside a fence line, aimed perpendicular, with
classification enabled, in a scene with controlled lighting, performs vastly better than the same
analytic on a general-purpose camera. **Most analytics failures are placement failures.**

**6. Tune, and budget for tuning.** Analytics are commissioned over weeks, not configured in an
afternoon. Every project that skips this gets the 3/day column. **Put tuning time in the
programme.**

### The environmental causes of false alarms

Spiders and their webs (drawn by IR — [lesson 03](03_sensors_and_low_light.md)), moving vegetation,
rain and snow, headlights and moving shadows, reflections off wet surfaces, birds and animals,
flags and banners, sunrise and sunset transitions, camera shake in wind, and insects crossing the
lens at close range. **Every one of these is a site condition**, which is why analytics performance
is a property of the installation and not of the product.

---

## Health monitoring: knowing the system still works

> **A camera that has been misaimed for six weeks is worse than no camera, because the client
> believed they were covered.**

| Duration undetected | Footage lost |
|---|---|
| 1 week | 7 days of a wall |
| 6 weeks | 42 days of a wall |
| 6 months | 182 days of a wall |

The failures that matter are the ones that **do not announce themselves**. A camera that goes
offline generates an alert on any system. A camera that is:

- knocked out of aim by a ladder, a door, or a delivery,
- gone soft because the varifocal drifted ([lesson 02](02_optics_and_lenses.md)),
- obscured by a spider web, dust, condensation, or a hazed dome,
- blocked by a pallet, a display, a parked lorry, or a tree in leaf,
- recording at a fraction of its configured resolution after a firmware update,
- stuck showing a frozen frame,
- or in permanent night mode because the IR cut filter stuck,

...is **online, streaming, recording, and green on every dashboard.** No basic health check catches
any of these.

### What to specify

| Check | Detects | How |
|---|---|---|
| **Device online / stream present** | Hard failures | Standard in every VMS |
| **Recording actually occurring** | Recorder-side failures, disk full, licence issues | Verify recording, not just streaming |
| **Retention actually achieved** | Under-sized storage, bitrate drift ([lesson 06](06_compression_and_bandwidth.md)) | Compare oldest available recording against specification, per camera |
| **Scene change detection** | **Misaiming, obstruction, tampering** | Compare a current reference frame against a stored one; alert on gross change. **The single most valuable non-standard check** |
| **Focus / sharpness metric** | Drift, condensation, dirty dome | Contrast measurement on a static region over time |
| **Illumination check** | Lighting failures, IR emitter failure | Mean luminance overnight vs. baseline |
| **Frame rate and bitrate deviation** | Firmware regressions, network problems, config drift | Alert on deviation from the commissioned baseline |
| **Time sync status** | The failure that destroys evidentiary value ([lesson 07](07_storage_and_retention.md)) | NTP offset monitoring |
| **Certificate and licence expiry** | Systems that stop for commercial reasons | Calendar alerting |

⚠️ **And the check that matters most: the alerts must reach a human who acts.** The most common
finding in any survey is monitoring configured to an address nobody reads — often a departed
employee's ([lesson 07](07_storage_and_retention.md) E7.3). **Specify the recipient by role, not by
person**, and test it during commissioning by deliberately failing a camera.

### The manual verification baseline

Automated checks do not remove the need to look. A quarterly walk of every camera view — comparing
the live image against the commissioned reference image — costs, for a 60-camera site at 5 minutes
each, **5 hours per quarter, or 20 hours per year.** That is a small fraction of one person's time
and it is the only check that catches "the view is technically fine but no longer shows what it was
put there to show."

> 🧠 **Specify the reference image at commissioning.** A screenshot of every camera's intended view,
> dated, stored with the as-built documentation. It costs an hour at handover, it is the baseline
> for every automated scene-change check, and it is the only objective answer to "has this camera
> moved?" three years later. Almost nobody does it, and everybody who has needed it has wished they
> had it.

## Acceptance testing

The design is not delivered until it is verified against the questions from
[lesson 09](09_camera_placement.md). Specify these tests, and attend them.

1. **Pixel density verification** — a person of known height at the design distance, at every
   identification camera, with the measured PPF recorded against the specified target.
2. **Night verification** — the same test after dark, with a **walking** subject
   ([lesson 03](03_sensors_and_low_light.md)). This is the test that gets skipped and the one that
   finds the real problems.
3. **Illumination measurement** — lux at the named plane, against the specification.
4. **Continuity walk** — the route from car park to secure area, confirming no gaps
   ([lesson 09](09_camera_placement.md)).
5. **Retention verification** — after 30+ days of operation, confirm the achieved retention per
   camera group ([lesson 07](07_storage_and_retention.md)).
6. **Failover test** — pull the power on a primary recorder; confirm behaviour and measure the gap
   ([lesson 08](08_vms_architecture.md)).
7. **Export test** — export a clip, open it on a machine without the VMS, verify timestamp and
   hash.
8. **Health alert test** — disconnect a camera and confirm the alert reaches the named recipient.
9. **Analytics tuning period** — a defined window with a false-alarm rate acceptance threshold.
10. **Reference image capture** — every camera, dated, filed.

⚠️ **Tests 2, 5, 6, 8, and 10 are the ones omitted from most acceptance regimes**, and they are
where the failures live. Naming them explicitly in the specification is what makes them happen.

## Design tradeoffs

| Decision | Buys | Costs |
|---|---|---|
| Analytics for live alarms | Real-time detection | Precision collapses at low base rates; operator trust |
| Analytics for search | Massive investigation speed-up | Nothing operationally — **the best value in analytics** |
| Object classification | Large false-alarm reduction | Licensing; processing |
| Dedicated analytics cameras | Detection that works | Extra cameras, placed for the analytic not the view |
| Edge vs. server analytics | Edge: no server load. Server: heavier models | Edge is camera-dependent; server needs hardware |
| Scene-change monitoring | Catches misaiming and obstruction | Configuration; some false positives from legitimate change |
| Quarterly manual verification | Catches what automation cannot | ~20 hours/year at 60 cameras |
| Reference images at handover | Objective baseline forever | One hour at commissioning |

## Common mistakes

⚠️ **Deploying live analytics without computing the precision.** Do the base-rate arithmetic first.

⚠️ **Believing a 90% false-alarm reduction fixes an ignored alarm system.** It does not; see the
table.

⚠️ **Bolting analytics onto cameras placed for viewing.** Analytics want different geometry.

⚠️ **Not budgeting tuning time.** Analytics are commissioned over weeks.

⚠️ **Buying "suspicious behaviour" detection.** No stable definition exists.

⚠️ **Monitoring only online/offline.** Misses every failure that matters.

⚠️ **Alerts to an unmonitored address.** The most common single finding in any survey.

⚠️ **No reference images.** No objective way to prove a camera moved.

⚠️ **Skipping night acceptance testing.** The system is accepted under the conditions it works
best in.

## Junior vs. Senior

| | Junior | Senior |
|---|---|---|
| Evaluates an analytic by | The demo | The base rate, the precision arithmetic, and a site trial |
| Deploys analytics as | Live alarms | Search and filtering first; alarms only where the base rate supports it |
| Reduces false alarms by | Asking for a better algorithm | Fixing the geometry, adding classification, and tuning over weeks |
| Specifies health monitoring as | Online/offline | Scene change, focus, retention achieved, time sync, and a named recipient |
| Handles acceptance by | Signing the installer's sheet | Attending, at night, with a walking subject and a light meter |
| Treats a green dashboard as | Proof the system works | Proof that cameras are streaming, which is not the same claim |
| Leaves behind | A commissioned system | A commissioned system, reference images, and a verification schedule someone owns |

## 🔧 Field exercise

1. On a live system, pick ten cameras at random and compare the current view against what it should
   be showing. Note anything misaimed, obstructed, soft, or dirty. Record the fraction.
2. Find out what health monitoring exists and who receives the alerts. Contact that person and ask
   when they last acted on one.
3. If analytics are running, count alarms over 24 hours and estimate how many were real. Compute
   the precision.
4. Ask an operator what they do when an analytic alarm fires. Compare with the written procedure.
5. Ask whether reference images exist from commissioning.

## Exercises

Work these before opening
[`_solutions/11_analytics_and_health_solutions.md`](_solutions/11_analytics_and_health_solutions.md).

**E11.1** A client proposes line-crossing analytics on 35 perimeter cameras for live alarm
response. The site has had 3 genuine intrusions in the last two years. The vendor claims 1 false
alarm per camera per day.
 (a) Compute alarms per year and the precision.
 (b) Compute how many false alarms an operator assesses per true event.
 (c) State what will happen operationally, and over what timescale.
 (d) Give the recommendation.

**E11.2** For each, state whether you would trust it on a real project, and what you would require
before relying on it:
 (a) Person vs. vehicle classification on a car park camera.
 (b) "Aggression detection" in a hospital waiting area.
 (c) People counting at a single entrance turnstile.
 (d) Object-left-behind in a busy airport concourse.
 (e) Licence plate recognition on the existing overview camera at a gate.

**E11.3** A 90-camera system has been in service three years. A survey finds 14 cameras
significantly misaimed or obstructed, and the client was unaware.
 (a) What does this imply about the health monitoring in place?
 (b) Design the monitoring regime that would have caught them, distinguishing automated from
     manual.
 (c) Compute the annual manual verification cost at 5 minutes per camera per quarter.
 (d) Write the finding for the report.

**E11.4** Write the acceptance test specification for the Meridian vestibule camera C1 from
[lesson 09](09_camera_placement.md). Include what is measured, under what conditions, by whom, and
what constitutes a pass.

**E11.5** 🧠 A client wants to replace their two overnight security officers with analytics-driven
monitoring, arguing that the analytics will alert a remote monitoring centre. The site is a
distribution centre with a 1,800 ft perimeter and 4 genuine incidents per year.
 (a) Compute what the analytics would have to achieve for this to be viable.
 (b) Name the functions the officers perform that analytics do not.
 (c) Give your recommendation, engaging honestly with the cost argument.

## Retrieval check

1. What distinguishes analytics that work from analytics that do not?
2. Define precision, and state it for 20 cameras at 3 false alarms/camera/day with 2 true
   events/year.
3. Does a 99% false-alarm reduction fix that system? What is the resulting precision?
4. What is the highest-value application of analytics, and why does precision not matter there?
5. Name four camera failures that do not show up as offline.
6. What is the single most valuable non-standard health check?
7. Which five acceptance tests are most often omitted?
8. What should be captured at commissioning and filed forever?

## References

- [`09_camera_placement.md`](09_camera_placement.md) — analytics placement must be decided during
  the placement process.
- [`07_storage_and_retention.md`](07_storage_and_retention.md) — retention verification and time
  sync, both health-monitored here.
- [`../01_Foundations/07_systems_and_failure_thinking.md`](../01_Foundations/07_systems_and_failure_thinking.md)
  — silent failure and the failure categories this lesson is an instance of.
- [`../18_Commissioning/`](../18_Commissioning/) — acceptance testing in depth *(not yet written)*.
- [`../19_Operations/`](../19_Operations/) — the operational regime that keeps a system true
  *(not yet written)*.
- [`../36_Human_Factors_Privacy_Ethics/`](../36_Human_Factors_Privacy_Ethics/) — alarm fatigue,
  operator vigilance, and the legal and ethical load of face recognition *(not yet written)*.
- `[PRACTICE]` The analytics reliability ordering is engineering judgment as of writing and will
  move. The false-alarm rates are illustrative; measure them on your own site.
- `[VERIFY]` Face recognition is subject to specific and rapidly changing legal restriction in many
  jurisdictions, and carries documented accuracy disparities across demographic groups. Treat any
  deployment as a legal and ethical question first and an engineering question second.

---

**Next:** [the park-and-ride garage capstone](_exercises/garage_design.md) — the whole module on
one site, and a design whose correct answer contradicts what lessons 04 and 09 will have trained
you to reach for.
