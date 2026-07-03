---
title: Unlimited-OCR — Baidu long-document OCR model
type: entity
tags: [entity, tool, ocr, tipdrop, k141]
keywords: [Unlimited-OCR, baidu, R-SWA, PyMuPDF, MIT, TipDrop, ingest]
related:
  - sources/eval-huggingface-models-v2-2026-07-03.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-wiki-ingest-workflow.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
---

## Relations

- @sources/eval-huggingface-models-v2-2026-07-03.md — K141 Adopt row
- @concepts/cemini-wiki-ingest-workflow.md — OSINT M4 ingest analog

## Raw Concept

K141 eval of [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) — long PDF parsing via Reference Sliding Window Attention.

## Narrative

| Field | Value |
|-------|-------|
| **HF / GitHub** | `baidu/Unlimited-OCR` |
| **License** | **MIT** (`gh api` on linked repo 2026-07-03) |
| **Verdict** | **Adopt** — TipDrop M4 + OSINT long-PDF ingest reference |
| **Steal** | Constant KV cache for 50+ page regulatory PDFs; vLLM/SGLang deploy |

**TipDrop compliance:** YES per eval — still route through M2 normalizer.

Brief: `../projects/tipdrop-workspace-kit/briefs/2026-07-03_k141-unlimited-ocr-ingest-adopt.md`

## Snippets

> "Maintaining a constant KV cache throughout the decoding process." [Source: Hugging Face Model Evaluation 2.docx URL 2 (retrieved 2026-07-03)]
