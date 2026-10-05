---
title: Minecraft agent MCP servers and coding-agent skills — shelf
type: entity
tags: [entity, tool, mcp, agents, minecraft, phase-0, shelf]
keywords: [mcp, minecraft-mcp, mineflayer, agent-skills, claude-code, modding]
related:
  - concepts/minecraft-agent-harness-shelf.md
  - concepts/minecraft-modding-ecosystem.md
  - concepts/agent-harness-castle-project.md
  - sources/minecraft-modding-deep-research-2026-10-05.md
maturity: validated
created: 2026-10-05
updated: 2026-10-05
wire_status: deferred
wire_target: concepts/agent-harness-castle-project.md
---

## Relations

- @concepts/minecraft-agent-harness-shelf.md — the mechanisms these tools demonstrate
- @concepts/agent-harness-castle-project.md — where a Godot equivalent would live

## Raw Concept

Survey of Model Context Protocol servers that let an LLM drive Minecraft or author mods, plus coding-agent skills for Minecraft development. Most are hobby-scale. They are recorded as **design references for tool-surface shape**, not as adoption candidates. [CONFIRMED]

## Narrative

### Play and control (bot-driving)

| Server | Licence | Stars | Tools | Note |
|--------|---------|-------|-------|------|
| **yuniko-software/minecraft-mcp-server** | Apache-2.0 | 770 | Movement, inventory, blocks, entities, chat | Most adopted; broken on MC 1.21.5 — pin 1.21.4 |
| **HarjjotSinghh/minecraft-mcp** | MIT | 0 | 29 over Mineflayer | Hobby-scale |
| **nacal/mcp-minecraft-remote** | **unverified** | — | Mineflayer remote control | — |

### Mod authoring

| Server | Licence | Stars | Purpose |
|--------|---------|-------|---------|
| **MCDxAI/minecraft-dev-mcp** | MIT | — | 21 tools: decompile, remap, search, analyze game source; validate Mixin and access wideners; version diffing |
| **guguzea/MC-AI-Coding-Assistant-Tool** | MIT | 17 | 86-tool MCP + CLI for modding; targets Cursor/Claude Code/Codex; human-in-the-loop by design |
| **AnCarsenat/minecode-mcp** | **conflict** (README MIT vs sidebar GPL-3.0) | 15 | 30 tools; reads `pack.mcmeta` to pin target version |
| **rogalKraft/mcp-rogal** | **conflict** (README CC0 vs sidebar MIT) | 0 | 26 tools; "honest command results" — real success flag, exact syntax error with cursor position |
| **langyo/minecraft-mod-mcp** | Apache-2.0 / MIT / CC0 (tri) | 39 | In-game GUI control via Java reflection across MC 1.7.2–26.3 |

### Wiki and reference

| Server | Licence | Stars |
|--------|---------|-------|
| **L3-N0X/Minecraft-Wiki-MCP** | **none** | 26 |

### Coding-agent skills

**Jahrome907/minecraft-agent-skills** is the strongest public artifact in this space: **MIT**, 165 stars, actively pushed 2026-09. It ships **13 skills** for Codex and Claude Code — `minecraft-modding` (NeoForge/Fabric/Forge), `minecraft-datapack`, `minecraft-multiloader` (Architectury), `minecraft-testing` (JUnit, MockBukkit, GameTests), `minecraft-ci-release`, worldgen, resource-pack, and server-admin — installable as a Claude Code plugin. [CONFIRMED]

Smaller entries: `Zhangmu-XL/minecraft-mod-skills` (MIT, 2★, Chinese-language), `sikadi233-hub/minecraft-dev` (DeepSeek Harness plugin, 8 skills), `shrimpwagon/ai-minecraft-mobs-creator` (MIT, 1★, NeoForge scaffold). [CONFIRMED]

### What to take from this shelf

Three mechanisms, all already reflected in @concepts/minecraft-agent-harness-shelf.md:

1. **Small composable verbs with machine-checkable results.** The yuniko server's per-action results, and `mcp-rogal`'s "honest command results" (a real success flag, an exact syntax error with a cursor position).
2. **Version pinning before generation.** `minecode-mcp` reads `pack.mcmeta` first, because models "get Minecraft syntax wrong confidently."
3. **Human-in-the-loop gating.** The 86-tool modding assistant deliberately requires a person for disk writes, Gradle runs, and jar copies.

### Licence caution

Two of these declare conflicting licences between the README and the repository sidebar, and one has no licence file. Treat all three as **unresolved** and do not vendor them. [CONFIRMED]

## Dead Ends

- Adopting any of these as-is for a Godot project. None are Godot tools.
- Trusting a repo's stated licence when the sidebar disagrees. Two here conflict.
- Reading star counts as quality. Most of this shelf is 0–39 stars and hobby-scale.
