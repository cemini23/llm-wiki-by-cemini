---
title: 'Enhancing Forex Forecasting Accuracy: The Impact of Hybrid Variable Sets in Cognitive Algorithmic Trading Systems'
type: source
tags: [pdf, deep-read, market-microstructure, quant-finance, ml-methods, forex, lstm, cemini-relevant]
keywords: [forex, EUR-USD, LSTM, fundamental variables, technical indicators, cognitive ATS, hybrid variable sets, support-resistance, Fibonacci, divergence, trading simulation]
related:
  - concepts/market-microstructure.md
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
  - concepts/recency-weighted-fundamental-data.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-04-30
clusters:
  - market-microstructure
  - quant-finance
  - ml-methods
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub
- @concepts/rl-marl-research.md — RL/MARL research hub; LSTM baselines, time-series forecasting context
- @concepts/recency-weighted-fundamental-data.md — Recency-weighted macro feature engineering concept page

## Raw Concept

- **Original title**: Enhancing Forex Forecasting Accuracy: The Impact of Hybrid Variable Sets in Cognitive Algorithmic Trading Systems
- **Author(s)**: Juan C. King, José M. Amigó (Centro de Investigación Operativa, Universidad Miguel Hernández, Elche, Spain)
- **Type**: Academic paper (arXiv preprint)
- **arXiv**: 2511.16657v1 [cs.AI], 20 Nov 2025
- **Location**: cemini-librarian:/opt/cemini-bulk/research/forex 1 4:4.pdf (22p)
- **Retrieved**: 2026-04-23
- **Read status**: deep-read

## Narrative

This paper presents a systematic experimental comparison of LSTM-based algorithmic trading models for EUR-USD, varying input feature sets across 10 configurations to determine whether fundamental macroeconomic data or technical indicators provide stronger predictive power. The answer is clear: **fundamental variables consistently outperform technical variables alone**. The best model (Model 7: tech + support/resistance + divergence + fundamental) achieves AUC_min = 0.66 with AUC_diff = 0.02. Model 2 (fundamental only) nearly matches at AUC_min = 0.65 — dramatically simpler while achieving the same ballpark.

### Architecture & methodology

- **Model**: LSTM recurrent neural networks. 180 configurations evaluated (10 variable sets × 18 hyperparameter combos).
- **Hyperparameter grid**: epochs {20, 40, 60}, LSTM layers {1, 4, 8}, look-back window {20, 30} days.
- **Target**: Binary directional index D(n, h=10) — a composite equally weighting (1) maximum attainable profit path, (2) maximum potential loss path, and (3) terminal price movement over a 10-day horizon. This accounts for intra-horizon stop-outs and take-profits rather than naive terminal-direction classification.
- **Training**: Jan 2012 – May 2023. **Out-of-sample test**: Jun 2023 – Mar 2024.
- **Overfitting metric**: AUC_diff = AUC_train − AUC_test, used as an explicit optimization constraint.

### Variable sets

**Fundamental (16 variables)**: 8 US macro series from Alpha Vantage + 8 Euro Area series from Eurostat — inflation rate (HICP), inflation contributions, annual/quarterly unemployment, net external debt (% GDP), government gross debt (EDP consolidated, annual + quarterly), debt by components. A "days since last publication" feature lets the LSTM weight each variable by recency, addressing the mixed-frequency problem (quarterly GDP alongside daily price).

**Technical (4 categories)**:
1. *Indicators/oscillators (11)*: SMA(20,55), EMA(20,55,200), Bollinger Bands(20,2), Ichimoku Cloud(9,26,52), RSI(6,12,14,24), MACD(12,26,9), ADX(14), Williams %R(14), ATR(14), Stochastic KDJ(14,3), Squeeze Momentum(20,50,200,2)
2. *Support/resistance*: 200-day rolling window → 10 non-overlapping 20-day sub-windows → local extrema → proximity clustering (δ = 4% of current price) → nearest-2-below and nearest-2-above
3. *Fibonacci retracement*: 23.6%, 38.2%, 50%, 61.8%, 78.6% + 127.2%, 161.8% extensions from 200-day rolling high/low
4. *Convergence/divergence*: Slope-product sign test between price trend lines and Squeeze Momentum trend lines (40-day rolling window), producing S_high and S_low binary states

### Key results

| Model | Features | MAX(AUC_min) | AVG(AUC_diff) |
|-------|----------|-------------|---------------|
| 0 | Price only | 0.56 | 0.06 |
| 1 | Technical only | 0.57 | 0.13 |
| 2 | **Fundamental only** | **0.65** | 0.04 |
| 3 | Tech + Fund | 0.64 | 0.15 |
| 7 | **Tech + S/R + Div + Fund** | **0.66** | 0.02 |
| 9 | All features | 0.62 | 0.19 |

Models without fundamentals (1, 4, 6, 8) achieve AUC_min ≤ 0.57 — barely above the price-only baseline. Adding fundamentals is the single largest performance lever. Counterintuitively, 8-layer LSTMs showed the lowest overfitting (AUC_diff = 0.08 vs 0.18 for 1-layer).

**Trading simulation (out-of-sample)**:
- Model 7 fixed-horizon long: 12W/2L, +69.64%, 85.71% win rate
- Model 7 fixed-horizon short: 6W/0L, +80.27%, 100% win rate
- Model 7 dynamic: 4 trades, 4 wins (100%), +4.38% aggregate
- All models performed better on short signals — LSTM more sensitive to EUR/USD decline patterns

### Cemini relevance

1. **Directional index formulation**: The D(n,h) composite that weights max-profit-path, max-loss-path, and terminal price equally is superior to simple binary up/down. Maps directly to how the Cemini Multi-broker EMS manages positions with stop-losses and take-profits active within the horizon.
2. **Recency-weighted fundamental data**: "Days since last publication" is lightweight and CPU-cheap — directly portable to the TimescaleDB + MAPPO pipeline for mixing quarterly macro with daily price data.
3. **Fundamental > Technical for 10-day horizon**: Challenges the bias toward pure price-action models. For Cemini's Kalshi macro-contract trading, fundamental variables may carry more signal than currently assumed.
4. **Conservative overfitting metric**: AUC_diff as an explicit optimization constraint (not just post-hoc) — the MAPPO retrain window could adopt a similar differential metric to gate hot-swap promotion.
5. **Deeper networks reduced overfitting**: 8-layer LSTMs had AUC_diff = 0.08 vs 0.18 for 1-layer — relevant for MAPPO feature extractor architecture decisions.

### Limitations

Single currency pair (EUR-USD); LSTM-only (no transformer/CNN comparison); fundamental data is backward-looking (published with lag); retail spreads assumed; 10-day horizon only.

## Snippets

> "This study confirms the central hypothesis that integrating both technical and fundamental variables within a unified prediction framework significantly enhances forecasting accuracy." [Source: forex 1 4:4.pdf p.13]

> "Models incorporating fundamental variables (particularly Models 2, 3, 5, 7, and 9) consistently outperformed those relying exclusively on technical analysis. This suggests that macroeconomic factors provide valuable signals that complement price-based technical indicators in forecasting EUR/USD movements." [Source: forex 1 4:4.pdf p.13]

> "Model 7 demonstrated exceptional performance across both long and short positions, achieving the highest win rates and substantial positive returns. All models exhibited superior capability in predicting downward movements (short positions), suggesting enhanced sensitivity to EUR/USD decline signals." [Source: forex 1 4:4.pdf p.12]

> "The directional index D(n,h) assigns equal weight to three critical price paths: the maximum attainable profit, the maximum potential loss, and the final price movement over the horizon. This design is particularly relevant for automated trading systems, where positions may be closed prior to the horizon's end due to profit-taking or stop-loss mechanisms." [Source: forex 1 4:4.pdf p.8]

> "Fundamental data exhibited significantly greater predictive power than technical indicators alone." [Source: forex 1 4:4.pdf p.13]

> "Is it possible to perform an analysis by a human agent that is not possible computationally? This is a question that we try to discuss in this paper from a scientific point of view." [Source: forex 1 4:4.pdf p.2]
