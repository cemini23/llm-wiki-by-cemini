---
title: Architecture - Kalshi by Cemini (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave5]
keywords: [Cemini-Financial-Suite, /opt/cemini, 8faf94e]
deploy-root: /opt/cemini
scanned-commit: 8faf94e
provenance: prod-briefs-out-architecture-2026-06-01-wave5
ai-first: true
module: Kalshi by Cemini
path: Kalshi by Cemini/
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md

## For future Claude

Prod `Kalshi by Cemini` @ 8faf94e.

# Kalshi by Cemini — Prediction Market Engine

Prediction-market trading for Kalshi: multi-domain analysis (BTC, Fed, weather, geo) with Kelly sizing and RSA-signed REST execution. Entry: `Kalshi by Cemini/README.md`.

## Modules (from README)

<!-- @generated:start -->
| Module | File | Purpose |
|--------|------|---------|
| Autopilot | `modules/execution/autopilot.py` | Main 30s scan-and-execute loop |
| SatoshiAnalyzer | `modules/satoshi_vision/analyzer.py` | Multi-timeframe BTC TA |
| PowellAnalyzer | `modules/powell_protocol/analyzer.py` | Treasury / rate decisions |
| WeatherAnalyzer | `modules/weather_alpha/analyzer.py` | NWS/OpenWeather consensus |
| SocialAnalyzer | `modules/social_alpha/analyzer.py` | X/Twitter sentiment (simulated data noted in README) |
| MuskPredictor | `modules/musk_monitor/predictor.py` | Tweet velocity model |
| GeoPulseMonitor | `modules/geo_pulse/monitor.py` | GDELT via Redis `intel:conflict_events` |
| MarketRover | `modules/market_rover/rover.py` | Cross-ref QuantOS sentiment ↔ Kalshi |
| CapitalAllocator | `modules/execution/allocator.py` | Kelly position sizing |
<!-- @generated:end -->

## Documented data gaps (README — not invented)

- `social_alpha` — hardcoded simulated tweets unless live X API wired
- `powell_protocol` — mock bracket prices noted
- `weather_alpha` — simulated order book prices noted
- `geo_pulse` — prefers live GDELT from Redis; fallbacks documented in README

## Runtime services

| Service | Compose file | Container |
|---------|--------------|-----------|
| `kalshi_autopilot` | `docker/compose.execution.yml` | `kalshi_autopilot` |
| `rover_scanner` | same | market discovery / logit assessments |

EMS mounts `Kalshi by Cemini/private_key.pem` → `/app/private_key.pem` (`compose.execution.yml`). Top-level `ems/kalshi_rest.py` implements REST v2 client used by EMS service.

## EMS / contracts touchpoints

- `cemini_contracts/kalshi.py`, `kalshi_weather_bracket.py`, PM cross-venue contracts
- `core/kalshi_slippage.py`, `core/ems/adapters/kalshi_rest.py`

## @user notes
