---
title: Architecture - agents (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave5]
keywords: [Cemini-Financial-Suite, /opt/cemini, 8faf94e]
deploy-root: /opt/cemini
scanned-commit: 8faf94e
provenance: prod-briefs-out-architecture-2026-06-01-wave5
ai-first: true
module: agents
path: agents/
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

Prod `agents` @ 8faf94e.

# agents — LangGraph Brain Orchestrator

Small top-level package (10 Python files) hosting the **primary brain cycle** implemented as a LangGraph `StateGraph`. Docker service `brain` builds from `docker/Dockerfile.brain` and runs this orchestrator.

## Key files

<!-- @generated:start -->
| File | Size (approx) | Role |
|------|---------------|------|
| `orchestrator.py` | ~62 KB | Main graph: watchlist, regime, signal publish, wiki context |
| `regime_gate.py` | ~6 KB | Macro regime thresholds, catalyst patterns |
| `exit_decision.py`, `exit_state.py` | small | Exit-decision agent path (recent brain feature per git mine) |
| `scenarios/` | dir | Scenario fixtures / tests |
<!-- @generated:end -->

## Dependencies (from `orchestrator.py` imports)

- `langgraph.graph.StateGraph`
- `core.intel_bus.IntelReader`
- `cemini_contracts` — `TradeSignalEnvelope`, `IntelPayload`, `PlaybookRegimePayload`, `safe_validate`
- `core.orchestrator_wiki_context`, `core.wiki_enforcement`
- `agents.regime_gate`
- Optional: `services.llm_analyst.conductor_client.ConductorClient` (macro overlay from librarian conductor)
- Optional: `services.llm_analyst.autots_client.read_panel_from_redis` when `AUTOTS_ENABLED`
- Optional Tree-of-Thought path when `TOT_ENABLED=true`

## Publish path

| Env / function | Role |
|----------------|------|
| `ENABLE_BRAIN_PUBLISH` | When true, `publish_signal_to_bus` publishes to Redis channel **`trade_signals`** |
| `publish_signal_to_bus` | Validates via `safe_validate(TradeSignalEnvelope, …)` before publish |
| `EXECUTION_CARD_ENABLED` | Optional execution-card branch inside publisher |
| `core/wiki_enforcement` | May abort cycle if wiki policy fails (`log_enforcement_abort`) |

Exits also publish to `trade_signals` (sync publish on module Redis client).

## Runtime environment (`docker/compose.intelligence.yml`)

Brain container sets `REDIS_HOST=redis`, `DB_HOST=postgres`, `ENABLE_BRAIN_PUBLISH=true`, tiered symbol env vars (`BRAIN_V2_*`), metrics on port 9101.

## Signal path (documented in root README)

Three cooperating engines on Redis pub/sub: **Brain (LangGraph)**, **QuantOS**, **Kalshi by Cemini**. Agents package implements the Brain leg; publishes validated envelopes for EMS consumption.

## @user notes
