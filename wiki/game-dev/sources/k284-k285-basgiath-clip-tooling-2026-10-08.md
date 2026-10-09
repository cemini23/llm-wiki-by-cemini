---
title: K284/K285 — Basgiath clip-production tooling (routed briefs, landed 2026-10-08)
type: source
tags: [source, triage, briefs, video, tooling, cross-wiki]
keywords: [artcraft, filmcraft, effectcraft, treg, licensenoassertion, clip-production, generative-video]
related:
  - sources/k283-bedrock-addon-extracts-2026-10-06.md
  - sources/k282-level-editors-tile-tooling-2026-10-05.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-10-08
updated: 2026-10-09
---

## Raw Concept

Two cross-wiki briefs from OSINT batches K284 (19 rows) and K285 (20 rows), landed here 2026-10-08. Both target **Basgiath** — the Bedrock fan map — and both are **clip and trailer production**, not map work. Combined verdict: one **Extract** (ArtCraft staging), three **Watch**, and **two licence flags** the originating eval did not raise. Free, non-monetised fan project.

## Narrative

### The rows

| Tool | What it is | Licence | Posture |
|------|-----------|---------|---------|
| [`storytold/artcraft`](https://github.com/storytold/artcraft) | Umbrella repo for the ArtCraft suite (6,064★, pushed 2026-10-07). "An intentional crafting engine for artists, designers, and filmmakers" | **NOASSERTION** at the API level | **Extract** — with the flag below |
| [`storytold/effectcraft`](https://github.com/storytold/effectcraft) | Headless motion-graphics rendering (1,236★) | Apache-2.0 | **Watch** |
| [`storytold/filmcraft`](https://github.com/storytold/filmcraft) | Clean-room Premiere replacement, headless NLE (2,443★) | Apache-2.0 | **Watch** |
| [`superdesigndev/treg`](https://github.com/superdesigndev/treg) | "OpenRouter for agent tools" (4,651★); paired with Fish Audio TTS and TikHub scraping for automated voiceover and TikTok clips | **NOASSERTION** — Apache-2.0 **plus additional terms** | **Extract** — with the flag below |

### The technically interesting idea — staged 3D before generative video

Generative video **drifts** on character and camera. ArtCraft's answer is to **block the scene in 3D first** — mannequin pose, camera path, staging — and render the generated clip *through* that structure. For Basgiath that is the difference between consistent dragon-flight clips and mush.

This is the same insight as the Minecraft research in @concepts/minecraft-data-driven-content-patterns.md: constrain the generative step with a structured intermediate rather than letting it free-run. Here the intermediate is a staged 3D scene; there it was a typed data component.

`effectcraft` and `filmcraft` are the layers that would **cut and finish** those clips.

### Licence flags — the part that matters

**Both `artcraft` and `treg` report NOASSERTION.** The individual K284 apps (photocraft, printcraft) verified cleanly **Apache-2.0**, and the eval flagged neither of these two. `treg` is described as Apache-2.0 **plus additional terms** — the eval did not surface that. [CONFIRMED — per the briefs]

Practical consequence: **use the per-app repos directly rather than the umbrella**, and **read `treg`'s additional terms before any wiring**. A clean-looking fan project is exactly where a licence surprise is costly.

### Gates and constraints

1. **Spend ceilings** on any TTS or scraping endpoint. Automated voiceover and clip production can run away.
2. **GPU-backed inference runs on the RunPod pod, not the laptop** — the same constraint recorded for the K283 bench task.
3. **Compare `treg` against `monid` (MIT)** before choosing a router, since one is flagged and the other is not.
4. **Clips come after the map.** Both briefs say this explicitly: do not let clip tooling delay the map bug fix or the GameTest bench.

### A workspace process note worth keeping

K285 states the rule that produced these briefs: **a prompt is one-shot; new Basgiath work is delivered as a brief in the project's own `briefs/` directory.** That is why these arrived as files rather than as instructions, and it is why this wiki can record them. [CONFIRMED — per the brief]

### Boundary

Free, non-monetised fan project. **Never Minecraft Marketplace.** No official art or book text in any clip; fan-made labels throughout.

## Dead Ends

- Wiring `artcraft` or `treg` from the umbrella repo before reading the licence. Both are NOASSERTION.
- Treating clip tooling as map work. It is promotion, and the map ships first.
- Running GPU inference on the laptop. It goes on the pod.
