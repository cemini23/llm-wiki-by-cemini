---
title: A Controlled Comparison of Deep Learning Architectures for Multi-Horizon Financial Forecasting
type: source
tags: [pdf, rl-marl, portfolio-strategy, quant-finance, ml-methods, time-series, crypto]
related:
  - concepts/portfolio-strategy.md
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-04-26
clusters:
  - rl-marl
  - portfolio-strategy
  - quant-finance
  - ml-methods
  - time-series
  - crypto
---

## Relations

- @concepts/portfolio-strategy.md — Portfolio Strategy corpus-index hub (Q 2026-04-27)
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub (Q 2026-04-27)
- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- Original title: A Controlled Comparison of Deep Learning Architectures for Multi-Horizon Financial Forecasting
- Authors: Nabeel Saidd (lead author per extraction)
- Affiliation: arXiv preprint (academic independent)
- Type: PDF, research paper (arXiv preprint)
- Location: research for cemini/agent 8 4:4.pdf
- Length: ~25+ pages
- Retrieved: 2026-04-23
- Publication date: 2025
- Read status: deep-read
- Primary cluster: time-series
- All clusters: rl-marl, portfolio-strategy, quant-finance, ml-methods, time-series, crypto

## Narrative

The paper runs a large, seed-controlled comparison of nine deep-learning architectures for multi-horizon financial forecasting: DLinear, N-HiTS, PatchTST, iTransformer, Autoformer, TimesNet, LSTM, TimeXer, and ModernTCN. 918 total experimental runs across multiple assets, horizons, and random seeds. The central analytical move is an ANOVA-style variance decomposition over the runs: **architecture explains 99.90% of performance variance while random seed explains only 0.01%**, which is a strong signal that architecture choice dominates stochastic noise in this setup.

Headline ranking: **ModernTCN wins with mean rank 1.333**, beating all transformer variants including PatchTST and iTransformer. DLinear (the simple linear baseline) is competitive on short horizons, consistent with prior "transformers are not always better" findings. Autoformer and TimesNet lag. LSTM is middling.

This is one of the cleaner pieces of evidence in the batch: real controlled experiment, proper seed replication, explicit variance decomposition. The implication for Cemini is concrete — *default to ModernTCN* (or a ModernTCN+DLinear ensemble) for the multi-horizon forecasting block rather than transformer-family models, and the ranking is robust across seeds so A/B gating can be bypassed for initial deployment.

## Key findings

- 918 controlled runs across 9 DL architectures, multiple assets and horizons.
- ModernTCN ranked #1 (mean rank 1.333) across the evaluation matrix.
- Architecture explains 99.90% of performance variance; seed explains 0.01%.
- DLinear competitive on short horizons — simple baseline is not a strawman.
- Autoformer and TimesNet consistently lag; PatchTST strong but not top.

## Snippets

- **results** — "ModernTCN achieves a mean rank of 1.333 across our 918 experimental runs" — the concrete recommendation.
- **variance decomposition** — "Architecture accounts for 99.90% of variance vs. 0.01% for random seed" — strong claim that the ranking is not seed-sensitive.
- **discussion** — DLinear's strong short-horizon showing reinforces prior work cautioning against transformer-first defaults for time-series forecasting.
