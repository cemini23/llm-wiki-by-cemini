---
title: Cemini backtest report kit — venue-agnostic sweep HTML
type: concept
tags: [concept, backtest, polymarket, reporting, plotly, laptop-research, cemini]
keywords: [backtest-report, parameter-sweep, plotly-html, pm-lp, hl-funding, kalshi, equities]
related:
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/prediction-market-historical-analysis.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/hftbacktest.md
  - meta/hl-funding-backtest-cadence.md
  - meta/pm-lp-backtest-cadence.md
maturity: validated
created: 2026-05-27
updated: 2026-05-27
---

## Relations

- @concepts/polymarket-lp-bot-phase0-spec.md — PM pilot simulates spread/sizing knobs from Phase-0 LP design
- @concepts/polymarket-lp-rewards-farming.md — strategy context for PM sweep
- @concepts/prediction-market-historical-analysis.md — future Layer 5 replay; v1 uses live CLOB history API
- @entities/tools/polymarket-clob-api.md — `prices-history` data source
- @entities/tools/polymarket-gamma-api.md — market discovery + volume filter
- @entities/tools/hftbacktest.md — Phase 2 fill-realistic path for cross-venue / L2
- @meta/hl-funding-backtest-cadence.md — sibling cadence for HL funding (Dune)
- @meta/pm-lp-backtest-cadence.md — quarterly PM LP sweep ritual

## Raw Concept

Prompted by the HL funding sniper HTML backtest report (2026-05-27): user asked for the same layout across Polymarket, Kalshi, equities, and crypto. OpenSpec change `cemini-backtest-report-kit` ships Phase 0 (shared report module) + PM LP pilot.

## Narrative

### Layout contract (all venues)

Self-contained Plotly HTML:

1. Summary cards (best Sharpe, best PnL, sweep count, data window)
2. 2D heatmaps (best metric per param pair)
3. Top-N configuration table
4. Per-parameter sensitivity (avg trades + Sharpe)
5. Best-config equity curve, PnL histogram, exit reasons, per-segment bars

Implementation: `scripts/cemini_backtest_report/` (`ReportConfig`, `generate_report()`). Pattern extracted from MIT `hl-funding-sniper` `backtest/report.py` (laptop reference clone).

### PM LP pilot (v1)

| Piece | Path |
|-------|------|
| Fetch | Gamma top markets + CLOB `prices-history` (hourly) |
| Sim | Two-sided quote at `mid ± spread_cents/2`; adverse fill on hourly cross; reward **proxy** `∝ 1/spread` |
| Sweep | `spread_cents`, `reward_scale`, `adverse_multiplier` |
| Run | `bash scripts/run_pm_lp_backtest.sh` or `python3 scripts/pm_lp_backtest/run.py` |
| Output | `.local/reports/pm-lp-backtest-YYYY-MM-DD.html` (+ `.sweep.csv`) |

**Not on-chain LP scoring** — proxy labeled in report disclaimer. Shadow-live on prod remains the gate per @concepts/polymarket-lp-bot-phase0-spec.md.

### Roadmap lanes

| Lane | Data | Status |
|------|------|--------|
| HL funding | Dune `hyperliquid.market_data` | Shipped (reference clone) |
| PM LP | Gamma + CLOB | **Pilot shipped** |
| Kalshi | Historical harvest | OpenSpec / brief |
| Equities | ArcticDB `equity_bars` on librarian | OpenSpec / brief |
| PM↔Kalshi arb | L2 + latency | `hftbacktest` Phase 1+ |

### OpenSpec

Change directory: `openspec/changes/cemini-backtest-report-kit/` (proposal, design, specs, tasks). Apply with `/opsx:apply` when extending to Kalshi/equities.

## Snippets

```bash
# PM LP report (laptop)
bash scripts/run_pm_lp_backtest.sh --quick
open ".local/reports/pm-lp-backtest-$(date +%Y-%m-%d).html"
```
