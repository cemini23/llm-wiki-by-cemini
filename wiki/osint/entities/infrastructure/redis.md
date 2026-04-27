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
updated: 2026-04-26
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

**Deployed pub/sub topology** (server probe 2026-04-26 K5 against
`/opt/cemini/services/`, `/opt/cemini/cemini_mcp/`, and live
`PUBSUB CHANNELS *`): the **`intel:*` namespace** is the heavily-used
publisher channel family. **30+ channel names enumerated in code**:

- **Macro / FRED**: `intel:fred_credit_spread`, `intel:fred_fed_policy`, `intel:fred_labor`, `intel:fred_yield_curve`, `intel:fed_bias`, `intel:geopolitical_risk`, `intel:conflict_events`
- **Crypto-specific**: `intel:btc_sentiment`, `intel:btc_spy_corr`, `intel:btc_volume_spike`
- **Kalshi**: `intel:kalshi_liquidity_spike`, `intel:kalshi_oi`, `intel:kalshi_orderbook_summary`
- **FX**: `intel:fx:calendar`, `intel:fx:carry`, `intel:fx:tick:*`
- **EDGAR / Earnings**: `intel:edgar_alert`, `intel:earnings_calendar`
- **LLM / agent layer**: `intel:agent_weights`, `intel:llm_signal:*`, `intel:debate_rubric`, `intel:debate_verdict`, `intel:logit_assessments`
- **Aggregates**: `intel:bar`, `intel:conviction_composite`, `intel:ensemble_signal`, `intel:fuzzy_scalar`, `intel:capability_manifest_hash`

Plus two non-`intel:*` active publisher channels at probe time:
`emergency_stop`, `trade_signals`. (Note: `PUBSUB CHANNELS *` only
shows channels with active subscribers at the moment of probe — the
`intel:*` family is enumerated from code paths, where `IntelPublisher`
+ `IntelReader` design pattern lives in 6+ files
(`/opt/cemini/rl_training/integration.py`,
`/opt/cemini/services/conviction_aggregator.py`, etc.). This pattern
+ namespace is the strongest as-built confirmation in K5; see
@sources/3-9-pm-research.md "Prescribed-vs-deployed gap" for the full
enumeration.)

**Other Redis usage:**
- **Redis Streams** used for durable event logs where at-least-once
  delivery matters (order submissions, fills) with consumer groups
  backed by the risk engine.
- **Rate-limit buckets** (INCR + EXPIRE) guard outbound API calls to
  Finnhub, Open-Meteo, and Kalshi. *(Earlier bullet listed Telegram
  (Telethon) as a rate-limit target; `[RETRACTED 2026-04-26 K3 deep-read]`
  per @entities/data-sources/telethon.md — Telethon and the Telegram
  ingester are not deployed.)*
- `[RETRACTED 2026-04-24]` An earlier bullet here claimed Redis holds a
  "session cache for Ollama prompt-completion pairs" — Ollama is not
  deployed on Cemini (see @entities/infrastructure/ollama.md), so this
  cache path does not exist. If a local-LLM is later stood up, the
  claim can be re-evaluated at that time.

**Note on K4 finding**: K4 found that `intel:orderbook` and
`intel:sentiment` channel names specifically don't exist (correct as
narrowly scoped). K5 broadens that finding: the `intel:*` family
*does* heavily exist, just under different specific channel names than
what @sources/3-18-crypto-integration-technical-audit.md para 165 + 202
assumed.

## Snippets

*(populate as source stubs are deep-read.)*
