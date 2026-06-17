---
title: "Bayesian VAR + Elliptical Black-Litterman Portfolio DRL (arXiv 2606.09104, 2026)"
type: source
tags: [source, portfolio-optimization, regime-detection, drl, fat-tails, k107]
keywords: [bavar-bled, black-litterman, student-t, td3, regime-change, heavy-tails, sharpe-sortino]
related:
  - concepts/regime-conditioned-evaluation.md
  - concepts/gmm-factor-lens-regime-modeling.md
  - concepts/regime-adaptive-continual-portfolio-learning.md
  - sources/arxiv-portbench-llm-portfolio-2605-27887-2026-06-02.md
  - sources/arxiv-regime-vol-forecast-return-prediction-2606.09478-2026-06-15.md
  - sources/arxiv-ensemble-rl-classifier-models-2502-17518-2026-06-17.md
  - sources/arxiv-heuristic-portfolio-optimization-2606-12612-2026-06-17.md
maturity: draft
read_status: read
created: 2026-06-09
updated: 2026-06-17
clusters: [quant-finance, rl-marl, portfolio-strategy]
---

## Relations

- @concepts/regime-conditioned-evaluation.md — regime-aware evaluation discipline
- @concepts/gmm-factor-lens-regime-modeling.md — macro regime buckets (K58)
- @concepts/regime-adaptive-continual-portfolio-learning.md — sibling continual PO
- @sources/arxiv-portbench-llm-portfolio-2605-27887-2026-06-02.md — LLM portfolio benchmark
- @sources/arxiv-regime-vol-forecast-return-prediction-2606.09478-2026-06-15.md — K117 sibling regime vol/return framework
- @sources/arxiv-ensemble-rl-classifier-models-2502-17518-2026-06-17.md — K120 sibling portfolio RL ensemble
- @sources/arxiv-heuristic-portfolio-optimization-2606-12612-2026-06-17.md — K120 HPO theory sibling

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Addressing Market Regime Changes and Heavy-Tailed Returns in Portfolio Optimization via Bayesian VAR and Elliptical Black-Litterman |
| **Authors** | Mikriukov, Sun, Stefanidis, Su, Jiang |
| **arXiv** | 2606.09104 |
| **Location** | `.local/archives/research/` (laptop; historical librarian path in prior ingest) |
| **Retrieved** | 2026-06-09 |
| **Read status** | read (abstract + intro) |

## Narrative

**BAVAR-BLED** combines Bayesian-averaging VAR (multi-scale temporal features, regime-aware return/dispersion estimates) with elliptical Black-Litterman using Student-t (BLED) inside TD3 DRL. Transformer views + CNN risk-aversion modules modulate allocation.

DJIA 29 constituents, decade backtest: Sharpe **1.72**, Sortino **2.70**, total return **57.26%** vs SOTA baselines (paper claim — not independently replicated here).

**Cemini posture:** **REFERENCE** for equity sleeve stress/regime framing — not prod deploy without ArcticDB replication + regime disclosure per @concepts/regime-conditioned-evaluation.md [NEEDS VERIFICATION 2026-06-09].

## Snippets

> "The majority of existing DRL frameworks for PO fail to account for the well-documented fat-tailed nature of financial returns… and treat historical data homogeneously, without accounting for temporal importance." [Source: arxiv-2606-09104-addressing-market-regime-changes-and-heavy-taile.pdf §1]
