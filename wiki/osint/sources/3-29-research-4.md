---
title: 'Cemini Financial Suite: Targeted Extraction Audit and Architecture Report (3/29 #4)'
type: source
tags: [docx, cemini-internal, rl-marl, llm-agents, quant-finance, prediction-markets, infrastructure, alt-data]
related:
  - concepts/quant-finance.md
  - entities/data-sources/gdelt.md
  - entities/frameworks/finbert.md
  - entities/platforms/kalshi.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
clusters:
  - rl-marl
  - llm-agents
  - quant-finance
  - prediction-markets
  - cemini-internal
  - infrastructure
  - alt-data
---

## Relations

- @concepts/quant-finance.md — Quantitative Finance corpus-index hub (Q 2026-04-27)
- @entities/data-sources/gdelt.md
- @entities/frameworks/finbert.md
- @entities/platforms/kalshi.md

## Raw Concept

- Original title: Cemini Financial Suite — Targeted Extraction Audit and Architecture Report (#4)
- Authors: Cemini internal authoring team (unsigned)
- Affiliation: Cemini internal
- Type: DOCX, internal technical audit
- Location: research for cemini/3_29 research 4.docx
- Length: long-form
- Retrieved: 2026-04-23
- Publication date: 2026-03-29
- Read status: deep-read
- Primary cluster: alt-data
- All clusters: rl-marl, llm-agents, quant-finance, prediction-markets, cemini-internal, infrastructure, alt-data
- Flag: **cemini-internal.**

## Narrative

Two main technical threads: (1) a **GDELT + FinBERT pipeline** for news-event-driven signal generation — GDELT for event stream, FinBERT for financial sentiment scoring, feeding into a signal layer for Kalshi and equity strategies; (2) evaluation of **6 Kalshi bot repos** on GitHub, with fit judgments for possible adoption or inspiration.

The GDELT + FinBERT pipeline is a well-documented engineering recipe: ingestion via GDELT v2 API, sentiment scoring via FinBERT on event headlines, aggregation to contract-level features, feeding forecasting/strategy code. No empirical backtest numbers in the doc, but the pipeline design is reasonable and matches external literature.

The 6 Kalshi bot repo evaluations are useful as a current landscape survey: what's publicly available for Kalshi automation as of late March 2026. Most are rejected for quality or licensing; a couple are marked "evaluate further."

Typical Cemini internal audit — not research, but a curated engineering assessment with actionable takeaways.

## Key findings

- GDELT + FinBERT pipeline design for news-driven signal generation.
- 6 Kalshi bot repos evaluated on GitHub with fit verdicts.
- Most Kalshi repos rejected for quality/licensing; few flagged for further evaluation.
- No empirical backtest numbers provided.
- Internal engineering audit; actionable pipeline recipe.

## Snippets

- **pipeline** — "GDELT v2 → FinBERT sentiment → contract-level feature aggregation → strategy signal" — the news pipeline.
- **Kalshi repo scan** — 6 bots evaluated; most rejected; actionable shortlist produced.
- **format** — Internal engineering audit; no empirical benchmarks.
