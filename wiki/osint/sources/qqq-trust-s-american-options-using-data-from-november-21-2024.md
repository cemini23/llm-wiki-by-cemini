---
title: 'FE620 — Pricing of Invesco QQQ Trust''s American Options (Nov 21 2024 data, Nov 29 2024 expiry)'
type: source
tags: [pdf, quant-finance, options-derivatives, k49]
keywords: [FE620, binomial tree, American options, QQQ, Monte Carlo, put-call parity, Greeks, delta hedging, option pricing]
related:
  - concepts/quant-finance.md
  - concepts/options-derivatives.md
clusters: [options-derivatives]
maturity: draft
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/options-derivatives.md — options & derivatives cluster hub
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub

## Raw Concept

- **Original title**: FE620: Pricing and Hedging — Pricing of Invesco QQQ Trust's American Options Using Data from November 21, 2024 for Expiration on November 29, 2024
- **Author(s)**: Stevens Institute of Technology, FE620 (Pricing and Hedging), Fall 2024 — Group #13 student project (individual authors not named)
- **Type**: PDF — graduate course project
- **Location**: research for cemini/QQQ Trust's American Options Using Data from November 21, 2024.pdf
- **Retrieved**: 2026-04-27
- **Length**: 36p
- **Read status**: deep-read
- **Cluster**: options-derivatives

## Narrative

A Stevens Institute FE620 graduate course project that prices American options on the Invesco QQQ ETF using a Cox-Ross-Rubinstein **binomial tree** as the primary model, with **Monte Carlo simulation** as an independent cross-check. Market data (QQQ spot, option quotes, Treasury rates) was pulled from Bloomberg Terminal, Yahoo Finance and the US Treasury website for the 24 trading days from 21 Oct to 21 Nov 2024; the target is the 29 Nov 2024 weekly expiry. Inputs: spot $505.40 (QQQ close 11/21/2024), implied volatility from Bloomberg, and a 4.20% risk-free rate (52-week T-bill). For each day the nine most-actively-traded calls and puts were retained.

Method: backward-induction on the binomial tree with early-exercise checks at each node. A convergence study over n = 5…1000 steps found prices stabilize by **n = 200**, which was adopted for all subsequent analysis. A put-call parity check showed computed C−P values lie consistently above the theoretical S₀−Ke^(−rT) line at a near-constant offset — attributed to volatility skew, dividends and transaction costs rather than arbitrage. Monte Carlo prices matched the binomial output with no statistically significant difference (t-test p = 0.9845 calls, 0.9781 puts). Versus actual market prices the binomial model tracked closely (t-test p = 0.3772) but ran consistently slightly high; the authors fit a constant correction factor (dividend-yield assumption + liquidity premium). Greeks were computed (call Δ 0.40–0.64, put Δ −0.37 to −0.60, Γ ≈ 0, Vega 29–31). A delta-hedge backtest (rebalance when |ΔΔ| > 0.1) beat the no-hedge book: mean PnL 1.537 vs 0.896 at lower stdev (1.436 vs 2.681).

**Cemini relevance**: a clean, end-to-end worked example of American-option pricing, model cross-validation and delta-hedge PnL accounting on QQQ — directly applicable to CeminiSuite's options-pricing and hedging modules, though it is a student project (kept at `maturity: draft`).

## Snippets

> "From Figure 7, we observe that the results converge almost entirely when n = 200... further increases in n (i.e., n > 200) yield diminishing returns. Therefore, all subsequent analyses and comparisons in this report are based on option prices calculated with n = 200."
> — [Source: QQQ Trust's American Options Using Data from November 21, 2024.pdf p.8]

> "The average value for Hedge_PnL is 1.537, and for No_Hedge_PnL is 0.896. Also, Hedge_PnL shows more stable performance with the standard deviation of 1.436 compared to No_Hedge_PnL that has a higher standard deviation of 2.681."
> — [Source: QQQ Trust's American Options Using Data from November 21, 2024.pdf p.19]

> "The differences between the two models are both minimal and statistically insignificant, with p-values for both the call and put options (0.9845 and 0.9781, respectively) well above the 0.05 significance threshold."
> — [Source: QQQ Trust's American Options Using Data from November 21, 2024.pdf p.12]
