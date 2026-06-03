---
title: Architecture — match_shock_v1 (in-play shock recovery)
type: architecture-module
date: 2026-06-02
updated: 2026-06-03
scanned-commit: dual-path-cli
ai-first: true
related:
  - projects/world-cup-bot/Architecture/Architecture - Overview.md
  - projects/world-cup-bot/Architecture/Architecture - match_shock_pmxt_backtest.md
  - projects/world-cup-bot/Architecture/OPEN-GAPS.md
  - entities/tools/world-cup-bot.md
  - concepts/polymarket-football-shock-recovery-trading.md
  - sources/rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
maturity: draft
---

## Relations

- @projects/world-cup-bot/Architecture/Architecture - Overview.md
- @projects/world-cup-bot/Architecture/Architecture - match_shock_pmxt_backtest.md — data paths (Data API, live WS, pmxt)
- @concepts/polymarket-football-shock-recovery-trading.md — RoH framework synthesis
- @sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md — advance LP stays `hard_halt`; this module is isolated v2

## For future Claude

Module **8** — `wc_match_shock_v1`. Repo: `world-cup-bot` (`match_shock.py`, `config/shock_match.yaml`). **Never** import from `quoter.py`. Pattern B logic version (inline `MATCH_SHOCK_SPEC`), same as cross-venue paper/exec.

## Purpose

Capture **statistical recovery** after in-play football price shocks on Polymarket **match markets** (not advance-to-knockout). Detect panic drops → classify context → place percentile ladder limits → exit on fixed recovery target.

## Unified mode handoff (same bot)

**One process, two modes** — `world_cup_bot/trading_mode.py`:

| Clock | Advance markets | Match markets |
|-------|-----------------|---------------|
| `hours_to_kickoff ≥ 10h` | **LP** | OFF |
| `0 < hours < 10h` | **OFF** (cancel window) | OFF |
| Live (`hours < 0`, ≤2h elapsed) | OFF | **SHOCK** (when enabled) |
| Post-match | OFF | OFF |

LP ends at the **same** `MIN_HOURS_BEFORE_KICKOFF` the calendar guard already enforces. Shock starts at kickoff on match slugs only — not a second bot.

## Isolation from v1 advance LP

| Concern | Advance LP (Module 3) | Match shock (Module 8) |
|---------|----------------------|-------------------------|
| Markets | `advance to knockout` | Match win / 90-min / beat |
| Time | Pregame; cancel ≥10h | Live after kickoff (≤2h) |
| Mode enum | `TradingMode.LP` | `TradingMode.SHOCK` |
| Policy | DR 09 — no in-play advance quotes | Explicit in-play match only |
| Registry | `strategy_logic_versions.yaml` | Inline `MATCH_SHOCK_SPEC` |
| Wallet | Operator LP wallet | Same wallet OK if modes never overlap per slug |

## Component map

```
┌─────────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ Tape ingest         │────▶│ Shock detector   │────▶│ 5D classifier   │
│ Data API / WS / pmxt│     │ 2m window        │     │ bucket_key      │
└─────────────────────┘     └──────────────────┘     └────────┬────────┘
                                                              │
┌─────────────────┐     ┌──────────────────┐                  ▼
│ Paper / live    │◀────│ Ladder planner   │◀──── Distribution lookup
│ execution       │     │ P50–P95 weights  │      (backtest JSON)
└─────────────────┘     └──────────────────┘
```

## Shipped (2026-06-03)

| Piece | Path |
|-------|------|
| Config | `config/shock_match.yaml` |
| Core logic | `world_cup_bot/match_shock.py` |
| Mode handoff | `world_cup_bot/trading_mode.py` |
| Gamma discovery | `world_cup_bot/match_market_discovery.py` |
| Data API client | `world_cup_bot/data_api_client.py` |
| Tape export | `world_cup_bot/shock_tape_export.py` |
| Live WS | `world_cup_bot/ws_market.py`, `match_shock_record.py` |
| Backtest CLI | `scripts/shock_backtest/run_bucket_backtest.py` |
| pmxt ETL (optional) | `scripts/shock_backtest/pmxt_parquet_to_jsonl.py`, sync scripts |
| CLI | `match-shock-discover`, `match-shock-export`, `match-shock-record` |
| Operator doc | `docs/MATCH_SHOCK_V1.md` |
| Tests | `tests/test_match_shock.py`, `test_match_market_discovery.py`, `test_ws_market.py`, … |

## CLI (operator)

```bash
world-cup-bot match-shock-discover --out data/local/match_markets.json
world-cup-bot match-shock-export --discovery data/local/match_markets.json
WC_SHOCK_ENABLED=1 world-cup-bot match-shock-record --discovery data/local/match_markets.json
```

**Dome API EOL 2026-04-28** — historical trades via Polymarket Data API (`data-api.polymarket.com`), not Dome.

## Shipped (repo @ 2026-06-03)

- Live limit POST — `match_shock_post.py` + `match-shock-post` CLI (gated: `WC_MATCH_SHOCK_LIVE` + `WC_MATCH_SHOCK_LIVE_ACK`)
- `match-shock-plan` paper/live loop — `match_shock_plan.py`
- systemd — discover/plan timers (monitor); record + live-plan (trading, manual)
- `tournament-ops check` — `_check_match_shock_readiness` (discovery + tapes + env gates)

## Deferred (v1.1)

- Match clock + score feed join for `elapsed_ms` / `goal_diff` precision beyond tape defaults
- Operator sets `operator.wc_volume_hypothesis` in `shock_match.yaml` after K97 sizing debate (larger overreactions vs deeper liquidity)

## Detection parameters (YAML)

| Param | Default | Source |
|-------|---------|--------|
| Window | 120s | RoH post |
| Min drop % | 15% | RoH post |
| Min drop abs | 8¢ | RoH post |
| Cooldown | 180s | RoH post |

## Five-dimension buckets

Key format: `{league}|{favoritism}|{book_depth}|{time}|{goal_state}`

Example: `deep|underdog|balanced|mid|level`

Min **5** samples per bucket before trusting distribution; else conservative defaults (6/9/13/18¢).

## Ladder + exit

| Percentile | Weight | Limit |
|------------|--------|-------|
| P50 | 10% | pre − P50 depth |
| P75 | 20% | pre − P75 depth |
| P90 | 30% | pre − P90 depth |
| P95 | 40% | pre − P95 depth |

Order TTL: 60s. Exit: **+4¢** recovery from fill (configurable).

Backtest filter default: **`moderate_fav`** buckets only (RoH tuning claim — verify on exported tapes).

## Ledger events

| `event` | When |
|---------|------|
| `match_shock_detected` | Shock fires + bucket classified |
| `match_shock_ladder_planned` | Ladder prices computed |
| `match_shock_paper_fill` | Paper touch fill + recovery PnL |

All rows: `logic_version=wc_match_shock_v1`, `strategy_key=pm_wc_match_shock`.

## Promotion gates

1. Data API + live WS bucket backtest → win rate ≥ 55% on filtered buckets
2. 3+ days paper ledger soak (`WC_MATCH_SHOCK_LIVE` unset)
3. Operator sign-off — separate from SHADOW Phase 4 advance LP
4. Non-US egress if live POST (same as Module 3)

## Env flags

| Flag | Meaning |
|------|---------|
| `WC_SHOCK_ENABLED=1` | Enable match-shock record path |
| `WC_MATCH_SHOCK_LIVE=1` | Allow live limit POST (default off; requires ACK + preflight) |
| `WC_MATCH_SHOCK_TAPE_DIR` | Export / live tape directory |
| `WC_MATCH_SHOCK_LEDGER_PATH` | JSONL path |

Master YAML switch: `config/shock_match.yaml` → `enabled: false`.

## Out of scope (this module)

- Tournament winner futures
- Advance-to-knockout markets
- Kalshi leg (PM-only v1)
- Sub-10ms courtsiding infra
