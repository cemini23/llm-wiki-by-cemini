---
title: hftbacktest — High-Frequency Backtesting Framework
type: entity
tags: [tool, backtesting, hft, market-making, microsecond-tick-data, adopt-tier, cemini-production-stack]
keywords: [hftbacktest, level-2-orderbook, level-3-market-by-order, latency-adjusted-backtest, event-order-correction, microsecond-tick, nkaz001]
related:
  - sources/5-5-moarrr-tool-eval.md
  - concepts/prediction-market-historical-analysis.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/polymarket-market-making-architectures.md
  - entities/tools/financetoolkit.md
  - entities/tools/riskfolio-lib.md
  - entities/tools/pybroker.md
  - sources/sabr-geometry-aware-correction-2605.06604.md
  - concepts/cemini-backtest-report-kit.md
maturity: validated
created: 2026-05-05
updated: 2026-05-29
---

## Relations

- @sources/5-5-moarrr-tool-eval.md — origin source: K31 Gemini DR eval URL 15, **Adopt** tier
- @concepts/prediction-market-historical-analysis.md — load-bearing addition to the backtest-pipeline plumbing concept; hftbacktest fills the microsecond-tick gap that daily-bar tools (yfinance EOD, FinanceToolkit GARCH on daily series) don't cover
- @concepts/cross-venue-arbitrage-pattern.md — direct downstream consumer; cross-venue arb threshold-tuning needs latency-adjusted backtests of the Polymarket-CLOB ↔ Kalshi-orderbook timing window
- @concepts/polymarket-market-making-architectures.md — direct downstream consumer; MM strategy parameter-tuning (spread sizing, inventory limits, cadence) requires microstructure-level backtest data
- @entities/tools/financetoolkit.md — companion library; FinanceToolkit covers daily-bar fundamentals, hftbacktest covers microsecond execution simulation. Different time-resolution layers of the backtest stack.
- @entities/tools/riskfolio-lib.md — companion library; portfolio-level optimization layer, same resolution gap as FinanceToolkit

## Raw Concept

Highly specialized framework for **ultra-precise, high-frequency trading + market-making backtesting**. Differentiates from standard daily-bar tools by ingesting microsecond-level tick data — specifically Level-2 Market-By-Price (MBP) and Level-3 Market-By-Order (MBO) data. Identified as **Adopt-tier** in the K31 Gemini DR eval (`@sources/5-5-moarrr-tool-eval.md` URL 15).

## Narrative

- **Repo**: [github.com/nkaz001/hftbacktest](https://github.com/nkaz001/hftbacktest) — 4,015 ★, 780 forks, 30 contributors
- **License**: **MIT** ✅ — verified against LICENSE file. [CONFIRMED]
- **Latest release**: `rust-v0.9.4` / `py-v2.4.4` (Dec 10, 2025) — PyPI maturity: **Production/Stable** (5/5)
- **Stack**: Python (≥3.11) + Rust core (76% Rust / 24% Python). Dependencies: `numpy>=2.0,<2.3`, `numba~=0.61`, `polars`, `matplotlib`, `holoviews`. Optional: `databento`.
- **Rust toolchain on Hetzner**: **NOT required** — pre-built `bdist_wheel` on PyPI includes compiled Rust backend. `pip install hftbacktest` succeeds in a venv on Hetzner. ✅
- **Data formats**: Level-2 MBP + Level-3 MBO tick-by-tick; venue-agnostic ingestion (works with any MBP/MBO feed, not equity-specific)
- **Build**: `maturin` build backend; Rust >= 1.91.1 if building from source

### Why Adopt for Cemini

Cemini's existing backtest plumbing (per `@concepts/prediction-market-historical-analysis.md`) covers the **Storage / Aggregation / Schema** layers but NOT microsecond-level execution simulation. For:

| Use case | Why hftbacktest is load-bearing |
|---|---|
| **Polymarket CLOB market-making** | MM spread + inventory parameters depend on microstructure (queue position, order-book depth, latency). Per `@concepts/polymarket-market-making-architectures.md`, all 5 reference MM impls assume microstructure-aware tuning |
| **Kalshi orderbook market-making** | Same, on the Kalshi side of the venue mix |
| **Polymarket-Kalshi cross-venue arbitrage** | Per `@concepts/cross-venue-arbitrage-pattern.md` risk caveat #1 ("network latency between venues — windows close fast"), arb-loop tuning needs latency-adjusted backtest. hftbacktest's event-order correction algorithm is the canonical primitive. |
| **Klaassen-Magnus Elo backtests** (per `@briefs/2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md`) | Tennis-prediction-market live execution requires latency-adjusted entry timing |

### Integration

- **Phase 0**: ✅ COMPLETE — source audit passed, license verified MIT, wheel install confirmed on Hetzner
- **Phase 1**: Drop into sandbox and replicate one Cemini backtest (e.g., a Polymarket-Kalshi BTC arb scenario) using hftbacktest's MBP ingest
- **Phase 2**: Integrate as a backtest-substrate in `services/llm_analyst/backtest/` alongside existing Riskfolio-Lib + FinanceToolkit
- **Phase 3**: Wire to Conductor as a `historical_replay` taxonomy class with `@mcp.tool` decorators

### Open questions

- [x] Exact GitHub URL — ~~per eval URL 15~~ → **confirmed `nkaz001/hftbacktest`**
- [x] License — ~~NEEDS VERIFICATION~~ → **MIT confirmed**
- [x] Maturity signals — ~~per eval~~ → **Production/Stable (v2.4.4), 4K+ stars, 30 contributors**
- [ ] Polymarket/Kalshi data-shape adaptation — MBP/MBO ingest is venue-agnostic, but Polymarket CLOB and Kalshi orderbook require adapter shims to map to hftbacktest's expected schema (see brief Phase 1 scope)
- [ ] Compute footprint — microsecond-tick data is 10⁶× daily bars; Phase 1 must verify Hetzner CPX31 (7 GB RAM, 75 GB disk) handles realistic 6-month backtest windows
- [ ] Build from source — if wheel install is insufficient, Rust 1.91.1+ needed; currently not on Hetzner

### Adoption gating

- Phase 0 source audit: **PASS** (license MIT, maturity Production/Stable, no Rust toolchain bottleneck)
- GO verdict: **GO** ✅ — proceed to Phase 1 sandbox replication
- If issues: mark NO-GO with documented re-evaluation triggers, follow K28+K30 audit-pattern discipline

## Snippets

- **Scope framing** (K31 eval): "Highly specialized framework engineered for ultra-precise, high-frequency trading and market-making backtesting... ingests microsecond-level tick data—specifically Level-2 Market-By-Price and Level-3 Ma[rket-by-Order]." [Source: 5_5 moarrr links.docx URL 15]

- **Recommendation tier**: "Adopt. The quantitative developers should integrate the engine into the Cemini production stack immediately. It resolves a critical capability gap by enabling latency-adjusted backtesting that accurately simulates hyper-liquid environments." [Source: 5_5 moarrr links.docx URL 15]

- **Install**: `pip install hftbacktest` (≥3.11, pre-built wheel includes Rust backend — no cargo needed). Or `git clone https://github.com/nkaz001/hftbacktest && cd py-hftbacktest && pip install -e .` for dev. [Source: README.rst + PyPI]

