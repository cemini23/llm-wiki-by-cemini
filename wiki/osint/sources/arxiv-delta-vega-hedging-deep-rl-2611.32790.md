---
title: "Delta-Vega hedging with deep reinforcement learning: from simulation to reality"
type: source
related:
  - concepts/deep-rl-delta-vega-hedging.md
  - concepts/local-stochastic-volatility-calibration.md
  - concepts/back-of-envelope-hedging-cost.md
  - concepts/options-derivatives.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Delta-Vega Hedging with Deep Reinforcement Learning: From Simulation to Reality |
| Author | Michele Colombi, Marco Di Francesco, Pietro Rossi (SNS Pisa, Bologna, Leithà/Unipol, Prometeia) |
| Type | arXiv preprint, q-fin.CP / reinforcement learning |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.32790-delta-vega-hedging-with-deep-reinforcement-learn.pdf` |
| Retrieved | 2026-11-25 |
| arXiv | 2611.32790v1, 24 Nov 2026 |
| Pages | 34 |
| Read status | read |

## Narrative

### Problem

A position hedged with the underlying alone stays exposed to volatility. A trader can hedge that exposure with a second instrument, a longer-dated option, but pays a wider spread for it. The paper learns a two-instrument hedging policy with reinforcement learning and tests whether it survives transfer to real market data.

### Method

The agent is trained with Proximal Policy Optimisation (PPO) on synthetic paths from a Heston stochastic-volatility model. It trades the underlying and one longer-dated vanilla option under discrete-time trading and transaction costs. The state is restricted to quantities a trader can observe: prices, holdings and contract specifications. The agent never sees the latent variance or the model parameters. That restriction is what makes sim-to-real transfer possible. The payoff is a mean-variance objective, so the agent trades off cost against replication error. [Source: arxiv-2611.32790-delta-vega-hedging-with-deep-reinforcement-learn.pdf p.2]

The learned policy is called "Delta-Vega-like". It trades the same two instruments as a model-based Delta-Vega hedge, but it learns the ratios from data.

### Results, synthetic then real

In a frictionless Heston setting, PPO reproduces the semi-analytical Delta-Vega hedge. With costs, it departs from the model hedge and improves the mean-variance objective. It beats Delta-only and Delta-Vega benchmarks in mild and high friction.

The real test uses daily S&P 500 index option data from 2019 to 2022, 1,193 episodes. Two-instrument strategies roughly halve the P&L dispersion of the Delta-only hedge. On the full sample, PPO reaches a mean-variance objective of −0.07, against −0.20 for Delta-Vega and −1.03 for Delta-only. Total P&L standard deviation is 0.484 for RL, 0.560 for Delta-Vega and 1.174 for Delta-only. [Source: arxiv-2611.32790-delta-vega-hedging-with-deep-reinforcement-learn.pdf p.25]

The agent systematically holds more of the hedging option than the practitioner benchmark: 0.77 units against 0.70, and less of the underlying, 0.12 against 0.18. That matches the Heston model hedge on which it was trained. The advantage concentrates in high-volatility episodes, 2020 above all. In that year the Delta-only P&L standard deviation is 2.18%, the Delta-Vega figure 1.03%, and the RL figure 0.72%.

### Honest limits

The authors state three limits. The sample is daily and short, so mean P&L estimates are not statistically distinguishable from zero. The agent inherits the shortcomings of its training simulator; on real data it behaves as it was trained to behave. And the cost model is an abstraction, not observed bid-ask microstructure. [Source: arxiv-2611.32790-delta-vega-hedging-with-deep-reinforcement-learn.pdf p.27]

### Why it matters here

The transferable lesson is about training environments, not about a ready strategy. A learned hedge learns the simulator. The paper shows that restricting the state to observable quantities is the condition for transfer, and that the gain is regime-dependent. For a small options book, the practical takeaway is that two-instrument hedging cuts dispersion roughly in half at comparable cost.

## Snippets

> "The agent is trained on data generated from a stochastic volatility model, and restricted to state variables observable in the market, so that the policy learned in simulation applies directly to real market data." [Source: arxiv-2611.32790-delta-vega-hedging-with-deep-reinforcement-learn.pdf p.1]

> "PPO holds on average 0.77 units of the hedging option on the S&P 500 test set, against 0.70 for Delta-Vega, and 0.12 units of the underlying asset, against the benchmark's 0.18." [Source: arxiv-2611.32790-delta-vega-hedging-with-deep-reinforcement-learn.pdf p.25]
