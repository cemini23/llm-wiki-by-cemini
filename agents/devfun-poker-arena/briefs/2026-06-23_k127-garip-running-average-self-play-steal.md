## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox.

## Summary

Steal **GARIP** running-average magnet pattern (arXiv 2606.22688): anchor HU chart refinement to a **Polyak running-average villain mixture** instead of periodic snapshot (R-NaD) or fixed prior (MMD). Complements K124 MAFP + K125 trajectory verifier.

## Body

### Scope / regime disclosure

| Dimension | GARIP paper (2606.22688) | Cemini target |
|-----------|--------------------------|---------------|
| Game | Tabular / DeepRL 2p zero-sum | **HU NLHE** discrete actions |
| Magnet | Running-average policy | **Running-average villain mix** from selfplay logs |
| Opponent | Average opponent | Population bots + lag archetypes |
| Runtime | PPO self-play training | **Offline chart update** only |

Architecture is **regime-conditioned** — paper exploit-return table is tabular/DeepRL; do not claim NLHE numbers transfer.

### P0 — running-average mixture anchor

1. After each selfplay batch, update **empirical villain mixture** μ̄_t (Polyak: μ̄_t ← (1-α)μ̄_{t-1} + α μ_t).
2. Best-response chart cells vs μ̄_t (not latest snapshot μ_t) — compare Δexploitability vs K124 MAFP-only baseline.
3. Log `garip_alpha`, `mixture_l2_drift` to `deploys.jsonl`.

### P1 — ablation vs snapshot magnet

- Run parallel track with **R-NaD-style** snapshot every K=200 hands — expect higher peak-lag exploitability per paper mechanism.
- Target: lower worst-case bb/100 vs adaptive lag without rock matchup regression.

### Pairing

| Layer | Role |
|-------|------|
| K124 MAFP | Stance-agent fictitious play |
| K125 verifier | Trajectory risk bound at submit |
| K127 GARIP (this) | Reference-update schedule for mixture anchor |

### Out of scope

- Full PPO + KL magnet training on Arena clock
- MARSHAL-Kuhn HF model (NO LICENSE — K127 HF eval Reject)

## Sources

- [Source: arXiv:2606.22688 (retrieved 2026-06-23)]
- @wiki/concepts/garip-running-average-self-play.md
- @wiki/sources/arxiv-garip-self-play-2606.22688-2026-06-23.md
- @wiki/concepts/multi-agent-fictitious-play-llm.md
