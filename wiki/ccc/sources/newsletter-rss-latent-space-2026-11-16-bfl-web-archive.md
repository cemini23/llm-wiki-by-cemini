---
title: "Latent Space — building visual intelligence with Black Forest Labs"
type: source
related:
  - concepts/frontier-model-release-cadence.md
  - sources/newsletter-rss-latent-space-2026-11-16-building-visual-intelligence-andreas-blattmann-d.md
  - concepts/harness-attribution-multimodal-eval.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Building Visual Intelligence — Andreas Blattmann & Dustin Podell, Black Forest Labs |
| Author | Latent Space (swyx, Alessio Fanelli) |
| Type | Newsletter podcast recap (RSS, free tier) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-16-bfl-web-archive.md` |
| Retrieved | 2026-11-22 (published 2026-11-16) |
| Pages | n/a |
| Read status | read |

## Narrative

This page and `@sources/newsletter-rss-latent-space-2026-11-16-building-visual-intelligence-andreas-blattmann-d.md` are the same episode captured twice from two URLs. Keep both for provenance; read either.

The episode covers FLUX 3, which Black Forest Labs trains on video, image and audio together. The argument for using video is that a clip carries evidence about how objects look from other angles. The argument for audio is timing: a sound can mark an impact the camera missed.

One engineering detail is reusable. If each frame is sharpened independently, the result shimmers when played, because the upscaler makes a different decision per frame. BFL derives its video upscaler from the same FLUX 3 backbone so the decisions stay temporally consistent.

The episode also compares autoregressive and diffusion training. Autoregressive models learn from all tokens at once; diffusion models can be distilled to a few sampling steps. Which matters depends on whether you pay for training or for latency.

Fit for CCC is low. It is image and video generation, which `@image-gen-wiki` owns. It is filed here only for the model-landscape note.

## Snippets

> "Sharpen each frame of a clip independently and each frame might look terrific. Hit play and the extra detail can shimmer, because the upscaler made a slightly different decision every time." [Source: newsletter-rss-latent-space-2026-11-16-bfl-web-archive.md]
