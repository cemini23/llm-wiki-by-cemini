---
title: Crypto pair trading with shielded DRL execution overlay
type: concept
tags: [concept, crypto, reinforcement-learning, statistical-arbitrage, k98]
keywords: [ppo, lstm, filter-then-rank, deterministic-shield, binance-futures]
related:
  - sources/arxiv-crypto-pair-trading-drl-shielded-2606-04574-2026-06-04.md
  - entities/data-sources/binance.md
maturity: draft
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- @sources/arxiv-crypto-pair-trading-drl-shielded-2606-04574-2026-06-04.md

## Raw Concept

arXiv:2606.04574 — hierarchical pair selection + RL execution inside deterministic risk bounds.

## Narrative

Classical pair trading fails in high-variance crypto when means/spreads are non-stationary. Paper proposes:

1. **Filter-then-rank** pair universe selection.
2. **Fixed Risk, Adaptive Mean** execution shell.
3. **PPO+LSTM** policy only where deterministic shields allow.

Statistical significance marginal at 5% on bootstrap — treat as **research reference**, not prod-ready alpha for Cemini core stack.

**Steal-from:** "neural policy anchored to robust statistical boundaries" — applicable metaphor for any future RL-assisted PM module with hard kill switches.

## Snippets

> "deterministic shielding … mitigates severe divergence risks"

[Source: arxiv-2606.04574-dynamic-multi-pair-trading-strategy-in-cryptocur.pdf p.1, retrieved 2026-06-04]
