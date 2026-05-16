---
title: Market Microstructure and Liquidity Analysis of QQQ ETF on 2024-08-01
type: source
tags: [pdf, market-microstructure, k49]
keywords: [market microstructure, liquidity, QQQ ETF, PIN, VPIN, probability of informed trading, quoted spread, effective spread, realized spread, Roll model, limit order book, Glosten-Harris, price impact, highfrequency R]
related:
  - concepts/market-microstructure.md
clusters: [market-microstructure]
maturity: draft
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure cluster hub

## Raw Concept

- **Original title**: Market Microstructure and Liquidity Analysis of QQQ ETF on 2024-08-01
- **Author(s)**: Unattributed student course project, FE570 (Financial Markets and Trading), Stevens Institute of Technology — references Dan Pirjol's FE570 Lecture 8 and FE570 liquidity-measures material; individual authors not named
- **Type**: PDF — graduate course project
- **Location**: research for cemini/Market Microstructure and Liquidity Analysis of QQQ ETF on 2024-08-01.pdf
- **Retrieved**: 2026-04-27
- **Length**: 10p
- **Read status**: deep-read
- **Cluster**: market-microstructure

## Narrative

A single-day microstructure study of the QQQ ETF (NASDAQ-100 tracker) on **2024-08-01**, a high-volume down day (QQQ fell ~2.5%) chosen specifically so volatile-regime liquidity could be examined. The dataset covers regular session hours (9:30–16:00) with **n = 246,796 trades**; the most active venues were ADF / Nasdaq High-Cap (102k trades), the Nasdaq exchange (52k) and NYSE Arca (32k). Analysis uses R's `highfrequency` package.

Liquidity was characterized via quoted, effective and realized spreads (`getLiquidityMeasures`). Average spreads were tight and venue-dependent — e.g. ADF quoted 0.030 / effective 0.078 / realized 0.088; the NAS exchange showed a **negative realized spread (−0.0067)**, a sign of adverse selection where market makers lose to informed flow post-trade. The realized spread fell as the post-trade lag rose (60–600s), consistent with cumulative price impact. The Roll model estimated the bid-ask spread (2c) at 0.111 — an overestimate — while the **improved Roll model** (incorporating trade signs via regression) gave 0.027, close to the effective spread on most venues. Roll-model annualized volatility for ADF came out at 41% (the paper notes the model overstates vol given the day's elevated activity). Limit-order-book imbalances swung between positive and negative but balanced over the day.

The headline finding is informed-trading intensity. The **PIN** (Probability of Informed Trading) model, estimated by maximum likelihood, gave **PIN = 0.455** — ~45.5% of trades plausibly informed. **VPIN** (volume-synchronized, 120s buckets) gave 0.424. A Glosten-Harris price-impact regression found per-unit signed-size impact λ ≈ 2.5e-07 (statistically significant but economically tiny — large trades barely move the mid) and a trade-direction component c ≈ 0.021 ($0.02). Conclusions: in volatile regimes the usual intraday-liquidity stylized facts (spreads narrowing into the close) break down; large trades are well-absorbed by liquidity providers; and QQQ on this day showed a high concentration of informed traders.

**Cemini relevance**: a concrete, reproducible template for ETF liquidity and informed-trading diagnostics — spread decomposition, Roll/improved-Roll calibration, PIN/VPIN, and Glosten-Harris price impact — directly relevant to CeminiSuite's execution-cost modeling and microstructure research. Student course project, so kept at `maturity: draft`.

## Snippets

> "The PIN value of 0.455 indicates that approximately 45.5% of the trades are assumed to be initiated by informed traders on 2024-08-01... By estimating the VPIN over a 120-second interval on the dataset, we obtained a value of 0.424, indicating that approximately 42% of traders are likely to be informed."
> — [Source: Market Microstructure and Liquidity Analysis of QQQ ETF on 2024-08-01.pdf p.7-8]

> "The Roll model estimates the bid-ask spread (2c) as 0.111, while the improved Roll model provides a better estimate of 0.027 which is very close to the effective spread on most exchanges."
> — [Source: Market Microstructure and Liquidity Analysis of QQQ ETF on 2024-08-01.pdf p.5]

> "What stands out is the realized spread of the NAS exchange, which is negative. This occurs when the future midpoint moves against the liquidity provider's position, meaning they effectively lose money after the trade... such as adverse selection, where market makers at the exchange are trading with informed traders."
> — [Source: Market Microstructure and Liquidity Analysis of QQQ ETF on 2024-08-01.pdf p.3-4]
