---
title: Architecture - db ERD (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave5]
keywords: [Cemini-Financial-Suite, /opt/cemini, 8faf94e]
deploy-root: /opt/cemini
scanned-commit: 8faf94e
provenance: prod-briefs-out-architecture-2026-06-01-wave5
ai-first: true
module: db ERD
path: db/
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
  - projects/cemini-financial-suite/Architecture/Architecture - db.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md
- @projects/cemini-financial-suite/Architecture/Architecture - db.md

## For future Claude

Prod `db ERD` @ 8faf94e.

# db — Logical ERD & table ownership

Derived from `db/schema.sql` (52 `public` tables @ `de5ad93`). **No FK graph** in dump — relationships below are **logical** (producer → consumer), not enforced constraints.

## Domain map

```mermaid
flowchart TB
  subgraph market["Market data"]
    raw[raw_market_ticks]
    fx[fx_ticks]
    vol[vol_surface_log]
  end

  subgraph playbook["Playbook / regime"]
    pb[playbook_logs]
    sector[sector_rotation_log]
  end

  subgraph exec["Execution & trades"]
    th[trade_history]
    br[broker_rejection_log]
    cpt[crypto_perp_trades]
    kpt[kalshi_paper_trades]
  end

  subgraph intel["Intel & memory"]
    isl[intel_stream_log]
    ie[intel_embeddings]
    idl[intel_dead_letters]
    snap[situation_snapshots]
  end

  subgraph agents["Agents / RL"]
    ewl[ensemble_weights_log]
    awl[agent_weight_log]
    rawl[regime_adjusted_weight_log]
    atl[agent_trust_log]
    rld[rl_decisions]
    rle[rl_episodes]
    rlt[rl_training_runs]
  end

  subgraph pmkalshi["PM & Kalshi shadow"]
    psl[polymarket_shadow_log]
    ksl[kalshi_shadow_log]
    pmr[pm_bootstrap_results]
    klr[kl_bootstrap_results]
    spl[sleeve_pnl_log]
  end

  subgraph weather["Weather"]
    wef[weather_ensemble_forecasts]
    wtp[weather_threshold_probabilities]
  end

  subgraph macro["Macro / sentiment / geo"]
    fred[fred_observations]
    macro[macro_logs]
    geo[geopolitical_logs]
    sent[sentiment_logs]
  end

  subgraph audit["Audit & compliance"]
    aic[audit_intent_log]
    ahc[audit_hash_chain]
    abc[audit_batch_commitments]
    djl[decision_journal]
    atl2[ai_trade_logs]
    gal[governor_audit_log]
  end

  subgraph debate["Debate"]
    ds[debate_sessions]
    dm[debate_memory]
    drs[debate_rubric_scores]
  end

  ingest[ingestion / scrapers] --> raw
  ingest --> fred
  playbook_svc[playbook service] --> pb
  brain[brain / agents] --> th
  brain --> djl
  ems[ems] --> th
  ems --> br
  harvesters --> psl
  harvesters --> ksl
  pb --> brain
```

## Table catalog by domain

<!-- @generated:start db-table-catalog -->
| Domain | Tables | Primary writers (evidence) |
|--------|--------|----------------------------|
| **Market** | `raw_market_ticks`, `fx_ticks`, `vol_surface_log` | `ingestion/*`, Polygon/Alpaca feeds |
| **Playbook** | `playbook_logs`, `sector_rotation_log` | `trading_playbook/playbook_logger.py` |
| **Execution** | `trade_history`, `broker_rejection_log`, `crypto_perp_trades` | `ems/`, adapters |
| **Kalshi paper** | `kalshi_paper_trades`, `kalshi_shadow_log` | Kalshi engine, shadow logger |
| **Polymarket** | `polymarket_shadow_log`, `pm_bootstrap_results` | `services/*`, PM scripts |
| **Stat arb** | `kl_bootstrap_results` | `scripts/pm_kl_*` |
| **Intel bus** | `intel_stream_log`, `intel_dead_letters` | Publishers via `core/intel_bus` |
| **Memory / vectors** | `intel_embeddings`, `situation_snapshots` | `intelligence/` |
| **Agent weights** | `ensemble_weights_log`, `agent_weight_log`, `regime_adjusted_weight_log`, `agent_trust_log` | Brain / ensemble services |
| **RL** | `rl_decisions`, `rl_episodes`, `rl_training_runs` | `rl_training/` |
| **Audit** | `audit_intent_log`, `audit_hash_chain`, `audit_batch_commitments`, `decision_journal`, `ai_trade_logs` | Brain, archives pipeline |
| **Governor / PnL** | `governor_audit_log`, `pnl_attribution`, `portfolio_summary`, `sleeve_pnl_log` | `risk_governor`, attribution jobs |
| **Debate** | `debate_sessions`, `debate_memory`, `debate_rubric_scores` | `debate_protocol/`, `services/debate_memory` |
| **Macro** | `fred_observations`, `macro_logs`, `geopolitical_logs`, `sentiment_logs`, `earnings_calendar` | Scrapers / harvesters |
| **EDGAR** | `edgar_alerts`, `edgar_filings_log`, `edgar_fundamentals`, `edgar_narrative_extracts` | `edgar_pipeline` |
| **Weather** | `weather_ensemble_forecasts`, `weather_threshold_probabilities` | NWP / EMOS stack |
| **Research** | `research_wiki_pages`, `walk_forward_results`, `discovery_audit_log` | Research / discovery |
| **Misc** | `discord_alert_log`, `discovery_audit_log`, `schema_migrations` | Ops / dbmate |
<!-- @generated:end db-table-catalog -->

## Core row shapes (high-signal)

| Table | Key columns |
|-------|-------------|
| `playbook_logs` | `timestamp`, `regime`, `payload` JSONB, `reasoning_trace` JSONB |
| `trade_history` | `timestamp`, `symbol`, `action`, `price`, `strategy`, `quarantined` |
| `raw_market_ticks` | OHLCV ticks (Timescale parent; chunks in `_timescaledb_internal`) |
| `audit_intent_log` | PM/Kalshi intent audit chain (pairs with `archives/audit/intents/`) |

## TimescaleDB notes

- Hypertable **chunks** excluded from `db/schema.sql` dumps (`scripts/dump_schema.sh`).
- Materialized hypertable refs may appear as views (e.g. `_materialized_hypertable_*`).

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - db.md — migrations & credentials
- @projects/cemini-financial-suite/Architecture/Architecture - data plane.md
- @projects/cemini-financial-suite/Architecture/Architecture - trading_playbook.md — `playbook_logs`

## @user notes
