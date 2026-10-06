---
title: "Wu Blockchain — September blockchain technology update: Hegotá, Solana, Liquid exploit (2026-10-06)"
type: source
tags: [source, k283, crypto, ethereum, solana, perps, security]
keywords: [hegota, glamsterdam, focil, eip-8411, eip-8198, solana-alpenglow, simd-0525, hyperliquid-funding-cap, liquid-exploit, memtensor-memoryos]
related:
  - concepts/k283-feeds-wave.md
  - concepts/crypto-derivatives-volume-2026.md
  - concepts/agent-setup-instruction-supply-chain.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
read_status: read
---

## Relations

- @concepts/k283-feeds-wave.md
- @concepts/crypto-derivatives-volume-2026.md
- @concepts/agent-setup-instruction-supply-chain.md

## Raw Concept

| Title | September Blockchain Technology Update: Hegotá Takes Shape, Solana Speeds Up, Liquid Exploited |
| Source | Wu Blockchain (Substack) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-wublock-2026-10-06-september-blockchain-technology-update-hegotá-ta.md` |
| Retrieved | 2026-10-06 |
| URL | https://wublock.substack.com/p/september-blockchain-technology-update-4e0 |
| Tier | free (RSS) |
| read-status | read |

## Narrative

The September engineering roundup. Two threads matter for this wiki: **Hyperliquid funding** and **LLM-era supply-chain attacks**.

### Hyperliquid (quant-relevant)

Hyperliquid plans to cut the **perpetual funding-rate cap from 4%/hour to 0.5%** in its next upgrade, and to expand **HIP-4 Outcome markets** — active Outcomes per deployer 100 → 200, daily deployment cap 500 → 1,000. The minimum Outcome order notional had already been planned to drop from $10 to $1. **This is the most concrete change for the HL funding lane.**

### Ethereum

- **Glamsterdam:** Sepolia activation **October 6**; Hoodi tentative October 27; go/no-go October 8. Focus: ePBS payload availability, BAL preservation, Engine API.
- **Hegotá:** scope narrowed. **FOCIL (EIP-7805)** and **Frame Transactions (EIP-8141)** ranked S-tier "must ship" (15 A-tier, 28 rejected). EF target: **fully post-quantum L1 by December 2029.**
- **EIP-8411** — chunked payload propagation: 1 MiB to half the network from ~5 s to **under 1 s**.
- **EIP-8198 "Quick Slots"** — make slot time a runtime parameter; initial goal 12 s → **10 s**. Aims to narrow arbitrage windows and reduce LVR.
- **EIP-8288 "Recursive STARK Mempool"** — aggregate mempool dependencies, recursive STARK proofs; ~100–300 kB per period.
- Vitalik: cryptography (FHE, obfuscation, iO) is advancing; chains move from "who can send what" to "who can **see** what".

### Solana

- **Alpenglow** consensus activated on Devnet; target finality **12.8 s → ~150 ms** (design target, unvalidated on mainnet).
- **SIMD-0525:** mainnet target slot time cut to **250 ms**; skipped-slot rate stable, but Asia/South-America validator latency rising.
- **Transaction V1** activated mainnet Sept 15: max tx size 1,232 → **4,096 bytes** (3.3×).
- **SIMD-0437:** storage rent 6,960 → 6,333 lamports/byte; target 696 (a 90% cut).

### Other chains

BNB Pasteur/BidBlock V2: ~98% of blocks, **+28% gas** vs V1, gas limit 55M → 70M. Celestia v10 (Fibre) on Mocha-5. Zcash NU7: 25 s blocks, mainnet Nov 5. a16z **Lattice Jolt** zkVM: post-quantum, 2–3× faster, <100 KB proofs. Bitcoin Core v32 RC (no consensus change).

### Security (the part worth a brief)

- **Liquid Network exploit (Sept 6).** Cache-key ambiguity in Elements Rangeproof verification let nodes accept a transaction with unbacked inputs. **~4,000 L-BTC minted**, pegged to BTC; **3,400 BTC returned, ~602 BTC unrecovered.** Fixed in Elements v23.3.4 (length-prefixed serialisation). *Lesson: a validation cache is part of the consensus security boundary.*
- **MemTensor supply-chain compromise.** `MemoryOS` on PyPI (2.0.34) and the npm `memtensor/memos-cloud-openclaw-plugin` (0.1.21/.23/.25) shipped a cross-platform Go binary that runs on import and can leak prompt content. **This is an agent-memory supply-chain attack** — directly relevant to `agent-setup-instruction-supply-chain`.
- **iOS "DarkSword" exploit kit** reused in the wild (WebKit → PAC bypass → sandbox escape → kernel → Keychain/wallet theft).
- **LLM vulnerability discovery:** Niklas Gögge notes LLMs cut the cost of vuln discovery; Project Loupe and others produced **>1,000 reports** on Bitcoin Core, mostly false positives. Proposes fuzzing/property tests over one-off LLM scans.
- **Ethereum Classic** social-engineering: an unreviewed `core-geth v1.13.0` "security update" was promoted to node operators. No fund loss, but chain-selection logic changed.
- **Chrome** CVE-2026-85046 (V8 type confusion) exploited in the wild; fix released.

### Why it matters here

The Hyperliquid funding-cap change is a direct input to the HL funding lane. The MemTensor attack is a fresh agent-memory supply-chain case. Everything else is context. **No xsp scp, no pm scp.**

## Snippets

> "Hyperliquid plans to reduce the perpetual futures funding-rate cap from 4% per hour to 0.5% in its next network upgrade." [Source: substack-rss-wublock-2026-10-06-september-blockchain-technology-update-hegotá-ta.md]

> "The attacker exploited ambiguous encoding in the cache key used for Elements Rangeproof verification … enabling the unbacked issuance of roughly 4,000 L-BTC." [Source: substack-rss-wublock-2026-10-06-september-blockchain-technology-update-hegotá-ta.md]

> "MemoryOS on PyPI and the official memtensor/memos-cloud-openclaw-plugin npm package … were found to contain a cross-platform Go binary that executed when the packages were loaded or imported." [Source: substack-rss-wublock-2026-10-06-september-blockchain-technology-update-hegotá-ta.md]
