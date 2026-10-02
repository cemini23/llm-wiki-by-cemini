---
title: K278 Gambling / PM Wave (Oct 2026)
type: concept
tags: [prediction-markets, gambling, k278]
keywords: [k278, kalshi, cbs, forecasting, no-level]
related:
  - concepts/k277-gambling-pm-wave.md
  - sources/substack-rss-event-horizon-2026-10-02-sponsored-pm-data-2026-10-02.md
  - sources/arxiv-2610.01955-dyor-forecasting-2026-10-02.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k277-gambling-pm-wave.md
- @sources/substack-rss-event-horizon-2026-10-02-sponsored-pm-data-2026-10-02.md
- @sources/arxiv-2610.01955-dyor-forecasting-2026-10-02.md

## Raw Concept

K278 cluster hub. Dual-ID **OSINT K278**. Prior @concepts/k277-gambling-pm-wave.md.

## Narrative

A product and media item, plus the first forecasting paper in the wiki. **No level to arm. No pm scp.**

### The media item

A **Kalshi and CBS News** partnership drew the criticism. The argument is narrow and worth recording: citing a prediction market as a source is fine; a sponsorship that puts the sponsor's own market data into editorial coverage is the thing to watch.

Volumes, Kalshi on 30 September: about **$2.065B**, split 59.5% parlays, 19.2% sports, 16.5% crypto. Trailing seven-day: Kalshi $17.0B, Polymarket US $2.95B, DKeX $613M, CDNA $499M, Novig $445M.

One survey figure belongs in the ledger. A consumer-finance site reported **79% of prediction-market users lost money** in the past year; 27% lost more than $500; 44% use the products for extra income. That is a retail-harm number, not a trading signal.

### The forecasting paper

A small open model, trained end to end on a search-and-forecast scaffold over 2,100+ resolved Polymarket questions, reached a soft-Brier of **0.254** against **0.256** for a frontier model, at about **5% of the cost** — $0.011 against $0.24 per question. Calibration error fell 31%. Search attempts fell from 3.8 to 2.25 per rollout.

Read the authors' own caveat, because it is the point. **They state plainly that no scaffold reliably beats the market without non-public information, which is why they withhold the market price.** A calibrated forecaster is not an edge.

The reusable parts are the three-layer leak filter — domain blocklist, date filter, per-result judge — and the Brier-score reward. Both are patterns, not products.

**Cemini posture:** FILE. **No level to arm. Never auto-arm. Never write `watches.json`. No pm scp. No auto-submit.**
