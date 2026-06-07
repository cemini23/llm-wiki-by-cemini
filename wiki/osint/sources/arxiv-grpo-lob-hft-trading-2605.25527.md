---
title: "DeepSeekMath Meets Order Book — GRPO/GSPO for HFT directional trading (arXiv:2605.25527)"
type: source
tags: [source, arxiv, rl-trading, limit-order-book, grpo, gspo, hft, k87]
keywords: [order-flow-imbalance, group-relative-policy-optimization, group-sequence-policy-optimization, ppo, q-learning, directional-trading, deepseekmath, drawdown-control]
clusters: [rl-marl, market-microstructure]
related:
  - concepts/rl-marl-research.md
  - concepts/market-microstructure.md
  - concepts/order-book-pressure-ml-market-making.md
  - sources/stanford-ml-orderbook-mm-gr4-2017.md
  - sources/training-free-grpo-cai-2025.md
  - sources/arxiv-inference-scaling-llms-2605.19775.md
maturity: validated
read_status: skimmed
created: 2026-05-30
updated: 2026-06-07
---

## Relations

- @concepts/rl-marl-research.md — first finance adaptation of DeepSeek-style group-aware policy optimization (GRPO/GSPO)
- @concepts/market-microstructure.md — LOB order-flow imbalance (OFI) state; directional (not market-making) agent
- @concepts/order-book-pressure-ml-market-making.md — sibling LOB-feature lane: MM skew (GR4) vs directional RL (this paper)
- @sources/stanford-ml-orderbook-mm-gr4-2017.md — MM baseline comparison; RF OBP edge thin vs no-signal
- @sources/training-free-grpo-cai-2025.md — TF-GRPO in agent harness space; this paper applies group-normalized RL to trading episodes
- @sources/arxiv-inference-scaling-llms-2605.19775.md — sibling DeepSeek-family RL objective lineage (LLM training → trading transfer)

## Raw Concept

- **Title**: DeepSeekMath Meets Order Book: Group-Aware Policy Optimization for High-Frequency Directional Trading
- **Authors**: Sayak Chakrabarty (Northwestern), Souradip Pal (Purdue) — equal contribution
- **Type**: arXiv preprint — arXiv:2605.25527
- **Submitted**: 2026-05-26
- **Retrieved**: 2026-05-30 (Tier-2 sweep `@sweeps/2026-05-30.md`, Tier-A)
- **Pages**: 9
- **Read status**: skimmed (abstract + methods + results; no repeated-seed uncertainty reported)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/2605.25527_grpo-lob-hft-directional-trading.pdf`

## Narrative

Studies **directional** (not market-making) RL on limit-order-book microstructure using **Order-Flow Imbalance (OFI)** features as state. Compares tabular Q-learning, vanilla PPO, and DeepSeekMath-inspired **GRPO** (update-level group-normalized advantages over episode batches) and **GSPO** (sequence-level importance ratios). Assets: AAPL, AMZN, GOOG under a simplified spread-scaled reward backtest.

**Key finding [TENTATIVE — single-seed tables, authors flag no CIs]:** GRPO and GSPO report higher average PnL, profitability %, and lower max drawdown vs PPO and Q-learning across all three tickers; Q-learning/PPO often negative or near-zero returns with larger drawdowns. Authors explicitly frame results as **indicative** — fixed partition, no transaction-cost/slippage/latency layer, no repeated seeds.

**Cemini relevance:** Steal-from pattern for applying **group-aware policy surrogates** (already validated in LLM RLHF stack) to noisy episodic trading without a critic network. Pairs with `@entities/tools/hftbacktest.md` for LOB replay infrastructure. **Not** production-ready — directional-only, three mega-cap names, simplified execution. Useful as a benchmark design reference and as a signal that GRPO-style variance reduction may help MARL training stability on sparse market rewards.

## Snippets

> "To the best of our knowledge, this is among the first applications of DeepSeekMath-inspired Group Relative Policy Optimization (GRPO) and Qwen's Group Sequence Policy Optimization (GSPO) to high-frequency trading."
> — [Source: 2605.25527_grpo-lob-hft-directional-trading.pdf p.2]

> "Under this setup, GRPO and GSPO achieve higher average return and profitability and lower observed maximum drawdown than PPO and tabular Q-learning across all three tickers."
> — [Source: 2605.25527_grpo-lob-hft-directional-trading.pdf p.8]

> "Because we do not report repeated-seed uncertainty, bootstrap confidence intervals, or additional market regimes, the numerical gaps should be viewed as indicative rather than conclusive."
> — [Source: 2605.25527_grpo-lob-hft-directional-trading.pdf p.8]
