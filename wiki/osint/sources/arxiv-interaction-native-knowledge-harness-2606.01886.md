---
title: Absorbing Complexity — interaction-native knowledge harness (arXiv 2606.01886)
type: source
tags: [source, arxiv, knowledge-harness, financial-agents, prediction-markets]
keywords: [2606.01886, inkh, temporal-graph, passive-injection, wiki-audit, copy-trading]
related:
  - concepts/interaction-native-knowledge-harness.md
  - concepts/librarian-server-architecture.md
  - concepts/kb-server-retrieval-scaling.md
  - concepts/agent-memory-critique.md
  - concepts/conductor-orchestrator.md
  - concepts/ems-execution-security-gaps.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/cemini-knowledge-application-architecture.md
  - entities/tools/claude-mem.md
  - sources/llm-wiki.md
  - sources/agentmemory-rohitg00-cpr-impl.md
maturity: draft
read_status: skimmed
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- `@concepts/interaction-native-knowledge-harness.md` — OSINT financial deployment synthesis
- `@concepts/librarian-server-architecture.md` — kb-server + stash as Cemini retrieval/audit stack
- `@concepts/polymarket-copy-trading-strategy.md` — primary paper workflow domain
- `@sources/llm-wiki.md` — Karpathy LLM Wiki pattern cited in paper
- `@sources/agentmemory-rohitg00-cpr-impl.md` — RRF graph+vector retrieval contrast
- `@ccc-wiki/sources/arxiv-interaction-native-knowledge-harness-2606.01886.md` — CCC harness-layer mirror (ingested 2026-06-04)
- `@ccc-wiki/concepts/interaction-native-knowledge-harness.md` — CCC steal-from patterns

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents |
| **Authors** | True Trading; Inc4.net |
| **arXiv** | 2606.01886 |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.01886-absorbing-complexity-an-interaction-native-knowl.pdf` |
| **Retrieved** | 2026-06-04 |
| **Read status** | skimmed — CCC cross-wiki handoff + abstract/intro; deep-read deferred |
| **Handoff** | `briefs/2026-06-04_inkh-financial-knowledge-harness-osint-handoff.md` from `@ccc-wiki` |

## Narrative

**InKH** (interaction-native knowledge harness) targets **financial cognition friction**: traders and agents repeatedly re-derive context (positions, regime, copy-trade signals, policy) instead of the system absorbing interaction traces into governed memory.

Architecture (paper): **event stream** → **temporal knowledge graph** (online retrieval) + **wiki audit surface** (human governance) + **passive knowledge injection** into a bounded working-context buffer (vs agent-driven wiki-walk at query time). **Write-time invalidation** and **maturity × action-risk gates** reduce stale facts reaching high-risk actions.

Benchmark claims `[TENTATIVE — single paper, not reproduced on Cemini stack]`:

- 82.95% latency reduction vs agent-driven wiki-walk memory
- 96.58% stale-knowledge reduction with invalidation enabled

**Cemini routing:** harness *patterns* overlap CCC federation ingest (`wiki_lint`, maturity tags, daily sweeps). **Trading temporal graph + financial invalidation on prod** stay OSINT-owned — pair with `@concepts/ems-execution-security-gaps.md` before any live memory write path.

## Snippets

> "Adoption happens when complexity is absorbed by the system rather than transferred to the user."

> "The graph should serve online retrieval, while the wiki remains the audit surface."

> "Retrieval is not solely a query-time decision made by the agent."

> — [Source: arxiv-2606.01886-absorbing-complexity-an-interaction-native-knowl.pdf p.1,4–5, retrieved 2026-06-04]
