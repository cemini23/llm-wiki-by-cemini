---
title: morganpage — local NPC dialogue system (2026)
type: source
tags: [source, npc, local-llm, ollama, indie]
keywords: [npc-dialogue, ollama, local-llm, python, unity]
related:
  - concepts/llm-npc-runtime-ai-shelf.md
  - concepts/agentic-npc-design-guardrails.md
read_status: partial
source_type: github
source_url: https://github.com/morganpage-tech/npc-dialogue-system
maturity: tentative
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

MIT prototype — **local** LLM NPC dialogue (Ollama/Python) for indie RPG; personality via system prompts + conversation memory.

## Narrative

### Features [CONFIRMED — README metadata]

- No cloud — M1-friendly local inference
- Character-specific personalities
- Unity game integration (C# + Python backend)

### Scale

~1★ — prototype quality; useful as **architecture sketch** for local Godot equivalent (HTTP to Ollama + JSON API).

### Guardrail gap

No documented lore fences / economy guards — pair with @concepts/agentic-npc-design-guardrails.md before any production use.

| Posture | **WATCH** — reference architecture only |
