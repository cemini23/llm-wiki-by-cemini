---
title: "TongGuOCR — Layout-Aware and Token-Augmented OCR for Chinese Historical Documents"
type: source
tags: [arxiv, k232, atto]
keywords: [2608.07917, ocr, chinese-historical, layout-analysis, token-augmentation, transkribus]
related:
  - entities/tools/transkribus.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
read_status: skimmed
---

## Relations

- @entities/tools/transkribus.md

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.07917 |
| sha256 | `53245cde7c57ee5e7203b316e9df7ee4c3ea6c26cefba315ec608fd65907e23c` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.07917-tongguocr-a-layout-aware-and-token-augmented-ocr.pdf` |
| retrieved | 2026-08-11 |

## Narrative

TongGuOCR (Zhou, Sun, He et al., SCUT + Huawei, 26 pp) targets **Chinese historical document OCR**, where scanned pages mix vertical columns, interlinear annotations, irregular blocks, rare glyphs, and complex reading orders. Two modules: **Layout-Aware Preprocessing** groups consecutive text lines into locally coherent recognition blocks (preserving character detail while retaining context); **Token-Augmented Recognition** adds (a) character-level vocabulary expansion so each rare glyph gets a single-token representation (removing subword fragmentation) and (b) line-to-line transition modeling that injects discrete spatial-displacement tokens to guide the decoder along complex reading paths. A three-stage SFT adapts the recognizer to historical documents.

Results: MTHv2 AR 97.93 / RO-ED 1.51; M5HisDoc AR 93.76, NED 10.43→6.15, RO-ED 7.53→3.49 vs best competitor. Demo `https://jzzh2004.github.io/TongGuOCR`.

**Routing:** Atto **Watch only** — layout/token-augmentation patterns are the steal; Chinese-historical model is OOD for Atto's Italian civil-record HTR. **Transkribus remains sole product HTR**; no Chinese-historical model download into Atto.

[Source: arXiv:2608.07917]
