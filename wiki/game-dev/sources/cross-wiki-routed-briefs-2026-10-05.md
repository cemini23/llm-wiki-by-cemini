---
title: Cross-wiki routed briefs — landed 2026-10-05 (4 briefs)
type: source
tags: [source, triage, cross-wiki, briefs, ingest]
keywords: [cross-wiki, briefs, routing, vlm-narration, anytalk, hydra-0, modern-cpp]
related:
  - sources/inbox-arxiv-reject-batch-2026-10-05.md
  - concepts/art-pipeline-v0-requirements.md
  - concepts/llm-npc-runtime-ai-shelf.md
  - concepts/agent-harness-castle-project.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-10-05
updated: 2026-10-05
---

## Raw Concept

Four briefs were routed into `briefs/` by sibling wikis between 2026-08-17 and 2026-09-09 and never landed as wiki pages. Each already carried a verdict from its source wiki. This page records them so the routing is auditable and the briefs are closed out. No new research was done; no verdict was changed.

## Narrative

| Brief | From | Verdict | Disposition |
|-------|------|---------|-------------|
| `2026-08-17_gameplay-vlm-narration-from-image-gen.md` | @image-gen-wiki | **SKIP** | `wont_wire` — recorded here |
| `2026-08-18_anytalk-from-image-gen.md` | @image-gen-wiki | **WATCH** | `wont_wire` here; entity stays in image-gen |
| `2026-08-19_hydra-0-from-image-gen.md` | @image-gen-wiki | **SKIP** (image-gen) | `wont_wire` — no game-dev hook yet |
| `2026-09-09_k258-modern-cpp-context.md` | @osint-wiki | **Context / SIZE-SKIP** | `wont_wire` — background only |

### Gameplay VLM narration (arXiv:2608.14016)

Cross-wiki brief from image-gen. Three mechanisms: a **3×3 temporal mosaic** packing nine sampled frames into one image so an image-native VLM sees motion at one-ninth the payload; **context-conditioned prompting** using the last K narrations as assistant-role history to stop per-segment repetition; and **duration-conditioned TTS with elastic alignment** so each utterance fills its slot without a forced aligner.

The PDF links a repository that was **404 at ingest**. No SPDX. Image-gen wired it `wont_wire` and this wiki agrees — the failure modes are hallucinated game state and mosaic resolution loss, and the value is in a persona-audio stack this wiki does not carry. **No action.**

### AnyTalk (arXiv:2608.16143)

Audio-driven **3D** facial animation for arbitrary blendshape characters with **no character animation data**. Character-specific fine-tuning adapts a video diffusion model on stills paired with zeroed audio embeddings, then uplifts the result to 3D by optimizing blendshape parameters. The distilled AnyTalkRT variant runs ~9 ms/frame.

Project page only; **no GitHub URL**, paper is CC-BY-NC-SA 4.0. Image-gen keeps the entity. Relevant here only if a future Tier 3+ NPC needs 3D speech animation — castle-sim has no such feature and Fork B art is not at rigs. **No action; revisit at Tier 3+.**

### Hydra-0 (arXiv:2608.18077)

Generalist world model conditioned on **action flow** — robot actions as pixel motion — with a shared visual interface across embodiments. Reported 90.4% lower robot-motion error and 60.2% lower object-motion error than an action-conditioned baseline.

This is robot control, not dialogue or persona. The only game-dev hook would be an interactive pixel-space world model, and this wiki's world-model work lives in CCC-primary stubs (@concepts/twin-test-time-world-model-stub.md, @concepts/vibeworlding-3d-agent-stub.md). **No action.**

### Modern C++ curriculum (K258)

`federico-busato/Modern-CPP-Programming`, CC-BY-SA-4.0 slides covering C++03–C++26. Eval tier **Context**, **SIZE-SKIP ~684 MB**. Routed from @osint-wiki.

No game-dev runtime wire. The value is systems, memory-model, and SIMD background if castle-sim performance work needs it. Godot uses GDScript and C++; the C++ surface matters only for GDExtension modules. **Background only.**

## Dead Ends

- Re-routing any of these four. Each was already triaged by its source wiki and the verdict holds here.
- Fetching the 404 narration repo. It did not exist at ingest and has not been re-checked.
- Adopting Hydra-0 as a game world model. It is a robotics result.
