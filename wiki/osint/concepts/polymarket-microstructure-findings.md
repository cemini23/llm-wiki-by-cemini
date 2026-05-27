---
title: Polymarket Microstructure Findings — Key Takeaways for Cemini
type: concept
tags: [polymarket, microstructure, prediction-markets, on-chain, order-book, trade-direction, findings, cemini-relevant]
keywords: [Polymarket microstructure, trade direction inference, longshot premium, depth concentration, maker diversity, wash trading, archive ingestion, depth decay, Kyle lambda, effective spread]
related:
  - sources/polymarket-microstructure-anatomy-2604.24366.md
  - sources/nber-w10504-wolfers-zitzewitz-prediction-markets-2004.md
  - concepts/prediction-markets-efficiency-wolfers-zitzewitz.md
  - entities/platforms/polymarket.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/market-microstructure.md
  - concepts/prediction-market-historical-analysis.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/event-based-prediction-market-ml.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/prediction-market-historical-analysis.md
  - sources/arxiv-coordination-layer-multi-agent-2605-03310.md
  - sources/arxiv-polymarket-fill-side-2605-11640.md
  - sources/polymarket-insider-trading-crackdown-2026-05.md
  - sources/arxiv-foresightflow-ils-polymarket-2605.00493.md
  - sources/arxiv-polymarket-ils-population-scale-2605.00459.md
  - concepts/prediction-market-information-leakage-score.md
  - entities/tools/polymarket-insider-tracker.md
  - concepts/polymarket-lp-bot-phase0-spec.md

maturity: draft
created: 2026-05-09
updated: 2026-05-16
---

## Relations

- @sources/arxiv-polymarket-fill-side-2605-11640.md — fill-side study: whale/HFO/power tiers hold 81.4% of notional across 12.6% of addresses
- @sources/arxiv-coordination-layer-multi-agent-2605-03310.md — uses 100 Polymarket binary markets as a multi-agent-coordination testbed
- @sources/polymarket-insider-trading-crackdown-2026-05.md — May 2026 regulatory backdrop: insider-trading enforcement + volume cooldown
- @sources/polymarket-microstructure-anatomy-2604.24366.md — canonical source; this page distills its findings for Cemini consumption
- @entities/platforms/polymarket.md — Polymarket venue entity
- @concepts/polymarket-market-making-architectures.md — K30 MM synthesis; these findings constrain MM strategy design
- @concepts/market-microstructure.md — corpus index; this page is a Polymarket-specific anchor
- @entities/tools/polymarket-insider-tracker.md — K49 tool: operationalizes "informed money" detection (Fresh Wallets, DBSCAN Sniper Clusters) on Polymarket
- @concepts/prediction-market-historical-analysis.md — historical-data backtest pipeline; replication package feeds Layer 1
- @concepts/cross-venue-arbitrage-pattern.md — cross-venue arb; Polymarket's microstructure determines arb feasibility

## Raw Concept

Distilled from: Dubach (2026), "The Anatomy of a Decentralized Prediction Market," arXiv:2604.24366. 
Full analysis: `@sources/polymarket-microstructure-anatomy-2604.24366.md`.

**Why this matters for Cemini**: Polymarket is our primary cross-venue price reference. Understanding its microstructure tells us what signals we can trust, what data sources we need, and where arbitrage opportunities live.

## Narrative

### The Headline Finding: Public Feed Direction is Unreliable

The single most important result for Cemini: **trade direction inferred from Polymarket's public WebSocket feed is noise-dominated**.

- Feed-inferred sign agreement with on-chain truth: **∼59%** (panel mean 0.615, barely above 50% chance baseline)
- Effective half-spread **changes sign** on 67% of top-100 markets when comparing feed-inferred vs. on-chain direction
- Kyle's λ **changes sign** on 60% of comparable markets
- Both 7-day windows sit at or below the chance band — far short of the ∼80% Lee-Ready accuracy on Nasdaq

**Implication for Cemini**: Any microstructure analysis using the public feed alone (spread decomposition, adverse-selection estimates, realized spread) will produce unreliable results. **We must source trade direction from on-chain OrderFilled events.** The paper's replication package (`polydata.onchain.trades.load_onchain_trades`) performs the off-chain-to-on-chain join.

### What IS Reliable (Without the On-Chain Join)

The eight stylized facts below hold on the full 600-market panel using only the off-chain feed — no direction inference needed:

| # | Finding | Cemini Relevance |
|---|---------|-----------------|
| SF1 | **Longshot spread premium**: 1,300–1,800 bps half-spread below 0.10 probability (vs. ∼400 bps central) | Inventory-risk premium on low-probability contracts; affects position sizing near tails |
| SF2 | **Depth is broadly distributed**: median L1/L10 = 0.137 (near uniform-grid 0.10), not top-of-book concentrated | Order execution algorithms can expect depth beyond top-of-book; different from equity microstructure assumptions |
| SF3 | **No block-clock alignment**: quote timing doesn't cluster on 2s Polygon block boundaries | No systematic timing advantage from block-aware execution |
| SF4 | **Broad maker diversity**: median ∼32 effective makers per market; HHI 0.031 | Resilient liquidity; no single-maker dependency risk. Tail (p90=0.119, ~8 makers) identifies thin markets |
| SF5 | **Category-conditional spreads**: Crypto median −0.039 pp, Sports 0.008 pp, Geopolitics 0.000 pp, Other −0.000 pp | Spread varies by domain; calibrate execution expectations per category |
| SF6 | **Sub-50 ms median ingestion delay** (41.5 ms); p99 multi-second | Collector pipeline lag, not exchange latency; relevant for real-time feed consumers |
| SF7 | **Low self-counterparty wash**: median 1%, max 22.2% | Wash activity exists but is structured differently from unregulated token exchanges (Cong et al. 25–70% is a sanity bound only) |
| SF8 | **Depth decays near resolution**: slope 0.55 on log seconds-to-close | Liquidity thins as markets close; execution costs rise near resolution — time-sensitive order management |

### Structural Constraints on Arbitrage

- Polymarket markets trade on **completely isolated order books** (no native cross-margin or dynamic pricing links between complementary markets)
- This structural isolation creates **transient pricing misalignments** across dependent markets — the mathematical basis for combinatorial arbitrage
- However, **shallow order-book depth structurally caps execution size**: 76.9% of combinatorial opportunities constrained to avg 14.8 shares (per companion paper, `@sources/polymarket-nba-arbitrage-2605.00864.md`)
- The **"Middle" jackpot is never empirically realized** — the theoretical max-arb is structurally unreachable

### Methodological Notes

- **Sample step sensitivity**: Kyle's λ varies by orders of magnitude across {1, 10, 60, 300}s step sizes on noisy markets. Effective spread and Amihud are stable to ∼10–20% at 60s relative to 1s
- **Volume weighting matters**: Effective-spread sign-flip rate rises from 67% to 86% when volume-weighted (largest market alone accounts for 2/3 of top-100 volume and sign-flips)
- **MEV confound**: On-chain record includes MEV bot fills. 60/40 seller/buyer asymmetry could be retail, MEV, or mixed. Separating them requires public-mempool + private-relay capture
- **V1→V2 cutover**: CTF Exchange V2 launched early April 2026; V1 orders rejected after switch. Opens venue-evolution comparison opportunity

### Replication Package

- Repo: https://github.com/philippdubach/polymarket-microstructure
- Zenodo: DOI 10.5281/zenodo.19811426
- Panel artifacts (panel.parquet, panel_trade_measures.parquet, panel_quote/*) included directly
- On-chain scrape pipeline reproducible via `scripts/scrape_onchain_fills.py`
- **Directly usable by Cemini**: the `polydata.onchain.join.aggregate_onchain_df` pipeline can be integrated into our Layer 1 historical-data harvester (per `@concepts/prediction-market-historical-analysis.md`)

## Cemini Action Items

1. ~~**Integrate replication package** into `scripts/` as the Polymarket historical-data harvester (Layer 1 per prediction-market-historical-analysis.md)~~ → **Shipped**: `briefs/2026-05-09_polymarket-onchain-data-pipeline.md` covers full integration plan.
2. **Do NOT use public-feed trade direction** for any microstructure measure — always source from on-chain OrderFilled events
3. **Factor depth decay (SF8) into execution algorithms** — liquidity thins predictably near resolution; time-sensitive orders need earlier placement
4. **Use maker-diversity metric (SF4) as a liquidity-health signal** — markets with HHI > 0.1 (∼8 or fewer makers) warrant caution on execution
5. **Category-aware spread calibration** — don't apply uniform spread assumptions across crypto/sports/geopolitics markets
6. **Track the V1→V2 cutover** — potential research opportunity on venue evolution

## Dead Ends

*(none yet — initial distillation. Future updates if findings are superseded or replication fails.)*