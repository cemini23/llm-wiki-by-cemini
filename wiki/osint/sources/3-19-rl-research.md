---
title: Advanced Reward Architectures and Training Dynamics for Heterogeneous Multi-Agent Financial Reinforcement Learning
type: source
tags: [docx, rl-marl, portfolio-strategy, options-derivatives, market-microstructure, quant-finance, cemini-internal, mappo, sortino, action-masking, curriculum]
related:
  - concepts/market-microstructure.md
  - concepts/options-derivatives.md
  - concepts/portfolio-strategy.md
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
maturity: validated
read_status: read-skim
created: 2026-04-23
updated: 2026-04-26
clusters:
  - rl-marl
  - portfolio-strategy
  - options-derivatives
  - market-microstructure
  - quant-finance
  - cemini-internal
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub (Q 2026-04-27)
- @concepts/options-derivatives.md — Options & Derivatives corpus-index hub (Q 2026-04-27)
- @concepts/portfolio-strategy.md — Portfolio Strategy corpus-index hub (Q 2026-04-27)
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub (Q 2026-04-27)
- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- **Original title**: Advanced Reward Architectures and Training Dynamics for Heterogeneous Multi-Agent Financial Reinforcement Learning
- **Author(s)**: Cemini internal research / consultant brief (no attributed author)
- **Type**: DOCX (internal Cemini research report)
- **Location**: research for cemini/3_19 RL research.docx
- **Length**: ~4500 words
- **Retrieved**: 2026-04-23 (filename date 2026-03-19)
- **Read status**: read-skim
- **Primary cluster**: rl-marl (cross-home options-derivatives in partition — mismatch, see flags)
- **All clusters**: rl-marl, portfolio-strategy, options-derivatives, market-microstructure, quant-finance, cemini-internal

## Narrative

Internal Cemini research brief that synthesizes the state-of-the-art in MARL reward design, action masking, curriculum learning, non-stationarity handling, and execution realism — specifically tailored to the Cemini 5-agent heterogeneous MAPPO ensemble (5-min scalper, swing, Kalshi, Forex, crypto) running CPU-only on a 128GB Hetzner VPS alongside 26 Docker containers, with the explicit IP-sale buyer lens of a prop trading firm.

The spine is the Differential Sortino Ratio (DSoR) — a vectorized CPU-friendly online approximation of the Sortino ratio via EMA of returns and downside-squared deviations — positioned as the mandatory replacement for gross-PnL rewards because institutional buyers discount high-return/high-drawdown algos. It extends to (1) transaction cost + slippage penalties and "temporal coherence" bonuses to mitigate churning, (2) per-agent stratified γ discount factors (scalper γ≈0.95 half-life 14 steps, swing γ≈0.99), (3) PBRS (potential-based reward shaping) for the Kalshi agent to densify sparse terminal binary rewards using Redis-streamed intermediate probability shifts, (4) MaskedCategorical action masking with macro-regime/liquidity/event-window triggers, (5) static volatility-sequenced curriculum (2013-17 bull → 2018-19 sideways → 2008/Q1-2020 crisis), (6) context windowing (regime vector into observation) over MAML (explicitly disqualified for CPU-only), and (7) walk-forward fine-tuning with Redis hot-swap.

Relevant to Cemini as the de facto design doc for the MAPPO reward layer. Honest limit: this is an internal brief, not peer-reviewed research — claims are consulting-grade synthesis, and the "IP sale valuation" framing throughout is sales-oriented (not a neutral technical evaluation). Citations exist but the document's own rigor is that of a polished consulting deliverable, not an academic paper. Cross-paper consistency with other Cemini DOCXs should be audit-checked before locking the architecture.

## Key findings

- Differential Sortino Ratio (DSoR) formalized with a concrete vectorized TorchRL implementation (in-place EMA state updates, [-1,1] clamp for gradient stability) — directly actionable for the Cemini pipeline.
- Stratified discount factors per agent type with explicit half-life math (scalper γ=0.95 ≈14 steps ≈70 min, swing γ=0.99 ≈100 steps).
- PBRS for sparse Kalshi rewards using market-price deltas — preserves MDP optimality while densifying the signal.
- Action masking strategies tied to concrete triggers: VIX-regime thresholds, LOB top-level volume % caps, 24h pre-earnings blackout.
- Curriculum: static dataset sequencing (Polars-segmented chronological bins) strongly preferred over dynamic teacher-student (flagged as CPU-prohibitive for solo dev).
- MAML explicitly disqualified (second-order Hessians unviable on CPU-only VPS) — context windowing via regime vectors in the observation is the prescribed alternative.
- Walk-forward optimization pattern: frozen inference weights + parallel background fine-tune on 30-90d rolling window + Schemathesis validation + Redis hot-swap.

## Snippets

- **Section 1** — "Optimizing for [Sharpe/Sortino] directly in an online learning environment yields delayed, sparse reward signals that severely destabilize policy gradients."
- **Section 1.3** — concrete TorchRL DSoR class with in-place `self.A.add_(self.eta * delta_A)` updates, reward clamp `torch.clamp(reward, min=-1.0, max=1.0)`.
- **Section 6.1** — "MAML requires computing second-order derivatives (Hessians) through the unrolled optimization path. On a CPU-only Hetzner VPS lacking GPU parallelization, MAML will result in prohibitive training bottlenecks… MAML is strictly disqualified for this stack."
- **Section 3.1** — "The Scalper Agent (Hyperliquid/CCXT): Operating on immediate order book imbalances at a 5-minute frequency equates to over 105,000 steps annually" — justifies low γ.
