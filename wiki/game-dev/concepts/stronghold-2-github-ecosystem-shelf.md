---
title: Stronghold 2 — GitHub ecosystem shelf (2026-06-13 scan)
type: concept
tags: [concept, stronghold-2, modding, github, reference]
keywords: [stronghold-2, patch, trainer, s2m, memory, analysehub, mp-ai]
related:
  - concepts/stronghold-modding-ecosystem-shelf.md
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-2-economy-storage-chains.md
  - concepts/operator-vision-sh2-personal-clone.md
  - sources/github-stronghold-2-scan-2026-06-13.md
  - entities/tools/stronghold2-mp-ai-patch.md
  - entities/tools/stronghold2-analyse-hub.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/stronghold-modding-ecosystem-shelf.md — **Crusader** mod stack (UCP2 MIT); SH2 has no equivalent community patch
- @sources/github-stronghold-2-scan-2026-06-13.md — raw scan notes

## Raw Concept

GitHub search for **Stronghold 2 (2005 / Steam Edition)** patches, trainers, and format tools. Ecosystem is **tiny vs Crusader** — no MIT “UCP2 for SH2”. Value is **retail play QoL**, **reverse-engineering reference**, and **map fixtures** — not code merge into `castle-sim`.

## Narrative

### Landscape summary [CONFIRMED — GitHub search 2026-06-13]

| Category | Crusader | Stronghold 2 |
|----------|----------|--------------|
| Community balance patch | UCP2 (MIT, active) | **None on GitHub** |
| Engine reimplementation | OpenSHC (GPL, Crusader) | **None** |
| Map format tooling | sourcehold-maps (GPL, **SH1/Crusader `.map` only**) | Eren121 SiegeExporter (`.s2m`, **no license**) |
| Memory / trainer | Many unlicensed | Ald0s, utreah (unlicensed) |
| Licensed patches | — | **MP AI enabler** (MIT, 2 repos) |
| Active RE (2025+) | UCP2 issues | **Stronghold2AnalyseHub** (MIT, DX9 hooks) |

**False positives:** ~40+ repos named `Stronghold2016` are **FRC robotics**, not Firefly.

### Tier 1 — MIT, safe to study / run locally

| Repo | Stars | What it does | Repurpose for clone project |
|------|-------|--------------|----------------------------|
| [Jpnock/Stronghold2-MP-AI](https://github.com/Jpnock/Stronghold2-MP-AI) | 13 | Pattern-scan + NOP **12 bytes** to unlock MP skirmish AI | **Operator QoL:** solo MP vs bots while studying AI; pattern-scan technique for version-tolerant patches → @entities/tools/stronghold2-mp-ai-patch.md |
| [Przodownik/Stronghold2-MP-AI-Patch](https://github.com/Przodownik/Stronghold2-MP-AI-Patch) | 0 | Fork / variant of above | Same |
| [crycodebaby/Stronghold2AnalyseHub](https://github.com/crycodebaby/Stronghold2AnalyseHub) | 1 | MIT DLL: **D3D9 + MinHook + ImGui** overlay, WndProc, logging | **Research harness** while playing retail — pathfinding viz, sim telemetry later; hook patterns reusable in Godot N/A but methodology for “play + instrument” → @entities/tools/stronghold2-analyse-hub.md |

**Proton / Mac note:** [Alleyv2/Stronghold2-AI-Enabler-Proton](https://github.com/Alleyv2/Stronghold2-AI-Enabler-Proton) wraps similar MP-AI memory write for Linux/Proton (`POINTER_OFFSET = 0x00ec5f28`, `ADDRESS_OFFSET = 0xd28`) — **no SPDX license**; treat as reference for CrossOver play only, do not copy code.

### Tier 2 — high analytic value, no license (reference read only)

| Repo | Value | Do not |
|------|-------|--------|
| [Eren121/Stronghold](https://github.com/Eren121/Stronghold) | **SiegeExporter** — Qt/C++ `.s2m` read/write (header + 3 zlib segments); README documents Firefly serialization (little-endian int32, wide strings). **StrongholdEngine** — unit class pointer map (`Archer EB367C`, `Lord EBCC7C`, …). **Instrumentation** — inline ASM patch framework. **Units.CT** — Cheat Engine table. | Merge code; ship prebuilt DLLs; import `.s2m` into public `castle-sim` |
| [Ald0s/Stronghold2-Trainer](https://github.com/Ald0s/Stronghold2-Trainer) | **Player economy struct layout** — offsets for wood→linen, granary foods, weapons, gold, honour (`PlayerUpdate_t` mirrors wiki stockpile/granary/armoury tables). Base offsets: local player `+0x6E7C60`, entity damage hook `+0x385380` (Steam v1.5 era). | Inject trainer in CI; copy hook code into Godot project |
| [utreah/stronghold2ext](https://github.com/utreah/stronghold2ext) | External trainer skeleton (C++) | Same as Ald0s |

#### Economy offset cross-check [TENTATIVE — Ald0s trainer vs wiki]

Trainer `Resources::Basic_e` order matches @concepts/stronghold-2-economy-storage-chains.md stockpile list (trainer labels **Linen** = wiki **Cloth**). Honour at relative `-0xF40` confirms honour is a distinct sim field — aligns with dual-meter design.

### Tier 3 — map fixtures (not code)

| Repo | License | Use |
|------|---------|-----|
| [EBoespflug/stronghold-maps](https://github.com/EBoespflug/stronghold-maps) | **None declared** | Kingmaker `.s2m` maps → `%USERPROFILE%\Documents\Stronghold2\Maps`; playtest estates layout |
| [Stronghold Fandom — S2M format](https://stronghold.fandom.com/wiki/Stronghold_2_S2M_file_format) | Community wiki | Format spec; overlaps Eren121 README |

**Not SH2:** [sourcehold/sourcehold-maps](https://github.com/sourcehold/sourcehold-maps) (GPL-3.0) — **Crusader/SH1 `.map` only**; do not assume `.s2m` parity without Eren121/SiegeExporter.

### Tier 4 — reject / ignore

- FRC `Stronghold2016*` robotics repos
- Minecraft stronghold finders, L5R card game `Stronghold` class, etc.
- Legacy Java **SH2 Map Unlocker** (Stronghold Nation) — broken on modern JRE; no GitHub maintenance

### What SH2 GitHub does **not** provide (build greenfield)

- No open **AI lord personality** files (Crusader has AIV ecosystem)
- No **balance patch** changelog equivalent to UCP2
- No **Godot/Unity reimplementation** of SH2 mechanics
- No licensed **asset pipeline** (Vision Engine `.pak` remains proprietary)

→ Clone mechanics still come from **SH2 Heaven + retail playtest**, with GitHub filling **memory layout**, **map I/O**, and **MP-AI QoL**.

### Recommended operator stack (personal research)

```
Retail SH2 Steam Edition (CrossOver on Mac)
  + MP-AI patch (MIT) or Proton enabler (reference)
  + optional AnalyseHub inject (MIT) for overlay/logging
  + briefs/research/sh2-playsession-checklist.md
  → wiki concepts + castle-sim JSON sim specs
```

### castle-sim repurposing matrix

| GitHub finding | Apply in Godot clone |
|----------------|---------------------|
| Ald0s / Eren121 resource field order | Validate `EconomyState` struct field order in sim tests |
| Eren121 `units_map.txt` | Phase D unit roster IDs → internal enum names (not Firefly offsets) |
| SiegeExporter S2M header keys (`type`, `mapsize`, `maxplayers`) | Future map loader spec if importing user maps |
| Jpnock signature scan | N/A for greenfield; useful if building **companion patcher** for retail |
| AnalyseHub D3D9 hook pattern | N/A; prefer Godot debug overlay |

## Snippets

MP-AI patch core (Jpnock — pattern scan, NOP 12 bytes):

```cpp
int iAddrToNOP = pMemoryExt.FindPatternMainModule(szMPAIFuncSig, szMPAIFuncMask);
pMemoryExt.NOPBytes((LPVOID)iAddrToNOP, 12);
```

S2M on-disk layout (Eren121 README):

```
header → zlib segment1 (events) → zlib segment2 (terrain) → zlib segment3 (units)
```

## Dead Ends

- **Waiting for “SH2 UCP2”** — does not exist; Crusader tooling does not transfer cleanly (3D Vision engine, different binary)
- **Importing Eren121 SiegeExporter into castle-sim** — no license; reimplement `.s2m` subset if ever needed
- **Trainer offsets as permanent API** — Steam EXE updates break absolute offsets; use for validation only
- **sourcehold-maps for SH2** — wrong game format
