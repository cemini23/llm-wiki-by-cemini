---
title: Broken wing butterfly options (directional and non-directional)
type: concept
tags: [concept, options, index-options, spx, butterfly, k79]
keywords: [broken-wing-butterfly, bwb, spx-options, iron-condor-variant, 0dte, delta-targeting, rsi-trigger]
related:
  - entities/organizations/smb-capital.md
  - sources/smb-capital-youtube-week-2026-05-22.md
  - sources/smb-capital-youtube-week-2026-03-22.md
  - concepts/options-capital-velocity-credit-spreads-smb.md
  - concepts/xsp-put-credit-spread-small-account-smb.md
  - concepts/wheel-options-strategy-smb.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @entities/organizations/smb-capital.md — SMB options education source
- @sources/smb-capital-youtube-week-2026-05-22.md — step-by-step SPX examples
- @sources/smb-capital-youtube-week-2026-03-22.md — XSP small-account sibling
- @concepts/xsp-put-credit-spread-small-account-smb.md — XSP put credit spread

## Raw Concept

What prompted this page: SMB Capital YouTube *How to Trade Broken Wing Butterflies Like a Pro* (2026-05-19) — classroom-style SPX index options walkthrough.

## Narrative

A **broken wing butterfly (BWB)** is a butterfly spread with **asymmetric wing distances** — one wing closer to spot than the other — often structured for **net credit** vs standard symmetrical butterfly debit.

### Index options context (SPX)

- **Cash-settled** index bets; $100/point payoff at expiration.
- **Daily expirations** since 2022 — enables short-dated structure trades.
- Short strikes often placed near **~10–20 delta** for high probability of expiring worthless [TENTATIVE — SMB examples].

### Three SMB use modes [TENTATIVE]

| Mode | Trigger / skew | Example from video |
|------|----------------|------------------|
| **Bullish BWB (puts)** | RSI ~30 after selloff | Pull upper wing closer → credit; needs ~$60k margin in full-size example |
| **Bearish BWB (calls)** | Overbought / rally exhaustion | Asymmetric wings around short call cluster |
| **Non-directional (iron-condor cousin)** | Neutral vol harvest | Dual BWB (call + put) far OTM; e.g. +$1,400 credit on ~$8,600 capital, 10-delta shorts |

### Risk discipline (SMB emphasis)

- All structures **can lose** — requires stop, profit target, and **many-instance backtest** of the trigger rule (e.g. RSI 30/70).
- Options framed as **hypothesis testing** — most ideas fail; survivors need large-N validation.
- **Time decay** can mask adverse spot moves until near expiry — monitor short strikes as DTE compresses.

### Cemini relevance

- Research catalog entry for **index options expression** of directional equity views — distinct from equity single-name options in ticker pages.
- Prod adoption blocked pending: margin model, SPX data feed, and backtest harness for RSI-triggered BWB [NEEDS VERIFICATION 2026-05-29].
- Related but not identical to **iron condor** references on ticker pages (e.g. @entities/tickers/intc.md).

## Snippets

> "The broken wing butterfly can therefore be directional and it can be non-directional." [Source: SMB Capital YouTube FDGN3sMF8AY, 2026-05-19]

> "Anything you do in the options world, you need to back test. You need to pick a stop, you need to pick a target profit, and then you have to run it for many, many instances." [Source: SMB Capital YouTube FDGN3sMF8AY, 2026-05-19]
