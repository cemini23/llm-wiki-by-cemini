---
title: K282 Project Stack Wave (Oct 2026)
type: concept
tags: [k282, level-editors, modding, basgiath, minecraft, ccc, eval]
keywords: [k282, tiled, sprytile, vibespace, universal-modder, bedrock-packaging, mcpedl, curseforge]
related:
  - concepts/k281-basgiath-wave.md
  - concepts/k282-agent-eval-wave.md
  - concepts/k282-feeds-wave.md
  - concepts/active-project-research-routing.md
  - sources/eval-project-stack-revenue-2026-10-05.md
  - concepts/k283-eval-wave.md
  - entities/tools/bedrock-ui-animations.md
  - entities/tools/mc-mod-migrator.md
  - sources/eval-bedrock-ecosystem-2026-10-06.md
maturity: draft
created: 2026-10-05
updated: 2026-10-25
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k281-basgiath-wave.md
- @concepts/k282-agent-eval-wave.md
- @concepts/k282-feeds-wave.md
- @concepts/active-project-research-routing.md
- @sources/eval-project-stack-revenue-2026-10-05.md

## Raw Concept

K282 cluster hub. One eval docx, 20 URLs. Dual-ID **OSINT K282**.

## Narrative

**Batch theme: level editors, modding infrastructure, agent workspaces, and Minecraft Bedrock tooling.** The eval ran the v10.7 prompt, so `basgiath overlap` is scored on every row.

### Tier spread

| Tier | Count |
|------|-------|
| Integrate | 0 |
| Extract | 3 |
| Context | 4 |
| Pass | 7 |
| UNAVAILABLE | 6 |

**0 product Integrate GO. Zero clones. No install.**

### The three Extract rows

**1. Bedrock add-on packaging (Basgiath).** The `xentropaff` guide scores `basgiath overlap 0.85` — the highest of the wave. It names the exact failure mode: a **manifest.json UUID mismatch breaks the Bedrock import dialog**, and the player churns before they see the world. The fix is mechanical — Behavior Pack and Resource Pack split, matched UUID pairs, one-click `.mcaddon`. This is the distribution analogue of the K281 test-bench idea: it removes a manual, error-prone step.

**2. `rehan-remade/universal-modder` (Basgiath + CCC).** Scored `0.75`. Already named in K281 for its skill layout; this wave adds the **fal MCP generative asset pipeline** (textures, sound, promo clips). Its layout is the one to copy. **Operator decision (2026-10-05): do not adopt the pipeline — it is a paid third-party service and we will not pay for it.** Extract the free layout and the asset-iteration loop only.

**3. `ProblemFactory/vibespace` (CCC).** Scored `local-abliterated-lab 0.45`, `atto 0.35`. A multi-agent CLI orchestrator with **detachable background workers** that survive daemon restarts, long-task cron, and tiled views. The gap it closes: our harness has no native background session detachment for multi-hour batch jobs.

### The Context rows

`mapeditor/tiled` (canonical 2D tilemap schema), `Sprytile/Sprytile` (Blender low-poly UV paint), `mateoltd/axial` (Rust client launcher), `cidwel/better-tile-editor` (Godot 4.6+ autotile). All game-dev reference; none touches a revenue project. Basgiath is a 3D voxel Bedrock target, so 2D tile tooling is Context at most.

### What was rejected

Seven Pass rows: five obsolete 2D/engine tools, one irrelevant 2D rigging tool, and **`brainage04/FabricModdingConventions`**. That last one is the instructive Pass — it *does* the thing Basgiath wants (headless GameTest regression CI for Minecraft entities), but it is **Java Fabric**, and Java Fabric cannot compile to the Bedrock runtime. **Goal match, stack mismatch.** The Bedrock equivalent would need `@minecraft/server` scripting and GameTest in Bedrock's own harness.

### Eval-quality warning

**6 of 20 URLs return 404**, including three "`*-Community-2026`" repos. That is the second wave in two days with a high dead-link rate (K281: 7 of 20). The eval's URL lists are partly generated. Score the technique it names; do not trust its per-row metrics.

### Boundary

No client-modification code recorded. Non-monetized fan project. **0 product Integrate GO.**
