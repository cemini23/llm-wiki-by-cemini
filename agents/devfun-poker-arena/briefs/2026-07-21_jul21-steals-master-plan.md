---
title: Master plan — Jul 21 brief steals (eval/docs; NO_REPLACE)
type: brief
target: Poker Arena
created: 2026-07-21
updated: 2026-07-21
---

## Target

`agents/devfun-poker-arena/` — **Cursor implements** (Grok CLI out until 2026-07-24). Route lane would be hard→Grok; fallback = this session.


## Summary

Operator brief: Master plan — Jul 21 brief steals (eval/docs; NO_REPLACE). `agents/devfun-poker-arena/` — **Cursor implements** (Grok CLI out until 2026-07-24). Route lane would be hard→Grok; fallback = this session.

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Live Active (pre-wave)

| | Value |
|--|-------|
| Active | `e3574bb4` texassolver-v1-rollback |
| hands | ~8.2k |
| μ | **≈ −37.6** (beats −38 success bar) |
| score | ≈ −57.6 |
| rank | ~204/264 |

## Triage

| Brief | Verdict |
|-------|---------|
| `k178-no-fit.md` | **SKIP** |
| `k198-k199-no-fit.md` | **SKIP** (biosecurity / smart-grid — no arena hook) |
| `k199-k201-solver-prune-steal.md` | **SHIP advisory** — solver-grounded numbers + tool-dump caps |
| `k200-context-prune-steal.md` | **WATCH / docs only** — no SWE-Pruner install (LICENSE) |
| `k197-defender-utility-eval-steal.md` | **SHIP advisory** — utility-ranked eval spots |
| `k160-wc2026-agents-eval-axes-steal.md` | **SHIP advisory** — three-axis HL eval (not runtime LLM) |

## Replace recommendation: **NO_REPLACE**

1. Rollback Active already **clears** the μ ≥ −38 bar @ ≥3k hands.
2. Today's steals are eval/docs — zero `decide()` TrueSkill delta.
3. Replacing would interrupt a recovering bot for methodology-only churn (Phase-2/DeepCFR lesson).

Cursor **must not** `--replace` this wave.

## Non-goals

- No gin / DeepCFR re-enable / opponent modes / runtime LLM reflection
- No SWE-Pruner Pro install
- No Grok CLI (unavailable until Jul 24)

---

## WP1 — K160 three-axis eval (HL / sandbox)

- `references/eval-three-axes.md` — calibration / decision quality / self-knowledge; hard non-LLM baseline required
- Optional: `examples/eval_three_axes.py` with `score_axes(report: dict) -> dict` advisory stub
- `tests/test_eval_three_axes.py`
- Do **not** add runtime LLM reflection into `decide()`

## WP2 — K199/K201 solver-grounded + dump prune

- `references/solver-grounded-numbers.md`
- `examples/solver_context_prune.py` — `prune_solver_context(ctx, *, max_keys=12, max_str=400)` caps verbose tool dumps; fail-open
- Wire optional use from `researcher_trajectory_summary` or HL brief path only (not hot-path decide unless already dumping)
- `tests/test_solver_context_prune.py`

## WP3 — K197 defender-utility ranking (eval)

- `references/defender-utility-eval.md` — rank spots by downstream utility, not raw fail rate
- Thin helper `rank_spots_by_utility(spots: list[dict]) -> list` in same module or `examples/eval_spot_utility.py`
- `tests/test_eval_spot_utility.py`

## WP4 — K200 WATCH

- One paragraph in `references/solver-grounded-numbers.md` or `references/context-prune-watch.md` — lab-only until LICENSE; measure decide quality not only tokens

## WP5 — Escalate NO_REPLACE

- `briefs/2026-07-21_jul21-steals-escalate.md`
- Pin unchanged: `researcher-ladder-s1.texassolver-v1-rollback.2026-07-20`
- Critical pytest green; no Arena submit

## Success criteria

- [ ] WP1–WP4 files + tests green
- [ ] Escalate says **NO_REPLACE**
- [ ] Active remains `e3574bb4`
- [ ] No `--replace` executed

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
