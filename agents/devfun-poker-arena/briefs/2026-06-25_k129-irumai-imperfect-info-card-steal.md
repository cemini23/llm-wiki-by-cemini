## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox (imperfect-information card-game patterns).

## Summary

Steal **IRumAI** (arXiv 2606.21975) patterns for **hidden-hand inference** and **meld-validity constraints** — orthogonal to NLHE but transferable to opponent modeling and fast inference budgets. Cross-wiki: `@gambling-wiki` owns Indian Rummy domain.

## Body

### Transfers to HU NLHE

| IRumAI mechanism | Arena steal |
|------------------|-------------|
| Dual-branch conv + meld-aware encoding | **Public-card + action-history** tensor layout audit for `decide()` features |
| Deadwood-driven reward shaping | **Street-level EV proxy** in offline chart scoring (not runtime reward) |
| Linear probing → hidden-hand model | Hypothesis: public interactions encode villain range — test on sandbox replays |
| 0.33 ms/action vs search baseline | **Latency budget** for Level 1 heuristic path (no search at runtime) |

### P0 — replay probing harness

1. Export 500 sandbox hands → linear probe on action history vs revealed villain cards (if API exposes).
2. Compare feature layouts vs current `examples/agent.py` observation tensor.
3. Document in `STRATEGY.md` only if probe AUC > baseline.

### Cross-wiki

- Full rummy domain owned by gambling-wiki (`briefs/2026-06-24_k127-emagnet-irumai-selfplay-steals.md` — K127 federated brief; K129 adds OSINT wiki source pages)

### Out of scope

- Building an Indian Rummy bot in poker-arena repo
- Claiming 53.9% win rate transfers to NLHE

## Sources

- [Source: arXiv:2606.21975 (retrieved 2026-06-25)]
- @wiki/concepts/irumai-indian-rummy-rl.md
- @wiki/sources/arxiv-irumai-indian-rummy-ppo-2606.21975-2026-06-25.md
