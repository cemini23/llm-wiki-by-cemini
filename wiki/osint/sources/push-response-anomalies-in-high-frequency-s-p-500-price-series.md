---
title: Push-response anomalies in high-frequency S&P 500 price series
type: source
tags: [pdf, market-microstructure, high-frequency, intraday-predictability, order-flow, spy]
keywords: [push-response, market mill, NBBO, SPY, intraday anomaly, price impact propagator, antisymmetry, symmetry decomposition, lag-resolved, liquidity replenishment, conditional response]
related:
  - concepts/market-microstructure.md
  - concepts/quant-finance.md
  - entities/tickers/spy.md
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub; this paper is a direct microstructure result (NBBO event-time, propagator, liquidity replenishment asymmetry)
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub; the push-response surface doubles as a tradable signal and a P&L risk-attribution tool
- @entities/tickers/spy.md — SPY is the sole instrument analyzed; ~2.6 billion NBBO events, Jan 2018 – Dec 2023

## Raw Concept

- **Original title**: Push-response anomalies in high-frequency S&P 500 price series
- **Author(s)**: Dmitrii Vlasiuk, Mikhail Smirnov — Department of Mathematics, Columbia University
- **Type**: PDF (arXiv:2511.06177v1 [q-fin.TR], November 2025)
- **Location**: research for cemini/Push-response anomalies in high-frequency S&P 500 price series.pdf
- **Retrieved**: 2026-04-27
- **Length**: 11p
- **Read status**: deep-read
- **Cluster**: market-microstructure

## Narrative

The paper tests whether consecutive intraday price changes in SPY — the most liquid U.S. equity ETF — are **conditionally non-random**, despite SPY appearing efficient under standard unconditional tests. It introduces a **push-response decomposition**: for each event-time lag L, a backward price increment (the "push", `p_t(L) = m_t − m_{t−L}`) is paired with the subsequent forward increment (the "response", `r_t(L) = m_{t+L} − m_t`), both standardized per-lag so conditional shapes are comparable across horizons.

**Method.** Data is ~2.6 billion NBBO mid-price events over ~1,512 regular trading days (Jan 2018 – Dec 2023), reconstructed from seven major exchanges, indexed in event time, winsorized at the 0.001% tails and cleaned of >\$1.50 intraday jumps. Pairs are formed only when t−L, t, t+L lie in the same session. Standardized pushes are binned on a fixed 320-bin grid spanning ±4σ; bins need ≥200 observations to count. The estimated object is the conditional surface `z̄_r(L, z_p) = E[z_r | z_p, L]` over short (1–5,000 ticks) and long (1k–500k ticks) lag families. The surface is split into a **symmetric** part S (magnitude-driven, sign-independent) and an **antisymmetric** part A (sign-driven drift), with a dominance index ρ(L) ∈ [−1,1] and a magnitude statistic M(L), uncertainty via bootstrap.

**Key results.** At short lags responses cluster near zero (high short-term efficiency); beyond ~5,000 ticks pronounced tails emerge — larger historical pushes increasingly correlate with non-zero conditional responses. A structured **ridge** appears for |z_p| ≈ 1–3 that *shifts with lag and push size*, meaning the most informative horizon depends on shock magnitude — state dependence that unconditional autocorrelation would hide. The surface reproduces the classical "market mill" reversal asymmetry at ~5k–150k lags. M(L) rises to a plateau then mildly increases; ρ(L) is strongly antisymmetric at short lags, dips negative at the short/long transition, then is weakly positive across a broad middle band. A robust finding: **large negative pushes are followed by stronger positive responses than equally large positive pushes**, consistent with asymmetric limit-order-book replenishment after sell-side shocks (bid depletion triggers faster, larger restoring adjustment).

**Why it matters for Cemini.** The push-response surface is a nonparametric estimate of the price-impact propagator that doubles as (i) a **lag-aware, variance-adjusted trade filter** — activate strategies only inside support-stable, post-cost predictive pockets — and (ii) a **risk-attribution tool** mapping realized P&L to lag-specific conditional responses. The standardized scale lets horizons be compared without raw-variance confounding. Authors note long implementations dominate short ones (shorting cost; symmetric regions favor positive responses for both push signs). [TENTATIVE — single paper; tradability claims rest on an illustrative analysis without explicit transaction-cost overlay]

## Snippets

> "We test the hypothesis that consecutive intraday price changes in the most liquid U.S. equity ETF (SPY) are conditionally non-random. ... for short lags (1-5,000 ticks), expected responses cluster near zero across most push magnitudes, suggesting high short-term efficiency; beyond that range pronounced tails emerge." [Source: Push-response anomalies in high-frequency S&P 500 price series.pdf p.1]

> "S captures magnitude-conditioned adjustment that does not depend on the sign of the push. A isolates sign-conditioned drift." — symmetric/antisymmetric decomposition `S(L,|j|) = ½[z_r(L,+j) + z_r(L,−j)]`, `A(L,|j|) = ½[z_r(L,+j) − z_r(L,−j)]`. [Source: Push-response anomalies in high-frequency S&P 500 price series.pdf p.4]

> "strong negative standardized pushes are followed, on average, by stronger positive conditional responses than the mirror positive pushes ... shocks that deplete the bid elicit a faster and larger restoring adjustment than shocks that deplete the ask, so the conditional response surface is steeper on the negative side." [Source: Push-response anomalies in high-frequency S&P 500 price series.pdf p.8]
