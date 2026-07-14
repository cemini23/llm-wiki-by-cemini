---
title: "Volatility in Prediction Markets: A Structural Approach (2607.08199)"
type: source
tags: [source, arxiv, prediction-markets, kalshi, volatility, k163]
keywords: [DR-AS, Wright-Fisher, Glosten-Milgrom, GARCH, Kalshi panel, interval score]
related:
  - concepts/prediction-market-structural-volatility-dr-as.md
  - entities/platforms/kalshi.md
  - concepts/proper-betting-clob-prediction-markets.md
  - concepts/polymarket-bot-architecture.md
maturity: validated
read_status: deep-read
created: 2026-07-14
updated: 2026-07-14
clusters: [k163-ingest, pm-kalshi]
---

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.08199](https://arxiv.org/abs/2607.08199) |
| **Authors** | Weiye Xi, Ciamac C. Moallemi, Mallesh Pai, Shouqiao Wang |
| **sha256** | `b7c09feeaebbbbbe663ab190b65ff9615a35d577d039b008760994ec19087184` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.08199-volatility-in-prediction-markets-a-structural-ap.pdf` |
| **Phase-0** | `scripts/adopt_k163_phase0.sh` (REFERENCE — math steal, no install) |

## Relations

- @concepts/prediction-market-structural-volatility-dr-as.md — K163 concept
- @entities/platforms/kalshi.md — empirics on Kalshi hourly panel Aug 2021–Apr 2026

## Narrative

Binary PM prices are bounded probabilities with known deadlines — plain ARCH/GARCH miss that structure. **DR-AS** = Wright-Fisher deadline-resolution `p(1-p)/τ` + Glosten-Milgrom adverse-selection `K·ν(V)·s²/4`. On ~880k Kalshi contract-hours, structural specs beat plain GARCH; **GARCH+DR-AS** best overall. Volatility peaks near 50¢, rises near resolution; sports more jump-like, economics smoother. Category-specific refits do **not** systematically help OOS — pooled structure transfers.

**Steal for pm-kalshi-bot:** use `p(1-p)/τ` + spread×volume as sizing / MM risk gates; prefer structural vol over raw return GARCH on binaries. **No code install** — REFERENCE mental model + brief.

## Snippets

> "Plain ARCH/GARCH benchmarks are dominated by structural specifications; combining the structural model with residual GARCH dynamics gives the best overall forecasts." [Source: 2607.08199 abstract]
