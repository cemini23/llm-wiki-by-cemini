---
title: "Li 2026 — WikiKV hierarchical path-indexed wiki storage (arXiv 2606.14275)"
type: source
tags: [source, arxiv, wiki, rag, librarian-tooling]
keywords: [2606.14275, WikiKV, path-indexed, hierarchical knowledge base, schema evolution]
related:
  - entities/tools/wikikv.md
  - concepts/wiki-tooling-evaluation.md
  - meta/librarian-decommission-2026-06-14.md
  - concepts/federated-daily-research-digest.md
  - concepts/retrieval-augmented-generation.md
maturity: validated
read_status: read
created: 2026-06-17
updated: 2026-06-17
cross-wiki-source: "@seo-wiki/sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md"
---

## Relations

- @entities/tools/wikikv.md
- @concepts/wiki-tooling-evaluation.md — adoption evaluation row (REFERENCE)
- @meta/librarian-decommission-2026-06-14.md — post-librarian laptop git wikis; steal navigation patterns
- @concepts/federated-daily-research-digest.md — federation wiki read path
- @concepts/retrieval-augmented-generation.md — hierarchical navigation vs flat RAG
- @seo-wiki/sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md — cross-wiki ingest from SEO digest

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | WikiKV: Schema-Evolving Path-Indexed Storage for Hierarchical Knowledge Navigation |
| **Authors** | Feifei Li, Haoliang Ming, Zihan Li, et al. (Tencent / WeChat) |
| **arXiv** | 2606.14275v1 |
| **Retrieved** | 2026-06-17 via @seo-wiki federated digest |
| **Read status** | read (model + deployment summary) |

## Narrative

Tencent production system for **LLM-curated hierarchical wikis**: path-as-key KV store with O(1) `GET`/`LS`, schema merge/split evolution, Error Book cross-batch correction, and budgeted `NAV(q,B)` with search-accelerated routing (O(depth)→O(1) expected hops). WeChat Official Account AI Assistant deployment; AUTHTRACE **63.2%** E2E answer correctness vs flat RAG baselines.

**Federation relevance (2026-06-17):** Post-librarian-decommission, laptop git wikis are canonical. WikiKV is **REFERENCE only** (no OSS) — steal hierarchical navigation + consistency protocol patterns; do not replace `wiki_lint.py` + grep read path with unbuilt storage engine.

## Snippets

> "No existing storage model natively supports this access pattern." [Source: arxiv-2606.14275 §I — on SQL/graph/flat-KV/FS mismatch for hierarchical wikis]
