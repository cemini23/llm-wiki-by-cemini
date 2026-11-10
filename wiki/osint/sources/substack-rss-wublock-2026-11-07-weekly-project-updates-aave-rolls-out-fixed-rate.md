---
title: "WuBlockchain Weekly Project Updates — Aave fixed-rate lending, Base Denim upgrade"
type: source
related:
  - concepts/k296-feeds-wave.md
  - entities/tickers/aave.md
  - entities/tickers/eth.md
  - entities/tickers/sol.md
  - concepts/crypto-custody-single-point-of-failure.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Weekly Project Updates: Aave Rolls Out Fixed-Rate Lending, WLFI Plans Token Buyback, Base Deploys Denim Upgrade, etc |
| Author | Wu Blockchain |
| Type | newsletter, RSS |
| Location | `research to be indexed/substack-rss-wublock-2026-11-07-weekly-project-updates-aave-rolls-out-fixed-rate.md` |
| Retrieved | 2026-11-07 |
| File | substack-rss-wublock-2026-11-07-weekly-project-updates-aave-rolls-out-fixed-rate.md |
| Read status | read |

## Narrative

Ten protocol items.

### Aave moves into fixed rate

Aave Labs acquired the team and technology of on-chain lender **Avon**. The deal includes Avon's fixed and floating-rate lending protocols, its on-chain order book, and its domain name. The price is not disclosed. Three Avon staff join Aave Labs: two in engineering, one in business development.

CEO Stani Kulechov said fixed-rate products extend Aave's reach to institutions, fintechs, and retail users. Aave reports network deposits over **$30bn** and active loans over **$12bn**. [Source: substack-rss-wublock-2026-11-07-weekly-project-updates-aave-rolls-out-fixed-rate.md]

That is the fact worth keeping. Aave's lending book is large, and a fixed-rate product changes the interest-rate risk it carries. A floating-rate pool passes rate risk to borrowers and lenders. A fixed-rate book takes duration onto the protocol.

### Ethereum: Glamsterdam compatibility risk

The Ethereum Foundation warned that the Glamsterdam upgrade may break existing contracts. Two EIPs are the cause:

- **EIP-8037 and EIP-8038** change the gas cost of some operations and the gas charging mechanism for state storage.

ChainSecurity found that these changes break execution assumptions in some projects. Core developers postponed the **Hoodi** testnet hard fork. The Foundation published eight categories of affected assumptions and examples on GitHub, and asked contract authors and auditors to review both on-chain contracts and off-chain services. [Source: substack-rss-wublock-2026-11-07-weekly-project-updates-aave-rolls-out-fixed-rate.md]

The pattern: a gas-cost change is a breaking change for any contract with a hard-coded gas assumption.

### Solana: validator delegation rules

The Solana Foundation changed its Validator Delegation Program. New rules:

- Participation is limited to **12 months**.
- Validators with more than **300,000 SOL** of non-SFDP stake must exit.
- The cap is **100** supported validators.
- Base delegation is about **5,000 SOL**, plus a match of **50%** of external stake, capped at **50,000 SOL** total.
- Validators must run their own nodes and keys. White-label services are banned. Third-party hosting is allowed.

[Source: substack-rss-wublock-2026-11-07-weekly-project-updates-aave-rolls-out-fixed-rate.md]

### Base: Denim upgrade

Base completed its fourth standalone upgrade, **Denim**. It retired Flashblocks and now produces a full canonical block every **200 milliseconds**, five per second. It also adds **BaseTime**, millisecond timestamps for contracts, blocks, transactions, and logs.

Denim updates transfer and compliance controls for the **B20** token standard: compliance policy reuse through a NOT operator, transfer-executor limits extended to direct transfers, and a ban on transfers to a token contract's own address. [Source: substack-rss-wublock-2026-11-07-weekly-project-updates-aave-rolls-out-fixed-rate.md]

Applications that relied on Flashblocks must migrate.

### Short items

- **Zcash NU7** activated at block 3,543,405. Target block time falls from 75 s to 25 s. Measured average was about 39 s at 04:59 UTC. The upgrade caps private transactions per block and disables the Sprout pool, leaving about **12,224 ZEC** temporarily unusable with no approved recovery plan.
- **WLFI** plans a token buyback, possibly funded from USD1 reserve fees. The stated goal is to concentrate voting power in long-term holders. No size or schedule.
- **Lido** launched token swaps on Ethereum, Arbitrum, and Base, powered by CoW Swap, with Chainlink price oracles.
- **ZetaChain** will halt L1 block production on December 9 and migrate ZETA 1:1 to Solana as an SPL token.
- **Scroll** will convert from a permissionless L2 to a permissioned privacy-AI network and move SCR to Ethereum. Its on-chain net profit is about **$42.50**, down roughly 92% in a year.
- **Zilliqa** will move from an independent L1 to an Ethereum L2 for regulated institutions.

The last three items share one cause: a general-purpose L1 or L2 cannot cover its own maintenance cost without demand.

## Snippets

> "Aave disclosed that its network deposits exceed 30 billion US dollars and active loans surpass 12 billion US dollars." [Source: substack-rss-wublock-2026-11-07-weekly-project-updates-aave-rolls-out-fixed-rate.md]

> "EIP-8037 and EIP-8038 will adjust the gas costs of certain operations and the gas charging mechanism for state storage, which may break the execution assumptions relied upon by existing contracts." [Source: substack-rss-wublock-2026-11-07-weekly-project-updates-aave-rolls-out-fixed-rate.md]

> "Scroll's on-chain net profit stands at merely around $42.50, representing a roughly 92% drop over the past year." [Source: substack-rss-wublock-2026-11-07-weekly-project-updates-aave-rolls-out-fixed-rate.md]

## Dead Ends

- **Treating the Aave acquisition as a product launch.** The fixed-rate product is announced, not measured. There is no rate, size, or launch date.
- **Assuming a 200 ms block removes latency risk.** Finality and ordering rules still apply. Five blocks per second does not mean five final blocks per second.
