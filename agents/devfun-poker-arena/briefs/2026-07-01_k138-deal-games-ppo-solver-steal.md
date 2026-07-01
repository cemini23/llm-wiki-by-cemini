## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox (solver literacy).

## Summary

Steal K138 **2606.29457** deal-auction benchmark: on enumerable imperfect-info games **exact CFR/MMD/PSRO beat PPO/PPG**; use PPO only post-enumeration with LBR lower-bound reporting — pairs with K136 Nash-solver provenance discipline.

## Body

### Scope / regime disclosure

| Dimension | Paper (29457) | Cemini target |
|-----------|---------------|---------------|
| Games | 2p0s takeover auctions (DealGame / OpenSpiel) | NLHE Arena — no tabular NE |
| Solvers | 9-way exact vs PG benchmark | Toy spikes + metadata only |
| Claim | PPO strongest **learning** solver, not overall | Provenance + exploitability floors |

### P0 — extend solver provenance (K136 carry-forward)

1. Any toy-game baseline JSON must include `solver_family=` and `exploitability=` when available.
2. Refuse to label PPO self-play output "GTO" without LBR or exact exploitability bound.

### P1 — optional OpenSpiel spike

1. Clone `zainnab-sparq/imperfect-information-deal-games` in sandbox only.
2. Reproduce one small auction — CFR vs PPO at equal wall-clock budget; log exploitability curves.
3. **Stop:** literacy — do not wire to `decide()`.

### Pairing

| Layer | Role |
|-------|------|
| K136 28308 | Nash-polytope member selection |
| K136 29169 | FP-PED hybrid |
| K138 29457 | Exact vs PG crossover + intractable LBR bounds |

## Sources

- [Source: arXiv:2606.29457 (retrieved 2026-07-01)]
- @wiki/concepts/takeover-auction-diligence-solvers.md
- @wiki/concepts/nash-equilibrium-solver-selection.md
