---
title: FinBERT
type: entity
tags: [model, nlp, finance, sentiment]
keywords: []
related:
  - sources/3-10-cryptographic-research.md
  - sources/3-17-git-research-pt2.md
  - sources/3-29-research-4.md
  - entities/data-sources/gdelt.md
  - entities/data-sources/telethon.md
  - entities/data-sources/finnhub.md
  - entities/infrastructure/pgvector.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-10-cryptographic-research.md
- @sources/3-17-git-research-pt2.md
- @sources/3-29-research-4.md
- @entities/data-sources/gdelt.md
- @entities/data-sources/telethon.md
- @entities/data-sources/finnhub.md
- @entities/infrastructure/pgvector.md

## Raw Concept

Synthesized from 3 source(s) referencing this entity across the Cemini research corpus. Category: frameworks.

## Narrative

FinBERT is the BERT variant fine-tuned on financial text for three-class
sentiment (positive/negative/neutral). Cemini runs a vendored FinBERT
checkpoint locally for sentiment scoring across every text feed:

- **GDELT headlines** — tone-adjusted score orthogonal to GDELT's
  native tone.
- **Finnhub earnings-call transcripts** — per-paragraph sentiment
  rolled up by speaker (CEO vs CFO vs analyst) for quarterly
  surprise signals.
- **Telegram / Discord messages** — score first, persist, then
  downstream strategies subscribe by sentiment-bucket.
- **Cemini-internal research notes** — embedded via pgvector for
  retrieval; sentiment score used as a research-corpus filter.

The weights are small (~440MB) and run comfortably on CPU, fitting
the Hetzner zero-GPU constraint.

## Snippets

*(populate as source stubs are deep-read.)*
