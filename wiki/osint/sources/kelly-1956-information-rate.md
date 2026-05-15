---
title: "A New Interpretation of Information Rate — Kelly (1956)"
type: source
tags: [paper, information-theory, kelly-criterion, bet-sizing, position-sizing, quant-finance]
keywords: [kelly-criterion, information-rate, channel-capacity, exponential-growth, optimal-betting, fair-odds, track-take, shannon, bell-system-technical-journal]
related:
  - concepts/kelly-sizing-quarter.md
  - concepts/shannon-entropy-kl-divergence-prediction-markets.md
  - concepts/three-formula-system-polymarket-rare-events.md
  - concepts/poisson-edge-rare-events.md
maturity: validated
read_status: deep-read
created: 2026-05-15
updated: 2026-05-15
clusters: [quant-finance]
---

## Relations

- @concepts/kelly-sizing-quarter.md — quarter-Kelly is a fractional application of the criterion derived here
- @concepts/shannon-entropy-kl-divergence-prediction-markets.md — Shannon's channel capacity theorem provides the upper bound Kelly equates to exponential capital growth
- @concepts/three-formula-system-polymarket-rare-events.md — all three formulas use Kelly-derived position sizing
- @concepts/poisson-edge-rare-events.md — Poisson edge formula applies fractional Kelly to low-frequency event bets

## Raw Concept

- **Title**: A New Interpretation of Information Rate
- **Author**: J. L. Kelly, Jr. (Bell Telephone Laboratories)
- **Type**: Academic paper
- **Journal**: Bell System Technical Journal, Vol. 35, pp. 917-926, July 1956
- **Retrieved**: 2026-05-15
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/A New Interpretation of Information Rate.pdf`
- **Pages**: 10
- **Read status**: deep-read
- **Reproduced with permission of AT&T**

## Narrative

This is the **original Kelly criterion paper** — the foundational text connecting Shannon's information theory to optimal gambling and position sizing. The problem Kelly set out to solve: Shannon's channel capacity `R` was given meaning only by a coding theorem (binary digits can be encoded and transmitted at rate `R` with arbitrarily small probability of error). But what meaning does `R` have when no coding is contemplated?

### Core insight

Kelly models a gambler who receives symbols from a communication channel and bets on the outcomes those symbols represent. The gambler's capital grows exponentially, and the **maximum exponential rate of growth G_max equals the rate of transmission R**:

```
G = lim(N→∞) (1/N) log(V_N / V_0)
G_max = R = H(X) − H(X|Y)
```

For a noisy binary channel with error probability `p` and correctness probability `q`, the optimal fraction `ℓ` to bet each round satisfies:

```
(1 + ℓ) = 2q
(1 − ℓ) = 2p
G_max = 1 + p·log(p) + q·log(q) = R
```

### Key results

1. **Fair odds case**: When odds are `α_s = 1/p(s)`, the gambler maximizes G by betting `a(s|r) = q(s|r)` — i.e., the gambler **ignores posted odds entirely** and bets proportional to posterior probabilities given the received signal.

2. **Unfair odds without track take**: G = Σ p(s)log(α_s) − H(X|Y). Any deviation from fair odds helps the gambler. The gambler still bets `a(s|r) = q(s|r)`.

3. **Track take case**: The problem becomes nonlinear — the gambler can no longer make canceling bets since the track takes a percentage. Kelly solves the constrained maximization explicitly, deriving a water-filling threshold: bet on outcome `s` iff `p(s)α_s > (1−p)/(1−σ)`, where `p` and `σ` are sums over the active bet set `λ`.

### Relevance to Cemini

The Kelly criterion is the **foundational bet-sizing algorithm** for all Cemini Polymarket strategies. The quarter-Kelly default (see @concepts/kelly-sizing-quarter.md) is a fractional application of the criterion derived here. The paper's treatment of unfair odds (Section "When the Odds Are Not Fair") directly models Polymarket conditions where market prices deviate from true probabilities.

## Snippets

> "If the input symbols to a communication channel represent the outcomes of a chance event on which bets are available at odds consistent with their probabilities (i.e., 'fair' odds), a gambler can use the knowledge given him by the received symbols to cause his money to grow exponentially. The maximum exponential rate of growth of the gambler's capital is equal to the rate of transmission of information over the channel." (p.917)

> "The gambler could obtain even money bets even though he already knew the result of each game. The amount of money he could make would depend only on how much he chose to bet. How much would he bet? Probably all he had since he would win with certainty. In this case his capital would grow exponentially and after N bets he would have 2^N times his original bankroll." (p.919)

> "the gambler ignores the posted odds in placing his bets!" (p.922, emphasis original)

> "Since the gambler's exponential gain would be H(α) − H(X) if he had no inside information, we can interpret R = H(X) − H(X|Y) as the increase of G_max due to the communication channel." (p.923)
