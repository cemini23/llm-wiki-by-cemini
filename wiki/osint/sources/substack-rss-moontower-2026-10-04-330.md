---
title: "Moontower #330 — INTC flow, Kelly wrap, Robinhood agentic platform (2026-10-04)"
type: source
tags: [source, k281, options, volatility, agents]
keywords: [k281, intc, moontower, kelly, agentic-trading, claim]
related:
  - sources/substack-rss-moontower-2026-10-04-academic-acceleration.md
  - sources/substack-rss-moontower-2026-10-04-option-ideas.md
  - concepts/k281-vol-quant-wave.md
  - concepts/k281-harness-wave.md
maturity: draft
created: 2026-10-04
updated: 2026-10-04
read_status: skimmed
---

## Relations

- @sources/substack-rss-moontower-2026-10-04-academic-acceleration.md
- @sources/substack-rss-moontower-2026-10-04-option-ideas.md
- @concepts/k281-vol-quant-wave.md
- @concepts/k281-harness-wave.md

## Raw Concept

| File | `substack-rss-moontower-2026-10-04-moontower-330.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-moontower-2026-10-04-moontower-330.md` |
| Archive | egress-fi 2026-10-04 |
| URL | https://moontowermeta.com/moontower-330/ |
| Retrieved | 2026-10-04 |
| Dual-ID | **OSINT K281** |
| Issue | **#330** |
| sha256 | see the archive record |

## Ingest note — this issue is a superset

Issue #330 contains, as sections, the content of **two other captures in this same inbox**:

- `substack-rss-moontower-2026-10-04-2-option-ideas-from-the-robinhood-summit-2026.md`
- `substack-rss-moontower-2026-10-04-academic-acceleration.md`

Both are near-verbatim sections of this issue. **Ingest #330 as the record; the two standalone captures get thin pointer pages.** Do not triplicate the content.

## Narrative

### The named structure — INTC October 16 130 calls

On 28 September there was **notable size buying in INTC October 16 130 calls**, roughly a week before Intel's 23 October earnings.

The author weighs a "sympathy" hypothesis — a buyer using INTC as a semiconductor proxy ahead of Micron's 30 September print — then checks the Micron earnings straddle (priced cheaply against prior years) and INTC implied vol (mid-range absolutely, high cross-sectionally, with rich call skew), and **leans toward fading the buyer.**

The stated fade: **selling INTC straddles, or writing calls against stock you already own.** With one useful caveat quoted: *"You don't have to sell the 130s to fade the 130 buyer"* — the 125s, 135s, and at-the-money options also richen.

**This is a claim for the ledger, not a trade.** No level is armed. See @concepts/k281-vol-quant-wave.md.

### The teaching example

A one-year 110-strike call against owning the stock. The numbers: about 2.2 calls cost **$2,194**, delta-equivalent to 100 shares of a $100 stock at $10,000. Shares win between roughly **$78 and $137**. The gap is widest at $110, where the calls expire worthless and the shares gain $1,000 — a **$3,200** difference. Below $78 the calls lose at most $2,194. Above $110 the calls behave like 217 shares.

The lesson the author draws: a long call beats shares on big up **and** big down moves, and loses on the middle. That is the shape of long volatility, stated as a comparison.

### The agent-tooling signal

The author attended the Robinhood Summit in Houston, ran a trading lab on buying options, and sat as a trader on a panel about **data providers on Robinhood's new agentic trading platform** — described as an app store where a user subscribes to vetted providers' data inside the trading agent.

That is the item for @concepts/k281-harness-wave.md. A brokerage exposing third-party data feeds as subscribable modules inside its own agent is a distribution model for exactly this workspace's kind of output. **No integration. Note the shape.**

### Also in the issue

A Kelly Criterion wrap-up linking a lecture with Matt Zeigler plus slides, and an academic-acceleration section.

No level to arm. FILE only.
