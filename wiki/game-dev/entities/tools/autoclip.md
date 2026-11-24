---
title: "autoclip — deferred blueprint for a local clip and frame pipeline (MIT)"
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
**Extract** tier.

**Status: DEFERRED / ON-DEMAND.** We build nothing now. This page holds the ready
recipe so the research is not repeated when the trigger arrives.

**Trigger:** the first recorded game-time devlog, or the first Basgiath
(`dragon-rider-map`) showcase that needs distribution clips. Neither exists yet.

The question this page answers: **what do we build, and what do we refuse, when a
recording finally exists?**

## Narrative

### What the source gave us

`autoclip` is a Python pipeline: transcribe, score highlights, reframe to vertical,
burn subtitles, generate covers and platform copy. It ships FastAPI, Celery, Redis,
SQLite, a React UI, an MCP server, and desktop bundles.

The value is the **decomposition**, not the application. We take the stage list and
rebuild it small.

### Target placement

A standalone Python and FFmpeg CLI at `tools/clip-pipeline/`, **outside** the
`game-time` `packages/` build graph. It must not enter pnpm, the sim-core typecheck, or
the renderer bundle.

One entry point, two profiles:

```bash
tools/clip-pipeline/run.py --profile game-time   <input> --out <dir>
tools/clip-pipeline/run.py --profile basgiath    <input> --out <dir>
```

The profile selects labels, title templates, and asset rules. The pipeline code does
not branch.

### Two consumers, one wrapper

The same FFmpeg wrapper serves two jobs. They share decoding, probing, and keyframe
selection, and nothing else.

| Consumer | Job | Output |
|----------|-----|--------|
| Marketing | Cut vertical clips from recorded footage | 1080x1920 MP4, burned SRT, cover frame |
| Acceptance test | Compare a frame before and after a render change | Two PNGs and a diff verdict |

The acceptance path is the smaller one and can ship first, because it needs no scoring
and no subtitles — only a deterministic frame extract at a fixed timestamp.

### Two input modes

**Narrated devlogs** — the operator speaks. Transcribe with optional local Whisper
(~220 MB). Timestamps come from the transcript, so highlight selection is a text
problem.

**Speech-sparse gameplay** — the operator mostly does not speak. Transcription returns
little, so use scene-change detection or uniform keyframe extraction, tiled into
storyboard contact sheets.

The storyboard approach has a hard budget. Cap at **4 storyboards of roughly 8.5k image
tokens each**, about 17k tokens total, well under Claude Code's 25,000-token MCP
ceiling. Sparse keyframes plus a summary beat uniform sampling, because uniform
sampling spends the budget on the middle of a clip where nothing happens.

### Scoring order

1. **Local heuristics first** — scene-change magnitude, audio energy, motion density.
   No model, no download, deterministic.
2. **Optional local vision second** — an Ollama vision model re-ranks the heuristic
   shortlist. It never sees the full recording, only the candidate frames.

Scoring is a ranking problem over a small set, not a description task over an hour of
video.

### Review gate

The pipeline stops at a manifest. Nothing renders until a human reads it.

`candidates.json` holds, per candidate:

- start and end timestamps
- score and the reason for it
- cover timestamp
- title and tags
- profile

Render is a second command that consumes the approved manifest.

### Output specification

- 1080x1920 vertical
- burned-in SRT
- cover frame exported as a separate PNG
- title and tags written next to the clip

### Caveats

**The 7.5-minute benchmark does not transfer.** The author's 2026-10-01 Apple Silicon
run produced 10 clips from a 1h43m **dialogue-heavy interview** using **cloud
`qwen-plus`**. Our case is local, speech-sparse, and gameplay footage. Do not quote
that figure as a local expectation. [TENTATIVE — author-reported]

**A 20 GB vision model competes with the game.** If local Ollama scoring runs on the
same machine as a capture session, measure before committing to it.

### Hard exclusions

Not vendored, not installed, not run:

- **FastAPI, Celery, Redis, React, SQLite UI** — a job server and a web app for a
  one-person, one-recording task.
- **Platform uploaders** — no automated posting to TikTok, Reels, or Shorts. Upload is
  a human step.
- **Unsigned desktop installers** — no prebuilt bundles from the project.
- **`autoclip-mcp` and `npx skills add`** — blocked by the Workstation Harness Freeze
  (Gate 3 of @osint-wiki/concepts/agent-link-evaluation-gates-v1013.md). The pipeline
  is a CLI we call, not a skill we install.
- **Any cloud ASR or cloud vision call** — the whole point is that footage stays local.

### Basgiath rules

`dragon-rider-map` is fan work. Every clip carries a **"Fan-made" label**, is
**non-monetized**, and contains **zero trademarked assets**. The pipeline enforces this
through the profile: the `basgiath` profile stamps the label and rejects any input
flagged for monetization.

### Phase-0, 2026-11-24

| Check | Result |
|-------|--------|
| Licence | MIT [CONFIRMED — GitHub API] |
| Maturity | 15k stars, 2.2k forks, 40 open issues |
| Cloud requirement | optional upstream — local Whisper and Ollama paths exist |
| Local gap | no video tooling in game-time [CONFIRMED — no `ffmpeg` under `packages/`] |

### What was already shipped

`atto` proved the local-engine guard pattern in `video_gate.py`: run the local engine,
keep the cloud key out of the environment, and assert no network call. Reuse that shape
here rather than inventing a second one.

## Snippets

> Author's Oct 1, 2026 Apple Silicon benchmark reports ~7.5 min for 10 clips from a
> 1h43m interview using author subtitles and cloud qwen-plus.
> [Source: Multi-Wiki Link Revenue Evaluation.docx, URL 8]

> Default 4 storyboards / ~8.5k image tokens; max 128 keyframes across 8 storyboards /
> ~17k tokens under Claude Code's 25,000-token MCP ceiling.
> [Source: Multi-Wiki Link Revenue Evaluation.docx, URL 18]

## Dead Ends

- **Deploying the full stack for a devlog.** Celery, Redis, and a React UI are overhead
  for one person and one recording.
- **Assuming the 7.5-minute figure holds locally.** It used a cloud model on dialogue.
- **Uniform frame sampling.** It spends the budget on the boring middle.
- **Building this before a recording exists.** Deferred until the trigger.
