---
title: "Square-root law of market impact — AAPL anonymous tape confirmation (arXiv 2606.24019)"
type: source
tags: [source, arxiv, market-microstructure, execution, k128]
keywords: [2606.24019, square-root law, market impact, AAPL, metaorder, Nasdaq TotalView-ITCH, Databento]
related:
  - concepts/square-root-law-market-impact.md
  - concepts/polymarket-bot-architecture.md
  - sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md
  - sources/arxiv-signal-adaptive-execution-2605-24242-2026-06-01.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
clusters: [market-microstructure, quant-finance, prediction-markets]
---

## Relations

- @concepts/square-root-law-market-impact.md — K128 synthesis
- @concepts/polymarket-bot-architecture.md — CLOB sizing discipline
- @sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md — optimal execution cluster

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Empirical Confirmation of the Square-Root Law of Market Impact in a U.S. Large-Cap Equity — A Reconstructed-Metaorder Study of AAPL Order Flow |
| **Authors** | Aniket Vasaikar (Independent Research) |
| **arXiv** | 2606.24019v1 (Jun 2026) |
| **sha256** | `d3d72075395f03cbecbf558ea81946d12c21f23ec9dcc31199b3a254735af772` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.24019-2606.24019v1-empirical-confirmation-of-the-squar.pdf` |
| **Retrieved** | 2026-06-24 (inbox) |
| **Read status** | read (abstract + methods headline) |

## Narrative

Tests **square-root law (SRL)** on **AAPL** using **Nasdaq TotalView-ITCH** via Databento (~178 trading days, Dec 2024–Aug 2025, ~0.5B events). Metaorders **reconstructed from anonymous tape** (no broker-tagged parents).

**Calibration:** I/σD = c (Q/VD)^½ with exponent fixed at ½.

**Headline results [TENTATIVE]:**

| Metric | Value |
|--------|-------|
| craw (bias-corrected ceff) | 0.69 (0.34) |
| Size tail exponent β | 1.54 ± 0.15 |
| vs linear impact | ΔAIC = 22 favors SRL |
| Sign shuffle null | directional impact 86% → 51% |
| Chronology scramble | 0/80 calibrations viable |
| Hurst (price) | 0.49 (diffusive) |
| Order-flow memory γ | 0.66 |

First SRL confirmation on **U.S. equity from anonymous L3 flow only** [TENTATIVE — author claim].

**Cemini steal:** PM/Kalshi **CLOB taker sizing** — impact scales ~√Q/V, not linear; informs ladder spacing and clip size on thin event books.

## Snippets

> "We test the square-root law (SRL) of market impact on a single U.S. large-capitalisation equity, Apple Inc. (AAPL), using the full Nasdaq TotalView-ITCH market-by-order feed over 178 trading days." [Source: arXiv:2606.24019 abstract (retrieved 2026-06-24)]

> "Shuffling trade signs collapses directional impact to chance (86% → 51%); and scrambling event chronology destroys the SRL (0 of 80 calibrations remain viable)." [Source: arXiv:2606.24019 abstract (retrieved 2026-06-24)]

> "A direct model comparison decisively prefers the square-root form over linear (ΔAIC=22) and logarithmic impact." [Source: arXiv:2606.24019 abstract (retrieved 2026-06-24)]

## Dead Ends

- Single-name U.S. equity — PM event contracts may have different V and toxicity; require PM-specific backtest before hard sizing rules.
