---
title: Architecture — match_shock_v1 (in-play shock recovery)
type: architecture-module
date: 2026-06-02
updated: 2026-06-02
scanned-commit: scaffold
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
- @projects/world-cup-bot/Architecture/Architecture - match_shock_pmxt_backtest.md — pmxt bucket backtest pipeline
- @concepts/polymarket-football-shock-recovery-trading.md — RoH framework synthesis
- @sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md — advance LP stays `hard_halt`; this module is isolated v2

## For future Claude

Module **8** — `wc_match_shock_v1`. Repo scaffold @ `world-cup-bot` (`match_shock.py`, `config/shock_match.yaml`). **Never** import from `quoter.py`. Pattern B logic version (inline `MATCH_SHOCK_SPEC`), same as cross-venue paper/exec.

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
| Markets | `advance to knockout` | Match win / 90-min |
| Time | Pregame; cancel ≥10h | Live after kickoff (≤2h) |
| Mode enum | `TradingMode.LP` | `TradingMode.SHOCK` |
| Policy | DR 09 — no in-play advance quotes | Explicit in-play match only |
| Registry | `strategy_logic_versions.yaml` | Inline `MATCH_SHOCK_SPEC` |
| Wallet | Operator LP wallet | Same wallet OK if modes never overlap per slug |

Roan's strategy explains **why** advance LP must cancel before kickoff: live shocks reprice related markets and pick off stale resting quotes.

## Component map

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ Trade/OB ingest │────▶│ Shock detector   │────▶│ 5D classifier   │
│ (WS / JSONL)    │     │ 2m window        │     │ bucket_key      │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                          │
┌─────────────────┐     ┌──────────────────┐              ▼
│ Paper / live    │◀────│ Ladder planner   │◀──── Distribution lookup
│ execution       │     │ P50–P95 weights  │      (pmxt backtest JSON)
└─────────────────┘     └──────────────────┘
```

### Shipped scaffold (2026-06-02)

| Piece | Path |
|-------|------|
| Config | `config/shock_match.yaml` |
| Core logic | `world_cup_bot/match_shock.py` |
| Mode handoff | `world_cup_bot/trading_mode.py` |
| Loader | `world_cup_bot/match_shock_config.py` |
| Backtest CLI | `scripts/shock_backtest/run_bucket_backtest.py` |
| pmxt ETL | `scripts/shock_backtest/export_pmxt_shock_tapes.py` |
| pmxt parquet → JSONL | `scripts/shock_backtest/pmxt_parquet_to_jsonl.py` |
| Librarian sync | `scripts/shock_backtest/sync_pmxt_football_to_librarian.sh` |
| Tests | `tests/test_match_shock.py` |
| Operator doc | `docs/MATCH_SHOCK_V1.md` |

### Not yet built

- CLOB WS live scanner + order POST layer
- CLI subcommands (`match-shock-scan`, `match-shock-plan`)
- systemd timer (monitor profile)
- Gemini DR prompt `12-match-shock-recovery-spec.md`

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

Backtest filter default: **`moderate_fav`** buckets only (RoH tuning claim — verify on pmxt data).

## Ledger events

| `event` | When |
|---------|------|
| `match_shock_detected` | Shock fires + bucket classified |
| `match_shock_ladder_planned` | Ladder prices computed |
| `match_shock_paper_fill` | Paper touch fill + recovery PnL |

All rows: `logic_version=wc_match_shock_v1`, `strategy_key=pm_wc_match_shock`.

## Promotion gates

1. pmxt (or Dome) bucket backtest → win rate ≥ 55% on filtered buckets
2. 3+ days paper ledger soak (`WC_MATCH_SHOCK_LIVE` unset)
3. Operator sign-off — separate from SHADOW Phase 4 advance LP
4. Non-US egress if live POST (same as Module 3)

## Env flags (planned)

| Flag | Meaning |
|------|---------|
| `WC_MATCH_SHOCK_LIVE=1` | Allow live limit POST (default off) |
| `WC_MATCH_SHOCK_LEDGER_PATH` | JSONL path |

Master YAML switch: `config/shock_match.yaml` → `enabled: false`.

## Out of scope (this module)

- Tournament winner futures
- Advance-to-knockout markets
- Kalshi leg (PM-only v1)
- Sub-10ms courtsiding infra
