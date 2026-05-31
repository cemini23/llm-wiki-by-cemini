---
title: "DRL portfolio SAC — global equity WFO (arXiv:2605.17307)"
type: source
tags: [source, arxiv, rl-trading, portfolio, sac, wfo, k48]
keywords: [soft-actor-critic, portfolio-allocation, walk-forward-optimization, nasdaq-100, nikkei-225, euro-stoxx-50, transaction-costs, hierarchical-dirichlet]
clusters: [rl-marl, portfolio-strategy]
related:
  - concepts/rl-marl-research.md
  - concepts/portfolio-strategy.md
  - sources/arxiv-fpilot-rl-trading-2605-12653.md
  - sources/arxiv-rmats-geopolitical-multi-agent-2605.25311.md

maturity: validated
read_status: skimmed
created: 2026-05-21
updated: 2026-05-30
---

## Relations

- @concepts/rl-marl-research.md — SAC + WFO methodology for financial RL
- @concepts/portfolio-strategy.md — dynamic allocation across global indices

## Raw Concept

- **Title**: Deep Reinforcement Learning Framework for Diversified Portfolio Management Across Global Equity Markets
- **Authors**: Kamil Kashif, Robert Ślepaczuk (University of Warsaw, Quantitative Finance Research Group)
- **Type**: arXiv preprint — arXiv:2605.17307
- **Submitted**: 2026-05-21 (per arXiv listing)
- **Retrieved**: 2026-05-21 (Tier-2 sweep `@sweeps/2026-05-21.md`, Tier-A)
- **Pages**: 67
- **Read status**: skimmed (abstract + introduction)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/2605.17307_drl-portfolio-sac-global-equity.pdf`

## Narrative

Develops **Soft Actor–Critic** for continuous portfolio weights in an MDP with transaction costs, turnover penalties, and diversification constraints. Compares five configurations (reward formulation, flat vs hierarchical Dirichlet policy, LSTM vs Transformer encoder). **Walk-forward optimization**: 16 OOS folds, 2003–2026, on Nasdaq-100, Nikkei 225, Euro Stoxx 50.

**Key finding [TENTATIVE — abstract only]**: RL competitive on risk-adjusted metrics mainly in **Euro Stoxx 50** (statistically significant abnormal returns there); **no** strategy beats Buy & Hold with HAC-robust excess returns across *all* markets. RL adds value in high-uncertainty regimes; cross-market ensemble improves risk-adjusted performance.

**Cemini relevance**: Benchmark reference for any CeminiSuite portfolio RL module — WFO discipline and explicit failure to beat B&H everywhere is a useful negative result for strategy promotion gates (MCPT / shadow-live).

## Snippets

> "The central hypothesis is only partially confirmed: no strategy achieves statistically significant excess returns relative to Buy & Hold under HAC-robust inference across all markets."
> — [Source: 2605.17307_drl-portfolio-sac-global-equity.pdf p.1]

> "Regime analysis reveals that RL adds the most value during periods of elevated uncertainty."
> — [Source: 2605.17307_drl-portfolio-sac-global-equity.pdf p.1]
