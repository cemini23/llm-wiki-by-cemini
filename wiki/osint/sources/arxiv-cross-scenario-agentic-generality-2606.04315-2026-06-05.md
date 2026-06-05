---
title: Cross-scenario generality of agentic memory systems (arXiv 2606.04315)
type: source
tags: [source, arxiv, agent-memory, automem, k100, cross-wiki-route]
keywords: [2606.04315, automem, cross-scenario, memory-harness, representation-failure, retrieval-failure]
related:
  - concepts/agent-memory-cross-scenario-generality.md
  - concepts/agent-memory-critique.md
  - concepts/interaction-native-knowledge-harness.md
  - concepts/agent-memory-pipeline-eval-rubric.md
  - concepts/conductor-orchestrator.md
maturity: validated
read_status: read
created: 2026-06-05
updated: 2026-06-05
---

## Relations

- @concepts/agent-memory-cross-scenario-generality.md — OSINT synthesis (prod handoff 2026-06-05)
- @ccc-wiki/sources/arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05.md — CCC K100 skim
- @ccc-wiki/concepts/agentic-memory-cross-scenario-generality.md — CCC thin stub

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline |
| **Authors** | Chen, Gu, Yin, Long, Zeng, Liu, Guo, Zhou, Tang (MSU / GMU / Purdue) |
| **arXiv** | 2606.04315 |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.04315-exploring-cross-scenario-generality-of-agentic-m.pdf` |
| **Retrieved** | 2026-06-05 |
| **Read status** | read — abstract + intro + CCC deep pass; full PDF on librarian |

## Narrative

Evaluates **eight memory architectures** plus a search-agent harness baseline across **five scenario families**: single-turn QA, multi-session chat, agentic-trajectory QA, memory stress tests, and long-horizon tasks. Tracks accuracy with **token cost and latency**.

**AutoMEM** — agentic memory harness with a **self-managed tool interface** — ranks best on **cross-scenario generality** among evaluated systems `[TENTATIVE — single paper]`.

**Two failure modes** on agentic trajectories:

1. **Representation failure** — build-time schemas drop step/action-level evidence.
2. **Retrieval failure** — passive retrieval cannot surface evidence the store already retains.

**K100 routing note:** memory paper — **not** tool-calling generalization (do not bundle with MAVEN 2605.30738).

**Cemini handoff:** prod brief `2026-06-05_automem-memory-cross-scenario-osint-handoff.md` requests OSINT eval of stash + conductor + InKH against the five-scenario matrix before any AutoMEM-style tooling investment.

## Snippets

> "AutoMEM, an agentic memory harness with a self-managed tool interface, achieving the best cross-scenario generality among the systems we evaluate."

> "Existing memory systems struggle on agentic trajectories through two failure modes… a representation-level failure… and a retrieval-level failure."

> — [Source: arxiv-2606.04315-exploring-cross-scenario-generality-of-agentic-m.pdf abstract, retrieved 2026-06-05]

> "Memory performance hinges on giving the agent active control over storage and retrieval rather than on a passive store behind a fixed pipeline."

> — [Source: arxiv-2606.04315 abstract, retrieved 2026-06-05]
