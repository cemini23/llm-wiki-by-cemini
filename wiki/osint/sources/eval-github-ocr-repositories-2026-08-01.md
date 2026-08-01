---
title: "Eval — Evaluate OCR GitHub Repositories 2026-08-01"
type: source
tags: [tool-eval, ocr, atto, k217]
keywords: [PaddleOCR, Unlimited-OCR, GOT-OCR2.0, localOCR, OCRmyPDF, DeepSeek-OCR, EasyOCR, Umi-OCR]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/gpuology-genealogy-agent-kit.md
  - entities/tools/transkribus.md
  - entities/tools/unlimited-ocr.md
  - entities/tools/curiosity-localocr.md
  - entities/tools/ocrmypdf.md
  - entities/tools/deepseek-ocr.md
maturity: draft
created: 2026-08-01
updated: 2026-08-01
read_status: deep-read
---

## Relations

- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/gpuology-genealogy-agent-kit.md
- @entities/tools/transkribus.md
- @entities/tools/unlimited-ocr.md
- @entities/tools/curiosity-localocr.md
- @entities/tools/ocrmypdf.md
- @entities/tools/deepseek-ocr.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Evaluate OCR GitHub Repositories.docx |
| sha256 | `6788b0520cc11922e90d7c1f5f263d207ac0ae9ed2dfb7324ee677c3218d965a` |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/osint/Evaluate OCR GitHub Repositories.docx |
| URLs | 19 OCR / VLM repos |
| read_status | deep-read |

## Narrative

Batch theme: VLM / layout OCR for archival extraction. **Product policy unchanged: Transkribus = sole HTR.** Phase-0 clones are REFERENCE / pre-process / UI only.

| Repo | Eval tier | SPDX (`gh api` 2026-08-01) | Cemini verdict |
|------|-----------|----------------------------|----------------|
| Curiosity-Ai-BV/localOCR | Extract | **MIT** | **GO Extract** UI/JSON gate — Phase-0 (~3MB) |
| baidu/Unlimited-OCR | Integrate | **MIT** | **GO Extract** multi-page PDF REFERENCE — Phase-0 (~187MB); not HTR replace |
| deepseek-ai/DeepSeek-OCR | Watch | **MIT** | **Watch** hallucination risk — Phase-0 (~17MB) |
| ocrmypdf/OCRmyPDF | Watch | **MPL-2.0** | **Watch** searchable PDF layer — Phase-0 (~19MB) |
| PaddlePaddle/PaddleOCR | Integrate | **Apache-2.0** | **NO-GO clone** size (~1.9GB API); patterns only |
| hiroi-sora/Umi-OCR | — | **MIT** | **Skip** ~275MB budget |
| JaidedAI/EasyOCR | — | **Apache-2.0** | **Skip** ~158MB budget |
| Ucas-HaoranWei/GOT-OCR2.0 | Integrate | **NULL** (no LICENSE) | **NO-GO** license |
| typo localOCR forks (×8) | Reject | mixed / NOT FOUND | Aggregate Reject — no stubs |

## Snippets

Eval Integrate set claimed PaddleOCR + Unlimited-OCR + GOT-OCR2.0. SPDX null on GOT and size cap on Paddle override eval Integrate → clone. [Source: Evaluate OCR GitHub Repositories.docx]
