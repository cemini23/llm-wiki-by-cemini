---
title: Leveraged ETF options — variance drag and conditional pricing
type: concept
maturity: draft
related:
  - sources/arxiv-conditional-gamma-letf-options-2611.22604.md
  - concepts/options-derivatives.md
  - concepts/vix-first-joint-spx-vix-calibration.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: why is a leveraged ETF option not a simple strike rescale of the index option, and how can the surface be built quickly?

Built from one paper, Chen et al. (JPMorganChase, arXiv 2611.22604, 2026-11-17).

## Narrative

**The identity.** A leveraged ETF targets a constant daily multiple `beta` of the underlying index return. After deterministic financing and carry are removed, the forward-normalised log-return is exact:

`RL = beta * RS - gamma * IT`, where `gamma = beta(beta-1)/2` and `IT` is realised integrated variance.

The drag term is path-dependent. A single remapped strike cannot carry that state dependence, so strike remapping drifts in the wings.

**Three constructions.**

1. *First-order strike remapping.* Closed form, simple, and it discards state dependence.
2. *Conditional Gamma.* Condition on the terminal underlying return. Then only the drag is random. Three one-dimensional forward PDEs under a calibrated local-volatility model give the conditional mean and variance of integrated variance. A Gamma law matched to those moments keeps realised variance non-negative and gives a closed-form price.
3. *Joint-law PDE.* Two-dimensional, no distributional assumption, used as the benchmark.

A shifted-Gamma variant also matches the conditional third moment; it helps most for inverse products at longer maturities. A Gamma-mixture extension covers the full skewness range that stays compatible with non-negative realised variance.

**Results.** On S&P 500 and Nikkei 225 surfaces, the conditional-Gamma smile tracks the benchmark closely at every leverage tested, including the wings. One full LETF smile takes 0.85 to 1.42 seconds against 197 to 224 seconds for the benchmark, a 158- to 236-fold speed-up. Against listed TQQQ quotes, the smile sits inside the bid-ask at most strikes.

**Out of scope in the paper.** Discrete rebalancing, tracking error, jumps and random fees.

**What transfers.** The identity and the conditioning idea. Any product with path-dependent drag needs a state-dependent correction, and a single rescaled strike hides it. For a single-account options lane this is a pricing sanity check, not an execution edge: when a LETF option looks rich or cheap versus a naive rescale, the difference is often drag, not edge.
