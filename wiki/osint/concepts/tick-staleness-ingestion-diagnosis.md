---
title: Tick staleness ingestion diagnosis — SIP/TRF semantics and prod SLOs
type: concept
tags: [concept, market-data, latency, alpaca, arctic, k77]
keywords: [tick-staleness, SIP, TRF, receive-latency, market_ticks, equity_bars, R14, R15]
related:
  - sources/low-latency-tick-staleness-diagnosis-2026-05-28.md
  - concepts/production-trading-blind-spots.md
  - concepts/clob-rate-limit-mitigation-strategies.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @sources/low-latency-tick-staleness-diagnosis-2026-05-28.md
- @concepts/production-trading-blind-spots.md
- @concepts/clob-rate-limit-mitigation-strategies.md — REST polling staleness

## Raw Concept

K77: operational diagnosis for R14 (Alpaca extend) + R15 (tick path health).

## Narrative

### Prod checklist (Phase 0 informed)

| Check | Artifact | Pass |
|-------|----------|------|
| Arctic last bar | `equity_bars` max date | > 2026-05-27 after backfill |
| CAGG freshness | `market_ticks_1min` latest bucket | < 2 min during RTH |
| Staleness metric | `now() - last_receive_ts` per symbol | p99 < 15 min budget |
| TRF filter | overnight print flag | exclude from NBBO signals |

### Scripts

- `scripts/backfill_arctic_equity_extend.py` — closes 2017 gap (R14)
- Monitor `alpaca_ingestor` container + WS upgrade path (R15)

## Snippets

> Use receive-time minus exchange-time histograms, not mean latency alone. [Source: Low-Latency Tick Staleness Diagnosis.docx]
