## Target

`agents/devfun-poker-arena/` — Researcher Round bundle harness + private regression suite.

## Summary

Steal **FaraGen1.5 tri-verifier** pattern (arXiv 2606.20785) for **`arena-tool` MCP** bundle eval: score trajectories on **correctness**, **efficiency**, and **critical-point adherence** — not function-call accuracy alone. Complements K131 ToolBench-X hazard taxonomy.

## Body

### Verifier mapping

| FaraGen verifier | Private harness check |
|------------------|----------------------|
| Task correctness | Action legal per `allowedActions`; session completes without forfeit |
| Efficiency | Act within per-decision budget; no idle poll loops burning match clock |
| Critical-point adherence | `reasoning_text` hand-specific; **join_pve before** reading harness/assets |

### P0 — regression suite addendum

1. Extend private bundle dry-run with **three scored dimensions** (pass/fail + log JSON).
2. Inject K131 hazards (timeout, bad amount, generic reasoning) under each verifier.
3. Read MIT `microsoft/fara` FaraGen docs for verifier composition — **do not** deploy CUA on consumer sites.

### Pairing

| Layer | Role |
|-------|------|
| K132 Fara (this) | Tri-verifier scoring template |
| K131 ToolBench-X | Hazard types + recovery paths |
| Sandbox guide wiki | Official `arena-tool` loop |
| Pure-code `decide()` | Policy unchanged |

### Out of scope

- Fara1.5-9B WebVoyager training for NLHE
- Browser CUA on DraftKings/FanDuel

## Sources

- [Source: arXiv:2606.20785 (retrieved 2026-06-27)]
- @wiki/sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md
- @wiki/sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md
- @wiki/sources/brief-k132-fara-agent-env-steals-2026-06-27.md
