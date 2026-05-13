---
title: "Arbitrage Analysis in Polymarket NBA Markets"
type: source
tags: [polymarket, arbitrage, prediction-markets, microstructure, on-chain, nba, sports-markets, combinatorial-arbitrage, cemini-relevant]
keywords: [Polymarket, NBA, arbitrage, combinatorial, moneyline, spread, order book, market microstructure, liquidity, middle jackpot]
related:
  - sources/polymarket-microstructure-anatomy-2604.24366.md
  - concepts/market-microstructure.md
  - concepts/cross-venue-arbitrage-pattern.md
  - entities/platforms/polymarket.md
  - concepts/polymarket-market-making-architectures.md
maturity: validated
read_status: deep-read
created: 2026-05-09
updated: 2026-05-09
---

## Relations

- @sources/polymarket-microstructure-anatomy-2604.24366.md — companion paper in the Polymarket microstructure family; this paper extends the anatomy work to sports/combinatorial arb using the same CTF Exchange data ecosystem
- @concepts/market-microstructure.md — market microstructure corpus-index hub; this source contributes to the microstructure + prediction-markets cluster
- @concepts/cross-venue-arbitrage-pattern.md — Cemini cross-venue arbitrage reference architecture; this paper provides empirical constraints on execution feasibility
- @entities/platforms/polymarket.md — Polymarket venue entity

## Raw Concept

**Title**: Arbitrage Analysis in Polymarket NBA Markets
**Authors**: Guang Cheng*, Jiaxin Yang and Haoxuan Zou
**Affiliation**: University of California, Los Angeles (UCLA)
**Date**: May 5, 2026
**arXiv**: 2605.00864 [q-fin.TR]
**Canonical location**: `cemini-librarian:/opt/cemini-bulk/research/2605.00864_polymarket-nba-arbitrage.pdf`
**Retrieved**: 2026-05-09 via preingest pipeline
**Read status**: deep-read (all 12 pages + appendices)

**Why this matters for Cemini**: Empirical quantification of arbitrage opportunity frequency, duration, and executability in Polymarket NBA markets — directly constrains the viability of any cross-venue or combinatorial arb strategy Cemini might pursue. Complements Dubach 2024.24366 (microstructure anatomy) by extending from microstructure characterization to arbitrage execution modeling.

## Narrative

### Paper Summary

Systematic empirical analysis of algorithmic arbitrage in Polymarket's NBA game markets using high-resolution limit order book snapshots. Two main findings:

1. **Single-market arbitrage is essentially nonexistent.** Across 75 million+ order book snapshots spanning 3,042 markets, only 7 valid exploitable in-game arbitrage episodes were found. Median duration: 3.6 seconds — well below the 3.6–5.5 second polling cadence.

2. **Combinatorial arbitrage (Moneyline + Spread) is more frequent but severely depth-constrained.** 290 active executable episodes found, overwhelmingly concentrated in the final minutes of live play. Median return of 101 basis points per execution is economically meaningful in percentage terms but absolute returns are tiny due to shallow order books.

3. **The "Middle" jackpot is never empirically realized.** The theoretical scenario where both legs of a combinatorial pair win simultaneously (yielding $2.00 on $1.00 risk) never occurred across the entire sample.

### Key Data

- **Dataset**: 75 million limit order book snapshots across 173 NBA games (Feb 4 – Mar 4, 2026)
- **Single-market arb episodes**: 7 total, all in-game, median duration 3.6s
- **Capped profit (single-market)**: $210.19 aggregate, median $11.01 per episode (stripping one outlier blowout)
- **Combinatorial episodes**: 290 total (279 in-game, 11 pre-game)
- **Combinatorial median yield**: 101.01 bps per execution
- **Capped vs uncapped profit gap**: $559.59 capped vs $2,032.75 uncapped — liquidity bottleneck quantified
- **Depth constraint**: 76.9% of combinatorial episodes constrained to ~14.8 shares average executable size
- **Post-game spread**: 7,532.65 bps median (7× wider than in-game), confirming stale liquidity withdrawal

### Methodological Notes

- **Unified State Machine** merges asynchronous Moneyline and Spread data streams via full outer join on UTC timestamps
- **Forward-fill imputation** prevents look-ahead bias when one market updates before its dependent counterpart
- **Trust Ceiling** caps episode duration by game phase (300s in-game, 1800s pre/post-game) to avoid misclassifying exchange outages as arb opportunities
- **Deduplication protocol** prevents double-counting from Long/Short synthetic book symmetry

### Cemini Relevance

- **Cross-venue arb assessment**: If single-market arb is nearly impossible and combinatorial arb is limited to retail scale (~14.8 shares avg), the execution layer for any Cemini arb strategy needs to account for this as a hard constraint.
- **Complements Dubach 2026**: While Dubach provides the microstructure anatomy (spread premia, depth profiles, maker diversity), this paper provides the execution feasibility analysis for the same venue.
- **Live-trading implications**: The 3.6s median episode duration is below the practical execution threshold for any API-based bot. Strategies need to be co-located or use WebSocket for sub-second detection.

### Limitations (from paper)
- 3.6–5.5s polling cadence means episodes entirely within one interval are missed (conservative lower bound)
- Single month, single sport (NBA), single venue — generalizability uncertain
- Spread markets had deeper liquidity vacuums during mispricings than moneylines

## Snippets

- **Episode scarcity**: "Only 7 valid, exploitable in-game arbitrage episodes across 3,042 markets" despite 75M+ snapshots. [Source: 2605.00864 Abstract]
- **Median duration**: "persisting for a median duration of just 3.6 seconds" [Source: 2605.00864 Abstract]
- **Combinatorial frequency**: "290 active episodes overwhelmingly concentrated in the final minutes of live play" [Source: 2605.00864 Abstract]
- **Median yield**: "median return of 101 basis points per execution" — "economically meaningful in percentage terms" [Source: 2605.00864 Abstract]
- **Jackpot never realized**: "The theoretical 'Middle' jackpot is never empirically realized" [Source: 2605.00864 Abstract]
- **Depth bottleneck**: "76.9% of combinatorial opportunities constrained to an average executable size of just 14.8 shares" [Source: 2605.00864 Abstract]
- **Post-game spread**: "median bid-ask spread explodes to 7,532.65 bps post-game, more than seven times wider than during live play" [Source: 2605.00864 Appendix A]
- **Liquidity as binding constraint**: "execution is severely bottlenecked by shallow order book depth" — "structurally bounded by liquidity, confining risk-free extraction to the retail scale" [Source: 2605.00864 Conclusion]

## Dead Ends

*(none yet — initial ingest, first deep-read of this paper)*
