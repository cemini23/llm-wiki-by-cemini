---
title: "LNG / Cheniere UW earnings preview desk pull (2026-07-29)"
type: source
tags: [equity-research, options-flow, dark-pool, cheniere, lng, earnings]
keywords: [LNG, Cheniere, Unusual Whales, CCL Stage 3, Train 7, Aug 6]
related:
  - entities/tickers/lng.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
read_status: deep-read
---

## Relations

- @entities/tickers/lng.md — ticker entity synthesized from this pull

## Raw Concept

- **Title**: Cheniere Energy (LNG) — Unusual Whales multi-endpoint + IR + opencli social preview into Q2’26 earnings
- **Author**: Cemini desk (operator-commissioned)
- **Type**: live market-data pull + primary IR cross-check
- **Location**: laptop brief `briefs/2026-07-29_lng-cheniere-uw-earnings-preview.md` (gitignored); UW JSON ephemeral `/tmp/lng_uw/`; canvas `lng-cheniere-uw-earnings-research`
- **Retrieved**: 2026-07-29
- **Read-status**: deep-read

## Narrative

Desk research session for **NYSE:LNG** ahead of **2026-08-06 BMO** earnings. Unusual Whales REST authenticated via tipdrop-scanner key on cemini-prod (`/opt/tipdrop-scanner/.env`). Prod-mcp was down. Cross-checked Cheniere IR timing PR + Q1’26 results/guidance raise, FERC Train 7 warm-end feedgas (Jul 28), and opencli twitter/reddit/google news/barchart.

Key instrumented endpoints: info, flow-alerts, darkpool, iv-rank, interpolated-iv, options-volume, greek-exposure, earnings, insider, congress, ohlc, max-pain, expiry-breakdown.

Synthesis lives on `@entities/tickers/lng.md` and the laptop brief (skill_audit PASS 100).

## Snippets

- UW info: `next_earnings_date=2026-08-06`, `announce_time=premarket`, marketcap ≈ $52.8B
- Session RTH close $258.61 (+2.55%); IV 37.4% / IVR ~60; 7d IV ~93rd percentile
- Dark pool ~$53M Jul 29 dominated by close AVG/PRIOR_REF prints

## Dead Ends

- Brave Search API monthly quota exhausted mid-session
- Several UW paths 404 (gex alias, short-data, news, dividend, institutional, anomalous)
