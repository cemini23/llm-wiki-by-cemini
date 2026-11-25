---
title: "ffmpeg-skill — 42 local FFmpeg operations for a coding agent (MIT)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-16-deep-research-link-eval-game-media.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - entities/tools/autoclip.md
updated: 2026-11-16
maturity: draft
---
## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-16-deep-research-link-eval-game-media.md, URL 7,
**Extract** tier. Routed to game-time.

The question this page answers: **how does an agent verify a rendered frame without
guessing at FFmpeg flags?**

## Narrative

### What it does

A local video editor for coding agents. It exposes 42 FFmpeg operations behind a
machine-readable interface — probe, trim, extract frames, transcode, overlay, measure —
so an agent calls an operation instead of composing a shell pipeline.

Everything runs on the local FFmpeg binary. No upload.

### Why it fits game-time

game-time renders a browser game. A visual change is verified by looking at a frame, and
today that means a human opening the export. Phase-0 on 2026-11-16 found no `ffmpeg`
reference anywhere under `Game time/packages`. [CONFIRMED]

A deterministic frame extract, probed for resolution and colour, closes a real
acceptance-test gap: the agent renders, extracts, and compares without a human in the
loop for the mechanical part.

The determinism matters more than the operation count. The same input must produce the
same frame, or the comparison means nothing.

### Maturity

6.6k stars, pushed the day of the check, 33 open issues, MIT. Active and small.

### Status

Extract. The interface shape and the operation set are the value; the skill wrapper
itself is blocked by the Workstation Harness Freeze.

### Merged into the deferred clip blueprint, 2026-11-24

This operation set now sits inside one deferred item with
@entities/tools/autoclip.md. The standalone `tools/clip-pipeline/` wrapper serves two
consumers from the same FFmpeg layer: marketing clips, and the before/after frame
comparison used for render acceptance.

**Status: DEFERRED / ON-DEMAND**, triggered by the first recorded devlog or Basgiath
showcase. The frame-comparison half needs no scoring or subtitles, so it can ship
first when the trigger arrives.

## Snippets

> Local video editor for coding agents: 42 FFmpeg tools with a machine-readable
> interface.
> [Source: Cemini Multi-Wiki Link Evaluation (1).docx, URL 7]

## Dead Ends

- **Wrapping FFmpeg by hand per test.** That is the gap; do not rebuild it ad hoc.
