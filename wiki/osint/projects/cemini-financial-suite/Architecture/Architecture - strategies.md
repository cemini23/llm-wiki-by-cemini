---
title: Architecture - strategies (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave4]
keywords: [Cemini-Financial-Suite, /opt/cemini, e8fd49f]
deploy-root: /opt/cemini
scanned-commit: e8fd49f
provenance: prod-briefs-out-architecture-2026-06-01-wave4
ai-first: true
module: strategies
path: strategies/
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

Prod `strategies` @ e8fd49f.

# strategies — Sleeve logic implementations

Executable strategy code for **Polymarket**, PM↔KL stat arb, and shared risk helpers. Distinct from **`trading_playbook/`** (macro regime + equity signal catalog).

## Boundary

| Layer | Path | Role |
|-------|------|------|
| Playbook | `trading_playbook/` | SPY regime, 6 equity detectors, kill switch — **not** PM CLOB |
| Strategies | `strategies/` | PM weather, LP rewards, sniper, stat arb scanners |
| Contracts | `cemini_contracts/strategy_logic_versions.py` | Version id on published brain signals |
| Config gates | `conviction.yaml`, phase gates | User-gated — not documented here |

## Key modules (filename evidence)

| Module | Domain |
|--------|--------|
| `polymarket_weather.py`, `polymarket_weather_*.py` | Weather buckets, EMOS, falsification |
| `polymarket_lp_rewards.py` | LP maker logic |
| `pm_kl_stat_arb.py` | PM ↔ Kalshi stat arb |
| `polymarket_arb_scanner.py`, `polymarket_sniper_scanner.py` | Arb / sniper |
| `polymarket_near_resolution.py` | Near-resolution sleeve |
| `regime_kelly.py`, `liquidity_monitor.py` | Shared sizing / liquidity |

## Runtime

Invoked from **host scripts** (`scripts/pm_*`, `scripts/wc_*`) and **systemd timers** more often than from `brain` container. See @projects/cemini-financial-suite/Architecture/Architecture - Polymarket.md and @projects/cemini-financial-suite/Architecture/Architecture - deploy-systemd.md.

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - trading_playbook.md
- @projects/cemini-financial-suite/Architecture/Architecture - cemini_contracts.md

## @user notes
