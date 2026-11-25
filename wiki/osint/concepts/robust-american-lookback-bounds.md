---
title: Robust American lookback bounds under martingale optimal transport
type: concept
maturity: draft
related:
  - sources/arxiv-robust-bounds-american-fixed-strike-lookback-2611.30980.md
  - concepts/options-derivatives.md
  - concepts/stochastic-calculus-foundations.md
updated: 2026-11-25
---

## Raw Concept

Question this page answers: how do you price a path-dependent American claim with no model, and why does the exercise region flip side?

From Xu, "Robust bounds for American fixed-strike lookback puts" (arXiv 2611.30980, 2026-11-23).

## Narrative

**The frame.** Martingale optimal transport (MOT) prices a derivative against the whole class of martingale models that repricing a finite set of observed options. The answer is a bound, not a point estimate. For American claims the price is a supremum over both models and stopping times, and those two suprema do not commute. That is what makes the American robust problem hard.

**The structural fact.** For a fixed-strike lookback, only one of four classical payoffs is genuinely American. At zero interest rate every lookback degenerates to its European value, because the discounted payoff is a sub-martingale. With positive `r`, the max-based call stays European-type: the running maximum is unbounded and arrives late. The min-based put is genuinely American: the running minimum is bounded below and attained early. [Source: arxiv-2611.30980-robust-bounds-for-american-fixed-strike-lookback.pdf p.3]

**Why the exercise region flips.** The standard American put exercises in the left tail, when the price is low. The American lookback put exercises in the right tail `{x >= x*}`. A high price locks the running minimum in place. Waiting then only forfeits the discount factor, so immediate exercise is optimal and captures the locked intrinsic value.

**The decomposition.** The continuation payoff splits exactly into a locked intrinsic part plus a "minimum-drop put". That reduces the two-period problem to a scalar MOT problem and gives a closed-form exercise criterion. The optimal coupling is the monotone martingale coupling, the third extremal coupling, with both shadow functions non-decreasing.

**Comparative statics.** The threshold rises with volatility, falls with the interest rate, and diverges as `r` tends to zero, where the American premium vanishes. For strikes at or above spot, the threshold is affine in the strike with a strike-independent shadow pair.

**Many marginals.** The right-tail structure survives any finite number of observed marginals. The coupling becomes a reflected iterated Azéma-Yor embedding, plus a mass-diffusion correction where an assumption fails. The correction is local, so the general problem collapses to iterating the three-marginal case.

**Use.** This is a pricing-discipline page, not a trading signal. Two takeaways carry: a model-free bound is the honest floor for a path-dependent American claim, and "is it American?" is a question about the running extremum and the interest rate, not about the label on the payoff.

[OPEN QUESTION 2026-11-25] The out-of-the-money strike regime, `K < s0`, is left to future work by the author. The two-branch decomposition does not carry over unchanged.
