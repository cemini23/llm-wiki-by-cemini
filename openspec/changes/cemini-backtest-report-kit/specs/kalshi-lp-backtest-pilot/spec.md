# kalshi-lp-backtest-pilot

## Purpose

Phase 1: Kalshi LP spread sweep using public `trade-api/v2` candlesticks (trade-derived hourly fallback), same HTML report kit as PM.

## Requirements

### Requirement: Public Kalshi data

The pilot SHALL use `GET /markets` (open, mve excluded) and `GET /series/{series}/markets/{ticker}/candlesticks` without authentication. When candlesticks are sparse, it MAY aggregate `GET /markets/trades`.

### Requirement: Shared report

Output SHALL use `cemini-backtest-report` and land under `.local/reports/kalshi-lp-backtest-YYYY-MM-DD.html`.

### Requirement: CLI

`bash scripts/run_kalshi_lp_backtest.sh` SHALL run the sweep and emit HTML + CSV.
