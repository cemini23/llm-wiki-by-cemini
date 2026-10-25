---
title: Interaction-native knowledge harness (InKH) — financial memory on Cemini
type: concept
tags: [concept, knowledge-harness, financial-agents, memory, governance, k99]
keywords: [2606.01886, inkh, temporal-graph, passive-injection, wiki-audit, stash, kb-server]
related:
  - sources/arxiv-interaction-native-knowledge-harness-2606.01886.md
  - concepts/librarian-server-architecture.md
  - concepts/kb-server-retrieval-scaling.md
  - concepts/agent-memory-critique.md
  - concepts/ems-execution-security-gaps.md
  - concepts/conductor-orchestrator.md
  - concepts/reviewer-passive-injection-corpus.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/cemini-knowledge-application-architecture.md
  - sources/agentmemory-rohitg00-cpr-impl.md
  - entities/tools/claude-mem.md
  - sources/llm-wiki.md
  - concepts/agent-memory-cross-scenario-generality.md
  - sources/arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05.md
maturity: draft
created: 2026-06-04
updated: 2026-07-08
---

## Relations

- `@sources/arxiv-interaction-native-knowledge-harness-2606.01886.md` — arXiv 2606.01886 (True Trading)
- `@concepts/librarian-server-architecture.md` — kb-server + stash deployment
- `@concepts/kb-server-retrieval-scaling.md` — brute-force RAG layer under graph complement
- `@concepts/agent-memory-critique.md` — lookup vs true memory; InKH claims consolidation + forgetting
- `@concepts/ems-execution-security-gaps.md` — action-risk gates before prod memory writes
- `@concepts/conductor-orchestrator.md` — passive injection vs agent tool-orchestrated retrieval
- `@concepts/reviewer-passive-injection-corpus.md` — K37 compiled reviewer bundle (manifest + build script)
- `@concepts/polymarket-copy-trading-strategy.md` — paper's primary workflow domain
- `@entities/tools/claude-mem.md` — laptop session observations vs persistent financial graph
- `@sources/agentmemory-rohitg00-cpr-impl.md` — RRF graph+vector pipeline contrast
- `@concepts/cemini-knowledge-application-architecture.md` — wiki→prod lesson registry vs passive injection
- `@ccc-wiki/concepts/interaction-native-knowledge-harness.md` — CCC harness/wiki-audit steal-from
- `@concepts/agent-memory-cross-scenario-generality.md` — InKH vs AutoMEM five-scenario eval (K100 handoff)
- `briefs/2026-06-04_inkh-financial-knowledge-harness-osint-handoff.md` — cross-wiki handoff provenance

## Raw Concept

Ingested 2026-06-04 from `@ccc-wiki` handoff brief after CCC skim of arXiv 2606.01886. OSINT owns **financial temporal graph + governance**; CCC owns passive-injection + wiki-audit patterns for federation wikis.

## Narrative

### InKH layers vs Cemini today

| InKH component | Paper role | Cemini analog (2026-06-04) | Gap |
|----------------|------------|----------------------------|-----|
| Event stream | Trades, chats, tool traces | `wiki/log.md`, daily sweeps, stash episodes, claude-mem observations | No unified **financial** event schema |
| Temporal KG | Low-latency retrieval + invalidation | stash (episodic) + kb-server (wiki RAG) | No trading-state temporal graph; invalidation manual (`[RETRACTED]`, lint) |
| Wiki audit surface | Human-readable governance | Git wiki + `wiki_lint.py` + maturity tags | **Already strong** — aligns with Karpathy LLM Wiki + Cemini ingest |
| Passive injection | Pre-load buffer before agent plans | `CLAUDE.md`, `hot.md`, SessionStart hooks, conductor static routing | Partial — still heavy query-time MCP fan-out |
| Maturity × action risk | Gate writes by claim strength + action type | EMS/RBAC on **orders**; wiki maturity not wired to execution | **Must not** map draft wiki claims to live trades without gates |

### Passive vs agent-driven retrieval

Paper argues **passive injection** beats agent-driven wiki-walk when planning overhead dominates irrelevant context `[TENTATIVE]`. Cemini conductor already biases toward **pre-classified tool routes** and kb_search fan-out rather than re-walking the whole vault each turn — compatible direction, not yet a formal InKH buffer.

### Posture

| Scope | Verdict |
|-------|---------|
| **Wiki-as-audit + ingest discipline** | **ALIGNED** — keep; see `@ccc-wiki/concepts/interaction-native-knowledge-harness.md` |
| **Prod trading temporal graph** | **REFERENCE** — no new memory write path on prod until EMS/RBAC + invalidation design reviewed |
| **Copy-trading / PM analysis agents** | **EVALUATE** — map paper workflows to `@concepts/polymarket-copy-trading-strategy.md` and bot state machines |

### Adoption sequence (if pursued)

1. **Spec invalidation** — which stash fact types expire on position close, regime flip, or market resolution
2. **Shadow passive context** — inject kb+stash bundle at conductor pre-read; measure latency vs tool-walk baseline
3. **Governance matrix** — wiki `maturity` × EMS action class (read / propose / execute)
4. **Prod** — only after `@concepts/ems-execution-security-gaps.md` P0s closed and SeClaw-style eval for memory tools `[OPEN QUESTION 2026-06-04]`

## Snippets

> "The graph should serve online retrieval, while the wiki remains the audit surface."

> — [Source: arxiv-2606.01886-absorbing-complexity-an-interaction-native-knowl.pdf p.4, retrieved 2026-06-04]
