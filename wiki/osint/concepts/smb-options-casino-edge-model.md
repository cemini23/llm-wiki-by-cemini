---
title: SMB options casino edge model (positive expectancy)
type: concept
tags: [concept, options, prop-trading, risk-management, k79]
keywords: [casino-edge, positive-expectancy, debit-spread, delta, backtest, seth-freudberg]
related:
  - entities/organizations/smb-capital.md
  - sources/smb-capital-youtube-week-2026-02-14.md
  - concepts/xsp-put-credit-spread-small-account-smb.md
  - concepts/options-capital-velocity-credit-spreads-smb.md
  - concepts/wheel-options-strategy-smb.md
  - concepts/options-martingale-1dte-iron-condor-warning-smb.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @entities/organizations/smb-capital.md — SMB options desk (Seth Freudberg)
- @sources/smb-capital-youtube-week-2026-02-14.md — Trade Options Like a Casino (2026-02-19)
- @concepts/xsp-put-credit-spread-small-account-smb.md — complementary small-account credit structure
- @concepts/options-capital-velocity-credit-spreads-smb.md — exit/roll discipline on credit spreads
- @concepts/options-martingale-1dte-iron-condor-warning-smb.md — anti-pattern contrast (Martingale 1DTE condors)

## Raw Concept

What prompted this page: SMB *Trade Options Like a Casino* — Seth Freudberg reframes prop options trading as **house-edge business** vs amateur directional gambling (2026-02-19).

## Narrative

### Casino analogy [TENTATIVE]

- **Players (amateurs)** — buy low-delta lottery tickets; win sometimes, bleed over time (Hasbro ~0.05 delta example).
- **House (prop desk)** — sells **positive expectancy** via backtested systems; edge from win rate **and** asymmetric payoff.

Roulette reference: ~52.7% house edge on even-money bets; disciplined options systems can exceed **60%** win rate with **2:1** reward:risk.

### Example system (SPX index debit spread) [TENTATIVE]

| Parameter | Value |
|-----------|-------|
| Trigger | Proprietary directional indicator (bull → call debit spread; bear → put debit spread) |
| Structure | ~75Δ long leg + short leg near 25Δ (put or call debit spread) |
| Profit target | **15%** of capital deployed |
| Stop | **7.5%** of capital (half of target — risk $1 to make $2) |
| Backtest win rate | ~**60%** hit target before close vs ~40% stopped |

Key insight: edge is not win rate alone — **payoff asymmetry** (double the loss on winners vs losers) compounds like a casino.

### Amateur vs pro delta discipline [TENTATIVE]

Directional buyers often hold **near-zero delta** OTM options — low probability, full premium at risk. Pros structure spreads with defined risk/reward and systematic exits.

### Cemini relevance

- Options sleeve automation requires **backtested expectancy** + explicit R:R — do not deploy indicator triggers without replication [NEEDS VERIFICATION 2026-05-29].
- Framework aligns with prod posture: sell edge / defined-risk structures, not naked directional lottery tickets.
- Distinct from @concepts/wheel-options-strategy-smb.md (assignment income) and credit-spread velocity rules — catalog as **intraday debit-spread template** pending backtest.

## Snippets

> "When you win, you get double what you lose … risking a dollar to make two dollars." [Source: SMB Capital YouTube rpFL_mEFPSg, 2026-02-19]

> "There was actually a 60% chance of it hitting its target profit … only a 40% chance … go the opposite way." [Source: SMB Capital YouTube rpFL_mEFPSg, 2026-02-19]
