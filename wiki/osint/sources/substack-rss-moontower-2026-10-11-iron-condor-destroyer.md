---
title: "Moontower — Iron Condor Destroyer: the Verticals workflow (2026-10-11)"
type: source
tags: [source, k289, options, xsp, volatility, screener]
keywords: [moontower, verticals, iron-condor, z-score, standard-deviation, strike-selection, fair-value, liquidity]
related:
  - concepts/k289-feeds-wave.md
  - concepts/xsp-vol-regime-gates.md
  - sources/substack-rss-moontower-2026-10-11-moontower-331.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
read_status: read
---

## Relations

- @concepts/k289-feeds-wave.md
- @concepts/xsp-vol-regime-gates.md

## Raw Concept

| Title | Iron Condor Destroyer |
| Source | Moontower Meta (Substack) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-moontower-2026-10-11-iron-condor-destroyer.md` |
| Retrieved | 2026-10-11 |
| URL | https://moontowermeta.com/iron-condor-destroyer/ |
| Tier | free (RSS) |
| read-status | read |

## Narrative

Moontower shipped a **Verticals** workflow: scan across tickers for the **cheapest vertical that pays in full if the stock reaches a target move**.

### The core idea

Do **not** screen on a raw percentage. **10% means different things in SPY vs TSLA.** Instead, normalise with **standard deviations computed from the name's own surface**. Pick a move — say **+1 SD by a chosen expiry** — and ask the same question of every name.

### Two knobs, one rule

- **An expiry.** Every row is the same maturity, so names compare like with like.
- **A signed move.** ±0.5, ±1, or ±1.5 SD. Positive = call spreads; negative = put spreads.

Target strike for a z-SD move: **K_z**. Strike selection keeps the whole spread **inside** the target so a stock landing exactly on the breakpoint collects the full strike width:

- **Calls:** short strike = the closest listed strike **at or below** K_z; long strike = the next one **down**.
- **Puts:** short strike = the closest listed strike **at or above** K_z; long strike = the next one **up**.

### The marking point worth stealing

**Mid is too noisy** when each leg is 40 cents wide and the spread is worth 30. The app shows a **Moontower fair value inside the bid-ask**, not mid. That is the same "the mid lies on wide markets" lesson the wiki tracks.

### Trust columns (the discipline)

The grid gives **Payout** first (a 1-point spread at $0.20 pays 4-to-1), then several columns to judge the mark: **spread bid/ask** · **market width** (both legs' widths) · **market width / strike width** (a 20-cent market on a $1 vertical is hard to fill near fair) · **leg width / vol** (puts a 20-cent market on a $400 stock and a $30 stock on the same footing) · **mid vs Price** (agreement = the model trusts it) · **liquidity tier**. Names with markets too wide to mark are **excluded**, and counted.

**The honest leaderboard:** *tight markets only* — market/strike width < 20%, liquidity high, sorted by payout.

### Why it matters here

A **vol-normalised comparison method** for the xsp/options lane, plus a reusable rule — **normalise by the name's own volatility before comparing payoffs.** **No trade, no scp.**

## Snippets

> "You don't want to screen across names for the best bang-for-your-buck on a 10% rally because 10% means something very different in SPY vs MU or TSLA." [Source: substack-rss-moontower-2026-10-11-iron-condor-destroyer.md]

> "A 1-point spread priced at $0.20 pays 4 to 1 if the stock gets to the target." [Source: substack-rss-moontower-2026-10-11-iron-condor-destroyer.md]
