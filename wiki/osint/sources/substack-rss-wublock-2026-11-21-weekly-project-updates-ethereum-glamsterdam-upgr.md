---
title: "Wu Blockchain — weekly project updates: Glamsterdam delayed, Lighter and Kava exploits"
type: source
maturity: draft
related:
  - concepts/crypto-custody-single-point-of-failure.md
  - entities/platforms/hyperliquid.md
  - concepts/prediction-market-regulation-2026.md
updated: 2026-11-22
read_status: read
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Weekly Project Updates: Ethereum Glamsterdam Upgrade Delayed, Solana 2027 Roadmap, First Tokenized Stock On-Chain Dividend |
| Author | Wu Blockchain |
| Type | newsletter, RSS, weekly digest |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-wublock-2026-11-21-weekly-project-updates-ethereum-glamsterdam-upgr.md` |
| Retrieved | 2026-11-22 |
| Published | 2026-11-21 |
| Read status | read |

## Narrative

**Ethereum.** Glamsterdam may slip to April or May 2027 over smart-contract compatibility. Gas-pricing changes could break existing contracts; the Ethereum Foundation and security firms have contacted at least 50 affected entities. Mainnet could activate as early as mid-January 2027 if the specification holds. [Source: substack-rss-wublock-2026-11-21-weekly-project-updates-ethereum-glamsterdam-upgr.md]

**Solana.** Anza's 2027 roadmap doubles compute capacity and cuts compute-unit use for token-account transactions by 80%. It raises accounts per transaction from 64 to 96, adds vector processing for fully on-chain models, and introduces Constellation for transaction ordering.

**CFTC and on-chain venues.** Chair Michael Selig said on-chain platforms such as Hyperliquid must register as an exchange or partner with a registered one to serve US retail, and comply with the same rules. He cited Backpack's FCM, DCM and DCO licences. On prediction markets he said the CFTC will work with the Department of Justice to defend federal authority against state suits. On single-stock perpetuals he said the absence of an expiry does not by itself make the contract a security swap. [Source: substack-rss-wublock-2026-11-21-weekly-project-updates-ethereum-glamsterdam-upgr.md]

**Lighter exploit.** About $10.39m of USDC was drained from two market-maker accounts, with total exposure about $15.48m. The suspected cause was leaked API keys, not a smart-contract flaw: the attacker closed positions, created a zero-fee pool with the victim accounts, took 99.99% of shares, then moved funds in and redeemed them, using the rule that transfers between accounts under the same L1 address need no extra signature. LIT fell more than 17%. Lighter paused withdrawals and pool creation, enabled Guardian mode, returned about $5m, and resumed operations. [Source: substack-rss-wublock-2026-11-21-weekly-project-updates-ethereum-glamsterdam-upgr.md]

**Kava Lend exploit.** The attacker suppressed net supply in the BUSD market to two minimum units and amplified the supply interest index about 243,000 times, then borrowed 55,205,050.60 KAVA in 127 transactions, worth about $3.76m before the attack. KAVA fell more than 41% within 24 hours.

**Tokenised equities.** Securitize paid the first on-chain dividend for tokenised Apple stock, $0.27 per CET unit in USDC. It also acquired River One to move into credit origination and AI credit underwriting.

**Other.** Polkadot approved a strategy shift to consumer apps and a DOT-backed stable token, with about 97% support. NEAR cut maximum annual issuance from 2.5% to 1.6%. PancakeSwap rebranded to Pancake. Sky's Peg Stability Module processed $518m of transactions linked to illicit wallets over five years, including $101.9m tied to North Korean hackers; Sky says the total is under 0.06% of more than $930bn cumulative volume, and on 19 November it handled more than $2bn of USDS-to-USDC swaps at a 1:1 peg. [Source: substack-rss-wublock-2026-11-21-weekly-project-updates-ethereum-glamsterdam-upgr.md]

The two exploits share one lesson: the weak point was signing and key custody, not the protocol. That matches the wiki's custody concept.

## Snippets

> "The protocol and smart contracts were unaffected." [Source: substack-rss-wublock-2026-11-21-weekly-project-updates-ethereum-glamsterdam-upgr.md]
