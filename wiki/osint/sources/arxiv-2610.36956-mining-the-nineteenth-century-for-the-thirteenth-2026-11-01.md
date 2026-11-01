---
title: "Legacy editions as zero-label HTR targets for Honorius III"
type: source
tags: [source, arxiv, htr, paleography, papal-registers]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Mining the Nineteenth Century for the Thirteenth: Register-Scale Forced Alignment and HTR Bootstrapping via Legacy Regesta and Antiquarian Editions |
| Authors | Tamás Kovács et al., University of Graz (Department of Digital Humanities) |
| arXiv | 2610.36956 |
| File | `arxiv-2610.36956-mining-the-nineteenth-century-for-the-thirteenth.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.36956 |
| Read status | skimmed (abstract + intro) |

## Narrative

Handwritten text recognition (HTR) for the registers of Pope Honorius III depends on modern expert transcriptions. Those transcriptions exist only for regnal years 1–2 of Reg. Vat. 9. For the remaining registers, nineteenth-century scholarship offers Pressutti’s regesta and partial editions.

The authors measure that legacy layer on fol. 1–203, where both layers exist. They first audit the transcriptions against the legacy layer. They report a division of labor across three tiers: orthographic, lexical, and topological.

At the orthographic tier, raw editions are at best neutral for adapting a recognizer to the second regnal year, and harmful without replay. Projection onto curial spelling, with replay of modern source lines, turns the editions into zero-label adaptation targets. Pooled over all 134 year-2 sides, the WER falls by 1.50 points (95% CI −1.84 to −1.15) and closes 33% of the gap to an oracle. The spelling changes at the year split, through the scribe or the transcriber. The hand changes visibly only at fol. 191r. These figures are single-source claims from this abstract.

At the lexical tier, the corpus-wide legacy lexicon contains 82.2% of the out-of-vocabulary words of unedited entries and flags recognition errors with 66.7% precision. Labels from pre-trained medieval NER models, distilled into the recognizer’s NER head, reach F1 82.1% on an expert-validated benchmark, level with the best tagger applied after recognition. At the topological tier, Pressutti’s regests, the closing datum clauses, and the regests’ dates converted to the chancery’s Roman form find 73.9% of entry starts in the recognized line stream. Edition agreement estimates a CER of 7.80% beyond fol. 203. Each of these figures is a single-source claim from this abstract.

The authors state that antiquarian scholarship can steer, check, and segment HTR across the untranscribed registers. A quant-finance and macro reader meets the same handoff when a modern labeled span ends and only an older edited record continues. This abstract reports the measured gain, and the harm of the raw legacy text, on one papal register.

## Snippets

> "For the remaining registers, nineteenth-century scholarship offers Pressutti’s regesta and partial editions." [Source: `arxiv-2610.36956-mining-the-nineteenth-century-for-the-thirteenth.pdf` p.1 (arXiv 2610.36956), retrieved 2026-11-01]

> "Antiquarian scholarship thus cannot replace modern transcription, but it can steer, check, and segment HTR across the untranscribed registers." [Source: `arxiv-2610.36956-mining-the-nineteenth-century-for-the-thirteenth.pdf` p.1 (arXiv 2610.36956), retrieved 2026-11-01]
