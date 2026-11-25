---
title: "EventDiffusion: native event-stream distribution from video (arXiv:2611.33096)"
type: source
tags: [paper, event-camera, neuromorphic, simulation, peripheral, reference-only]
keywords: [EventDiffusion, event camera, event stream, DVS, EAD, ESA, ETD, CEFS, ESIM, v2e, DVS-Voltmeter, DSEC, EDS, BS-ERGB, CEAR, event forecasting]
related:
  - concepts/event-stream-diffusion-simulation.md
  - sources/arxiv-eventspeech-neuromorphic-tts-2605-26672.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | EventDiffusion: Learning Native Event Stream Distribution from Videos |
| Authors | Karthik Sundar Senthilkumar, Christopher Thirgood, Simon Hadfield (University of Surrey) |
| Type | arXiv preprint, cs.CV |
| arXiv | 2611.33096v1, 24 Nov 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.33096-eventdiffusion-learning-native-event-stream-dist.pdf` |
| URL | https://arxiv.org/abs/2611.33096 |
| Retrieved | 2026-11-25 |
| Pages | 32 |
| Read status | read |
| Domain fit | **Peripheral. Reference only.** The paper generates event-camera streams, not pixels. It has no T2I, T2V, LoRA, or persona content. It matters only where an event sensor enters the capture or dataset path. |

## Narrative

### Problem

Event cameras report local brightness changes asynchronously, with microsecond timing and high dynamic range. Recordings are scarce, so most event-model research depends on simulators.

An event stream between two RGB frames is underdetermined. The same frames can come from different motion, polarity, and timing. Existing simulators commit to one realization through fixed sensor models and interpolated brightness. The result is limited diversity and weak sim-to-real transfer.

### Method

EventDiffusion learns the conditional **distribution** of native event streams from paired RGB and event recordings. It splits the problem into three stages:

1. **Event Activity Diffusion (EAD)** samples discrete event counts for a time window.
2. **Event Spatial Allocation (ESA)** distributes those counts across pixels and preserves the total.
3. **Event Timing Diffusion (ETD)** samples continuous timestamps for each event.

Timestamps stay native. The user can bin the stream at any resolution after generation.

The same model **forecasts** future events from past observations, including a single RGB frame, with no future frames. Forecast quality is best from past events at short horizons; RGB frames slow the falloff at longer horizons.

### Metric

The authors introduce **CEFS**, a decomposable score on count, polarity, space-time allocation, and timing against a paired recording. They show that EQS is weak here: an empty output scores 0.94 or higher. CEFS separates real streams from empty ones.

### Results

Event-fidelity table, CEFS higher is better:

| Dataset | Best prior simulator | EventDiffusion-FT |
|---------|---------------------|-------------------|
| DSEC | 0.576 (DVS-Voltmeter) | 0.684 |
| EDS | 0.634 (V2CE) | 0.658 |
| BS-ERGB | 0.472 (ESIM) | 0.592 |
| CEAR | 0.461 (V2CE) | 0.509 |

Timing fidelity also improves: mean same-timestamp error is 0.052 against 0.078 for V2CE and 0.089 for DVS-Voltmeter. Fano-factor log error is 0.904 against 2.84 for V2CE.

Under sparse input (every fifth frame) the gap widens. Mean CEFS is 0.425 against 0.289 for ESIM, while both lose accuracy.

### Workspace relevance

No production relevance for image generation today. The wiki carries one other event-camera source, @sources/arxiv-eventspeech-neuromorphic-tts-2605-26672.md, and both point at the same horizon: event sensors beat 30 fps RGB for fast motion and lip micro-dynamics. Both need hardware that the laptop stack does not have.

A realistic use is dataset work. A future high-frame-rate motion or lipsync dataset could be simulated with plausible event timing, at low cost, and then tested against a small real recording. [OPEN QUESTION 2026-11-25]

## Snippets

> "Sparse RGB observations cannot uniquely determine intervening events since identical frames may correspond to streams with different activity, polarities, and timing." [Source: arxiv-2611.33096 p.1]

> "EventDiffusion decomposes generation into three probabilistic processes: Event Activity Diffusion (EAD) learns stochastic discrete event counts, Event Spatial Allocation (ESA) distributes these counts to individual pixels while preserving cardinality, and Event Timing Diffusion (ETD) learns continuous asynchronous timestamp distributions." [Source: arxiv-2611.33096 p.1]

> "Beyond generating events between RGB frames, EventDiffusion forecasts individual future events without requiring future RGB observations." [Source: arxiv-2611.33096 p.1]

## Dead Ends

The model needs paired RGB and event recordings for training. Public paired sets are small and sensor-specific. The paper does not state a code release in the main text `[NEEDS VERIFICATION 2026-11-25]`.
