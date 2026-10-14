---
title: Blockbench — low-poly 3D model and animation editor
type: entity
tags: [entity, tool, art, 3d, modeling, phase-0]
keywords: [blockbench, voxel-modeling, gpl-3.0, gltf, plugin-api, format-registry]
related:
  - concepts/minecraft-modding-ecosystem.md
  - concepts/minecraft-bedrock-addons-scripting.md
  - concepts/art-pipeline-v0-requirements.md
  - concepts/godot-3d-sh2-architect-spike-plan.md
  - entities/projects/castle-sim.md
  - sources/k283-bedrock-addon-extracts-2026-10-06.md
maturity: validated
created: 2026-10-05
updated: 2026-10-05
wire_status: deferred
wire_target: concepts/art-pipeline-v0-requirements.md
---

## Relations

- Site: [blockbench.net](https://www.blockbench.net/)
- Source: [JannisX11/blockbench](https://github.com/JannisX11/blockbench)
- Cross-wiki: 3D asset technique → @image-gen-wiki

## Raw Concept

Free, open-source low-poly 3D model and animation editor. It is the Minecraft community's standard asset tool and an official tool of Mojang. It serves Java and Bedrock through a **format-module system**, and it has a plugin store. [CONFIRMED]

## Narrative

### Phase-0 verdict (2026-10-05)

| Check | Result |
|-------|--------|
| SPDX / LICENSE | **GPL-3.0** |
| Maturity | Active; ~6.0k stars; official tool of Mojang, Hytale, Noxcrew |
| Latest release | v5.2.1 (2026-09-21) |
| Verdict | **CONDITIONAL-GO** — usable for castle-sim art; **not adopted yet** |

GPL-3.0 applies to the tool, not to assets you create with it. Using Blockbench to author models imposes no licence obligation on the exported art. [TENTATIVE — standard reading; confirm before commercial use]

### Formats and export

Eight format projects: Java Block/Item, Bedrock Model, Bedrock Legacy, Modded Entity, OptiFine Entity, OptiFine Part, Generic Model, GeckoLib Model. Export targets include `.json`, `.java`/`.jem`/`.jpm`, **`.obj`**, **`.gltf`**, and `.bbmodel` (native). A built-in plugin store adds tools, formats, and generators. Java models cap at 3×3×3; other formats are unlimited. Only Bedrock formats use Molang animation. [CONFIRMED — blockbench.net/wiki]

`.gltf` export is what matters for Godot 3D. [TENTATIVE — Godot imports glTF natively]

### Why it is interesting beyond the assets

Blockbench's architecture is a small editor with **a plugin API and a central format registry**: one tool, one UI, many output targets, each implemented as a format module. That is a good model for a data-driven asset pipeline, and it is the same shape as the data-component pattern in @concepts/minecraft-data-driven-content-patterns.md. [TENTATIVE — design reading]

### castle-sim fit (Fork B, Godot 3D)

Relevant to @concepts/godot-3d-sh2-architect-spike-plan.md. Buildings, walls, towers, and props are low-poly modular pieces — exactly Blockbench's strength. Two caveats: it is a box-modeling tool, so organic shapes and high-detail terrain are out of scope, and the Java 3×3×3 cap does not apply to the generic formats, so use a generic or glTF format for larger structures. [TENTATIVE]

## Dead Ends

- Using Blockbench for terrain or organic sculpts. It is a box and low-poly modeler.
- Assuming the GPL covers exported assets. It covers the editor.
- Adopting before the art milestone starts. It is deferred, not rejected.
