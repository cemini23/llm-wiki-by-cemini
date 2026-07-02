---
title: Indie kingdom-builder lessons — scope and economy patterns
type: concept
tags: [concept, indie, scope, economy, postmortem]
keywords: [indie, kingdoms-and-castles, northgard, scope, economy]
related:
  - concepts/scope-tiers.md
  - concepts/vertical-slice-v0.md
  - sources/gdc-kingdoms-and-castles-postmortem-2019.md
  - sources/northgard-economy-case-study-2018.md
  - sources/simon-bradbury-stronghold-heaven-sh3-2011.md
  - sources/gamespy-stronghold-2-bradbury-qa-2004.md
  - sources/firefly-about-us-studio-history.md
  - sources/mandate-order-city-walls-shelf-2026-06-25.md
  - sources/arxiv-2606.26925-vr-dynamic-feedback-pointing-2026-07-02.md
  - concepts/agent-harness-castle-project.md
maturity: validated
created: 2026-06-13
updated: 2026-07-02
---

## Relations

- @sources/simon-bradbury-stronghold-heaven-sh3-2011.md — AAA/sim veteran scope discipline

## Raw Concept

Cross-source lessons for hobby castle-sim from GDC postmortems, Firefly interviews, and Northgard economy analysis.

## Narrative

### Scope discipline

| Source | Lesson |
|--------|--------|
| Kingdoms & Castles GDC | Validate audience **before** ship; scope evolved — document cuts |
| Simon Bradbury | Reject oversized maps; fewer unit types > many unbalanced types |
| Simon Bradbury | SH2 features cut when fans wanted SH1 feel — **sequel regression is OK** |
| GameSpy SH2 Q&A | Fans wanted **no sword-wall hacking** — siege breaches only; informs Tier 2 siege |
| Firefly about-us | Definitive/Crusader DE sales prove **return-to-SH1** market — validates Tier 1 scope |
| Northgard analysis | Anti-snowball via caps + drains — don't add all systems at once |
| Vertical slice v0 | One resource, one military type, no AI lord |
| Mandate Order (2026 press) | Walls as whole-settlement test — genre active [@sources/mandate-order-city-walls-shelf-2026-06-25.md] |

### Economy patterns (Tier 2 candidates)

| Pattern | Source | Tier 1? |
|---------|--------|---------|
| Villager-as-resource | Northgard | Simplified (cap only) |
| Territory expansion reward | Northgard | Defer |
| Seasonal drain (winter) | Northgard | Defer |
| Popularity ↔ tax/rations | Stronghold manual | Defer |
| Stockpile placement optimization | Stronghold Heaven guides | Tier 1 wood only |

### Marketing / dev process

- K&C: test interest pre-release [TENTATIVE GDC summary]
- Firefly: modding/editor = replayability multiplier — defer editor until slice ships

## Snippets

Bradbury map-size rule: extra march time without combat = bad pacing → keep castle-sim maps small for v0 spike (20×20 OK).
