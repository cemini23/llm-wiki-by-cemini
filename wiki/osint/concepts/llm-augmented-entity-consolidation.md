---
title: "LLM-augmented entity consolidation (cross-domain pattern)"
type: concept
tags: [concept, methodology, embeddings, llm-curation, k71]
keywords: [entity normalization, canonical vocabulary, recipe ingredients, epicure, string deduplication]
related:
  - sources/arxiv-epicure-food-embeddings-2605.22391.md
  - concepts/high-signal-paper-patterns.md
maturity: draft
created: 2026-05-27
updated: 2026-05-27
---

## Relations

- @sources/arxiv-epicure-food-ingredients-2605.22391.md — K71 Epicure paper (food domain; pattern source)
- @concepts/high-signal-paper-patterns.md — Filter 3 fail for Epicure on trading domain; pattern still portable
- @sources/arxiv-epicure-food-embeddings-2605.22391.md — K71 primary source

## Raw Concept

Cross-domain methodology note: use an LLM pass to collapse noisy surface strings into a canonical entity vocabulary before graph/embedding training — Epicure 6,653→1,790 ingredients [Source: arXiv 2605.22391].

## Narrative

**OSINT relevance:** Wiki ingest already performs entity stub consolidation manually; automated pre-ingest canonicalization (tickers, handles, venue aliases) could reduce orphan duplicates — **research backlog**, not implemented.

**Not** a license to ingest Epicure food embeddings into Cemini trading stack.

## Snippets

> "LLM-augmented pipeline" consolidating raw strings to canonical entries before Metapath2Vec training. [Source: arXiv 2605.22391, 2026-05-27]
