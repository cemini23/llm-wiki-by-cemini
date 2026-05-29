---
title: Wheel options strategy (SMB cash-flow income)
type: concept
tags: [concept, options, income-strategy, equities, k79]
keywords: [wheel-strategy, cash-secured-put, covered-call, qqq-example, warren-buffett-put-selling]
related:
  - entities/organizations/smb-capital.md
  - sources/smb-capital-youtube-week-2026-02-28.md
  - concepts/options-capital-velocity-credit-spreads-smb.md
  - concepts/xsp-put-credit-spread-small-account-smb.md
  - concepts/broken-wing-butterfly-options.md
  - concepts/smb-options-casino-edge-model.md
  - concepts/options-martingale-1dte-iron-condor-warning-smb.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @entities/organizations/smb-capital.md — SMB options education
- @sources/smb-capital-youtube-week-2026-02-28.md — primary source (2026-02-28)
- @concepts/options-capital-velocity-credit-spreads-smb.md — sibling SMB options sleeve (velocity / early close)
- @concepts/xsp-put-credit-spread-small-account-smb.md — small-account credit spread variant
- @concepts/broken-wing-butterfly-options.md — other SMB options structures

## Raw Concept

What prompted this page: SMB *The Wheel Options Strategy Explained* (2026-02-28). Cyclical **cash-secured put → assignment → covered call → repeat** on stocks/ETFs you want to own at lower prices.

## Narrative

### Mechanics

1. **Sell OTM put** (monthly, 3rd Friday) at strike where you'd buy 100 shares (cash-secured margin).
2. **If assigned** — own shares at strike; keep premium.
3. **Sell covered call** ~25 points above cost basis (next monthly expiry); collect premium.
4. **If called away** — sell at strike profit + accumulated premium.
5. **"Wheel"** — rotate back to put side below market; repeat.

### QQQ walkthrough (Oct 2025 – Feb 2026) [TENTATIVE — SMB promo example]

- Sell 595 put Oct 17 → assigned Nov 21; $1,249 premium.
- Sell 620 calls Dec/Jan → premiums + Jan assignment at 620.
- Claimed ~$5,813 wheel profit vs ~$488 buy-and-hold on same capital over ~4 months [marketing math — verify independently].

### Prerequisites

- Only on names you'd **own long-term** at strike (Buffett-style put selling cited).
- Buy on retracement, not chase highs.
- Capital for 100-share assignment at put strike.

### Cemini relevance

- **P2 options sleeve** catalog entry alongside credit spreads / BWB — automation requires assignment risk, dividend, and call-away modeling on backtest before prod.
- Not prediction-market scope; equity income sleeve reference only.

## Snippets

> "Get paid while you wait to buy a stock at the price you want to pay for it." [Source: SMB Capital YouTube K6YVPHULzPA, 2026-02-28]

> "It's called the wheel because we sell below the market … rotate up … then rotate back down to the put side." [Source: SMB Capital YouTube K6YVPHULzPA, 2026-02-28]
