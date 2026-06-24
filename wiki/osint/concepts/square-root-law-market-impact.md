---
title: Square-root law of market impact — sizing and execution
type: concept
tags: [concept, market-microstructure, execution, k128]
keywords: [square-root law, SRL, market impact, metaorder, optimal execution, Q-over-V]
related:
  - sources/arxiv-square-root-law-aapl-2606.24019-2026-06-24.md
  - concepts/polymarket-bot-architecture.md
  - sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md
  - sources/arxiv-signal-adaptive-execution-2605-24242-2026-06-01.md
  - concepts/active-project-research-routing.md
maturity: draft
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- @sources/arxiv-square-root-law-aapl-2606.24019-2026-06-24.md — K128 AAPL anonymous-tape confirmation
- @concepts/polymarket-bot-architecture.md — CLOB clip sizing
- @sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md — execution cluster sibling

## Raw Concept

What is the empirical relationship between metaorder size and price impact, and how should retail bots size clips on thin books?

## Narrative

The **square-root law (SRL)** states impact scales as **I/σD ∝ (Q/VD)^½** — sublinear in participation rate Q/V. Vasaikar (2026) confirms on **AAPL** from reconstructed anonymous Nasdaq ITCH metaorders with structural null tests (sign shuffle, chronology scramble).

### Operator checklist

1. **Sublinear sizing:** doubling clip size increases impact by ~√2, not 2× — ladder bots should space levels accordingly.
2. **Chronology matters:** impact lives in **signed, time-ordered** flow — randomizing order destroys SRL (86% → 51% in paper null).
3. **Book depth V:** thin PM books → higher impact per share; size down when V drops.

### Cemini surfaces

| Surface | Application |
|---------|-------------|
| pm-kalshi-bot | CLOB taker clip caps, ladder spacing |
| XSP killer | Equity execution sibling (Lane A sizing) [secondary] |

## Snippets

> "Impact as I/σD = c (Q/VD)^1/2 with the exponent fixed at the universal value 1/2." [Source: arXiv:2606.24019 abstract (retrieved 2026-06-24)]

> "A direct model comparison decisively prefers the square-root form over linear (ΔAIC=22)." [Source: arXiv:2606.24019 abstract (retrieved 2026-06-24)]

## Dead Ends

- AAPL prefactor c ≈ 0.34 (bias-corrected) does not transfer to PM without venue-specific calibration.
