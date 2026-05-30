---
title: "World Cup 2026 — tournament phases LP strategy (group → final)"
type: concept
tags: [concept, world-cup-2026, polymarket, knockout, lp-bot, tournament-phases, k85]
keywords: [knockout-round, reach-final, in-play, lineup-injury, phase-router, market-phases]
related:
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - sources/gemini-sports-prediction-bot-pitfalls-2026-05-29.md
  - entities/tools/world-cup-bot.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @concepts/world-cup-advance-market-bot-v1.md — v1 scope = group advance only; this page plans v2 through final
- @concepts/polymarket-sports-lp-operating-rules.md — cancel window, fill handler invariants apply to all phases
- @entities/tools/world-cup-bot.md — `config/market_phases.yaml` stub; DR prompts 08–10

## Raw Concept

User requirement (K85): comprehensive World Cup bot through finals, not group-stage-only. Research + architecture mapping before Issue 3 launch (2026-06-03). v1 ships group advance LP; v2 adds knockout via phase router.

## Narrative

### Polymarket market taxonomy (Exa May 2026) [TENTATIVE]

| Phase | PM market type | LP v1 | LP v2 candidate |
|-------|----------------|-------|-----------------|
| Group | Advance to knockout | **IN** | Keep |
| Long | Reach final | OUT | **IN** post-group |
| Long | WC Winner (immediate No on KO exit) | OUT | Alert only |
| Knockout | Match winner / tie advance | OUT | Research |
| Props | Golden boot, specials | OUT | OUT |

[Source: https://polymarket.com/event/world-cup-team-to-advance-to-knockout-stages (retrieved 2026-05-29)]

### Issue categories

| Category | v1 posture | v2 research (DR 09) |
|----------|------------|---------------------|
| Pregame XI / injury | 10h cancel; human_review | 24h KO window? |
| In-play goals | **Hard halt** | Live-score breaker |
| Elimination cascade | Manual cancel | Auto cancel all phases |
| Phase transition | Manual YAML | Phase router (DR 10) |

### Gemini DR queue (pre-launch)

- `knockout-market-map` — prompt 08
- `inplay-pregame-risks` — prompt 09
- `tournament-phase-router` — prompt 10
- `conviction-staleness` — LP safety pre-friendlies

### Milestones

| When | What |
|------|------|
| 2026-06-03 | v1 launch (group advance) |
| 2026-06-06 | LP safety DR checkpoint |
| Post-group | v2 phase router implementation |

## Snippets

> WC winner markets resolve immediately to No on knockout elimination — not LP-safe. [Source: polymarket.com WC winner rules, retrieved 2026-05-29]
