---
title: Mineflayer — JavaScript bot API for Minecraft
type: entity
tags: [entity, tool, agents, minecraft, phase-0]
keywords: [mineflayer, prismarinejs, bot-api, mit, agent-harness]
related:
  - concepts/minecraft-agent-harness-shelf.md
  - concepts/minecraft-modding-ecosystem.md
  - concepts/agent-harness-castle-project.md
  - sources/minecraft-modding-deep-research-2026-10-05.md
maturity: validated
created: 2026-10-05
updated: 2026-10-05
wire_status: wont_wire
wire_target: concepts/minecraft-agent-harness-shelf.md
---

## Relations

- Source: [PrismarineJS/mineflayer](https://github.com/PrismarineJS/mineflayer)
- Family: [PrismarineJS](https://github.com/PrismarineJS) — node-minecraft-protocol, minecraft-data, prismarine-viewer

## Raw Concept

High-level JavaScript API for creating Minecraft bots. The maintained foundation of the Minecraft agent ecosystem, and the base layer of nearly every Minecraft MCP server. [CONFIRMED]

## Narrative

### Phase-0 verdict (2026-10-05)

| Check | Result |
|-------|--------|
| SPDX / LICENSE | **MIT** |
| Maturity | Active — last push 2026-10-03; 7.5k stars |
| Ecosystem | node-minecraft-protocol (BSD-3-Clause), minecraft-data, prismarine-viewer (MIT), mineflayer-pathfinder (MIT) |
| Verdict | **STEAL-FROM** — pattern only, `wont_wire` |

### Why it is not adopted

castle-sim is a Godot project, not a Minecraft mod. Mineflayer runs in Node and speaks the Minecraft protocol. There is nothing to integrate. It is recorded because its **tool surface** is the clearest existing example of the agent tool granularity this wiki recommends. [CONFIRMED]

### The tool surface

Mineflayer exposes many small composable verbs — move, dig, place, craft, equip, look, chat — each with a machine-checkable result, plus `mineflayer-pathfinder` for A-to-B movement. An LLM agent composes them. This is rule **H1** in @concepts/agent-harness-castle-project.md: named high-level operations with primitive fallback, rather than one opaque `do_task` call. See @concepts/minecraft-agent-harness-shelf.md.

### Licence note for the ecosystem

Mineflayer itself is MIT, but several downstream research projects in the same space are **not**: MineRL and Craftium publish "Other"/unverified licences. Do not assume MIT propagates. Verify per repo before any adoption. [CONFIRMED]

## Dead Ends

- Running Minecraft as a castle-sim test environment. Wrong engine, wrong platform.
- Assuming the research frameworks share Mineflayer's permissive licence. They do not.
