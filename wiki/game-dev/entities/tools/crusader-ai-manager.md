---
title: CrusaderAIManager — lord slot swap tool
type: entity
tags: [entity, tool, stronghold, crusader, modding, steal-from]
keywords: [crusader-ai-manager, nmme, aiv, mod-pack, ucp]
related:
  - sources/crusader-ai-manager-phase-0-audit-2026-06-20.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - entities/tools/unofficial-crusader-patch2.md
  - entities/tools/evrey-shc-aiv.md
  - entities/tools/krarilotus-crusader-efficient-ai.md
  - entities/tools/monsterfisch-strongholds-of-conquest.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/stronghold-crusader-ai-modding-shelf.md — toolchain stack
- Gitignored brief: `briefs/research/crusader-aiv-study-loop.md`

## Raw Concept

[NMme/CrusaderAIManager](https://github.com/NMme/CrusaderAIManager) — Python GUI/CLI to inject a custom lord mod (AIV + bink + speech) into **one of 16 Crusader slots** without replacing the full roster.

**License:** MIT [CONFIRMED]

## Narrative

### Workflow

1. Select base mod pack (vanilla or UCP-enhanced)
2. Pick target lord slot (1–16)
3. Point at custom lord folder (`.aiv`, `.bik`, `.wav`)
4. Output merged pack under `data/output/`

### castle-sim mapping

| Crusader | Godot target |
|----------|--------------|
| 16-slot roster | Kingmaker lobby lord picker |
| Per-slot swap | Hot-swap `lord_profiles.json` + template without full rebuild |

### Phase-0 verdict

**STEAL-FROM (modding UX)** — @sources/crusader-ai-manager-phase-0-audit-2026-06-20.md

## Dead Ends

- Runtime dependency in castle-sim — Windows/Crusader retail only
