---
title: "Project stack revenue evaluation — 20 rows: level editors, modding infra, Bedrock tooling (2026-10-05)"
type: source
tags: [source, k282, basgiath, minecraft, eval, level-editors, ccc]
keywords: [k282, bedrock, mcpedl, curseforge, level-editor, packaging, extract, vibespace, universal-modder]
related:
  - concepts/k282-level-editors-wave.md
  - concepts/k281-basgiath-wave.md
  - concepts/active-project-research-routing.md
maturity: draft
created: 2026-10-05
updated: 2026-10-05
read_status: read
---

## Relations

- @concepts/k282-level-editors-wave.md
- @concepts/k281-basgiath-wave.md
- @concepts/active-project-research-routing.md

## Raw Concept

| File | `Project Stack Revenue Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Project Stack Revenue Evaluation.docx` |
| Retrieved | 2026-10-05 |
| Dual-ID | **OSINT K282** |
| Batch theme | Level editors, modding infrastructure, agent workspaces, and Minecraft Bedrock tooling |
| Rows | 20 URLs |
| sha256 | `a8c61a2b13d04a32…` |

## Narrative

A 20-row eval batch. The theme is wide: 2D level editors, modding infrastructure, agent workspaces, and Bedrock add-on tooling. The eval ran the v10.7 prompt, so `basgiath overlap` is scored.

### Tier spread

| Tier | Count |
|------|-------|
| Integrate | 0 |
| Extract | 3 |
| Context | 4 |
| Pass | 7 |
| UNAVAILABLE | 6 |

**Zero product Integrate.** The three Extract rows are the only actionable items, and two of them are Basgiath-facing.

### The Extract rows

| URL | Technique | Route |
|-----|-----------|-------|
| `ProblemFactory/vibespace` | Multi-agent CLI orchestration with **detachable background workers** (`vibespace-job`), long-task cron, telemetry reconnects across daemon restarts | CCC harness |
| `rehan-remade/universal-modder` | Claude Code modding skill tree (free — adopt) + **fal MCP** generative asset pipeline (**paid — rejected**) + in-game agent verification + promo-clip generation | Basgiath + CCC |
| `xentropaff` Bedrock add-on guide | **Manifest.json UUID pairing**, behavior-pack / resource-pack split, `.mcaddon` packaging for one-click import | Basgiath packaging |

**The Basgiath pair is the headline.** The packaging guide closes a real churn source: a manifest UUID mismatch breaks the Bedrock import dialog and the player leaves. The `universal-modder` layout was already named in K281 — this batch scores it `basgiath overlap 0.75`. Its **fal MCP asset pipeline is rejected: it is paid, and we will not pay.** Extract the free layout and the asset-iteration loop only.

### The Context rows

- `mapeditor/tiled` — canonical TMX/JSON 2D tilemap schema (the 2D reference; Basgiath is 3D voxel, so Context only).
- `Sprytile/Sprytile` — Blender low-poly UV-paint workflow; Bedrock standardises on Blockbench, so Context.
- `mateoltd/axial` — Rust Minecraft client launcher with memory tuning and integrity checks (Java/desktop; Basgiath ships `.mcworld`/`.mcaddon`).
- `cidwel/better-tile-editor` — Godot 4.6+ autotile / multi-tile stamping algorithms.

### What was rejected

Seven Pass rows are legacy or stack-mismatched (Tiled2Unity, Unity TileEditor, rs-tiled, godot-tiled-importer, HexTiles, `FabricModdingConventions`, Bonesmith). **`FabricModdingConventions` is Java Fabric — it cannot compile to the Bedrock runtime**, so its headless GameTest pattern does not transfer even though the goal matches.

### Eval-quality warning

**6 of 20 URLs return HTTP 404** — including three "`*-Community-2026`" repos that read as generated, not real. That is the second batch in two days with a high dead-link rate (K281 had 7 of 20). Treat per-row star counts and claims as leads, not verified findings.

### Boundary

**Zero clones. No install. Nothing vendored. 0 product Integrate GO.** The Bedrock client-modification rows were Pass and nothing from them is recorded. Basgiath stays a free, non-monetized fan project: no Minecraft Marketplace, no official art or book text, clear "fan-made" labelling.

### Distribution

- Basgiath rows → `Projects/dragon-rider-map/briefs/2026-10-05_k282-basgiath-packaging.md`
- CCC harness row → `Cemini claude code CCC/briefs/2026-10-05_k282-ccc-harness.md`
- Level-editor / tile rows (11) → Game Dev wiki `briefs/2026-10-05_k282-level-editors-from-osint.md`
- `universal-modder` was already ingested in K281 (@sources/universal-modder-2026-10-04.md) — this wave adds its `basgiath overlap 0.75` score. Its fal MCP pipeline is **rejected (paid; we will not pay)**.

## Snippets

> "Extract Background daemon session persistence and task-detaching mechanics into the central agent runner, enabling uninterrupted multi-hour genealogical deep-link verification and market alert scraping runs." [Source: Project Stack Revenue Evaluation.docx]

> "Basgiath's success relies entirely on fan reach and smooth player onboarding on CurseForge and MCPEDL. Packaging mistakes or manifest UUID mismatches break Bedrock import dialogs, leading to immediate player churn." [Source: Project Stack Revenue Evaluation.docx]

> "Because Java Fabric conventions cannot execute within or compile to Bedrock runtimes, the project is scored Pass." [Source: Project Stack Revenue Evaluation.docx]

> "6 of 20 URLs return HTTP 404." [Source: Project Stack Revenue Evaluation.docx, derived from row tiers]
