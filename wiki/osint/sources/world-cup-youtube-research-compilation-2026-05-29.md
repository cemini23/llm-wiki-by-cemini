---
title: "World Cup 2026 bot research — YouTube compilation (35 videos, 4 batches)"
type: source
read_status: read
tags: [source, youtube, world-cup-2026, polymarket, kalshi, lp-rewards, research-compilation, k82]
keywords: [deadball-tv, crypto-gorilla, seb-montgomery, dunehammer, cross-venue-arb, group-previews, conviction-matrix]
related:
  - sources/gemini-world-cup-market-structure-research-2026-05-29.md
  - sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md
  - sources/gemini-world-cup-squad-mispricing-analysis-2026-05-29.md
  - sources/gemini-wc2026-third-place-advancement-2026-05-29.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/polymarket-sports-microstructure-bot-taxonomy.md
  - entities/platforms/kalshi.md
maturity: validated
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @concepts/world-cup-2026-group-conviction-matrix.md — DeadBall + B Wade group tables
- @concepts/polymarket-sports-lp-operating-rules.md — batch 4 LP mechanics
- @concepts/world-cup-advance-market-bot-v1.md — v1 spec consumer

## Raw Concept

| Field | Value |
|-------|-------|
| Title | World Cup 2026 YouTube research compilation |
| Author | OSINT session ingest (user-curated URLs) |
| Type | transcript synthesis (local `.local/youtube-ingest/`) |
| Retrieved | 2026-05-29 |
| Videos | 35 across 4 batches |
| Read status | deep-read (synthesis); raw transcripts gitignored locally |

### Batch inventory

| Batch | Count | Focus | Key channels |
|-------|-------|-------|--------------|
| 1 | 12 | PM basics + pundit conviction | Crypto Gorilla, SportsGrid, GOATV, FFT, ESPN |
| 2 | 11 | DeadBall group previews A,C–L | DeadBall TV |
| 3 | 3 | Group B partial + Kalshi guide | B Wade Picks, SharpMoney |
| 4 | 9 | LP farming + cross-venue arb | Seb Montgomery, Dextrabot, predictionist |

**Gap:** DeadBall **Group B** not published as of 2026-05-29; B Wade partial fill (Switzerland 53% Kalshi win).

## Narrative

### Tier A — bot design (mechanics)

**Crypto Gorilla (`7HZGjVqzzSg`):** limit orders only; LP rewards; sports fees/rebates; US geo blocked on web — **deploy on eligible server** (`@entities/infrastructure/cemini-egress-fi.md`); read resolution rules; no market-dump exits.

**Seb Montgomery × DuneHammer (`N8QP23vcXM0`):** canonical sports LP playbook — distant kickoff, rewards tab max spread/min shares, both sides if side <10¢, cancel **6–10h pre-match**, exit fills at break-even, ~$2K cap/market, avoid whale books. [CONFIRMED multi-source with Gemini LP report]

**Dextrabot (`pxaRX8q-e6M`):** automated LP — queue depletion ($300 ahead filled → cancel), 25% drop cooldown, don't get bid accepted.

**Ali Nuraldin (`-_E_PLRui7c`):** bot earned rewards, **lost on directional leg** — public OSS cautionary tale.

**SharpMoney Kalshi (`8usYfZ2gG2g`):** limit=maker, market=taker fees; **free public API** for bots.

### Tier A — WC market navigation

**PM WC how-to videos (batch 1):** Sports → FIFA World Cup; advance + group + match markets; sell-before-resolution repricing thesis.

**SportsGrid (`y8dQ0Kgy7-A`):** "Bet repricing not outcomes"; USA marketing volume inflation on Kalshi.

### Tier B — group conviction (see `@concepts/world-cup-2026-group-conviction-matrix.md`)

DeadBall match-by-match standings (11 groups) + B Wade Kalshi % snapshots. Major split: **DeadBall eliminates USA (Group D 4th)** vs B Wade USA 45% group winner vs Gemini/Kalshi ~44% R16.

### Tier B — cross-venue (alert-only)

- **predictionist / wangr:** resolution text must match; ≥2% after fees; ≥5–6% manual review threshold.
- Semantic mismatch example: "announced" vs "becomes" AG — same headline, different oracle.

### Repricing thesis (multi-source)

Advance markets reprice during group play as results land — bot holds conviction YES LP pre-match, exits NO fills fast, optionally trades repricing (v2) not outright winner futures.

## Snippets

> "We're not betting outcomes — we're betting repricing as the WC goes on." [Source: SportsGrid y8dQ0Kgy7-A via batch 1 synthesis]

> "Your number one goal should be avoid getting filled." [Source: N8QP23vcXM0 — Seb Montgomery podcast]

> "Group D… USA… in fourth, I got the USA on three points." [Source: DeadBall 3bqj4ObETss via batch 2 synthesis]

## Dead Ends

- Paid arb scanner promos (Champ zAEFF6qDSLk) — workflow reference only, not endorsed.
- `$POLY` airdrop optimization (Aero McngyiHdFuE) — explicitly **out of v1** scope.
