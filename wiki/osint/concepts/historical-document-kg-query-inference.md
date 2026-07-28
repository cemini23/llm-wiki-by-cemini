---
title: Historical-document KG query inference (Atto)
type: concept
tags: [concept, genealogy, atto, htr, k198]
keywords: [knowledge graph, query inference, HTR, sentence embeddings, TSDAE]
related:
  - sources/arxiv-2607.24475-historical-doc-kg-query.md
  - sources/arxiv-2607.24542-ancient-sentence-embeddings.md
  - sources/arxiv-2607.21936-historical-doc-rag-restoration.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - entities/tools/book-to-skill.md
  - entities/tools/geolibre.md
  - sources/x-lamgary-harvey-scaling-document-processing-2026-07-27.md
  - concepts/document-processing-pipeline-scale-patterns.md
maturity: draft
created: 2026-07-28
updated: 2026-07-28
---

## Relations

- @concepts/document-processing-pipeline-scale-patterns.md — K199

- @sources/x-lamgary-harvey-scaling-document-processing-2026-07-27.md — K199 Harvey scale

- @sources/arxiv-2607.24475-historical-doc-kg-query.md
- @sources/arxiv-2607.24542-ancient-sentence-embeddings.md
- @sources/arxiv-2607.21936-historical-doc-rag-restoration.md
- @concepts/computational-genealogy-archival-automation.md
- @concepts/gpuology-genealogy-agent-kit.md
- @entities/tools/book-to-skill.md
- @entities/tools/geolibre.md

## Raw Concept

How should Atto treat noisy HTR/ATR text before human-gated GEDCOM merge?

## Narrative

Two complementary 2026-07 papers: (1) **KG query inference/execution** for robust historical interpretation (2607.24475); (2) unsupervised **TSDAE/CSE sentence embeddings** for ancient-language reuse on noisy ATR (2607.24542) — CSE works with 4–8k sentences on a laptop GPU. Stack with K196 ARI entity restore. Product path: Transkribus/HTR → provisional embeddings/KG queries → human gate → truth.ged. **No LLM-NAS.** book-to-skill packages methodology into SKILL.md; GeoLibre for place maps.
