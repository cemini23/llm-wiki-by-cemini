---
title: "Rough volatility across assets (arXiv 2608.16749)"
type: source
tags: [arxiv, vol, xsp, k241]
keywords: [rough-volatility, Hurst, realized-variance, cross-asset]
related:
  - concepts/xsp-lane-trading-framework.md
  - concepts/market-memory-hurst-regime.md
  - sources/substack-rss-wublock-2026-08-18-miners-power.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
read_status: read
---

## Relations

- @concepts/xsp-lane-trading-framework.md — awareness only; **no named implementable rule**
- @concepts/market-memory-hurst-regime.md — H estimates across asset classes
- @sources/substack-rss-wublock-2026-08-18-miners-power.md — same-day wiki-only finance

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.16749, "Rough Volatility Across Assets" |
| Authors | Saad Mouti (University of New Haven) |
| Retrieved | 2026-08-18 |
| File | `arxiv-2608.16749-rough-volatility-across-assets.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.16749-rough-volatility-across-assets.pdf` |
| Type | q-fin.MF preprint |
| Dual-ID | **OSINT K241**. xsp awareness; **no xsp scp** (no named implementable rule). |

## Narrative

Gatheral et al. (2018) documented equity-index log-vol as fBM with \(H\sim 0.1\). This paper estimates \(H\) across **3,926 US equities**, **34 CME futures roots**, and options on **44 underlyings**. Realized volatility is rough in every asset class. Class medians: livestock 0.05; rates/FX/ag/energy/metals 0.08–0.10; single stocks 0.13; equity indices 0.20 (\(R^2\approx 0.98\)). ATM-skew identifies \(H\) only where the skew term structure is clean (equity indices 0.21–0.28); rates/FX skew regression fails (\(R^2\sim 0\)) even though RV stays rough. Mean-reversion contaminates the fractional OU second-moment estimator; lags up to ten days avoid it.

**No xsp scp.** There is no named implementable collar/roll/lane rule — just a cross-asset H map and a failure taxonomy. Wiki + Hurst-regime awareness only.

## Snippets

> "Realized volatility is rough in every asset class. Class medians range from 0.05 (livestock) … to 0.13 (single stocks) and 0.20 (equity indices)" [Source: arxiv-2608.16749 abstract]
