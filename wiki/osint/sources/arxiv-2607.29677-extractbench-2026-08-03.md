---
title: "arXiv 2607.29677 — ExtractBench schema-guided enterprise extraction"
type: source
tags: [source, arxiv, extraction, atto, genealogy, k219]
keywords: [2607.29677, ExtractBench, LlamaExtract, schema-guided, grounding]
related:
  - concepts/computational-genealogy-archival-automation.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
read_status: skimmed
---

## Relations

- @concepts/computational-genealogy-archival-automation.md
- @concepts/gpuology-genealogy-agent-kit.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction |
| arXiv | https://arxiv.org/abs/2607.29677 |
| Filename | `arxiv-2607.29677-extractbench-a-benchmark-for-schema-guided-enter.pdf` |
| sha256 | `96686a0deed88ecffbb92b4600a7995eb7839dd7f1ab0b503230313b4c1e6fdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.29677-extractbench-a-benchmark-for-schema-guided-enter.pdf` |
| read_status | skimmed |

## Narrative

Benchmark for schema-guided extraction with **grounding metadata** + measured cost: **370 docs / 4,869 pages**, 8 domains, 67 types. Reports value F1, record completeness, word-/page-level grounding F1, and cost. VLMs strong on short docs but truncate long lists; coding agents costlier. **LlamaExtract Agentic Plus** tops the three accuracy/grounding metrics.

**Atto / civil-doc extraction** relevance: schema + evidence grounding pattern for Italian civil registers — eval bar, not a vendor lock-in.

## Snippets

> We present ExtractBench… 4,869 pages across 370 enterprise documents… LlamaExtract Agentic Plus ranks first on all three metrics… [Source: arXiv:2607.29677]
