---
title: "Gemini DR — World Cup 2026 Group B LP microstructure"
type: source
tags: [source, gemini-deep-research, world-cup-2026, group-b, lp-bot, polymarket, kalshi, k83]
keywords: [canada, switzerland, bosnia, qatar, fade-watch, yes-conviction, alphonso-davies, cross-venue]
related:
  - sources/gemini-wc2026-third-place-advancement-2026-05-29.md
  - sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - concepts/world-cup-advance-market-bot-v1.md
  - entities/tools/world-cup-bot.md
maturity: validated
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @concepts/world-cup-2026-group-conviction-matrix.md — Group B row filled (was DeadBall pending)
- @entities/tools/world-cup-bot.md — `config/conviction.yaml` v3 applied

## Raw Concept

| Field | Value |
|-------|-------|
| Title | FIFA World Cup 2026 Group B Analysis |
| Author | Gemini Deep Research |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/FIFA World Cup 2026 Group B Analysis.docx` |
| Retrieved | 2026-05-29 |
| Read status | deep-read |

## Narrative

Gemini DR **Group B advance-to-knockout LP** report — fills the missing DeadBall Group B slot from K82. Focus: programmatic tier assignments for a maker-only bot, not directional betting.

### LP posture table [CONFIRMED for YAML]

| Team | P(advance) research | PM mid | Gap | Tier | Cap |
|------|---------------------|--------|-----|------|-----|
| Switzerland | 88% | 87¢ | 1pp | bilateral_only (fade_watch in YAML — precedence) | $2000 |
| Canada | 79% | 77¢ | 2pp | yes_conviction | **$2500** |
| Bosnia & Herzegovina | 60% | 58¢ | 8pp vs Kalshi 66–69¢ | **fade_watch** | alert only |
| Qatar | 20% | 18¢ | 11–14pp vs Kalshi 29–32¢ | **fade_watch + skip** | no auto quote |

### Key mechanisms

- **48-team format** inflates group implied probs (~240% sum in Group B) — third-place path matters for Canada/Bosnia hinge match (June 12 Toronto).
- **Cross-venue toxic flow:** ≥5pp PM↔Kalshi on Bosnia/Qatar → adverse selection if bot quotes PM mids blindly.
- **Canada:** Alphonso Davies hamstring (May 8); doubtful for June 12 opener — bot should treat injury news as monitor trigger, not auto-downgrade until confirmed out for group stage.
- **Calendar:** pull quotes **10h before** June 12 Canada–Bosnia kickoff (19:00 UTC).

## Snippets

> "Canada represents the single most optimal asset for algorithmic accumulation within Group B… authorized to elevate maximum notional exposure to USD 2500." [Source: FIFA World Cup 2026 Group B Analysis.docx]

> "Persistent divergence greater than 5pp acts as a beacon for adverse selection… Bosnia and Qatar… fade_watch tier." [Source: FIFA World Cup 2026 Group B Analysis.docx]
