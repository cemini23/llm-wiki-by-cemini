---
title: PnL attribution logic versioning
type: concept
tags: [concept, pnl, attribution, versioning, cemini-prod, operations, k75]
keywords: [logic_version, strategy_logic_versions, pnl_attribution, pnl_scope, legacy_unversioned, brain_equity, kalshi_weather, pm_lp_rewards, fifo, reconciliation]
related:
  - concepts/production-trading-blind-spots.md
  - concepts/trading-bot-logging-discipline.md
  - concepts/equity-fair-value-evaluation.md
  - concepts/polymarket-bot-architecture.md
  - concepts/perps-dex-funding-carry-strategy.md
  - entities/infrastructure/cemini-stack.md
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
  - concepts/shadow-to-live-transition-engineering.md
  - concepts/lp-algorithm-live-promotion-gates.md
maturity: validated
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/production-trading-blind-spots.md — catalog of slow-discovery failures; PnL version mixing is the headline case
- @concepts/trading-bot-logging-discipline.md — structured logs must carry `logic_version` on every PnL-relevant event
- @concepts/equity-fair-value-evaluation.md — `brain_equity` version bump tied to fair-value sleeve rules (2026-05-28)
- @concepts/polymarket-bot-architecture.md — phantom-WIN / internal-counter lessons are the same failure family
- @concepts/perps-dex-funding-carry-strategy.md — reconciliation-first posture generalizes here
- @entities/infrastructure/cemini-stack.md — `pnl_attribution` container + Postgres hypertables
- @sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md — Polymarket CSV as source-of-truth precedent
- @concepts/shadow-to-live-transition-engineering.md — registry bump at live cutover
- @concepts/lp-algorithm-live-promotion-gates.md — `pm_lp_rewards` promotion requires version bump

## Raw Concept

What prompted this page: operator discovery (2026-05-28) that headline PnL was polluted for months because strategy logic changed without separating historical rows by version. Prod now ships `cemini_contracts/strategy_logic_versions.py`, `core/pnl_logic_version.py`, DB `logic_version` columns, and `--scope current|legacy|all` on report scripts — but the wiki had no concept page documenting the pattern.

## Narrative

### The failure mode

When signal logic, sizing rules, or execution plumbing change, **PnL computed before and after the change is not comparable**. Mixing them produces:

- Inflated or deflated win rates (old bug-fix rows counted against new logic)
- False "strategy regression" after a fix (good new logic looks bad because legacy losses remain in the window)
- Months of debugging the wrong layer (strategy vs attribution vs fill detection)

This is the **equities/Kalshi/PM generalization** of the Polymarket operator lesson: never trust the bot's internal counter when venue truth differs — here the "venue truth" is **which code version produced the row**.

### Prod architecture (cemini-prod, read-only audit 2026-05-28)

**Registry** — `cemini_contracts/strategy_logic_versions.py`:

| `strategy_key` | Current `version_id` | Deployed (UTC) | Notes |
|---|---|---|---|
| `kalshi_weather` | `kalshi_weather_bracket_v1` | 2026-05-27 14:00 | Bracket match before cheap YES |
| `kalshi_autopilot` | `kalshi_autopilot_v1` | 2026-05-27 14:00 | Non-weather modules |
| `brain_equity` | `brain_playbook_v2` | 2026-05-28 12:30 | Equities brain + fair-value sleeves |
| `pm_weather` | `pm_weather_k70_v1` | 2026-05-27 13:00 | K70 adversary skip union |
| `pm_lp_rewards` | `pm_lp_k69_v1` | 2026-05-27 13:00 | K69 capital ledger + pre-resolution exit |
| `pm_btc_updown` | `pm_btc_updown_k67_v1` | 2026-05-28 14:00 | K67 FOK shadow-first exec |

Each spec carries `legacy_version_ids` plus sentinel `legacy_unversioned` for NULL/empty rows.

**Helpers** — `core/pnl_logic_version.py`:

- `filter_rows_by_scope()` — `current` | `legacy` | `all`
- `summarize_pnl_by_version()` — grouped metrics + `legacy_excluded` block for headlines
- `sql_logic_version_filter()` — SQL fragment for reports
- `era_sql_filter()` — fallback time cutoff when column missing on old rows

**Stamping at write time**:

- Kalshi paper trades, `trade_history`, PM weather paper, PM LP sync, PM CLOB writer, paper EMS adapter — all stamp `logic_version` from registry
- Migration `20260528120000_strategy_logic_version_columns.sql` backfills legacy IDs on NULL rows

**Report scripts** (default `scope=current`):

- `scripts/brain_paper_pnl_report.py` — FIFO round-trips on `trade_history`, `--scope`, `by_logic_version` breakdown
- `scripts/kalshi_paper_pnl.py` — module-aware filtering via `filter_kalshi_rows_by_scope()`

**Separate daily attribution engine** — `services/pnl_attribution.py` (Step 60):

- Brinson-Fachler asset-class decomposition + MAPPO agent attribution
- Writes to Timescale hypertable `pnl_attribution` (JSONB payload) — **portfolio-level**, not per-trade `logic_version`
- Do not confuse with per-strategy versioned paper PnL; they answer different questions

**Sleeve log** — `sleeve_pnl_log` hypertable (Step 80): daily per-sleeve realized/unrealized PnL for Darwinian allocator; complements versioned trade rows.

### Operational rules

1. **Bump registry on every material logic change** — new `version_id`, `deployed_at`, move old ID to `legacy_version_ids`, one-line `note`.
2. **Default reports to `scope=current`** — legacy visible via `--scope all` for forensics only.
3. **Headline metrics must print version banner** — `version_banner(spec)` in CLI output.
4. **Replay test** — same fills + same `logic_version` → identical FIFO PnL; if not, attribution bug.
5. **When column missing** — use `era_sql_filter()` on timestamp as secondary guard, not primary.

### Relation to fair-value equities (2026-05-28)

`brain_playbook_v2` explicitly versions the equities-only brain loop where sleeve classification uses `core/equity_valuation.py` signals (`fair_value_usd`, `value_gap_pct`, FMP + LLM candidates). Changing valuation weights or gap thresholds **requires a version bump** — otherwise hold vs tactical sleeve PnL mixes incompatible decision rules.

## Snippets

> "Bump ``version_id`` and ``deployed_at`` when signal, sizing, or execution logic changes. PnL scripts default to *current* version only so legacy rows do not pollute headline metrics." [Source: cemini-prod `cemini_contracts/strategy_logic_versions.py` module docstring, retrieved 2026-05-28]

> "FIFO on scoped logic_version rows; legacy excluded when scope=current." [Source: cemini-prod `scripts/brain_paper_pnl_report.py`, retrieved 2026-05-28]

## Dead Ends

- **Portfolio Brinson-Fachler alone does not solve version mixing** — it decomposes asset-class effects on a day; it does not tag which strategy revision produced each trade.
- **Time-cutoff-only filtering** — fragile when deploy timestamps slip or hotfixes land mid-session; `logic_version` column is authoritative when present.
