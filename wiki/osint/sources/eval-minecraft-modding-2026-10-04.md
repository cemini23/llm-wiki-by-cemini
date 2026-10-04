---
title: "Minecraft modding repository evaluation — 20 rows (2026-10-04)"
type: source
tags: [source, k281, basgiath, minecraft, eval]
keywords: [k281, bedrock, mcpedl, orchestration, extract]
related:
  - concepts/k281-basgiath-wave.md
maturity: draft
created: 2026-10-04
updated: 2026-10-04
read_status: skimmed
---

## Relations

- @concepts/k281-basgiath-wave.md

## Raw Concept

| File | `Minecraft Repositories Revenue Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Minecraft Repositories Revenue Evaluation.docx` |
| Archive | egress-fi 2026-10-04 |
| Retrieved | 2026-10-04 |
| Dual-ID | **OSINT K281** |
| Batch theme | Minecraft modding frameworks, Bedrock world and inventory tooling, server orchestration, community asset generation |
| sha256 | see the archive record |

## Narrative

Twenty rows for the **Basgiath** workstream. Distribution target is MCPEDL and CurseForge, non-monetized.

### Tier spread

| Tier | Count |
|------|-------|
| Integrate | 1 |
| Extract | 5 |
| Context | 2 |
| Watch | 1 |
| Pass | 4 |
| UNAVAILABLE | 7 |

**Seven rows were unreachable.** That is the highest unavailable rate of any batch this month, and it is worth noting separately: several "repositories" do not resolve, which suggests the eval's URL list was partly generated rather than verified.

### The Integrate row

**`thejacedev/McHeads-API`** (MIT). Serves cached **isometric player heads, 3D body renders, and raw skins**, supporting **Bedrock Edition XUIDs as well as Java UUIDs**.

Why it matters: legacy skin renderers are Java-only. Basgiath runs on Bedrock, so an identity layer that understands Bedrock player IDs solves a real gap for personalized flight scoreboards, rider profiles, and Discord embeds.

### The Extract rows

| Repo | Technique |
|------|-----------|
| `dadeeen/MCBE_Inventory_Editor` | Offline inspection of **Bedrock LevelDB NBT** player records. Lets you set inventory state without launching the game client |
| `itzg/docker-minecraft-server` | Container lifecycle scripts for **headless** world-gen and behavior-pack validation |
| `TheRemote/MinecraftBedrockServer` | systemd provisioning, auto-restart backups, version pinning, **Box64** for 64-bit ARM |
| `ewanhowell5195/MinecraftTitleGenerator` | Blockbench 3D typography presets for promotional art |
| `Romoslayer/Hit-Indication-Port` | Radial 360-degree damage-direction arrows; the **UX pattern** ports to Bedrock UI JSON even though the Java code does not |

**The most useful pairing is the first two.** `MCBE_Inventory_Editor` plus a headless container is a test bench: set an inventory, boot the world, assert the loadout, without a human clicking through a client.

### What was rejected

`MinecraftForge` and `MinecraftDev` are Java toolchains — Pass for a Bedrock target. `meteor-client` is a Java anticheat-evasion client: Pass, and **no code, no technique, and no configuration from it belongs in this wiki.** The Spice Road, bons-and-furious, and the four unreachable rows are Pass or UNAVAILABLE.

### Boundary

**Zero clones.** The techniques above are implementable in our own code. Nothing is vendored. No client-modification code is recorded here.
