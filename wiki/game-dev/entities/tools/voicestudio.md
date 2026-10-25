---
title: VoiceStudio — local TTS/ASR studio with MCP (AGPL-3.0)
type: entity
tags: [tool, game-dev, tts, asr, voice-cloning, agpl]
keywords: [VoiceStudio, local TTS, Whisper, Parakeet, dubbing, Basgiath]
related:
  - @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
  - entities/tools/dessa.md
  - entities/tools/pausevfx.md
maturity: draft
created: 2026-10-25
updated: 2026-10-25
phase_0_verdict: CONDITIONAL-GO — isolate only
wire_status: wont_wire
wire_note: AGPL-3.0. Run as an external local studio. Never vendor, link, or bundle into Atto.
---

## Raw Concept

Phase-0 on [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio), 2026-10-25. Source: v10.9 multi-wiki link evaluation, URL 3, scored Extract (Game-dev primary) for basgiath, atto, family-tree.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/debpalash/VoiceStudio |
| **License** | **AGPL-3.0** (verified) |
| **Last commit** | 2026-10-25 (very active) |
| **Size** | 139 MB / 4072 files |
| **Stars** | 84.2k per report |
| **Verdict** | CONDITIONAL-GO — isolate only |

### What it does

One local studio over 16 TTS engines and 11 ASR engines, with a REST API and an MCP server. Voice cloning in about three seconds, text-prompted voice design, dubbing, streaming dictation. Runs on Apple Silicon or a local GPU with no cloud key.

Phase-0 confirmed the MCP surface: `tests/test_mcp_bare_path.py`, `test_mcp_bindings.py` are present in the clone.

### Why isolate only

AGPL-3.0. Atto's policy is no copyleft vendoring. VoiceStudio is a **tool the operator runs**, not a library to link.

That is a normal and workable arrangement: generate audio out-of-process, import the resulting files.

### Where it lands

- **Basgiath** (`dragon-rider-map`) — fan-made narrator voices and localized dubbing for TikTok and Shorts. Basgiath is non-monetized and fan-made; that constraint holds.
- **family-tree dogfood** — offline transcription of private Italian oral histories. Lock to local models; disable hosted line-rewriting.
- **Atto** — multilingual audio for playbook demos.

### Two guards

1. **Turn off hosted translation.** Its advanced translation line-rewriting mode can call a hosted LLM. For family recordings, local models only.
2. **Never clone a commercial audiobook narrator** for Basgiath.

### Unverified

Real-time latency and memory footprint per engine (OmniVoice vs CosyVoice 3 vs IndexTTS 2.5) on this hardware. Nobody has benchmarked it.

## Snippets

> "AGPL-3.0 — strict copyleft network license. Must NEVER be linked, vendored, or bundled inside /Users/claudiobarone/Projects/atto" — source report, URL 3

## Dead Ends

- Vendoring into Atto. AGPL-3.0.
- Using hosted translation on family recordings.
