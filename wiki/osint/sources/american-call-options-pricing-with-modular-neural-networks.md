---
title: American Call Options Pricing With Modular Neural Networks (Unnikrishnan 2024)
type: source
tags: [pdf, options-derivatives, neural-networks, options-pricing]
keywords: [American call options, modular neural network, MNN, FNN, Barone-Adesi-Whaley, binomial option pricing, RMSE, early exercise, AAPL, NVDA, QQQ]
related:
  - concepts/options-derivatives.md
  - entities/tickers/aapl.md
  - entities/tickers/nvda.md
  - entities/tickers/qqq.md
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/options-derivatives.md — Options & Derivatives corpus-index hub (Q 2026-04-27)
- @entities/tickers/aapl.md — AAPL is one of the three underlyings on which the MNN model is trained/evaluated
- @entities/tickers/nvda.md — NVDA options dataset; the MNN's largest RMSE gain over traditional models appears here
- @entities/tickers/qqq.md — QQQ options dataset; third evaluation underlying

## Raw Concept

- **Original title**: American Call Options Pricing With Modular Neural Networks
- **Author(s)**: Ananya Unnikrishnan
- **Type**: PDF (arXiv:2409.19706v1 [q-fin.CP], 29 Sep 2024)
- **Location**: research for cemini/American Call Options Pricing With Modular Neural Networks.pdf
- **Retrieved**: 2026-04-27
- **Length**: 16p
- **Read status**: deep-read
- **Cluster**: options-derivatives

## Narrative

This paper proposes a **Modular Neural Network (MNN)** for pricing American call options and benchmarks it against two traditional models — the Barone-Adesi & Whaley (B-AW) analytic approximation and the Cox-Ross-Rubinstein Binomial Option Pricing (BOP, 100 steps) — plus a plain Feed-forward Neural Network (FNN). The motivation: traditional models rest on rigid assumptions (e.g. constant volatility) and struggle with the non-linear early-exercise dynamics of American options.

**Method.** The MNN decomposes pricing into **six specialized modules**, each consuming a disjoint feature subset tied to a recognized pricing driver: (1) Intrinsic Value & Moneyness; (2) Time Value & Volatility; (3) Early Exercise & Dividend; (4) Liquidity & Market Conditions; (5) Macro-Economic & Sentiment; (6) Option Greeks & Interaction. Module outputs feed a final aggregation network. Inputs combine raw fields and engineered interaction terms (e.g. DTE × implied vol, gamma / DTE, delta × dividend yield). Data covers 2023 AAPL, NVDA and QQQ call options, enriched with Yahoo Finance dividends, FRED macro indicators (GDP growth, inflation, unemployment), and DTE-matched Treasury rates as the risk-free proxy. Hyper-parameters (1-3 layers; 32/64/128 neurons; ReLU/ELU/Tanh/Swish) were tuned via Keras Tuner on the AAPL set only, then reused for NVDA and QQQ.

**Results.** The MNN delivers the lowest RMSE and normalized-RMSE on all three underlyings, beating both traditional models and the FNN. AAPL: MNN RMSE 3.335 vs FNN 3.551 vs B-AW 8.632 / BOP 8.639. NVDA: 17.516 vs 19.563 vs ~41.7. QQQ: 8.052 vs 8.699 vs ~14.9. The modular structure also improves interpretability — each module maps to a well-understood financial concept — and supports parallel training.

**Relevance to Cemini.** A directly usable architecture pattern for the options-pricing layer of a quant/RL stack: modular feature grouping cleanly slots into a feature-vector design where Greeks, macro, and liquidity signals are already separated. The empirical lesson that the FNN nearly matches the MNN, and that tuning transferred across tickers, tempers the marginal gain against added engineering cost.

## Snippets

> "Experimental results indicate that the MNN model outperform both traditional models as well as a simpler Feed-forward Neural Network (FNN) across multiple stocks (AAPL, NVDA, QQQ), with significantly lower RMSE and nRMSE (by mean)."
> [Source: American Call Options Pricing With Modular Neural Networks.pdf p.1]

> "The MNN architecture divides the prediction process into six specialized modules, each responsible for a particular set of features, which represent the different factors that affect an option's price."
> [Source: American Call Options Pricing With Modular Neural Networks.pdf p.4]

> AAPL RMSE / nRMSE — MNN: 3.335 / 0.0849; B-AW: 8.632 / 0.2191; BOP: 8.639 / 0.2192; FNN: 3.551 / 0.0904.
> [Source: American Call Options Pricing With Modular Neural Networks.pdf p.12]
