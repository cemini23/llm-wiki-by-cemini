---
title: Escalate — DeepCFR-lite Phase 3
type: brief
target: Poker Arena
created: 2026-07-20
updated: 2026-07-20
---

## Target

Cursor owns **`--replace`** after local gate green. Grok lane no-op'd; Cursor implemented WP0–WP4.

## Summary

Phase-2 opponent modes + ±0.16 bias regressed μ (−38→−43). Ship **DeepCFR-lite** on 90 HU bucket infosets + unstack modes + Phase-1 bias.

Proposed pin: **`researcher-ladder-s1.deepcfr-lite-v1.2026-07-20`**

Pre-replace Active: **`8d66b6e0`** (~10.4k hands, μ≈−43, rank ~183/261).  
Success bar: beat prior good Active **`a7a677b7`** μ≈−38 over ≥3k hands.


## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## What changed

| Item | Detail |
|------|--------|
| Train | `examples/deepcfr_lite_train.py` — tabular regret-matching, 50k iters, seed 7 |
| Bake | `research/deepcfr_hu_buckets.json` — `generator=deepcfr_lite_v1`, 90 keys |
| Wire | `CEMINI_DEEPCFR=1` path resolve in `postflop_buckets.py`; harness setdefault |
| Unstack | `CEMINI_OPPONENT_MODES` setdefault removed; gate audit uses `=0` |
| Bias | texas_solver + deepcfr → clamp **0.14** / free **0.15** / facing 0.18·0.15·0.225 |
| Docs | `references/deepcfr-lite.md` |
| Tests | `tests/test_deepcfr_lite.py` |

## Gate (2026-07-20) — verbatim summary

Bundle: `reports/researcher-round/gate-hu-20260720T130317Z`

```
GATE PASS
tight selfplay: +42.0 bb/100
TEN advisory: +35.5 bb/100
maniac_shark advisory: +69.0 bb/100
rock +17.7 / maniac +59.2 / lag +37.0
series_win_rate rock 60% / maniac 80% / lag 60%
VPIP 46.2% (advisory >42%) / VPIP−PFR 7.4%
trajectory gates: PASS
RESEARCHER SANDBOX GATE OK
```

Critical tests: `test_deepcfr_lite` + `test_postflop_buckets` + `test_opponent_modes` — **28 passed**.

Build-only: `dist/sandbox-pvp-bundle.zip` (no submit until Cursor `--replace`).

## Live success metric

TrueSkill **μ** better than **−38** over ≥3k hands on new Active (primary). Stretch ≤ −30. Rollback if still ≤ −43 @ ≥3k.

## Ops (Cursor)

```bash
bash scripts/rsync_poker_arena_code.sh
# on prod:
cd /opt/devfun-poker-arena && . venv/bin/activate
uv run python examples/submit_sandbox_pvp.py --build --replace \
  --pin researcher-ladder-s1.deepcfr-lite-v1.2026-07-20 \
  --competition-id cmr3n8tft01nilecm1u5jlny7
python3 scripts/poll_ladder_rank.py
```

## Hard DO-NOTS held

- No gin flip / no torch in bundle / no runtime open_spiel
- texas_solver prior JSON retained
- No `--replace` until this escalate + gate green (now)

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
