# Quiz 32 — Engineering Math

**Take this COLD, before reading Module 32.** You will do badly, especially on Part C. That is
the design — failed retrieval primes learning far better than confident reading does. Then retake
it after the module and compare.

**Format:** 30 questions. 16 derivation and concept (1 pt), 6 scenario (2 pts), 8 calculation
(3 pts). **52 points total.**
**Time:** 75 minutes. **Target on retake:** ≥ 80% overall, and ≥ 90% on Part C.

**You may use a calculator. You may not use `psec`.** The whole point of this module is that you
can do it without the code; using the code here tests nothing.

Answers and full worked explanations:
[`_answer_keys/quiz_32_answers.md`](_answer_keys/quiz_32_answers.md).
**Write your answers down before you open it.**

> ⚠️ Several questions touch code-driven or standards-driven values. The correct answer to any of
> them is never a number recalled from memory — it is the reasoning plus a statement of what you
> would look up and where. The answer key scores you on that.

**Constants you may use** (they are given so the quiz tests understanding, not recall):

```
   Sensor 1/2.8"  =  5.37 mm × 3.02 mm
   K, copper at 75 °C  =  12.9 Ω·cmil/ft
   Circular mils:  22 AWG 640.4    20 AWG 1020    18 AWG 1624    16 AWG 2583    14 AWG 4107
   DORI, pixels per foot:  detect 8   observe 19   recognise 38   identify 76
   Frame-rate scaling exponent = 0.7      H.265 factor = 0.5
   Battery derate 1.25       Aging factor 1.25       Usable fraction 0.8
```

---

## Part A — Derivations and concepts (1 pt each)

**1.** Write the angle-of-view formula and say what geometric model it comes from.

**2.** Write the field-of-view width formula. Explain why an equation that divides millimetres by
millimetres and multiplies by feet is dimensionally sound.

**3.** State the inverse form of the FOV equation — lens from required coverage — and say why that
is the direction a designer actually uses.

**4.** Define slant range. Name the class of camera for which ignoring it overstates coverage the
most, and say why.

**5.** Write the pixel density formula both ways: from FOV width, and in the combined form that
skips it.

**6.** Pixel density falls as `1/D`, not `1/D²`. State what does fall as `1/D²`, and why confusing
the two leads to a specific bad design decision.

**7.** `D_max ∝ px · f`. State in one sentence what resolution and focal length trade against each
other, and what they explicitly do **not** trade against.

**8.** DORI is defined in pixels per metre. Why is the per-foot table in `psec` deliberately not
the exact metric conversion?

**9.** Rank the legitimate sources of a bitrate figure, best first.

**10.** Frame-rate scaling in this module is sub-linear. Give the two physical reasons, and say
why a documented modelling choice beats an undocumented one.

**11.** Storage is sized on average bandwidth but network links are sized on peak. Explain the
asymmetry.

**12.** A motion duty cycle below 1.0 is described in the module as "a risk to be named rather
than a saving to be booked." Explain.

**13.** State the difference between PSE power and PD power, and say which one you budget a switch
against.

**14.** Name the four independent ways a PoE switch design fails.

**15.** Derive `Vd = 2·K·I·L / CM` from Ohm's law in three steps. Explain the factor of 2 and say
what a circular mil is.

**16.** Peak current governs one thing and standby current governs another. Name both and give the
physical reason they differ.

---

## Part B — Scenario (2 pts each)

**17.** A vendor's online calculator says a 4 MP camera needs 4.2 TB for 30 days. Yours says
7.9 TB. Neither of you has made an arithmetic error. Explain how both can be right, and state
what you put in the proposal.

**18.** A client shows you a switch summary: 24 ports, 8 used, 16 free, and asks how many more
cameras they can add. What do you need to know before answering, and what is the shape of the
answer you give them?

**19.** An access-controlled door releases reliably every morning and intermittently by mid
afternoon. Integration has been called twice and found nothing. State your first hypothesis, the
two measurements you would take, and the reason the fault is time-of-day dependent.

**20.** You size a battery to exactly meet a 4-hour standby requirement using the raw amp-hour
figure with no derating. State the two things that will be true in eighteen months, and which of
the two standard factors addresses each.

**21.** A path analysis returns "NOT TIMELY, short by 300 s," and a colleague proposes adding a
600 s barrier at the site perimeter. Explain why this may buy nothing at all, and state the
condition under which it would work.

**22.** A calculation returns a required detection point of **−240 s**. Interpret that number.
State what a well-built calculator should return instead, and why.

---

## Part C — Calculation (3 pts each)

Show your working. An answer with no units scores zero.

**23.** A camera with a 1/2.8" sensor and a **6 mm** lens views a target plane **40 ft** away.
Compute the horizontal angle of view, the scene width, and the pixel density for a 2688-pixel
horizontal count. Which DORI class does it meet?

**24.** You need a **30 ft** wide scene at **75 ft** on the same sensor. Compute the focal length
required. The stocked lens sizes are 9, 12, and 16 mm. Which do you specify, and why that
direction?

**25.** A 2688-pixel camera with a **4 mm** lens on a 1/2.8" sensor. Compute the maximum range at
which it still meets **recognise**. Then state what happens to that range if you switch to an
8 MP camera (3840 px) on the same lens and sensor.

**26.** A stream runs at **6.0 Mbps**, recording **18 hours per day**, retained **45 days**.
Compute GB/day and total TB. Then compute the same day figure in **GiB**, and state the percentage
gap between the two and where it comes from.

**27.** A 24-port switch with a **240 W** PoE budget is loaded with **12 cameras**, all classifying
as **802.3at**. Compute ports used, power used, and utilisation. List every finding. State which
constraint binds.

**28.** A 12 VDC device draws **0.25 A** over a **175 ft** run of **22 AWG**. Its minimum operating
voltage is **10.5 V**. Compute the drop, the voltage at the device, and the drop as a percentage.
Does it pass? If not, compute the maximum length 22 AWG would allow, and name the smallest
conductor that works at 175 ft.

**29.** A panel draws **0.8 A** standby and **2.5 A** in alarm. Required standby is **6 hours**
with a **10-minute** alarm. Compute the raw amp-hours, the sized amp-hours using both standard
factors, and the recommended supply current at 25% headroom. Then state which figure you would
have got wrong if you had used the alarm current for the battery.

**30.** An adversary path has three tasks of **200 s**, **180 s**, and **220 s**. Detection occurs
at the **completion of the first task**. Assessment delay is **45 s**. Response time is **400 s**
and the required confidence margin is **60 s**.

Compute `T_T`, `T_D`, and `T_A`. State the verdict and the shortfall. Then compute the required
detection point and say what it means for where detection has to go.

---

## Scoring

| Range | Reading |
|---|---|
| 47–52 | You can derive this module. Go do the capstone. |
| 39–46 | Solid. Re-read the lessons behind whichever Part C question you lost points on. |
| 26–38 | The concepts are there and the arithmetic is not. Work every problem set. |
| < 26 | Expected on a cold take. Read the module. |

**Score Part C separately.** A high Part A score with a low Part C score means you have read the
module rather than done it, which is the failure mode this module exists to prevent.

---

Next: the [integrated sizing capstone](../32_Engineering_Math/_exercises/integrated_sizing.md) —
one site, all eight lessons, and a design that fails four times before it works.
