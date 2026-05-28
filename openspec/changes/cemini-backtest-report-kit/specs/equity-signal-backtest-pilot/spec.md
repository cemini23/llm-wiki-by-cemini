# equity-signal-backtest-pilot

## Purpose

Phase 2: daily momentum z-score sweep on librarian ArcticDB `equity_bars`, HTML via shared kit.

## Requirements

- SSH export from `cemini-librarian` (CSV; no pyarrow on librarian venv).
- Sweep `lookback`, `entry_z`, `stop_loss_pct`.
- MCPT on best-config trades optional in CLI output.
- Output `.local/reports/equity-signal-backtest-YYYY-MM-DD.html`.
