---
title: Generative event-stream simulation (diffusion from video)
type: concept
tags: [concept, event-camera, neuromorphic, simulation, dataset, reference]
keywords: [event camera, DVS, event stream simulation, ESIM, v2e, DVS-Voltmeter, CEFS, event forecasting, EAD, ESA, ETD, high-frame-rate capture, lipsync]
related:
  - sources/arxiv-2611-33096-eventdiffusion-native-event-stream.md
  - sources/arxiv-eventspeech-neuromorphic-tts-2605-26672.md
maturity: draft
created: 2026-11-25
updated: 2026-11-25
---

## Raw Concept

The question this page answers: how do you get realistic event-camera data when recordings are scarce, and when does that matter for this wiki? Synthesized from @sources/arxiv-2611-33096-eventdiffusion-native-event-stream.md and @sources/arxiv-eventspeech-neuromorphic-tts-2605-26672.md.

## Narrative

### What an event camera is

An event camera reports local log-intensity changes that pass a contrast threshold. Each event carries a pixel, a polarity, and a microsecond timestamp. There is no frame. The advantages are microsecond timing and high dynamic range; the cost is sparse, non-grid data that standard pipelines do not accept.

### Why simulation is hard

Two RGB frames cannot fix the events between them. Different motion paths produce the same endpoints with different activity, polarity, and timing. Physics simulators (ESIM, v2e, DVS-Voltmeter, IEBCS) pick one trajectory and apply a fixed sensor model. Learned simulators (V2CE, FracEvent) predict an aggregate representation. Both approaches commit to a single answer where a distribution belongs.

### The generative approach

Learn the conditional distribution instead. EventDiffusion factors the problem:

- **Count**: how many events in a window (discrete diffusion).
- **Space**: which pixels carry them, with the total preserved (allocation, not independent sampling).
- **Time**: when each event fires (continuous diffusion).

Native timestamps survive generation. The same stream can be binned at any rate for downstream training, so one generation serves several consumer formats. The model also forecasts forward from past events or from a single frame.

### Measurement

Event-stream metrics are not interchangeable. EQS rates an empty output at 0.94 or higher. The CEFS score compares count, polarity, space-time allocation, and timing against a paired recording, and it separates empty from real. Any future event-simulation work in this wiki should report CEFS, not EQS alone.

### When this matters here

Neither event source in this wiki has a production path. Both point at one opportunity: an event sensor sees fast motion and lip micro-dynamics that 30 fps RGB blurs. EventSpeech argues that RGB exposure smears lip dynamics and flattens TTS prosody. EventDiffusion supplies a way to synthesize the missing event training data.

[OPEN QUESTION 2026-11-25] Neither claim is tested on this workspace's hardware. The test needs an event camera and a paired RGB rig, and neither is on the laptop. Treat this page as a research horizon note, not a build track. RGB plus a lipsync model remains the canonical persona path.

## Snippets

> "Event cameras asynchronously report local log-intensity changes exceeding a contrast threshold. Their microsecond-scale temporal resolution and high dynamic range suit fast motion and challenging illumination." [Source: arxiv-2611.33096 p.1]
