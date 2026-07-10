---
title: Transkribus (HTR for historical manuscripts)
type: entity
tags: [tool, genealogy, htr, paleography, draft]
keywords: [Transkribus, READ-COOP, handwriting recognition, Latin, PAGE XML]
related:
  - sources/gemini-automated-deep-genealogy-research-2026-07-09.md
  - concepts/computational-genealogy-archival-automation.md
  - entities/tools/gcerretani-antenati.md
  - entities/tools/italian-parish-records.md
maturity: draft
created: 2026-07-09
updated: 2026-07-09
---

## Relations

- @sources/gemini-automated-deep-genealogy-research-2026-07-09.md — HTR section primary cite
- @concepts/computational-genealogy-archival-automation.md — parish/notarial transcription layer
- @entities/tools/gcerretani-antenati.md — typical image source for Italian civil packs
- @entities/tools/italian-parish-records.md — parish image corpus companion (K154)

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
