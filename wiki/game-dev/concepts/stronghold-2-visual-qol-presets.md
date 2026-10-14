---
title: Stronghold 2 — visual & comfort QoL presets
type: concept
tags: [concept, stronghold-2, modding, graphics, qol]
keywords: [visual, hd, enb, matteele, winter, presets, comfort]
related:
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - concepts/art-pipeline-v0-requirements.md
  - concepts/operator-vision-sh2-personal-clone.md
  - sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md
  - sources/sh2-nevikov-new-balance-sheet-2026-06-18.md
  - concepts/art-pipeline-v0-requirements.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @concepts/stronghold-2-mod-ecosystem-shelf.md — full mod catalog + mechanics QoL
- @concepts/art-pipeline-v0-requirements.md — Godot art bar; presets inform Phase C targets
- `castle-sim/data/sh2/graphics_presets.json` — machine-readable preset stubs

## Raw Concept

**Visual mods are player QoL.** HD packs, ENB, and biome total conversions reduce eye strain, improve readability, and extend session comfort — same operator value as mechanics patches. castle-sim should ship **in-engine graphics presets** that reproduce mod *intent* without importing Firefly/modder binaries.

## Narrative

### Why visual = QoL [CONFIRMED — operator framing]

| Pain on retail SH2 | Popular mod fix | Comfort outcome |
|--------------------|-----------------|-----------------|
| Soft/blurry 2005 textures | [HD Reworked 5.0](https://www.nexusmods.com/stronghold2/mods/5) | Sharper walls/units; less shimmer |
| Washed-out daylight | [ENB / SH2 Lighting](https://www.nexusmods.com/stronghold2/mods/6) | Contrast + bloom; easier depth read |
| Same biome fatigue | [Matteele Crusader Edition](https://www.moddb.com/mods/stronghold-2-crusader-matteele-edition) | Desert palette + crusader audio variety |
| Seasonal novelty | ModDB Winter mod | Snow readability + mood |
| Pixel nostalgia | Matteele Pixel mod | High-contrast silhouettes |

Nexus top-4 mods are **all visual** — validates demand even when mechanics unchanged.

### Preset catalog → Godot implementation

| Preset ID | Mod inspiration | Godot target |
|-----------|-----------------|--------------|
| `retail_steam` | Official 2017 refresh | Default PBR + widescreen UI |
| `enhanced_hd` | Nexus HD Reworked / Enhanced Graphics | 2× texture budget; UI sharpen; `@image-gen-wiki` upscales |
| `cinematic_enb` | ENB + ModDB Lighting | Post-FX: AO, bloom, ground-biased shadows, cooler grade |
| `matteele_desert_crusader` | Matteele TC | Warm color grade; desert biome pack; optional SHC-style VO |
| `winter_seasonal` | Winter mod | Cool grade; snow terrain shader |
| `pixel_retro` | Pixel mod showcase | Optional pixelate filter for readability/accessibility |

**Legal boundary:** presets describe **rendering parameters + biome flags** — never ship Nexus/ModDB texture files in public repo. Operator may use mods locally for screenshot parity.

### Retail visual mod install notes

```
Steam Edition + HD pack: expect longer load; Large Address Aware sometimes required (Gigachad HD comments)
ENB: disable MSI Afterburner; may need Stronghold2.GraphicsSettings.xml tweaks
Matteele / legacy mods: NEVER blind-copy fx/ — restore vanilla fx first
```

### Settings UX (castle-sim)

- Main menu: **Graphics preset** dropdown (above advanced toggles)
- Advanced overrides per preset: shadows, bloom, biome, audio pack
- Persist to `user://settings.cfg`; default `retail_steam`

### Art pipeline hook

When Phase C replaces placeholders:

1. Author **temperate** baseline albedo set (retail parity)
2. Fork **desert** + **winter** biome variants (Matteele / Winter mod references)
3. Run optional 2× upscale pass via @image-gen-wiki for `enhanced_hd` preset

## Snippets

Graphics preset shape in `castle-sim`:

```json
"rendering": {
  "upscale_textures": true,
  "post_process": "light_sharpen",
  "bloom": false,
  "ambient_occlusion": false,
  "color_grade": "neutral_clarity"
}
```

## Dead Ends

- Bundling Nexus 405 MB HD Reworked in git — use preset + operator-local mod for reference captures only
- RTX Remix / Reshade dependency in castle-sim — implement native Godot Environment + compositor
