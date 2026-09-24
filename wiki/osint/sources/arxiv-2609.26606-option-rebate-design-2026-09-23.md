---
title: "Liquidity Provision and Rebate Design in Option Markets"
type: source
tags: [arxiv, source, k270, options, market-making, quant]
keywords: [k270, market-making, rebates, HJB, make-take]
related:
  - concepts/k270-vol-quant-wave.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
read_status: skimmed
---

## Relations

- @concepts/k270-vol-quant-wave.md

## Raw Concept

| Paper | arXiv:2609.26606 |
| File | `arxiv-2609.26606-liquidity-provision-and-rebate-design-in-option.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.26606-liquidity-provision-and-rebate-design-in-option.pdf` |
| Authors | Samuel N. Cohen, Lyndon Drake, Zihan Guo, Christoph Reisinger |
| Retrieved | 2026-09-23 |
| Pages | 36 |
| Dual-ID | **OSINT K270** |
| sha256 | `d38ee1cca55f6f86fa2985fb9319535a282c5650ac97a2a9718bc7021fc98bad` |

## Narrative

The paper models the **nested optimisation problem** of market making and rebate design in option markets, and finds optimal strategies.

**Market-making problem.** A single market maker trades multiple European call options in a **local-stochastic volatility** option market. The maker uses both make and take strategies. The paper models make as **continuous controls** and take as **impulse controls**. The objective is to maximise net profit of option portfolio value plus cumulative rebate revenue, over all admissible make-take strategies. A **penalty on residual portfolio delta and vega** constraints the objective.

**Exchange problem.** The paper shows how an exchange can incentivise a market maker to improve market liquidity by setting suitable fee rebates. This resolves the exchange's own liquidity-attraction problem.

**Rebate design scheme.** The paper proposes a **three-step** rebate design scheme. The scheme has flexibility to accommodate specific liquidity targets imposed by an exchange.

**Validation.** Numerical results validate the effectiveness of the proposed scheme.

**Keywords:** market making, limit order book, make-take fees, rebate design, inventory risk, Hamilton–Jacobi–Bellman quasi-variational inequality.

**Cemini relevance:** options market-making and rebate-design model only. **FILE only. 0 product Integrate GO. No sizing change. No live order routing.**
