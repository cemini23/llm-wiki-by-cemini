---
title: Architecture - trading_playbook (prod)
type: architecture-module
module: trading_playbook
path: trading_playbook/
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, gap-close]
keywords: [Cemini-Financial-Suite, /opt/cemini, de5ad93]
deploy-root: /opt/cemini
scanned-commit: de5ad93
provenance: prod-briefs-out-architecture-2026-06-01-gap-close
ai-first: true
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md — project hub
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md — MOC

## For future Claude

Prod module `trading_playbook` @ de5ad93; gap-close handoff.

# trading_playbook — Regime, risk observation & playbook intel

Docker service **`playbook`** (`docker/compose.intelligence.yml`). Default **5-minute** scan loop (`trading_playbook/runner.py`). Primary output: **`intel:playbook_snapshot`** on Redis (consumed by brain regime gate and MCP).

## Components (from `trading_playbook/README.md`)

<!-- @generated:start -->
| Component | File | Role |
|-----------|------|------|
| Macro regime | `macro_regime.py` | GREEN / YELLOW / RED (SPY vs EMA21/SMA50, JNK/TLT) |
| Signal catalog | `signal_catalog.py` | Six tactical detectors |
| Risk engine | `risk_engine.py` | Fractional Kelly, CVaR, drawdown |
| Kill switch | `kill_switch.py` | PnL velocity, rate, latency → emergency stop |
| Logger | `playbook_logger.py` | Postgres `playbook_logs` + JSONL archive + Redis |
| Runner | `runner.py` | Orchestrates cycle |
<!-- @generated:end -->

## Relationship to brain

`agents/regime_gate.py` reads `intel:playbook_snapshot` and **blocks BUY** when regime is YELLOW or RED. Brain and playbook are separate containers but coupled via Redis.

## Orders vs observation

- README states playbook **does not place orders** by default (observation + logging for RL corpus).
- `runner.py` optionally imports `core.ems.router` (**Step 86B**) for EMS routing when available — env-gated / feature path, not the main brain → `trade_signals` path.

## Signal paths (contrasted)

| Path | Channel / key | Producer | Consumer |
|------|---------------|----------|----------|
| Playbook intel | `intel:playbook_snapshot` | `playbook` | `brain`, `cemini_mcp` |
| Brain trades | `trade_signals` | `brain` (`ENABLE_BRAIN_PUBLISH`) | `ems` |

## Data outputs

- Postgres: `playbook_logs`
- JSONL: `/mnt/archive/playbook/` (EMS volume mount `../archives`)
- Redis: latest snapshot for intel bus

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - agents.md
- @projects/cemini-financial-suite/Architecture/Architecture - ems.md
- @projects/cemini-financial-suite/Architecture/Architecture - cemini_contracts.md — `playbook.py`, `regime.py`

## @user notes
