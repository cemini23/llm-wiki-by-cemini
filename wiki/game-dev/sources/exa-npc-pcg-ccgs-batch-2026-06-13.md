---
title: Exa NPC + PCG + CCGS batch — 2026-06-13
type: source
tags: [source, exa, ingest, npc, pcg, ccgs]
keywords: [exa, llm-npc, agentic-pcg, ccgs, procedural]
related:
  - concepts/llm-npc-runtime-ai-shelf.md
  - concepts/agentic-npc-design-guardrails.md
  - concepts/agentic-pcg-level-design.md
  - concepts/ccgs-workflow-extraction.md
  - sources/exa-ai-gamedev-tools-batch-2026-06-13.md
read_status: read
source_type: exa-batch
source_url: wiki/sweeps/2026-06-13-exa-npc-pcg-ccgs-batch.json
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

Third Exa pass — three lanes in one batch: **runtime LLM NPCs**, **agentic PCG**, **CCGS deep extraction**.

## Narrative

### Clusters (11)

| Lane | Clusters | Top hits |
|------|----------|----------|
| Runtime NPC | llm-npc-dialogue-gdc, nvidia-ace, ubisoft-neo-npc, llm-npc-indie, narrative-ai-safety | NVIDIA ACE GDC25, Ubisoft Teammates, LLMUnity, morganpage npc-dialogue |
| Agentic PCG | agentic-pcg-games, llm-level-design, godot-procedural-generation-ai, pcg-unity-unreal-agent | AgenticPCG (Jiang), ai-powered-level-designer, Edgar.Godot |
| CCGS extract | ccgs-claude-code-game-studios, claude-code-game-dev-skills | workflow-catalog.yaml, 49 agents, 73 skills, Starlog deep dive |

**82 unique URLs** — `wiki/sweeps/2026-06-13-exa-npc-pcg-ccgs-batch.json`

### GDC / industry NPC gap

No single "how to ship LLM NPCs in Godot indie" canonical talk — industry stack is **Unreal + NVIDIA ACE** or **Ubisoft research demos**. Indie path = local LLM plugins (Unity-first) or scripted + optional LLM layer at Tier 3+.

### Pages written

@concepts/llm-npc-runtime-ai-shelf.md, @concepts/agentic-npc-design-guardrails.md, @concepts/agentic-pcg-level-design.md, @concepts/ccgs-workflow-extraction.md + sources below.
