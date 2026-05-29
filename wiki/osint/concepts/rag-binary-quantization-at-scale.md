---
title: RAG binary quantization at scale
type: concept
tags: [concept, rag, vector-search, kb-server, embeddings, k78]
keywords: [binary-quantization, hamming-distance, float32, retrieval-latency, vector-compression]
related:
  - sources/trading-posts-compilation-6-2026-05-29.md
  - concepts/librarian-server-architecture.md
  - concepts/kb-server-retrieval-scaling.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @sources/trading-posts-compilation-6-2026-05-29.md — K78 Post 2 (@Suryanshti777)
- @concepts/librarian-server-architecture.md — kb-server hosting context
- @concepts/kb-server-retrieval-scaling.md — scaling frame if page exists

## Raw Concept

Compress dense float32 embeddings to **binary vectors** (sign bit per dimension) for ~**32×** memory reduction and faster Hamming-distance retrieval — infrastructure layer for production RAG at millions+ vectors.

## Narrative

### Claimed shift (Post 2 framing)

- Demo RAG: embed → store → retrieve chunks.
- Production RAG: permission-aware sync, hybrid search, rerank, **index economics** dominate.
- Binary quantization moves bottleneck from storage to orchestration.

### Cemini / librarian angle

- Relevant if `cemini-librarian` vector index grows beyond comfortable RAM for float32 wiki embeddings.
- Requires quality eval: **`[TENTATIVE 2026-05-29]`** — binary embedding → Hamming rerank is standard (~32× memory vs float32 per dimension); Cemini-specific **recall@k loss on wiki embeddings** still needs librarian benchmark before reindex.
- Pairs with existing Ollama embedding path — not a drop-in without reindex + benchmark.

## Snippets

> "Sometimes by ~32x." [Source: Posts.docx K78 Post 2 — memory reduction claim, @Suryanshti777]
