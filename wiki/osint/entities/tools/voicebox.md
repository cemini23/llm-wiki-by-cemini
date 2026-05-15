---
title: "voicebox — Local-First AI Voice Studio (jamiepine)"
type: entity
tags: [voice-cloning, tts, mlx, fastapi, mcp-server, rust, mit, adopted-tier, laptop-only]
keywords: [voicebox, tts-studio, voice-cloning, mlx-metal, paralinguistic-tags, mcp-server, persona-ops]
related:
  - sources/multi-wiki-tool-evaluation-v3.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations
- @ccc-wiki/briefs/2026-05-15_voicebox-mcp-ccc.md  (cross-wiki brief)
- @image-gen-wiki/entities/voicebox.md  (cross-wiki stub)

- @sources/multi-wiki-tool-evaluation-v3.md — v3 batch eval: Adopt tier, Image-gen wiki primary fit

## Raw Concept

From the Cemini Multi-Wiki Link Evaluation Report v3 (May 2026). MIT-licensed v0.5.0, 25.7k stars. Local-first AI voice studio with 7 TTS engines, MLX/Metal hardware acceleration, and integrated MCP server.

## Narrative

Voicebox solves TTS and voice-cloning for Image-gen wiki persona-ops. MLX/Metal support ensures local M-series Mac inference without leaking voice profiles to external APIs. The MCP server integration enables Claude Code to trigger speech generation directly from terminal. Supports paralinguistic tags ([laugh], [sigh]) and multi-language generation.

**Tier: Adopt** — MIT license, safe for IP perimeter. Cross-wiki routing: document MCP server initialization in CCC wiki for terminal-native TTS from agent runtime.

**NEEDS VERIFICATION:** WebSocket `/transcribe/stream` latency over local network topologies.
