---
title: "Beyond strike remapping — conditional-Gamma pricing of leveraged ETF options"
type: source
maturity: draft
related:
  - concepts/leveraged-etf-options-pricing.md
  - concepts/options-derivatives.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Beyond Strike Remapping: Conditional-Gamma Pricing of Leveraged ETF Options under Local Volatility |
| Author | Guolin Chen, Jiang Zhou, Richard Ma, Xia Sheng, Anson Tse, Terry Wei (JPMorganChase) |
| Type | arXiv preprint, q-fin.CP |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.22604-beyond-strike-remapping-conditional-gamma-pricin.pdf` |
| Retrieved | 2026-11-22 |
| arXiv | 2611.22604v1, 17 Nov 2026 |
| Pages | 37 |
| Read status | read |

## Narrative

Leveraged ETF (LETF) options trade off the LETF volatility surface. That surface is hard to build, because path-dependent variance drag makes it inconsistent with the underlying index smile. After financing and carry are removed, the forward-normalised LETF log-return is exactly

`RL = beta * RS - gamma * IT`, with `gamma = beta(beta-1)/2` and `IT` the realised integrated variance. [Source: arxiv-2611.22604-beyond-strike-remapping-conditional-gamma-pricin.pdf p.1]

The paper compares three ways to build the LETF surface:

1. Closed-form first-order strike remapping. Simple, but it discards state dependence in the drag.
2. A new conditional-Gamma method. It conditions on the terminal underlying return, so only the drag term is random. Three one-dimensional forward PDEs under a calibrated local-volatility model give the conditional mean and variance of integrated variance. A Gamma law matched to these moments keeps realised variance non-negative and prices the option in closed form.
3. A two-dimensional joint-law PDE. It makes no distributional assumption and serves as the benchmark.

A shifted-Gamma variant also matches the conditional third moment. It helps most for inverse products at longer maturities. A Gamma-mixture extension covers the full skewness range that stays compatible with non-negative realised variance.

Results: on S&P 500 and Nikkei 225 surfaces the conditional-Gamma smile tracks the benchmark closely at every leverage tested, including the wings where strike remapping drifts. A full LETF smile takes 0.85 to 1.42 seconds against 197 to 224 seconds for the benchmark. That is a 158- to 236-fold speed-up. Against listed TQQQ quotes, the smile sits inside the market bid-ask at most strikes. [Source: arxiv-2611.22604-beyond-strike-remapping-conditional-gamma-pricin.pdf p.1]

Caveats the authors state: discrete rebalancing, tracking error, jumps and random fees are outside the model.

For a single-account options lane, the transferable idea is the identity and the conditioning trick, not the JPMorgan calibration. Any product with path-dependent drag has a state-dependent correction. A single remapped strike hides it.

## Snippets

> "A full LETF smile takes 0.85–1.42 seconds against 197–224 seconds for the benchmark, a 158- to 236-fold speed-up." [Source: arxiv-2611.22604-beyond-strike-remapping-conditional-gamma-pricin.pdf p.1]
