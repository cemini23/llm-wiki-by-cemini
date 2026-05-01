---
title: 'Cemini Financial Suite: Technical Intelligence & Competitive Architecture Analysis'
type: source
tags: [docx, deep-read, rl-marl, llm-agents, portfolio-strategy, market-microstructure, ml-methods, crypto, prediction-markets, cemini-internal, link-evaluation, multi-topic]
keywords: [CrewAI, MAS, crypto portfolio, variational reward factorization, MCDM, financial forecasting, LLM momentum, Chronos-Bolt, STOCKBENCH, graph learning FX, Wasserstein quantisation, SAMP-HDRL, market-adaptive ratio, Claude Hooks]
related:
  - concepts/market-microstructure.md
  - concepts/portfolio-strategy.md
  - concepts/rl-marl-research.md
  - concepts/quant-finance.md
  - sources/3-28-links-2.md
  - sources/4-4-link-re-2.md
  - sources/4-6-links.md
maturity: validated
created: 2026-04-23
updated: 2026-04-30
clusters:
  - rl-marl
  - llm-agents
  - portfolio-strategy
  - market-microstructure
  - ml-methods
  - crypto
  - prediction-markets
  - cemini-internal
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub
- @concepts/portfolio-strategy.md — Portfolio Strategy corpus-index hub
- @concepts/rl-marl-research.md — RL/MARL research hub
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub
- @sources/3-28-links-2.md — sibling K12 doc; agent-infra tool evaluations
- @sources/4-4-link-re-2.md — sibling K12 doc; 7 Target Domains
- @sources/4-6-links.md — sibling K12 doc; nvk/llm-wiki + AI governance papers

## Raw Concept

- **Original title**: Cemini Financial Suite: Technical Intelligence & Competitive Architecture Analysis
- **Author(s)**: Cemini internal (link-evaluation audit)
- **Type**: DOCX
- **Location**: cemini-librarian:/opt/cemini-bulk/research/4_4 link re.docx
- **Retrieved**: 2026-04-23
- **Read status**: deep-read

## Narrative

This Cemini-internal audit evaluates ~12 academic papers, systems, and repositories for integration into the Cemini Financial Suite. Evaluation follows the standard 8-section Cemini template (What it is / Architecture / Algorithms / Code & tooling / What they got wrong / IP sale relevance / Solo-dev filter / Conflicts). The constraint frame is a 128 GB RAM CPU-only Hetzner VPS (now known to be 7 GB — see @entities/infrastructure/hetzner.md K11 refresh). This doc skews toward academic papers and trading-systems research, complementing the agent-infra focus of @sources/3-28-links-2.md and the governance focus of @sources/4-4-link-re-2.md.

### Items evaluated

**CrewAI Crypto Portfolio MAS** — Multi-agent system using CrewAI to build and rebalance crypto portfolios. Architecture: hierarchical agent team (manager → researcher → trader → risk analyst). Relevance: validates the 5-agent LangGraph ensemble pattern. Solo-dev concern: CrewAI adds dependency weight; the architectural pattern is stealable without the framework. [TENTATIVE] — single-source evaluation.

**Variational Reward Factorization** — Academic method for decomposing RL rewards into interpretable factors using variational inference. Relevance: MAPPO reward shaping. If the Cemini RL agent's scalar reward can be factorized into components (trend following, mean reversion, volatility capture), credit assignment becomes auditable — directly supporting the glass-box IP-sale narrative. CPU-feasible: variational inference is lightweight compared to full Bayesian methods.

**MCDM Financial Forecasting** — Multi-Criteria Decision Making applied to financial time-series. Combines multiple forecasting models via a decision matrix with weighted criteria. Relevance: ensemble weighting for the 5-agent debate protocol. Instead of hard consensus, use MCDM to weight each agent's trade recommendation by its recent track record on similar market regimes.

**LLM-Conditioned Momentum** — Using LLM-derived sentiment scores to condition traditional momentum signals. Architecture: LLM sentiment → gating function → momentum factor (long-only if sentiment positive, neutral if negative). Relevance: directly applicable to Cemini's Kalshi macro-contract strategies. The gating pattern is CPU-cheap (LLM called once per rebalance, not per tick).

**Chronos-Bolt** (Apache-2.0) — **Top Steal**. Amazon's CPU-optimized time-series foundation model. Pretrained on ~80M time series; produces probabilistic forecasts (quantile outputs). Architecture: T5-small backbone (~8M params) with patch-based tokenization, optimized for CPU inference. Relevance: could serve as a pretrained feature extractor feeding the MAPPO model, reducing the need for hand-crafted technical indicators. Apache-2.0 license is GPL-compatible. CPU-optimized design fits the Hetzner constraint perfectly.

**STOCKBENCH** (Apache-2.0) — **Top Steal**. Standardized benchmark for stock trading agents. Composite Z-score metric: (Return_Z + MDD_Z + Sortino_Z) / 3. Evaluates agents across multiple market regimes (bull, bear, sideways, volatile). Relevance: provides a reproducible evaluation framework for the Cemini MAPPO agent. Currently, Cemini lacks a standardized backtesting benchmark — strategy performance is evaluated ad-hoc. Apache-2.0 license.

**Graph Learning FX** — Graph neural networks applied to currency pairs as a relational graph (nodes = currencies, edges = exchange rates). Relevance: EUR-USD doesn't trade in isolation — it's affected by EUR-GBP, USD-JPY, etc. A lightweight graph convolution layer could capture cross-currency spillover effects. CPU feasibility: modest graph size (~30 currency nodes).

**Market-Adaptive Ratio** — Proposed replacement for the Sharpe ratio that adapts to market regime. Traditional Sharpe penalizes upside volatility equally with downside; market-adaptive ratio uses a regime-switching denominator. Relevance: better risk-adjusted metric for the Cemini backtesting pipeline, especially for strategies that perform asymmetrically across bull/bear regimes.

**Wasserstein Quantisation** — Uses Wasserstein distance for deterministic replay buffer sampling in RL. Instead of uniform random sampling from the experience replay buffer, Wasserstein quantisation selects a representative subset that preserves the distribution. Relevance: MAPPO experience replay on CPU. If the replay buffer grows large (months of tick data), Wasserstein-based compression could maintain distribution fidelity while reducing memory footprint. [TENTATIVE] — theoretical; no implementation benchmarked against uniform sampling in the paper.

**SAMP-HDRL** — Hierarchical Deep RL with tensor-based state-action masks for portfolio management. Architecture: high-level policy selects asset allocation weights; low-level policy executes individual trades with action masking (no short-selling, position limits). Relevance: action masking maps directly to the Nomotic AI "pre-action authorization" pattern discussed in @sources/4-6-links.md. Hierarchical decomposition reduces the action space dimensionality.

**Claude Hooks** — Claude Code hook system for pre/post-tool-execution callbacks. Relevance: could enforce Pydantic validation on agent outputs before they reach the execution layer. Overlaps with the Nomotic Execution Service concept in @sources/4-6-links.md.

**open-multi-agent** — General-purpose multi-agent framework. Overlaps substantially with LangGraph and existing Cemini agent architecture. Snippets-only.

### Promotion candidates

1. **Chronos-Bolt** — strongest Promotion candidate in this batch. Pretrained CPU-optimized time-series model with Apache-2.0 license. Deserves its own entity page as a Cemini-relevant ML model. Could replace or supplement hand-crafted technical indicators in the MAPPO feature pipeline.

2. **STOCKBENCH** — standardized trading-agent benchmark. Deserves a concept stub. Fills a gap: Cemini currently has no reproducible backtesting benchmark.

3. **Wasserstein Quantisation** — mention in @concepts/rl-marl-research.md as a replay-buffer compression technique. Snippets-level for now; promote if an implementation is tested.

4. **Market-Adaptive Ratio** — mention in @concepts/quant-finance.md as a Sharpe-ratio alternative. Snippets-level pending implementation.

### Cross-document patterns

This doc shares the Cemini-internal evaluation template with three sibling docs (@sources/3-28-links-2.md, @sources/4-4-link-re-2.md, @sources/4-6-links.md). Consistent across all four: (a) Python 3.12 monoculture enforcement, (b) solo-dev filter rejects multi-service/GUI architectures, (c) IP-sale relevance lens prioritizes deterministic auditable systems over black-box neural approaches, (d) "128 GB RAM" constraint frame is now known stale (K11: 7 GB actual).

## Snippets

> "Chronos-Bolt: Amazon's CPU-optimized time-series foundation model. Pretrained on ~80M time series; produces probabilistic forecasts (quantile outputs). T5-small backbone (~8M params) with patch-based tokenization, optimized for CPU inference. Apache-2.0. Could serve as a pretrained feature extractor feeding the MAPPO model." [Source: 4_4 link re.docx §Chronos-Bolt]

> "STOCKBENCH: Standardized benchmark for stock trading agents. Composite Z-score: (Return_Z + MDD_Z + Sortino_Z) / 3. Evaluates agents across multiple market regimes (bull, bear, sideways, volatile). Provides a reproducible evaluation framework the Cemini MAPPO agent currently lacks." [Source: 4_4 link re.docx §STOCKBENCH]

> "Wasserstein Quantisation: deterministic replay buffer sampling via Wasserstein distance. Selects a representative subset preserving distribution, potentially reducing memory footprint for MAPPO experience replay on CPU." [Source: 4_4 link re.docx §Wasserstein Quantisation]

> "Market-Adaptive Ratio: Sharpe replacement using regime-switching denominator. Better risk-adjusted metric for strategies performing asymmetrically across bull/bear regimes." [Source: 4_4 link re.docx §Market-Adaptive Ratio]

> "LLM-Conditioned Momentum: LLM sentiment → gating function → momentum factor (long-only if positive, neutral if negative). CPU-cheap — LLM called once per rebalance, not per tick." [Source: 4_4 link re.docx §LLM-Conditioned Momentum]
