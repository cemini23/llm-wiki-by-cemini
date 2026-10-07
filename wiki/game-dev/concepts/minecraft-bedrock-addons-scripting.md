---
title: Minecraft Bedrock add-ons and the Script API (2026)
type: concept
tags: [concept, minecraft, bedrock, modding, scripting, reference]
keywords: [bedrock, addons, behavior-pack, script-api, minecraft-server, blockbench, marketplace]
related:
  - concepts/minecraft-modding-ecosystem.md
  - concepts/minecraft-data-driven-content-patterns.md
  - entities/tools/blockbench.md
  - sources/minecraft-modding-deep-research-2026-10-05.md
  - entities/projects/castle-sim.md
  - sources/k283-bedrock-addon-extracts-2026-10-06.md
maturity: validated
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- @concepts/minecraft-modding-ecosystem.md — the hub; Java and Bedrock compared
- @concepts/minecraft-data-driven-content-patterns.md — the JSON and manifest patterns
- @entities/tools/blockbench.md — the shared asset tool

## Raw Concept

Deep reference on Bedrock Edition add-ons: the pack model, the JavaScript Script API, the official Editor, the tool ecosystem, and the Marketplace. Bedrock is the interesting case because it is a **closed, cross-platform engine that added a sandboxed scripting layer** rather than opening the code. [CONFIRMED]

## Narrative

### Add-on anatomy

Bedrock has no arbitrary code execution. Content is declared in JSON. A **pack** is one of several types: a **Behavior Pack** (game logic, module type `data`), a **Resource Pack** (textures, models, sounds, UI, module type `resources`), a skin pack, or a world template. An **add-on** bundles a behavior pack with a resource pack. [CONFIRMED — MicrosoftDocs]

Every pack has a `manifest.json` at root, typed `minecraft:packmanifestdocument`. Its fields: `format_version`, `header`, `modules`, `dependencies`, `capabilities`, `subpacks`, `metadata`. The `header` carries `name`, `description`, `uuid`, `version`, `min_engine_version`, `base_game_version`. Each entry in `modules` has a `type` (`data`, `resources`, or `script`), a `uuid`, and a `version`; script modules add `entry` (file path) and `language` (`javascript`). [CONFIRMED]

`capabilities` is a string array. Two values matter: **`script_eval`** (enables `eval()` and `Function()`) and **`editorExtension`** (for Editor worlds). [CONFIRMED]

Distribution file types: **`.mcpack`** (one zipped pack), **`.mcaddon`** (a zip of packs — the common form), **`.mcworld`**, **`.mctemplate`**, **`.mcproject`** (Editor only). [CONFIRMED]

### The Script API

The `@minecraft/*` JavaScript API is Bedrock's closest thing to real code modding. It runs on a customized **QuickJS** engine with ECMAScript modules, server-side. [CONFIRMED]

| Module | Role | Status |
|--------|------|--------|
| `@minecraft/server` | World, entities, blocks, items, events | **Stable** |
| `@minecraft/server-ui` | Forms and dialogs to players | **Stable** |
| `@minecraft/common` | Error classes, shared interfaces | **Stable** |
| `@minecraft/server-admin` | Secrets and variables from admin JSON | **Beta**, BDS only |
| `@minecraft/server-net` | HTTP requests | **Beta**, BDS only |
| `@minecraft/server-gametest` | Automated testing | **Beta** |
| `@minecraft/debug-utilities`, `server-editor`, `server-graphics` | Debug, Editor, graphics | **Beta** |

**Versioning.** Three tracks: stable, beta, and internal. Stable versions are backward-compatible within a major line. **Beta does not follow semver** — any increment may remove methods — and requires the **"Beta APIs"** experiment toggle. `@minecraft/server` bumps roughly once per Minecraft minor release: `1.11.0` at 1.21.0, `1.17.0` at 1.21.60, `2.5.0` at 1.26.0. [CONFIRMED — MicrosoftDocs versioning page]

**Limits.** No `setTimeout` or `setInterval` — scripts use `system.runTimeout` and `system.runInterval` at one-tick precision. Scripts are server-side only. `server-admin` and `server-net` exist only on the Bedrock Dedicated Server. `eval()` needs the `script_eval` capability. [CONFIRMED — wiki.bedrock.dev]

**The design lesson.** This is a capability-sandbox: the platform exposes a curated set of modules, a versioned surface, and an explicit opt-in for dangerous features. That is the model for a game that wants scripting without handing over the process. [TENTATIVE — design reading]

### Official tooling

The **Bedrock Editor** is an in-game, scriptable world editor. It previewed in March 2023, went stable on 2024-12-03, is Windows-only, and launches via `minecraft://creator/?Editor=true`. It uses `@minecraft/server-editor` and the `editorExtension` capability. Microsoft publishes vanilla add-on samples and starter templates, and the Launcher has a **Creator Tools** tab. [CONFIRMED]

### Community tools

| Tool | Purpose | Maintenance (2026) |
|------|---------|-------------------|
| **Blockbench** | 3D models, textures, animations | Active — v5.2.1 |
| **bridge.** | Add-on IDE (compiler, previews, Molang) | Active — standalone app v2.7.54 |
| **MCreator** | Visual generator; Java mods and Bedrock add-ons | Active — GPL-3.0 |
| **Snowstorm** | Particle editor (web + VS Code) | Active — v3.2.1 |
| **Amethyst** | Native C++ client-side Bedrock modding | Partial — open in 1.21.x, partly closed in 1.26.x |
| **Blockception VSCode extension** | VS Code schemas and Molang | **Archived 2025-09-28** |

Two notable shifts: **bridge. left VS Code** to become a standalone app, and the **Blockception VS Code extension was archived** — the editor-integration lane consolidated. [CONFIRMED]

### Distribution and economics

- **Minecraft Marketplace** — the only paid channel. Entry goes through the **Partner Program**: 18+, a registered business, and roughly 3+ polished original packs. Application review takes 2–12 weeks; each item is reviewed again for 1–2 weeks. Creators keep **70%**. Payouts are quarterly with a **$200** minimum. Sales use **Minecoins**. [CONFIRMED for the 70/30 split and process; Minecoin pricing is third-party and lower confidence]
- **MCPEDL** — free, community-run hosting with manual file checks.
- **CurseForge** — free hosting; lists Bedrock add-ons alongside Java.

### Java versus Bedrock capability gap

| | Java | Bedrock |
|---|------|---------|
| Code mods | Arbitrary JVM code | Sandboxed Script API only |
| Custom shaders / fonts | Yes | **No** |
| Custom particles and fog | Limited | **Yes** |
| Redstone | Quasi-connectivity | Different behavior |
| World format | Anvil | LevelDB |
| Players (fan estimate) | ~22% | ~78% |
| Community | Larger, code-centric | Younger, JSON/Marketplace-centric |

The Script API exists precisely because Bedrock is closed and cross-platform — it is the minimum code surface the platform could safely expose. [TENTATIVE — interpretation]

### Version churn on Bedrock

Stable `@minecraft/server` takes a major bump roughly each Minecraft minor release, so stable packs need periodic migration. Beta APIs break at any increment and need the **Beta APIs** toggle. Since 2026, product versions use "26.x" while JSON and APIs still use `1.26.xx.yyz`. [CONFIRMED]

## Dead Ends

- Writing client-side Bedrock mods. The Script API is server-side; Amethyst is the only native client path and it is partly closed.
- Assuming a stable `@minecraft/server` dependency is permanently stable. A major bump per minor release makes periodic migration normal.
- Treating Marketplace revenue as accessible. The Partner Program gate is real and the review is manual.
