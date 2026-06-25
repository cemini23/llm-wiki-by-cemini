## Target

`agents/devfun-poker-arena/` — K129 poker research implementation (EMAgnet + IRumAI steals).

## Summary

Shipped P0 from `2026-06-25_k129-emagnet-ema-self-play-steal.md` and `2026-06-25_k129-irumai-imperfect-info-card-steal.md`: uniform-entropy GARIP ablation with `exploitability_proxy` / `emagnet_tau` deploy logging, plus offline HU linear range probe harness with showdown villain labels from selfplay.

## Body

### Track A — EMAgnet / GARIP (done)

| Item | Location |
|------|----------|
| Uniform-entropy mixture baseline | `examples/garip_mixture.py` — `uniform_stance_mixture()` |
| Exploitability proxy | `exploitability_proxy(garip_ΔEV, uniform_ΔEV)` |
| Per-round logging | `examples/garip_chart_refinement.py` — `deploys.jsonl` notes: `emagnet_tau`, `uniform_delta_ev`, `exploitability_proxy` |
| Tests | `tests/test_garip_mixture.py` |

### Track B — IRumAI probe (done)

| Item | Location |
|------|----------|
| Showdown villain labels in trajectory | `examples/selfplay.py` — `hand_result.villain_hole_key`, `board_key` (HU) |
| Linear probe harness | `examples/irumai_range_probe.py` — 500-hand default, rank-AUC vs position baseline |
| Tests | `tests/test_k129_probe.py` |

### STRATEGY.md gate

No root `STRATEGY.md` in repo. Probe runner sets `beats_baseline` when probe AUC > baseline + 0.02. Only add STRATEGY.md notes after a green probe on `cemini_decide` at 500 hands.

### Follow-ups

1. `uv run python examples/irumai_range_probe.py --decide examples/cemini_decide.py --hands 500`
2. GARIP lag-archetype ablation with `--garip-alpha-decay` on exploit spots (MAFP audit export)
3. Prod rsync + `AGENT_VERSION` bump when validated
4. Sandbox submit when comp window open (`submit_sandbox_pvp.py --replace`)

### Out of scope (K129)

- PPO / NN training, Indian Rummy bot, runtime search expansion

## Sources

- @briefs/2026-06-25_k129-emagnet-ema-self-play-steal.md
- @briefs/2026-06-25_k129-irumai-imperfect-info-card-steal.md
