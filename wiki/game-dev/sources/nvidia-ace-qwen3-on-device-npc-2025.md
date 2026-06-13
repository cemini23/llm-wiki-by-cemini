---
title: NVIDIA ACE — Qwen3-8B on-device NPC SLM (2025)
type: source
tags: [source, nvidia, ace, npc, slm, unreal]
keywords: [nvidia-ace, qwen3, on-device, npc, igi-sdk]
related:
  - concepts/llm-npc-runtime-ai-shelf.md
read_status: read
source_type: official
source_url: https://developer.nvidia.com/blog/nvidia-ace-adds-open-source-qwen3-slm-for-on-device-deployment-in-pc-games/
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

NVIDIA **ACE** adds open-source **Qwen3-8B** SLM via In-Game Inferencing (IGI) SDK for on-device PC game NPCs — speech, reasoning, animation pipeline.

## Narrative

### Capabilities [CONFIRMED]

- Real-time non-scripted reasoning + dynamic player-input responses
- On-device deployment (PC) — reduces cloud latency/cost vs per-bark API
- Magpie TTS Flow plugin — multilingual (ES/DE) experimental
- IGI SDK: MultiLoRA, CUDA-in-Graphics for Vulkan, function-calling sample

### Stack position

Middleware for **digital humans** — targets UE/NvRTX branch demos (Naraka, inZOI integrations mentioned in ecosystem news).

### castle-sim relevance

**Not applicable to Godot hobby path** without custom port — catalog as industry reference for Tier 3+ "what AAA ships toward."

Watch: GDC25 session `gdc25-gdc1010` on-device ACE SLMs.

## Snippets

Download: NVIDIA IGI SDK + Qwen3 plugin from developer.nvidia.com ACE resources.
