---
title: Escalate — Jul 21 brief steals (eval/docs; NO_REPLACE)
type: brief
target: Poker Arena
created: 2026-07-21
updated: 2026-07-21
---

## Target

Cursor implemented (Grok CLI unavailable until **2026-07-24**). Route lane would be hard→Grok; Cursor is the allowed fallback.


## Summary

Operator brief: Escalate — Jul 21 brief steals (eval/docs; NO_REPLACE). Cursor implemented (Grok CLI unavailable until **2026-07-24**). Route lane would be hard→Grok; Cursor is the allowed fallback.

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Replace recommendation: **NO_REPLACE**

Live Active **`e3574bb4`** (texassolver-v1-rollback) @ ~8.2k hands: **μ ≈ −37.6** — already beats the −38 success bar. Today's steals are eval/docs only.

**Do not** `--replace` / discard-active / Arena submit this wave.

## Pin (unchanged)

`researcher-ladder-s1.texassolver-v1-rollback.2026-07-20`

## Triage

| Brief | Action |
|-------|--------|
| K178, K198/K199 no-fit | skipped |
| K160 three-axis | shipped advisory |
| K199/K201 solver-grounded + prune | shipped advisory |
| K197 defender-utility | shipped advisory |
| K200 SWE-Pruner | WATCH docs only |

## What shipped

- `references/eval-three-axes.md` + `examples/eval_three_axes.py` + test
- `references/solver-grounded-numbers.md` + `examples/solver_context_prune.py` + test
- `references/defender-utility-eval.md` + `examples/eval_spot_utility.py` + test

## Gate

```bash
uv run pytest tests/test_eval_three_axes.py tests/test_solver_context_prune.py tests/test_eval_spot_utility.py -q --tb=line
```

## Live success metric (unchanged Active)

Keep measuring `e3574bb4`. Primary already met (μ better than −38 @ ≥3k). Rank ~204 is stretch / field-relative.

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
