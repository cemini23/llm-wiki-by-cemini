---
title: Options & Derivatives — Corpus Index
type: concept
tags: [concept, options-derivatives, derivatives, research-index]
keywords: [options, derivatives, implied-volatility, delta-hedging, rough-volatility, variance-swap, cemini-corpus]
related:
  - concepts/derivative-informed-operator-learning.md
  - sources/arxiv-derivative-informed-operator-learning-2606-05900-2026-06-07.md
  - sources/3-19-on-chain-alpha-research.md
  - sources/3-19-rl-research.md
  - sources/3-19-trading-options-data-research.md
  - sources/autonomous-ai-agents-for-option-hedging.md
  - sources/deep-hedging-with-reinforcement-learning.md
  - sources/3-26-blog-re-2.md
  - sources/3-29-research-5.md
  - sources/4-14-re.md
  - sources/american-call-options-pricing-with-modular-neural-networks.md
  - sources/cost-effective-algorithmic-trading-api-stack.md
  - sources/loosening-your-collar-alternative-implementations-of-qqq-collars.md
  - sources/mixed-fractional-models.md
  - sources/qqq-trust-s-american-options-using-data-from-november-21-2024.md
  - sources/crypto-13-4-11.md
  - sources/github-analysis.md
  - sources/greeks-10-3-29.md
  - sources/greeks-2-3-29.md
  - sources/greeks-3-3-29.md
  - sources/greeks-4-3-29.md
  - sources/greeks-6-3-29.md
  - sources/greeks-8-3-29.md
  - sources/greeks-9-3-29.md
  - sources/greeks1-3-29.md
  - sources/options-4-5.md
  - sources/rough-martingale-optimal-transport.md
  - sources/the-three-dimensional-decomposition-of-volatility-memory.md
  - sources/black-scholes-iv-explicit-schadner-2026.md
  - sources/gemini-dr-wave3-link-eval-2026-04-28.md
  - sources/pta-metric-anchoring-ssrn-4549819.md
  - sources/mit-quant-bible.md
  - sources/arxiv-deep-hedging-delta-corrections-2605.21696.md
maturity: draft
created: 2026-04-27
updated: 2026-05-30
---

## Relations

- @sources/3-19-on-chain-alpha-research.md — Options & Derivatives source in the Cemini research corpus
- @sources/3-19-rl-research.md — Options & Derivatives source in the Cemini research corpus
- @sources/3-19-trading-options-data-research.md — Options & Derivatives source in the Cemini research corpus
- @sources/autonomous-ai-agents-for-option-hedging.md — deep-read 2026-05-16; shortfall-aware RL (QLBS/RLOP) option hedging benchmarked against Black-Scholes / jump-diffusion / Heston; IVRMSE shown to be a weak proxy for after-cost hedging quality
- @sources/deep-hedging-with-reinforcement-learning.md — deep-read 2026-05-16; RL actor-critic (GAE) overlay hedging equity-index option exposure using option-surface + macro state features
- @sources/arxiv-deep-hedging-delta-corrections-2605.21696.md — K87: TD3 delta haircut vs daily BS; downside-shortfall reward; symbolic distillation; 2022 regime fragility
- @sources/3-26-blog-re-2.md — Options & Derivatives source in the Cemini research corpus
- @sources/3-29-research-5.md — Options & Derivatives source in the Cemini research corpus
- @sources/4-14-re.md — Options & Derivatives source in the Cemini research corpus
- @sources/american-call-options-pricing-with-modular-neural-networks.md — Options & Derivatives source in the Cemini research corpus
- @sources/cost-effective-algorithmic-trading-api-stack.md — Options & Derivatives source in the Cemini research corpus
- @sources/loosening-your-collar-alternative-implementations-of-qqq-collars.md — K49 deep-read; QQQ collar (protective put + covered call) strategy, credit-crisis + out-of-sample performance
- @sources/mixed-fractional-models.md — K49 deep-read; boundary inference (LAN + score tests at H=3/4) for mixed fractional Brownian / OU volatility models
- @sources/qqq-trust-s-american-options-using-data-from-november-21-2024.md — K49 deep-read; QQQ American-option pricing via binomial tree + Monte Carlo validation
- @sources/crypto-13-4-11.md — Options & Derivatives source in the Cemini research corpus
- @sources/github-analysis.md — Options & Derivatives source in the Cemini research corpus
- @sources/greeks-10-3-29.md — Options & Derivatives source in the Cemini research corpus
- @sources/greeks-2-3-29.md — Options & Derivatives source in the Cemini research corpus
- @sources/greeks-3-3-29.md — Options & Derivatives source in the Cemini research corpus
- @sources/greeks-4-3-29.md — Options & Derivatives source in the Cemini research corpus
- @sources/greeks-6-3-29.md — Options & Derivatives source in the Cemini research corpus
- @sources/greeks-8-3-29.md — Options & Derivatives source in the Cemini research corpus
- @sources/greeks-9-3-29.md — Options & Derivatives source in the Cemini research corpus
- @sources/greeks1-3-29.md — Options & Derivatives source in the Cemini research corpus
- @sources/options-4-5.md — Options & Derivatives source in the Cemini research corpus
- @sources/rough-martingale-optimal-transport.md — Options & Derivatives source in the Cemini research corpus
- @sources/the-three-dimensional-decomposition-of-volatility-memory.md — Options & Derivatives source in the Cemini research corpus

## Raw Concept

Hub page for the options-derivatives cluster of the Cemini research corpus (23 sources at bootstrap from the Q 2026-04-27 sweep). Sources cover options and derivatives-related research surfaced by the corpus-bootstrap cluster router (first-keyword-wins regex match against `options-derivatives` keyword set).

This page is a discovery index — it gives the tagged sources at least one inbound reference and makes the cluster navigable. Pages should be individually deep-read before their findings are promoted to entity or concept pages.

## Narrative

The options-derivatives cluster covers (non-exhaustively):

- American/European option pricing models
- stochastic volatility (rough-vol, fractional models)
- delta / gamma / vega hedging frameworks
- variance swaps and volatility-of-volatility
- regulatory + audit applications of derivative-pricing math

Cluster membership is established by the corpus-bootstrap router's regex matching against `options-derivatives` keywords (see `scripts/bootstrap_extract.py` and `scripts/bootstrap_inbox.py`). False-positives are expected: first-keyword-wins routing matches surface-level vocabulary, not topical intent. Manual re-cluster on deep read is acceptable.

Cross-cluster overlap with other hubs is explicit (a single source can be tagged into multiple of: options-derivatives, market-microstructure, quant-finance, portfolio-strategy). Each hub lists every member regardless of overlap — the hubs are discovery aids, not partitioning categories.

## Snippets

*(None yet — index-only hub page.)*
