---
title: Architecture - QuantOS (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave5]
keywords: [Cemini-Financial-Suite, /opt/cemini, 8faf94e]
deploy-root: /opt/cemini
scanned-commit: 8faf94e
provenance: prod-briefs-out-architecture-2026-06-01-wave5
ai-first: true
module: QuantOS
path: QuantOS/
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

Prod `QuantOS` @ 8faf94e.

# QuantOS — Stock & Crypto Trading Engine

Equity and cryptocurrency engine within CeminiSuite. Documented entry point: `QuantOS/README.md`.

## Purpose

Market scanning, RSI-based signal generation, order execution helpers, and broker-agnostic portfolio logic. Runs historically as Docker `signal_generator` (QuantOS build context); **disabled by default** since 2026-02-24 as redundant with the main `brain` service (`docker/compose.intelligence.yml` comments).

## Key components (from QuantOS/README)

<!-- @generated:start -->
| Component | File | Purpose |
|-----------|------|---------|
| TradingEngine | `core/engine.py` | Main trading loop, bracket orders, sunset reports |
| QuantBrain | `core/brain.py` | RSI signal scoring |
| ExecutionEngine | `core/execution.py` | Buy/sell/bracket + paper mode |
| MoneyManager | `core/money_manager.py` | Score-based position sizing |
| RiskManager | `core/risk_manager.py` | Daily stop, position cap |
| MasterStrategyMatrix | `core/strategy_matrix.py` | Confluence: spikes + sentiment |
| AsyncScanner | `core/async_scanner.py` | Alpaca primary, Yahoo fallback |
| XOracle | `core/sentiment/x_oracle.py` | Trust scoring + FinBERT sentiment |
<!-- @generated:end -->

## Data flow

```
AsyncScanner → TradingEngine → QuantBrain (RSI)
  → MasterStrategyMatrix → ExecutionEngine → Broker adapter
```

## Broker adapters

Factory: `core/brokers/factory.py`; router: `core/brokers/router.py`. README lists Kalshi (active API), Robinhood, Alpaca (paper default), IBKR planned.

## Compose integration

| Service | Compose file | Status |
|---------|--------------|--------|
| `signal_generator` | `docker/compose.intelligence.yml` | Profile-gated; replicas 0 in Swarm |
| `brain` | same | Primary intelligence container (non-QuantOS Dockerfile) |

EMS references `QUANTOS_HOST=signal_generator` in `docker/compose.execution.yml` when co-scheduled.

## Relationship to suite

- Shares `cemini_contracts` and Redis intel patterns with `agents/` brain cycle.
- Kalshi engine (`Kalshi by Cemini`) cross-references QuantOS sentiment via MarketRover module per Kalshi README.

## @user notes
