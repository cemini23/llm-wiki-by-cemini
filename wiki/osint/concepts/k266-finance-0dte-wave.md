---
title: K266 Finance 0DTE Wave (Sep 2026)
type: concept
tags: [options, 0dte, k266, backtest, execution]
keywords: [SPY, regime gate, delta band, OCO, OTO, look-ahead, stale quotes, rules-based]
related:
  - concepts/k265-newsletter-macro-wave.md
  - concepts/k266-ood-stub-wave.md
  - sources/x-article-buildwithpublic-0dte-2026-09-19.md
  - entities/tools/openjev.md
maturity: draft
created: 2026-09-19
updated: 2026-09-19
harness_verb: FILE
wire_status: wont_wire
---

## Relations

- @entities/tools/openjev.md
- @concepts/k265-newsletter-macro-wave.md
- @concepts/k266-ood-stub-wave.md
- @sources/x-article-buildwithpublic-0dte-2026-09-19.md

## Raw Concept

K266 cluster hub. Dual-ID **OSINT K266**. One X Article on a 0DTE SPY options scalping desk. **No live desk. No xsp/pm scp. Not a Jev app.**

## Narrative

@BuildwithPublic (175 likes / 414 bookmarks / 32,143 impressions) publishes a full postmortem for a same-day-expiry SPY options scalper built on the Public API. The author states he helps lead API trading at Public — read the API sections as vendor-adjacent. **Wiki FILE only.**

**Design.** Three layers: a daily-bar **regime gate** (DSS Bressert double-smoothed stochastic plus a Lyapunov exponent over a Hodrick-Prescott filtered series, latching BULLISH / BEARISH / NEUTRAL; puts-only means no call routes, neutral means nothing routes), a **delta-band contract scout** (`|Δ| 0.40–0.60`, plus gamma floor, open interest, spread cap in ticks, session volume, strike distance), and **native OCO/OTO bracket routing**. Instruments: SPY 0DTE. Same-day expiry means the entire holding period is one session.

**Why this page exists — the defect catalogue.** The strategy is not the transferable asset; the failure modes are.

1. **A parameter search finds harness bugs, not edge.** A 660-cell exit sweep produced a champion (six-tick target / one-tick trail, +$1.28 per cycle) that two modelling defects had manufactured.
2. **Floating-point tick arithmetic.** Modelling the bid as mid minus half a tick is exactly between two cents at a one-tick spread; binary floating point resolved it inconsistently, so the modelled bid equalled the mid on 50.9% of observations. Fix: snap both sides to the tick grid in whole ticks.
3. **Look-ahead in trailing stops.** The simulator set the running peak, moved the stop, and tested the fill inside one observation — selling at the exact high of every bar. All eighteen profitable exits of the winning cell were that artifact. Fix: defer the fill by one observation.
4. **Fixing both inverted the answer.** The trail was the leak, not the target. With the trail off, the three-tick target is profitable at every stop width and in every session (+$0.68 to +$0.92 per cycle vs −$0.57 with the trail live).
5. **Economics first.** Round-trip credit ~+$0.11 per contract against **$1.00 per tick** on a single contract — one tick of spread costs about nine times the credit. A three-tick target against a twenty-five-tick risk needs **88.89%** accuracy to break even. Compute the number before designing the exit.
6. **Sweep the inherited parameters.** The entry ladder's mean windows were ported from a futures engine and never examined. Every twelve-minute slow window beat every thirty-minute slow window across the whole grid; expectancy went +$0.68 → +$1.74 and stopped-out cycles 7 → 4 at five fast / twelve slow.
7. **Stale vendor timestamps.** A poll returned 250ms-fresh quotes while the broker-side `bidTimestamp` on the same payload was nearly three hours old. Live measurement: median ~**1.8s** of age already built into the quote on arrival, tail past 2.7s. Fail closed — no timestamp, no trade — and accept that five to ten percent of cycles are permanently refused.
8. **ACK is not a fill.** Never auto-replay a write; a retried order is a duplicate position. Network ambiguity marks the order unknown, then disarms the engine.
9. **Boot stopped and disarmed.** Routing stays off until explicitly armed. Exclusive single-instance lock. Execution-quality log: quote age, submit-to-ACK latency, cancel/replace latency, signed slippage.
10. **Small-sample discipline.** The author publishes no performance table and schedules a formal read at ten sessions. Rule 605 covers NMS stocks, not options, so there is no published fill dataset.

**Cemini reading.** **Wiki FILE. 0 product Integrate GO. No live desk. No xsp/pm scp.** This is not a Jev application and not a CeminiSuite product candidate. Borrow the defect checks into existing backtest hygiene: tick-grid modelling, deferred trail fills, inherited-parameter sweeps, vendor-timestamp freshness gates, and disarm-on-ambiguity. The closing API feature list and risk disclaimer are **advertorial framing — do not reproduce.** See `@briefs/2026-09-19_k266-finance-0dte-wave.md`.
