---
title: "Markov-chain & Hidden-Markov regime-switching models for trading"
type: concept
tags: [concept, quant-finance, regime-switching, markov-chain, hidden-markov-model, signal-generation, k49]
keywords: [markov-chain, transition-matrix, chapman-kolmogorov, stationary-distribution, hidden-markov-model, baum-welch, viterbi, regime-switching, walk-forward-backtest, maximum-likelihood-estimator, hmmlearn]
related:
  - sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md
  - concepts/quant-finance.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/macro-weather-regime.md
  - concepts/prediction-market-statistical-arbitrage.md
maturity: draft
created: 2026-05-16
updated: 2026-05-18
---

## Relations

- @sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md — @RohOnChain post this page synthesizes
- @concepts/quant-finance.md — corpus-index parent cluster
- @concepts/regime-conditioned-evaluation.md — sibling: evaluating strategies *conditioned on* regime; this page is about *detecting* the regime
- @concepts/macro-weather-regime.md — sibling regime concept (macro/weather state framing)
- @concepts/prediction-market-statistical-arbitrage.md — K52: its cross-venue predictive signal uses a rolling Markov transition matrix (the same transition-matrix machinery this page documents)

## Raw Concept

Synthesized from the @RohOnChain post in `posts.docx` (May 2026): a first-principles framework for using Markov chains and Hidden Markov Models to model market regimes and generate trading signals. The page captures the method; it deliberately strips the post's "win every trade" marketing framing.

## Narrative

### Why Markov chains over independence models

Naive probability models assume each step is independent of history. Markets are not independent — and pure independence produces impossible paths (the post's example: a portfolio of loans where a "current" loan jumps to "90+ days late" in one month). A Markov chain introduces **local conditional dependence**: the next state depends only on the *current* state.

**Markov property**: `P(Xₙ₊₁ = s | X₀,…,Xₙ) = P(Xₙ₊₁ = s | Xₙ)`. This makes the model simultaneously tractable and expressive — it captures the essential dependency structure without tracking full history.

### Observable Markov chain — the pipeline

1. **State space** — must be mutually exclusive and collectively exhaustive. Common definitions: trend regimes (Bull/Bear/Sideways via rolling-return thresholds), volatility regimes, liquidity regimes, credit regimes (risk-on/off). Starter model: 3-state trend regime, 20-day rolling return vs ±2% thresholds.
2. **Transition matrix** — entry `P(i,j)` = probability of moving state i→j in one step; each row sums to 1. Maximum-likelihood estimator is just counting: `P̂(i,j) = Count(i→j) / Count(i→any)`.
3. **Multi-step forecasts** — Chapman-Kolmogorov: the n-step transition matrix is `Pⁿ` (matrix power). `[Pⁿ]ᵢⱼ` is the probability of being in j after n steps starting from i.
4. **Stationary distribution** — as n→∞ the distribution converges to a fixed `π` solving `π = πP`, independent of start state. This is the long-run baseline; a strategy betting heavily on a regime the stationary distribution says is rare is carrying tail risk.
5. **Signal generation** — at each step take the one-step-ahead vector `P[current_state]`; `signal = bull_prob − bear_prob` maps to a position (long / short / flat / scaled).
6. **Walk-forward backtest** — re-estimate the transition matrix at each step using *only* historical data available then. This prevents lookahead bias and is the difference between a realistic and a fantasy backtest. Reports Sharpe, max drawdown, annual return.

### Hidden Markov Models — when the regime is latent

The observable Markov chain has a flaw: you never *observe* the regime — you reverse-engineer it from price. A bear regime building up via quiet institutional repositioning, not yet visible in price, is invisible to hand-labeled states.

A **Hidden Markov Model** treats the regime as an unobservable hidden state; only noisy returns are observed; each hidden state emits returns from its own distribution (bull = positive mean / low variance, bear = negative mean / high variance). Two algorithms:

- **Baum-Welch** — estimates all parameters (transition matrix, per-regime emission distributions, start probabilities) from the return sequence alone, no labels. Forward-backward iteration to convergence. Finds a *local* maximum → run from multiple random starts, keep highest log-likelihood.
- **Viterbi** — given a fitted model, decodes the single most-likely hidden-state sequence behind the observed returns.

`hmmlearn`'s `GaussianHMM` implements both. Signal generation is identical to the observable case: posterior `predict_proba` → multiply by `transmat_` → `next_probs[bull] − next_probs[bear]`.

**Emission-variable choice is the highest-leverage decision**: returns alone carry limited regime information. Returns + realized volatility + credit spreads + VIX term structure give a much richer signal. Domain knowledge compounds the mathematics here.

### The three breaking assumptions

1. **Markov property** — markets sometimes show longer-range dependence; a 6-month-old trend may transition differently than a fresh one. Mitigation: expand the state space with duration information (increases complexity).
2. **Time homogeneity** — transition probabilities are assumed constant; they are not (Bull→Bear in 2008 ≠ 2021). Mitigation: rolling-window re-estimation — shorter windows adapt faster but are noisier; longer windows are stable but lag regime changes.
3. **Estimation-data sufficiency** — the MLE converges only with enough observed transitions. Rule: every transition-matrix cell should be estimated from ≥20–30 observed transitions, else merge states or extend history.

### Cemini relevance

- **Strategy module candidate** — a regime-detection layer for the `/opt/cemini` analyst node; the HMM `bull_prob − bear_prob` signal is a clean position primitive.
- **Conditioning input** — feeds `@concepts/regime-conditioned-evaluation.md`: detect regime here, evaluate/allocate strategies conditioned on it there.
- **Honest framing** — `[TENTATIVE]` the post claims production deployment "at real firms" generating "real edge"; Markov regime-switching is genuinely standard at quant shops (Citadel/Two Sigma cited), but no specific Cemini-verified performance number attaches. Markov models *quantify transition probability*; they do not "predict the future."

## Snippets

> "P^(n)(i,j) = [Pⁿ]ᵢⱼ — To compute the probability of transitioning from any state to any other state in n steps, you simply multiply the transition matrix by itself n times." [Source: posts.docx — Post 3, Part 3]

> "The emission variables you choose matter more than any other design decision. Returns alone carry limited information about the true economic regime. Returns combined with realized volatility, credit spreads, and VIX term structure give the model a much richer signal." [Source: posts.docx — Post 3, Part 6]

## Dead Ends

- **Naive independence models** — produce mathematically impossible state paths; the entire reason Markov chains exist for this problem.
- **Hand-labeled observable states as the final model** — they reverse-engineer regime from price and miss latent repositioning; the post explicitly frames HMM as the fix.
- **Single Baum-Welch initialization** — converges to a local maximum; frequently produces suboptimal regime assignments.
