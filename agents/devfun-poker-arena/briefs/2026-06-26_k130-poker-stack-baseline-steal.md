## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox.

## Summary

K130 poker-repo eval confirms **PokerKit** as canonical Arena engine (already deployed) and adds **RLCard** for offline HU baseline ablations. Steal **PokerHandEvaluator** (Apache-2.0) if treys hot path becomes a profiling bottleneck.

## Body

### P0 — stack confirmation (no new deps in Arena)

| Repo | Tier | Action |
|------|------|--------|
| uoftcprg/pokerkit | Adopt | **No change** — verify pin + selfplay adapter parity each season |
| datamllab/rlcard | Adopt | **Isolated venv** only — offline chart / population bot experiments |
| dickreuter/*, pokerth | Reject | GPL/AGPL — never vendor |

### P1 — RLCard offline ablation track

1. Use `scripts/gambling_research_venv.sh` pattern (or arena-local `.venv-rlcard`) — **not** `pyproject.toml` core deps.
2. Run Leduc / limit-HU baseline to compare chart cell stability vs treys MC paths (log only — no Arena submit claims).

### P2 — PokerHandEvaluator steal (optional)

- If `pokerkit` + treys profiling shows hand-rank eval >5% of `decide()` latency, spike Apache-2.0 **PokerHandEvaluator** bindings.
- **Out of scope:** pokersolver (JS), PokerGPT (LLM runtime — Level 5 only with user GO).

### Cross-wiki

- RLCard domain depth → gambling-wiki (`briefs/2026-06-26_k130-rlcard-offline-baseline-adopt.md`)

## Sources

- @wiki/sources/eval-poker-github-repos-2026-06-26.md
- @wiki/entities/tools/pokerkit.md
- @wiki/entities/tools/rlcard.md
- [Source: Poker GitHub Repository Evaluation.docx (retrieved 2026-06-26)]
