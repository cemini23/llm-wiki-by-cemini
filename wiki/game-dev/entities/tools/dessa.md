---
title: Dessa (Block) — full-duplex speech-to-speech model
type: entity
tags: [tool, game-dev, speech, watch]
keywords: [Dessa, Block, full-duplex, speech model, Apple Silicon]
related:
  - @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
  - entities/tools/voicestudio.md
maturity: draft
created: 2026-10-25
updated: 2026-10-25
phase_0_verdict: WATCH
wire_status: none
wire_note: Waitlist only. No weights, no SDK, no licence terms.
---

## Raw Concept

Source: v10.9 multi-wiki link evaluation, URL 18, scored Watch (Game-dev primary). Announced 2026-10-23.

## Narrative

| Field | Value |
|-------|-------|
| **Site** | https://block.xyz/dessa |
| **License** | Unreleased |
| **Availability** | Public waitlist; early access limited to vetted AI safety researchers |
| **Verdict** | WATCH |

### What is notable

A speech-to-speech model trained only on human conversation audio — no text intermediate, no pretrained text LLM. Trained on one NVIDIA GB200 NVL72; runs faster than real time on an M4 Max MacBook Pro.

It perceives and produces emotion, sarcasm, sighs, interruptions, and backchanneling natively. That is different from stitching ASR to an LLM to a TTS voice.

### Why it is Watch

Nothing shippable exists. No weights, no binary, no SDK, no pricing, no redistribution terms. The page says "Launch links are coming soon."

### Why it is not the priority

VoiceStudio already ships local voice cloning and dubbing today, under AGPL, for free. Dessa would be better at conversational emotion — but Basgiath trailers do not need backchanneling.

Revisit when weights or an SDK ship.

## Dead Ends

- Planning around Dessa before it has an artefact.
