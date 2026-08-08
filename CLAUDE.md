# CLAUDE.md — Physical Security Engineering Academy

This is a **content repository**, not an application. Most work is authoring Markdown
lessons. The only code is `28_Calculators/psec/` and `16_Automation/data_model/`.

## Read before writing anything

1. `COURSE_PROGRESS.md` — build status. Read first when resuming.
2. `docs/AI_CONTEXT.md` — authoring standards, module template, voice.
3. `docs/HANDOFF.md` — architecture, conventions, verification commands.
4. `docs/CURRENT_TASK.md` — the active work item.

## Conventions that must not drift

- **No placeholder files.** A file exists only if it has real instructional content.
  Unwritten = empty directory + a `COURSE_PROGRESS.md` row.
- **Solutions isolated** in `_solutions/` and `_answer_keys/`. Never inline an answer.
- **Tags:** `[CODE]` `[STANDARD]` `[GUIDELINE]` `[PRACTICE]` `[MFR]` `[VERIFY]`.
  Tag every numeric code or standard claim `[VERIFY]`. Never invent a code requirement.
- **Calculators are stdlib-only** — they must run on a locked-down work laptop.
- **Tests encode the hand calculations.** If a test fails after a formula change, redo the
  hand calc; do not change the test.
- **The validator reports, never mutates.** Automate the repetitive work, never the
  engineering judgment.
- ASCII diagrams only.

## Verification (run before and after any code change)

```bash
python3 28_Calculators/tests/test_psec.py                       # 66 tests → OK
python3 28_Calculators/demo.py                                   # 8 worked examples
python3 16_Automation/data_model/validate.py \
        16_Automation/sample_data/devices_flawed.csv CD          # 25 errors (intentional)
```

## Workflow

Feature branch per work item (e.g. `module/35-doors-hardware`), then merge to `main`.
Update `COURSE_PROGRESS.md`, `PHASES.md`, and `docs/ENGINEERING_LOG.md` in the same commit
as the content they describe. Stage specific files; never `git add .`.

## Skill routing

When the user's request matches an available skill, invoke it via the Skill tool. When in doubt, invoke the skill.

Key routing rules:
- Product ideas/brainstorming → invoke /office-hours
- Strategy/scope → invoke /plan-ceo-review
- Architecture → invoke /plan-eng-review
- Design system/plan review → invoke /design-consultation or /plan-design-review
- Full review pipeline → invoke /autoplan
- Bugs/errors → invoke /investigate
- QA/testing site behavior → invoke /qa or /qa-only
- Code review/diff check → invoke /review
- Visual polish → invoke /design-review
- Ship/deploy/PR → invoke /ship or /land-and-deploy
- Save progress → invoke /context-save
- Resume context → invoke /context-restore
- Author a backlog-ready spec/issue → invoke /spec
