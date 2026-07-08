---
title: Moontower Meta — VIX and buy signals
type: source
tags: [source, newsletter-rss, moontower, options, vol, k147]
keywords: [moontower, VIX, buy-the-dip, Sharpe, risk-adjusted, xsp]
related:
  - sources/substack-rss-moontower-2026-07-08-betting-as-a-tax-on-bullshit.md
  - concepts/xsp-lane-trading-framework.md
  - sources/substack-rss-moontower-2026-07-05-moontower-319.md
maturity: draft
created: 2026-07-06
updated: 2026-07-08
read_status: read
---

## Relations

- @concepts/xsp-lane-trading-framework.md — vol regime gates for Lane A/B sizing
- @sources/substack-rss-moontower-2026-07-05-moontower-319.md — newsletter issue wrapper

## Raw Concept

| Field | Value |
|-------|-------|
| **URL** | https://moontowermeta.com/vix-and-buy-signals/ |
| **Feed** | moontower |
| **Published** | 2026-07-05 |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-moontower-2026-07-05-vix-and-buy-signals.md` |

## Narrative

Kris Abdelmessih debunks lazy **"VIX > 30 = buy"** FT framing. Elm Wealth backtest (S&P + VIX 1990–2026): static portfolio Sharpe **0.50** beats buy-on-spike (**0.47**); inverse sizing when VIX high (**0.54**); momentum cut when market falling (**0.59**). Risk scales with variance — doubling VIX quadruples risk; doubling down needs ~8× return bump.

**XSP steal:** Prefer **reduce** long-call exposure on vol spikes; `@ptuomov` rule — add risk when VIX elevated *but trending down* after ~6mo high; target weight ∝ target risk / VIX. Brief: `briefs/xsp-2026-07-06_moontower-vix-regime-steal.md`.

## Snippets

> "A strategy that buys more when VIX > 30% (the popular advice): 0.47 which is slightly worse than the null case." [Source: moontowermeta.com/vix-and-buy-signals — Elm Wealth cite]

> "The correct time to take more equity risk is when VIX has been high for six months but has been trending down." [Source: same — @ptuomov on X]
