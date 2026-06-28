---
title: Krafton PUBG Ally — NVIDIA ACE co-playable character — 2026-06-25
type: source
tags: [source, nvidia, ace, npc, krafton, digest]
keywords: [pubg, ally, nvidia-ace, co-playable, runtime-npc]
related:
  - sources/nvidia-ace-qwen3-on-device-npc-2025.md
  - concepts/llm-npc-runtime-ai-shelf.md
  - concepts/agentic-npc-design-guardrails.md
  - sources/inbox-arxiv-reject-batch-2026-06-28.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: news-digest
source_url: https://gamedev.net/news/how-krafton-built-pubg-ally-a-co-playable-character-powered-by-nvidia-ace-r4114/
maturity: validated
created: 2026-06-28
updated: 2026-06-28
---

## Raw Concept

Digest pick (2026-06-25): Krafton **PUBG Ally** — co-playable teammate powered by **NVIDIA ACE** stack. Industry reference for runtime LLM NPCs; not Godot/castle-sim path.

## Narrative

### Pattern [TENTATIVE — press summary]

| Layer | Notes |
|-------|-------|
| Runtime | ACE-powered ally joins squad as AI teammate (not chat-only bark) |
| Stack | Extends @sources/nvidia-ace-qwen3-on-device-npc-2025.md on-device SLM + animation pipeline |
| Design | Co-playable = gameplay agency, not dialogue novelty |

### castle-sim relevance

| Extract | Skip |
|---------|------|
| Tier 3+ shelf: authored fences + on-device inference for companion units | SH2 lord AI (JSON director, no LLM) |
| Guardrail patterns → @concepts/agentic-npc-design-guardrails.md | Porting ACE to Godot hobby stack |

**Verdict:** **WATCH (industry)** — update @concepts/llm-npc-runtime-ai-shelf.md; no Phase-0.

## Dead Ends

- Replacing LordProfile JSON with PUBG-style LLM teammate for vertical slice
