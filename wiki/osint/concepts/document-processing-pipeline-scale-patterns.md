---
title: Document-processing pipeline scale patterns (Harvey → Atto)
type: concept
tags: [concept, document-processing, atto, harness, k199]
keywords: [Job Framework, UDF, Arrow IPC, OCR fallback, dual-write, stage queues]
related:
  - sources/x-lamgary-harvey-scaling-document-processing-2026-07-27.md
  - concepts/historical-document-kg-query-inference.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/code-as-agent-harness.md
  - concepts/verifier-deployment-gap.md
  - concepts/skill-regression-tax.md
  - sources/arxiv-2608.13463-mllm-ensembles-2026-08-14.md
maturity: draft
created: 2026-07-28
updated: 2026-08-14
---

## Relations

- @sources/x-lamgary-harvey-scaling-document-processing-2026-07-27.md
- @concepts/historical-document-kg-query-inference.md
- @concepts/gpuology-genealogy-agent-kit.md
- @concepts/computational-genealogy-archival-automation.md
- @concepts/code-as-agent-harness.md
- @concepts/verifier-deployment-gap.md
- @concepts/skill-regression-tax.md

## Raw Concept

What production patterns should Atto steal when vault/intake dumps grow beyond one-shot HTR jobs?

## Narrative

Harvey's 2026-07 scale narrative maps cleanly onto Atto's document path (scan/IIIF → HTR → structure → search/share):

| Pattern | Steal for Atto |
|---------|----------------|
| Durable job framework | Resume mid-batch Antenati town sprints; isolate corrupt pages |
| Split extract / embed / index | OCR-heavy parish pages must not starve KG/query stage |
| Typed intermediate format (UDF) | Versioned page/table/image slices — not one giant LLM blob |
| Embedding persistence + cheap handoff | Avoid re-embedding; prefer columnar/IPC over JSON between stages |
| OCR fallback chain | Transkribus primary → local/deterministic → mark fail |
| Dual-write / shadow-read migrations | When swapping vault search backends |
| External quality bar | "No observed regression" needs field/span eval — not self-score (K198 verifier gap) |

Do **not** copy Harvey's proprietary stack; copy the stage boundaries and failure model. Keep PII vault + human-gated GEDCOM merge.
