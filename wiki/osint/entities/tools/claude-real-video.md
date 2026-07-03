---
title: claude-real-video — scene-aware video ingest pattern
type: entity
tags: [entity, tool, video, osint, multimodal, steal-from, k142]
keywords: [claude-real-video, ffmpeg, yt-dlp, whisper, keyframes, transcript, MIT]
related:
  - sources/multi-wiki-url-evaluation-2026-07-03.md
  - concepts/cemini-wiki-ingest-workflow.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
---

## Relations

- @sources/multi-wiki-url-evaluation-2026-07-03.md — K142 Steal-from row
- @concepts/cemini-wiki-ingest-workflow.md — local multimedia ingest extension

## Raw Concept

K142 Phase-0 audit of [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video), a local Python/FFmpeg pipeline for scene-aware keyframes plus transcript sidecars.

## Narrative

| Field | Value |
|-------|-------|
| **Verdict** | **Steal-from** — copy pipeline ideas, not dependency |
| **License** | MIT (`gh api`, 2026-07-03) |
| **Maturity** | New repo, ~500★, no strong CI signal |
| **Failure mode** | Fast-cut over/under sampling and context budget blowups |

The reusable primitive is the manifest: scene-change frames, density floor, sliding-window dedupe, optional Whisper transcript, and threshold-tuning report. That maps to OSINT video evidence ingest without sending sensitive material to cloud video services.

## Snippets

> "scene-aware, deduplicated frames + transcript, from a URL or local file." [Source: https://github.com/HUANGCHIHHUNGLeo/claude-real-video (retrieved 2026-07-03)]
