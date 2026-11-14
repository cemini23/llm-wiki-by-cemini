---
title: "Convergence rates for truncated and discretised signature expansions (arXiv 2611.16087)"
type: source
related:
  - concepts/signature-expansion-truncation-rates.md
  - concepts/options-derivatives.md
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Convergence rates for truncated and discretised signature expansions |
| Author | Eduardo Abi Jaber, Dorinel Bastide, Ronan Pécheux, Clément Rey (CMAP École Polytechnique; BNP Paribas RISK) |
| Type | arXiv preprint, math.PR |
| arXiv | 2611.16087v1, 11 Nov 2026 |
| Pages | 39 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.16087-convergence-rates-for-truncated-and-discretised.pdf` |
| Retrieved | 2026-11-14 |
| Read status | read |

## Narrative

### The question

A signature expansion writes a process as an infinite linear sum of iterated integrals of the driving path. Two approximations are always needed in practice. Truncate the signature at level **M**. Replace the Brownian path by a piecewise-linear path on **N** steps. The paper gives the error of both steps, explicitly in M, in N, and in the regularity of the test function.

### Main rates

| Quantity | Rate | Note |
|---|---|---|
| Truncation, strong error | about (B^M / (M!)^ε)^a | Geometric-or-faster decay; uniform in N and in time |
| Truncation, weak error | same exponent | No weak gain, unlike the Itô setting |
| Discretisation, strong error in Lp | N^(-a/2) | Uniform in M |
| Discretisation, weak error for polynomial g | N^-1 | Sharp in one dimension at grid points |
| Total error | sum of both terms | M and N chosen independently |

Here **a** is the regularity exponent of the test function g. It is 1 for polynomials and the Hölder exponent otherwise. **ε** in (0, 1/2] measures how much factorial decay survives the growth of the coefficients.

Because each bound is uniform in the other parameter, the two errors separate. Set M from the target accuracy. Set N of order (M!)^(2ε) B^(-2M) to balance the terms.

### The coefficient class

The paper defines a space of tensor coefficients satisfying |ℓ_v| ≲ (‖v‖!)^(1/2−ε). The condition is calibrated against the known (‖v‖!)^(-1/2) decay of signature moments. The class is stable under the usual algebraic operations. It contains non-Markovian processes: delay equations and Volterra processes. The Ornstein–Uhlenbeck process sits in both this class and the classical Itô–Taylor class.

### What the authors extend

The estimates transfer to three further error types:

- errors in probability
- errors on distribution functions
- errors on coherent risk measures, including Expected Shortfall and Value-at-Risk

The density conditions these need bear on the target law only, never on the approximation.

The applications are linear stochastic delay equations, Gaussian Volterra processes, and option pricing in signature volatility models. In the volatility model the price is not a known linear functional of the signature, but its logarithm is. The scheme therefore prices up to an arbitrarily small loss in ε.

### Why it matters here

The result tells an implementer how to budget compute in a signature-based model. It also states a negative result that matters: for Stratonovich signatures the weak error does not beat the strong error. A practitioner who assumed a weak-order gain from Itô–Taylor theory would over-credit the method.

[Source: arxiv-2611.16087-convergence-rates-for-truncated-and-discretised.pdf p.3]

### The honest limit

No Cemini project prices with signature volatility models today. The XSP and PM/Kalshi lanes use option-implied and realised vol surfaces, not signature expansions. This paper is a reference for a possible future options-research lane, not a wiring candidate.

The paper carries a disclaimer: the article represents the opinions of the authors, not the position of BNP Paribas. [Source: arxiv-2611.16087-convergence-rates-for-truncated-and-discretised.pdf p.1]

## Snippets

> "The exponent ε is sharp, even for the weak error and uniformly in N: in contrast with the Itô setting of Kloeden and Platen (1992), in general, no weak gain is possible for Stratonovich signatures." [Source: arxiv-2611.16087-convergence-rates-for-truncated-and-discretised.pdf p.3]

> "M is set by the target accuracy, and N of order (M!)^(2ε) B^(-2M) balances the two terms." [Source: arxiv-2611.16087-convergence-rates-for-truncated-and-discretised.pdf p.3]
