---
title: "Risk-Aware Financial Forecasting Enhanced by Machine Learning and Intuitionistic Fuzzy MCDM"
type: source
tags: [pdf, portfolio-strategy, ml-methods, time-series]
clusters: [portfolio-strategy, ml-methods, time-series]
related:
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @entities/components/kelly-cvar-risk-engine.md — risk engine covering options-derivatives and portfolio-strategy concepts

## Raw Concept

- Original title: Risk-Aware Financial Forecasting Enhanced by Machine Learning and Intuitionistic Fuzzy MCDM
- Authors: Turgay et al. (Turkish academic team)
- Affiliation: Turkish university (unnamed in extract — BIST 100 focus)
- Type: PDF, preliminary draft / preprint
- Location: research for cemini/sort 5 4:3.pdf
- Length: ~20 pages
- Retrieved: 2026-04-23
- Publication date: 2025 (preliminary draft manuscript)
- Read status: deep-read
- Primary cluster: time-series
- All clusters: portfolio-strategy, ml-methods, time-series

## Narrative

The authors combine a heterogeneous ML ensemble (XGBoost, LSTM, Graph Neural Network, TabNet) with an intuitionistic fuzzy MCDM (multi-criteria decision-making) layer for selecting among forecasting models on a BIST 100 Turkish defense-sector equity. Reported metrics: MAPE 3.03%, Sortino ratio 1.80 on the selected-model portfolio. The fuzzy MCDM is the novelty — instead of picking the best-Sharpe model, the framework scores models on multiple criteria (accuracy, drawdown, stability, robustness) with fuzzy weights and picks a Pareto-appropriate model per regime.

The paper reads as a preliminary draft: narrow single-ticker evaluation, modest sample window, no out-of-universe validation, and the fuzzy MCDM framing adds conceptual surface area without a clearly demonstrated lift over simpler model-selection methods (e.g., walk-forward Sharpe). The 1.80 Sortino on a single Turkish defense ticker during a period of active geopolitical narrative is hard to generalize.

Relevant as an idea source (fuzzy MCDM for model selection under multi-criteria pressure is uncommon in US quant literature) but the rigor bar is lower than the top papers in the batch. Use as a pointer to the MCDM literature for model-selection, not as an endorsement of the specific fuzzy construction.

## Key findings

- Ensemble: XGBoost + LSTM + GNN + TabNet with intuitionistic fuzzy MCDM for model selection.
- Reported MAPE 3.03% and Sortino 1.80 on BIST 100 defense ticker.
- Single-ticker, single-window evaluation — generalizability untested.
- Fuzzy MCDM contribution is conceptual; no clear delta vs. simpler selection baselines.
- Preliminary draft manuscript; rigor bar below the top batch papers.

## Snippets

- **results** — "MAPE 3.03%, Sortino 1.80 on the BIST 100 defense ticker evaluation window" — headline, with narrow scope caveat.
- **methodology** — Intuitionistic fuzzy MCDM scores models on multiple criteria simultaneously rather than single metric.
- **limitations** — Single-ticker scope and lack of out-of-universe validation.
