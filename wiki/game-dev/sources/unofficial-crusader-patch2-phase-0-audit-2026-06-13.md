---
title: UnofficialCrusaderPatch2 Phase-0 audit — 2026-06-13
type: source
tags: [source, phase-0, stronghold, modding, audit]
keywords: [ucp2, stronghold, crusader, aiv]
related:
  - entities/tools/unofficial-crusader-patch2.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - entities/games/stronghold-series.md
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
read_status: read
source_type: operator-audit
source_url: https://github.com/UnofficialCrusaderPatch/UnofficialCrusaderPatch2
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Raw Concept

Phase-0 audit of **UnofficialCrusaderPatch2** — MIT community patcher for Stronghold Crusader 1 (design archaeology, not runtime dependency).

## Narrative

### Method

Clone @ main (2024-10-06) to `/tmp/phase0-audit/UnofficialCrusaderPatch2`. Inventory solution layout, `SHC_AIV/`, README, LICENSE.

### Checks

| Gate | Result |
|------|--------|
| License | **MIT** [CONFIRMED — LICENSE file] |
| Maturity | ~435★; active Discord/issues; UCP3 released on sibling repo — **v2 repo still valid for AIV study** |
| Stack | C++ patcher (GUI + console), binary hooking against **retail Crusader exe** |
| Content | Community AIV castles in `SHC_AIV/`; does **not** ship Firefly binaries |
| castle-sim fit | **NO-GO** runtime — greenfield Godot; **GO** design reference for AI village layouts + balance changelogs |
| IP risk | Do not redistribute Firefly assets; MIT covers studying patch **methodology** only |

### Steal value

| Extract | Skip |
|---------|------|
| AIV parameter categories (economic vs military weights) | Binary patch installer |
| Issue threads on pathfinding/AI behavior | Memory hook C++ into retail game |
| Balance rationale in patch notes | Importing `.aiv` binaries into castle-sim |

### Verdict

**STEAL-FROM / NO-GO install** — wiki + `briefs/systems/aiv-design-notes.md` only. Cross-link @cybersecurity-wiki for hooking case study.

## Snippets

UCP3 note: newer releases at `UnofficialCrusaderPatch/UnofficialCrusaderPatch` — track for balance docs; v2 repo sufficient for AIV folder survey at audit time.
