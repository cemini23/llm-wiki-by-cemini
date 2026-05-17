---
title: "Interpretable Machine Learning for Macro Alpha: A News Sentiment Case Study"
type: source
tags: [pdf, k49, quant-finance]
clusters: [quant-finance]
related:
  - concepts/quant-finance.md
  - entities/data-sources/gdelt.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/quant-finance.md — cluster hub for quantitative-finance research in the Cemini corpus
- @entities/data-sources/gdelt.md — GDELT data-source — interpretable-ML macro-alpha case study

## Raw Concept

- **Original title**: Interpretable Machine Learning for Macro Alpha: A News Sentiment Case Study
- **Author(s)**: Yuke Zhang (University of Pennsylvania; research conducted in personal capacity). arXiv:2505.16136v1, June 2025.
- **Type**: PDF
- **Location**: research for cemini/gdelt 4 3:29.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 12p
- **Read status**: deep-read
- **Primary cluster**: quant-finance
- **All clusters**: quant-finance

## Narrative

This paper builds an **interpretable ML framework to extract macroeconomic alpha from global news sentiment**. It ingests the **GDELT** Project's worldwide news feed and scores each article with **FinBERT**, a finance-pretrained BERT variant, then aggregates scores into a daily feature suite: mean tone, sentiment **dispersion**, news volume, Goldstein scores, plus lags and rolling statistics. These features drive an **XGBoost** classifier (benchmarked against a transparent logistic-regression baseline) to predict next-day return direction for three macro assets: **EUR/USD**, **USD/JPY**, and **10-year U.S. Treasury futures (ZN)**.

Out-of-sample testing uses 5-fold expanding-window cross-validation over Jan 2015–April 2025 (OOS period roughly 2017–April 2025), with realistic transaction costs included. The XGBoost strategy reports exceptional cost-adjusted performance: **Sharpe ratios of 5.87 (EUR/USD), 4.65 (USD/JPY), and 4.65 (ZN)**, with CAGRs exceeding 50% in FX and 22% in bonds, and results persisting across subperiods and cost assumptions. **SHAP** (Shapley Additive Explanations) attributions confirm that **sentiment dispersion and article impact** are the dominant predictive features, aligning the black-box model with economic intuition and supporting use in regulated environments.

**Cemini relevance**: directly quant-finance — a concrete, reproducible recipe (GDELT + FinBERT → daily sentiment indices → gradient-boosted next-day direction model) for generating macro alpha from publicly available alt-data, with interpretability built in. The Sharpe figures are headline-strong but warrant skepticism given known overfitting risk in expanding-window backtests; treat as a methodology template rather than a validated live-tradeable result.

## Snippets

> "Rigorous out-of-sample (OOS) backtesting ... demonstrates exceptional, cost-adjusted performance for the XGBoost strategy: Sharpe ratios achieve 5.87 (EUR/USD), 4.65 (USD/JPY), and 4.65 (Treasuries), with respective compound annual growth rates (CAGRs) exceeding 50% in Foreign Exchange (FX) and 22% in bonds." [Source: gdelt 4 3:29.pdf p.1]

> "Shapley Additive Explanations (SHAP) affirm that sentiment dispersion and article impact are key predictive features. Our findings establish that integrating domain-specific Natural Language Processing (NLP) with interpretable ML offers a potent and explainable source of macro alpha." [Source: gdelt 4 3:29.pdf p.1]
