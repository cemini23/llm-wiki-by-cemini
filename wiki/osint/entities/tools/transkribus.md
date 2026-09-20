---
title: Transkribus (HTR for historical manuscripts)
type: entity
tags: [tool, genealogy, htr, paleography, draft]
keywords: [Transkribus, READ-COOP, handwriting recognition, Latin, PAGE XML]
related:
  - sources/arxiv-2608.01646-spike-htr.md
  - entities/tools/spike-htr.md
  - entities/tools/pdf-inspector.md
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
  - entities/tools/dhfbk-tint.md
  - sources/gemini-automated-deep-genealogy-research-2026-07-09.md
  - concepts/computational-genealogy-archival-automation.md
  - entities/tools/gcerretani-antenati.md
  - entities/tools/italian-parish-records.md
  - sources/arxiv-2607.15509-llm-automl-handwritten-ocr.md
  - sources/gemini-italian-civil-register-extraction-2026-07-21.md
  - sources/arxiv-2607.21936-historical-doc-rag-restoration.md
  - sources/eval-github-ocr-repositories-2026-08-01.md
  - sources/eval-github-repo-revenue-analysis-htr-2026-08-01.md
  - entities/tools/curiosity-localocr.md
  - entities/tools/simplehtr.md
  - entities/tools/unlimited-ocr.md
  - entities/tools/deepseek-ocr.md
  - entities/tools/htrflow.md
  - entities/tools/kurrentschrift.md
  - sources/arxiv-2608.07917-tongguocr-2026-08-11.md
  - concepts/k264-atto-wave.md
  - sources/arxiv-2609.20064-ppocrv6-historical-2026-09-18.md
  - concepts/k265-atto-wave.md
  - entities/tools/tax-doc-classifier.md
  - concepts/k267-atto-wave.md
maturity: draft
created: 2026-07-09
updated: 2026-09-20
---

## Relations

- @concepts/k267-atto-wave.md

- @sources/arxiv-2608.01646-spike-htr.md
- @concepts/k265-atto-wave.md
- @entities/tools/tax-doc-classifier.md

- @entities/tools/spike-htr.md

- @entities/tools/pdf-inspector.md — K218 scanned-vs-text PDF routing

- @sources/arxiv-2607.21936-historical-doc-rag-restoration.md — K196 backlink
- @sources/arxiv-2607.15509-llm-automl-handwritten-ocr.md — K177 LLM-NAS HTR Watch (contrast)
- @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md — K176 GPUOLOGY business DR
- @concepts/gpuology-genealogy-agent-kit.md — product strategy concept
- @sources/gemini-italian-civil-register-extraction-2026-07-21.md — K180 Italian Handwriting M1 + layout/marginalia; human-in-loop

- @sources/gemini-automated-deep-genealogy-research-2026-07-09.md — HTR section primary cite
- @concepts/computational-genealogy-archival-automation.md — parish/notarial transcription layer
- @entities/tools/gcerretani-antenati.md — typical image source for Italian civil packs
- @entities/tools/italian-parish-records.md — parish image corpus companion (K154)
- @entities/tools/dhfbk-tint.md — K175 Italian NLP after HTR/OCR text exists
- @sources/eval-github-ocr-repositories-2026-08-01.md — K217 OCR eval (Transkribus remains sole product HTR)
- @sources/eval-github-repo-revenue-analysis-htr-2026-08-01.md — K217 HTR eval
- @entities/tools/curiosity-localocr.md — UI gate Extract
- @entities/tools/simplehtr.md — CTC lexicon REFERENCE
- @entities/tools/unlimited-ocr.md — multi-page PDF REFERENCE
- @entities/tools/deepseek-ocr.md — VLM OCR Watch
- @entities/tools/htrflow.md — EUPL Reference-only
- @entities/tools/kurrentschrift.md — ductus Extract
- @concepts/k264-atto-wave.md — PP-OCRv6 FILE; Transkribus remains sole product HTR
- @sources/arxiv-2609.20064-ppocrv6-historical-2026-09-18.md

## Raw Concept

READ-COOP platform for Handwritten Text Recognition on historical scripts (community models for Latin / early modern hands). Site: [transkribus.org](https://www.transkribus.org/). REST API for headless jobs → PAGE/ALTO/text.

## Narrative

| Field | Value |
|-------|-------|
| **When** | Unindexed parish/notarial images where Tesseract-style OCR fails |
| **Alt** | Multimodal LLMs (Gemini roadmap claims ~5–7% CER on some 18–19c hands — **vendor claim / secondary**; verify on your script) [NEEDS VERIFICATION 2026-07-09] |
| **Verdict** | **Watch** — not a CeminiSuite trading dependency; optional for personal archival projects after civil acts are exhausted |
| **Phase-0** | Required before paid API spend or local model ops |

Script eras in the Gemini roadmap (Caroline, Gothic, Humanist, Secretary Hand) are orientation guides, not auto-classifier outputs.

## Snippets

> Dedicated HTR beats glyph OCR on connected early-modern cursive; pick model by century/script. [Source: @sources/gemini-automated-deep-genealogy-research-2026-07-09.md]
