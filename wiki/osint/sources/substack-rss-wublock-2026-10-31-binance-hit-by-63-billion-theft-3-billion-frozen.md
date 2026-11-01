---
title: "Wu Blockchain: Binance $6.3 Billion Theft, $3 Billion Frozen"
type: source
tags: [source, newsletter, binance, exchange-security, asset-freeze]
related: []
maturity: draft
read_status: read
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Binance Hit by $6.3 Billion Theft: $3 Billion Frozen, Engineer's Computer Compromise Identified as Potential Entry Point |
| Source | Wu Blockchain |
| File | `substack-rss-wublock-2026-10-31-binance-hit-by-63-billion-theft-3-billion-frozen.md` |
| Retrieved | 2026-11-01 |
| URL | https://wublock.substack.com/p/binance-hit-by-63-billion-theft-3 |
| Read status | read |

## Narrative

Wu Blockchain reports Binance's preliminary account of a large theft. Every dollar figure below is a claim in this one report. In an announcement at 10:23 p.m. EDT on October 29, Binance estimated the total impact at approximately $6.3 billion. Binance said blockchain partners froze around $3 billion of related assets on-chain. The earlier verified frozen total was $2.54 billion. The estimated total impact is the gross figure before frozen and recovered assets.

Binance said it set aside more than $6.34 billion in company funds to cover the incident. Approximately $5 billion was already held in the corresponding affected tokens. Binance was buying the rest through market and OTC channels. Limited liquidity in some tokens, and the time for OTC settlement, could slow those purchases. These cover funds exclude frozen or protected assets. Approximately $3 billion remains subject to recovery and verification. Binance said it will cover confirmed shortfalls with company resources and later publish proof of reserves.

Deposits remained open. Withdrawals remained suspended while Binance remediated withdrawal services and related addresses. Binance said the relevant outflows stopped after the suspension. Withdrawal services were expected to resume within 45 hours of that statement.

Binance first said a DevOps engineer's laptop may have been compromised. That access may have reached a service container and allowed unauthorized withdrawal transactions. Binance later said investigators found additional intrusion points and called the attack sophisticated. Binance said it found no evidence that wallet private keys had leaked. A valid on-chain signature does not show that a private key leaked. The attacker could have used a signing service without reading the key. How the valid signatures were produced remains unconfirmed. Blockaid, Cobo co-founder Shenyu, and SlowMist founder Cosine are cited on that gap. Shenyu pointed to possible private-key or signing-system issues and said there was no evidence that a smart-contract flaw directly caused the incident. Binance's internal clues do not yet confirm that view.

EIP-7702 explains operations on the address Binance 14 after a malicious authorization took effect. Blockaid said one authorization in a nonce set matched, so the attacker could batch-transfer ETH and tokens and sweep later deposits. Cosine said EIP-7702 was used to simplify batch sweeps and that the mechanism itself was sound. The same delegation leaves abnormal transfers on other chains unexplained. Other hot wallets used ordinary transfers with valid signatures. Bitquery said Binance 14 cleared the EIP-7702 delegation at 8:10 p.m. EDT on October 29. Binance confirmed that authorizations for affected addresses were revoked.

Third parties reported separate response steps. The Arbitrum Security Council moved approximately 74.56 million ARB and 8,425 ETH to an intermediary frozen wallet. ZachXBT valued those assets at approximately $30.5 million. Specter said First Digital blacklisted an attacker address holding approximately 3.4 million FDUSD. Wu Blockchain says no complete breakdown shows whether these sums already sit inside the aggregate freeze, so they should not be added again. Lookonchain said seven tokens — UNI, ENA, PEPE, LINK, AAVE, ONDO, and WLD — were sold for a combined 70,480 ETH, worth approximately $158.25 million at the time. Onchain Lens tracked more than $1 billion in ETH moving to new wallets and said the attacker had begun selling STRK. A mixer claim stayed speculative. LlamaRisk said an implicated address deposited approximately 60 million USDT into Aave and borrowed 19,762 WETH. The position was adequately collateralized at the time of that assessment. Aave froze a combined 292 asset reserves across V3 and V4. New deposits and borrowing stopped. Repayments, withdrawals, and liquidations continued.

For a quant-finance and macro reader, the report is a venue-risk and flow note. Binance plans market and OTC token buys to fill a shortfall. Reported attacker sales already converted listed tokens into ETH. A withdrawal halt, a large on-chain freeze, and an Aave reserve freeze change usable balances, collateral conditions, and the timing of proof of reserves. The full attack path is still open in this report.

## Snippets

> "Binance said it had set aside more than $6.34 billion in company funds to cover the incident. Approximately $5 billion was already held in the corresponding affected tokens, with the remainder being purchased through market and OTC channels." [Source: https://wublock.substack.com/p/binance-hit-by-63-billion-theft-3 (retrieved 2026-11-01)]
