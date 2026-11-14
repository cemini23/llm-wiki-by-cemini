---
title: "Wu Blockchain — weekly project updates: CFTC weighs charges against Kalshi, NYSE on Avalanche"
type: source
related:
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - concepts/prediction-market-regulation-2026.md
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Weekly Project Updates: CFTC Weighs Charges Against Kalshi, NYSE Uses Avalanche for Tokenized Stocks, Zcash Pushes NU8 Major Upgrade |
| Author | Wu Blockchain |
| Type | newsletter, RSS |
| URL | https://wublock.substack.com/p/weekly-project-updates-cftc-weighs |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-wublock-2026-11-14-weekly-project-updates-cftc-weighs-charges-again.md` |
| Retrieved | 2026-11-14 |
| Published | 2026-11-14 |
| Read status | read |

## Narrative

### The CFTC enforcement threat

The CFTC is investigating whether Kalshi failed to complete required notification for dozens of proposed contracts. The agency has warned Kalshi of possible enforcement action.

The mechanism under scrutiny is **self-certification**. An exchange may launch a product the day after it certifies compliance, with no explicit approval. The CFTC warned operators in July against overly broad certification language. Kalshi responds that the issue is procedural, concerns a small number of contracts, and many have not launched.

In parallel, the CFTC is investigating whether **Polymarket** breached the access terms of its 2022 settlement agreement with US users.

A fine is survivable. A rule that forces a 90-day review on every new contract is not, because it removes the speed advantage that self-certification creates. That is the real risk in the item.

### Tokenized securities

- **NYSE and Avalanche**: Ava Labs will supply the core ledger for a tokenized-securities platform built by an NYSE affiliate. It targets round-the-clock trading, clearing and settlement across tokens issued on different chains. Launch needs regulatory approval.
- **Payward (Kraken)** added more than **200** UK and EU tokenized stocks to xStocks, taking the total above **1,500**. Tokens are 1:1 backed by shares at a regulated custodian. UK investors and US persons remain excluded.
- **Securitize and Ethena** launched a **$100m** 24/7 liquidity facility for BlackRock's BUIDL fund. Qualified investors can redeem BUIDL shares for stablecoins such as USDC outside trading hours. It was seeded with $50m, split equally between BUIDL and USDC.

### DeFi and infrastructure

- **Aave V3.8** is live on 15 markets. It uses EIP-1153 transient storage for reentrancy protection on external callbacks, with minimal extra gas.
- **NEAR AI** was breached through a vulnerability in its SGLang inference engine on 8 November. The access is blocked and the flaw is fixed. NEAR mainnet and other ecosystem services were unaffected. NEAR AI Cloud stays suspended until security is confirmed.
- **MegaETH rebranded to MEGA** and will spend **$30m** of reserves on new products, starting with an AI inference marketplace in December. TVL is about **$12m**, down from a peak above **$245m**.
- **Katana** is replacing vKAT staking incentives with avKAT revenue distribution from 17 November. Buybacks will draw on four revenue lines: spot, perpetuals, Vault Bridge and the sequencer. The unstaking cooldown falls from 45 days to 7.
- **Flop Labs** will launch its Flop Network testnet and airdrop on 24 November.

### Zcash

The NU8 proposal targets late January 2027. It would launch the Tachyon privacy pool, raise the maximum block size from 2 MB to 8 MB for about **200** private transactions per second, and add SPHINCS-based post-quantum signature opcodes with ML-KEM encryption. It also sets a cutoff on new deposits to the legacy Sapling pool.

This follows the NU7 activation reported in the 12 November item. Two upgrades in one quarter is a fast schedule for a privacy chain. [NEEDS VERIFICATION 2026-11-14] Neither activation is confirmed against the node release.

### Why it is filed here

The self-certification investigation is the single most consequential regulatory item of the week for a prediction-market operator. It attacks the listing mechanism rather than any one contract.

See @concepts/prediction-market-regulation-2026.md, @entities/platforms/kalshi.md and @entities/platforms/polymarket.md.

## Snippets

> "Under current rules, exchanges may launch trading as early as the next day after certifying to the CFTC that new products comply with regulatory requirements, without explicit approval." [Source: substack-rss-wublock-2026-11-14-weekly-project-updates-cftc-weighs-charges-again.md]

> "A fine would be survivable, but a rule that makes every new contract wait in line would cut into Kalshi's plan to list products quickly." [Source: substack-rss-wublock-2026-11-14-weekly-project-updates-cftc-weighs-charges-again.md]
