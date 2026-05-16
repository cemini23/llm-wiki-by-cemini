---
title: 'Autonomous AI Agents for Option Hedging: Enhancing Financial Stability through Shortfall Aware Reinforcement Learning'
type: source
tags: [pdf, rl-marl, option-hedging, options-derivatives, tail-risk]
keywords: [QLBS, RLOP, shortfall-probability, expected-shortfall, CVaR, delta-hedging, replication, transaction-costs, IVRMSE]
related:
  - concepts/rl-marl-research.md
  - concepts/options-derivatives.md
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus
- @concepts/options-derivatives.md — RL option-hedging vs parametric pricers (Black-Scholes, jump-diffusion, Heston); IVRMSE shown to be a poor proxy for after-cost hedging quality
- @entities/components/kelly-cvar-risk-engine.md — uses Expected Shortfall / CVaR and shortfall probability as the optimization objective; downside-sensitive, survival-centric hedging

## Raw Concept

- **Original title**: Autonomous AI Agents for Option Hedging: Enhancing Financial Stability through Shortfall Aware Reinforcement Learning
- **Author(s)**: Minxuan Hu (Cornell), Ziheng Chen (UT Austin), Jiayu Yi (NTU), Wenxi Sun (Johns Hopkins). arXiv:2603.06587v1 [cs.AI], 1 Feb 2026
- **Type**: PDF
- **Location**: research for cemini/Autonomous AI Agents for Option Hedging.pdf
- **Retrieved**: 2026-04-27
- **Length**: 13p
- **Read status**: deep-read
- **Cluster**: rl-marl

## Narrative

This paper introduces two RL frameworks for autonomous option hedging that shift the learning objective from minimizing replication error to optimizing **shortfall probability** — the frequency of any after-cost loss — addressing the gap between static pricing-model calibration and realized hedging outcomes in markets with frictions.

**Method.** Two complementary formulations are proposed. (1) **Adaptive-QLBS**, a backward, value-based extension of Halperin's Q-learner in Black-Scholes that redefines the value function as an Ft-adapted process: it adds a horizon discount factor `d_T(t)` smoothing the terminal payoff's influence and replaces variance terms with their square roots for dimensionless, numerically stable estimates. The authors prove (Proposition 1) the option price is monotonically increasing in both risk aversion lambda and transaction-friction epsilon. (2) **RLOP (Replication Learning of Option Pricing)**, a novel forward formulation in which the agent trades a self-financing portfolio and is rewarded by how closely terminal wealth tracks the option payoff; it stacks an ensemble of maturities for intermediate learning signals and a shortfall-probability objective that promotes capital preservation. Both use a Gaussian policy on a shared ResNet-style architecture trained with REINFORCE-with-baseline (Adam, lr 1e-4). Empirical evaluation uses listed SPY and XOP (energy-sector ETF) call options across two regimes — 2020Q1 (COVID dislocation) and 2025Q2 (calm) — benchmarked against Black-Scholes, Merton jump-diffusion, and Heston stochastic-volatility, evaluated by realized-path delta hedging under proportional transaction costs.

**Results.** RL policies deliver a systematic cost advantage: an RL method achieves the lowest average transaction cost in every slice, indicating lower turnover under the same daily rebalancing schedule. RLOP is the most consistent winner on loss frequency — lowest shortfall probability in six of eight tau=28d slices, including all four XOP slices — and shows the clearest tail-risk (Expected Shortfall) improvement in the stress/sector regime (XOP 2020Q1). Crucially, parametric models typically win same-day implied-volatility fit (IVRMSE), yet IVRMSE is shown to be a poor predictor of after-cost hedging performance, motivating a hedging-facing, full-distribution evaluation criterion.

**Relevance to Cemini.** Directly reinforces the Kelly/CVaR risk engine's design philosophy: optimize a downside-sensitive objective (shortfall probability, Expected Shortfall) rather than a mean-squared replication error. The risk-cost map (transaction cost vs replication dispersion) and net-CDF distributional evaluation are reusable diagnostics for any cost-aware hedging policy. The headline caution — strong calibration fit does not imply good realized hedging — is a useful guardrail for model selection in the trading stack.

## Snippets

> "We quantify tail losses using the shortfall `SF_T := max(0, -PnL_net_T)`, and report Expected Shortfall (ES; also known as Conditional Value-at-Risk/CVaR) at tail levels alpha in {5%, 10%} ... We also report the shortfall probability `P(PnL_net_T < 0)` to separate loss frequency from loss severity." [Source: Autonomous AI Agents for Option Hedging.pdf p.6]

> "RLOP is the most consistent winner on loss frequency: across the eight slices, it achieves the lowest shortfall probability in six cases (including all four XOP slices)." [Source: Autonomous AI Agents for Option Hedging.pdf p.6]

> "While diagnostics like IVRMSE favor parametric models, we demonstrate that static fit is an insufficient proxy for hedging quality under market frictions. Our full-distribution analysis reveals that RL policies materially mitigate tail-risk losses, particularly during operationally salient periods like the 2020 liquidity crash." [Source: Autonomous AI Agents for Option Hedging.pdf p.9]
