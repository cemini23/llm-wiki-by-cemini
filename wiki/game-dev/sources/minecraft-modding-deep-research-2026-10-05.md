---
title: Minecraft modding deep research — web batch (2026-10-05)
type: source
tags: [source, minecraft, research, ecosystem, modding]
keywords: [minecraft, neoforge, fabric, bedrock, script-api, modrinth, deobfuscation]
related:
  - concepts/minecraft-modding-ecosystem.md
  - concepts/minecraft-bedrock-addons-scripting.md
  - concepts/minecraft-data-driven-content-patterns.md
  - concepts/minecraft-agent-harness-shelf.md
  - entities/tools/blockbench.md
  - entities/tools/mineflayer.md
  - entities/tools/minecraft-agent-mcp-shelf.md
  - sources/minecraft-social-scan-2026-10-05.md
read_status: read
source_type: web-research-batch
source_url: https://fabricmc.net/2025/10/31/obfuscation.html
maturity: validated
created: 2026-10-05
updated: 2026-10-05
---

## Raw Concept

Operator-directed deep research into the Minecraft modding ecosystem, both editions, run 2026-10-05. Four parallel research agents covered Java loaders and toolchain, Bedrock add-ons and scripting, AI agents in Minecraft, and modding tooling and infrastructure. Methods: WebSearch, WebFetch, primary-source verification. Routing was sandbox-blocked, so external cheap executors were unavailable.

## Narrative

### Headline findings

1. **Minecraft Java dropped obfuscation.** Announced 2025-10-31, effective after 1.21.11. Yarn is deprecated, Intermediary ceases to exist, and **no mod compiled for 1.21.11 or earlier works on 26.1 without recompilation.** Verified against the primary Fabric post. [CONFIRMED]
2. **Blockbench is GPL-3.0 and actively maintained** (v5.2.1, 2026-09-21), with glTF export — a real candidate for castle-sim Fork B art. [CONFIRMED]
3. **The AI-agent lane is the strongest transfer.** Mineflayer (MIT, active) is the maintained foundation; Malmo is archived and MineRL is stale. MCP servers for Minecraft exist but are hobby-scale. 13 coding-agent skills for Minecraft modding ship under MIT. [CONFIRMED]
4. **Data components (1.20.5+) are the most reusable engineering pattern** — typed, registry-backed, default-valued. [CONFIRMED]

### Per-area detail

- **Java loaders and toolchain** → @concepts/minecraft-modding-ecosystem.md
- **Bedrock packs and Script API** → @concepts/minecraft-bedrock-addons-scripting.md
- **Data-driven content patterns** → @concepts/minecraft-data-driven-content-patterns.md
- **AI agents, MCP, benchmarks** → @concepts/minecraft-agent-harness-shelf.md

### Key primary sources

| Source | What it establishes |
|--------|---------------------|
| [fabricmc.net/2025/10/31/obfuscation.html](https://fabricmc.net/2025/10/31/obfuscation.html) | The deobfuscation announcement; Yarn and Intermediary deprecation |
| [fabricmc.net/2026/03/14/261.html](https://fabricmc.net/2026/03/14/261.html) | 26.1 breaks pre-existing mods without recompilation |
| [neoforged.net/news/2023-retrospection](https://neoforged.net/news/2023-retrospection/) | Why the Forge fork happened |
| [docs.modrinth.com/api](https://docs.modrinth.com/api/) | 300 req/min, PAT and OAuth2 |
| [MicrosoftDocs minecraft-creator](https://github.com/MicrosoftDocs/minecraft-creator) | Manifest reference, Script module versioning, 1.26.0 notes |
| [wiki.bedrock.dev](https://wiki.bedrock.dev/scripting/api-environment.html) | QuickJS, ESM, no setTimeout, script_eval |
| [minecraft.wiki — Data component format](https://minecraft.wiki/w/Data_component_format) | The 1.20.5+ typed component change |
| [docs.fabricmc.net/develop/loom/](https://docs.fabricmc.net/develop/loom/) | Datagen, build-time content generation |
| [github.com/MineDojo/Voyager](https://github.com/MineDojo/Voyager) | The skill-library mechanism (arXiv 2305.16291) |
| [arXiv 2303.13512](https://arxiv.org/abs/2303.13512) | BASALT retrospective — fuzzy tasks unsolved |
| [bokmcdok.com](https://www.bokmcdok.com/the-pains-of-porting-mods/) | Porting cost, six parallel versions |

### Confidence and gaps

- **Well corroborated:** the deobfuscation event, licences (GPL-3.0, MIT, Apache-2.0), Modrinth API limits, Bedrock manifest and module versioning, data components, Voyager's mechanisms.
- **Lower confidence:** Minecoin pricing and Marketplace earnings tiers (third-party guides); the 78/22 Bedrock/Java player split (fan estimate, no methodology).
- **Unresolved:** CurseForge rate limits (not publicly documented); two MCP repos with conflicting licence declarations; Amethyst's exact open/closed split.
- **Not claimed:** nothing here was tested by running Minecraft.

## Dead Ends

- Treating "Forge is dead" as fact. Its changelog shows active releases; it is legacy, not dead.
- Trusting a repo's licence from the rendered page alone. Two conflicted between README and sidebar.
