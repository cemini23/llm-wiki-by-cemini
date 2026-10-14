---
title: Exa flow-fields + Firefly batch — 2026-06-13
type: source
tags: [source, exa, ingest, pathfinding, stronghold, firefly]
keywords: [exa, flow-field, firefly, gdc, emerson, godot]
related:
  - concepts/flow-field-pathfinding.md
  - concepts/rts-pathfinding-approaches.md
  - sources/exa-deep-research-batch-2026-06-13.md
  - sources/gamespy-stronghold-2-bradbury-qa-2004.md
  - sources/emerson-game-ai-pro-flow-field-tiles-2013.md
  - sources/vav-labs-godot-flow-fields-2026.md
read_status: read
source_type: exa-batch
source_url: wiki/sweeps/2026-06-13-exa-flowfields-firefly-batch.json
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

Second Exa pass focused on **GDC Stronghold/Firefly** postmortems and **flow-field** implementation references — follow-up to first deep batch.

## Narrative

### Clusters run (8)

| Cluster | Query focus | Notable hits |
|---------|-------------|--------------|
| gdc-stronghold-firefly | GDC Firefly Stronghold postmortem | **No Stronghold-specific GDC talk found** |
| firefly-bradbury-interviews | Simon Bradbury design Q&A | GameSpy SH2 (2004), Legends making-of (2018) |
| emerson-flow-field-tiles | Game AI Pro Ch.23 | Taylor & Francis / GameAIPro PDF |
| leifnode-flow-field | Tutorial implementation | leifnode.com 2013 |
| flow-field-pathfinding-game | General game dev | Red Blob Games 2024, How to RTS, jdxdev |
| flow-field-rts-tutorial | Godot + dynamic obstacles | **Vav Labs Godot 2026**, bcaptain blog |
| continuum-crowds-paper | Academic crowd sim | ACM corridor map papers |
| openage-bevy-flow | Engine refs | openage README, bevy_flowfield_tiles_plugin |

**68 unique URLs** — raw JSON: `wiki/sweeps/2026-06-13-exa-flowfields-firefly-batch.json`

### GDC gap [CONFIRMED — search negative]

Exa + web search found **no dedicated GDC Vault talk by Firefly on Stronghold design**. Best substitutes for castle-sim research:

| Substitute | Why |
|------------|-----|
| @sources/gamespy-stronghold-2-bradbury-qa-2004.md | Primary designer on siege/walls/3D pivot |
| @sources/simon-bradbury-stronghold-heaven-sh3-2011.md | Scope discipline, SH1 return |
| @sources/gdc-kingdoms-and-castles-postmortem-2019.md | Adjacent indie kingdom-builder GDC |
| @sources/gdc-total-war-warhammer-siege-ai.md | Tier 2+ siege AI (not castle-builder) |

### Pages written from batch

- Concept: @concepts/flow-field-pathfinding.md
- Sources: Emerson, Leif Node, Vav Labs, Red Blob Games, GameSpy SH2, Firefly about-us, Legends making-of

## Snippets

```bash
# Batch artifact only — no dedicated runner script yet
# Re-run via Exa API with cluster keys in wiki/sweeps/2026-06-13-exa-flowfields-firefly-batch.json
```
