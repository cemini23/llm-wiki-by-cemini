---
title: Crypto Asset Taxonomy — Functional Categories Across the Cemini Crypto-Native Watchlist
type: concept
tags: [concept, crypto_native, taxonomy, blockchain-l1, oracle-networks, store-of-value, smart-contracts, watchlist-organization]
keywords: [taxonomy, layer-1, smart-contract platform, store of value, oracle, middleware, proof-of-work, proof-of-stake, EVM, EUTXO]
related:
  - entities/ticker-watchlist.md
  - entities/tickers/btc.md
  - entities/tickers/eth.md
  - entities/tickers/sol.md
  - entities/tickers/doge.md
  - entities/tickers/ada.md
  - entities/tickers/avax.md
  - entities/tickers/link.md
  - entities/data-sources/coingecko.md
  - concepts/oracle-networks.md
  - sources/agent-3-4-4.md
  - sources/agent-4-4-4.md
  - sources/agent-5-4-4.md
  - sources/stocks-1-4-5.md
  - sources/dune-analytics-mcp.md
maturity: validated
created: 2026-04-25
updated: 2026-05-02
---

## Relations

- @entities/ticker-watchlist.md — parent watchlist this taxonomy organizes
- @entities/tickers/btc.md, @entities/tickers/eth.md, @entities/tickers/sol.md, @entities/tickers/doge.md, @entities/tickers/ada.md, @entities/tickers/avax.md, @entities/tickers/link.md — the 7 crypto-native tickers being categorized
- @entities/data-sources/coingecko.md — canonical reference-data source for the market-cap / FDV / dev-activity / circulating-supply facts that anchor each of the 4 functional categories on a per-ticker basis
- @concepts/oracle-networks.md — sister concept, deeper treatment of the middleware category (LINK)

## Raw Concept

The Cemini watchlist contains 7 crypto-native assets categorized under a single label (`category: crypto_native`). At the protocol layer they are heterogeneous — BTC and LINK barely look like the same kind of thing. This page provides a functional taxonomy to make cross-ticker queries tractable: "which assets are smart-contract platforms?" "which serve as middleware?" "which are non-programmable settlement layers?"

Synthesized from the seven Gemini Deep Research ticker reports themselves; this page makes no first-order factual claims that aren't anchored to those reports. Where specific protocol-internal terminology (consensus algorithm names, execution-engine names) is cited without verbatim source-page anchoring, claims are tagged `[NEEDS VERIFICATION YYYY-MM-DD]`.

## Narrative

### The four functional categories

The seven crypto-native assets in the watchlist resolve cleanly into four functional categories, defined by what role they play in the broader decentralized-systems stack rather than by surface attributes (price, market cap, age).

#### 1. Store-of-value blockchains — BTC

Bitcoin is "decentralized digital currency and a secure ledger of unspent transaction outputs" — explicitly NOT a smart-contract platform [Source: @entities/tickers/btc.md, Section 1 Protocol Overview]. The Bitcoin Script language is intentionally non-Turing-complete, prioritizing predictability and security over programmability [CONFIRMED] [Source: @entities/tickers/btc.md — "The lack of a Turing-complete base layer intentionally restricted decentralized application (dApp) development"]. Use case = monetary scarcity, settlement of large transfers, sovereign-grade store-of-value.

**Watchlist ticker**: BTC.

#### 2. Programmable Layer-1 smart-contract platforms — ETH, SOL, ADA, AVAX

These four are general-purpose decentralized computers — they execute arbitrary state-transition functions, host smart contracts, and support DeFi/NFTs/DAOs/etc. They differ along three architectural axes: consensus, execution model, and the modular-vs-monolithic posture of the protocol itself.

| Asset | Consensus | Execution model | Architectural posture |
|---|---|---|---|
| **ETH** | PoS (post-Merge) | EVM (Ethereum Virtual Machine), Solidity, account-based | Modular — rollup-centric: L1 = settlement / data availability / coordination, L2s do execution [Source: @entities/tickers/eth.md, Section 1 Protocol Overview] |
| **SOL** | PoH + PoS hybrid [CONFIRMED] [Source: @entities/tickers/sol.md — "Proof of History (PoH), a mechanism that operates in tandem with a Delegated Proof of Stake (dPoS) consensus model"] | Parallel-execution, single state machine, synchronous on-chain interaction | Monolithic — execution + consensus on L1, no L2 reliance [Source: @entities/tickers/sol.md, Section 1 Protocol Overview] |
| **ADA** | PoS (Ouroboros family) [CONFIRMED] [Source: @entities/tickers/ada.md — "Ouroboros, the blockchain industry's first provably secure, peer-reviewed proof-of-stake consensus algorithm"] | EUTXO (Extended Unspent Transaction Output) accounting model, smart contracts on a Computation Layer separate from the Settlement Layer | Bifurcated — Cardano Settlement Layer (CSL) + Cardano Computation Layer (CCL) as distinct concerns [Source: @entities/tickers/ada.md, Section 1 Protocol Overview] |
| **AVAX** | PoS (Snow consensus family) [CONFIRMED] [Source: @entities/tickers/avax.md — "anchored by the 'Snow' family of consensus algorithms"] | Multi-chain (P-chain platform / X-chain exchange / C-chain EVM-compatible) plus app-specific subnets [CONFIRMED] [Source: @entities/tickers/avax.md — "the architecture pioneers the concept of 'Avalanche L1s' (formerly designated as Subnets)"] | Heterogeneous L1 — single base protocol with subnets for app-specific chains [Source: @entities/tickers/avax.md, Section 1 Protocol Overview] |

The architectural divide between **modular (ETH)** and **monolithic (SOL)** — abstracting execution to L2s vs. keeping it on L1 — is the central live debate in this category. ADA and AVAX represent intermediate positions (bifurcated layering and subnet-based heterogeneity respectively).

**Watchlist tickers**: ETH, SOL, ADA, AVAX.

#### 3. Memecoin / payments-focused PoW chains — DOGE

Dogecoin is a Layer-1 PoW chain in the Bitcoin/Litecoin lineage (Litecoin → Luckycoin → DOGE). It is NOT a smart-contract platform [Source: @entities/tickers/doge.md, Section 1 Protocol Overview]. Distinguishing features:

- **Scrypt hashing** with **AuxPoW (merged mining) since 2014** — Litecoin miners secure DOGE simultaneously without expending additional compute, giving DOGE Litecoin-grade security despite no dedicated proprietary hash power [Source: @entities/tickers/doge.md].
- **Use cases**: micro-transactions, tipping, speculative trading [Source: @entities/tickers/doge.md].
- **Cultural / valuation driver**: meme momentum and retail enthusiasm rather than fundamental cash-flow economics — DOGE was "originally conceptualized to satirize the speculative fervor surrounding early digital assets" [Source: @entities/tickers/doge.md].

Architecturally DOGE is closer to BTC than to ETH; functionally its market behavior is closer to a high-beta speculative asset.

**Watchlist ticker**: DOGE.

#### 4. Middleware / oracle networks — LINK

Chainlink is *not a blockchain*. It is a Decentralized Oracle Network (DON) — middleware that bridges deterministic smart contracts on any L1 with off-chain data, computation, and other blockchains [Source: @entities/tickers/link.md, Section 1 Protocol Overview]. The "oracle problem" — how do you get reliable real-world data into a closed deterministic system without compromising consensus — is what Chainlink exists to solve.

LINK as an asset is paid to node operators in exchange for serving oracle requests. Its value accrual is structurally different from L1 tokens (which capture transaction-fee value from native execution).

See @concepts/oracle-networks.md for the deeper treatment.

**Watchlist ticker**: LINK.

### Cross-cutting axes

Independent of the four functional categories, several architectural dimensions cut across the taxonomy:

- **Programmability**: BTC ≈ DOGE (non-programmable / minimally programmable) < ETH ≈ SOL ≈ ADA ≈ AVAX (general-purpose smart contracts). LINK occupies a special position — it is *consumed by* programmable contracts on other chains rather than hosting them itself.
- **Consensus**: PoW (BTC, DOGE) vs. PoS (ETH, ADA, SOL-via-hybrid, AVAX) vs. DON consensus (LINK).
- **Throughput posture**: monolithic-high-throughput (SOL) vs. modular-base-layer-with-L2s (ETH) vs. bifurcated-by-purpose (ADA) vs. subnet-fragmented (AVAX) vs. predictable-low-throughput (BTC, DOGE).
- **Regulatory exposure**: securities-classification ambiguity is highest for tokens with active staking yields and centralized issuance (parts of ADA, AVAX, SOL discourse); BTC has the most jurisprudential clarity (commodity in US per CFTC) [TENTATIVE] — inherent forward-looking regulatory assessment; SEC/CFTC jurisdictional boundaries remain contested.

### Why this taxonomy matters for Cemini

Strategy categories map roughly onto the functional categories:

- **Store-of-value carry / volatility-harvesting**: BTC.
- **Smart-contract-platform momentum / DeFi-yield strategies**: ETH, SOL, ADA, AVAX.
- **High-beta speculative / sentiment-driven**: DOGE.
- **Infrastructure-leverage plays** (oracle outages = systemic-risk events; oracle-fee growth = DeFi-volume proxy): LINK.

For ticker-watchlist organization, this taxonomy lets queries like "which of our crypto holdings are on-chain programmable platforms?" return the right four (ETH/SOL/ADA/AVAX) rather than all seven, and makes "what's our pure infrastructure exposure?" answer with LINK alone.

## Snippets

*Source-quoting belongs in the individual ticker pages; this concept page is purely synthetic. Cross-link to ticker pages for verbatim protocol descriptions.*
