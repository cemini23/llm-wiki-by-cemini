---
title: K281 Vol Quant Wave (Oct 2026)
type: concept
tags: [quant, options, volatility, k281]
keywords: [k281, intc, straddle, claim-ledger, no-trade]
related:
  - concepts/k278-vol-quant-wave.md
  - sources/substack-rss-moontower-2026-10-04-330.md
maturity: draft
created: 2026-10-04
updated: 2026-10-04
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k278-vol-quant-wave.md
- @sources/substack-rss-moontower-2026-10-04-330.md

## Raw Concept

K281 cluster hub. Dual-ID **OSINT K281**. Prior @concepts/k278-vol-quant-wave.md.

## Narrative

One item, and it is a **claim for the ledger, not a trade.**

### The named structure

On 28 September there was **notable size buying in INTC October 16 130 calls**, about a week before Intel's 23 October earnings. The author weighs a sympathy hypothesis against Micron's 30 September print, checks the Micron straddle and INTC implied vol, and **leans toward fading the buyer.**

The stated fade: **selling INTC straddles, or writing calls against stock you already own.** With the caveat that the 125s, 135s, and at-the-money options also richen — you do not have to sell the exact 130s.

**Record it as a claim with a date and a strike. Do not arm it.** This is a third-party flow read, not our signal, and the workspace has no XSP or PM scp.

### The teaching comparison

A one-year 110-strike call against owning 100 shares:

| | Value |
|---|---|
| Cost of ~2.2 calls | **$2,194** |
| Equivalent shares | 100 at $100 = $10,000 |
| Shares win | roughly **$78 to $137** |
| Widest gap | at $110 — calls expire worthless, shares +$1,000, a **$3,200** difference |
| Max call loss | $2,194 |
| Above $110 | calls behave like 217 shares |

The shape: a long call beats shares on big up **and** big down moves, and loses on the middle. That is long volatility stated as a comparison, and it is a clean way to explain a vol position to someone who thinks in share terms.

### Boundary

**No trade. No sizing change. No xsp scp. Never auto-arm.** FILE only.
