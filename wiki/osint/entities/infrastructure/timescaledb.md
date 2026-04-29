---
title: TimescaleDB
type: entity
tags: [infrastructure, database, time-series, postgres]
keywords: []
related:
  - sources/3-10-cryptographic-research.md
  - sources/3-18-git-3.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-19-telegram-discord-research.md
  - sources/3-19-timescaledb-optimization-for-trading-platform.md
  - sources/3-9-pm-research.md
  - sources/forex-research-3-18.md
  - sources/osint-prediction-markets-trading-architecture.md
  - concepts/cryptographic-audit-trail.md
  - entities/infrastructure/pgvector.md
  - entities/infrastructure/redis.md
  - entities/infrastructure/polars.md
  - sources/4-5-links-2.md
  - sources/pta-metric-anchoring-ssrn-4549819.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @sources/3-10-cryptographic-research.md
- @sources/3-18-git-3.md
- @sources/3-19-ip-sale-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-19-telegram-discord-research.md
- @sources/3-19-timescaledb-optimization-for-trading-platform.md
- @sources/3-9-pm-research.md
- @sources/forex-research-3-18.md
- @sources/osint-prediction-markets-trading-architecture.md
- @concepts/cryptographic-audit-trail.md
- @entities/infrastructure/pgvector.md
- @entities/infrastructure/redis.md
- @entities/infrastructure/polars.md

## Raw Concept

Synthesized from 9 source(s) referencing this entity across the Cemini research corpus. Category: infrastructure.

## Narrative

TimescaleDB is the time-series extension for PostgreSQL, Cemini's primary
persistence layer for tick data, order-flow, alt-data feeds, and strategy
P&L. It appears in 9 of the corpus sources — the most-referenced
infrastructure component after Kalshi.

Architectural choices documented across the 3-19 TimescaleDB optimization
research and crypto-integration audit:
- **Hypertables** partitioned by time (1-day chunks) with per-asset
  space partitioning; continuous aggregates precompute 1m/5m/1h/1d bars.
- **Compression policy** — tick data older than 7 days compresses with
  segment-by `(symbol)` + order-by `time DESC`, yielding ~12–18x storage
  reduction on forex and equities feeds.
- **Retention policy** — raw ticks dropped at 180 days; continuous
  aggregates retained indefinitely.
- **Cryptographic audit integration** — `[RETRACTED 2026-04-24 Track C]` per @concepts/cryptographic-audit-trail.md (J pass) and re-confirmed by K4 + K5 server probes: **pg_tamperlog extension is not installed**, **pymerkle is not in deps**, **OpenTimestamps integration is not deployed**. The architectural-integration claim in this bullet was a wiki synthesis error from prescriptive Cemini-internal blueprints (3-10-cryptographic-research, 3-9-pm-research's VCP/SCITT/Merkle prescription). The TimescaleDB tick-storage layer is real; the cryptographically-anchored audit-trail layer wrapping it is build-spec, not deployed.

## Snippets

*(populate as source stubs are deep-read.)*
