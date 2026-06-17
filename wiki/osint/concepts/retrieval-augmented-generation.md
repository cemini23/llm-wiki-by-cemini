---
title: Retrieval-augmented generation (RAG) — grounding LLMs in external corpora
type: concept
tags: [concept, rag, retrieval, llm-grounding, embedding-search, vector-db, knowledge-base]
keywords: [retrieval augmented generation, RAG, embedding search, vector database, hybrid search, BM25, rerank, retrieval during reasoning]
related:
  - sources/retrieve-during-reasoning.md
  - concepts/reasoning-models.md
  - concepts/cemini-deployment.md
  - sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md
maturity: draft
created: 2026-05-13
updated: 2026-06-17
---

## Relations

- `@sources/retrieve-during-reasoning.md` — primary source: retrieval interleaved with reasoning (next-gen RAG)
- `@concepts/reasoning-models.md` — sibling concept; retrieval-during-reasoning sits at the intersection
- `@concepts/cemini-deployment.md` — Cemini RAG surfaces (wiki, raw-source store, ticker-watchlist) live here

## Raw Concept

What prompted this page: retrieve-during-reasoning source flagged a missing RAG concept hub. RAG is the central technique behind Cemini's wiki + raw-source store, so the page is overdue.

## Narrative

Retrieval-augmented generation: at query time, fetch relevant documents from an external corpus and stuff them into the LLM prompt so it can ground its answer in that text rather than (or in addition to) its parametric weights.

**Three components, in roughly the order they execute**:
1. **Embedding / index** — pre-compute vector representations of corpus chunks; store in a vector DB (or a hybrid BM25 + dense store).
2. **Retrieval** — embed the query; pull top-k matches; optionally re-rank with a cross-encoder.
3. **Generation** — feed retrieved chunks plus the query to the LLM, with a prompt that says "use these as grounding".

**Variants worth knowing**:
- **Hybrid retrieval** — BM25 + dense embeddings, often outperforms either alone, especially on rare-term queries.
- **Multi-hop RAG** — chain retrievals; first hop sets up context for the second hop's query.
- **Retrieval-during-reasoning** (cf. `@sources/retrieve-during-reasoning.md`) — model issues retrieval calls mid-CoT, not just upfront. Useful when the relevant facts depend on intermediate conclusions.
- **GraphRAG** — retrieve over a knowledge graph rather than a flat corpus.

**Cemini fit**: the wiki itself is a curated RAG corpus (see `@concepts/cemini-deployment.md`). The raw-source store on librarian is a deeper RAG layer for ticker-research deep-dives. The retrieval layer is `kb-server` + the `conductor` MCP for cross-wiki queries.

This is a stub.
