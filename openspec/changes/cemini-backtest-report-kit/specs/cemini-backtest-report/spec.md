# cemini-backtest-report

## Purpose

Venue-agnostic HTML backtest report generator matching the HL funding sniper layout (Plotly self-contained file).

## Requirements

### Requirement: Generate self-contained HTML

The system SHALL write a single `.html` file that loads Plotly from CDN and requires no local server to view.

#### Scenario: Open report in browser

- **WHEN** the user opens the output path in a desktop browser
- **THEN** all sections render without additional assets beyond the CDN script

### Requirement: Summary section

The report SHALL include summary cards for best Sharpe configuration, best total PnL configuration, sweep combination count, and a data-window summary string supplied by the caller.

#### Scenario: Empty sweep

- **WHEN** the sweep DataFrame has zero rows
- **THEN** the summary states that no results are available without raising an exception

### Requirement: Heatmaps

The report SHALL render at least one 2D heatmap per configured pair, where each cell is the maximum of the chosen metric across all other parameter values for that (x, y) pair.

### Requirement: Top configurations table

The report SHALL include a sortable HTML table of the top N configurations by `sharpe_annual` (default N=20) showing parameter columns and standard metrics.

### Requirement: Sensitivity charts

For each parameter column in the sweep, the report SHALL chart average trade count and average Sharpe by parameter value.

### Requirement: Best-config detail

The report SHALL include equity curve, trade PnL histogram, exit-reason bar chart, and per-segment breakdown for the best-Sharpe configuration.

### Requirement: Configurable labels

The caller SHALL supply `title`, `param_cols`, and a `format_config` callable so venue-specific parameter names appear in summary cards.
