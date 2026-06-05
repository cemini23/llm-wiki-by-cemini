---
title: "Gemini DR — WC 2026 market probability gaps (fade-watch qualify map)"
type: source
tags: [source, gemini-deep-research, world-cup-2026, cross-venue, fade-watch, group-qualify, k99]
keywords: [kxwcgroupqual, round-of-32-qualifiers, fee-adjusted-edge, alert-threshold, usa-bias]
related:
  - sources/gemini-wc2026-cross-venue-scanner-research-2026-06-05.md
  - sources/gemini-wc2026-cross-venue-arbitrage-dynamics-2026-05-29.md
  - sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - entities/tools/world-cup-bot.md
maturity: validated
created: 2026-06-05
updated: 2026-06-05
---

## Relations

- @sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md — May 29 group-**winner** sweep; this report adds **group qualify / R32** pairs
- @entities/tools/world-cup-bot.md — K99 `group_qualify` pairs + fee-adjusted alert gate in `cross_venue.yaml`

## Raw Concept

| Field | Value |
|-------|-------|
| Title | World Cup 2026 Market Probability Gaps |
| Author | Gemini Deep Research |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/gemini-wc2026-market-probability-gaps-2026-06-05.docx` |
| Retrieved | 2026-06-05 |
| Read status | deep-read |

## Narrative

Live snapshot **2026-06-05** — fade-watch **group qualify** (R32 escape) pairs for alert-only Module 6.

### Verified equivalent pairs (group qualify)

| Team | PM mid | Kalshi ticker | Kal mid | Raw gap | Alert ≥5pp? | Fee-adj note |
|------|--------|---------------|---------|---------|-------------|--------------|
| USA | 82.0% | `KXWCGROUPQUAL-26D-USA` | 86.0% | **4.0pp** | No | **-2.02pp** |
| Mexico | 93.0% | `KXWCGROUPQUAL-26A-MEX` | 92.0% | 1.0pp | No | -0.64pp |
| England | 97.4% | `KXWCGROUPQUAL-26L-ENG` | ~97.0% | 0.4pp | No | — |
| Croatia | — | `KXWCGROUPQUAL-26L-CRO` | ~21.5% | ~1.0pp | No | thin book |
| Switzerland | 93.3% | `KXWCGROUPQUAL-26B-SUI` | **unavailable** | N/A | Blocked | force Kalshi fetch |

**None** trigger raw ≥5pp. USA is max dislocation; fee-adjusted negative.

### PM hint phrasing

- "Round of 32 Qualifiers" / "to reach Round of 32" on Polymarket
- Kalshi: `KXWCGROUPQUAL-26{GROUP}-{TEAM}`

### YAML seed (K99 → bot repo)

Exported to `world-cup-bot/exports/k99-cross-venue-research-2026-06-05.json` and `config/cross_venue.yaml` `group_qualify` pairs (enabled, `rules_hash: group_qualify_v1`).

### Reject directory [CONFIRMED]

- PM "Reach Round of 16" ↔ Kalshi group qualify — **false**
- PM stub slugs (50¢ placeholders) — **false**
- Croatia summary table typo (`KXWCWIN` group winner) — use **GROUPQUAL** for qualify map

## Snippets

> "The algorithmic matching process yielded four fully verified, semantically equivalent contract pairs for the target teams, with one pair blocked due to unavailable live order book data on Kalshi." [Source: World Cup 2026 Market Probability Gaps.docx]

> "The alert scanner must process this exact formula for every tick to prevent the notification of mathematically inviable opportunities." [Source: World Cup 2026 Market Probability Gaps.docx]
