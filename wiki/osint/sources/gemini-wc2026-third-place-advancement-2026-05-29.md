---
title: "Gemini DR — World Cup 2026 third-place advancement math"
type: source
tags: [source, gemini-deep-research, world-cup-2026, third-place, goal-difference, lp-bot, k83]
keywords: [48-team, eight-best-thirds, ivory-coast, scotland, dr-congo, gd-sensitivity]
related:
  - sources/gemini-wc2026-group-b-lp-analysis-2026-05-29.md
  - sources/world-cup-youtube-research-compilation-2026-05-29.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - concepts/world-cup-advance-market-bot-v1.md
  - entities/tools/world-cup-bot.md
maturity: validated
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @sources/world-cup-youtube-research-compilation-2026-05-29.md — B Wade third-place explainer (prior)
- @concepts/world-cup-2026-group-conviction-matrix.md — third-place tiebreak section

## Raw Concept

| Field | Value |
|-------|-------|
| Title | 2026 World Cup Third-Place Advancement Analysis |
| Author | Gemini Deep Research |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/2026 World Cup Third-Place Advancement Analysis.docx` |
| Retrieved | 2026-05-29 |
| Read status | deep-read |

## Narrative

Quantitative **third-place / GD** study for 48-team format (12×4, **8 best thirds** advance). Feeds conviction caps and skip list — not hardcoded mids.

### Thresholds [TENTATIVE — simulation-heavy]

- **4 points** as third → near-certain advancement among 12 thirds.
- **3 points** → GD / goals-scored tiebreak dogfight (bubble tier).
- **2 points** → effectively dead for third-place route.

### Actionable mispricings

| Team | PM mid (advance) | Research P(advance) | Mispricing | YAML action |
|------|------------------|---------------------|------------|-------------|
| **Ivory Coast** | 37% | 88% | **+51pp** | yes_conviction; cap **$2500** |
| **Scotland** | 34% | 65% | +31pp | yes_conviction; normal cap |
| **DR Congo** | 38% | 28% | **−10pp** | **skip** (GD blowout vs POR/COL) |

### Borderline thirds ranked (bubble)

Czechia, Ghana, Iran, Bosnia — GD-dependent; Bosnia also cross-venue fade (see Group B source).

### Safe thirds (research)

Sweden, Ivory Coast, Paraguay, Scotland — defensive/low-event profiles protect GD.

## Snippets

> "Ivory Coast's Polymarket Round of 16 / Advance pricing sits inexplicably low at a 37% implied probability… research implies 84% to 90%." [Source: 2026 World Cup Third-Place Advancement Analysis.docx]

> "DR Congo… overpriced at 38%… quantitative probability closer to 28%… blowout defeats to Portugal and Colombia will destroy their GD." [Source: 2026 World Cup Third-Place Advancement Analysis.docx]
