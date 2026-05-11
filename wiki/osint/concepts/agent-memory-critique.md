---
title: "Agent Memory Critique — Lookup vs True Memory"
type: concept
tags: [llm-agents, agent-memory, rag, vector-stores, infrastructure]
keywords: [agent-memory, RAG, vector-stores, lookup, episodic-memory, consolidation, forgetting, Stash, kb-server]
related:
  - sources/contextual-agentic-memory-critique-2604.27707.md
  - sources/agent-native-research-artifacts-2604.24658.md
  - concepts/agent-native-research-artifacts.md
  - entities/infrastructure/librarian-server-architecture.md
  - concepts/exploration-graph-dead-ends.md
  - entities/tools/letta-memgpt.md
maturity: draft
created: 2026-05-02
updated: 2026-05-11
---

## Raw Concept

Are current "agent memory" systems (vector stores, RAG, context-window extension) actually memory? What would true agent memory require?

## Narrative

Current agent memory systems — kb-server's pgvector search, Stash's episodic store, context-window stuffing — are **lookup mechanisms** (memos), not memory. True memory requires four capabilities that current systems lack:

1. **Selective encoding** — not everything is worth storing; memory must filter
2. **Consolidation over time** — reorganizing and strengthening important memories across sessions
3. **Context-dependent retrieval** — relevance depends on the current task, not just vector similarity
4. **Active forgetting** — pruning obsolete, incorrect, or superseded information

This is not an argument against memo systems. A memo pad is useful. The argument is that calling lookup "memory" creates false expectations about agent continuity and reliability.

For Cemini: kb-server and Stash are legitimate memo infrastructure. They should be used for what they're good at (factual retrieval, calibration data storage for token-prior construction). They should not be expected to provide agent continuity across sessions — that requires capabilities beyond current infrastructure.

**ARA connection**: The @concepts/agent-native-research-artifacts.md Live Research Manager partially addresses the memory gap for the narrow domain of research-process capture. It operates at session boundaries, distilling researcher-agent conversations into typed events (decisions, dead ends, experiments) that accumulate in the artifact's exploration graph. This is selective encoding + consolidation — two of the four missing criteria — but only for research trajectories, not general agent memory. The exploration graph's dead_end nodes with structured failure modes are a concrete implementation of "active forgetting via preservation" (keeping what was tried and abandoned, rather than silently discarding).

## Snippets

- Four criteria for true memory: selective encoding, consolidation over time, context-dependent retrieval, forgetting. Current agent memory systems satisfy zero of four. [Source: contextual-agentic-memory-critique-2604.27707.pdf]
- "Memo" systems are useful but should not be confused with memory. [Source: contextual-agentic-memory-critique-2604.27707.pdf]
