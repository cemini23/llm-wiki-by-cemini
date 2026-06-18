---
title: SH2 deep research batch — Exa + Heaven + YouTube (2026-06-17)
type: source
tags: [source, stronghold-2, exa, research-batch]
keywords: [stronghold-2, batch, exa, strategy, mechanics]
related:
  - sources/gamespot-stronghold-2-qanda-2004.md
  - sources/gamespot-stronghold-2-honor-sieges-2004.md
  - sources/gamespy-stronghold-2-siege-dev-diary-2005.md
  - sources/sh2-heaven-kingmaker-strategy-2026-06-17.md
  - sources/firefly-sh2-production-interview-youtube-2026-06-17.md
  - sources/sh2-youtube-parity-watchlist-2026-06-17.md
  - concepts/stronghold-2-kingmaker-strategy.md
  - concepts/stronghold-2-siege-warfare.md
  - concepts/stronghold-2-estates-system.md
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-2-military-units.md
  - concepts/stronghold-2-campaign-economy-curriculum.md
  - concepts/stronghold-2-ai-lords.md
  - sources/sh2-heaven-military-units-2026-06-17.md
  - concepts/stronghold-2-castle-structures.md
  - sources/sh2-heaven-castle-structures-2026-06-18.md
  - sources/sh2-heaven-pow-missions-2026-06-18.md
  - sources/sh2-heaven-kingmaker-ranks-2026-06-18.md
  - sources/sh2-nation-fandom-ai-lords-2026-06-18.md
  - sources/sh2-heaven-campaign-walkthroughs-2026-06-17.md
  - sources/sh2-heaven-buildings-industry-civilian-2026-06-18.md
  - concepts/stronghold-2-production-buildings.md
  - entities/projects/castle-sim.md
read_status: read
source_type: research-batch
maturity: validated
created: 2026-06-17
updated: 2026-06-17
---

## Raw Concept

Operator-requested **deep SH2 research pass** for castle-sim development — Exa API + SH2 Heaven + Stronghold Nation + Firefly YouTube transcripts + prior GameSpy ingest.

## Narrative

### New sources (this batch)

| Slug | Type |
|------|------|
| gamespot-stronghold-2-qanda-2004 | Designer interview |
| gamespot-stronghold-2-honor-sieges-2004 | Preview |
| gamespy-stronghold-2-siege-dev-diary-2005 | Dev diary |
| sh2-heaven-kingmaker-strategy-2026-06-17 | Community strategy |
| firefly-sh2-production-interview-youtube-2026-06-17 | Dev interviews |

### New concepts

| Page | Purpose |
|------|---------|
| stronghold-2-kingmaker-strategy | Opening builds, tax/pop balance, AI quirks |
| stronghold-2-siege-warfare | Attack/defense roster + designer pipeline |
| stronghold-2-estates-system | Multi-estate economy + carters |

### Reinforced from Heaven (re-fetch 2026-06-17)

- Full **popularity tables** — @concepts/stronghold-2-popularity-model.md
- Full **honour tables** + punishment honour clock — @concepts/stronghold-2-crime-punishment-loop.md
- **Kingmaker rank unlock table** — @concepts/stronghold-2-systems-inventory.md

### Community strategy patterns [CONFIRMED — multiple sources]

1. **Tax offset:** extra/double rations + ale + church compensate cruel tax (walkthroughs + Kingmaker tips)
2. **Market-first weapons:** buy bows/spears vs full weapon chain (Kingmaker tips + walkthrough pow5-2)
3. **Pause-heavy campaign:** SH2 pause for economy coordination (Path of War ch7 walkthrough)
4. **Trebuchet behind walls** for defense; **multiple siege camps** for offense (Steam guide + Stronghold Nation)
5. **AI Kingmaker:** buys estates vs ranks up; harassment raids; hard-coded not moddable (Fandom wiki)

### Still deferred

- Per-unit stat tables (SH2 Heaven military pages incomplete)
- AI lord personality matrix (Barclay 50 archers etc.) — forum snippets only [TENTATIVE]
- Steam manual full OCR — partial via Exa

### castle-sim backlog injection

Top implementable learnings:

1. Popularity **8-category panel** with tax/food/ale/church presets
2. **Honour spend** on rank + units without upgrading existing army
3. **Siege camp** building + ladderman resupply loop
4. **Estate carter** manual routing for luxuries
5. **Visual feedback** on church/ale (Bradbury GameSpot)

## Snippets

Exa query clusters: `Bradbury interview`, `Kingmaker strategy`, `siege units`, `honor impressions`, `AI mechanics`.

YouTube tool: `youtube_transcript_api` — Jo5pwX9RQIc, m5CI9ch7b0U, baK1Kiib7gY (+ prior parity watchlist 7 videos).
