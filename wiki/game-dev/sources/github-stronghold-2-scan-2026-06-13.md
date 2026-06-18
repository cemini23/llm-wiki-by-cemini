---
title: GitHub Stronghold 2 ecosystem scan (2026-06-13)
type: source
tags: [source, stronghold-2, github, modding]
keywords: [github, patch, trainer, s2m, mp-ai, analysehub]
related:
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - concepts/stronghold-2-systems-inventory.md
  - entities/tools/stronghold2-analyse-hub.md
  - entities/tools/stronghold2-mp-ai-patch.md
  - sources/stronghold2-analyse-hub-phase-0-audit-2026-06-13.md
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md
  - sources/stronghold2-mp-ai-patch-phase-0-audit-2026-06-13.md
  - concepts/stronghold-2-mod-ecosystem-shelf.md
read_status: read
source_type: github-scan
source_url: https://github.com/search?q=stronghold2&type=repositories
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Raw Concept

Operator-requested GitHub sweep for SH2 patches and repurposable tooling. Method: `gh search repos`, `search code`, README + license API, spot-read of key source files.

## Narrative

### Repos verified

| Repo | License | Last updated | Verdict |
|------|---------|--------------|---------|
| Jpnock/Stronghold2-MP-AI | MIT | 2024-10 | STEAL-FROM (patch pattern) |
| Przodownik/Stronghold2-MP-AI-Patch | MIT | 2025-08 | fork |
| crycodebaby/Stronghold2AnalyseHub | MIT | 2026-02 | STEAL-FROM (research DLL) |
| Alleyv2/Stronghold2-AI-Enabler-Proton | none | 2025-10 | reference (Proton offsets) |
| Eren121/Stronghold | none | 2019-11 | reference (S2M + units) |
| Ald0s/Stronghold2-Trainer | none | 2020-10 | reference (player struct) |
| utreah/stronghold2ext | none | 2025-11 | reject |
| EBoespflug/stronghold-maps | none | 2021-07 | map fixtures |
| sourcehold/sourcehold-maps | GPL-3.0 | active | **SH1/Crusader only** |

### Key extracted data

**MP-AI:** `Signatures.h` byte pattern + 12-byte NOP at match in `Stronghold2.exe` main module.

**Proton enabler:** `POINTER_OFFSET = 0x00ec5f28`, `ADDRESS_OFFSET = 0xd28`, module `Stronghold2.exe`.

**Trainer (Steam ~v1.5):** local player static `base + 0x6E7C60`; player slot stride; resource enum offsets in `player.h`; entity damage `+0x385380`.

**Eren121 units (example):** `Archer EB367C`, `Swordsman EB25CC`, `Lord EBCC7C` — runtime class vtables/pointers, not names.

**S2M:** Qt SiegeExporter implements header + 3× zlib segments; README protobuf-style spec.

### Search noise

Majority of `stronghold2` / `Stronghold2016` hits are unrelated (FRC 2016 game, Minecraft, student projects).

## Dead Ends

- No GitHub repo for Firefly official Steam Edition patch sources
- No MIT SH2 map editor successor to broken Java map unlocker
