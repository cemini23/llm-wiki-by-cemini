---
title: Meetily — local ASR meeting transcription app
type: entity
tags: [entity, tool, audio, transcription, osint, defer, k142]
keywords: [Meetily, Tauri, Rust, Whisper, Parakeet, local ASR, MIT]
related:
  - sources/multi-wiki-url-evaluation-2026-07-03.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
---

## Relations

- @sources/multi-wiki-url-evaluation-2026-07-03.md — K142 Defer row

## Raw Concept

K142 Phase-0 audit of [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily), a local-first Tauri/Rust meeting assistant with Whisper/Parakeet transcription and local summarization.

## Narrative

| Field | Value |
|-------|-------|
| **Verdict** | **Defer** |
| **License** | MIT (`gh api`, 2026-07-03) |
| **Maturity** | ~14k★, tagged releases, active desktop app |
| **Failure mode** | Monolithic desktop UI, Rust/Tauri/audio/GPU dependency weight, PRO split |

The OSINT-relevant piece is local ASR, not the meeting-product shell. Keep as a future extraction reference if audio/call evidence becomes a first-class ingest surface.
