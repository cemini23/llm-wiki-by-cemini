---
title: Options capital velocity — early close and roll (SMB)
type: concept
tags: [concept, options, put-credit-spread, capital-efficiency, k79]
keywords: [velocity-of-capital, 76-percent-rule, roll-spread, bollinger-band, put-credit-spread, seth-freudberg]
related:
  - entities/organizations/smb-capital.md
  - sources/smb-capital-youtube-week-2026-03-14.md
  - concepts/xsp-put-credit-spread-small-account-smb.md
  - concepts/broken-wing-butterfly-options.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @entities/organizations/smb-capital.md — SMB options desk
- @sources/smb-capital-youtube-week-2026-03-14.md — Seth Freudberg walkthrough (2026-03-17)
- @concepts/xsp-put-credit-spread-small-account-smb.md — sibling put-credit-spread education
- @concepts/broken-wing-butterfly-options.md — SMB index options curriculum

## Raw Concept

What prompted this page: SMB *How to Maximize Options Profits* — Seth Freudberg on **velocity of capital** for put credit spreads (QQQ example, Nov 2025).

## Narrative

Retail options traders often **hold credit spreads to expiry** and leave P&amp;L on the table. SMB teaches **close early + re-establish** when a large fraction of max profit is already captured.

### Mechanics [TENTATIVE]

1. **Entry example:** QQQ at lower Bollinger Band → bullish put credit spread (sell ATM put, buy put 5 strikes lower), ~13 DTE.
2. **Mid-trade:** After rally, spread captures **≥76% of max profit** (max profit = initial credit received) in **4 days** vs 9 days remaining.
3. **Action:** Close spread (reverse legs) → immediately open **new spread at current price**, same expiry — strikes moved up with underlying.
4. **Outcome:** First leg locks ~76% of $1,910; second leg collects fresh premium ($1,680) on recycled capital → combined profit **exceeds** hold-to-expiry on original spread alone.

**Velocity of capital** = redeploying the same buying power multiple times within one thesis window instead of waiting for time decay on a stale strike ladder.

### Rules of thumb

- Credit spread max profit is capped at **initial cash collected** (both legs expire worthless).
- When unrealized profit is a **substantial portion** of that cap mid-trade, closing + rolling is usually superior to passive hold [TENTATIVE — single worked example].
- Entry timing still matters (Bollinger / regime); this video focuses on **exit and recycle**.

### Cemini relevance

- Options sleeve **exit policy** candidate — needs backtest on SPX/XSP/QQQ credit spreads before prod [NEEDS VERIFICATION 2026-05-29].
- Pairs with @concepts/xsp-put-credit-spread-small-account-smb.md (entry) — this page is **exit/recycle**.

## Snippets

> "This concept is called the velocity of capital, and it's very useful to greatly improve your returns as an options trader." [Source: SMB Capital YouTube TpAPTwLMb44, 2026-03-17]

> "Closing trades early when they've attained a substantial portion of their maximum profit… then reestablish a new one." [Source: SMB Capital YouTube TpAPTwLMb44, 2026-03-17]

> "We got 76% of [max profit] in 4 days… if we turn right around and enter a new trade… we can vastly increase our profit." [Source: SMB Capital YouTube TpAPTwLMb44, 2026-03-17]
