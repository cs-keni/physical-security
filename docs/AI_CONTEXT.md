# AI_CONTEXT — Authoring standards for this repository

Read before generating any content here.

## What this repository is

A self-study curriculum for an entry-level Physical Security Engineer (CS background, strong
software skills, beginner physical-security knowledge) targeting independent facility design
capability within 12 months, with ASIS APP → PSP as a secondary track.

**It is content, not an application.** The "code" is the calculator package and the automation
tooling; everything else is instructional Markdown.

## The 20-part module template

Every major topic must contain:

1. Learning objectives
2. ELI5 (for hard concepts) — **immediately followed by** the professional explanation
3. Beginner explanation
4. Detailed engineering explanation
5. Vocabulary
6. Diagrams (ASCII/Markdown; must render in a plain text editor)
7. Relevant calculations, worked with real numbers
8. Real-world examples
9. Design tradeoffs (table form)
10. Common mistakes (⚠️)
11. "What a junior engineer should know"
12. "What a senior engineer should know"
13. Field/design checklist
14. Practice exercises
15. Scenario questions
16. Quiz
17. Answer explanations — **in a separate `_solutions/` or `_answer_keys/` file**
18. Flashcards (CSV, Anki-importable)
19. Suggested authoritative references, tagged
20. Connection to APP/PSP domains

Not every lesson needs all 20; every *module* does.

## Conventions

| Convention | Rule |
|---|---|
| Tags | `[CODE]` `[STANDARD]` `[GUIDELINE]` `[PRACTICE]` `[MFR]` `[VERIFY]` — see `31_References/source_index.md` |
| Icons | 🧮 worked calculation · 🔧 hands-on lab · ⚠️ common mistake · 🧠 senior insight |
| Solutions | **Always** in `_solutions/` or `_answer_keys/` subfolders, never inline |
| Units | US customary primary (feet, AWG, °F) with metric where the standard is metric (mm lenses, IEC px/m). Always state units. |
| Cross-links | Relative Markdown links. Verify targets exist or are listed as pending in `COURSE_PROGRESS.md` |
| Tables | Preferred over prose for comparisons and tradeoffs |

## Hard rules

1. **Never invent a code requirement.** Teach the *shape* of requirements and how to find the
   current text. Tag every numeric code claim `[VERIFY]`. Do not reproduce copyrighted code or
   certification-book text.
2. **Never fabricate an API, a feature, or a product capability.** Bluebeam Scripting is
   Max-only and this user has Complete — build on documented exports instead.
3. **Defensive security only.** No bypass technique, no credential cloning procedure, no
   detection evasion. The correct depth is "this class of attack exists, here is the
   countermeasure."
4. **Synthetic data only.** Never real facilities, real IP schemes, real client information.
   Every case study is fictional and labelled as such.
5. **Life safety outranks security, always.** Any lesson touching egress must say so.
6. **No placeholder files.** A file exists only if it has real content. Empty directories plus
   a `COURSE_PROGRESS.md` row are how "not yet written" is represented.
7. **Code must be tested.** Standard library only. Expected values hand-computed. The test
   file is the record of the derivation.
8. **State uncertainty.** Where confidence is low, say so in-line and in the source index.
   Overselling reliability is worse than a gap.

## Voice

Write as a principal engineer teaching a capable junior who will be running projects in three
years. That means:

- **Concrete over general.** Real numbers, real failure modes, real conversations.
- **Explain the reasoning, not just the rule.** "Fail secure here" is a rule. "Fail secure
  here *because* free egress is provided mechanically by the lever, so the electric hardware
  never sits on the egress path" is teaching.
- **Say the uncomfortable thing.** That most camera systems document rather than prevent. That
  the client's proposed solution addresses the wrong risk. That the highest-value
  recommendation is outside your scope and reduces your fee.
- **No filler.** No "in today's fast-paced world." No restating the heading. If a paragraph
  doesn't carry information, delete it.
- **Respect the reader's background.** They know distributed systems, APIs, and databases. Use
  those bridges — and be explicit about where the analogy *breaks*, because that's where the
  costly mistakes live.

## Anti-patterns

- Generic prose that could apply to any topic
- Device lists presented as design
- Bullet points that restate the heading
- Certification-style rote content divorced from engineering reasoning
- Solutions visible in the same file as the exercise
- Confident numeric claims about codes
- Vendor-specific content presented as principle

## Verification loop

Before completing any work item:

```bash
python3 28_Calculators/tests/test_psec.py            # must be OK
python3 28_Calculators/demo.py                        # must run clean
python3 16_Automation/data_model/validate.py \
        16_Automation/sample_data/devices_flawed.csv CD
```

Then update `COURSE_PROGRESS.md`, `PHASES.md`, and `docs/ENGINEERING_LOG.md`.
