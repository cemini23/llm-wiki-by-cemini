---
title: "tfgh6/bedrock-ui-animations — JSON UI easing for Bedrock HUDs"
type: entity
tags: [tool, minecraft, bedrock, ui, basgiath, k283]
keywords: [bedrock-ui-animations, json-ui, easing, hud, basgiath, speedometer, stamina, k283]
related:
  - sources/eval-bedrock-ecosystem-2026-10-06.md
  - concepts/k283-eval-wave.md
  - concepts/k282-level-editors-wave.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-bedrock-ecosystem-2026-10-06.md — K283 eval (tier: Extract, Basgiath 0.85 — highest of the batch)
- @concepts/k283-eval-wave.md — K283 cluster hub
- @concepts/k282-level-editors-wave.md — Bedrock packaging wave

## Raw Concept

- **Repo:** `github.com/tfgh6/bedrock-ui-animations`
- **Tier (K283):** **Extract** (Basgiath overlap **0.85**)
- **License:** NOT FOUND (docx)
- **Stack:** Bedrock UI JSON, animation controllers, JSON UI assets (claimed)
- **Note:** listed twice in the docx (URL 13 and URL 20) — URL 20 is a duplicate, scored Pass

## Narrative

Advanced **Bedrock JSON UI animations**: easing curves, smooth progress-bar interpolation, and transition keyframes inside the Bedrock client UI engine.

### Why it matters here

Basgiath flight instruments — speedometer, altitude display, stamina bar — need smooth interpolation to look professional. This is the highest-scoring Basgiath row in the K283 batch. The technique (JSON UI easing) is small and self-contained.

### Boundary

**Free fan project.** Non-monetized; no Marketplace. Verify rendering across platform targets (Windows vs iOS/Android). Extract the JSON UI easing definitions, not the pack wholesale.

## Snippets

> "Extracting these JSON UI animation definitions enables smooth interpolation for dynamic dragon flight indicators and player stamina bars." [Source: eval-bedrock-ecosystem-2026-10-06.md]
