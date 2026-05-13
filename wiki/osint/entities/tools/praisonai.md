---
title: PraisonAI — Multi-agent orchestration with Doom-Loop Detection (Adopt-tier, Cemini-financial primary)
type: entity
tags: [tool, orchestration, multi-agent, mit, adopt-tier, cemini-financial, doom-loop-detection, shadow-git-checkpoints, mcp-native, langgraph-competitor]
keywords: [praisonai, doom loop detection, shadow git checkpoints, multi-agent orchestration, mcp protocol, langgraph alternative, autonomous trading safety]
related:
  - sources/tool-evaluation-wiki-fit-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/conductor-orchestrator.md
  - concepts/agent-trajectory-triage-signals.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/tool-evaluation-wiki-fit-2026-05-13.md` — origin source (Doc 3, K42), Adopt-tier
- `@concepts/tool-evaluation-framework.md` — methodology
- `@concepts/conductor-orchestrator.md` — **direct competitor / replacement candidate for LangGraph in Cemini Conductor stack**
- `@concepts/agent-trajectory-triage-signals.md` — Doom-Loop Detection is functionally adjacent to post-hoc trajectory triage

## Raw Concept

- **URL**: `https://github.com/MervinPraison/PraisonAI`
- **License**: MIT
- **Stars**: 7.5k / 66 open issues / 3,715 commits
- **Stack**: Python (87.1%), TypeScript, Rust, SQLite/PostgreSQL/Neo4j
- **Tier**: Adopt
- **Primary fit**: Cemini financial

## Narrative

The most credible Cemini-financial Adopt candidate of all K42 docs. Key safety primitives:

- **Doom Loop Detection** — auto-recover from recursive logic traps. Directly addresses autonomous trading buy/sell-loop risk.
- **Shadow Git Checkpoints** — filesystem rollback on execution failures. Direct utility for sandboxed Polymarket/Kalshi adapter execution.
- **MCP Protocol** native (stdio + HTTP transports)
- **PostgreSQL** support aligns with existing Cemini DB schema

### Phase-0 audit — REQUIRED before adoption

LangGraph already wires Conductor's 4-stage pipeline. Replacing or supplementing requires:

1. License verification (LICENSE file → confirm MIT)
2. Migration cost from current LangGraph adapters
3. Performance latency vs Polymarket/Kalshi adapter SLAs
4. Compare Doom-Loop Detection vs existing reviewer-agent + trajectory-triage stack
5. Doom-Loop Detection failure modes (false-positive abort risk on live trades)
6. Multi-DB orchestration (SQLite/Postgres/Neo4j) — overkill for current Cemini scope?

### ROADMAP K42 follow-up

Item: **PraisonAI Phase-0 audit** — gates Adopt-tier acceptance.

[NEEDS VERIFICATION 2026-05-13]

[Source: Tool Evaluation and Wiki Fit.docx URL 9 (retrieved 2026-05-13)]
