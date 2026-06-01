---
title: Architecture — world_cup_bot package
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
module: world_cup_bot
scanned-commit: 17a6647
tags: [architecture, world-cup-bot, python]
ai-first: true
related:
  - projects/world-cup-bot/Architecture/Architecture - Overview.md
  - projects/world-cup-bot/World Cup Bot.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/polymarket-clob-api.md
maturity: validated
---

## Relations

- @projects/world-cup-bot/Architecture/Architecture - Overview.md — system diagram
- @entities/tools/polymarket-gamma-api.md — Gamma discovery
- @entities/tools/polymarket-clob-api.md — quotes, fills, rewards

## For future Claude

The **`world_cup_bot`** Python package (52 source files @ `17a6647`) implements all CLI subcommands registered in `__main__.py`. Grouped below by README “Module” numbers where they exist; cross-venue and phase-router are parallel tracks.

<!-- @generated:start -->

## Responsibilities (from code layout)

| Area | Key files | CLI / behavior |
| --- | --- | --- |
| **Scanner (1)** | `scanner.py`, `pm_discovery.py` | `scan` — Gamma advance markets, live mids |
| **Conviction (2)** | `conviction.py`, `conviction_staleness.py`, `conviction_patch.py` | YAML filter; `conviction-staleness`, `conviction-patch` |
| **Quoter (3)** | `quoter.py`, `order_manager.py`, `clob_live.py`, `clob_auth.py` | `plan` — post-only GTC; cancel-replace; `MissingClobAuthError` if no L2 |
| **Fill handler (4)** | `fill_handler.py`, `ws_user.py`, `reconcile.py` | `watch`, `fill` — kill-switch, queue depletion |
| **Calendar (5)** | `calendar_guard.py`, `fixture_watch.py` | `calendar`, `fixture-check` — CC0 `data/worldcup2026-fixtures.json` |
| **Cross-venue (6)** | `cross_venue_scanner.py`, `cross_venue_paper.py`, `cross_venue_exec.py`, `cross_venue_fills.py`, `kalshi_*` | `cross-venue-scan`, `cross-venue-pnl`, `cross-venue-exec`, `cross-venue-fill` |
| **Ledger (7)** | `ledger.py`, `event_log.py`, `logic_version.py`, `rewards_sync.py` | JSONL audit; `pnl`, `rewards sync` |
| **Liquidity gate** | `liquidity_scanner.py` | `liquidity-scan`; `plan --liquidity-gate` |
| **Phase router (1b)** | `phase_router.py`, `market_phases.py`, `settlement_gate.py`, `fifa_match_gate.py`, `phase_replay.py` | `phase status|set|purge`; env-gated |
| **Risk / ops** | `risk.py`, `preflight.py`, `shadow_checklist.py`, `alerts.py`, `venue_reconcile.py` | `preflight`, `shadow-status`, `venue-reconcile compare` |
| **UI / research** | `ui_server.py`, `ui_data.py`, `research.py`, `advisor.py` | `ui` (localhost:8765); `research` subcommands |

## External dependencies (runtime)

- **Polymarket** — Gamma HTTP + CLOB REST/WS (`http_client.py`, `clob_rest.py`, `clob_signing.py`)
- **Kalshi** — optional REST for cross-venue (`kalshi_rest.py`, `kalshi_orders.py`)
- **Fixtures** — vendored openfootball JSON (not live prices)

## Invariants (enforced in code + CI)

- Price/mid thresholds in `scanner.py`, `quoter.py`, `fill_handler.py` must come from YAML (`scripts/check_hardcoded_thresholds.py`)
- Settlement gate fails closed on Gamma errors (`settlement_gate.py`)
- Cross-venue exec does not book manual fill / realized PnL on dry-run submit (see tests `test_cross_venue_exec.py`)

<!-- @generated:end -->
