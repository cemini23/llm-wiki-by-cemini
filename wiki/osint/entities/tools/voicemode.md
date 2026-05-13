---
title: "voicemode — Whisper.cpp + Kokoro voice MCP for Claude Code (Adopt, workflow)"
type: entity
tags: [tool, voice, mcp, whisper, kokoro, claude-code, m-series-mac, gemini-eval-doc1, phase-0-adopt-candidate]
keywords: [voicemode, voice mode, mbailey, whisper.cpp, kokoro tts, core ml, m-series, mcp-native, bidirectional voice]
related:
  - sources/evaluating-github-repos-trading-stack-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - "@image-gen-wiki/entities/persona-ops/voicemode.md"
maturity: draft
created: 2026-05-12
updated: 2026-05-12
gemini_eval_doc1_url: 19
phase_0_verdict: ADOPT-CANDIDATE 2026-05-12 (workflow-laptop, M-series Mac fit)
adoption_status: PRE-PHASE-0 2026-05-12
---

## Relations

- `@sources/evaluating-github-repos-trading-stack-2026-05-12.md` — source eval (URL 19)
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — corrected multi-wiki prompt
- `@image-gen-wiki/entities/persona-ops/voicemode.md` — cross-routed for persona-ops voice angle

## Raw Concept

- **Repo**: `github.com/mbailey/voicemode`
- **License** [per Gemini eval]: MIT
- **Tier**: Adopt
- **Primary fit**: Workflow (laptop-side Claude Code)
- **Cross-route**: image-gen wiki (persona-voice ops on M-series Mac)

## Narrative

Bidirectional voice MCP server for Claude Code: Whisper.cpp (STT) + Kokoro (TTS), Core ML accelerated on M-series Mac. Replaces cloud-API voice loops with fully local stack — privacy-preserving, no per-token cost, no network dependency.

### Integration vector

Direct workflow adopt for laptop-side Claude Code sessions. Phase-0 audit: license verification, M-series Core ML model size + RAM footprint, MCP wiring against existing skill stack. Cross-route stub to image-gen wiki for persona-voice angle.

### Open questions

- Latency: STT round-trip on M-series for 30-second clip
- Kokoro voice quality + voice-set variety for persona-ops use
