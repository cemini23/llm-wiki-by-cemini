---
title: "claude-video — video ingest for agents (MIT; the default engine is a cloud upload)"
type: entity
tags: [tool, video, agents, transcription, whisperx, local, mit]
keywords: [claude-video, frame extraction, whisperx, gemini engine, local engine, ban-4]
related:
  - "@osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-11.md"
maturity: draft
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-11.md, URL 16, **Integrate** tier. Routed to Collectibles and game-time.

The question this page answers: **can an agent watch a video without the video going anywhere?**

## Narrative

### What it does

An agent skill for Claude Code, Codex, and other Agent Skills hosts. Turns a URL or local file into **timestamped frames plus a transcript**, so the agent can answer questions about the video.

**MIT.** Frames capped at 100, sampled every 5 seconds, auto-scaled, aligned against native captions or a local WhisperX transcript.

### Phase-0, 2026-11-11 — the data path is engine-dependent

The report rates this Integrate and does not discuss where the video goes. It depends entirely on which engine runs.

| Engine | Condition | What happens |
|--------|-----------|--------------|
| **Gemini** | **Default when a key is present** | YouTube links go straight to Google. Other URLs and **local files are uploaded to Google's Files API**. Uploads are supposedly deleted after the answer; an undeletable upload expires within 48 hours. `--start`/`--end` limit what Google analyses. |
| **Local** | Default with no key | ffmpeg/yt-dlp on the machine. Nothing is sent. |
| WhisperX | Key-free | Runs wherever the agent executes — on the laptop, audio stays local; in a cloud session it does not. |
| Groq / OpenAI | Optional speech backends | Extracted audio goes to whichever provider is chosen. |

**This is a ban-4 hazard with the same shape as the last four batches.** A key in the environment silently selects the cloud path. On this machine that is the normal state.

**The fix is the same as `jevals`:** use the local engine, and assert in a test that no network call happens.

### Setup cost

Python 3.12 in a **separate environment**, about 3 GB disk, 8 GB RAM. WhisperX downloads models on first use and needs network for that; later runs work from cache.

That is not trivial on a laptop already running local models, but it is a one-time cost.

### What it is for

- **Collectibles** — review a raw-card video for condition and centering before grading. The frames are timestamped, so a finding points at a moment.
- **game-time** — extract gameplay reference from Travian or Civ Revolution footage without uploading someone else's video.

### Status

Integrate, **local engine only**. Set no provider keys, or pin the engine explicitly.

## Snippets

> "**Gemini engine (default when a key is present):** YouTube links are sent straight to Google. Other URLs and local files are uploaded to Google's Files API." [fetched 2026-11-11]

> With no key, it defaults to the **local engine**; WhisperX is key-free and handles videos without captions. [fetched 2026-11-11]

## Dead Ends

- **Running the default with a Gemini key present.** Local files are uploaded.
- **Assuming WhisperX keeps audio local in a cloud session.** It runs where the agent runs.
