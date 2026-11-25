---
title: "Robust bounds for American fixed-strike lookback puts"
type: source
related:
  - concepts/robust-american-lookback-bounds.md
  - concepts/options-derivatives.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Robust bounds for American fixed-strike lookback puts |
| Author | YongQing Xu (Shenzhen Technology University) |
| Type | arXiv preprint, mathematical finance (q-fin.MF) |
| Location | `research to be indexed/osint/arxiv-2611.30980-robust-bounds-for-american-fixed-strike-lookback.pdf` |
| Retrieved | 2026-11-25 |
| arXiv | 2611.30980v1, 23 Nov 2026 |
| Pages | 28 |
| Read status | read |

## Narrative

### Question

The paper prices an American fixed-strike lookback put with no model. The price must hold for every martingale model that matches a finite set of observed option prices. This is the martingale optimal transport (MOT) method. Prior work covers European lookbacks and the standard American put. This paper combines the two.

### The payoff and why one case is trivial

The instrument pays `(K - m_t)^+` at exercise, where `m_t = min_{0<=u<=t} e^{ru} X_u` is the running minimum of the discounted price.

Two structural facts do most of the work. At zero interest rate, every classical lookback collapses to its European value, because the discounted payoff is a sub-martingale. With `r > 0`, the max-based lookback call stays European-type. The running maximum is unbounded and arrives late. Only the min-based put is genuinely American, because the running minimum is attained early and is bounded below. [Source: arxiv-2611.30980-robust-bounds-for-american-fixed-strike-lookback.pdf p.3]

### Main result: the exercise region is the right tail

For the standard American put, the optimal exercise region is the left tail: exercise when the price is low. Here it is the opposite. The optimal region is a right tail `{x >= x*}`. A high price leaves the running minimum locked, so waiting only loses the discount factor, and immediate exercise locks the intrinsic value. [Source: arxiv-2611.30980-robust-bounds-for-american-fixed-strike-lookback.pdf p.2]

The continuation value is split exactly into two parts: a locked intrinsic part plus a "minimum-drop put". That decomposition reduces the two-period problem to a scalar MOT problem and yields a closed-form exercise criterion.

The optimal coupling is the monotone martingale coupling. The author calls it the third extremal coupling, alongside the left-curtain and right-curtain couplings. Both of its shadow functions are non-decreasing.

### Comparative statics

The exercise threshold `x*` rises with volatility and falls with the interest rate. It diverges as `r` tends to zero, where the American premium vanishes. For `K >= s0`, `x*` is affine in the strike, with a shadow pair that does not depend on the strike. [Source: arxiv-2611.30980-robust-bounds-for-american-fixed-strike-lookback.pdf p.3]

### Extension to many marginals

The structure extends to any finite number of observed marginals. At every stage the optimal region is a right tail. The optimal coupling is a reflected iterated Azéma-Yor embedding of the observed marginals. When the reflected Oblój-Spoida assumption fails, the coupling carries a mass-diffusion correction. The author shows numerically that this correction is local, so the `n > 3` problem reduces to iterating the explicit `n = 3` correction. [Source: arxiv-2611.30980-robust-bounds-for-american-fixed-strike-lookback.pdf p.3]

Linear-programming experiments confirm the theory. The American premium of the call is identically zero over all tested strikes and rates. The put premium grows in both.

### Why it matters here

The result discipline for pricing: a model-free bound is the honest floor for a path-dependent American claim. The paper also gives a clean statement of when a lookback is "genuinely American", which is a pricing and hedging question, not a labelling one. No direct trading use. Value is in the bounds and in the decomposition technique.

## Snippets

> "At r > 0 the max-based fixed-strike lookback call remains European-type ... whereas the min-based fixed-strike lookback put is genuinely American." [Source: arxiv-2611.30980-robust-bounds-for-american-fixed-strike-lookback.pdf p.2]

> "The optimal exercise region is a right tail {x >= x*} — the opposite of the left-tail exercise region of the standard American put, because the running minimum ratchets only down." [Source: arxiv-2611.30980-robust-bounds-for-american-fixed-strike-lookback.pdf p.3]
