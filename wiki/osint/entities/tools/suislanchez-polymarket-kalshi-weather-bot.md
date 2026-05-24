---
title: suislanchez polymarket-kalshi-weather-bot — cross-venue weather + BTC microstructure
type: entity
tags: [entity, tool, polymarket, kalshi, weather-trading, steal-from, conditional-go, k60]
keywords: [suislanchez, polymarket-kalshi-weather-bot, kxhigh, gfs-ensemble, brier-score, kelly, cross-venue, k60]
related:
  - sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/kalshi-api-reference.md
  - concepts/ensemble-weather-forecasting.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-24
updated: 2026-05-24
---

## Relations

- @sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md — K60 URL cluster re-audit (403★; missed on first pass)
- @concepts/polymarket-weather-trading-strategy.md — weather temperature strategy parent
- @concepts/cross-venue-arbitrage-pattern.md — Kalshi KXHIGH + Polymarket in one scanner (weather leg, not BTC arb)
- @concepts/kalshi-api-reference.md — KXHIGHNY/CHI/MIA/LAX/DEN series auto-discovery
- @concepts/ensemble-weather-forecasting.md — GFS ensemble probability layer
- @concepts/cemini-license-posture.md — README MIT badge vs missing LICENSE file

## Raw Concept

K60 v4 first pass aggregated URLs 11–20 as “duplicate stack reject.” Re-audit (2026-05-24): **`suislanchez/polymarket-kalshi-weather-bot`** (~403★) is the strongest **new** steal-from in the weather cluster — cross-platform weather + signal calibration — distinct from `@alteregoeth-ai/weatherbot` (Polymarket-only).

## Narrative

- **Repo**: [github.com/suislanchez/polymarket-kalshi-weather-bot](https://github.com/suislanchez/polymarket-kalshi-weather-bot) (~403★, pushed 2026-03-02)
- **Stack**: FastAPI backend + React/TypeScript dashboard + SQLite + APScheduler; free data sources (Open-Meteo GFS ensemble, exchange candles)
- **License**: README badge claims **MIT**; `gh api` returns **no LICENSE file** [CONFIRMED 2026-05-24] — treat as unlicensed until file appears; **pattern-extract only** for IP-sale path

### Distinctive patterns (Steal-from)

| Pattern | Detail | Cemini relevance |
|---------|--------|------------------|
| **Cross-venue weather** | Same GFS ensemble signal trades **Kalshi KXHIGH** tickers + Polymarket temperature bins | Direct fit for existing Kalshi + Polymarket prod adapters |
| **31-member GFS ensemble** | Open-Meteo ensemble → threshold exceedance probabilities | Extends 3-model ICON/GFS/ECMWF narrative with explicit ensemble count |
| **Signal calibration** | Tracks predictions vs outcomes; **Brier score** | Portable to `@concepts/reviewer-agent-inference-time-feedback.md` eval loop |
| **Kelly + caps** | Fractional Kelly (~15%) with per-trade caps | Same family as weatherbot; verify params independently |
| **Ops surface** | React dashboard, simulation mode, equity curves | Reference for internal weather-bot monitoring UI |

Secondary (non-weather): bundled **BTC 5-min Up/Down** microstructure scanner (RSI, VWAP, SMA composite) — overlaps Gustafsson/K55 BTC bot workstreams; harvest only if weather scope expands.

### Verdict: **Steal-from (CONDITIONAL-GO Phase-0)**

Phase-0 before any code import:

1. Confirm LICENSE file (README MIT claim is unreliable per K-series catalog mode).
2. Clone to `/tmp/suislanchez-weather-audit/` — map Kalshi KXHIGH discovery + ensemble probability code paths vs Cemini's existing Kalshi weather stub.
3. Extract **calibration + cross-venue scan loop** as design reference; do not install monolith on prod.

**Do not Adopt** until license verified and Phase-0 passes overlap check with in-house weather module.

## Snippets

> "Scans weather temperature markets on Kalshi (KXHIGH series) and Polymarket every 5 minutes. Uses 31-member GFS ensemble forecasts from Open-Meteo… Trades when edge > 8%." [Source: github.com/suislanchez/polymarket-kalshi-weather-bot README, retrieved 2026-05-24]
