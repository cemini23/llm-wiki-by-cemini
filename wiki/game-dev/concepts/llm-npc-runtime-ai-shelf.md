---
title: LLM runtime NPC AI — research shelf (Tier 3+)
type: concept
tags: [concept, npc, llm, ai, runtime, deferred]
keywords: [llm-npc, nvidia-ace, ubisoft, dialogue, runtime-ai]
related:
  - concepts/agentic-npc-design-guardrails.md
  - concepts/scope-tiers.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - sources/ubisoft-teammates-ai-experiment-2025.md
  - sources/nvidia-ace-qwen3-on-device-npc-2025.md
  - sources/llmunity-unity-npc-plugin.md
  - sources/morganpage-local-npc-dialogue-2026.md
  - sources/exa-npc-pcg-ccgs-batch-2026-06-13.md
  - sources/ixie-agentic-npc-balance-2026.md
maturity: draft
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @concepts/vertical-slice-v0.md — v0 has **no** LLM NPCs
- @concepts/stronghold-systems-inventory.md — SH1 dialogue is scripted barks

## Raw Concept

**Runtime** LLM-driven NPCs (dialogue, voice commands, adaptive squad AI) — distinct from **dev-time** AI assistants. Shelf until Tier 3+ or spin-off project; castle-sim v0–v2 uses scripted peasants/lords.

## Narrative

### Dev AI vs runtime AI

| | Dev-time (now) | Runtime NPC (shelf) |
|---|----------------|---------------------|
| Purpose | Write code, art, tests | Player-facing dialogue/behavior |
| Stack | Cursor, Claude Code, MCP | SLM on-device, cloud LLM, voice |
| Risk | MCP security, scope creep | Balance, lore drift, cost/DAU |
| castle-sim | **GO** wiki + harness | **DEFER** |

### Industry stack (2025–2026)

| Source | Pattern | Engine | Relevance |
|--------|---------|--------|-----------|
| NVIDIA ACE + Qwen3-8B SLM | On-device inference, TTS, IGI SDK | UE middleware | AAA PC; not Godot hobby path [@sources/nvidia-ace-qwen3-on-device-npc-2025.md] |
| Ubisoft Teammates / Neo NPC | Voice commands, squad AI, authored "fences" for improv | Custom research FPS | Design patterns for guardrails [@sources/ubisoft-teammates-ai-experiment-2025.md] |
| GDC 2025 ACE talk | On-device SLMs for character reasoning | — | Watch for Godot ports |

### Indie / open-source implementations

| Tool | Engine | Notes | Posture |
|------|--------|-------|---------|
| [LLMUnity](https://github.com/undreamai/LLMUnity) | Unity | ~1.6k★, llama.cpp, RAG, character API | Unity only — @sources/llmunity-unity-npc-plugin.md |
| [morganpage npc-dialogue-system](https://github.com/morganpage-tech/npc-dialogue-system) | Unity + local Python/Ollama | Local inference, personality prompts | Prototype scale |
| [merrymaker14/unity-llm-npc](https://github.com/merrymaker14/unity-llm-npc) | Unity | — | WATCH |
| Godot LLM NPC | — | **No mature OSS equivalent** found in Exa pass | Gap |

### Stronghold / castle-sim mapping

| SH feature | Tier 1–2 | Tier 3+ LLM option |
|------------|----------|------------------|
| Peasant barks | Random scripted pool | Optional flavor only |
| Lord messages | Event-triggered text | Not needed for slice |
| Advisor / tutorial | UI tooltips | Could use constrained SLM later |
| Multiplayer taunt chat | N/A | Never cloud LLM in lockstep sim |

### Adoption gate

Adopt runtime LLM NPCs only when:

1. Core loop shipped and fun without them
2. @concepts/agentic-npc-design-guardrails.md implemented (constraints, memory, telemetry)
3. Cost model bounded (caps, cache, VIP NPCs only)
4. Godot integration path chosen (custom HTTP to local Ollama vs wait for mature plugin)

## Snippets

Tier tag for ROADMAP:

```
Tier 3+: runtime LLM NPC layer (optional spin-off: "castle advisor" demo)
```

## Dead Ends

- Shipping Ubisoft-style voice squad AI in hobby Godot RTS — engine/integration gap + scope
- Cloud LLM per peasant bark — unit economics kill at scale [iXie LiveOps section]
