---
title: "Moontower — compounding through risk, not return (Maymin brothers on Flirting with Models)"
type: source
related:
  - concepts/compounding-through-risk-not-return.md
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Compounding Through Risk, Not Return |
| Author | Kris Abdelmessih (Moontower Meta), curating Flirting with Models S7E35 |
| Type | newsletter, RSS; transcript curation |
| URL | https://moontowermeta.com/compounding-through-risk-not-return/ |
| Location | `research to be indexed/substack-rss-moontower-2026-11-11-compounding-through-risk-not-return.md` |
| Retrieved | 2026-11-11 |
| Published | 2026-11-11 |
| Read status | read |

## Narrative

### The guests

Corey Hoffstein interviews Philip and Alan Maymin, co-heads of global asset allocation at Janus Henderson. They run the group Myron Scholes founded there. Philip came through LTCM, academia and behavioural analytics. Alan came through high-frequency derivatives and prop desks.

The core idea: investors live in an average-return world and should not. Compound growth is what matters. The easier lever on compounding is risk, not return.

### Why risk is the easier lever

Philip gives three reasons:

| Reason | Statement |
|---|---|
| Alpha is fickle | A source of alpha can disappear in a career. Risk knowledge compounds and transfers across environments |
| Measurement | Alpha needs decades to separate from zero statistically. Risk estimates improve as you cut the sampling interval, from monthly to weekly to daily |
| Environment | Environments always change. A risk process expects that; a return process assumes continuity |

The Merton 1980 appendix is the anchor: to distinguish a mean from zero you need a long calendar window, not a finer sampling grid. Risk is the opposite.

### Reading the options market

Alan: an option price is a forward-looking estimate with premium at risk. The chain gives a distribution across strikes and expiries, so it prices upside and downside separately. Tracking the ratio of the two shows how an asset's risk shape changes.

Philip on unknown unknowns: option prices cover all outcomes, not one named event. The market is the next best thing to an oracle, and the alternative is the rearview mirror.

The framing is that thousands of analysts are publishing their confidence through prices, and almost nobody reads it. The group does not assume the prices are wrong. It reads them and deviates only with a specific view.

### Risk-neutral versus real world

The obvious objection: options are priced under Q, and the group uses them to say things about P.

Philip's answer has three parts:

1. The biggest difference between the measures is the drift. The rest of the distribution is fairly robust.
2. The process uses **tails**, not the middle. The paper claim: throw away the middle 80% of a distribution and risk is essentially unchanged, with 80 to 90% correlation.
3. The signal is the **change** in the tail shape over time, not a single reading.

Kris adds a caution from his own work. If option spreads look mispriced against realised outcomes, most of the edge is the risk-free-rate drift assumption. Use an empirical upward drift and the mispricing disappears. A trader who "exploits" the risk-neutral assumption may be harvesting equity risk premium and calling it option edge.

### Correlations in the tails

Philip's claim is that middle correlations are unstable and hard to estimate, but tail correlations are easy. In a shock, correlations go to plus or minus one. The only question is the sign.

A simple regime proxy:

| Vol state | Implied tail correlation |
|---|---|
| Both assets in the top quartile of their own vol history | About +1 |
| One top quartile, one bottom quartile | About −1 |
| Neither extreme | About 0 |

The objective function is a tail analogue of mean-variance: expected tail gain divided by expected tail loss squared. Downside gets the dominant weight.

### What risk means

Alan rejects volatility as the definition. Risk is the chance of falling short of the client's objective. Volatility treats gains and losses alike; the process separates upside risk, which may be wanted, from downside risk, which it tilts away from.

### When it goes mainstream

Philip's answer to "if this works, why does it persist": most large investors are benchmark-relative and mechanically rebalance, which blocks the trade. He quotes Scholes: the signal that the approach has won is when investors carry **risk-managed dynamic benchmarks** — "down 30%" rather than "60/40" — instead of static ones.

His argument against static benchmarks: a passive dollar allocation has wildly changing risk because risk is regime-dependent. Time-series risk concentration is as real as cross-sectional concentration.

### Why it is filed here

It gives a clean, quotable statement of the tail-first sizing doctrine that several Cemini lanes already use in practice: vol-regime gates on the XSP lane, and the drawdown rules in the PM/Kalshi retail bot.

The transferable testable claim is the middle-80% discard: if true at the workspace's horizons, a risk model can ignore the body and model only the tails.

[OPEN QUESTION 2026-11-14] The middle-80% result is cited to an unpublished paper. No reproduction was run here.

## Snippets

> "Alpha is fickle... But risk? Risk is easier to measure, it's reflecting the environment that things can change, you're able to compound your knowledge." — Philip Maymin [Source: substack-rss-moontower-2026-11-11-compounding-through-risk-not-return.md]

> "You could throw away the middle 80% of a distribution, and your risk is basically the same. You're gonna have an 80 to 90% correlation, and 80, 90% of the risk is still there." — Philip Maymin [Source: substack-rss-moontower-2026-11-11-compounding-through-risk-not-return.md]

> "In the tails, we know the correlations are one. The only real challenge is it gonna be plus one or minus one." — Philip Maymin [Source: substack-rss-moontower-2026-11-11-compounding-through-risk-not-return.md]
