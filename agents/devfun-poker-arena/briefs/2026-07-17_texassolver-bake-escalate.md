---
title: Escalate — TexasSolver postflop bake v1
type: brief
target: Poker Arena
created: 2026-07-17
updated: 2026-07-17
---

## Target

Cursor `--build --replace` for S1 HU ladder after local gate green.

## Summary

Replaced `heuristic_bucket_v1` with **`texas_solver_v1`** frequencies from TexasSolver console (30 spots: 18 flop + 6 turn + 6 river). Stronger bias (±0.14) when provenance is solver. No gin flip. No runtime solver.

Proposed pin: `researcher-ladder-s1.texassolver-v1.2026-07-17`

Pre-replace Active: `bf7679bd` (~4.4k hands, μ≈−45, rank ~189/259) — **Discarded**.

Live Active: **`a7a677b7-a70e-432e-9cfe-b296bd7fae03`** (`pvp.continuous=true`, unlimited).

## What changed

| Item | Detail |
|------|--------|
| Bake | `examples/bake_texassolver_buckets.py` |
| Grid | `research/texassolver_spot_grid.json` |
| Buckets | `research/postflop_hu_buckets.json` — `meta.generator=texas_solver_v1`, 90 keys, 30/30 spots |
| Bias | `postflop_buckets.bias_thresholds_from_freqs` — solver scale ±0.14 / ~1.5× |
| Solver | `.local/texassolver/.../console_solver` (not bundled; AGPL) |
| Tree | Street-scoped bet sizes only (full 3-street trees hung on laptop) |
| Dump path | `/tmp/cemini-texassolver-dumps` (space-free — path with spaces hangs TexasSolver) |

## Gate (2026-07-17)

```
GATE PASS
TEN advisory: +17.5 bb/100
maniac_shark advisory: −25.2 bb/100 (advisory)
rock +17.7 / maniac −17.4 / lag +43.1
series_win_rate maniac 60% / lag 60%
trajectory gates: PASS
```

Critical tests: `tests/test_postflop_buckets.py` + mafp/wire/scan — **33 passed**. Full `pytest tests/` hung mid-suite (pre-existing flaky hang; not introduced as gate blocker).

## Live success metric

TrueSkill **μ** lift over ≥3k hands vs pre-replace Active — not peak adj bb/100.

## Ops

```bash
bash scripts/rsync_poker_arena_code.sh
# on prod:
cd /opt/devfun-poker-arena && . venv/bin/activate
uv run python examples/submit_sandbox_pvp.py --build --replace \
  --pin researcher-ladder-s1.texassolver-v1.2026-07-17
python3 scripts/poll_ladder_rank.py
```

## Notes

- Grok started implement; hung on first full-tree solve (spaces in path + 3-street tree). Cursor finished bake + gate.
- Phase 2 (opponent-conditioned modes) still next if μ plateaus.

## Sources

- Internal Arena ops / prior escalate briefs in this directory.
