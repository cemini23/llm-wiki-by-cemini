---
title: "PyPottery: AI suite for archaeology documentation (2610.02072)"
type: source
tags: [source, k278, atto, htr, archaeology]
keywords: [k278, pypottery, olmocr, htr, no-clone]
related:
  - concepts/k278-atto-htr-wave.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
read_status: skimmed
---

## Relations

- @concepts/k278-atto-htr-wave.md

## Raw Concept

| File | `arxiv-2610.02072-pypottery-an-ai-powered-end-to-end-suite-for-pot.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.02072-pypottery-an-ai-powered-end-to-end-suite-for-pot.pdf` |
| Archive | egress-fi 2026-10-02 |
| Retrieved | 2026-10-02 |
| sha256 | `490718261c766df13f969834b44c0b7095c63fd05e38cd994ca669e854a4f0e4` |
| Dual-ID | **OSINT K278** |
| arXiv | 2610.02072 |
| Author | Lorenzo Cardarelli (Gottingen; ISMed-CNR) |
| Repo | `https://github.com/lrncrd/PyPottery` |
| Docs | `https://lrncrd.github.io/PyPottery/` |

## Narrative

An open-source suite that semi-automates the ceramic documentation pipeline. The target is the post-production bottleneck that leaves archaeological data unpublished. The author frames it as augmentation of the archaeologist, not replacement.

Four modules. Scan handles image extraction, handwriting OCR, and structured parsing. Ink does pencil-to-ink image translation. Trace does semantics-aware vectorisation. Layout generates the publication plate. The OCR step uses a 7B vision-language model in 4-bit. Parsing uses few-shot prompting on a 7B model. Vectorisation uses a segmentation model plus custom algorithms.

Evaluated on 50 hand-drawn sheets with 240 drawings from a site in Italy, plus a five-expert usability study.

| Measure | Result |
|---------|--------|
| OCR character error rate | 6.2% (plus or minus 1.2) |
| OCR word error rate | 18.6% (plus or minus 3.5) |
| Parsing exact-match, 1 example | 13.56% |
| Parsing exact-match, 3 examples | 52.63% |
| Parsing exact-match, 10 examples | 67.60% (accuracy 93.13%) |
| Full pipeline | about 103 minutes for 240 drawings, 140 per hour |
| Auto-vectorisation needing manual fixes | 21 records, 8.75% |
| Usability, task completion | 83.3% |
| Usability, SUS score | 83.5 (Grade A) |
| Perceived speedup, median | 40x, range 17.5x to 120x |

The author admits the limits. It needs 300 DPI scans and legible handwriting. Complex vessel views still vectorise poorly. The source drawings cannot be released, so results can be audited but not re-executed. One site, one documentation tradition, five usability participants.

Result for Atto: the closest analogue in the wiki so far. Both projects turn hand-drawn, hand-written archival records into structured data, and both face an OCR stage then a field-parsing stage. Two numbers matter: a 6.2% character error rate on **cursive archaeological handwriting**, and the few-shot curve, which shows parsing needs about 10 examples before it is useful. That few-shot curve is a concrete planning number for any Atto parsing work.

Read the licence before any action. The repo is named but not yet checked by `gh api`. No clone. **Transkribus stays the only product HTR.**
