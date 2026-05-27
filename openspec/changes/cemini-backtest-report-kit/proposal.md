## Why

The HL funding backtest produced a self-contained Plotly HTML report that made parameter sweeps immediately legible (summary cards, heatmaps, top configs, equity curve). Cemini covers Polymarket, Kalshi, equities, and crypto perps, but only Hyperliquid funding has that reporting loop today. We need a **venue-agnostic report kit** plus a **first Polymarket pilot** so strategy work on PM LP farming can reuse the same visual contract before prod briefs.

## What Changes

- Add `scripts/cemini_backtest_report/` — shared HTML generator (Plotly, HL-layout-compatible) parameterized by venue/strategy metadata.
- Add `scripts/pm_lp_backtest/` — laptop-only PM LP-rewards **shadow simulator** using public Gamma + CLOB `prices-history` (no wallet, no prod writes).
- Add wiki concept `@concepts/cemini-backtest-report-kit.md` and cadence meta `@wiki/meta/pm-lp-backtest-cadence.md`.
- Output reports under `.local/reports/` (gitignored), same open-in-browser workflow as HL funding.
- Document OpenSpec change for future lanes (Kalshi, equities ArcticDB, cross-venue).

## Capabilities

### New Capabilities

- `cemini-backtest-report`: Venue-agnostic sweep → HTML report (summary, heatmaps, top-N table, sensitivity charts, equity curve, trade histogram, exit reasons, per-segment breakdown).
- `pm-lp-backtest-pilot`: Fetch PM markets + hourly mids; simulate two-sided LP spread sweep; emit sweep CSV + HTML via the shared report module.

### Modified Capabilities

<!-- None — greenfield laptop tooling -->

## Impact

- **OSINT workspace**: new `scripts/` packages; optional `pandas`/`plotly`/`requests` for PM pilot (same stack as HL reference clone).
- **Prod / librarian**: no deploy; briefs may reference report paths after human review.
- **Wiki**: one concept page, index row, log entry, related backlinks on PM LP + historical-analysis pages.
- **Dependencies**: public Polymarket Gamma + CLOB APIs only for pilot; no Dune credits required for PM v1.
