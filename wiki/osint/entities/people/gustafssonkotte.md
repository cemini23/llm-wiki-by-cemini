---
title: "@Gustafssonkotte — Polymarket 5-minute BTC UpDown bot operator (multi-module conflict-detector pattern)"
type: entity
tags: [entity, person, polymarket-bot-operator, updown-bot, conflict-detector, chainlink-data-streams, k55]
keywords: [gustafssonkotte, polymarket-btc-5min-bot, multi-module-conflict-detector, broken-data-corruption-debugging, phantom-win-fix, chainlink-data-streams-execution-via-polymarket-clob]
related:
  - sources/gustafssonkotte-cheat-code-position-already-2026-05-24.md
  - sources/trading-posts-compilation-38-2026-05-26.md
  - sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
  - concepts/polymarket-three-quadrant-blacklist-microtrend.md
  - concepts/polymarket-btc-already-position-gate.md
  - concepts/multi-module-bot-conflict-detector-pattern.md
  - concepts/polymarket-bot-architecture.md
  - sources/trading-posts-compilation-k84-2026-05-30.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - entities/tools/chainlink-data-streams.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-20
updated: 2026-05-26
---

## Relations

- @sources/trading-posts-compilation-38-2026-05-26.md — K67 Post 32 (FOK vs 12s resting fill)
- @sources/gustafssonkotte-cheat-code-position-already-2026-05-24.md — K62 “cheat code” pivot (position-already gate)
- @concepts/polymarket-btc-already-position-gate.md — K62 synthesized pattern
- @sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md — K57 Post 2 (quadrant/blacklist/micro-trend)
- @concepts/polymarket-three-quadrant-blacklist-microtrend.md — K57 synthesis
- @sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md — Post 3 source
- @concepts/multi-module-bot-conflict-detector-pattern.md — synthesized concept
- @concepts/polymarket-bot-architecture.md — fourth independent operator confirming the broader bot-discipline lessons
- @concepts/polymarket-updown-bot-taxonomy.md — short-resolution UpDown market specialist
- @entities/tools/chainlink-data-streams.md — price-feed oracle his bot uses (separate from execution venue)

## Raw Concept

Pseudonymous Polymarket bot operator publishing a debugging post-mortem + architectural rewrite of a BTC 5-minute UpDown bot. K55 ingest source. Documents the **broken-data corruption** failure mode (phantom WINs in logs, no-op risk gates) and the **multi-module conflict-detector** fix — patterns that generalize beyond his specific market.

## Narrative

### Handle

X / Twitter: **@Gustafssonkotte**

### Bot description

- **Market**: Polymarket 5-minute BTC Up/Down markets.
- **Stack**: Python, Chainlink Data Streams for BTC price feed, Polymarket CLOB for execution, multi-exchange WebSocket feeds (Binance/Bybit/OKX/Coinbase) for the levels-and-walls module, Ubuntu VPS.
- **Schedule**: weekday trading hours (Moscow time); weekends fully blocked. Bot stays running during off-hours but blocks new entries (accumulates state for the next session).

### Architectural distinctives

1. **Multi-module conflict-detector**: three modules (trend, levels, momentum) each output `(probability, strength)`; `spread > THRESHOLD → SKIP`. See `@concepts/multi-module-bot-conflict-detector-pattern.md`.
2. **Time-aware sizing**: position size scales by minutes-left-in-candle (5-min markets have a predictability arc).
3. **Price-feed separate from execution venue**: Chainlink Data Streams for truth, Polymarket CLOB for execution. No exchange API in the BTC-pricing path.
4. **Polymarket exports as source-of-truth for stats** — never the bot's internal counter.

### Reported performance (single-day post-rewrite [TENTATIVE])

| Phase | Trades | WR | Direction-correct | P&L |
|---|---|---|---|---|
| Old (2w, broken data) | 17 | 41% | 47% | red |
| v4 (day 1, clean) | 33 | 60% | 60% | green |

Author goal: 70% over next 100 trades. Symmetry between UP-side / DOWN-side fills is the more interesting feature than the absolute WR (old bot longed a falling market 7× in a row — systematic skew).

### Why Cemini cares

- **Third independent operator** (after @0x_Punisher and @adiix_official) corroborating the **execution > strategy** lesson.
- **Conflict-detector pattern** is portable to any Cemini multi-signal strategy (UpDown, sports consensus, GARCH × Markov).
- **Chainlink Data Streams as oracle separate from venue** is a structural pattern Cemini should explicitly document and consider using.

### Caveats

- Single-day post-rewrite sample (33 trades). WR claim is not statistically robust yet — the author is explicit.
- Pseudonymous; no on-chain identity verification.
- No promotional layer in the post itself (no Telegram channel, no paid product). One of the cleaner operator write-ups in the K55 batch.
