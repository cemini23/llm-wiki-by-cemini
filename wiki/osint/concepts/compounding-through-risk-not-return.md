---
title: Compounding through risk, not return — tail-first portfolio doctrine
type: concept
related:
  - sources/substack-rss-moontower-2026-11-11-compounding-through-risk-not-return.md
  - concepts/options-derivatives.md
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

How should a portfolio manager improve compound growth when alpha is unreliable? This page records the Maymin brothers' answer, as curated by Moontower Meta: manage risk, read the option tails, and treat the middle of the distribution as irrelevant.

Source: @sources/substack-rss-moontower-2026-11-11-compounding-through-risk-not-return.md (Flirting with Models S7E35).

## Narrative

### The core identity

Compound return equals average return minus a risk drag. Average return is alpha, and alpha is fickle. Risk is measurable and the measurement improves with finer sampling. Therefore risk is the tractable lever.

The Merton 1980 appendix is the formal support:

| Quantity | How to sharpen it |
|---|---|
| Mean return | Needs a longer calendar window; sub-sampling does not help |
| Risk | Improves as the sampling interval shrinks, monthly to weekly to daily |

A manager who wants a statistically reliable alpha estimate may need decades, by which time the firm that generated it has changed. A manager who wants a reliable risk estimate needs a finer grid.

### Read the option chain as a forecast

An option price is a forward-looking distribution with premium at risk. The chain gives:

- a distribution across strikes
- across several expiries
- with separate prices for upside and downside

Two derived signals follow. The first is the ratio of upside risk to downside risk for one asset. The second is how that ratio changes over time.

The group's stated posture is that it does not assume the prices are wrong. It reads them and deviates only with a specific view. The analogy given is traffic-enabled navigation: deviate rarely, and usually regret it.

### The tails, not the middle

Three claims carry the method:

1. **The risk-neutral versus real-world gap is mostly drift.** The shape of the distribution is fairly robust across the measure change.
2. **The middle does not matter.** The cited result: discard the middle 80% of a distribution and 80 to 90% of the risk remains, at 80 to 90% correlation.
3. **Track changes, not levels.** One reading is not a truth; the movement of the tail shape is the signal.

A caution worth filing next to the method. If option spreads look mispriced against realised outcomes, most of the apparent edge can be the risk-free-rate drift assumption. Substitute an empirical upward drift and the mispricing disappears. The trader may be harvesting equity risk premium and calling it option edge.

### Tail correlation

Middle correlations move between about −0.3 and +0.3 and are hard to estimate. Tail correlations are simpler: in a shock they go to ±1, and the only question is the sign.

A regime proxy from the interview:

| Vol state of two assets | Implied tail correlation |
|---|---|
| Both in the top quartile of their own history | about +1 |
| One top quartile, one bottom quartile | about −1 |
| Neither extreme | about 0 |

The objective becomes a tail analogue of mean-variance: expected tail gain divided by expected tail loss squared. Downside carries the dominant weight.

### The definition of risk

Alan Maymin rejects volatility. Risk is the probability of missing the client's objective. Volatility punishes gains and losses equally; an objective-based process separates upside risk, which may be desirable, from downside risk, which it tilts away from.

### Why it persists

Two answers. First, most large allocators are benchmark-relative and must rebalance mechanically, which blocks the trade. Second, the tell that the method has won is when clients carry **risk-managed dynamic benchmarks** — a drawdown cap rather than "60/40" — instead of static ones.

The argument against a static benchmark: a passive dollar allocation has wildly changing risk, because risk is regime-dependent. Time-series risk concentration is as real as cross-sectional concentration.

### Use in this workspace

The doctrine backs three existing practices:

- vol-regime gates on the XSP lane
- drawdown rules in the PM/Kalshi retail bot
- Kelly-style sizing that treats volatility as the estimable input

[OPEN QUESTION 2026-11-14] The middle-80% discard is cited to an unpublished paper. No test was run on workspace returns.

## Snippets

> "Volatility treats gains and losses alike. What we do is we try to separate out the upside risk, which for all intents and purposes, could be something that you want." — Alan Maymin [Source: substack-rss-moontower-2026-11-11-compounding-through-risk-not-return.md]

> "We're not thinking like there's a mistake in the option pricing in the market and we could take advantage of it. On the contrary, there's just all this free information that people are shouting from the rooftops." — Philip Maymin [Source: substack-rss-moontower-2026-11-11-compounding-through-risk-not-return.md]
