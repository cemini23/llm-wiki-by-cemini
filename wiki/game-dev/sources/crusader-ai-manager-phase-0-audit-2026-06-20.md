---
title: CrusaderAIManager — Phase-0 audit — 2026-06-20
type: source
tags: [source, phase-0, stronghold, crusader, modding, audit]
keywords: [crusader-ai-manager, nmme, aiv, mod-pack]
related:
  - entities/tools/crusader-ai-manager.md
  - entities/tools/unofficial-crusader-patch2.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
read_status: read
source_type: operator-audit
source_url: https://github.com/NMme/CrusaderAIManager
maturity: validated
created: 2026-06-20
updated: 2026-06-20
---

## Raw Concept

Phase-0 audit of **NMme/CrusaderAIManager** — Python GUI/CLI to swap custom AI mods into one of 16 Crusader lord slots without manual `.aiv`/`.bik` renaming.

## Narrative

### Checks

| Gate | Result |
|------|--------|
| License | **MIT** [CONFIRMED — GitHub API] |
| Maturity | Active 2026; tkinter GUI + pyinstaller build |
| Mechanism | Pick base mod (vanilla/UCP) → replace slot → output `data/output/` pack |
| castle-sim fit | **STEAL-FROM (workflow)** — lord slot swap UX metaphor for JSON template rotation |
| Runtime | Requires retail Crusader + UCP ecosystem |

### Steal value

| Extract | Skip |
|---------|------|
| 16-slot roster manager pattern | Shipping Python tool in castle-sim |
| Auto rename speech/bink/aiv paths | Firefly asset redistribution |

### Verdict

**STEAL-FROM (modding UX)** — operator brief: gitignored `briefs/research/crusader-aiv-study-loop.md`

## Dead Ends

- Using as castle-sim dependency — study-only Windows/Crusader host
