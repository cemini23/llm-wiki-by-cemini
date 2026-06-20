## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox (Jun 21 beta).

## Summary

Steal **MAFP** fictitious-play pattern (arXiv 2606.19308): offline multi-stance equilibrium refinement for preflop charts — treat villain archetypes as stance agents, iterate best-response before Arena submit. Complements K122 axis gates + K123 verifier stack.

## Body

### Scope / regime disclosure

| Dimension | MAFP paper (2606.19308) | Cemini target |
|-----------|-------------------------|---------------|
| Task | Open language policies (13 game/negotiation scenarios) | **HU/6-max NLHE** discrete actions |
| Stances | Negotiation/game stakeholders | rock / lag / maniac + hero seat |
| Runtime | Multi-round LLM MAS | **Offline only** — no Arena latency budget |
| Metrics | Tournament strength + robustness | Axis exploitability proxy + regression oracle |

Architecture is **regime-conditioned** steal — do not claim NUS benchmark numbers transfer to dev.fun LB.

### P0 — offline fictitious-play spike (pre Jun 21)

1. **Stance agents:** three villain profiles already in super-audit (rock/maniac/lag) + hero chart constraints.
2. **Aggregation operator:** empirical action-mix histogram per (position, stack bucket) from `selfplay` logs.
3. **Best-response operator:** adjust chart cell if EV vs mixture improves > threshold (MC equity sim, existing treys path).
4. **Stop:** 3–5 rounds or ΔEV < ε — log to `deploys.jsonl` as `mafp_round=N`.

### P1 — robustness check

- After fictitious-play convergence, run 150h selfplay vs **adaptive** lag (tracks hero frequency) — compare worst-case bb/100 vs pre-MAFP chart.
- Target: raise **robustness** floor without sacrificing rock matchup (MAFP paper's dual metric).

### Pairing with K122/K123

| Layer | Role |
|-------|------|
| K122 axes | M₇ mixing entropy floor post-MAFP |
| K123 verifier | Block illegal / M₈ hallucinated reasoning at submit |
| MAFP (this) | Reduce pre-submit exploitability in chart space |

### Out of scope

- Runtime multi-LLM MAFP on Arena action clock
- Team zero-sum solver install (2606.16139 is theory-only)

## Sources

- [Source: arXiv:2606.19308 (retrieved 2026-06-20)]
- @wiki/concepts/multi-agent-fictitious-play-llm.md
- @wiki/sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md
- @wiki/concepts/poker-arena-multi-axis-cognitive-profile.md
