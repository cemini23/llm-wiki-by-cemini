---
title: "Gemini DR — World Cup 2026 market gap live verification (May 29)"
type: source
tags: [source, gemini-deep-research, world-cup-2026, cross-venue, fade-watch, live-verification, k83]
keywords: [group-winner, advance-tbd, alert-threshold, kxwcgroupwin, semantic-blocker]
related:
  - sources/gemini-wc2026-cross-venue-arbitrage-dynamics-2026-05-29.md
  - sources/gemini-world-cup-squad-mispricing-analysis-2026-05-29.md
  - sources/gemini-wc2026-group-b-lp-analysis-2026-05-29.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - concepts/world-cup-advance-market-bot-v1.md
  - entities/tools/world-cup-bot.md
maturity: validated
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @sources/gemini-world-cup-squad-mispricing-analysis-2026-05-29.md — prior book-vs-Kalshi gaps; **partially superseded** by this live sweep for group-winner pairs
- @sources/gemini-wc2026-group-b-lp-analysis-2026-05-29.md — Group B cross-venue context
- @concepts/world-cup-advance-market-bot-v1.md — Module 6 `cross_venue.yaml` seed
- @entities/tools/world-cup-bot.md — `config/cross_venue.yaml` seeded from this report

## Raw Concept

| Field | Value |
|-------|-------|
| Title | World Cup 2026 Market Gap Analysis |
| Author | Gemini Deep Research |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/World Cup 2026 Market Gap Analysis.docx` |
| Retrieved | 2026-05-29 |
| Read status | deep-read |

## Narrative

**Live verification** (May 29, 2026) of fade_watch cohort: USA, Switzerland, England, Croatia, Mexico. Closes K82 open item "Gemini report #5 ticker map" for **group-winner** markets.

### Headline findings [CONFIRMED]

1. **Advance-to-knockout PM↔Kalshi pairs are NOT semantically pairable today** — PM advance/R32 slugs **TBD** for fade_watch teams; Kalshi has split `KXWCGROUPQUAL` vs `KXWCROUND-26RO16`.
2. **Five verified equivalent pairs** — all **group winner** only; raw gaps **below 5pp alert threshold** (max Croatia 2.0pp).
3. **Fee-adjusted:** all verified gaps are **negative EV** after Kalshi ~7% profit fee.
4. **Croatia 2pp gap** — Kalshi volume ~$266; likely stale/wide spread, not actionable.

### Verified pairs (May 29)

| Team | PM mid | Kalshi mid | Gap | Alert? |
|------|--------|------------|-----|--------|
| USA | 38.5% | 39.5% | 1.0pp | No |
| Switzerland | 54.5% | 53.0% | 1.5pp | No |
| England | 70.5% | 69.5% | 1.0pp | No |
| Croatia | 22.0% | 20.0% | 2.0pp | No |
| Mexico | 52.5% | 52.5% | 0.0pp | No |

### Impact on prior mispricing thesis

K82 squad-mispricing **advance** gaps (e.g. Switzerland +37pp book vs Kalshi) are **not reproduced** on live group-winner mids May 29. Keep fade_watch for **sentiment / book divergence** monitoring; do not assume persistent 5pp+ cross-venue on equivalent contracts until PM advance markets list.

## Snippets

> "True semantic equivalence for advance-to-knockout derivatives is presently absent between the two platforms." [Source: World Cup 2026 Market Gap Analysis.docx]

> "No pairs successfully triggered the predefined ≥5pp raw gap alert threshold." [Source: World Cup 2026 Market Gap Analysis.docx]
