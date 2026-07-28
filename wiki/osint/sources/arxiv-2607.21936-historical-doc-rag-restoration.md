---
title: "Historical document restoration via RAG-LLMs / ARI (arXiv 2607.21936)"
type: source
tags: [source, arxiv, genealogy, htr, rag, k196, atto]
keywords: [ARI, historical document restoration, RAG, named entities, HTR]
related:
  - concepts/computational-genealogy-archival-automation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - entities/tools/transkribus.md
  - concepts/skill-regression-tax.md
  - concepts/historical-document-kg-query-inference.md
  - sources/arxiv-2607.24475-historical-doc-kg-query.md
maturity: draft
read_status: skimmed
created: 2026-07-27
updated: 2026-07-28
clusters: [k196-ingest]
---

## Relations

- @sources/arxiv-2607.24475-historical-doc-kg-query.md — K198 backlink

- @concepts/historical-document-kg-query-inference.md — K198 backlink

- @concepts/computational-genealogy-archival-automation.md
- @concepts/gpuology-genealogy-agent-kit.md
- @entities/tools/transkribus.md
- @concepts/skill-regression-tax.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `arxiv-2607.21936-leveraging-external-knowledge-for-historical-doc.pdf` |
| **sha256** | `432f551ee35e1cd43a3493712efaeeeacc3f8213992833bdf37a84255dab858c` |
| **arXiv** | [2607.21936](https://arxiv.org/abs/2607.21936) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.21936-leveraging-external-knowledge-for-historical-doc.pdf` |

## Narrative

Masked LM restoration uses local context well but fails on **named entities** that need external historical knowledge. **ARI** pairs LLM priors with RAG over external archives so damaged proper nouns can be inferred from retrieved context, not only neighboring glyphs.

**Steal (Atto):** keep Transkribus/HTR for glyph recovery; add retrieval-gated entity restore for surnames/places (Antenati/comune priors) — never invent pedigree. Aligns with sources-before-automation discipline.

## Snippets

> "existing restoration methods … struggle to restore named entities that require external historical knowledge"
