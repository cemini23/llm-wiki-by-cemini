---
title: Moontower Meta — collar shopping
type: source
tags: [newsletter, k234, options, xsp, moontower]
keywords: [moontower, collar, risk-reversal, implied-vol, hedge, sndk, zero-cost-collar]
related:
  - concepts/high-iv-collar-shopping.md
  - concepts/options-derivatives.md
  - concepts/xsp-lane-trading-framework.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: read
---

## Relations

- @concepts/high-iv-collar-shopping.md
- @concepts/options-derivatives.md
- @concepts/xsp-lane-trading-framework.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | collar shopping |
| Author | Moontower Meta / Kris Abdelmessih |
| URL | https://moontowermeta.com/collar-shopping/ |
| sha256 | `517094847c5b57ec0eea12c6198653fff97508ba62b0de343433549445ea6d5f` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-moontower-2026-08-12-collar-shopping.md` |
| retrieved | 2026-08-12 |

## Narrative

Dean Curnutt–style screens for attractive equity collars when **high implied vol** makes OTM calls rich relative to OTM puts (risk-neutral / lognormal geometry + forward from rates). Natural holders can finance a higher put strike by overwriting calls — often near zero-cost — improving hedge R:R vs unhedged long stock.

Key framing: risk-neutral no-arbitrage pricing looks "wacky" to real-world underwriters who care about terminal payoff, not replication cost. Deferred rates at multi-year highs + concentrated high-vol winners expand the hedge menu. Mentions beta-adjusting delta-defined strikes (idiosyncratic upside trade-off) and the put-call parity puzzle (collared stock ≡ call spread cost difference).

Route: wiki concept + **xsp** brief for Lane B / concentrated-book hedge shopping vocabulary (not an auto LIVE collar bot). No Atto/GW.

[Source: https://moontowermeta.com/collar-shopping/ (retrieved 2026-08-12)]
