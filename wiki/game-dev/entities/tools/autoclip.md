---
title: "autoclip — long video to vertical clips, locally (MIT)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - entities/tools/ffmpeg-skill.md
updated: 2026-11-24
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md, URL 8,
**Extract** tier. Routed to game-time, with Basgiath as the second target.

The question this page answers: **what turns a one-hour recording into ten short clips
without a subscription and without uploading the video?**

## Narrative

### What it does

A pipeline, not a model:

1. **Transcription** — local Whisper (~220 MB) or cloud ASR.
2. **Highlight scoring** — a multimodal model picks the moments worth clipping.
3. **Vertical layout** — reframe to 9:16 with the subject tracked.
4. **Subtitle and cover generation** per platform.
5. **Platform copy** for TikTok, Reels, and Shorts.

Stack: Python, FastAPI, Celery/Redis, SQLite, a React UI, FFmpeg. Ships a CLI, an MCP
server, and desktop bundles.

**The important property:** editing and rendering stay local. Fully local operation
needs local Whisper plus Ollama or LM Studio. A cloud model and cloud ASR are optional
speed-ups, not requirements.

### Published benchmark

The author's 2026-10-01 Apple Silicon run reports ~7.5 min to produce 10 clips from a
1h43m interview, using author-supplied subtitles and cloud `qwen-plus`.
[TENTATIVE — author-reported, and the cloud model is part of the timing]

Treat that number as an upper bound on quality with a lower bound on privacy. A fully
local run will be slower and slightly worse.

### Why it is only Extract

The value is the **pipeline decomposition**, not the application. game-time has its own
sim core and renderer; it does not need a Celery deployment. What it lacks is any
video-to-clip capability at all — there is no `ffmpeg` or clip reference anywhere under
`packages/`. [CONFIRMED — local check 2026-11-24]

The extract is a lean standalone script: transcript, score, cut, reframe, burn
subtitles. That is a few hundred lines against local FFmpeg, and it pairs with the
already-queued `ffmpeg-skill` entry for frame extraction.

### Second target

Basgiath (`dragon-rider-map`) carries an explicit clip and TikTok reach target in its
distribution docs. The same pipeline serves it with no code change — only different
source footage.

### Phase-0, 2026-11-24

| Check | Result |
|-------|--------|
| Licence | MIT [CONFIRMED — GitHub API] |
| Maturity | 15k stars, 2.2k forks, pushed the day of the check, 40 open issues |
| Cloud requirement | optional — local Whisper and Ollama/LM Studio paths exist |
| Local gap | no video clip tooling in game-time [CONFIRMED] |

### Status

Extract. Queued for game-time; Basgiath is the same build applied to different input.

## Snippets

> Author's Oct 1, 2026 Apple Silicon benchmark reports ~7.5 min for 10 clips from a
> 1h43m interview using author subtitles and cloud qwen-plus.
> [Source: Multi-Wiki Link Revenue Evaluation.docx, URL 8]

## Dead Ends

- **Deploying the full stack for a devlog.** Celery, Redis, and a React UI are overhead
  when one person runs one recording.
- **Assuming the 7.5-minute figure holds locally.** It used a cloud model.
