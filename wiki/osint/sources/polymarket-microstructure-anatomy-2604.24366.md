---
title: Polymarket Microstructure Anatomy — Cross-Sectional Evidence from 600 Markets
type: source
tags: [polymarket, microstructure, prediction-markets, on-chain, order-book, limit-order-book, trade-direction, k30, cemini-relevant]
keywords: [Polymarket, microstructure, limit order book, effective spread, Kyle lambda, wash trading, depth decay, longshot premium, trade direction inference, on-chain, WebSocket]
related:
  - entities/platforms/polymarket.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/market-microstructure.md
  - concepts/prediction-market-historical-analysis.md
  - concepts/polymarket-microstructure-findings.md
  - sources/polymarket-nba-arbitrage-2605.00864.md
  - sources/polymarket-informed-minority-gomezcram-2026.md
  - sources/polymarket-predictions-mcp.md
  - sources/polymarket-5-5-tool-eval.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - concepts/cross-venue-arbitrage-pattern.md
maturity: validated
created: 2026-05-09
updated: 2026-05-11
---

## Relations

- @entities/platforms/polymarket.md — Polymarket venue entity; this source is the definitive microstructure reference for Cemini's prediction-market work
- @concepts/polymarket-market-making-architectures.md — K30 MM synthesis; MM design needs this microstructure data as input
- @concepts/market-microstructure.md — corpus index; this is the Polymarket anchor for the microstructure cluster
- @concepts/prediction-market-historical-analysis.md — historical-data backtest pipeline; replication package feeds directly into Layer 1 collection
- @concepts/polymarket-microstructure-findings.md — distilled findings page created from this source
- @sources/polymarket-nba-arbitrage-2605.00864.md — companion paper on Polymarket NBA arbitrage; shares same data ecosystem
- @sources/polymarket-informed-minority-gomezcram-2026.md — early Polymarket microstructure finding (informed minority)
- @sources/polymarket-predictions-mcp.md — MCP access layer
- @sources/polymarket-5-5-tool-eval.md — K30 Polymarket tool evaluation batch
- @sources/caiovicentino-polymarket-mcp-server.md — K30 Adopt; 45-tool MCP server for Polymarket

## Raw Concept

**Source**: Dubach, P. (2026). "The Anatomy of a Decentralized Prediction Market: Microstructure Evidence from the Polymarket Order Book." arXiv:2604.24366 [q-fin.TR]. https://arxiv.org/abs/2604.24366  
**Accessed**: 2026-05-09 via preingest pipeline (b227zvrr9.txt).  
**Why this matters for Cemini**: Definitive cross-sectional microstructure reference for Polymarket — the venue Cemini uses as cross-venue price reference. Trade-direction inference finding (∼59% accuracy) directly constrains what microstructure measures we can trust from the public feed vs. on-chain data.

## Narrative

### Paper Summary

**The Anatomy of a Decentralized Prediction Market: Microstructure Evidence from the Polymarket Order Book**  
Author: Philipp D. Dubach (Zurich, Switzerland)  
Date: April 28, 2026 (arXiv v1)  
JEL: G14, G12, G19, C58, L86  

The paper studies Polymarket's microstructure using a continuous tick-level archive of the public WebSocket order-book feed (30 billion events over 52 days, 2026-02-21 to 2026-04-15) joined to the authoritative on-chain trade record (255 million OrderFilled events on CTF Exchange V1, 28-day overlap window 2026-02-28 to 2026-03-27). Analysis runs on a pre-registered stratified panel of 600 markets.

### Two Main Contributions

1. **Trade-direction inference from the public feed is noise-dominated.** Six standard direction-dependent measures (effective spread, realized spread, Kyle's λ, Amihud, Roll, Abdi-Ranaldo) need an aggressor sign for each trade. The Polymarket public feed's `change_side` field marks which side of the book moved, not which side initiated the trade. Feed-inferred sign agreement with on-chain truth sits at ∼59% volume-weighted (panel mean 0.615, bootstrap 95% CI [0.58, 0.65], IQR [0.53, 0.68]) — barely above the 50% chance baseline. On the comparable top-100 subset, effective half-spread changes sign on 67% of markets in the first 7-day window (50% in a second); Kyle's λ changes sign on 60% (43% in second). Both windows sit at or below the chance band, well short of the ∼80% Lee-Ready accuracy on Nasdaq. **Any Polymarket microstructure result depending on trade direction must source it from on-chain OrderFilled events.**

2. **Eight cross-sectional stylized facts on the 600-market panel** (none require the on-chain join):
   - **SF1 — Longshot spread premium**: Median spread ∼400 bps in [0.4, 0.6] range, climbing to 1,300–1,800 bps below 0.10. Asymmetric: low-probability side wider. An order of magnitude wider than racetrack/parimutuel longshot premia — reads more like liquidity-provision constraint than risk-love.
   - **SF2 — Depth concentration**: L1/L10 ratio median 0.137, close to uniform geometric grid (0.10 benchmark), p10=0.033, p90=0.428. The folk view that prediction-market books are top-of-book concentrated does not hold.
   - **SF3 — Null block-clock alignment**: Quote-update timing does not cluster on Polygon block boundaries to a meaningful degree (median share 0.102 vs. null 0.10).
   - **SF4 — Broad maker-wallet diversity**: Median HHI 0.031 (∼32 effective makers). Right-skewed: p90=0.119 (∼8 makers), max 0.40 (∼3 makers). Liquidity is decentralised on most markets, thin tail of niche markets dominated by 1–3 wallets.
   - **SF5 — Category-conditional effective spread**: Crypto (348), Sports (142), Other (75), Geopolitics (35). Cross-category median dispersion within ±0.04 prob pp; wide within-category IQR for Crypto and Sports (p75−p25≈0.3 pp).
   - **SF6 — Sub-50 ms median archive-ingestion delay**: p50=41.5 ms, p90=166 ms, p99=6,108 ms. Inter-market spread tight (p25–p75: 39–47 ms), suggesting collector-pipeline behavior, not trader latency.
   - **SF7 — Self-counterparty wash**: Median 0.97%, p90=4.5%, p99=10.6%, max 22.2%. Author's direct-detection method (maker==taker or flipped pair within 128 blocks) is an explicit lower bound; Cong et al. [2023] network-classifier range of 25–70% on unregulated token exchanges is a sanity bound, not an apples-to-apples reference.
   - **SF8 — Depth decay near resolution**: Within-category slope of 0.55 on log seconds-to-close (t=3.85, R²=0.22). Bivariate slope 0.818 (R²=0.13). A 0.31 slope (after volume mediation) ≈ ∼6% less mean depth per 10× reduction in seconds-to-close.

### Key Methodological Points

- **Data architecture**: 1,262 hourly Parquet files (623.8 GB), 30,287,264,368 event rows. Off-chain feed keyed on (market_id, token_id); on-chain record keyed on (makerAssetId, takerAssetId). Join via (condition_id, yes_token_id, no_token_id) mapping from CLOB REST.
- **Panel pre-registration**: Selection rule committed before analysis; deterministic build script emits panel parquet with recorded SHA-256 (docs/preregistration_plan3c.md).
- **Reconciliation**: CLOB REST resolves all 385,198 archive market IDs; Gamma metadata API indexes only 34,764 — not the right source for the join.
- **Wash-filter lower bound**: Direct-detection method covers only direct self-match and one-step roundtrip; extended-graph patterns (Cong et al.) require network-classifier extension.
- **MEV confound**: On-chain trade record includes MEV bot fills; 60/40 seller/buyer asymmetry could be retail, MEV, or mixed. Public-mempool capture alone misses private relay traffic (Marlin Relay, Bloxroute, Flashbots-on-Polygon).

### Extensions (from Conclusion)

- CTF Exchange V1→V2 cutover at end of April 2026 enables venue-evolution comparison
- Combined public-mempool + private-relay capture to separate MEV from retail
- Per-market depth time series for within-market depth-decay regression
- Cross-venue analysis vs. Kalshi, PredictIt, or sportsbook mirrors (price-discovery question: leader or follower?)

### Replication Package

- Repository: https://github.com/philippdubach/polymarket-microstructure
- Archived at Zenodo: DOI 10.5281/zenodo.19811426 [Dubach, 2026]
- Full 624-GB WebSocket archive not redistributed (collector configuration provided instead)
- Panel artifacts (panel.parquet, panel_trade_measures.parquet, panel_quote/*) included directly
- On-chain scrape pipeline (scripts/scrape_onchain_fills.py) reproducible against any Polygon RPC with archive-node access
- Code was developed with assistance from Claude Opus 4.7 (disclosed in §9)

## Snippets

- **Aggregate data scale**: "30,287,264,368 events across 385,198 distinct markets… 255,425,405 [on-chain] fills." [Source: 2604.24366, §4]
- **Trade-direction noise**: "Trade direction inferred from Polymarket's public order-book feed agrees with on-chain ground truth only ∼59% of the time (volume-weighted across the top-100 stratum and four disjoint 7-day windows; panel mean 0.615, market-clustered bootstrap 95% CI [0.58, 0.65], IQR [0.53, 0.68])." [Source: 2604.24366, Abstract]
- **Effective spread sign-flips**: "On the comparable subset of the top-100 panel, the effective half-spread changes sign between feed- and on-chain trade directions on 67% of markets in the first 7-day window (50% in a second non-overlapping window)." [Source: 2604.24366, Abstract]
- **Kyle's λ sign-flips**: "Kyle's λ changes sign on 60% (43% in the second window); both windows fail to recover the on-chain sign at anything close to the ∼80% rate that Lee-Ready achieves on equity venues." [Source: 2604.24366, Abstract]
- **Longshot premium**: "Median spread is ∼400 bps in the central [0.4, 0.6] range and climbs to 1,300–1,800 bps for markets trading below 0.10." [Source: 2604.24366, §5.1]
- **Depth profile**: "The folk view that prediction-market books are concentrated at top-of-book does not hold on Polymarket: depth is generally layered deeper into the book." Median L1/L10 ratio 0.137, close to uniform-grid benchmark of 0.10. [Source: 2604.24366, §5.2]
- **Maker diversity**: "Median HHI is 0.031 (∼32 effective makers)… Maker liquidity is decentralised on most markets in the panel." [Source: 2604.24366, §5.4]
- **Archive latency**: "Median per-market p50 delay is 41.5 ms, with p90 = 166 ms and p99 = 6,108 ms." [Source: 2604.24366, §5.6]
- **Wash share**: "Median wash share is 0.97%, with p90 = 4.5%, p99 = 10.6%, and a maximum of 22.2%." [Source: 2604.24366, §5.7]
- **Depth decay**: "Within-category log-log slope of 0.55 on log seconds-to-close (t = 3.85)." [Source: 2604.24366, §5.8]
- **Core constraint**: "Microstructure work on Polymarket therefore needs to source trade direction from on-chain OrderFilled events." [Source: 2604.24366, Abstract]

## Dead Ends

*(none yet — initial ingest. Future updates if replication attempts fail or findings are superseded.)*