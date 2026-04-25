---
title: Finnhub
type: entity
tags: [data-source, equities, news, fundamentals]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - entities/frameworks/finbert.md
  - entities/data-sources/gdelt.md
  - concepts/publishers-exclusion.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-19-compliance-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @entities/frameworks/finbert.md
- @entities/data-sources/gdelt.md
- @concepts/publishers-exclusion.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: data-sources.

## Narrative

Finnhub is a commercial market-data API providing equities quotes,
fundamentals, earnings transcripts, company news, and sentiment. Cemini
uses Finnhub as a paid layer on top of IEX (via Alpaca) for:

- **Earnings transcript sentiment** — transcripts fed to FinBERT for
  quarterly surprise-augmentation signals.
- **Company news corpus** — news items cross-referenced with GDELT events
  to filter noise.
- **Fundamentals snapshots** — quarterly metrics used by the
  replacement-cost valuation concept on portfolio positions.

The compliance research notes Finnhub's per-user commercial license as a
minor deal-killer candidate during IP-sale due diligence — the acquiring
firm would need to re-negotiate the license under their entity — so the
milestone ledger tracks Finnhub-dependent feature flags separately from
fully-open-data features.

## Snippets

*(populate as source stubs are deep-read.)*
