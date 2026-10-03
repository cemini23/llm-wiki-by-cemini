---
title: "Wu Blockchain — Weekly Project Updates: zkAPI, Base Cobalt (2026-10-03)"
type: source
tags: [source, k280, crypto, infra, no-level]
keywords: [k280, zkapi, base-cobalt, usdt-bitcoin, no-level]
related:
  - concepts/k280-ood-stub-wave.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
read_status: skimmed
---

## Relations

- @concepts/k280-ood-stub-wave.md

## Raw Concept

| File | `substack-rss-wublock-2026-10-03-weekly-project-updates-ethereum-launches-zkapi-b.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-wublock-2026-10-03-weekly-project-updates-ethereum-launches-zkapi-b.md` |
| Archive | egress-fi 2026-10-03 |
| URL | https://wublock.substack.com/p/weekly-project-updates-ethereum-launches |
| Retrieved | 2026-10-03 |
| Dual-ID | **OSINT K280** |
| sha256 | see the archive record |

## Ingest note — late arrival

This file landed in the inbox **after** the K280 preingest run. The archive sweep then moved it to egress before it had a source page. Written now so the record is complete. **Watch for this: a file that arrives mid-session gets swept by the archive loop even if it was never ingested.** The K280 log entry says "one eval docx"; this is the second file.

## Narrative

A crypto project-update weekly. Headlines only.

**zkAPI (Ethereum Foundation and Open Anonymity).** Uses zero-knowledge proofs to decouple API usage from payment identity, live on mainnet. A user deposits into an on-chain vault, then proves payment for a single request or a whole session. Service providers verify payment without learning the payer. Supports short-lived rate-limited API keys for compatible endpoints, with settlement on actual usage.

The one line worth keeping: **it decouples payment from usage but not from IP address, request timestamps, or prompt content.** That is an honest limit stated in the source, and it is the part a privacy claim usually omits.

**Base Cobalt upgrade.** Third mainnet upgrade. Adds Validity Transactions (pre-submitted time-bound transactions that execute on a condition), composite policies that combine rules with AND/OR logic, and a balance-reassignment function for asset seizure with an on-chain memo. Base states an intent to cut block time from 2 seconds to 200 milliseconds.

**USDT on Bitcoin.** A Tether-backed issuer plans to issue USDT on Bitcoin this month under a commercial licence, built on the RGB protocol and the UTXO model with most data off-chain. Three use cases named: private transfers, direct BTC-to-USDT swaps, and BTC-collateralised lending without wrapping.

**Governance and politics.** Aave Labs proposed a Cayman Islands foundation to hold protocol trademarks and IP, with governance powers staying with the DAO. A Trump meme-coin holder dinner is scheduled for 22 November for the top 185 holders; the token is reported down roughly 95% from its high. Democratic lawmakers signalled further scrutiny of the family's crypto businesses after the midterms.

No price level to arm. FILE only. **No pm scp. Never auto-arm.**
