## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-20_jul20-steals-grok-prompt.md).

# Grok task — Jul 20 poker brief steals (NO_REPLACE)

ROLE: Implementer. Cursor wrote the plan. You write ALL code/docs/tests + escalate brief.
You do **NOT** Arena `--replace`, submit, or discard-active. Cursor will also NOT replace this wave.

CWD: `/Users/claudiobarone/Projects/OSINT WORKSPACE/agents/devfun-poker-arena`

READ FIRST:
1. `briefs/2026-07-20_jul20-steals-master-plan.md` — full WPs
2. Triage briefs: `k191-k193-turn-rubric-steal.md`, `k195-rubric-capability-tree-steal.md`, `k143-memoryless-threshold-delta.md`, `k177-ar-bugs-controllability-light-steal.md`
3. Skip `k196-no-fit.md`
4. AGENTS.md Hard NEVERs

CONTEXT:
- DeepCFR-lite Active `760c44ad` just shipped — measuring μ. Do not interrupt.
- These steals are eval/docs/fixtures only — no decide() μ ship.

DO WP1–WP5 NOW. Write files before any long narration.

### WP1 — turn scores
- `examples/turn_street_scores.py`
- optional wire in `researcher_trajectory_summary.py` (`turn_street_scores` key)
- `references/turn-street-scores.md` + `references/expert-rubric-checklist.md`
- `tests/test_turn_street_scores.py`

### WP2 — K195 diagnosis
- `diagnose_rubric_failures` in `examples/capability_tree.py`
- thin config/docs update
- `tests/test_k195_rubric_capability_diagnosis.py`

### WP3 — K143
- `references/memoryless-threshold.md` (+ light test or config note)
- NO decide() changes

### WP4 — K177
- one AR-class claimed-auth fixture/test + `references/ar-bugs-controllability.md`

### WP5
- Run critical pytest (unpiped)
- Write `briefs/2026-07-20_jul20-steals-escalate.md` with gate numbers and explicit **NO_REPLACE**
- Do **not** change pin `agentVersion` off deepcfr-lite-v1

DONE WHEN these pass and escalate exists:
```
uv run pytest tests/test_turn_street_scores.py tests/test_k195_rubric_capability_diagnosis.py tests/test_k164_capability_tree.py tests/test_claimed_authorization.py tests/test_deepcfr_lite.py -q --tb=line
```

HARD FAIL if you exit with zero new files or if you run `--replace`.

## Summary

Operator brief: 2026-07-20 jul20-steals-grok-prompt. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-20_jul20-steals-grok-prompt.md).


## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
