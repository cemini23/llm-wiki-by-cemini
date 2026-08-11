---
title: "Wu Blockchain — BIP-110 fork stalls after two blocks: Bitcoin 'junk data' debate (2026-08-10)"
type: source
tags: [newsletter, wublock, k231, crypto, bitcoin, governance]
keywords: [BIP-110, UASF, Ordinals, OP_RETURN, Luke Dashjr, Saylor, replay protection]
related:
  - concepts/xsp-lane-trading-framework.md
  - concepts/crypto-asset-taxonomy.md
maturity: draft
created: 2026-08-10
updated: 2026-08-10
read_status: read
---

## Relations

- @concepts/xsp-lane-trading-framework.md — crypto regime awareness
- @concepts/crypto-asset-taxonomy.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | BIP-110 Fork Stalls After Two Blocks: Where Is Bitcoin's "Junk Data" Debate Headed? |
| URL | https://wublock.substack.com/p/bip-110-fork-stalls-after-two-blocks |
| sha256 | `44baca5a84e29746fb75e4f2ef6c87e68971de6fd6b76c231534f74e09b9d713` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-wublock-2026-08-10-bip-110-fork-stalls-after-two-blocks-where-is-bi.md` |
| retrieved | 2026-08-10 |
| read_status | read |

Wiki crypto-governance context only — no prod bot.

## Narrative

**BIP-110 ("Reduced Data Temporary Softfork")** by pseudonymous Dathon Ohm (Luke Dashjr input): ~1-year, seven consensus restrictions (34-byte script limits, OP_RETURN ≤83 bytes, data-push/witness caps at 256 bytes, Taproot limits) to make large contiguous inscriptions (Ordinals) more costly. Not a ban; doesn't address non-bitcoin tokens (policy-layer).

**Timeline:** Bitcoin Core 30.0 (Oct 10, 2025) relaxed default `-datacarriersize` to 100,000 bytes; BIP-110 draft Oct 24, assigned Dec 3; activation client v0.1 Jan 28, 2026 (Bitcoin Knots base); OCEAN first signaling block Mar 1; BIP status → Complete Jun 25; mandatory signaling period began Aug 9, 2026 at block 961,632. During prior difficulty adjustment only 51 blocks signaled (2.53% vs 55% threshold). On Aug 9 the BIP-110 branch produced just two blocks (mined by Roughnecks via OCEAN) before stalling; Roughnecks stopped mining under its name and recommended suspending participation. Saylor: ~99.85% hash power remained on main chain; minority chain's next difficulty adjustment could take ~25 years (personal estimate). No replay protection on the minority chain — Kevin Loaec + Ledger warned same-signed transactions could replay on mainnet.

**Debate:** Supporters (Ohm, Dashjr) — miners earn fees once while every full node downloads/verifies/stores data; data competes with payments. Opponents (Saylor, Adam Back, PlanB) — consensus rules shouldn't restrict a legal use that pays fees; fee market + node policy; "solution more dangerous than the problem." Leonidas' DOG Mode = opposite policy-layer relaxation (tx limit 400k→3.9M WU, dust to 1 sat; no repo yet). Governance spillover: Murch proposed removing Dashjr as BIP editor (process violations); PR open. BIP status PRs (Complete→Deployed→Closed) open but unmerged.

**Verdict:** BIP-110 effectively failed as a network-wide consensus change; next moves return to relay-policy/template layer. **Route:** wiki crypto governance context; xsp awareness only; no prod bot.

## Snippets

> "BIP-110 ultimately looks more like a governance stress test. Nodes can, of course, choose to enforce their own rules, but whether a UASF can change Bitcoin depends on its ability to secure sufficiently broad economic support." [Source: Wu Blockchain 2026-08-10]
