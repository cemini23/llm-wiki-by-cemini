---
title: Redis
type: entity
tags: [infrastructure, cache, pubsub, streaming]
keywords: []
related:
  - sources/3-18-crypto-integration-technical-audit.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-19-telegram-discord-research.md
  - sources/3-9-pm-research.md
  - sources/forex-research-3-18.md
  - concepts/scatter-gather-topology.md
  - entities/infrastructure/timescaledb.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-18-crypto-integration-technical-audit.md
- @sources/3-19-ip-sale-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-19-telegram-discord-research.md
- @sources/3-9-pm-research.md
- @sources/forex-research-3-18.md
- @concepts/scatter-gather-topology.md
- @entities/infrastructure/timescaledb.md

## Raw Concept

Synthesized from 6 source(s) referencing this entity across the Cemini research corpus. Category: infrastructure.

## Narrative

Redis is the in-memory pub/sub and cache layer between Cemini's market-
data ingestion and strategy/execution layers. Sits in front of TimescaleDB
as a hot path for the current tick and a fanout to strategy subscribers.

Documented topology across the corpus:
- **Pub/sub channels** per venue + symbol (e.g., `oanda:EURUSD`,
  `hyperliquid:BTC-PERP`) feed the LangGraph scatter-gather nodes.
- **Redis Streams** used for durable event logs where at-least-once
  delivery matters (order submissions, fills) with consumer groups
  backed by the risk engine.
- **Rate-limit buckets** (INCR + EXPIRE) guard outbound API calls to
  Telegram (Telethon), Finnhub, Open-Meteo, and Kalshi.
- `[RETRACTED 2026-04-24]` An earlier bullet here claimed Redis holds a
  "session cache for Ollama prompt-completion pairs" — Ollama is not
  deployed on Cemini (see @entities/infrastructure/ollama.md), so this
  cache path does not exist. If a local-LLM is later stood up, the
  claim can be re-evaluated at that time.

## Snippets

*(populate as source stubs are deep-read.)*
