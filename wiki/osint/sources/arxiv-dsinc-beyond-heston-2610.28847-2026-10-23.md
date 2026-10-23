---
title: "DSINC beyond Heston — American options on non-affine stochastic volatility"
type: source
related:
  - concepts/k294-osint-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-23
---

## Raw Concept

Title: DSINC beyond Heston
Author: Andrey Itkin, NYU
Type: arXiv preprint (2610.28847), 22 Oct 2026
Inbox file: `research to be indexed/ccc/arxiv-2610.28847-dsinc-beyond-heston-the-3-2-and-other-non-affine.pdf`
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.28847-dsinc-beyond-heston-the-3-2-and-other-non-affine.pdf`
Retrieved: 2026-10-23
Read status: skimmed (abstract)

## Narrative

DSINC is a damped-sinc method for American option pricing. The paper extends it past affine Heston to one-factor stochastic volatility.

The collapse identity still holds. Damping between zero and one is admissible when the discounted spot is a nonnegative local martingale.

The 3/2 model has closed-form joint transforms in Kummer functions. Uncorrelated SABR has a Bessel form.

Tests cover 3/2, SABR, GARCH, and lognormal volatility. Each agrees with fine finite-difference benchmarks to within one basis point of the strike. Cost is comparable or lower, except the slower Hankel form of uncorrelated SABR.

Filed as a method reference. **No trade.**
