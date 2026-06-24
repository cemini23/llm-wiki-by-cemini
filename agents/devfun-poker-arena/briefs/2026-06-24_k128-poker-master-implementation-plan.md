# K128 poker master implementation plan (2026-06-24)

## Target

`agents/devfun-poker-arena/` — execute remaining K122–K127 brief items; K128 daily ingest had **no poker brief** (PM LVR/SRL + game-dev BBMOD only).

## Summary

Opus planning pass + parallel execution (Kimi/GPT workers). Stack was **already shipped** for P0 steals; this session closed P1/P2 gaps and hyper-maniac margin bug.

## K128 daily digest — poker candidates (not ingested)

| Paper | Verdict |
|-------|---------|
| EMAgnet 2606.23995 | Fold into GARIP `--garip-alpha-decay` (mixture-space EMA); no HF training |
| IRumAI 2606.21975 | Out of scope — full RL training |
| GARIP/MAFP | Already in wiki from K127/K124 |

## Done (this session)

| Item | Files |
|------|-------|
| K125 P2 Memory-Gap tagging | `cemini_decide.get_trajectory_bound_telemetry`, `selfplay` trajectory fields, `researcher_trajectory_summary.compute_memory_gap` |
| K123 P1 Best-of-N verifier | `CEMINI_VERIFIER_BON=1` default on (researcher + trajectory-bound path) |
| Hyper-maniac margin fix | `cemini_decide` — call-down vs +fold margins that crushed maniac series |
| GARIP EMA decay (EMAgnet micro-spike) | `garip_mixture.decayed_alpha`, `--garip-alpha-decay` CLI |

## Already shipped (pre-session)

K122 axes + gates, K124 MAFP, K125 trajectory bound live veto, K126 Kuhn reference, K127 GARIP chart refinement.

## Operator next (not code)

1. `bash scripts/run_hu_sandbox_gate.sh --hands 500` — confirm maniac series ≥38% advisory
2. Sandbox submit when window open: `uv run python examples/submit_sandbox_pvp.py --replace`
3. Optional: `garip_chart_refinement.py --write --garip-alpha-decay 0.85`

## Sources

- Opus master plan 2026-06-24
- `@wiki/sweeps/2026-06-24-daily.md`
- Briefs K122–K127 in `agents/devfun-poker-arena/briefs/`
