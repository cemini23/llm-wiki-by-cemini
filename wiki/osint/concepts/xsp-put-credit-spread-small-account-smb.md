---
title: XSP put credit spread — sub-$100 small-account options (SMB)
type: concept
tags: [concept, options, xsp, small-account, index-options, k79]
keywords: [xsp, put-credit-spread, 20-day-ma, small-account, seth-freudberg, options-selling]
related:
  - entities/organizations/smb-capital.md
  - sources/smb-capital-youtube-week-2026-03-22.md
  - concepts/options-capital-velocity-credit-spreads-smb.md
  - concepts/broken-wing-butterfly-options.md
  - concepts/wheel-options-strategy-smb.md
  - concepts/smb-options-casino-edge-model.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @entities/organizations/smb-capital.md — SMB options desk
- @sources/smb-capital-youtube-week-2026-03-22.md — Seth Freudberg walkthrough
- @concepts/broken-wing-butterfly-options.md — sibling SMB index-options education
- @concepts/options-capital-velocity-credit-spreads-smb.md — exit/recycle on put credit spreads

## Raw Concept

What prompted this page: SMB *The $100 New Options Strategy* (Seth Freudberg, 2026-03-25) — **XSP** (1/10 notional SPX) put credit spreads for sub-$100 capital small accounts.

## Narrative

**Problem:** SPX index too large for small retail; buying OTM options ≈ lottery tickets on tiny accounts.

**SMB approach** [TENTATIVE]:

- Trade **XSP** index options (cash-settled, $100/point like SPX).
- **Signal:** XSP closes **above 20-day MA** after having been below (simple regime filter).
- **Structure:** 1-point-wide **ATM put credit spread** (~2-week expiry) — sell put at strike just below spot, buy put 1 strike lower.
- **Capital:** Max loss $100/contract width minus credit received; example net **$62** broker requirement after $38 credit (Apr 2025 example in video).
- **Exit:** Close on 20-DMA break below OR hold through expiry if index stays above short strikes.
- **Discipline:** Repeat when signal re-fires; selling not buying for steady small-account growth.

### Cemini relevance

- Education-only for index options sleeve — prod needs margin model + systematic backtest before any automation [NEEDS VERIFICATION 2026-05-29].
- XSP as SPX proxy already noted in BWB concept (@concepts/broken-wing-butterfly-options.md).

## Snippets

> "We're not going to suggest you go down that road [buying options]… the strategy we're going to be teaching today is… an options selling strategy." [Source: SMB Capital YouTube Jniwt90PUS4, 2026-03-25]

> "Your broker is going to require you to have $62 in capital… the largest loss… is $100." [Source: SMB Capital YouTube Jniwt90PUS4, 2026-03-25]
