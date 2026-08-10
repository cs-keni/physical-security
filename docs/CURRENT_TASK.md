# CURRENT_TASK

**Status:** Session 6 complete. No task in progress.

## Just completed (2026-08-09)

**`03_Video_Surveillance/` is written — 11 lessons, ~76k words, the largest module in the
academy.** Branch `module/03-video-surveillance`. Roadmap months 3 and 4 are unblocked, and
Projects 2 and 4 now have their prerequisite.

- **Overview + 11 lessons + `_solutions/` for every one**, written in the same commits as the
  lessons that link to them (the standing convention).
- **The Cedar Junction park-and-ride capstone** with a full reference solution — a site chosen to
  make three of the module's own instincts produce the wrong answer.
- **Quiz 03** (30 questions, 54 points) with an isolated key, and **114 flashcards**, CSV-validated.
- **Repo-wide link check clean** for module 03 (25 files). The only broken link left in the repo is
  still `30_Capstones/data_center_campus/` → `_reference_solution/`.

**The governing design decision:** module 32 derives the math; module 03 applies it and does not
re-derive any of it. The overview opens with a **division-of-labour table** stating exactly which
question is answered where. Every lesson needing a formula links to module 32 and states the
result. Without this the module would have duplicated roughly 40% of module 32.

**Every numeric value was produced by running `psec` and transcribed**, per the module 32
convention — `psec.optics` for geometry, `psec.video` for bandwidth and storage, `psec.pps` for the
capstone's timeliness analysis. Depth-of-field and exposure-budget arithmetic is shown in full
in-lesson because `psec` does not implement it.

## Results worth remembering

**Three calculations inverted the answer I expected while writing, and each became a teaching
point rather than being smoothed over:**

1. **The vestibule camera passes the pixel geometry at 2.11× the identify threshold and is still
   unusable at night.** A 1/30 s shutter smears a walking subject across 23.5 px against a 33.4 px
   eye-to-eye distance. Generalised in the solutions: the smear-to-detail ratio is **invariant
   under pixel density** (0.704 at both 12 ft and 22 ft), so resolution cannot fix blur — only a
   faster shutter (light) or a slower subject (a chokepoint) can.
2. **Camera count is a ceiling function.** An 8 MP upgrade needs the *same* count as 4 MP on a
   90 ft elevation, so the extra pixels are wasted while still costing 1.03 stops of light.
3. **A 99% false-alarm reduction still leaves 0.905% precision** at 2 true events/year. The base
   rate, not the detector, is the constraint.

**One correction made mid-module:** lesson 01's E1.1(c) answer attributed a soft face beside a
sharp plate to depth of field. Checking it with real numbers showed that holds only for **long**
lenses — at 12 mm both planes are in focus; at 50 mm the DOF is 2.2 ft. The condition is now stated
explicitly. **Compute before asserting, even when the claim is textbook.**

## Next task

**`04_Access_Control/` lessons 01–11.**

Now the highest-priority module. Module 35 lessons 03, 04, and 06 hand off to it directly —
offline controller behaviour, REX strategy, and reader-in/reader-out are raised there and resolved
here. Module 03 lesson 08 also forward-references it for PACS/video integration.

**Apply module 03's convention:** module 04 applies what module 35 derives about doors and
hardware. Open with a division-of-labour table and link rather than restate.

See `COURSE_PROGRESS.md` → "Next logical work item" for the full priority order.
