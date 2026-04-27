---
title: Pricing and Hedging for Liquidity Provision in Constant Function Market Making
type: source
tags: [pdf, options-derivatives, market-microstructure, crypto, cfmm, amm, uniswap, impermanent-loss, lvr, carr-madan]
related:
  - concepts/market-microstructure.md
  - concepts/options-derivatives.md
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
clusters:
  - options-derivatives
  - market-microstructure
  - crypto
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub (Q 2026-04-27)
- @concepts/options-derivatives.md — Options & Derivatives corpus-index hub (Q 2026-04-27)
- @entities/components/kelly-cvar-risk-engine.md — risk engine covering options-derivatives and portfolio-strategy concepts

## Raw Concept

- **Original title**: Pricing and Hedging for Liquidity Provision in Constant Function Market Making
- **Author(s)**: Jimmy Risk, Shen-Ning Tung, Tai-Ho Wang
- **Type**: PDF (arXiv:2603.01344v1, q-fin.MF)
- **Location**: research for cemini/crypto 13 4:11.pdf
- **Length**: 36p
- **Retrieved**: 2026-04-23 (download date, not publication)
- **Publication date**: 2026-03-02
- **Read status**: read-skim
- **Primary cluster**: options-derivatives
- **All clusters**: options-derivatives, market-microstructure, crypto

## Narrative

Risk, Tung & Wang reparametrize Constant Function Market Makers (Uniswap v2/v3, Balancer, etc.) from the natural (token reserves) coordinates into a coordinate system defined by price and intrinsic liquidity. The key structural insight: once expressed in (p, L) coordinates, asset reserves and value functions are linear in the liquidity profile L, which makes arbitrage-free pricing, delta hedging, and systematic risk management tractable under a single dimensional convention (√ETH×USDC intrinsic liquidity, consistent across bonding curves).

Applying the Carr-Madan spanning formula, the paper represents Impermanent Loss (IL) as a weighted strip of vanilla European options indexed by strike — this allows an implied-volatility structure to be read off directly from LP positions and compared to exchange-traded IV. A path-dependent analysis of IL is developed using the last-passage time of the price process. Empirical validation uses Uniswap v3 ETH/USDC pools and Deribit options quotes: the fitted IL-implied smile is consistent with the Deribit smile, supporting the framework's utility as a fair-value metric for liquidity provision.

Relevant to Cemini for any CFMM/LP exposure and for cross-venue relative-value trades between Deribit options and on-chain LP positions (IL hedging, delta-neutral LP, Panoptic-style perpetual options). Honest limits: pure mathematical finance paper — empirical section is validation, not a live trading strategy; assumes frictionless hedging and no gas costs; arbitrage costs against informed flow (LVR) are acknowledged via citation but not deeply modeled in the hedging framework.

## Key findings

- Canonical reparametrization of CFMMs into (price, intrinsic liquidity) coordinates — dimensionally consistent √ETH×USDC across Uniswap v2/v3 and Balancer.
- Asset reserves and LP value functions are linear in the liquidity profile — closed-form delta hedges follow directly.
- Impermanent Loss characterized as a Carr-Madan strip of vanilla options → fine-grained implied volatility structure readable from an LP position.
- Path-dependent IL analysis via last-passage time of the price process.
- Empirical: Uniswap v3 ETH/USDC pools + Deribit quotes produce a volatility smile consistent with crypto market dynamics, validating the framework for fair-value pricing of liquidity.
- Unifies constant-product and concentrated-liquidity pricing results under one representation.

## Snippets

- **p.1 (abstract)** — "we characterize Impermanent Loss (IL) as a weighted strip of vanilla options, thereby defining a fine-grained implied volatility structure for liquidity profiles."
- **p.1** — "asset reserves and value functions exhibit a linear dependence on this intrinsic liquidity. This linear structure facilitates a streamlined approach to arbitrage-free pricing, delta hedging, and systematic risk management."
- **p.1** — "Empirical results from Uniswap v3 ETH/USDC pools and Deribit option markets confirm a volatility smile consistent with crypto-asset dynamics, validating the framework's utility in characterizing the risk-neutral fair value of liquidity provision."
- **p.2** — "Fukasawa et al. [FMW23] demonstrate that IL in constant product markets can be perfectly hedged using a weighted variance swap of order 1/2" — related-work anchor for hedging strategies.
