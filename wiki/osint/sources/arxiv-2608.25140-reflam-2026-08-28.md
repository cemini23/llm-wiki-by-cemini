---
title: "RefLAM — reference-grounded Arabic manuscript line annotation (arXiv 2608.25140)"
type: source
tags: [arxiv, k248, atto, htr, arabic]
keywords: [RefLAM, AraMS-28k, Confidence-100, manuscript, line-annotation]
related:
  - concepts/k248-atto-manuscript-wave.md
  - sources/arxiv-2608.26921-arams-28k-2026-08-28.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
read_status: read
---

## Relations

- @concepts/k248-atto-manuscript-wave.md — Atto HTR / manuscript FIND cluster
- @sources/arxiv-2608.26921-arams-28k-2026-08-28.md — dataset companion released with RefLAM pipeline

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.25140, RefLAM — a reference-grounded line annotation pipeline for Arabic manuscripts |
| Retrieved | 2026-08-28 |
| File | `arxiv-2608.25140-reflam-a-reference-grounded-line-annotation-pipe.pdf` |
| sha256 | `068333df0badf8223f90c195010d8a00d1ec609557bc8bf47ceb9068d33911c2` |
| Dual-ID | **OSINT K248** → Atto manuscript wave |

## Narrative

RefLAM is a reference-grounded pipeline for Arabic manuscript **line-level** annotation. It is Atto-adjacent for HTR / FIND workflows that need high-trust line boxes before transcription. Core operating rule: **Confidence-100** — only accept annotations that clear a full-confidence gate rather than soft-score dumps that pollute training sets.

Reported throughput is about **75×** human baseline: roughly **3000 lines/hour** automated versus about **40 lines/hour** manual. The pipeline is used to build **AraMS-28k** and is validated across **7 books**. For Atto, steal the confidence gate and reference-grounding pattern; do not assume modern handwriting OCR transfers to historical script without book-level validation.

## Snippets

> "Confidence-100 rule; ~75× throughput (3000 vs 40 lines/hr); builds AraMS-28k; 7 books validated." [Source: arxiv-2608.25140-reflam-a-reference-grounded-line-annotation-pipe.pdf (retrieved 2026-08-28)]
