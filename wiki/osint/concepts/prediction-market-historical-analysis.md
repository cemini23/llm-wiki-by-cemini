---
title: Prediction-Market Historical Analysis — Backtest Pipeline Foundation
type: concept
tags: [trading-strategy, prediction-markets, historical-data, backtest-pipeline, polymarket, kalshi, k30-synthesis]
keywords: [historical-data-harness, prediction-market-analysis, polymarket-sports-analysis, indexing-aggregation, schema-standardization, backtest-foundation]
related:
  - sources/5-5-links-2-tool-eval.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/cross-venue-arbitrage-pattern.md
  - entities/tools/financedatabase.md
  - entities/tools/financetoolkit.md
  - entities/tools/klaassen-magnus-elo.md
maturity: draft
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-links-2-tool-eval.md — origin source surfacing 3 historical-data harness Steal-from items: URL 6 (`prediction-market-analysis`), URL 16 (`polymarket-sports-analysis`), URL 2 (`kalshi-ai-trading-bot` historical layer)
- @entities/platforms/polymarket.md — one of two canonical venues this analysis targets
- @entities/platforms/kalshi.md — second canonical venue
- @concepts/polymarket-market-making-architectures.md — sibling K30 synthesis; MM strategy parameters (spread sizing, inventory limits, cadence) are tuned against historical data
- sources/polymarket-microstructure-anatomy-2604.24366.md — canonical Polymarket microstructure study; replication package directly usable as Layer 1 harvester
- @concepts/polymarket-microstructure-findings.md — distilled findings; documents constraints on trade-direction inference and public-feed limitations
- @concepts/cross-venue-arbitrage-pattern.md — sibling K30 synthesis; arb threshold-tuning and viability assessment depend on historical price-divergence statistics
- @entities/tools/financedatabase.md — K30 Adopt; 300k offline financial-symbol catalog, complementary to prediction-market historical data (one is symbol-universe, the other is venue-specific time series)
- @entities/tools/financetoolkit.md — K28 Adopt; 150-metric library that operates over historical data (downstream consumer)
- @entities/tools/klaassen-magnus-elo.md — K28 Steal-from; tennis-prediction Elo runs on historical match data, the predictions feed prediction-market trades — direct downstream consumer

## Raw Concept

Three Steal-from items in the K30 5_5-links-2 batch all converge on the same architectural problem: **how do you build the historical-data foundation that prediction-market backtests, MM parameter tuning, and cross-venue arb viability all sit on top of?** This page synthesizes the lifted patterns into one design rubric for Cemini's eventual prediction-market backtest pipeline.

The current Cemini `market dataset/` layout is real-time-focused (per `@CLAUDE.md`). Adding a historical-data substrate is a separate workstream — not "more of the same" but a fundamentally different quality bar (point-in-time correctness, replay determinism, cross-venue schema reconciliation).

## Narrative

### Why this matters for Cemini

Every downstream Cemini workstream eventually needs canonical prediction-market historical data:

| Downstream consumer | Need |
|---|---|
| Polymarket MM strategy tuning | Per-market spread + cadence parameters require historical liquidity profile |
| Kalshi MM strategy tuning | Same |
| Cross-venue arbitrage threshold-tuning | Historical price-divergence statistics inform profit-threshold calibration |
| Klaassen-Magnus Elo tennis prediction | Historical tennis match outcomes (commercial-data-licensed; per `@entities/tools/klaassen-magnus-elo.md`) feed the Elo + predict prediction-market positions |
| Conductor cost / quality A/B | Routing-decision improvements require backtest-replayable prediction-market scenarios |
| Risk model calibration | VaR / drawdown distributions need point-in-time-correct historical samples |

Without a clean historical-data substrate, every downstream workstream re-implements its own ingest. Centralizing the substrate is the leverage point.

### The lifted patterns

Three K30 Steal-from items contributed:

#### 1. `prediction-market-analysis` (`@sources/5-5-links-2-tool-eval.md` URL 6, MIT)

> "Highly comprehensive Python framework designed to collect, index, and analyze massive amounts of historical data from prediction m[arkets]." [Source: 5_5 links 2.docx URL 6]

Provides: end-to-end harvest + index + analyze pattern across multiple prediction-market venues. The most comprehensive of the three; the architectural reference.

#### 2. `polymarket-sports-analysis` (`@sources/5-5-links-2-tool-eval.md` URL 16, MIT)

> "Highly structured Python-based data analytics suite tailored explicitly for tracking and analyzing sports prediction markets." [Source: 5_5 links 2.docx URL 16]

Provides: domain-specific extension pattern (sports markets have distinctive resolution mechanics — game outcomes, point spreads, etc.). Direct relevance per `@memory/prediction_market_scope` (Cemini's prediction-market scope explicitly includes sports).

#### 3. `kalshi-ai-trading-bot` historical layer (`@sources/5-5-links-2-tool-eval.md` URL 2, MIT)

> "Comprehensive toolkit for constructing automated trading strategies specifically targeting the Kalshi prediction m[arket]." [Source: 5_5 links 2.docx URL 2]

Provides: Kalshi-specific historical-data ingest patterns. The runtime architecture also covers strategy execution (per `@sources/5-5-links-2-tool-eval.md`, Steal-from for runtime patterns), but the historical-layer is what feeds this concept page.

### Architecture

Synthesizing the three patterns:

```
┌────────────────────────────────────────────────────────────────────┐
│              Cemini Prediction-Market Historical Stack             │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Layer 1 — Collection (rate-limited venue API harvest)             │
│    Polymarket harvester  → CLOB historical endpoint                │
│    Kalshi harvester      → trades + market-resolution endpoints    │
│    Sports-data harvester → commercial-licensed feed (per           │
│                            @entities/tools/klaassen-magnus-elo.md  │
│                            license-pattern caveat)                 │
│    All harvesters: explicit rate-limit handling, resume from       │
│      checkpoint, idempotent writes                                 │
│                                                                    │
│  Layer 2 — Storage / indexing (canonical at-rest format)           │
│    Per-venue Parquet files partitioned by date + market            │
│    SQLite FTS index for contract-name lookup                       │
│    pgvector index for semantic-similarity contract matching        │
│      (e.g., "find Kalshi market closest to this Polymarket         │
│      contract")                                                    │
│                                                                    │
│  Layer 3 — Aggregation (per-contract / per-venue / per-window)     │
│    Per-contract daily / hourly / minute roll-ups                   │
│    Per-venue volume + spread + inventory profiles                  │
│    Cross-venue same-contract pricing-divergence series (feeds      │
│      @concepts/cross-venue-arbitrage-pattern.md)                   │
│                                                                    │
│  Layer 4 — Schema standardization                                  │
│    Kalshi shape ↔ Polymarket shape ↔ Cemini canonical shape        │
│    The non-trivial part: contract identification across venues     │
│      (the same problem from cross-venue-arbitrage-pattern.md)      │
│                                                                    │
│  Layer 5 — Backtest interface (the consumer surface)               │
│    Replayable historical-tape API: `replay(start, end, venues=)` → │
│      stream of synthetic-market events                             │
│    Point-in-time correctness: never-leak future data into a        │
│      backtest reading at time T                                    │
└────────────────────────────────────────────────────────────────────┘
```

### Cemini implementation outline

**Storage location**: extend the existing `market dataset/` layout (per `@CLAUDE.md`). New subtrees:
- `market dataset/prediction-markets/polymarket/` — Parquet files, date-partitioned
- `market dataset/prediction-markets/kalshi/` — same
- `market dataset/prediction-markets/sports/` — commercial-licensed feed cache (NC-data-pattern-aware per `@concepts/cemini-license-posture.md` pattern #4)

**Scripts**: new under `scripts/`:
- `harvest_polymarket_history.py` — Layer 1
- `harvest_kalshi_history.py` — Layer 1
- `index_prediction_markets.py` — Layer 2 (SQLite FTS + pgvector)
- `aggregate_prediction_markets.py` — Layer 3
- `replay_prediction_market.py` — Layer 5 backtest interface

**Entity entries**: add `entities/data-sources/polymarket-history.md` and `entities/data-sources/kalshi-history.md` once Layer 1 ships.

### Backtest pipeline implications

This concept is the **plumbing** under multiple downstream briefs:

| Brief | Reads from this stack |
|---|---|
| `@briefs/2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md` | Tennis historical data → Elo backtest |
| `@briefs/2026-05-04_quant-libs-fastmcp-integration.md` | Riskfolio-Lib + FinanceToolkit operate over historical samples |
| `@briefs/2026-05-04_probablyprofit-pattern-extraction.md` | Kelly + ensemble validation requires backtest-replayable scenarios |
| `@briefs/2026-05-05_polymarket-stack-adoption.md` | Polymarket strategy parameter tuning |
| `@briefs/2026-05-04_autoresearch-conductor-evolution.md` | Conductor's autoresearch fitness function may use backtest results as one of its objective signals |

**None of those briefs depend on this concept being built first** — they can ship without it. But once they ship, the question of "where does the historical data come from" is unavoidable, and this page is the answer.

### Cemini-side action items

1. **Harvester brief shipped** — `briefs/2026-05-09_polymarket-onchain-data-pipeline.md` covers integration of Dubach's `polydata.onchain` pipeline as Layer 1. This is the primary action item.
2. **Kalshi equivalent** — `pykalshi` is adopted (K30) but needs its own Layer 1 harvester script (parallel workstream).
3. **License caveat** — sports historical data is the highest-license-risk vertical (per `@entities/tools/klaassen-magnus-elo.md` and `@concepts/cemini-license-posture.md` pattern #4 CC-BY-NC training-data contamination). Polymarket + Kalshi own data are MIT-licensed-equivalent (their public APIs); third-party sports feeds need commercial licensing.
4. **Cross-venue contract identification is the hard problem** — invest curator time on the contract-mapping table BEFORE writing any cross-venue logic (arb, comparison, etc.). Same problem appears in `@concepts/cross-venue-arbitrage-pattern.md`.
5. **Don't over-design Layer 5** — the backtest interface should be intentionally simple (event-replay over canonical Parquet files). Resist the urge to build a full backtest framework here; downstream consumers can compose their own backtest logic on top of replay primitives.

### What we don't take

- The specific visualization / dashboard layers in `prediction-market-analysis` (Cemini is headless; replay output goes to logs + Parquet, not browser dashboards)
- Hardcoded venue-specific assumptions in `kalshi-ai-trading-bot`'s historical layer (re-derive against current Kalshi API; Kalshi's API has evolved since the upstream's commit history)
- Sports-rules logic in `polymarket-sports-analysis` (sport-specific business logic doesn't belong in the historical-data layer; lives in the strategy layer)

The patterns are at the architectural-shape level, not the line-of-code level.

## Snippets

- **prediction-market-analysis scope** (URL 6): "Highly comprehensive Python framework designed to collect, index, and analyze massive amounts of historical data from prediction m[arkets]." [Source: 5_5 links 2.docx URL 6]

- **polymarket-sports-analysis specialization** (URL 16): "Highly structured Python-based data analytics suite tailored explicitly for tracking and analyzing sports prediction markets." [Source: 5_5 links 2.docx URL 16]

- **kalshi-ai-trading-bot historical layer** (URL 2): "Comprehensive toolkit for constructing automated trading strategies specifically targeting the Kalshi prediction m[arket]." [Source: 5_5 links 2.docx URL 2]

- **License caveat for sports data** (per `@entities/tools/klaassen-magnus-elo.md`): tennis_atp dataset is CC-BY-NC-SA 4.0; algorithm extracts cleanly under MIT but data-coupled weights inherit NC restriction. Same pattern applies to any sports historical-data vendor — verify licensing of the feed before training derivative models. [Source: K28 license-pattern catalog #4]

## Dead Ends

*(none yet — first synthesis. Future updates land here when a specific harvester / aggregation / schema-mapping approach is rejected during Cemini's eventual implementation.)*
