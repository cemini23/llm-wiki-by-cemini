# pm-lp-backtest-pilot

## Purpose

Laptop-only Polymarket LP spread parameter sweep using public Gamma + CLOB price history, producing sweep results and an HTML report via `cemini-backtest-report`.

## Requirements

### Requirement: Public data only

The pilot SHALL fetch market metadata from Gamma and hourly mids from CLOB `prices-history` without wallet authentication.

#### Scenario: Offline cache hit

- **WHEN** cached price series exist for a token and `--refresh` is not set
- **THEN** the pilot SHALL skip refetching that series

### Requirement: Market selection

The pilot SHALL default to active, non-closed markets ordered by `volume24hr` with a configurable cap (default 12).

### Requirement: Parameter sweep

The pilot SHALL grid-search at minimum: `spread_cents`, `min_volume24hr`, and `reward_scale` (reward proxy multiplier).

#### Scenario: Sweep completion

- **WHEN** all combinations finish
- **THEN** the pilot SHALL write a sweep DataFrame with columns compatible with `cemini-backtest-report` metrics (`n_trades`, `hit_rate`, `total_pnl_usd`, `sharpe_annual`, `max_drawdown_pct`, `profit_factor`, `avg_pnl_pct`, `exit_reason` on trades)

### Requirement: Simulation disclaimer

The HTML report SHALL state that LP reward accrual is a **proxy model**, not Polymarket’s on-chain scoring formula.

### Requirement: Output location

The pilot SHALL write the HTML report under `.local/reports/` with a date-stamped filename.

### Requirement: CLI entrypoint

The pilot SHALL provide `python3 scripts/pm_lp_backtest/run.py` (or equivalent) accepting `--markets`, `--quick`, and `--output` flags.
