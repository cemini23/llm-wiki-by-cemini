---
title: Cheniere Energy (LNG)
type: entity
tags: [ticker, energy, lng, options-flow, earnings]
keywords: [LNG, Cheniere Energy, CCL Stage 3, Corpus Christi, Sabine Pass, Unusual Whales]
related:
  - sources/lng-cheniere-uw-earnings-preview-2026-07-29.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
---

## Relations

- @sources/lng-cheniere-uw-earnings-preview-2026-07-29.md — UW + IR + opencli desk pull (2026-07-29)
- Laptop brief (gitignored): `briefs/2026-07-29_lng-cheniere-uw-earnings-preview.md` — skill_audit PASS 100
- Canvas: `lng-cheniere-uw-earnings-research`

## Raw Concept

Entity page for **Cheniere Energy, Inc. (NYSE: LNG)** prompted by operator desk request for Unusual Whales options flow + dark pool + earnings preview ahead of **Q2’26 results (Thu 2026-08-06 BMO)**. Synthesis from UW REST (tipdrop-scanner key on cemini-prod), Cheniere IR, opencli socials. Not on CeminiSuite active 30-ticker watchlist.

## Narrative

**Cheniere** is the leading U.S. LNG producer/exporter (~55 mtpa operating + >6 mtpa under construction) via Sabine Pass (CQP) and Corpus Christi. UW as of 2026-07-29: market cap ~**$52.8B**, next earnings **2026-08-06 premarket**, beta **−0.53**, has_dividend true, tag `altenergy`.

### Spot / vol (2026-07-29 RTH)

- Close **$258.61** (+2.55%) after Jul 27–28 washout from Jul 24 high ~$277 (~−6.6% drawdown from high).
- IV **37.4%** · IV rank **~60** · RV **~34%**. Short-dated IV rich into the print (7d IV ~**93rd** percentile; ~±4.4% implied 7d move).

### Earnings / financials

- Company timing PR (Jul 9): release **Aug 6 BMO**; call **11:00 a.m. ET**.
- Street EPS ~$2.93–$3.05 · revenue ~$4.9B; UW est. EPS **$3.13** (UW historical EPS surprises are noisy vs company Adj. figures).
- Q1’26 (May 7): revenue **$5.87B**, Consol. Adj. EBITDA **$2.33B**, DCF **$1.67B**, GAAP net loss **−$3.50B** (deriv. MTM). Raised FY26 Adj. EBITDA guide to **$7.25–$7.75B** and DCF to **$4.75–$5.25B**.
- Prefer Adj. EBITDA / DCF over GAAP EPS for monitoring.

### CCL Stage 3 ops

- Train 5 SC Mar 2026; Trains 6–7 SC expected by YE26.
- FERC Jul 28 authorized **warm-end feedgas** on Train 7 (final midscale train). Ops chatter: cold-end next → commercial ops early–mid September.

### UW flow / dark pool (pulled 2026-07-29)

- 14d flow-alerts ~$2.7M premium · **~64% calls**; notable repeated **Nov $240 put sweeps**.
- Session options volume light vs 30d avg; **bearish premium > bullish** that day ($620k vs $444k).
- Dark pool ~$53M notional dominated by mid + close **AVG / PRIOR_REF** prints — not a clean accumulation signal.
- Insider UW aggregate 2026 YTD: ~$58M sells / $0 buys (routine liquidity read).

### Social pulse

- X: Train 7 FERC + Corpus N₂ feedgas quality (~1.4%); commodity LNG headlines pollute `$LNG` keyword search.
- Reddit: thin Cheniere-specific thesis density.

### Watch into Aug 6

1. Adj. EBITDA / DCF vs raised FY bands  
2. Train 6 first LNG + Train 7 cold-end / SC timing  
3. Short-dated IV crush vs realized move  
4. Nov $240 put follow-through  

**Compliance:** Observational desk notes only. Not investment advice. CFTC 4.41.

## Snippets

- "plans to issue its earnings release with respect to second quarter 2026 financial results on Thursday, August 6, 2026 before the market opens" — Cheniere timing PR (Jul 9, 2026)
- Q1 raised Consol. Adj. EBITDA guidance to $7.25–$7.75B — Cheniere Q1’26 results PR (May 7, 2026)

## Dead Ends

- Prod-mcp down during pull — used UW REST directly with tipdrop key.
- Brave Search monthly quota exhausted — IR + opencli + WebSearch used instead.
- `briefs/` path is gitignored; this entity page is the tracked wiki anchor.
