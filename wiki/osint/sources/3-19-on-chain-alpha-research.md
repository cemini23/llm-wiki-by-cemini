---
title: "Algorithmic Trading Architectures: Integrating On-Chain Blockchain Data for Predictive Alpha Generation"
type: source
tags: [docx, rl-marl, llm-agents, options-derivatives, market-microstructure, quant-finance, crypto, cemini-internal, on-chain, hyperliquid, ccxt, net-flows, mvrv, sopr, nvts, tvl, funding-rate, whale-detection, defillama, etherscan]
clusters: [rl-marl, llm-agents, options-derivatives, market-microstructure, quant-finance, crypto, cemini-internal]
related:
  - concepts/rl-marl-research.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- **Original title**: Algorithmic Trading Architectures: Integrating On-Chain Blockchain Data for Predictive Alpha Generation
- **Author(s)**: Cemini internal research (no attributed author)
- **Type**: DOCX (internal research brief)
- **Location**: research for cemini/3_19 On-Chain Alpha Research.docx
- **Length**: ~4597 words, 132 paragraphs
- **Retrieved**: 2026-04-23 (filename date 2026-03-19)
- **Read status**: read-skim
- **Primary cluster**: crypto (partition-assigned `options-derivatives` is misclustered — paper is explicitly about on-chain crypto metrics, see flags)
- **All clusters**: rl-marl, llm-agents, options-derivatives, market-microstructure, quant-finance, crypto, cemini-internal

## Narrative

Cemini internal architecture brief on the on-chain-crypto alpha layer, specifically targeting Hyperliquid perpetual futures (on-chain CLOB DEX) and CCXT spot markets. Aggressively CPU-only, 128GB Hetzner, Polars-first, Redis pub/sub, LangGraph-orchestrated. Sections cover: predictive metrics & feature engineering, API provider comparison, whale detection & entity clustering, funding-rate alpha, TimescaleDB schema optimization, crisis early-warning, liquidation heatmaps, Python abstractions.

**§1 — On-chain metrics with documented predictive power.** Five primary features feeding the 28-feature MAPPO observation space:
- **Net exchange flows** — 7d/30d MA + acceleration (2nd derivative); inflows → selling pressure, outflows → accumulation.
- **MVRV Z-score** (market-value-to-realized-value) — macro tops/bottoms, regime-filter for Kelly/CVaR risk engine.
- **SOPR** (spent output profit ratio) — 1.0 as support in bull regimes, resistance in bear regimes.
- **NVTS** (network-value-to-transactions) — crypto P/E ratio, high Shapley feature importance.
- **TVL momentum** — proxy for DeFi network utility, cross-chain bridge flows precede narrative rotations.

**§1.2 — Implementation**: 15m/1h/4h rolling STDs and EWMAs in Polars lazy-eval; serialized to Redis pub/sub; avoids retaining raw ticks in memory.

**§2 — API provider strategy**: rejects building a proprietary indexer (violates two-week solo-dev threshold + hardware constraints). Tiered ingestion: Hyperliquid native WebSockets for high-freq, CoinGecko+Etherscan async polling for mid-freq, DefiLlama+Dune scheduled daily/hourly for low-freq macro. Redis-backed token-bucket rate limiter (distributed Docker containers mustn't collectively exceed Etherscan 5 req/s).

**§3 — Whale detection and entity clustering** without proprietary labels:
- Threshold: $1M-equivalent transfer or wallet holding fractional-% of supply.
- Distinguish hot wallets from individual whales via **network-theoretic heuristics**: hot wallets have massive in/out-degree + Poisson-distributed 24/7 stream; whales show low degree + bursty episodic transfers.
- **Common Input Ownership Heuristic** (UTXO): inputs to a single tx belong to same entity; connected-components over time merges into a single logical whale.
- Implementation: rejects graph DB — instead, relational edge tables in PostgreSQL + Polars rolling 30-day counterparty count flags addresses with variance above threshold as "infrastructural" vs directional.

**§4 — Hyperliquid funding rates as predictive alpha**: settled hourly (vs 8h centralized), capped at 4%/hr. Funding = clamped interest rate + premium based on impact bid/ask vs spot oracle. Extreme persistent positive funding + flattening price = bullish exhaustion → mean-reversion short signal; persistent negative funding + stable price = bearish exhaustion → mean-reversion long. Integrate funding-rate changes over multi-day windows as explicit RL observation feature.

Remaining sections (not fully extracted in 80-line read): §5 TimescaleDB schema with continuous aggregates + hypertable partitioning on address + tx-timestamp; §6 crisis early-warning heuristics (stablecoin outflows from exchanges, bridge reserves); §7 real-time liquidation heatmaps (aggregate open interest × leverage tier); §8 Python abstractions — CCXT wrapper + FastMCP tool surface.

Relevant to Cemini as the canonical internal spec for the on-chain feature layer — directly actionable, concrete thresholds, concrete libraries, concrete rate-limit math. Honest limits: (a) this is a spec, not an empirical validation — "feature importance" claims are cited to external sources (refs 1-28 inline but bibliography not captured in extraction); (b) the free-tier API thresholds (Etherscan 5 req/s) are 2025-vintage and drift; (c) "$1M-equivalent" whale threshold is asset-class-specific and needs per-asset calibration; (d) whale-vs-hot-wallet classifier relies on heuristics that sophisticated exchanges can defeat with transaction batching; (e) IP-sale framing is present in register but less aggressive than the 3-26-blog-re audits.

## Key findings

- **FLAG: MISCLUSTERED** — home cluster `options-derivatives` is wrong; this is pure on-chain crypto alpha research. Correct home is `crypto`.
- Five primary on-chain features for the 28-dim MAPPO observation: net exchange flows (+ 2nd derivative), MVRV Z-score, SOPR, NVTS, TVL momentum.
- Tiered API ingestion: Hyperliquid WS (high-freq) + CoinGecko/Etherscan async polling (mid) + DefiLlama/Dune scheduled (low), Redis token-bucket rate limiter.
- Reject proprietary indexer; use third-party APIs — free-tier-first, key-upgrade path for IP-sale scale.
- Whale detection: $1M-equivalent tx + fractional-% supply; hot-vs-whale classifier via degree centrality + transaction-stream Poisson vs bursty.
- Common Input Ownership Heuristic + PostgreSQL edge tables + Polars rolling counterparty counts; no graph DB.
- Hyperliquid funding rate (hourly, 4%/hr cap) as mean-reversion/exhaustion signal; "persistent funding + flattening price → exhaustion" pattern codified.
- CPU-only architectural invariant honored throughout; no GPU, no non-Python runtime.
- Polars lazy-eval 15m/1h/4h rolling STD+EWMA to avoid raw-tick memory retention.
- Directly supplies the crypto-specific portion of the 28-feature observation space design.

## Snippets

- **§1.1** — "Net exchange flows, representing the delta between assets transferred into centralized or decentralized exchange wallets and assets withdrawn to self-custody, serve as the primary proxy for immediate market liquidity."
- **§1.1** — "the Spent Output Profit Ratio… in established upward market regimes, a Spent Output Profit Ratio resting at exactly 1.0 acts as a mathematical support level, as market participants hesitate to sell at a loss; in downward regimes, it acts as resistance."
- **§2.2** — "asynchronous polling must be governed by a strict token-bucket rate limiting algorithm implemented via Redis, ensuring that distributed Docker containers do not collectively exceed the five requests per second limit imposed by Etherscan."
- **§3.2** — "Centralized exchange hot wallets interact with thousands of unique retail addresses daily, exhibiting massive in-degree and out-degree centrality within the transaction graph. Individual whales, conversely, typically exhibit exceptionally low degree centrality."
- **§3.2** — "entity clustering and degree centrality approximations must be executed using relational edge tables within PostgreSQL. The Polars engine can query these edge tables, calculate the unique counterparty count for a given address over a rolling thirty-day window, and flag addresses exceeding a predefined variance threshold."
- **§4.1** — "Hyperliquid's funding rate is settled hourly, providing significantly higher granularity and signal frequency than traditional centralized exchanges that typically settle on eight-hour epochs. The rate is capped at four percent per hour."
- **§4.2** — "A persistently high positive funding rate accompanying a flattening or declining price action indicates bullish exhaustion."
