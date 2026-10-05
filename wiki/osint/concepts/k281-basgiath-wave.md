---
title: K281 Basgiath Wave (Oct 2026)
type: concept
tags: [basgiath, minecraft, k281, gamedev]
keywords: [k281, basgiath, bedrock, dragon-rider, mcpedl]
related:
  - concepts/active-project-research-routing.md
  - concepts/k280-atto-htr-wave.md
  - concepts/k280-ood-stub-wave.md
  - sources/eval-minecraft-modding-2026-10-04.md
  - sources/eval-minecraft-bedrock-protocol-2026-10-04.md
  - sources/universal-modder-2026-10-04.md
maturity: draft
created: 2026-10-04
updated: 2026-10-04
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/active-project-research-routing.md
- @concepts/k280-atto-htr-wave.md
- @concepts/k280-ood-stub-wave.md
- @sources/eval-minecraft-modding-2026-10-04.md
- @sources/eval-minecraft-bedrock-protocol-2026-10-04.md
- @sources/universal-modder-2026-10-04.md

## Raw Concept

K281 cluster hub for the **Basgiath** workstream. Dual-ID **OSINT K281**.

## Narrative

**New project registered.** The operator named a second co-primary workstream alongside GuruWatcher: **Basgiath**, a Minecraft **Bedrock** addition in the Empyrean series (dragon riders, a war college). The eval docx lists it as priority #2 and carries `basgiath` as its own overlap key next to `atto`, `guruwatcher`, `ceminiDFS`, and `ceminiparlays`.

**The repo is `Projects/dragon-rider-map/`.** The README opens with `# Basgiath` and an ASCII dragon. Recent commits are world-building: *"Build the college at the player's feet on a glowing stair"*, *"Start the player on the ground and make a parapet fall fatal."*

**Distribution is fan-facing:** MCPEDL and CurseForge. That is a non-monetized fan project, and the eval repeatedly cites the fan-project rules as the constraint.

### What the two docx files contain

Both are Minecraft. This wave is wider than the usual mix.

| Batch | Rows | Theme |
|-------|------|-------|
| Modding | 20 | Frameworks, Bedrock tooling, server orchestration, asset generation |
| Protocol | 19 | Bedrock protocol engineering, client runtimes, anticheat proxies, MCP automation |

### The two Integrate rows

**`thejacedev/McHeads-API`** (MIT). Renders isometric player heads, 3D body renders, and raw skins **from Bedrock XUIDs as well as Java UUIDs**. The eval's angle: personalized flight scoreboards, rider profiles, and Discord embeds. The Bedrock identity support is the real value — most skin renderers are Java-only.

**`bedrock-mc/mcpelauncher-agent`** (protocol batch). An MCP automation layer over the Bedrock launcher. This is the one that would let an agent drive a running client headlessly.

### The structural extract worth taking

The named repo `rehan-remade/universal-modder` is the most interesting item in the wave, and it is worth reading in full at @sources/universal-modder-2026-10-04.md. Short version: MIT, 2,919 stars, pushed the same day it was checked. It ships **one canonical skill tree with symlinked agent entry points** (`.agents/skills`, `.claude/skills`, `.gemini/skills`, `.github/skills` → `skills/`), a **single `AGENTS.md`** that `CLAUDE.md` and `GEMINI.md` point at, and a **field-notes knowledge base** where the agent must write down what it learned for the next agent.

That last instruction is the one to steal. It is this workspace's own ingest discipline, applied per-game.

### What does not transfer

It targets PC games; Basgiath is Bedrock. Its asset pipeline routes through a paid third-party generation service — a new spend line and a new dependency. **Adopt the layout, not the pipeline.**

### Boundary

No install. Zero clones. The fan-project rules stand: no monetization of the add-on, and the eval's own constraint language is worth keeping. **0 product Integrate GO.**
