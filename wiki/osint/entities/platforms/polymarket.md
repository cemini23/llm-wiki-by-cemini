---
title: Polymarket
type: entity
tags: [platform, prediction-markets, on-chain, cemini-venue-adjacent]
keywords: []
related:
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-9-pm-research.md
  - sources/kalshi-3-3-29.md
  - sources/kalshi-4-3-29.md
  - sources/osint-prediction-markets-trading-architecture.md
  - sources/cftc-anprm-prediction-markets-2026-03-16.md
  - sources/cftc-selig-house-ag-testimony-2026-04-16.md
  - concepts/favorite-longshot-bias.md
  - concepts/publishers-exclusion-apa.md
  - concepts/dcm-state-preemption.md
  - entities/platforms/kalshi.md
  - sources/polymarket-informed-minority-gomezcram-2026.md
  - sources/polymarket-predictions-mcp.md
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - sources/last30days-skill-mvanhorn.md
  - sources/links-3-5-4-tool-eval.md
  - sources/polymarket-5-5-tool-eval.md
  - sources/5-5-links-2-tool-eval.md
  - entities/tools/polymarket-agents.md
  - entities/tools/polymarket-python-order-utils.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/prediction-market-historical-analysis.md
maturity: validated
created: 2026-04-23
updated: 2026-04-30
---

## Relations

- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-9-pm-research.md
- @sources/kalshi-3-3-29.md
- @sources/kalshi-4-3-29.md
- @sources/osint-prediction-markets-trading-architecture.md
- @sources/cftc-anprm-prediction-markets-2026-03-16.md — March 12 2026 ANPRM Question 19 will define "gaming" under CEA §5c(c)(5)(C); outcome shapes whether sports-event contracts (Polymarket included) survive at federal level
- @sources/cftc-selig-house-ag-testimony-2026-04-16.md — Polymarket-Trump-family proximity (Trump Jr. advisor + investor; Truth Social launching competing Truth Predict) raised by Rep. McGovern (D-MA) during testimony
- @concepts/favorite-longshot-bias.md
- @concepts/publishers-exclusion-apa.md
- @concepts/dcm-state-preemption.md — federal-vs-state preemption fight extends beyond Kalshi; Polymarket's on-chain non-DCM status is structurally weaker than Kalshi's
- @entities/platforms/kalshi.md
- @sources/gemini-dr-wave5b-osint-2026-04-30.md — Wave 5B canonical brief; 7 of 18 evaluated URLs target Polymarket directly (Polymarket cluster). Surfaces caiovicentino's full-trade MCP, sibling poly_data Reject (license-metadata discrepancy), BridgeWard arbitrage Steal-from, poly-maker market-making Steal-from, Polymarket-BTC-15-Min-Bot Steal-from. Polymarket's deployment-stack toolchain is now meaningfully more complete than 30 days ago
- @sources/caiovicentino-polymarket-mcp-server.md — Wave 5B Adopt; comprehensive 45-tool MCP across 5 categories (markets / trades / portfolio / orders / data). MIT, Python, 395★, 1 contributor (fork-and-pin pattern). Trade-execution leg of the dual-MCP-Polymarket pattern (real-time-odds = kukapay's; trade-execution = this). USDC.e + MetaMask + Polygon network

## Raw Concept

Synthesized from 5 source(s) referencing this entity across the Cemini research corpus. Category: platforms.

## Narrative

Polymarket is an on-chain prediction market running on Polygon, offering
USDC-denominated binary event contracts. For Cemini it primarily serves as
a **cross-venue price reference** — arbitrage and divergence signals
between Kalshi and Polymarket feed the signal-fusion engine — rather than a
primary execution venue, because US retail access is geofenced and because
the institutional buyer archetype targeted by the IP-sale thesis prefers
CFTC-regulated venues.

Documented across the corpus: Polymarket's AMM-adjacent LMSR mechanics
produce tighter spreads on political/macro contracts than Kalshi during
high-volume events; the lack of US retail access means retail-driven
favorite-longshot bias is weaker than on Kalshi, creating a useful
efficiency-gradient signal. Polymarket is explicitly flagged in the
compliance research as a venue Cemini can **reference** (via public
on-chain data) but not **execute on** without restructuring — hence its
status as a read-only data source in the current stack.

## Snippets

*(populate as source stubs are deep-read.)*
