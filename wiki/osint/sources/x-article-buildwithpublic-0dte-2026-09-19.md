---
title: "I built a 0DTE options scalping desk on the Public API (@BuildwithPublic)"
type: source
tags: [source, k266, options, backtest, execution, finance]
keywords: [k266, 0DTE, SPY, regime gate, delta band, OCO, OTO, look-ahead, stale quotes]
related:
  - concepts/k266-finance-0dte-wave.md
  - concepts/k266-ood-stub-wave.md
  - sources/x-article-0xmovez-jev-engineering-2026-09-19.md
maturity: draft
created: 2026-09-19
updated: 2026-09-19
read_status: read
---

## Relations

- @sources/x-article-0xmovez-jev-engineering-2026-09-19.md
- @concepts/k266-finance-0dte-wave.md
- @concepts/k266-ood-stub-wave.md

## Raw Concept

| File | `x-article-buildwithpublic-0dte-public-api-2026-09-19.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/x-article-buildwithpublic-0dte-public-api-2026-09-19.md` |
| Retrieved | 2026-09-19 |
| Dual-ID | **OSINT K266** |
| Author | @BuildwithPublic — post id `2101011678997405745` |
| Kind | X Article — *I built a 0DTE options scalping desk on our trading API @public* |
| Metrics | 175 likes · 414 bookmarks · 32,143 impressions (X MCP 2026-09-19) |
| sha256 | `4e173b5611d6c5322f57fb4d3bdeb4587d00ac9f9ef141a1356711431bcfc488` |
| Bias | **Author states he helps lead API trading at Public.** Treat as vendor-adjacent. |

**Not a Jev source. No live desk. No xsp/pm scp.**

## Narrative

Detailed build postmortem for a same-day-expiry SPY options scalper on the Public API. The value for Cemini is the **backtest-defect catalogue**, not the strategy. The author declares his own bias as a Public API employee.

**Engine.** TypeScript execution engine, Python research tooling. Three layers: **regime gate** (daily bars — DSS Bressert double-smoothed stochastic plus a Lyapunov exponent over a Hodrick-Prescott filtered series across about two years; emits BULLISH / BEARISH / NEUTRAL and latches), **contract scout** (delta band `|Δ| 0.40–0.60` on absolute value, plus gamma floor, open interest, max spread in ticks, session volume, max strike distance), and **bracket routing** (limit entry with attached take-profit and stop, using Public's native OCO and OTO).

**Why the first selector failed.** A fixed premium band drifts away from peak gamma as gamma sharpens. In one captured session the ATM strike moved from about **$1.20** in the morning to roughly **$0.35** by 15:00. A **$1.15 floor left no near-the-money candidate at all in ten of twelve sampled bars at 14:00** — the desk would have gone blind every afternoon and the author did not know until he measured. Every rejection is now counted and surfaced: too cheap 66, ask cap 153, delta band 14, no quote 72.

**Two-safeguards-paralysis.** The desk held a call while the regime had latched bearish. Entries were correctly refused, but the scout ranks on structure alone so its top pick sat on the forbidden side, and the anti-churn dwell timer then protected that pick. Two safeguards, each correct alone, combined into a full-session idle.

**Cost structure.** Per contract per round trip: about **$0.02** fees on the buy, **$0.03** on the sell, against roughly **$0.08** rebate credit per leg → about **+$0.11** net credit before price movement. One tick on a single-contract option is **$1.00**. So **one tick of spread costs about nine times that entire credit on one leg**. Break-even arithmetic: a three-tick target against a twenty-five-tick risk is **+$3.11 vs −$24.89** net of credit — the strategy must be right **88.89%** of the time just to break even.

**The backtest defects (the transferable lesson).** A sweep of **660 exit shapes** produced a champion: six-tick target with a one-tick trail, **+$1.28 per cycle** against a live configuration losing **$0.23**. Two defects in the author's own harness manufactured it:

1. **Floating-point spread.** The bid was modelled as mid minus half the spread. At a one-tick spread that is mid minus half a cent — exactly between two cents. Binary floating point resolved it down for some prices and up for others. The modelled bid equalled the mid on **50.9%** of observations and sat a full tick below on the rest. Both sides now sit on the tick grid in whole ticks.
2. **Look-ahead trail.** Inside one observation the simulator set the running peak, moved the trailing stop to peak minus one tick, then immediately tested whether the bid had reached that stop — so it filled on the spot. All **eighteen** of the winning cell's profitable exits were that artifact. The real stop is registered on one poll and can only be taken on a later one; the fill is now deferred by one observation.

Fixing both dropped the winner from **$114.90 to $26.90** — no better than the same configuration with the trail switched off. The answer then **inverted**: all **fifteen** top configurations out of 660 use the existing three-tick target with an arm distance high enough that the trail can never engage. With the trail off, the three-tick target is profitable at every stop width and in every session, about **+$0.68 to +$0.92 per cycle** against **−$0.57** with the trail live. The trail was the leak.

**Stated caveats.** The result rests on a one-tick spread; at two ticks it turns negative, because a three-tick target cannot carry a two-tick spread. Contracts passing the filters quote one tick wide about **90%** of the time. The result is about **ninety cycles across two sessions in the same regime** — a direction to test, not a conclusion.

**The inherited-parameter lesson.** The mean-reversion entry ladder (five running means of the underlying) was ported from a trusted futures engine: two fast rungs over five minutes, two slow rungs over thirty minutes, plus a cumulative session mean. The window lengths were never examined. Re-running every captured session across a grid: **every twelve-minute slow window beat every thirty-minute slow window**, at all five fast windows tested — the entire row, not one cell. At five fast / twelve slow, expectancy went from **+$0.68 to +$1.74** a cycle and stopped-out cycles fell from **seven to four**, with the cycle count identical in every cell. The fast window showed unordered noise from four to ten minutes. Shipped: five and twelve. Both unanswerable questions are named: sub-four-minute fast legs are unmeasurable on one-minute bars, and twelve minutes is the shortest measurable slow window, so "twelve wins" may mean "the shortest thing I can test wins".

**Operational lessons.**

- **Stale quotes.** The polling loop returned quotes 250ms fresh while the broker-side `bidTimestamp` on the same payload read nearly three hours old — the session had closed. The desk now refuses any quote whose broker timestamp exceeds a freshness threshold and **fails closed**: no timestamp, no trade. Live measurement across fourteen consecutive samples at 150–300ms request latency showed a median of about **1.8 seconds** of age already built into the quote on arrival, with a tail past **2.7s**. Against a three-second ceiling, five to ten percent of cycles will be refused as stale permanently. The author's conclusion: that is the shape of REST-polled options data, not a tuning bug.
- **Auth and rate limits.** A 401 latches per credential generation instead of hammering; a 429 sets a shared cooldown honouring `Retry-After`. **Never auto-replay a write — a retried order is a duplicate position.**
- **Ambiguity.** Network failures mark an order **unknown**, then disarm and stop the engine. If it is unknown whether an order reached the exchange, stop and reconcile by hand.
- **Single instance.** Exclusive lock before start; two engines on one account is a bad day.
- **Execution-quality log.** Quote age, submit-to-ACK latency, cancel/replace latency, signed slippage per cycle. Vocabulary discipline: **a broker ACK is not a fill.**
- **Boot discipline.** The desk boots stopped and disarmed every session; routing stays off until explicitly armed. A formal read is scheduled at **ten sessions**; no performance table is published before that.

**Other named limits.** Whether the stop parameter matters at all — across every width from twenty to fifty ticks it is reached on only a handful of cycles, so on current evidence it is insurance rather than a tuned parameter. Real fill distribution is unknown: **Rule 605 covers NMS stocks, not options**, so there is no published dataset and the forward log is the only honest route.

**Cemini reading.** Wiki FILE. **No live desk. No xsp/pm scp. Not a Jev app.** The reusable content is the defect catalogue: floating-point ticks, look-ahead trail fills, stale-vendor timestamps, ACK-is-not-a-fill, disarm-on-ambiguity, and "a parameter search finds your harness's bugs faster than it finds an edge". Pair with the existing falsification material in `@concepts/k266-finance-0dte-wave.md`. The article ends with a Public API features argument and a risk disclaimer — **advertorial framing, do not reproduce.**

## Snippets

> "A parameter search finds your harness's bugs faster and more enthusiastically than it finds an edge, and hands them to you dressed as the winner. When a sweep produces a surprising champion, the first hypothesis should be a modelling defect." [Source: x-article-buildwithpublic-0dte-public-api-2026-09-19.md]

> "One tick on a single-contract option position is $1.00 - a penny of premium against a hundred multiplier. So one tick of spread costs about nine times that entire credit, on one leg." [Source: x-article-buildwithpublic-0dte-public-api-2026-09-19.md]

> "My cycle targets three ticks and risks twenty-five. Net of credit that is +$3.11 against −$24.89 - so the strategy must be right 88.89% of the time simply to break even." [Source: x-article-buildwithpublic-0dte-public-api-2026-09-19.md]

> "My polling loop returned quotes 250ms fresh while the broker-side bidTimestamp on the same payload read nearly three hours old. The session had closed. My poll was fresh; the data behind it was not." [Source: x-article-buildwithpublic-0dte-public-api-2026-09-19.md]

> "I never auto-replay a write - a retried order is a duplicate position." [Source: x-article-buildwithpublic-0dte-public-api-2026-09-19.md]

> "I spent weeks sweeping targets and stops, the two numbers that felt like the strategy, while a parameter I had inherited without reading sat there worth more than both. Sweep the things you copied in, not just the things you chose." [Source: x-article-buildwithpublic-0dte-public-api-2026-09-19.md]
