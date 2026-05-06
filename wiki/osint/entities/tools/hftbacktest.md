---
title: hftbacktest — High-Frequency Backtesting Framework
type: entity
tags: [tool, backtesting, hft, market-making, microsecond-tick-data, adopt-tier, cemini-production-stack]
keywords: [hftbacktest, level-2-orderbook, level-3-market-by-order, latency-adjusted-backtest, event-order-correction, microsecond-tick]
related:
  - sources/5-5-moarrr-tool-eval.md
  - concepts/prediction-market-historical-analysis.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/polymarket-market-making-architectures.md
  - entities/tools/financetoolkit.md
maturity: draft
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-moarrr-tool-eval.md — origin source: K31 Gemini DR eval URL 15, **Adopt** tier
- @concepts/prediction-market-historical-analysis.md — load-bearing addition to the backtest-pipeline plumbing concept; hftbacktest fills the microsecond-tick gap that daily-bar tools (yfinance EOD, FinanceToolkit GARCH on daily series) don't cover
- @concepts/cross-venue-arbitrage-pattern.md — direct downstream consumer; cross-venue arb threshold-tuning needs latency-adjusted backtests of the Polymarket-CLOB ↔ Kalshi-orderbook timing window
- @concepts/polymarket-market-making-architectures.md — direct downstream consumer; MM strategy parameter-tuning (spread sizing, inventory limits, cadence) requires microstructure-level backtest data
- @entities/tools/financetoolkit.md — companion library; FinanceToolkit covers daily-bar fundamentals, hftbacktest covers microsecond execution simulation. Different time-resolution layers of the backtest stack.

## Raw Concept

Highly specialized framework for **ultra-precise, high-frequency trading + market-making backtesting**. Differentiates from standard daily-bar tools by ingesting microsecond-level tick data — specifically Level-2 Market-By-Price (MBP) and Level-3 Market-By-Order (MBO) data. Identified as **Adopt-tier** in the K31 Gemini DR eval (`@sources/5-5-moarrr-tool-eval.md` URL 15).

## Narrative

- **URL**: per K31 eval URL 15 (verify exact GitHub path during Phase 0 audit)
- **License**: per eval claim — [NEEDS VERIFICATION 2026-05-05]; verify MIT or other permissive license against LICENSE file
- **Stack**: Python + likely Rust core (typical for HFT backtesters; verify in Phase 0)
- **Maturity signals**: per eval, framework supports Level-2 MBP + Level-3 MBO data ingestion + event-order correction algorithms — production-grade tooling implied. Stars / commits / latest-version specifics [NEEDS VERIFICATION 2026-05-05]

### Why Adopt for Cemini

Cemini's existing backtest plumbing (per `@concepts/prediction-market-historical-analysis.md`) covers the **Storage / Aggregation / Schema** layers but NOT microsecond-level execution simulation. For:

| Use case | Why hftbacktest is load-bearing |
|---|---|
| **Polymarket CLOB market-making** | MM spread + inventory parameters depend on microstructure (queue position, order-book depth, latency). Per `@concepts/polymarket-market-making-architectures.md`, all 5 reference MM impls assume microstructure-aware tuning |
| **Kalshi orderbook market-making** | Same, on the Kalshi side of the venue mix |
| **Polymarket-Kalshi cross-venue arbitrage** | Per `@concepts/cross-venue-arbitrage-pattern.md` risk caveat #1 ("network latency between venues — windows close fast"), arb-loop tuning needs latency-adjusted backtest. hftbacktest's event-order correction algorithm is the canonical primitive. |
| **Klaassen-Magnus Elo backtests** (per `@briefs/2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md`) | Tennis-prediction-market live execution requires latency-adjusted entry timing |

### Integration

- Phase 0: clone repo, verify license + stars + commits, inspect API surface (Python? Rust core? Polars-friendly?)
- Phase 1: drop into a sandbox and replicate one Cemini backtest (e.g., a Polymarket-Kalshi BTC arb scenario) using hftbacktest's MBP ingest
- Phase 2: integrate as a backtest-substrate in `services/llm_analyst/backtest/` alongside existing Riskfolio-Lib + FinanceToolkit
- Phase 3: wire to Conductor as a `historical_replay` taxonomy class with `@mcp.tool` decorators

### Open questions [NEEDS VERIFICATION 2026-05-05]

- Exact GitHub URL + license + stars + commits + latest version + PyPI package name
- Whether the framework natively supports Polymarket / Kalshi data formats, or if Cemini needs adapter shims
- Compute footprint — microsecond-tick data is 10⁶× the volume of daily bars; verify Hetzner CPX31's 7 GB RAM + 75 GB disk envelope handles realistic 6-month backtest windows
- License compatibility check (eval-claim verification before commit)

### Adoption gating

- Phase 0 source audit (Explore agent template — same as K28 SwarmVault, K30 PageIndex)
- If GO: stage Phase 1+ as a new prod brief, sister to `@briefs/2026-05-04_quant-libs-fastmcp-integration.md`. Both briefs land in `services/llm_analyst/`.
- If issues: mark NO-GO with documented re-evaluation triggers, follow K28+K30 audit-pattern discipline

## Snippets

- **Scope framing** (K31 eval): "Highly specialized framework engineered for ultra-precise, high-frequency trading and market-making backtesting... ingests microsecond-level tick data—specifically Level-2 Market-By-Price and Level-3 Ma[rket-by-Order]." [Source: 5_5 moarrr links.docx URL 15]

- **Recommendation tier**: "Adopt. The quantitative developers should integrate the engine into the Cemini production stack immediately. It resolves a critical capability gap by enabling latency-adjusted backtesting that accurately simulates hyper-liquid environments. Implementing the utility's event-order correction algorithm[...]." [Source: 5_5 moarrr links.docx URL 15]
