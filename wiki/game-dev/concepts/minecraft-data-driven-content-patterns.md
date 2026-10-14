---
title: Minecraft data-driven content patterns — what castle-sim should copy
type: concept
tags: [concept, minecraft, data-driven, architecture, patterns, castle-sim]
keywords: [data-components, datapack, datagen, worldgen, loot-tables, registries, godot]
related:
  - concepts/minecraft-modding-ecosystem.md
  - concepts/minecraft-bedrock-addons-scripting.md
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-2-production-buildings.md
  - entities/projects/castle-sim.md
  - sources/minecraft-modding-deep-research-2026-10-05.md
  - sources/k282-level-editors-tile-tooling-2026-10-05.md
  - sources/arxiv-2610.02023-sphere-vr-scene-routing-2026-10-06.md
maturity: validated
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- @concepts/stronghold-2-production-buildings.md — the balance tables this pattern would hold
- @concepts/minecraft-modding-ecosystem.md — the parent ecosystem page

## Raw Concept

The reusable engineering ideas from Minecraft's data layer, translated for a Godot castle-sim. Minecraft has iterated on data-driven content for a decade and made a specific, well-documented correction in 1.20.5. That correction is worth copying directly. [CONFIRMED]

## Narrative

### Pattern 1 — typed, default-valued data components

**What Minecraft did.** Before 1.20.5, item data lived in **free-form NBT**: an untyped dictionary. In **1.20.5+** Mojang replaced that with **typed, registry-backed data components** — namespaced IDs with a schema, a default, and a fixed attachment point. [CONFIRMED — minecraft.wiki]

Three properties make it work:

1. Each component has a **registered ID and a schema** — so it can be validated.
2. Each has a **default**, so stored data stays minimal; defaults are not saved per item.
3. Components attach to a **fixed item type**, not to arbitrary tags.

Command syntax became `item_id[component=value,...]`; a `!` prefix removes a component. Examples: `custom_name`, `damage`, `enchantments`, `food`, `container`, `attack_range`. [CONFIRMED]

**Why castle-sim should copy it.** The current design carries Stronghold-2 balance data in JSON tables (see @concepts/stronghold-2-production-buildings.md). A component model would give: schema validation at load, defaults that shrink save files, and a typed place to hang new behaviour without a loose dictionary. For a Godot project, the natural analogue is a `Resource` class per component with exported defaults, composed onto building and unit definitions. [TENTATIVE — design recommendation, unbuilt]

### Pattern 2 — build-time content generation (datagen)

Fabric Loom's **datagen** generates recipes, loot tables, tags, and models **as code at build time**. The JSON is a build output, not a hand-maintained file. [CONFIRMED — docs.fabricmc.net]

**Why it matters.** Hand-written balance tables drift from the systems that read them. Generating them means one source of truth, and a validation step that runs in CI. For castle-sim, the Stronghold-2 cost tables could be generated from a typed data source and diffed on every build.

The strong form of this, and the one this wiki should remember: **the data file is a build artifact**. Review happens on the source, not the output.

### Pattern 3 — namespacing and explicit load order

A datapack is a folder with `pack.mcmeta`, organised under `data/<namespace>/`. Namespaces prevent collisions between packs. Load order is explicit, and a duplicate file in a later pack **overrides** the earlier one. Tags **merge** unless they set `"replace": true`. [CONFIRMED — minecraft.wiki]

**Why it matters.** Override and merge are the two operations a content system needs, and they need different defaults: replace for definitions, merge for sets. Castle-sim's mod-facing content, if it ever exists, wants the same split.

### Pattern 4 — namespaced registries as the extension point

Blocks, items, and entities are added through **registries** — the canonical extension point. Content is addressed by namespaced ID, never by array index. [CONFIRMED]

### Pattern 5 — weighted loot tables

Loot tables are **weighted random dispensers**: pools carry `rolls` and `bonus_rolls`; entries carry `weight` and `quality` (luck-tilted). Composite entries (`group`, `alternatives`, `sequence`) flatten before rolling, and a `random_sequence` makes drops seed-deterministic. [CONFIRMED — minecraft.wiki]

**Why castle-sim should copy it.** A castle sim runs many weighted rolls — raid composition, hunt yields, market stock. The reusable details are the two-variable model (weight plus a luck tilt) and **seed-determinism**, which makes a bad outcome reproducible in a test.

### Pattern 6 — worldgen as a registry pipeline

Java worldgen is a set of JSON registries in a datapack: noise settings, density functions, biomes, configured and placed features, configured structures, structure sets, template pools, processor lists. Generation runs in fixed steps: `empty → structure_starts → structure_references → biomes → terrain → features → light → spawn → full`. [CONFIRMED — minecraft.wiki]

**Jigsaw structures** assemble large builds from reusable pieces: a jigsaw block holds a target pool, a name, a joint type, and selection/placement priority, and a template pool selects the connecting piece. [CONFIRMED]

**Why castle-sim should copy it.** This is directly a **castle generator**. A Stronghold-style castle is procedurally assembled from wall segments, towers, and gatehouses with connection rules. The jigsaw model — pieces with typed connection points, a pool to pick from, and a priority — is the proven design. For the map scale, Java caps structure blocks at 48×48×48 and Bedrock at 64×384×64. [CONFIRMED]

### Pattern 7 — server plugins versus client mods

The server lineage is **Bukkit → Spigot → Paper → Purpur**, with Folia for regionised threading and Velocity as a proxy. A **plugin** runs server-side only and never changes the client. A **mod** changes the game. Keeping those two surfaces separate is what let the server ecosystem stay stable while client mods churned. [CONFIRMED]

**Why it matters for castle-sim.** If castle-sim ever supports player content, the server-plugin boundary is the one that ages well: content that cannot desync a client is content that does not need a matching-version handshake. Relevant to @concepts/rts-networking-deferred.md.

### Summary table

| Pattern | Source | castle-sim use |
|---------|--------|----------------|
| Typed default-valued components | 1.20.5+ data components | Building/unit data model |
| Build-time generation | Fabric datagen | Balance tables as build output |
| Namespacing + load order | Datapacks | Content registries |
| Weighted loot with seed determinism | Loot tables | Raid/hunt/market rolls |
| Jigsaw piece assembly | Structure generation | Castle generator |
| Server/client surface split | Bukkit/Paper lineage | Future mod API |

## Dead Ends

- Copying NBT-style free-form data. Mojang removed it for good reasons; do not reintroduce it.
- Hand-maintaining generated balance tables. It is the drift problem datagen exists to solve.
- Building a full jigsaw castle generator before the vertical slice. This is a Tier 2+ pattern — see @concepts/scope-tiers.md.
