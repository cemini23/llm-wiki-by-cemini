---
title: Cross-Venue Arbitrage Pattern — Polymarket × Kalshi BTC Reference Architecture
type: concept
tags: [trading-strategy, arbitrage, prediction-markets, polymarket, kalshi, architectural-pattern, cross-doc-duplicate-signal, k30-synthesis]
keywords: [cross-venue-arbitrage, polymarket-kalshi-arb, btc-arbitrage, atomic-execution, dual-venue-pricing, partial-fill-risk, cross-doc-duplicate]
related:
  - sources/5-5-links-2-tool-eval.md
  - sources/links-3-5-4-tool-eval.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/high-signal-paper-patterns.md
  - sources/polymarket-microstructure-anatomy-2604.24366.md
  - sources/polymarket-nba-arbitrage-2605.00864.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/prediction-market-historical-analysis.md
  - concepts/kalshi-api-reference.md
  - concepts/non-latency-arbitrage-strategies.md
  - concepts/polymarket-marginal-polytope-arbitrage.md
  - concepts/prediction-market-statistical-arbitrage.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - entities/tools/pmxt.md
  - sources/analyzing-github-projects-agentic-infra-2026-05-21.md
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - sources/multi-wiki-link-eval-41url-2026-05-18.md
  - entities/tools/hftbacktest.md
  - entities/tools/prediction-market-analysis.md
  - entities/tools/poly-arbitrage-bot.md
  - concepts/perps-dex-funding-carry-strategy.md
  - entities/tools/suislanchez-polymarket-kalshi-weather-bot.md
  - entities/tools/aruneshdev-kalshi-weather-xgboost.md
  - concepts/cemini-backtest-report-kit.md
  - meta/cross-venue-backtest-cadence.md
  - concepts/world-cup-advance-market-bot-v1.md
  - sources/gemini-world-cup-squad-mispricing-analysis-2026-05-29.md
  - sources/gemini-sports-prediction-bot-pitfalls-2026-05-29.md
  - sources/gemini-world-cup-market-structure-research-2026-05-29.md
  - sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md
  - sources/gemini-wc2026-cross-venue-arbitrage-dynamics-2026-05-29.md
  - sources/world-cup-youtube-research-compilation-2026-05-29.md
maturity: draft
created: 2026-05-05
updated: 2026-05-29
---

## Relations

- @sources/5-5-links-2-tool-eval.md — origin URL 8 (Polymarket-Kalshi BTC Arbitrage Bot, MIT, Steal-from tier)
- @sources/links-3-5-4-tool-eval.md — origin URL 17 (same project, second independent Steal-from verdict — the cross-doc-duplicate signal)
- @entities/platforms/polymarket.md — venue 1 of 2 in the canonical pair
- @entities/platforms/kalshi.md — venue 2 of 2 in the canonical pair
- @concepts/polymarket-market-making-architectures.md — sibling K30 synthesis; some Polymarket MM impls bundle arbitrage as a strategy (e.g., Polymarket Trading Bot v3.1's `Arbitrage` and `DipArb`); the core arb-loop is the same
- @concepts/high-signal-paper-patterns.md — K8/K9 cross-doc-duplicate discipline source; this page is a direct application of that signal-detection rule
- @sources/polymarket-microstructure-anatomy-2604.24366.md — canonical Polymarket microstructure study; documents the depth-decay, spread, and liquidity dynamics that constrain cross-venue arb execution
- @sources/polymarket-nba-arbitrage-2605.00864.md — companion NBA arb study; shares same data ecosystem, documents shallow-depth constraint on executable arb size
- @concepts/polymarket-microstructure-findings.md — distilled findings from Dubach 2026; key constraint: public-feed direction is unreliable, must use on-chain OrderFilled events
- @concepts/prediction-market-historical-analysis.md — historical price-divergence statistics inform arb threshold-tuning + viability assessment
- @concepts/non-latency-arbitrage-strategies.md — the slow-arb complement: standing-order strategies (Dutch-book, YES/NO complement, slow cross-venue, calendar) whose edge is a logical inconsistency rather than a ms-scale quote race
- @concepts/prediction-market-statistical-arbitrage.md — the quant *signal* layer for this loop: cointegration + Ornstein-Uhlenbeck calibration decides *when* a Poly×Kalshi spread is tradeable and at what threshold; this page is the poll→execute→reconcile machinery that acts on it
- @concepts/polymarket-updown-bot-taxonomy.md — K52 6-type bot taxonomy; its Type 4 (cross-timeframe lag, 5min↔15min) is the within-venue cousin of this cross-venue loop
- @sources/x-posts-quant-oss-polymarket-bots-2026-05.md — K52 X-posts batch; Post 4 (@ridark_eth) supplies the quant math layer for this loop
- @entities/tools/prediction-market-analysis.md — K52-verified MIT dataset; its cross-venue `comparison/` analyses + trade-price history are a backtest substrate for tuning this loop's profit thresholds
- @sources/multi-wiki-link-eval-41url-2026-05-18.md — K53 eval; surfaced `zostaff/poly-arbitrage-bot`, a concrete implementation of this pattern
- @entities/tools/poly-arbitrage-bot.md — a small (~20★) but on-target MIT implementation of this exact Polymarket↔Kalshi arb loop; Reference/Steal-from for the dual-venue auth + paper-trading patterns
- @entities/tools/suislanchez-polymarket-kalshi-weather-bot.md — K60: same dual-venue pattern on **weather** (KXHIGH + Polymarket temperature), not BTC price arb
- @entities/tools/aruneshdev-kalshi-weather-xgboost.md — K66: Kalshi-origin weather ML; Polymarket port per @AlterEgo_eth
- @concepts/cemini-backtest-report-kit.md — Phase 3 laptop divergence lab (`scripts/cross_venue_backtest/`)
- @meta/cross-venue-backtest-cadence.md — quarterly re-run ritual
- @concepts/world-cup-advance-market-bot-v1.md — K82 FIFA advance-market alert-only scanner (v1)
- @sources/gemini-world-cup-squad-mispricing-analysis-2026-05-29.md — book vs PM/Kalshi divergence table
- @sources/world-cup-youtube-research-compilation-2026-05-29.md — SharpMoney Kalshi API + Dextrabot cross-venue mechanics

## Raw Concept

The Polymarket-Kalshi BTC Arbitrage Bot (MIT) is the only project to receive a Steal-from-tier verdict in **two independent Gemini DR eval batches** during K30 (2026-05-05 Polymarket-readiness wave): once in `5_5 links 2.docx` URL 8 and once in `links 3 5_4.docx` URL 17. Per the K8/K9 ingest discipline (`@concepts/high-signal-paper-patterns.md`), cross-doc duplicates are a high-confidence architectural-pattern signal — both evaluators independently surfaced the same project, both assigned the same verdict, both quoted similar value-extraction language.

This concept page documents the architectural pattern (cross-venue arbitrage on prediction markets) so Cemini's eventual implementation has a baseline reference rather than re-deriving from source pages each time.

## Narrative

### The signal: why this pattern matters

Two independent Gemini DR evaluator passes, run with different prompt framings (one focused on prediction-market-and-trading-stack, the other focused on Cemini Stack & Wiki Stack), surfaced the same project as a worth-stealing-from architectural reference. That convergence is rare:

| Eval batch | URL | Tools evaluated | Verdict on Polymarket-Kalshi BTC Arb Bot |
|---|---|---|---|
| `5_5 links 2.docx` | URL 8 | 32 prediction-market tools | Steal-from (full-stack arb monitor + visualizer) |
| `links 3 5_4.docx` | URL 17 | 24 Cemini-stack tools | Steal-from (real-time risk-free profit-opportunity scanner) |

Per `@concepts/high-signal-paper-patterns.md` cross-doc-duplicate rules, this is among the strongest in-corpus signals we've registered. The implication: the architectural pattern is load-bearing for Cemini's eventual cross-venue arb workstream, even if the specific implementation isn't directly adopted.

### The architectural pattern

Extracted from both evals' descriptions of the project's runtime:

```
┌──────────────────────────────────────────────────────────────────┐
│              Cross-venue arbitrage loop (per cycle)              │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. POLL — fetch current Polymarket CLOB prices + Kalshi         │
│     orderbook, in parallel (latency budget ~50-100ms)            │
│                                                                  │
│  2. DETECT — compute the price difference for the same           │
│     underlying contract (e.g. BTC > $X by Y o'clock today)       │
│                                                                  │
│  3. THRESHOLD — gate on profit_threshold ≥ (estimated fees +     │
│     Polygon gas + slippage + safety margin)                      │
│                                                                  │
│  4. EXECUTE — if threshold met, place both legs (buy on cheaper  │
│     venue, sell on expensive) concurrently. Record both order    │
│     IDs.                                                         │
│                                                                  │
│  5. RECONCILE — within a fixed window (~1-3s), confirm both      │
│     fills.                                                       │
│         If both filled: profit captured; record P&L.             │
│         If one filled, one didn't: cancel the unfilled, hold     │
│           the orphaned position, log the partial-fill event.     │
│         If neither filled: no-op, return to POLL.                │
│                                                                  │
│  6. SLEEP — back to POLL after a configurable interval (depends  │
│     on cadence requirement; for BTC 1h contracts ~250-500ms).    │
└──────────────────────────────────────────────────────────────────┘
```

### Risk caveats (what makes this hard, not what makes it impossible)

1. **Network latency between venues** — windows close fast. Polymarket settles on Polygon (block time ~2s); Kalshi is centralized API. Cross-Atlantic latency between Cemini's Hetzner host and the venues' edges varies. Tight windows demand co-located or low-latency connectivity, not just any cloud host.

2. **Fee structures differ across venues**:
   - Polymarket: Polygon network gas (variable, USD-cents-per-tx) + zero exchange fee
   - Kalshi: maker rebate / taker fee schedule (variable per market and side)
   - Both: USDC slippage on size

   The profit-threshold gate (step 3) must compute these correctly. A simple "spread > $0.01" rule is wrong; the right rule is "spread > all-in costs + safety margin."

3. **Partial-fill risk** — if leg A executes and leg B doesn't, Cemini holds an unhedged directional position. Recovery options:
   - Wait for leg B to fill at the same price (timer; if exceeded, cancel and accept the orphan)
   - Aggressively re-quote leg B at worse pricing to force a fill
   - Hedge via a third-venue position if the orphan is large
   
   Each option has its own risk; choice depends on operator's discretionary loss tolerance.

4. **Jurisdictional issues** — Cemini operator residency vs venue access. Per `@wiki/concepts/cemini-deployment.md`, US operators can use Kalshi and (carefully) Polymarket; EU operators face geo-blocks. Same applies to server hosting region. This isn't a code problem; it's a legal + infrastructure problem.

5. **Same-contract identification** — Polymarket and Kalshi list contracts under different naming conventions for the same underlying event ("BTC > $X by Y" vs equivalent). The contract-mapping step is non-trivial and needs careful curation. Misidentification = arbitraging two different contracts ≠ risk-free profit.

6. **Resolution timing** — both venues resolve contracts at known cutoff times, but the resolution mechanism differs (Polymarket via UMA optimistic oracle; Kalshi via internal ToS-based determination). On rare occasions resolutions diverge. The arb assumption is that both venues will resolve identically; verify this for each contract pair before going live.

### Cemini-side application

#### Initial scope: BTC 1h Bitcoin pricing contracts

The cross-doc-duplicate project specifically targets BTC contracts, suggesting the BTC pair is the canonical entry point. Both venues list 1-hour BTC pricing markets continuously; the same underlying (BTC-USD spot, sourced from Coinbase/Binance/etc.) drives both resolutions. Lowest contract-mapping risk + highest liquidity.

#### Expansion: any asset listed on both venues

The pattern is asset-agnostic. After BTC validation, extend to:
- ETH 1h pricing
- Election contracts (Trump-Biden 2024 was the canonical historical example; future presidential and major-state elections)
- Sports binary outcomes (per `@memory/prediction_market_scope`, sports is in scope)
- Healthcare/biotech catalysts (FDA approval contracts on both venues)

Each extension requires its own contract-mapping curation step. Don't auto-generalize from BTC.

#### Pairs with K30 Polymarket Stack adoption

The arb loop **depends on** the K30 Polymarket integration stack (`@briefs/2026-05-05_polymarket-stack-adoption.md`):
- Polymarket Agents (foundation)
- python-order-utils (signing)
- py-clob-client (CLOB API)
- polymarket-mcp-server (MCP bridge)

…plus Cemini's existing Kalshi integration (which K30 will refresh via pykalshi adoption per `@entities/tools/pykalshi.md`).

**Don't start arb work before the foundation ships.** Once both venue integrations are stable, the arb loop is a thin layer on top.

#### Optional: bundle into Polymarket MM

Per `@concepts/polymarket-market-making-architectures.md`, the multi-strategy bundling posture (Polymarket Trading Bot v3.1) packages arbitrage as a sibling strategy alongside two-sided MM and smart-money copy. Cemini can either:
- Run cross-venue arb as its own service (single-purpose, easier to reason about)
- Bundle into the larger MM runtime (more efficient resource usage, more coupling)

Recommended: standalone service for v1; bundle later if operations show that resource sharing is the bottleneck.

### What we don't take from the cross-doc-duplicate project

- The specific UI / visualization layer (Cemini is headless)
- TypeScript / Node parts (Cemini is Python; rewrite)
- Hardcoded configuration values (re-tune for Cemini's cost/latency profile)

The pattern is the asset, not the code.

### K82 extension — World Cup advance markets (alert-only v1)

@concepts/world-cup-advance-market-bot-v1.md applies this loop to **FIFA 2026 group-stage advance** contracts on Polymarket vs Kalshi. Key deltas vs BTC hourly arb:

| Dimension | BTC arb reference | WC advance v1 |
|-----------|-------------------|---------------|
| Contract mapping | Same underlying, different tickers | **Semantic rules match** mandatory — UMA (PM) vs ESPN/FOX (Kalshi); 90-min vs ET |
| Execution | Auto both legs | **Alert-only** — human or Phase-2 auto after ticker map validated |
| Threshold | Fee + gas + slippage | **≥5pp** after venue fees; ignore &lt;3pp noise |
| Price source | CLOB + Kalshi API at runtime | Same — **no hardcoded mids**; prod Gamma/CLOB keys on `cemini-prod` |
| Inventory risk | Short horizon | Squad news / injury repricing — scanner is signal, LP bot handles inventory |

Pending Gemini report #5 for full PM↔Kalshi ticker map. **Resolved K83:** @sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md — group-winner map live; advance pairs blocked (PM TBD). Ticker seed: `world-cup-bot/config/cross_venue.yaml`.

### World Cup 2026 live verification (K83) [CONFIRMED 2026-05-29]

- **Pairable today:** `KXWCGROUPWIN` ↔ PM group-winner only (USA, SUI, ENG, CRO, MEX fade_watch set).
- **Not pairable:** PM advance-to-knockout slugs TBD; Kalshi `KXWCGROUPQUAL` vs PM advance = rules mismatch.
- **Alerts:** zero pairs ≥5pp raw on verified equivalents; fee-adjusted all negative EV.
- **Bot config:** alert-only; no auto-hedge. Prior K82 book-gap narrative retained as fade_watch sentiment, not arb signal.

See @sources/gemini-wc2026-cross-venue-arbitrage-dynamics-2026-05-29.md for contract taxonomy reference.

## Snippets

- **First eval verdict** (`5_5 links 2.docx` URL 8): "This is a full-stack application explicitly designed to monitor, identify, and visualize risk-free arbitrage opportunities within Bitcoin 1[-hour markets]." [Source: 5_5 links 2.docx URL 8]

- **Second eval verdict** (`links 3 5_4.docx` URL 17): "A real-time arbitrage scanner specifically programmed to detect mathematically risk-free profit opportunities existing between the Polymarke[t and Kalshi BTC markets]." [Source: links 3 5_4.docx URL 17]

- **Cross-doc-duplicate framing** (per `@concepts/high-signal-paper-patterns.md`): "Cross-doc duplicates are an explicit signal of high-relevance per the K8 + K9 ingest discipline. Two independent evals reach Steal-from verdict for [the same] arbitrage scanner — pattern is the load-bearing extract." [Source: K30 cross-doc analysis]

## Dead Ends

*(none yet — first synthesis. Future updates record specific arb-pair attempts that failed, e.g. "tried ETH 4h, contract-mapping mismatched too often, abandoned 2026-MM-DD" so the same dead end isn't re-walked.)*
