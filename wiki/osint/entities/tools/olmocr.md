---
title: olmOCR — Ai2 PDF-to-Markdown VLM OCR toolkit
type: entity
tags: [entity, tool, ocr, pdf, osint, tipdrop, adopt-tier, k142]
keywords: [olmOCR, AllenAI, Ai2, Qwen2-VL, PDF, Markdown, Apache-2.0, TipDrop M4]
related:
  - sources/multi-wiki-url-evaluation-2026-07-03.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
---

## Relations

- @sources/multi-wiki-url-evaluation-2026-07-03.md — K142 Adopt row
- @concepts/cemini-wiki-ingest-workflow.md — OSINT ingest target surface
- @concepts/wiki-tooling-evaluation.md — tool-eval doctrine

## Raw Concept

K142 Phase-0 audit of [allenai/olmocr](https://github.com/allenai/olmocr), an Ai2 PDF linearization toolkit that converts complex PDFs into Markdown with VLM-assisted layout recovery.

## Narrative

| Field | Value |
|-------|-------|
| **Verdict** | **Adopt** — OSINT PDF ingest + TipDrop M4 candidate |
| **License** | Apache-2.0 (`gh api` + repo metadata, 2026-07-03) |
| **Maturity** | 18.6k★, v0.4.x release train, Ai2-backed |
| **Failure mode** | Local path needs NVIDIA GPU / 12GB+ VRAM and must beat existing parser baselines on Cemini PDFs |

`olmocr` is the cleanest K142 OCR candidate because it targets the exact wiki-ingest failure mode: long regulatory PDFs with tables, diagrams, and multi-column layout. The adoption gate is empirical rather than architectural: benchmark on Cemini/TipDrop fixtures before making it a default stage.

**TipDrop/David:** stage a P0 comparing `olmocr` Markdown output against current PyMuPDF/OCR output for a 30+ page SEC/CFTC PDF; keep output behind M2 compliance normalization.

## Snippets

> "Toolkit for linearizing PDFs for LLM datasets/training." [Source: https://github.com/allenai/olmocr (retrieved 2026-07-03)]
