---
title: Polymarket LP weather market discovery
type: concept
tags: [concept, polymarket, lp-rewards, weather, geo, prediction-markets]
keywords: [lp-rewards, weather-markets, sampling-simplified-markets, highest-temperature, maker-rebate, PM_LP_INCLUDE_WEATHER, market-discovery]
related:
  - concepts/polymarket-lp-weather-guard.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/ensemble-weather-forecasting.md
maturity: validated
created: 2026-05-26
updated: 2026-05-26
clusters: [polymarket, market-making, weather]
---

## Relations

- @concepts/polymarket-lp-weather-guard.md — pre-resolution exit on accidental LP fills
- @concepts/polymarket-lp-rewards-farming.md — maker-side LP strategy hub
- @concepts/polymarket-lp-bot-phase0-spec.md — Phase-0 bot design
- @concepts/polymarket-weather-trading-strategy.md — directional weather **edge** (separate bot)
- @concepts/ensemble-weather-forecasting.md — NWP ensemble path (orthogonal)

## Raw Concept

Prod handoff (2026-05-26) plus retail field validation from X @GnatykA (weather LP lifehack thread, operator screenshot). Documents how the Cemini **LP rewards bot** discovers **daily temperature** markets when `PM_LP_INCLUDE_WEATHER=true`.

## Narrative

When `PM_LP_INCLUDE_WEATHER=true`, the LP rewards bot adds a **second discovery pass** alongside standard long-dated market discovery. It does **not** reuse the directional weather bot’s Gamma city/slug crawler.

### Scan pipeline

1. Paginate CLOB `GET /sampling-simplified-markets` for active **liquidity-reward** rows.
2. Enrich via Gamma `markets?condition_ids=` for `slug`, `volume24hr`, resolution time.
3. Optional FLOX Redis book for live mid / volume.
4. Rank by total `rewards_daily_rate` (USDC/day); merge with standard pass (dedupe by `condition_id`, higher pool wins).

Prod egress: **Helsinki FI SOCKS** (`cemini-egress-fi`) for geoblocked CLOB/Gamma.

### Geo slug filter

Gamma `slug` must match:

```text
highest-temperature | lowest-temperature | temperature-in-
```

Example: `highest-temperature-in-seoul-on-may-26-2026`.

LP discovers whatever temperature markets appear in the **rewards sampling feed**, not a fixed US city list (`RESOLUTION_STATIONS` is directional K66 only).

### Weather vs standard LP gates

| Gate | Standard LP | Weather LP pass |
|------|-------------|-----------------|
| Min days to resolution | 14 | 0 |
| Max days to resolution | — | 3 |
| Min 24h volume | $40k | $5k |
| YES mid band | 0.40–0.60 | 0.20–0.80 |
| Min forecast daily USDC | $1 | $0.50 default |

Env: `PM_LP_WEATHER_*` in `services/polymarket_lp_weather.py`; orchestration in `scripts/run_polymarket_lp_rewards.py` (`_discover_weather_markets`).

### Retail field validation (2026-05-26) `[CONFIRMED — screenshot + X thread]`

Independent operator @GnatykA claimed **~5% per day** on weather via “limit buy + limit sell at 99¢.” Screenshot evidence shows a different mechanism:

| Observation | Implication |
|-------------|-------------|
| Seoul: highest temp **25°C+** on May 26 — Sell No **30¢**, 16 shares, **$4.80** | Same-day temp bin; mid inside 0.20–0.80 |
| Warsaw: highest temp **26°C** on May 26 — Sell Yes **48¢**, 10 shares, **$4.80** | Non-US cities appear in incentivized books |
| **Maker rebate $5.96** between trades | Rebate can exceed single-leg notional; track separately from `rewards_daily_rate` |
| No visible 99¢ fills | Do **not** tune bot for viral 99¢ exit; use **two-sided quotes near mid** |

`[TENTATIVE]` “5% per day” is on **deployed maker capital**, not total wallet — not independently verified.

### Ops notes

- Weather pass often returns **0 markets** if no incentivized temp bins sit in mid band that day.
- `PM_LP_LIVE_POST=false` after pilot — discovery can run without quoting.
- Prod briefs: `briefs/2026-05-26_polymarket-lp-weather-market-discovery-osint-handoff.md`, `briefs/2026-05-26_polymarket-lp-weather-retail-validation-gnatyk-cemini.md` (on `cemini-prod`; local `briefs/` gitignored).

### Discovery tuning backlog (from retail brief)

- **P0:** Log reject reasons when weather discover returns 0.
- **P1:** Report `maker_rebate_usd` separately in LP daily P&L.
- **P3:** Shadow fixtures for `seoul` / `warsaw` slug shapes.

## Snippets

> "Retail validation 2026-05-26: Seoul/Warsaw same-day temp bins; maker rebate $5.96 > individual $4.80 sells; mids 30¢/48¢." [Source: X @GnatykA thread + operator screenshot; prod brief 2026-05-26]

> Code: `discover_reward_markets(..., theme_predicate=is_weather_lp_theme)` — `services/polymarket_lp_market_discovery.py`
