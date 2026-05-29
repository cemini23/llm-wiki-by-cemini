---
title: Cemini backtest report kit — venue-agnostic sweep HTML
type: concept
tags: [concept, backtest, polymarket, reporting, plotly, laptop-research, cemini]
keywords: [backtest-report, parameter-sweep, plotly-html, pm-lp, hl-funding, kalshi, equities]
related:
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/prediction-market-historical-analysis.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/lo-mackinlay-variance-ratio-test.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/arcticdb.md
  - entities/tools/hftbacktest.md
  - meta/hl-funding-backtest-cadence.md
  - meta/pm-lp-backtest-cadence.md
  - meta/kalshi-lp-backtest-cadence.md
  - meta/equity-signal-backtest-cadence.md
  - meta/cross-venue-backtest-cadence.md
  - concepts/kalshi-api-reference.md
  - entities/platforms/kalshi.md
  - sources/trading-posts-compilation-38-2026-05-28.md
maturity: core
created: 2026-05-27
updated: 2026-05-29
---

## Relations

- @concepts/polymarket-lp-bot-phase0-spec.md — PM pilot
- @concepts/cross-venue-arbitrage-pattern.md — Phase 3 divergence lab (not atomic arb)
- @concepts/monte-carlo-permutation-test-mcpt.md — `scripts/backtest_common/mcpt_gate.py`
- @entities/tools/arcticdb.md — Phase 2 data on librarian
- @meta/hl-funding-backtest-cadence.md — HL Dune quarterly
- @meta/pm-lp-backtest-cadence.md — PM LP quarterly
- @meta/kalshi-lp-backtest-cadence.md — Kalshi LP quarterly
- @meta/equity-signal-backtest-cadence.md — equity momentum quarterly
- @meta/cross-venue-backtest-cadence.md — PM×Kalshi quarterly

## Raw Concept

Unified Plotly HTML sweep reports for Cemini lanes: HL funding, PM LP, Kalshi LP, equity momentum (ArcticDB), PM×Kalshi divergence. OpenSpec: `cemini-backtest-report-kit`.

## Narrative

### Shared kit

`scripts/cemini_backtest_report/` — `ReportConfig`, `generate_report()`.

`scripts/backtest_common/` — metrics + `mcpt_gate.py`.

### Lanes (all shipped 2026-05-27)

| Phase | Lane | Runner | Report |
|-------|------|--------|--------|
| 0 | PM LP | `run_pm_lp_backtest.sh` | `pm-lp-backtest-*.html` |
| 0b | HL funding | `run_hl_funding_report.sh` | `hl-funding-backtest-*.html` (from reference sweep parquet) |
| 1 | Kalshi LP | `run_kalshi_lp_backtest.sh` | `kalshi-lp-backtest-*.html` |
| 2 | Equities | `run_equity_signal_backtest.sh` | `equity-signal-backtest-*.html` |
| 3 | PM×Kalshi | `run_cross_venue_backtest.sh` | `cross-venue-backtest-*.html` |

### Future

- Fill-realistic PM↔Kalshi: @entities/tools/hftbacktest.md
- Matched-event pairing for cross-venue (not BTC-proxy)

## Snippets

```bash
bash scripts/run_pm_lp_backtest.sh --quick
bash scripts/run_kalshi_lp_backtest.sh --quick
bash scripts/run_equity_signal_backtest.sh --quick
bash scripts/run_cross_venue_backtest.sh --quick
bash scripts/run_hl_funding_report.sh
python3 scripts/backtest_common/mcpt_gate.py .local/reports/equity-signal-backtest-2026-05-27.trades.csv
```
