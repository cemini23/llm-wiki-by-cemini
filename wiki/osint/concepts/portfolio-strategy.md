---
title: Portfolio Strategy — Corpus Index
type: concept
tags: [concept, portfolio-strategy, allocation, research-index]
keywords: [portfolio, Sharpe, risk-parity, factor-model, mean-variance, Kelly, allocation, rebalanc, cemini-corpus]
related:
  - sources/3-10-agent-orchestration-research-audit.md
  - sources/3-10-engineering-audit.md
  - sources/3-17-competition-research.md
  - sources/3-17-git-research.md
  - sources/3-19-alternative-data-for-prediction-markets-research.md
  - sources/3-19-automated-trading-strategy-discovery-pipeline-research.md
  - sources/3-19-live-transition-checklist.md
  - sources/3-19-rl-research.md
  - sources/3-26-blog-re-2.md
  - sources/3-26-git-re.md
  - sources/3-26-link-re-3.md
  - sources/3-29-11.md
  - sources/3-29-research-5.md
  - sources/3-5-git-pt-2.md
  - sources/3-9-pm-research.md
  - sources/4-4-link-re.md
  - sources/4-5-links.md
  - sources/agent-7-4-4.md
  - sources/agent-8-4-4.md
  - sources/cyrpto-12-4-11.md
  - sources/github-analysis.md
  - sources/greeks-2-3-29.md
  - sources/greeks-5-3-29.md
  - sources/greeks-7-3-29.md
  - sources/loosening-your-collar-alternative-implementations-of-qqq-collars.md
  - sources/options-2-4-5.md
  - sources/rl-technical-audit-findings-3-9.md
  - sources/sort-1-4-3.md
  - sources/sort-5-4-3.md
  - sources/sort-6-4-3.md
  - sources/sort-7-4-3.md
  - sources/sortino-3-4-3.md
  - sources/sortino-4-4-3.md
  - sources/ssrn-3247865.md
  - sources/hedgge-fund-1-4-5.md
  - sources/stocks-2-4-5.md
  - sources/stocks-3-4-5.md
  - sources/toplogical-risk-parity.md
maturity: draft
created: 2026-04-27
updated: 2026-05-02
---

## Relations

- @sources/3-10-agent-orchestration-research-audit.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-10-engineering-audit.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-17-competition-research.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-17-git-research.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-19-alternative-data-for-prediction-markets-research.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-19-automated-trading-strategy-discovery-pipeline-research.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-19-live-transition-checklist.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-19-rl-research.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-26-blog-re-2.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-26-git-re.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-26-link-re-3.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-29-11.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-29-research-5.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-5-git-pt-2.md — Portfolio Strategy source in the Cemini research corpus
- @sources/3-9-pm-research.md — Portfolio Strategy source in the Cemini research corpus
- @sources/4-4-link-re.md — Portfolio Strategy source in the Cemini research corpus
- @sources/4-5-links.md — Portfolio Strategy source in the Cemini research corpus
- @sources/agent-7-4-4.md — Portfolio Strategy source in the Cemini research corpus
- @sources/agent-8-4-4.md — Portfolio Strategy source in the Cemini research corpus
- @sources/cyrpto-12-4-11.md — Portfolio Strategy source in the Cemini research corpus
- @sources/github-analysis.md — Portfolio Strategy source in the Cemini research corpus
- @sources/greeks-2-3-29.md — Portfolio Strategy source in the Cemini research corpus
- @sources/greeks-5-3-29.md — Portfolio Strategy source in the Cemini research corpus
- @sources/greeks-7-3-29.md — Portfolio Strategy source in the Cemini research corpus
- @sources/loosening-your-collar-alternative-implementations-of-qqq-collars.md — Portfolio Strategy source in the Cemini research corpus
- @sources/options-2-4-5.md — Portfolio Strategy source in the Cemini research corpus
- @sources/rl-technical-audit-findings-3-9.md — Portfolio Strategy source in the Cemini research corpus
- @sources/sort-1-4-3.md — Portfolio Strategy source in the Cemini research corpus
- @sources/sort-5-4-3.md — Portfolio Strategy source in the Cemini research corpus
- @sources/sort-6-4-3.md — Portfolio Strategy source in the Cemini research corpus
- @sources/sort-7-4-3.md — Portfolio Strategy source in the Cemini research corpus
- @sources/sortino-3-4-3.md — Portfolio Strategy source in the Cemini research corpus
- @sources/sortino-4-4-3.md — Portfolio Strategy source in the Cemini research corpus
- @sources/ssrn-3247865.md — 151 Trading Strategies compendium (Kakushadze & Serur, 2018); 550+ formulas across all asset classes with backtesting source code
- @sources/hedgge-fund-1-4-5.md — "Do Hedge Funds Prefer Safe Stocks?" (Cao, Green & Li, 2014): hedge funds prefer safe/low-volatility stocks; safety preference strongest during recessions. Informs defensive strategy weighting + regime-conditional allocation
- @sources/stocks-2-4-5.md — Portfolio Strategy source in the Cemini research corpus
- @sources/stocks-3-4-5.md — Atmaz & Basak (2021, J. Finance): no-dividend stocks have lower returns but higher vol/betas. Informs factor-construction + no-dividend-premium awareness in portfolio allocation
- @sources/toplogical-risk-parity.md — Portfolio Strategy source in the Cemini research corpus

## Raw Concept

Hub page for the portfolio-strategy cluster of the Cemini research corpus (36 sources at bootstrap from the Q 2026-04-27 sweep). Sources cover portfolio strategy-related research surfaced by the corpus-bootstrap cluster router (first-keyword-wins regex match against `portfolio-strategy` keyword set).

This page is a discovery index — it gives the tagged sources at least one inbound reference and makes the cluster navigable. Pages should be individually deep-read before their findings are promoted to entity or concept pages.

## Narrative

The portfolio-strategy cluster covers (non-exhaustively):

- Sharpe / Sortino / Calmar ratio optimization
- risk parity and equal-risk-contribution allocation
- mean-variance + Black-Litterman
- Kelly sizing under finite capital
- rebalance frequency and turnover control

Cluster membership is established by the corpus-bootstrap router's regex matching against `portfolio-strategy` keywords (see `scripts/bootstrap_extract.py` and `scripts/bootstrap_inbox.py`). False-positives are expected: first-keyword-wins routing matches surface-level vocabulary, not topical intent. Manual re-cluster on deep read is acceptable.

Cross-cluster overlap with other hubs is explicit (a single source can be tagged into multiple of: options-derivatives, market-microstructure, quant-finance, portfolio-strategy). Each hub lists every member regardless of overlap — the hubs are discovery aids, not partitioning categories.

## Snippets

*(None yet — index-only hub page.)*
