---
title: High-IV collar shopping
type: concept
tags: [concept, options, collar, hedge, xsp, k234]
keywords: [collar, risk-reversal, implied-vol, zero-cost-collar, hedge, moontower]
related:
  - sources/newsletter-moontower-collar-shopping-2026-08-12.md
  - sources/substack-rss-moontower-2026-08-16-324-rssb.md
  - concepts/options-derivatives.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/xsp-vol-regime-gates.md
maturity: draft
created: 2026-08-12
updated: 2026-08-17
---

## Relations

- @sources/newsletter-moontower-collar-shopping-2026-08-12.md
- @sources/substack-rss-moontower-2026-08-16-324-rssb.md — K240 RSSB implied stock-bond corr
- @concepts/options-derivatives.md
- @concepts/xsp-lane-trading-framework.md
- @concepts/xsp-vol-regime-gates.md

## Raw Concept

What this page answers: when elevated IV makes call-overwrites finance attractive put protection (collars / risk reversals), and how that maps to XSP/concentrated-book hedge vocabulary.

## Narrative

**Mechanism:** under risk-neutral / lognormal pricing, higher IV lifts OTM calls faster than OTM puts for a fixed dollar distance from spot; rates that push the forward up reinforce call richness. Natural long-stock holders can sell rich calls to buy puts — often near zero premium — improving downside R:R vs naked long.

**Operator use (not a bot):** screen for names/regimes where collar R:R is attractive (Dean-style tables; sector/beta filters). For XSP / Lane B: treat as **hedge-shopping language** when vol regime is elevated and a book needs financed protection — do not auto-LIVE collar without explicit GO.

Pairs `@concepts/xsp-vol-regime-gates.md` (high-vol regimes) and Moontower source `@sources/newsletter-moontower-collar-shopping-2026-08-12.md`. Prod brief: `briefs/xsp-k234-moontower-collar-shopping.md`.

[Source: Moontower Meta 2026-08-12]
