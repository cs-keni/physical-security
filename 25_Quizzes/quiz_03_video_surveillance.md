# Quiz 03 — Video Surveillance

**Take this COLD, before reading Module 03.** You will do badly, especially on Parts B and C. That
is the design — failed retrieval primes learning far better than confident reading does. Then
retake it after the module and compare.

**Format:** 30 questions. 14 concept and judgment (1 pt), 8 scenario (2 pts), 8 calculation
(3 pts). **54 points total.**
**Time:** 80 minutes. **Target on retake:** ≥ 80% overall, and ≥ 90% on Part C.

**You may use a calculator. You may not use `psec`.**

Answers and full worked explanations:
[`_answer_keys/quiz_03_answers.md`](_answer_keys/quiz_03_answers.md).
**Write your answers down before you open it.**

> ⚠️ This module's hardest questions are not the calculations. Several questions below have a
> correct arithmetic answer **and** a correct engineering answer that contradicts it. The key
> scores you on both, and on noticing that they differ.

**Constants you may use:**

```
   Sensor 1/2.8"  =  5.37 mm × 3.02 mm      1/1.8"  =  7.20 mm × 5.40 mm
   DORI, pixels per foot:  detect 8   observe 19   recognise 38   identify 76
   DORI, pixels per metre: detect 25  observe 62.5 recognise 125  identify 250
   1 m = 3.28084 ft        Walking pace 3 mph = 4.4 ft/s
   Adult interpupillary distance ≈ 2.5 in     Depression angle practice limit ≈ 30°
   Circle of confusion (2 px on 1/2.8", 2688 px) = 0.00400 mm
   Hyperfocal  H = f²/(N·c) + f
   Near/far    D_n = s(H−f)/(H+s−2f)     D_f = s(H−f)/(H−s)
```

---

## Part A — Concept and judgment (1 pt each, 14 pts)

**A1.** Name the eight links of the imaging chain in order.

**A2.** Which link is most often the binding constraint, and which link do clients most often try
to buy their way out with?

**A3.** State one thing each of links [1], [3], and [5] can destroy that no downstream link can
restore.

**A4.** What exactly distinguishes **recognise** from **identify**? Why does the distinction matter
legally as well as technically?

**A5.** Light gathered scales as what function of the f-number? Depth of field collapses as roughly
what function of focal length?

**A6.** Does gain improve signal-to-noise ratio? What does it actually do?

**A7.** Give the two independent reasons one camera cannot capture both a number plate and a
driver's face at a vehicle entry.

**A8.** Why can a 2 MP camera on a windy car park consume more bandwidth than a 4 MP camera in a
corridor?

**A9.** What does CBR protect, and under what circumstance does it fail?

**A10.** Does motion-triggered recording reduce **peak** bandwidth? Explain.

**A11.** What does RAID protect against? Name three things it does not.

**A12.** State the governing rule of camera placement.

**A13.** Name four camera failure modes that do **not** appear as "offline" on a monitoring
dashboard.

**A14.** What distinguishes analytics that work reliably from analytics that do not?

---

## Part B — Scenario (2 pts each, 16 pts)

**B1.** A vestibule camera delivers 160 ppf at a 16° depression angle — over twice the identify
threshold at a good angle — and the 3 a.m. footage cannot identify anyone. Give the most likely
cause and the cheapest effective fix.

**B2.** A client proposes replacing 2 MP cameras with 8 MP cameras on the same 1/2.8" sensor to fix
poor night images. State what happens to light collected per photosite, and what the client's net
position becomes if they were already 2 stops short.

**B3.** A camera specification reads "80 ppf, meets identify." The camera is at 14 ft; the subject
is at 30 ft floor distance. Name two things wrong with the specification as written.

**B4.** A design uses a single 3 Mbps figure for all 60 cameras. Measured, the 40 interior cameras
average 2.2 Mbps and the 20 exterior average 9.8 Mbps. Retention was specified at 30 days. Explain
qualitatively why the array fills early, and why the error survived design review.

**B5.** A vendor states their VMS is "fully redundant." Give three questions that establish what
that actually means, and say what a weak answer to each would reveal.

**B6.** A retail store's exit camera is aimed outward at the car park. State the problem, the cost
of the fix, and why this is a design failure rather than an installation one.

**B7.** A survey finds 14 of 90 cameras significantly misaimed or obstructed, and the client was
unaware. What does this imply about the monitoring in place, and what single automated check would
have caught them?

**B8.** A client wants to replace two overnight security officers with analytics alerting a remote
monitoring centre. Name three functions the officers perform that analytics do not.

---

## Part C — Calculation (3 pts each, 24 pts)

Show your working. State any assumption you make.

**C1.** A 4 MP camera (2688 × 1520, 1/2.8" sensor, 4 mm lens) is mounted at 9 ft. A subject's face
plane is 5 ft above the floor, at 20 ft floor distance.
 (a) Compute the slant range.
 (b) Compute the scene width and the pixel density.
 (c) Which DORI class does it meet?

**C2.** For the same camera, compute the maximum distance at which it still meets **identify**.

**C3.** A person walks at 3 mph past a camera delivering 120 ppf. The camera's shutter is 1/30 s.
 (a) Compute the motion smear in inches and in pixels.
 (b) Compute the eye-to-eye distance in pixels.
 (c) State the ratio, and say what happens to that ratio if the camera is replaced with one of
     twice the resolution.

**C4.** A scene measures 4 lux. In that light the camera settles on 1/25 s at f/1.4. You require
1/125 s.
 (a) How many stops short are you?
 (b) What illuminance is required?
 (c) Name the only source of those stops that carries no image penalty.

**C5.** A 16 mm lens on a 1/2.8" sensor (c = 0.00400 mm) is focused at 45 ft, at f/2.0.
 (a) Compute the hyperfocal distance.
 (b) Compute the near limit of depth of field.
 (c) A doorway at 20 ft must be sharp. Is it? If not, state one fix and its cost.

**C6.** A 110 ft building elevation must be covered at **recognise** using 4 MP cameras
(2688 px horizontal). Allow 15% overlap.
 (a) How many cameras?
 (b) How many for **identify**?
 (c) An 8 MP option (3840 px) is offered for identify. Recompute, and comment.

**C7.** A 12 MP fisheye distributes about 4000 px around its circle.
 (a) At what radius does it drop below **recognise**?
 (b) What area does it cover at recognise or better?
 (c) A vendor claims it "covers a 50 ft × 50 ft open office." Assess the claim.

**C8.** A perimeter has 25 cameras running line-crossing analytics. The site experiences 2 genuine
intrusions per year. The analytic produces 2 false alarms per camera per day.
 (a) Compute alarms per year and the precision.
 (b) Compute false alarms per true event.
 (c) The vendor offers an upgrade reducing false alarms by 95%. Compute the new precision and
     state whether it changes your recommendation.

---

## Scoring

| Part | Questions | Points |
|---|---|---|
| A — Concept and judgment | 14 × 1 | 14 |
| B — Scenario | 8 × 2 | 16 |
| C — Calculation | 8 × 3 | 24 |
| **Total** | **30** | **54** |

| Score | Reading |
|---|---|
| < 27 (50%) | Re-read the module. Expected on a cold take |
| 27–37 | Working knowledge; revisit the parts you missed |
| 38–43 (70–80%) | Solid. Check whether your losses cluster in Part B — judgment is the harder half |
| ≥ 44 (80%) | Module competency. Attempt [the capstone](../03_Video_Surveillance/_exercises/garage_design.md) |

> 🧠 **If you scored well on Part C and badly on Part B, that is the most common and most important
> pattern.** The arithmetic in this module is the easy half and `psec` already does it. The
> judgment — which class, which link binds, what to tell the client — is what the module is for,
> and it is what the capstone tests.
