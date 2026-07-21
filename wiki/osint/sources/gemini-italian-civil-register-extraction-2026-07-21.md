---
title: Italian Civil Register Extraction (Gemini DR — acts + HTR)
type: source
tags: [source, docx, genealogy, htr, stato-civile, k180, italy]
keywords: [atto di nascita, marginalia, Part II, Transkribus, eScriptorium, Kraken, evidence packet, ARK, DGS]
clusters: [k180-ingest]
related:
  - concepts/computational-genealogy-archival-automation.md
  - concepts/antenati-deep-link-grammar.md
  - entities/tools/transkribus.md
  - entities/tools/gcerretani-antenati.md
  - sources/gemini-portale-antenati-research-guide-2026-07-21.md
  - sources/gemini-italian-genealogy-research-tools-2026-07-21.md
  - sources/arxiv-2607.15509-llm-automl-handwritten-ocr.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
read_status: read
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- @entities/tools/transkribus.md — Italian Handwriting M1 / layout-aware HTR; human-in-loop
- @concepts/computational-genealogy-archival-automation.md — evidence packets before tree merge
- @concepts/antenati-deep-link-grammar.md — ARK citation targets
- @sources/gemini-portale-antenati-research-guide-2026-07-21.md — portal URL / dual-original companion
- @sources/arxiv-2607.15509-llm-automl-handwritten-ocr.md — LLM-NAS HTR Watch (contrast; Atto NO-GO)
- @entities/tools/gcerretani-antenati.md — local image source for HTR
- @sources/gemini-italian-genealogy-research-tools-2026-07-21.md — Processetti / product companion
- @concepts/gpuology-genealogy-agent-kit.md — Approve gate = human review of candidates

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Extraction and Analysis of Structured Data from Historical Italian Civil Registers |
| **Author / origin** | Gemini Deep Research (Atto research prompt → inbox) |
| **Type** | Word docx |
| **Filename** | `Italian Civil Register Extraction.docx` |
| **sha256** | `d84e11b1483a4448599e288fa27fc54198d1219e23dfbe4ca9586a4b015b9498` |
| **Size** | 2,995,291 bytes |
| **Retrieved** | 2026-07-21 (inbox) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Italian Civil Register Extraction.docx` |
| **read_status** | read |

## Narrative

How to turn late-19th / early-20th-c *Stato Civile* images into **evidence packets** (candidate facts), not auto-merged trees. Covers dual-original + annual/decennial indices; Part I vs Part II (“S”) delayed/foundling regs; morphological layouts of *nascita* / *matrimonio* / *morte* (declaration date ≠ birth date; informants vs parents; witnesses; *annotazioni marginali* as multi-decade life-course overlays). Paleography/abbreviation pitfalls. Non-LLM HTR path: Transkribus (layout / P2PaLA, Italian Handwriting M1), eScriptorium + Kraken baselines — OOV proper nouns still need human review. Citation patterns: Antenati ARK + register year + *numero dell'atto*; FamilySearch DGS + image number.

**Wiki scope:** schema + HTR ops. No LLM-NAS training loops. No private pedigree.

## Snippets

> Birth preamble date is the **declaration**; birth hour/date often differs in the *ha dichiarato* clause. [Source: Italian Civil Register Extraction.docx]

> Marginalia collapse marriage/death/legitimation onto the birth page years later — vertical/diagonal script breaks naive layout HTR. [Source: Italian Civil Register Extraction.docx]

> Part II / “S” indices hold delayed registrations and foundlings — miss them and you invent “gaps.” [Source: Italian Civil Register Extraction.docx]

> Prefer Transkribus / eScriptorium+Kraken with human review; OOV surnames are the failure mode. [Source: Italian Civil Register Extraction.docx]
