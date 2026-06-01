---
title: Architecture - cemini_contracts (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave4]
keywords: [Cemini-Financial-Suite, /opt/cemini, e8fd49f]
deploy-root: /opt/cemini
scanned-commit: e8fd49f
provenance: prod-briefs-out-architecture-2026-06-01-wave4
ai-first: true
module: cemini_contracts
path: cemini_contracts/
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

Prod `cemini_contracts` @ e8fd49f.

# cemini_contracts — Typed cross-service envelopes

Foundation layer: **no internal repo imports** (`scripts/check_imports.py`). All higher layers validate against these Pydantic models via `cemini_contracts.safe_validate`.

## Domain groupings

<!-- @generated:start -->
| Domain | Example modules | Consumers |
|--------|-----------------|-----------|
| **Trade & execution** | `trade.py`, `execution_decision.py`, `broker_rejection.py`, `slippage.py` | `agents/`, `ems/`, `core/ems/` |
| **Intel & playbook** | `intel.py`, `playbook.py`, `regime.py`, `signals.py` | `core/intel_bus`, `trading_playbook`, `cemini_mcp` |
| **Prediction markets** | `polymarket.py`, `pm_btc_updown.py`, `pm_kl_stat_arb.py`, `polymarket_lp_rewards.py`, `prediction_market.py` | `services/llm_analyst`, PM scripts |
| **Kalshi & weather** | `kalshi.py`, `kalshi_weather_bracket.py`, `weather_ensemble.py`, `weather_nwp_stack.py` | Kalshi engine, weather systemd path |
| **Agents & governance** | `agent_budget.py`, `agent_lifecycle_event.py`, `byzantine_consensus.py`, `hitl_approval.py`, `rbac.py` | `services/`, debate, HITL gates |
| **Risk & portfolio** | `risk.py`, `risk_governor.py`, `portfolio.py`, `position.py` | EMS, `risk_governor` service |
| **Research & ML** | `backtest.py`, `walk_forward.py`, `rl_contracts.py`, `ensemble.py` | `research/`, `rl_training/` |
| **Ops & audit** | `audit.py`, `operator_alert.py`, `pipeline_phase.py`, `tool_adopt_registry.py` | Archives, phase gates |
| **Wiki** | `wiki_search.py` | `cemini_mcp`, `core/wiki_enforcement` |
<!-- @generated:end -->

## Critical envelopes

| Type | Used for |
|------|----------|
| `TradeSignalEnvelope` | Brain → Redis `trade_signals` → EMS (`decision` field added @ `17cf48e`) |
| `IntelPayload` | `intel:*` Redis values |
| `PlaybookRegimePayload` | Playbook snapshot publishing |
| `GovernorDecision` / `OrderRequest` | EMS ↔ `risk_governor` HTTP |

## Versioning

`strategy_logic_versions.py` — `current_version_id()` referenced from `agents/orchestrator.py` when publishing signals.

## @user notes
