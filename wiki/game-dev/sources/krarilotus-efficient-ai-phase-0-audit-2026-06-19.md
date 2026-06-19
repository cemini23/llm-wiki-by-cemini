---
title: Krarilotus Crusader efficient AI — Phase-0 audit — 2026-06-19
type: source
tags: [source, phase-0, stronghold, crusader, modding, audit]
keywords: [aic, krarilotus, crusader, aiv, aggressive]
related:
  - entities/tools/krarilotus-crusader-efficient-ai.md
  - entities/tools/evrey-shc-aiv.md
  - entities/tools/unofficial-crusader-patch2.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - sources/evrey-shc-aiv-phase-0-audit-2026-06-19.md
  - sources/stronghold-franchise-research-pass2-2026-06-18.md
read_status: read
source_type: operator-audit
source_url: https://github.com/Krarilotus/Stronghold-Crusader-efficient-AI
maturity: validated
created: 2026-06-19
updated: 2026-06-19
---

## Raw Concept

Phase-0 audit of **Krarilotus/Stronghold-Crusader-efficient-AI** — efficient **AIV** prototypes + **aggressive AIC** for Crusader skirmish (2k gold baseline).

## Narrative

### Method

GitHub README (2026-06-19). Project stage: **prototyping** (Rat finished; Snake/Pig/etc. in progress).

### Checks

| Gate | Result |
|------|--------|
| License | **None declared** — reference only |
| Maturity | Active WIP; bundled aggressive `.aic`; 15 test maps; build-order Google Doc |
| Goals | Same build-step count across 8 castles/lord; fast AI setup; skirmish-trail compatible footprint |
| castle-sim fit | **STEAL-FROM (timing + aggression)** — harass/siege thresholds for `lord_profiles.json` |
| Pairing | Designed for Evrey AIV + UCP2 |

### Steal value

| Extract | Skip |
|---------|------|
| First-attack timing benchmarks (high/low pressure maps) | Incomplete lord roster |
| Build-order documentation discipline | Copying WIP AIV files |
| Aggressive AIC behaviour deltas | Expecting MIT license |

### Verdict

**STEAL-FROM (design, WIP)** — use for AI director tuning once prototypes stable. Track Rat/Snake completion.

## Dead Ends

- Adopting as primary AIV set before Stage 1 completes — Evrey pack more complete today
