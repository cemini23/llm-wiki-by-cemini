---
title: Polymarket LP weather guard
type: concept
tags: [concept, polymarket, lp-rewards, weather, risk]
keywords: [pre-resolution-exit, accidental-fill, PM_LP_WEATHER_PRE_RESOLUTION_EXIT_HOURS, temperature-bins]
related:
  - concepts/polymarket-lp-weather-market-discovery.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/polymarket-weather-trading-strategy.md
maturity: validated
created: 2026-05-26
updated: 2026-05-26
clusters: [polymarket, market-making, weather]
---

## Relations

- @concepts/polymarket-lp-weather-market-discovery.md — weather LP discover pass
- @concepts/polymarket-lp-rewards-farming.md — K55 default 14d / 40–60¢ gates
- @concepts/polymarket-lp-bot-phase0-spec.md — Phase-0 LP bot spec
- @concepts/polymarket-weather-trading-strategy.md — directional entry window (orthogonal)

## Raw Concept

Accidental-fill risk when LP-posting on **same-day temperature bins** (0–3d resolution). Prod guard shipped 2026-05-26 with weather LP discover pass.

## Narrative

Standard LP discovery targets long-dated, mid-band politics/geopolitics. Daily temperature bins have **incentive pools** but can move one-way as observations accumulate.

**Guard:** `PM_LP_WEATHER_PRE_RESOLUTION_EXIT_HOURS` (default **12**) — inventory flattener force-exits weather-tagged positions inside that window before resolution, even below normal inventory caps. Runs in LP `tick` and `inventory-flattener` sidecar (~5m).

**Enable:** `PM_LP_INCLUDE_WEATHER=true` on `lp-rewards-bot` + `inventory-flattener`.

Code: `services/polymarket_lp_weather.should_weather_pre_resolution_exit`, `services/llm_analyst/polymarket_inventory_flattener.py`.

Directional K66 weather (`strategies/polymarket_weather.py`) remains separate; do not conflate ensemble edge with LP rewards.

## Snippets

> K55: min 14d resolution for default LP — weather pass is an explicit operator override, not default K55 behavior. [Source: @concepts/polymarket-lp-rewards-farming.md]
