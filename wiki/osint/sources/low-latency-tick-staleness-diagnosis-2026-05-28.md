---
title: Low-Latency Tick Staleness Diagnosis — Timestamps, TRF, eBPF, Disruptor
type: source
tags: [source, market-data, latency, alpaca, polygon, k77]
keywords: [tick-staleness, SIP, TRF, eBPF, LMAX-Disruptor, polygon, alpaca, R14, R15]
related:
  - concepts/tick-staleness-ingestion-diagnosis.md
  - concepts/production-trading-blind-spots.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/tick-staleness-ingestion-diagnosis.md
- @concepts/production-trading-blind-spots.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Low-Latency Tick Staleness Diagnosis |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/Low-Latency Tick Staleness Diagnosis.docx` |
| Retrieved | 2026-05-28 |
| Read-status | deep-read |

## Narrative

Diagnosing stale ticks in equity/crypto feeds:

- **Timestamp semantics:** exchange vs SIP vs receive-time; Polygon `sip_timestamp` vs Alpaca `t` field
- **TRF overnight anomaly:** off-exchange prints can look "fresh" but are stale for NBBO strategies
- **Validation:** 15-minute rolling max staleness budget; alert when p99 receive lag > threshold
- **Architecture:** LMAX Disruptor ring buffers, eBPF kernel latency probes for prod ingest path

Direct R14/R15: prod `market_ticks_1min` CAGG (Apr–May 2026) proves recent ingest exists but **Arctic equity_bars frozen 2017** — separate paths; extend Arctic backfill + tick freshness SLO on live adapter.

## Snippets

> Staleness is not monotonic with wall clock — TRF prints can reset freshness counters incorrectly. [Source: Low-Latency Tick Staleness Diagnosis.docx — paraphrase]
