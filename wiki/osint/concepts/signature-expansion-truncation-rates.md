---
title: Signature expansion truncation and discretisation rates — what the error bounds buy you
type: concept
related:
  - sources/arxiv-convergence-rates-truncated-discretised-signature-expansions-2611.16087.md
  - concepts/options-derivatives.md
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

A signature model replaces a path by an infinite sum of iterated integrals. Every implementation must truncate the sum and discretise the path. This page records the published rates for both, so a future options-research lane can size the compute before it writes code.

Source: @sources/arxiv-convergence-rates-truncated-discretised-signature-expansions-2611.16087.md (Abi Jaber, Bastide, Pécheux, Rey; BNP Paribas RISK and CMAP).

## Narrative

### The two knobs

| Knob | Symbol | What it does |
|---|---|---|
| Truncation level | M | Discards signature words longer than M |
| Discretisation | N | Replaces the Brownian path by a piecewise-linear path on N steps |

The paper writes the target as X(M, N) with X(∞, ∞) the exact object, and controls both errors uniformly in the other parameter.

### The rates

Let **a** be the regularity of the test function: 1 for polynomials, the Hölder exponent otherwise. Let **ε** in (0, 1/2] measure the factorial decay left after accounting for coefficient growth.

| Error | Rate | Uniform in |
|---|---|---|
| Truncation, strong | (B^M / (M!)^ε)^a | N, and time |
| Truncation, weak | same | N |
| Discretisation, strong in Lp | N^(-a/2) | M |
| Discretisation, weak, polynomial g | N^-1 | M |

Three practical consequences:

1. **Truncation error decays faster than any geometric sequence.** The (M!)^ε term dominates. Small M is often enough.
2. **Discretisation error is a plain root-N law** in the strong sense. Refining the grid has a poor return; a weak-quantity target gets N^-1 instead.
3. **M and N are independent.** Set M from the accuracy target, then set N of order (M!)^(2ε) B^(-2M).

### The negative result

In the Itô–Taylor setting the weak error improves on the strong error. For Stratonovich signatures it does not. The exponent ε is sharp for the weak error too.

This matters because signature volatility models use Stratonovich signatures. A practitioner who imports an Itô–Taylor intuition will over-credit the method and under-budget the grid.

### Where the estimate extends

The bounds transfer to:

- errors in probability
- errors on distribution functions
- errors on coherent risk measures, including Expected Shortfall and Value-at-Risk

The density conditions these need apply to the target law only. The approximation needs no such condition. That is a useful asymmetry: you can bound a risk-measure error without knowing the approximation is well behaved.

### What it costs to use

The coefficient class requires |ℓ_v| ≲ (‖v‖!)^(1/2−ε). A model whose coefficients grow faster sits outside the theorem. The paper gives two boundary examples: a shifted Riemann–Liouville fractional Brownian motion still decays geometrically, while another boundary family diverges past a finite horizon.

### Status here

No Cemini lane prices with signatures. [OPEN QUESTION 2026-11-14] Nobody has measured whether a signature volatility model beats a plain parametric vol surface on the instruments the workspace trades.

The page exists so that a future evaluation starts from the published error budget instead of a guess.

## Snippets

> "The two parameters can therefore be chosen independently: M is set by the target accuracy, and N of order (M!)^(2ε) B^(-2M) balances the two terms." [Source: arxiv-2611.16087-convergence-rates-for-truncated-and-discretised.pdf p.3]
