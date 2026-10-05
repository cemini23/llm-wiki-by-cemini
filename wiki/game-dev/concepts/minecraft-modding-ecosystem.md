---
title: Minecraft modding ecosystem — Java and Bedrock (2026)
type: concept
tags: [concept, minecraft, modding, ecosystem, reference, tooling]
keywords: [minecraft, neoforge, fabric, bedrock, addons, modrinth, version-churn, deobfuscation]
related:
  - concepts/minecraft-bedrock-addons-scripting.md
  - concepts/minecraft-data-driven-content-patterns.md
  - concepts/minecraft-agent-harness-shelf.md
  - entities/tools/blockbench.md
  - sources/minecraft-modding-deep-research-2026-10-05.md
  - sources/minecraft-social-scan-2026-10-05.md
  - entities/projects/castle-sim.md
  - concepts/scope-tiers.md
maturity: validated
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- @concepts/minecraft-bedrock-addons-scripting.md — Bedrock deep dive
- @concepts/minecraft-data-driven-content-patterns.md — the reusable design patterns
- @concepts/minecraft-agent-harness-shelf.md — AI agents in Minecraft
- @entities/projects/castle-sim.md — the consumer of these lessons

## Raw Concept

Reference on the Minecraft modding ecosystem in 2026, both editions. Purpose is not to mod Minecraft, but to study the largest long-lived modding ecosystem in games for lessons on modder-facing APIs, data-driven content, community infrastructure, and version churn. [CONFIRMED]

## Narrative

### Why this is in scope

Castle-sim is a Stronghold-2-style builder. Minecraft's core loop — place blocks, assemble structures, build a settlement — is the closest mass-market analogue to castle building. More useful: Minecraft has run a modding API for over a decade, across a whole-edition engine change, and its failures are well documented. That is a free lesson set. [TENTATIVE — analogy, not measured transfer]

### Java Edition — loaders

| Loader | Maintainer | 2026 status | Approach | Current line |
|--------|-----------|-------------|----------|--------------|
| **NeoForge** | NeoForged team | Active; promoted successor to Forge | Patches (NeoForm) + Mixin | `26.1.0.1-beta`+ |
| **Forge** | LexManos et al. | Active but legacy | Patches + Mixin | `1.21.10-60.0.3` |
| **Fabric** | FabricMC | Active; the lightweight default | Mixins + Fabric API | For MC 26.1 |
| **Quilt** | QuiltMC | Declining | Mixins + Quilt API | Fabric-compatible |

**The Forge→NeoForge fork** happened on 2023-07-12. Almost the entire Forge team moved; LexManos stayed. NeoForge's own retrospective gives two reasons: disagreement between the triage team and management, and a wish to refactor internals that Forge's "strict stances against changes" blocked. Forge is **not dead** — it still ships patch releases — but it is the legacy lane. [CONFIRMED — neoforged.net retrospective]

**Quilt's decline** is the cautionary tale. Its Quilt Standard Libraries were discontinued in **December 2025**: the maintainers said keeping Fabric API compatibility while tracking Minecraft releases was too costly. A loader fork that stays compatible with its parent inherits the parent's churn plus its own. [CONFIRMED]

### Java Edition — the deobfuscation break

The single most important 2026 event. Mojang announced on **2025-10-31** that Java Edition drops obfuscation after the *Mounts of Mayhem* (1.21.11) release. Consequences, as Fabric stated them: [CONFIRMED — fabricmc.net/2025/10/31/obfuscation.html]

- The game ships Mojang's official names at runtime.
- **Yarn is deprecated** ("we can't see a way to justify maintaining Yarn in its current state").
- **Intermediary will no longer exist.**
- Method parameter and local variable names become visible for the first time.
- Fabric API needs no major rewrite; Loom gains a new mode.

Result: **no mod compiled for 1.21.11 or earlier works on 26.1 without at least recompilation.** A whole-ecosystem break in one release. [CONFIRMED — fabricmc.net/2026/03/14/261.html]

**The lesson.** Mojang took roughly sixteen years to ship a stable, documented, unobfuscated target. Every year before that, the modding ecosystem paid a porting tax on every release. If castle-sim ever exposes a mod or script API, unobfuscated, versioned, documented names from day one is the single highest-leverage decision. [TENTATIVE — design recommendation]

### Version churn — the real cost

- One developer reports the 1.21.4 port took about a week, and they now maintain **six Minecraft versions in parallel**. Minecraft's data-generation code had been rewritten so heavily since 1.21.1 that they relearned it "from scratch." [CONFIRMED — bokmcdok.com]
- Third-party porting commissions run roughly **$30–$500** per port — a rough proxy for effort.
- The community response is **version-gating**: modders pick a stable "LTS" target (1.21.1, likely 26.1) and sit on it. Loader teams gate the whole ecosystem, because modders wait for a stable loader release before porting.

### Distribution

| Platform | Model | Java | Bedrock | Notable |
|----------|-------|------|---------|---------|
| **Modrinth** | Open source, open API | Yes | No | 300 req/min, PAT + OAuth2, 75/25 creator split |
| **CurseForge** | Closed, gated API | Yes | Yes | Largest catalog; 2022 API change let authors block third-party launchers |
| **Minecraft Marketplace** | Official, paid | No | Yes | 70/30 split, Partner Program gate |

Modrinth is the developer-friendly default for new Java mods; CurseForge remains larger and is the only major channel covering Bedrock. Many authors publish to both. [CONFIRMED]

### Community hubs

- **r/feedthebeast** — modpack and mod discussion, the largest player-facing hub.
- **r/MinecraftCommands** — datapack and command-technical help.
- **FabricMC Discord**, **NeoForged Discord** — the primary developer help channels. NeoForge has openly asked for more maintainer help.
- **Modrinth Discord** — platform and API support.

### Bedrock Edition in one paragraph

Bedrock has no arbitrary code mods. "Modding" means **add-ons**: JSON behavior packs and resource packs, optionally driven by a sandboxed **JavaScript Script API** (`@minecraft/*`, running on QuickJS). It has a first-class in-game **Editor**, an official **Marketplace**, and roughly 78% of players by fan estimate. Full detail: @concepts/minecraft-bedrock-addons-scripting.md.

### What castle-sim should take

| Minecraft practice | castle-sim action |
|-------------------|-------------------|
| Unobfuscated, versioned, documented API | If a mod API ever ships, do this from day one |
| Typed, default-valued data components | Use for entity/item data instead of loose dicts — @concepts/minecraft-data-driven-content-patterns.md |
| Build-time content generation (datagen) | Generate balance tables and content from code |
| Namespaced content + explicit load order | Namespace castle-sim content registries |
| Version-gated LTS target | Pin the Godot version; do not chase every release |
| Loader forks fragment the ecosystem | One supported path beats two half-supported ones |

### Art pipeline note

Blockbench (GPL-3.0, active) is the community's 3D model and animation editor, and it serves both editions through a format-module system. For castle-sim Fork B (Godot 3D) it is a real candidate for buildings and props, and the format-registry pattern is worth copying. See @entities/tools/blockbench.md. Cross-wiki: 3D asset technique belongs to @image-gen-wiki.

## Snippets

```
Minecraft versioning, 2026: product releases use "26.x"; JSON and the Script API
still use 1.26.xx.yyz internally.
```

## Dead Ends

- Treating Minecraft as a target platform for castle-sim. It is a reference ecosystem.
- Assuming "Forge is dead" — its changelog shows active releases. It is legacy, not dead.
- Copying Java's Mixin approach into a Godot game. GDScript has no bytecode weaving layer; the transferable part is the data and API design, not the patching.
