---
title: "arXiv 2607.15509 — LLM-Driven AutoML for Cross-Lingual Handwritten OCR"
type: source
tags: [source, arxiv, genealogy, ocr, htr, k177]
keywords: [2607.15509, handwritten-ocr, neural-architecture-search, arabic, persian, english, automl]
related:
  - concepts/computational-genealogy-archival-automation.md
  - entities/tools/transkribus.md
maturity: draft
read_status: read
created: 2026-07-20
updated: 2026-07-20
clusters: [k177-ingest]
---

## Relations

- @concepts/computational-genealogy-archival-automation.md — HTR / parish OCR contrast
- @entities/tools/transkribus.md — production HTR baseline (not LLM-NAS)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | 2607.15509 |
| **sha256** | `765a6339641055513ea9575af8891e488ae8e56b428ea1eb2c1d9c879f2ec225` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.15509-llm-driven-automl-for-cross-lingual-handwritten.pdf` |

## Narrative

Closed-loop **LLM-as-architect** NAS: GPT-5 / GPT-4o / Claude Sonnet 4 independently propose/refine CNN architectures for handwritten OCR on Arabic, English, Persian (30 trials/language). Claims >93% average test accuracy with real-time-capable inference; no human architecture selection. **Family-tree:** Watch-only method — contrast against Transkribus/HTR for Latin/cursive parish acts; do **not** auto-run frontier NAS loops on Antenati dumps (cost + ToS + script mismatch). Steal = automated architecture search *idea* for script-agnostic HTR eval harness, not a ship path.
