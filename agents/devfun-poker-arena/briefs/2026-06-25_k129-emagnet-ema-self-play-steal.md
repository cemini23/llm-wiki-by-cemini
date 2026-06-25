## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox.

## Summary

Steal **EMAgnet** parameter-space EMA magnet (arXiv 2606.23995): regularize self-play toward an **EMA of policy parameters** instead of uniform entropy — reduces exploitability in games with dominated strategies. Offline chart analogue to K127 GARIP running-average mixture anchor.

## Body

### Scope / regime disclosure

| Dimension | EMAgnet paper | Cemini target |
|-----------|---------------|---------------|
| Game | Tabular / industrial IIG (Riot) | **HU NLHE** discrete actions |
| Magnet | EMA of NN parameters | **Offline mixture/chart decay** inspired by EMA schedule |
| Training | Full PPO self-play | **No Arena-clock PPO** — chart refinement only |

### P0 — EMA decay on villain mixture anchor

1. Extend K127 `--garip-alpha` with optional **parameter-EMA decay** on chart cell weights (not full NN training).
2. Ablate vs uniform-entropy prior baseline on lag-archetype exploit spots.
3. Log `emagnet_tau`, `exploitability_proxy` to `deploys.jsonl`.

### Pairing

| Layer | Role |
|-------|------|
| K127 GARIP | Running-average mixture anchor |
| K124 MAFP | Stance fictitious play |
| K125 verifier | Trajectory risk at submit |
| K129 EMAgnet (this) | Adaptive magnet vs uniform entropy |

### Out of scope

- Riot-scale PPO training on Arena clock
- Claiming NLHE numbers from industrial IIG sims

## Sources

- [Source: arXiv:2606.23995 (retrieved 2026-06-25)]
- @wiki/concepts/emagnet-parameter-space-ema-self-play.md
- @wiki/sources/arxiv-emagnet-parameter-space-ema-2606.23995-2026-06-25.md
- @wiki/concepts/garip-running-average-self-play.md
