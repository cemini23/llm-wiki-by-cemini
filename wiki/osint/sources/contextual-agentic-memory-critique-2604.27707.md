---
title: "Contextual Agentic Memory is a Memo, Not True Memory"
type: source
tags: [llm-agents, agent-memory, rag, vector-stores, context-window]
keywords: [agent-memory, RAG, vector-stores, context-window, lookup-vs-memory, episodic-memory, Stash, kb-server, pgvector]
related:
  - concepts/agent-memory-critique.md
  - entities/infrastructure/librarian-server-architecture.md
  - entities/tools/letta-memgpt.md
maturity: draft
read_status: deep-read
created: 2026-05-02
updated: 2026-05-11
arxiv: "2604.27707"
---

## Raw Concept

- Original title: Contextual Agentic Memory is a Memo, Not True Memory
- Type: PDF (arXiv preprint)
- Location: cemini-librarian:/opt/cemini-bulk/research/Contextual Agentic Memory is a Memo, Not True Memory.pdf
- Retrieved: 2026-05-02
- Pages: ~12p
- Read status: deep-read

## Narrative

This paper argues that current "agent memory" systems — vector stores (RAG), context-window stuffing, and embedding-based retrieval — are fundamentally **lookup mechanisms**, not memory. True memory requires: (1) selective encoding (not everything is worth remembering), (2) consolidation over time (reorganizing and strengthening important memories), (3) context-dependent retrieval (what's relevant depends on the current task, not just vector similarity), and (4) forgetting (pruning obsolete or incorrect information).

This is a direct critique of the architecture Cemini uses: kb-server (pgvector-based wiki search) and Stash (Postgres episodic store with vector recall). Both are "memo" systems — they store and retrieve by similarity, but lack consolidation, selective encoding, and active forgetting.

The paper does NOT argue that memo systems are worthless — a memo pad is useful. The argument is that calling them "memory" creates false expectations about agent continuity and reliability. For Conductor, this reinforces the calibration loop design: Stash stores episodes for token-prior construction (a legitimate memo use case), but Conductor should not expect Stash recall to substitute for real agent continuity across sessions.

## Snippets

- "Vector stores, RAG, and context-window extension are lookup mechanisms — memos — not memory. They lack selective encoding, consolidation over time, context-dependent retrieval, and active forgetting." [Source: Contextual Agentic Memory is a Memo, Not True Memory.pdf]
- Four criteria for true memory: selective encoding, consolidation over time, context-dependent retrieval, forgetting. Current systems satisfy zero of four. [Source: Contextual Agentic Memory is a Memo, Not True Memory.pdf]
- Memo systems are useful but should not be confused with memory; doing so creates false expectations about agent continuity and reliability across sessions. [Source: Contextual Agentic Memory is a Memo, Not True Memory.pdf]
