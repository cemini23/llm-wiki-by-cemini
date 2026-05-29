---
title: Options Martingale 1DTE iron condor warning (SMB)
type: concept
tags: [concept, options, risk-management, iron-condor, k79]
keywords: [martingale, 1dte, iron-condor, spx, tail-risk, community-blowup, seth-freudberg]
related:
  - entities/organizations/smb-capital.md
  - sources/smb-capital-youtube-week-2026-02-04.md
  - concepts/smb-options-casino-edge-model.md
  - concepts/wheel-options-strategy-smb.md
  - concepts/options-capital-velocity-credit-spreads-smb.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @entities/organizations/smb-capital.md — SMB options desk (Seth Freudberg)
- @sources/smb-capital-youtube-week-2026-02-04.md — Killer Mistake video (2026-02-04)
- @concepts/smb-options-casino-edge-model.md — positive-expectancy contrast (defined R:R, no size doubling)
- @concepts/options-capital-velocity-credit-spreads-smb.md — disciplined credit spread exits

## Raw Concept

What prompted this page: SMB cautionary simulation — ~1,000-member community lost **>$50M in ~4 days** on daily **1DTE SPX iron condors** compounded by **Martingale** size escalation (2026-02-04). Reported case; video uses illustrative math, not forensic audit.

## Narrative

### Strategy sketch [TENTATIVE]

- Near close: sell **market-neutral iron condor** on **next-day-expiry** SPX options
- Target ~**$1.75+ credit** per lot; profit if index closes between short strikes
- Works in range — until **directional streak** blows through short call wing

### Martingale flaw [TENTATIVE]

After loss, community **increases lot size** so next day's credit **exceeds cumulative losses** — classic gambler's Martingale applied to options income.

Simulated spiral (Dec 2025 SPX rally streak):

| Day | Approx lot scale | Outcome |
|-----|------------------|---------|
| 1 | ~9,000 lots | Large loss (~$2.9M illustrative) |
| 2 | ~16,000 lots | Larger loss |
| 3 | ~42,000 lots | ~$13M+ loss |
| 4 | ~105,000 lots | **>$50M cumulative** — capital exhaustion |

Capital required scales faster than edge; **no unlimited bankroll** → bankruptcy before "inevitable" recovery win.

### Why this is anti-professional [TENTATIVE]

- Confuses **high win-rate premium collection** with **unlimited-risk tail** when sized recursively
- Opposite of @concepts/smb-options-casino-edge-model.md — pros use **fixed fractional risk**, 2:1 reward:risk, backtested stops
- Community / social proof amplifies blow-up (life-savings concentration)

### Cemini relevance

- **Hard NO-GO** for any automated 1DTE condor + loss-recovery sizing in prod [CONFIRMED for policy — single authoritative warning source].
- If options income sleeve exists, enforce **max daily loss**, **no Martingale**, **tail scenario stress** on short-call wings before deployment [NEEDS VERIFICATION 2026-05-29].

## Snippets

> "Any system predicated on ballooning capital after each losing trade … you won't be there to take that final bet." [Source: SMB Capital YouTube 9EFSF444b7Q, 2026-02-04]

> "The Martingale system … sure as hell doesn't work in trading." [Source: SMB Capital YouTube 9EFSF444b7Q, 2026-02-04]

> "There are plenty of options trading systems that have edge with steady levels of capital." [Source: SMB Capital YouTube 9EFSF444b7Q, 2026-02-04]
