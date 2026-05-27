## Context

HL funding backtest lives in `.local/tools/hl-funding-sniper-reference/backtest/report.py` (upstream MIT). The layout is the product: summary cards, 2D heatmaps (best metric per param pair), top-20 table, per-parameter sensitivity, equity + trade distribution + segment bars.

Cemini wiki already defines PM LP Phase-0 (`@concepts/polymarket-lp-bot-phase0-spec.md`) and historical-data plumbing (`@concepts/prediction-market-historical-analysis.md`) but no unified sweep UI.

**Boundary**: laptop research only. No `main.py` on prod/egress. Reports inform briefs; they do not auto-promote parameters.

## Goals / Non-Goals

**Goals:**

- One `generate_report()` API usable by any venue simulator that outputs a standard sweep DataFrame + best-config trade/equity/segment frames.
- PM pilot v1: LP spread sweep on hourly CLOB mids for top-volume active markets.
- Same HTML skin as HL report (Plotly CDN, card grid, section numbering).

**Non-Goals (v1):**

- Fill-realistic L2 replay (`hftbacktest`) or cross-venue PM↔Kalshi latency.
- Kalshi / equities simulators (Phase 1+ briefs).
- Committing `.local/reports/` or Dune SQL for PM.

## Decisions

### 1. Package split

| Package | Role |
|---------|------|
| `scripts/cemini_backtest_report/` | `ReportConfig` + `generate_report()` |
| `scripts/pm_lp_backtest/` | Data fetch, LP engine, sweep, CLI |

Import path: `from cemini_backtest_report import ReportConfig, generate_report` with `PYTHONPATH=scripts` or relative sys.path in CLI.

### 2. ReportConfig contract

- `title`, `subtitle`, `param_cols`, `metric_cols`, `heatmap_pairs` (list of `(x, y, metric, suffix?, colorscale?)`)
- `format_config(row) -> str` for summary cards
- `segment_col` default `"segment"` for per-market/coin bar chart
- `trade_pnl_col` default `"net_pnl_pct"`

### 3. PM LP simulation (toy but honest)

Hourly bars from `GET /prices-history?market={token_id}&interval=max&fidelity=60`.

Per bar:

- Quote bid/ask at `mid ± spread_cents/200` (cents → probability units).
- **Adverse fill**: if next mid crosses our quote, realize mark-to-market PnL on unit notional.
- **Reward proxy**: `reward_rate / spread_cents` per bar when quoted (inverse-spread incentive; not on-chain truth — labeled in report).
- Aggregate metrics per config across N markets via `scripts/pm_lp_backtest/metrics.py` (same column names as HL sweep for report compatibility).

### 4. Output layout

```
.local/reports/pm-lp-backtest-YYYY-MM-DD.html
.local/reports/pm-lp-backtest/cache/   # parquet/csv optional
```

### 5. Cadence

Mirror HL: `wiki/meta/pm-lp-backtest-cadence.md` — quarterly user-gated prompt, not auto-run.

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| Reward proxy ≠ real LP scoring | Report banner + wiki `[TENTATIVE]`; compare shadow PnL vs reward proxy |
| Hourly bars miss sub-hour adverse selection | Phase 2: `fidelity=1` or recorded L2 |
| API rate limits | Cap markets (default 12), cache price series to `.local/` |
| Sharpe looks good, PnL negative | Summary shows **best PnL** and count of positive-PnL configs (HL lesson) |

## Migration Plan

1. Ship Phase 0 + PM pilot (this change).
2. Optional: refactor HL reference clone to import `cemini_backtest_report` instead of vendored `report.py`.
3. Phase 1 brief: Kalshi harvest + same report kit.
4. Phase 2: ArcticDB equity signal sweep on librarian export.

Rollback: delete `scripts/cemini_backtest_report` and `scripts/pm_lp_backtest`; wiki page remains as design record.

## Open Questions

- Wire MCPT gate (`@concepts/monte-carlo-permutation-test-mcpt.md`) as post-sweep script? → defer to Phase 1.
- Publish static report under `ui/`? → laptop-only until user asks.
