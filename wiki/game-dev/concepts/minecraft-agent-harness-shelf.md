---
title: Minecraft AI agents — platforms, MCP, benchmarks, harness lessons
type: concept
tags: [concept, minecraft, agents, harness, benchmarks, reference]
keywords: [mineflayer, voyager, minedojoo, mcp, miner, agent-harness, skill-library]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/minecraft-modding-ecosystem.md
  - entities/tools/mineflayer.md
  - entities/tools/minecraft-agent-mcp-shelf.md
  - sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md
  - sources/minecraft-modding-deep-research-2026-10-05.md
maturity: validated
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- @concepts/agent-harness-castle-project.md — the castle-sim harness this informs
- @entities/tools/mineflayer.md — the bot API
- @entities/tools/minecraft-agent-mcp-shelf.md — the MCP servers
- @sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md — the verified-ledger harness (rule H3)

## Raw Concept

Minecraft is the most-used environment in LLM-agent research, and its community has built real agent tooling: bot clients, MCP servers, and coding-agent skills for mod development. This page collects the platforms, the benchmarks, and the concrete harness mechanisms worth stealing. [CONFIRMED]

## Narrative

### Platforms

| Name | What it is | Licence | Stars | Status |
|------|-----------|---------|-------|--------|
| **Mineflayer** | High-level JS API for building Minecraft bots | MIT | 7.5k | Active (push 2026-10-03) |
| **node-minecraft-protocol** | Packet parse/serialize, auth, encryption | BSD-3-Clause | 1.4k | Active |
| **minecraft-data** | Language-independent Minecraft data module | unverified | 947 | Active |
| **prismarine-viewer** | Web viewer for servers and bots | MIT | 395 | Active |
| **Voyager** | LLM lifelong-learning agent (GPT-4) | MIT | 7.2k | Reference implementation |
| **MineDojo** | Open-ended agent framework, 3,142 tasks | MIT code, CC-BY data | 2.3k | Low activity |
| **MineRL** | RL package and competition environment | "Other" — **unverified** | 977 | Stale (push 2025-01) |
| **Project Malmo** | Microsoft AI research platform | MIT | 4.3k | **Archived 2026-08-18** |
| **Craftium** | Fast voxel RL env on Luanti | "Other" — **unverified** | 214 | Active |
| **Odyssey** | Voyager-based, 40 + 183 skills, IJCAI 2025 | MIT | 409 | 2025 |

Two closures matter: **Malmo is archived**, and **MineRL is stale**. The maintained lane is PrismarineJS (Mineflayer and friends). [CONFIRMED]

### The Voyager mechanism

Voyager is the reference design, and it still is. Three mechanisms, no fine-tuning: [CONFIRMED — arXiv 2305.16291]

1. **Automatic curriculum** — the model proposes progressively harder tasks from current agent state.
2. **Skill library** — executable JavaScript indexed by description embeddings, retrieved and composed.
3. **Iterative prompting** — programs are improved using **environment feedback, execution errors, and self-verification**.

Reported results: 3.3× unique items, 2.3× travel distance, up to 15.3× faster tech-tree milestones, the only method to unlock the diamond tier, and zero-shot transfer of the skill library to a new world. [CONFIRMED]

Successors scale the same shape: Odyssey (183 compositional skills), JARVIS-1, OpenHA ("Chain of Action"), ADAM (causal world knowledge), MindForge (theory of mind). [CONFIRMED]

### Benchmarks

- **MineRL BASALT** — four reward-free "fuzzy" tasks (FindCave, MakeWaterfall, CreateVillageAnimalPen, BuildVillageHouse), judged by humans. The 2022 retrospective concluded **no team solved the fuzzy tasks robustly**. This is the key negative result: for aesthetic or design goals, a scalar reward does not work. [CONFIRMED — arXiv 2303.13512]
- **MineDojo** — 3,142 tasks, and the internet-scale knowledge base that grounds them.
- **Craftium** — high-throughput voxel environment, ICML 2025.
- **OpenHA** — 800+ verified embodied tasks; reported success rates in the tens of percent.

The general state: VLM-based hierarchical agents now beat specialist RL policies on many tasks, but **absolute success rates remain low**. [CONFIRMED]

### Harness lessons

These are the transferable mechanisms, and they line up with the rules already wired in @concepts/agent-harness-castle-project.md.

1. **Tool granularity beats monolithic actions.** Mineflayer and the MCP servers expose small composable verbs — dig, place, craft, goto. The agent composes them. This is rule **H1** (name high-level operations, keep primitive fallback) seen from the other side. [CONFIRMED]
2. **A skill library is executable code, not prompts.** Store verified programs indexed by description; retrieve and reuse instead of regenerating. Voyager's cross-world transfer is the evidence. [CONFIRMED]
3. **Verification must be execution-grounded.** Voyager feeds back execution errors and environment feedback, then self-verifies. The practical form is an "honest command result" — a real success flag and an exact error with position — not prose. [CONFIRMED]
4. **Version-pin the target before generating.** One MCP server reads `pack.mcmeta` to fix the pack format first, because models "get Minecraft syntax wrong confidently." A game-dev harness should pin the engine and API version in context before any code generation. [CONFIRMED]
5. **Automatic curriculum drives long-horizon progress.** Generate the next task from current state rather than working a fixed list. [CONFIRMED]
6. **Human judgment for fuzzy goals.** BASALT shows scalar rewards fail on fuzzy tasks. Keep a person or a rubric in the loop for aesthetic and design goals. This matches the mod-dev MCP tools that deliberately gate disk writes and builds behind a human. [CONFIRMED]
7. **Isolate components so the harness is swappable.** One framework layers Task / View / Tools / Trainer components selected by YAML, with architecture tests enforcing import direction. Planner, executor, and verifier become separately testable. [CONFIRMED]

Lesson 3 and rule **H4** (audit something the executor did not nominate) are the same argument from two directions: the verifier needs machine-checkable ground truth, and it must not let the worker choose what gets checked.

### AI-assisted mod development

The strongest public artifact is **minecraft-agent-skills** (MIT, 165★, active): 13 skills for Codex and Claude Code covering modding, datapacks, multiloader, testing, CI release, and worldgen, installable as a Claude Code plugin. Smaller entries exist for NeoForge scaffolds and Paper plugins. [CONFIRMED — see @entities/tools/minecraft-agent-mcp-shelf.md]

The social scan found the same theme from the community side: high-engagement posts through late 2026 show AI agents porting and grafting whole games — "the model did not make a mod, it made the thing that makes mods." [CONFIRMED — see @sources/minecraft-social-scan-2026-10-05.md]

## Dead Ends

- Adopting a research framework (MineRL, Malmo) as a harness. Both are stale or archived.
- Scalar rewards for aesthetic castle-design goals. BASALT is the evidence against it.
- Copying Voyager wholesale into Godot. The transferable part is the mechanism, not the Minecraft-specific skill library.
