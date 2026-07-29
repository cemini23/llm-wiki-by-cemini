---
title: Escalate — opponent modes + deeper TexasSolver bake
type: brief
target: Poker Arena
created: 2026-07-19
updated: 2026-07-19
---

## Target

Cursor owns **`--replace`** after local gate green. Grok implementer: **no** `--replace`, no Arena poll-submit.

## Summary

Policy delta for S1 HU ladder (close μ gap vs Active `a7a677b7` ≈ −38):

1. **Opponent-conditioned best-response modes** (`nit` / `lag` / `wide_passive` / `balanced`) from K156 risk-spectrum tags.
2. **Deeper TexasSolver bake** — 44 spots, `texas_solver_v1`, stronger bias (±0.16 / free 0.18 / facing ~1.2×).

Proposed pin: **`researcher-ladder-s1.opp-modes-bake-v2.2026-07-19`**

Pre-replace Active: **`a7a677b7`** (~13.7k hands, μ≈−38, rank ~178/261).


## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## What changed

| Item | Detail |
|------|--------|
| Modes | `examples/opponent_modes.py` + `tests/test_opponent_modes.py` + `references/opponent-modes.md` |
| Wire | `cemini_decide.py` after HUD enrich; apply only when private HUD mode is `unknown`/`balanced` (no double-stack on rock/maniac/tight) |
| Flag | `CEMINI_OPPONENT_MODES=1` harness `setdefault` |
| Spectrum docs | `references/risk-spectrum-tags.md` — BR modes OK, still not “copy GPT VPIP” |
| Grid | `research/texassolver_spot_grid.json` — **44** spots (was 30 solved) |
| Bake | `research/postflop_hu_buckets.json` — `generator=texas_solver_v1`, **spots_solved=44**, 90 keys |
| Bias | `postflop_buckets.bias_scale_params` — clamp **±0.16**, free_mult **0.18**, facing 0.216/0.18/0.27 |
| Dump path | `/tmp/cemini-texassolver-dumps` (space-free) |
| Gate script | `PYTHONHASHSEED=0` default; audit enables `CEMINI_OPPONENT_MODES=1` (cemini_decide path has no harness setdefault) |

## Gate (2026-07-19) — verbatim summary

Bundle: `reports/researcher-round/gate-hu-20260719T124845Z`

```
GATE PASS
tight selfplay: +42.0 bb/100
TEN advisory: +4.8 bb/100
maniac_shark advisory: −2.0 bb/100 (advisory)
rock +17.7 / maniac +57.6 / lag +34.0
series_win_rate rock 60% / maniac 60% / lag 60%
VPIP 43.9% (advisory >42%) / VPIP−PFR 7.1%
trajectory gates: PASS
RESEARCHER SANDBOX GATE OK
```

Critical tests: `tests/test_opponent_modes.py` + `tests/test_postflop_buckets.py` — **23 passed**.

Build-only: `dist/sandbox-pvp-bundle.zip` written (no submit).

Bake assert: `generator=texas_solver_v1`, `spots_solved=44`, `buckets=90`.

## Live success metric

TrueSkill **μ** better than **−38** over ≥3k hands on new Active (primary). Rank exit from bottom third is stretch.

## Ops (Cursor)

```bash
bash scripts/rsync_poker_arena_code.sh
# on prod:
cd /opt/devfun-poker-arena && . venv/bin/activate
uv run python examples/submit_sandbox_pvp.py --build --replace \
  --pin researcher-ladder-s1.opp-modes-bake-v2.2026-07-19 \
  --competition-id cmr3n8tft01nilecm1u5jlny7
python3 scripts/poll_ladder_rank.py
```

## Hard DO-NOTS held (Grok)

- No `--replace` / Arena poll-submit
- No `CEMINI_SANDBOX_ENGINE` change / no gin
- No runtime solver in `decide()`
- No dump paths with spaces
- Unpiped pytest only

## Notes

- Training HUD maps `TRAINING_OPPONENT_MODE=lag` → rock fallback in private exploit (pre-existing); modes skip when private mode is set so audit does not double-count.
- Lag `series_win_rate` (5×80h) is noisy without `PYTHONHASHSEED`; gate script now defaults it to `0`.
- K174 no-fit brief ignored for ship.

## Sources

- `briefs/2026-07-19_opponent-modes-deeper-bake-master-plan.md`
- Live baseline: Active `a7a677b7` μ≈−38 @~13.7k

## Live replace (Cursor)

- New Active: `8d66b6e0-3183-45fb-a988-dc6f8aefa302` (continuous)
- Prior `a7a677b7` Discarded @13668 hands
