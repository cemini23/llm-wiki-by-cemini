---
title: Polymarket Market-Making Architectures — Synthesis of 5 MIT Reference Implementations
type: concept
tags: [trading-strategy, market-making, polymarket, prediction-markets, mit, architectural-pattern, k30-synthesis]
keywords: [polymarket-mm, market-making, amm-keeper, two-sided-liquidity, risk-aware-mm, smart-money-copy, btc-15min-niche, polymarket-trading-bot-v3]
related:
  - sources/links-3-5-4-tool-eval.md
  - sources/polymarket-5-5-tool-eval.md
  - sources/5-5-links-2-tool-eval.md
  - sources/polymarket-microstructure-anatomy-2604.24366.md
  - sources/polymarket-nba-arbitrage-2605.00864.md
  - concepts/polymarket-microstructure-findings.md
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-agents.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/prediction-market-historical-analysis.md
  - concepts/polymarket-lp-rewards-farming.md
maturity: draft
hub: true
created: 2026-05-05
updated: 2026-05-20
---

## Relations

- @sources/links-3-5-4-tool-eval.md — origin source: K30 batch evaluating 5 Polymarket MM impls (URLs 11, 12, 14, 19, 20)
- @sources/polymarket-5-5-tool-eval.md — companion K30 batch with related Polymarket-internal tools (py-clob-client, python-order-utils — the substrate any MM impl depends on)
- @sources/5-5-links-2-tool-eval.md — additional K30 batch with prediction-market-analysis (historical-data harness that feeds MM strategy parameters)
- @entities/platforms/polymarket.md — Polymarket venue entity; this concept describes architectures FOR that venue
- @entities/tools/polymarket-agents.md — official-sanctioned framework foundation; any of the MM patterns below should be built ON Polymarket Agents, not parallel to it
- @concepts/cross-venue-arbitrage-pattern.md — sibling K30 synthesis page; some MM impls below also bundle arbitrage as a strategy
- @concepts/prediction-market-historical-analysis.md — sibling K30 synthesis page; historical data is the parameter-tuning input for any MM strategy

## Raw Concept

Five different Polymarket market-making implementations were surfaced as **Steal-from-tier** in the K30 ingest (2026-05-05 Polymarket-readiness research wave). All five are MIT-licensed; all five are runtime-architecture references, not wholesale-adoption candidates. This page synthesizes their distinguishing patterns into one decision-rubric for Cemini's eventual Polymarket MM workstream.

The pattern density is itself the signal: 5 independently-developed MIT-licensed Polymarket MM systems is the most concentrated single-venue MM ecosystem documented in the wiki. None individually is "the answer" — each represents a different architectural posture. Cemini's eventual MM design picks an architectural posture (or composes several), then implements rather than wholesale-adopts.

## Narrative

### The five reference implementations

| Source | Project | Distinguishing architectural posture | Strategy set | Language | Verdict |
|---|---|---|---|---|---|
| `@sources/links-3-5-4-tool-eval.md` URL 11 | poly-market-maker | **Minimal AMM-keeper** — single-loop automated keeper; cleanest minimal implementation | Single-strategy: AMM-style two-sided | Python | Steal-from |
| `@sources/links-3-5-4-tool-eval.md` URL 12 | poly-maker | **Full two-sided liquidity provider** — comprehensive automated MM with full bid/ask management | Multi-spread strategies on liquid markets | Python | Steal-from |
| `@sources/links-3-5-4-tool-eval.md` URL 14 | polymarket-market-maker | **Risk-aware MM scaffolding** — explicitly risk-controls-first design (drawdown caps, position limits, kill-switch hooks) | Risk-bounded two-sided | Python | Steal-from |
| `@sources/links-3-5-4-tool-eval.md` URL 19 | Polymarket Trading Bot v3.1 - Enhanced Risk Management | **Multi-strategy bundling** — TypeScript, packages 4 strategies in one runtime (Arbitrage, DipArb, Smart Money copy, [4th]) | 4 bundled (arb + DipArb + smart-money copy + ...) | TypeScript | Steal-from |
| `@sources/links-3-5-4-tool-eval.md` URL 20 | Polymarket-BTC-15-Minute-Trading-Bot | **HF-niche specialization** — single-asset, single-time-frame focus on BTC 15-min markets; high-cadence | Single-niche (BTC 15-min only) | Python | Steal-from |

### Architectural postures

Each implementation represents a different point in the MM design space. Cemini chooses by selecting which traits matter most.

#### Posture 1 — Minimal AMM-keeper (poly-market-maker)

**When it fits**: bootstrap stage — Cemini wants to be present on Polymarket as a passive liquidity provider before committing to active strategy. The keeper-loop pattern (poll → decide → place/cancel orders → sleep → repeat) is the irreducible MM core; every other implementation builds on this.

**Extractable**: the loop's decision-frequency calibration, the place/cancel order-pacing, the resilience-to-API-errors discipline.

**Limitations**: no inherent risk controls; a poorly-tuned keeper can sell the entire bankroll in a thin-liquidity market. Pair with explicit kill-switches (per `@briefs/2026-05-04_probablyprofit-pattern-extraction.md`) before live deployment.

#### Posture 2 — Full two-sided liquidity (poly-maker)

**When it fits**: production-grade liquidity provision on Polymarket's high-volume markets (election contracts in election season, sports during seasons, etc.). poly-maker covers the full bid-ask-management problem: spread sizing, inventory rebalancing, adverse-selection protection.

**Extractable**: spread-tuning patterns by contract-volatility, inventory-limit enforcement, the bid/ask cancellation logic when positions get unbalanced.

**Limitations**: Polymarket markets vary wildly in liquidity. A configuration tuned for the BTC-1h market will be wrong for an obscure niche contract. Per-market parameterization needed.

#### Posture 3 — Risk-aware scaffolding (polymarket-market-maker)

**When it fits**: when the operator's primary concern is **bounded loss**, not maximum profit. polymarket-market-maker is the most conservative of the five — explicit drawdown caps, position limits, and kill-switch integration are first-class concerns.

**Extractable** (most directly Cemini-applicable): the risk-controls-first scaffolding pattern. Combine with K28's probablyprofit kill-switch + Riskfolio-Lib position-sizing (per `@briefs/2026-05-04_quant-libs-fastmcp-integration.md`) to form the production safety harness.

**Recommended Cemini starting point**: build on this scaffolding, layer strategies from Postures 2 and 4 on top.

#### Posture 4 — Multi-strategy bundling (Polymarket Trading Bot v3.1)

**When it fits**: portfolio-of-strategies stage — Cemini operates not just as MM but as a multi-tactic Polymarket participant. The 4-strategies-in-one-runtime architecture solves coordination questions (which strategy gets which capital allocation, how do they share state) that emerge late.

**Extractable**: the strategy-bundling architecture (one runtime, isolated strategy modules, shared connection pool + risk-budget allocator). Smart-money copy-trading pattern specifically — multiple K30 sources (this URL 19 + Polymarket 5_5 URL 17) confirm the pattern.

**Caveat**: TypeScript. Cemini's stack is Python. Useful as architectural reference; full port is not warranted just for this.

#### Posture 5 — HF-niche specialization (Polymarket-BTC-15-Minute-Trading-Bot)

**When it fits**: an opportunistic single-market focus where high-cadence trading exploits a specific time-of-day pattern or volatility regime. BTC 15-minute markets on Polymarket have distinctive microstructure (high resolution + crypto-volatility + regular cadence) that rewards specialization.

**Extractable**: the high-cadence loop tuning, the niche-specialization mindset. A specialized bot can run alongside a general-purpose MM without conflict.

**Limitations**: niches dry up. The 15-min BTC market may not be tomorrow's best opportunity. Don't over-invest in niche-specific code.

### Recommended Cemini reference architecture

Synthesizing the postures into one starting blueprint:

```
┌─────────────────────────────────────────────────────────────────┐
│                  Cemini Polymarket MM (proposed)                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 1: Foundation (from @entities/tools/polymarket-agents)   │
│    Polymarket Agents official-sanctioned framework              │
│                                                                 │
│  Layer 2: Risk-aware scaffolding (from Posture 3)               │
│    Drawdown caps, position limits, kill-switch hooks            │
│    + integration with K28 probablyprofit multi-vector kill      │
│    + integration with K28 Riskfolio-Lib position sizing         │
│                                                                 │
│  Layer 3: Core MM loop (from Posture 1)                         │
│    Minimal keeper loop with explicit decision cadence           │
│    + resilience-to-API-error discipline                         │
│                                                                 │
│  Layer 4: Strategy modules (composable, from Postures 2 + 4)    │
│    - Two-sided liquidity (default; from poly-maker patterns)    │
│    - Smart-money copy-trading (multi-source confirmed pattern)  │
│    - Cross-venue arbitrage (see @concepts/cross-venue-          │
│      arbitrage-pattern.md)                                      │
│    - HF niche (optional; if BTC-15-min opportunity persists)    │
│                                                                 │
│  Layer 5: Parameterization (from @concepts/prediction-market-   │
│           historical-analysis.md)                               │
│    Per-market spread/size/cadence configs derived from          │
│    historical-data backtests                                    │
└─────────────────────────────────────────────────────────────────┘
```

### Cross-pattern observations

- **Risk controls are the differentiator**, not strategy choice. Postures 1, 2, 4 vary on strategy; Posture 3 makes risk first-class. Cemini's existing risk-discipline doctrine (per K28 license-posture + probablyprofit kill-switch) aligns with Posture 3.
- **Smart-money copy** appears in 3+ K30 sources (Polymarket Trading Bot v3.1 + polymarket-copy-trading-bot + cross-references in other batches). This is the single most-confirmed strategy-pattern in the K30 wave.
- **Cross-venue arbitrage** appears in Postures 4 (bundled) AND in the cross-doc-duplicate Polymarket-Kalshi BTC arb (`@concepts/cross-venue-arbitrage-pattern.md`). Treat as a separate workstream, not bundled into MM.
- **None of the 5 are wholesale-adopt** because each ships with strategy choices and parameter values that won't match Cemini's portfolio. The architectural patterns are reusable; the configurations are not.

### Cemini-side action items

1. **No active workstream yet** — Polymarket MM is downstream of the K30 Polymarket Stack Adoption brief (`@briefs/2026-05-05_polymarket-stack-adoption.md`). The integration foundation must ship before MM strategies make sense.
2. **When MM work begins**: this synthesis page is the entry point. Pick a starting posture (recommend Posture 3 risk-aware scaffolding), implement the layers above on top of Polymarket Agents, parameterize from historical data per `@concepts/prediction-market-historical-analysis.md`.
3. **Initial deployment**: paper-trade for ≥30 days before live. Validate kill-switches before any non-trivial capital allocation.
4. **Avoid over-engineering**: pick 2-3 strategy modules max for v1. Add complexity only after v1 demonstrates positive PnL net of fees + gas.

## Snippets

- **poly-market-maker AMM-keeper framing** (URL 11): "Operates as a dedicated automated market maker (AMM) 'keeper' for the Polymarket Central Limit Order Book (CLOB). It systematically..." [Source: links 3 5_4.docx URL 11]

- **poly-maker comprehensive framing** (URL 12): "Comprehensive, automated market-making solution for Polymarket explicitly designed to maintain simultaneous buy and sell orders to ensure..." [Source: links 3 5_4.docx URL 12]

- **polymarket-market-maker risk-aware framing** (URL 14): "Highly disciplined, risk-aware automated market-making infrastructure engineered to provide two-sided liquidity on the Polymarket platform..." [Source: links 3 5_4.docx URL 14]

- **Polymarket Trading Bot v3.1 multi-strategy framing** (URL 19): "TypeScript-based, automated retail trading bot that actively packages four highly distinct strategies (Arbitrage, DipArb, Smart Money copy, ..." [Source: links 3 5_4.docx URL 19]

- **BTC-15-Minute HF-niche framing** (URL 20): "High-performance, production-grade automated trading bot engineered strictly to exploit Polymarket's highly volatile 15-minute Bitcoin pre[diction markets]." [Source: links 3 5_4.docx URL 20]

- **Smart-money pattern confirmation across batches**: pattern appears in `links 3 5_4.docx` URL 19 (Polymarket Trading Bot v3.1) AND `Polymarket 5_5.docx` URL 17 (polymarket-copy-trading-bot) — two independent Steal-from verdicts strengthen the architectural-pattern signal. [Source: K30 cross-doc analysis]

## Dead Ends

*(none yet — first synthesis. Future updates land here when a specific architectural posture is rejected during Cemini's eventual MM implementation.)*
