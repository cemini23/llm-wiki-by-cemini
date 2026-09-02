---
title: Unlimited-OCR — Baidu long-document OCR model
type: entity
tags: [entity, tool, ocr, tipdrop, k141]
keywords: [Unlimited-OCR, baidu, R-SWA, PyMuPDF, MIT, TipDrop, ingest]
related:
  - sources/eval-huggingface-models-v2-2026-07-03.md
  - sources/eval-github-ocr-repositories-2026-08-01.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-wiki-ingest-workflow.md
  - entities/tools/franken-ocr.md
  - entities/tools/curiosity-localocr.md
  - entities/tools/transkribus.md
maturity: draft
created: 2026-07-03
updated: 2026-08-01
harness_verb: FILE
---

## Relations

- @sources/eval-huggingface-models-v2-2026-07-03.md — K141 Adopt row
- @sources/eval-github-ocr-repositories-2026-08-01.md — K217 Phase-0 clone
- @concepts/cemini-wiki-ingest-workflow.md — OSINT M4 ingest analog
- @entities/tools/franken-ocr.md — CPU path Phase-0 Extract
- @entities/tools/curiosity-localocr.md — UI gate Extract
- @entities/tools/transkribus.md — sole product HTR (Unlimited-OCR is PDF REFERENCE only)

## Raw Concept

K141 eval of [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) — long PDF parsing via Reference Sliding Window Attention.

## Narrative

| Field | Value |
|-------|-------|
| **HF / GitHub** | `baidu/Unlimited-OCR` |
| **License** | **MIT** (`gh api` on linked repo 2026-07-03) |
| **Verdict** | **Adopt** — TipDrop M4 + OSINT long-PDF ingest reference |
| **Steal** | Constant KV cache for 50+ page regulatory PDFs; vLLM/SGLang deploy |
| **Local** | `.local/adopts/Unlimited-OCR` (~187MB shallow, K217) |
| **Product** | TipDrop M4 + Atto multi-page REFERENCE — **not** Transkribus HTR replace |

**TipDrop compliance:** YES per eval — still route through M2 normalizer.

Brief: `../projects/tipdrop-workspace-kit/briefs/2026-07-03_k141-unlimited-ocr-ingest-adopt.md`

## Snippets

> "Maintaining a constant KV cache throughout the decoding process." [Source: Hugging Face Model Evaluation 2.docx URL 2 (retrieved 2026-07-03)]
