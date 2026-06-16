---
title: Tokenized fixed income — price-discovery admissibility
type: concept
tags: [concept, tokenization, fixed-income, price-discovery, measurement, crypto, k118]
keywords: [tokenized-treasuries, convenience-yield, basis-admissibility, affine-term-structure, nav-reconciliation]
related:
  - sources/arxiv-tokenized-fixed-income-admissibility-2606.13822-2026-06-16.md
  - concepts/tokenized-us-equities-onchain-basis-trade.md
  - concepts/quant-finance.md
maturity: draft
created: 2026-06-16
updated: 2026-06-16
---

## Relations

- @sources/arxiv-tokenized-fixed-income-admissibility-2606.13822-2026-06-16.md — K118 primary source
- @concepts/tokenized-us-equities-onchain-basis-trade.md — equities on-chain basis sibling
- @concepts/quant-finance.md — corpus hub

## Raw Concept

K118 arXiv 2606.13822 — on-chain tokenized Treasury "yield discount" is ill-posed until (1) measurement reconciliation and (2) **admissibility** (series carries market information) are established.

## Narrative

### Wrong order of questions

Practitioners often compute `APY_token − yield_Treasury` and call the gap "tokenization discount." Paper argues the gap mixes **four bookkeeping artifacts** (day-count, fees, amortized-cost lag, maturity mismatch) with any economic wedge.

### Admissibility test (falsifiable)

On reconciled basis series, require weak necessary conditions:

- Non-trivial **serial dependence** (not pure republication smoothness)
- **Idiosyncratic dispersion** consistent with slow-moving basis (not dominated by rounding/latency noise)

**2026 sample:** 1 of 4 products pass (~$6B universe).

### Admitted mapping structure

Minimal two-factor affine model: rates (RN measure, Treasury cross-section) + **orthogonal additive basis** (P measure). Features: ~quarterly mean reversion, March 2026 parity tightening, haircut sensitivity to persistence uncertainty.

**Cemini posture:** monitoring category for cross-asset / on-chain research — **do not** treat raw APY spreads as alpha without reconciliation. No prod pipeline unless tokenized Treasury marks enter `intel:*`.

## Snippets

> "Inference on it is inference on an ill-posed quantity." [Source: arxiv-2606.13822-price-discovery-admissibility-in-tokenized-fixed.pdf §1, on raw yield gap]
