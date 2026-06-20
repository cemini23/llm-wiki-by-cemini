---
title: Monsterfisch Strongholds of Conquest — Phase-0 audit — 2026-06-20
type: source
tags: [source, phase-0, stronghold, crusader, modding, audit]
keywords: [monsterfisch, conquest, aiv, historical]
related:
  - entities/tools/monsterfisch-strongholds-of-conquest.md
  - entities/tools/evrey-shc-aiv.md
  - entities/tools/unofficial-crusader-patch2.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
read_status: read
source_type: operator-audit
source_url: https://github.com/Monsterfisch/StrongholdsOfConquest_
maturity: validated
created: 2026-06-20
updated: 2026-06-20
---

## Raw Concept

Phase-0 audit of **Monsterfisch/StrongholdsOfConquest_** — historical Crusader **AIV** rework + bundled aggressive **AIC** (UCP-dependent).

## Narrative

### Checks

| Gate | Result |
|------|--------|
| License | **None declared** — study layouts only |
| Maturity | Complete 16-lord set; historical plan references; requires UCP |
| Content | Per-lord AIV + presentation screenshots; optional visual edit zip |
| castle-sim fit | **STEAL-FROM (layout quality bar)** — historical choke + economy density reference |

### Steal value

| Extract | Skip |
|---------|------|
| Historical castle → gameplay layout translation | Redistributing `.aiv` binaries |
| UCP aggressive AIC pairing | Expecting MIT license |

### Verdict

**STEAL-FROM (design)** — complement Evrey/Krarilotus in study loop; transcribe to `castle_templates/`.

## Dead Ends

- README "ALL RIGHTS RESERVED" — no redistribution into public repo
