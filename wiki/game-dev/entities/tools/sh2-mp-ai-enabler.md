---
title: sh2_mp_ai_enabler — Stronghold 2 multiplayer AI (GitLab)
type: entity
tags: [entity, tool, stronghold-2, modding, qol]
keywords: [stronghold-2, multiplayer, ai, daerandin, questforgaming]
related:
  - entities/tools/stronghold2-mp-ai-patch.md
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md
  - sources/sh2-mp-ai-enabler-phase-0-audit-2026-06-18.md
  - concepts/operator-vision-sh2-personal-clone.md
  - concepts/stronghold-2-systems-inventory.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @entities/tools/stronghold2-mp-ai-patch.md — MIT GitHub variant (Jpnock); same feature class
- @concepts/stronghold-2-mod-ecosystem-shelf.md — Tier A QoL #1

## Raw Concept

[Daniel Jenssen / sh2_mp_ai_enabler](https://gitlab.com/Daerandin/sh2_mp_ai_enabler) — external tool (v0.3.1) that enables **AI opponent slots in Stronghold 2 multiplayer** and restores **random AI** button. Primary community-maintained build; binaries at [questforgaming.com/stronghold2](https://www.questforgaming.com/stronghold2/).

**License:** no SPDX on GitLab — **reference/run locally only**; do not copy source into castle-sim.

## Narrative

### Mechanism [CONFIRMED — GitLab README]

1. Launch enabler **before** Stronghold 2 (host only)
2. Attaches to `Stronghold2.exe`; **NOPs 7 bytes** on instruction that clears “add AI” UI flag
3. Also NOPs guard for **random AI** slot filler
4. **No disk changes** — memory-only

Prior versions polled a byte every second; v0.3+ patches the writer instruction instead.

### vs Jpnock MIT patch

| | sh2_mp_ai_enabler | Jpnock/Stronghold2-MP-AI |
|--|-------------------|--------------------------|
| Maintenance | Active 2023+ | Last GitHub push 2024 |
| License | None declared | MIT |
| Technique | NOP instruction | Pattern scan + 12-byte NOP |
| Platform | Win + Linux (AUR package) | Windows C++ |

### Value for castle-sim

Retail SH2 pain point → **native feature** in clone: mixed human/AI Kingmaker without external patcher.

### Phase-0 verdict

**CONDITIONAL-GO** for operator retail research — verify against current Steam 1.5 EXE; watch for “AI only attacks host” MP bug reported on forums.

## Dead Ends

- Expecting Firefly to ship official MP AI — declined in Steam discussions
- Merging enabler into Godot repo — greenfield sim includes AI slots by design
