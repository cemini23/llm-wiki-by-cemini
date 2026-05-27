---
title: Hyperliquid
type: entity
tags: [platform, crypto, perpetuals, dex, cemini-venue]
keywords: []
related:
  - sources/3-18-crypto-integration-technical-audit.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - sources/cftc-selig-house-ag-testimony-2026-04-16.md
  - concepts/cryptographic-audit-trail.md
  - concepts/ip-sale-readiness.md
  - entities/frameworks/ccxt.md
  - concepts/perps-dex-funding-carry-strategy.md
  - entities/tools/hl-funding-sniper.md
  - sources/trading-posts-compilation-25-2026-05-27.md
maturity: validated
created: 2026-04-23
updated: 2026-05-27
---

## Relations

- @sources/3-18-crypto-integration-technical-audit.md — primary; deep-read 2026-04-26 (K4)
- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md
- @sources/3-19-langgraph-scatter-gather-financial-analysis.md
- @sources/cftc-selig-house-ag-testimony-2026-04-16.md — Rep. Austin Scott (R-GA) pressed Selig on offshore perpetual-futures availability; Selig signaled CFTC plan to expand perp-futures availability to retail (forward-looking commentary, not regulatory action)
- @concepts/cryptographic-audit-trail.md — pg_tamperlog/Merkle leg `[RETRACTED 2026-04-24]` (Track C); see retraction table below for the cleanup
- @concepts/ip-sale-readiness.md
- @entities/frameworks/ccxt.md
- @sources/trading-posts-compilation-25-2026-05-27.md — K72 Post 16 (`hl-funding-sniper`)
- @concepts/perps-dex-funding-carry-strategy.md — funding-carry template
- @entities/tools/hl-funding-sniper.md

## Raw Concept

`[RESOLVED — 2026-04-26 K4 deep-read]` — This page previously asserted *"Cemini integrates via Hyperliquid Agent Wallets… Orders are EIP-712 signed, routed through Flashbots Protect RPC to mitigate MEV, and every on-chain transaction is logged into pg_tamperlog before going to the Merkle-anchored audit ledger… AES-GCM vault for agent-wallet private keys, Web3.py for signing."* That narrative collapsed two distinct things into one false assertion:

1. **The library is real.** `hyperliquid-python-sdk>=0.5.0` is in `/opt/cemini/requirements.txt` (server probe 2026-04-26). The K4 source @sources/3-18-crypto-integration-technical-audit.md prescribes Hyperliquid as the canonical DEX execution venue, and the SDK presence is *consistent with* Phase 1 of that audit having been started.
2. **The full architecture wrapping it is not.** Server-side probe returned: zero `Web3.py` references in any `requirements.txt`; zero `flashbots` / `MEV` references in any service code; zero `AESGCM` / `aes_gcm` / `secrets.enc` references anywhere. The pg_tamperlog / Merkle audit ledger leg is itself `[RETRACTED 2026-04-24]` per @concepts/cryptographic-audit-trail.md (Track C). **The Agent-Wallet-via-Web3.py + Flashbots Protect + AES-GCM-vault flow as described is not the deployed pattern — it's the prescribed build spec.**

The page is reframed as the **venue reference + Cemini-prescribed integration spec**, not as documentation of a deployed pipeline. See @sources/3-18-crypto-integration-technical-audit.md "Prescribed-vs-deployed gap (2026-04-26 K4 deep-read)" for the full evidence trail.

## Narrative

### What Hyperliquid actually is
Hyperliquid is a high-performance on-chain perpetuals DEX with sub-second block times and a fully on-chain orderbook. Two execution interfaces matter for a programmatic strategy:

- **Native Hyperliquid Python SDK** (`hyperliquid-python-sdk`) — covers order placement, cancellation, position queries, and the WebSocket fill/orderbook stream. Signs orders with EIP-712 by default (an SDK-internal call, not a Web3.py call).
- **Agent Wallets** — a Hyperliquid-native delegated-signing pattern: the master wallet authorizes a derived "agent" key (cannot withdraw, can only sign trades). This is a *configuration choice on top of* the SDK, not an SDK default. The SDK will happily sign with a raw private key in a `.env` file too — Agent Wallet usage requires (a) creating the agent on-chain via the master wallet's signature, then (b) loading the agent key into the bot. **(b) is the part that the K4 audit prescribes via AES-GCM vault; absent that vault, an Agent Wallet workflow can still exist but with a plaintext private key in `.env`, which negates the custody-isolation argument.**

### Deployed integration (what's actually on the server, 2026-04-26)
- `hyperliquid-python-sdk>=0.5.0` in `/opt/cemini/requirements.txt` — the SDK is importable. No Cemini service container is named `hyperliquid_*` (the integration sits inside `ems_executor`-class services, not as its own container).
- Multi-venue execution layer (`ems_executor`) is running and CCXT (`ccxt>=4.2.80` + `ccxt_normalizer` container) handles the centralized-exchange leg.
- **Custody mechanism for the Hyperliquid keypair is undetermined from the outside** — could be plaintext `.env` private key, could be Agent-Wallet-with-plaintext-key, could be something not visible to the ssh probe. What is *not* present: AES-GCM vault, Web3.py-mediated tx signing, Flashbots Protect routing.

### Prescribed Cemini deployment (build spec — NOT shipped)
Per @sources/3-18-crypto-integration-technical-audit.md (Phase 1 + Gap 2 + Gap 4):

- **AES-GCM encrypted local vault** holding agent-wallet private keys. Decryption password injected manually via SSH at container startup; password destroyed from memory immediately after key load. (Para 35.) Server probe: zero AES-GCM evidence. Phase 1 Step 1 ("Eradicate all plaintext .env private keys across the 18 Docker containers" — para 217) is unstarted.
- **Hyperliquid Agent Wallet flow**: master wallet authorizes a delegated signing key on-chain; the bot loads only the agent key (mathematically cannot withdraw funds). (Para 35 cont., para 150-156.) The on-chain authorization step requires Web3.py for the EVM-side transaction; Web3.py is absent from server deps.
- **Flashbots Protect RPC** routing for any EVM-side transaction (e.g., the agent-wallet authorization, deposits/withdrawals on the master). Bypasses the public mempool; eliminates the sandwich-attack vector. (Para 89.) Server probe: zero Flashbots references in any service code.
- **CCXT-Hyperliquid double-sign** *(this was a wiki fabrication on the previous version of @entities/frameworks/ccxt.md; the K4 source does not prescribe double-signing — it prescribes CCXT for CEX legs and the Hyperliquid native SDK for the DEX leg, distinct order paths)*. Cleaned up in the same K4 commit.
- **Tamper-evident audit ledger** for on-chain transactions — the version of this page that referenced "pg_tamperlog → Merkle-anchored ledger" predated the @concepts/cryptographic-audit-trail.md Track C retraction (2026-04-24). The audit-trail blueprint exists in concept; the implementation is unbuilt and the specific pg_tamperlog/Merkle naming was synthesis error. Source's actual position on tamper-evidence is "msgpack serialization for deterministic order signing" (para 169-180), not Merkle-anchored chains.

### Why this matters for IP sale
Hyperliquid integration is on the **deal-killer ledger** at @concepts/ip-sale-readiness.md from two angles:

1. **Custody-isolation angle**: a buyer's compliance audit will look for *provable* signing-key isolation — the AES-GCM vault + Agent Wallet pattern is the defensibility argument. A plaintext `.env` Hyperliquid key materially harms valuation.
2. **MEV-protection angle**: institutional buyers expect Flashbots-Protect-style private routing for any DEX-touching strategy; absence is a remediation item rather than a deal-killer, but it lengthens diligence cycles.

Both items map to Phase 1 work in the K4 source — zero-cost foundation work that the audit explicitly prescribes as the prerequisite to scaling crypto exposure.

### What the previous narrative got wrong (and why)
The pre-K4 page collapsed prescription into description on four claims:

| Pre-K4 claim | Server reality / source reality |
|---|---|
| "Orders are EIP-712 signed [via Web3.py], routed through Flashbots Protect RPC" | EIP-712 signing happens inside the Hyperliquid SDK (not Web3.py); Web3.py absent from server deps; Flashbots absent from server code. **Both are prescribed but unbuilt.** |
| "every on-chain transaction is logged into pg_tamperlog before going to the Merkle-anchored audit ledger" | The pg_tamperlog / Merkle leg is `[RETRACTED 2026-04-24]` per @concepts/cryptographic-audit-trail.md Track C. The K4 source itself never names "pg_tamperlog" — that was wiki synthesis on top of an audit-trail blueprint that no longer holds. |
| "AES-GCM vault for agent-wallet private keys, Web3.py for signing" | Both prescribed in the audit (para 35); neither deployed (zero AES-GCM / Web3.py refs on server). |
| "Cemini integrates via Hyperliquid Agent Wallets" | SDK is installed; Agent Wallet usage is a *configuration choice* requiring on-chain authorization via Web3.py — which is absent. The actual Hyperliquid signing-key handling on the server is undetermined from the outside but cannot match the prescribed flow. |

This is the same prescribed-vs-deployed collapse pattern documented in @entities/data-sources/telethon.md (the K3 reframe), @concepts/scatter-gather-topology.md (the K reframe), and @entities/infrastructure/deepseek-r1-14b.md (the local-LLM retraction). Cause: bootstrap-time synthesis read Cemini-internal architectural audits as as-built descriptions because the documents adopt confident "the system uses" / "the platform integrates via" prose. Fix: ground every Cemini-deployment claim against a server probe before promoting from `draft` → `validated`. K4 differs from K3 in being a **partially-deployed** scenario (the SDK *is* in `requirements.txt`) rather than fully blueprint-only — but partial library presence does not imply the full architecture is wired up.

## Snippets

> Furthermore, when interacting with decentralized exchanges like Hyperliquid, the system must utilize "Agent Wallets," which are delegated signing keys authorized by the main wallet to execute trades but mathematically restricted from withdrawing funds.
>
> *— @sources/3-18-crypto-integration-technical-audit.md para 35. Agent Wallets are the right pattern for Hyperliquid; without the AES-GCM vault and without Web3.py for the on-chain authorization tx, however, the Agent Wallet flow as described isn't currently the implemented pattern. The Hyperliquid SDK alone can sign with a raw private key — Agent Wallet usage is a configuration choice, not an SDK-default.*

> By routing Web3.py transactions through Flashbots, the bundle is submitted directly to block builders, preventing public mempool visibility and eliminating sandwich attack vectors. Running a dedicated RPC node locally requires terabytes of storage and constant maintenance, which violates the solo developer constraint. Therefore, leveraging established third-party node providers combined with private routing endpoints is mandatory for on-chain execution.
>
> *— @sources/3-18-crypto-integration-technical-audit.md para 89. The Flashbots prescription. Web3.py absent from server deps; Flashbots refs absent from all service code. **Both legs of this prescription are unbuilt.***

> Eradicate all plaintext .env private keys across the 18 Docker containers. Build the Python decryption pipeline to load secrets into memory purely at runtime, destroying the master password immediately after instantiation. Cost: $0. Prerequisite: None.
>
> *— @sources/3-18-crypto-integration-technical-audit.md para 217 (Phase 1 Step 1). The first concrete action item that would close the custody-isolation gap on Hyperliquid keys. Container count is now 40, not 18 — the source is six-plus weeks stale on the deployment-state baseline. Step is unstarted.*
