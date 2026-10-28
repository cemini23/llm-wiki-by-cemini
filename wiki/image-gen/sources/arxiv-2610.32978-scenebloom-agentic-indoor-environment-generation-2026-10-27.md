---
title: "SceneBloom — agentic generation of physically valid 3D indoor scenes"
type: source
tags: [source, arxiv, 3d-generation, scene-generation, agents]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning |
| Authors | Yuhan Liu, Lianhui Qin, Shenji Wan (New York University; UC San Diego) |
| arXiv | 2610.32978 |
| File | `arxiv-2610.32978-scenebloom-agentic-indoor-environment-generation.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.32978 |
| Read status | skimmed (abstract + intro) |

## Narrative

The problem is the gap between a good-looking generated scene and a scene that is physically valid. Visual generative models hold strong priors about plausible furniture arrangements. Their outputs still need geometric reasoning before they become valid 3D scenes. Language-guided methods plan semantics well but ground space poorly.

SceneBloom attacks the gap with a two-stage agentic design. A **hierarchical sampler** uses diffusion priors to place furniture inside functional zones. A **compiler** then reads the relations out of each proposal and uses them to drive geometric fitting and local pose correction. The compiler is the part that converts a picture into a scene.

The reported results are concrete. Across **five room types** the method attains the highest visual quality and physical stability among the compared methods. It is also **the only method with no detected mesh collisions and no out-of-bounds objects**. Its layouts sit closer to the distribution of real rooms than every baseline. One comparison figure puts SceneBloom at 100% against SceneWeaver at 18% on one validity measure.

The downstream result is the one worth keeping. Object-navigation policies trained in these generated scenes reach a **higher success rate on held-out real scans** than policies trained on an equal number of real training scans. Synthetic environments therefore beat a matched budget of real ones for this policy, which is a stronger claim than "synthetic data helps."

Code is public at `github.com/Tinaliu0123/scenebloom`.

Single source, abstract-level read. The count of generated scenes and the exact baseline set are not recorded here.

## Snippets

> "A hierarchical sampler uses diffusion priors to generate furniture arrangements within functional zones. A compiler then uses relations extracted from each proposal to guide geometric fitting and local pose correction." [Source: `arxiv-2610.32978-scenebloom-agentic-indoor-environment-generation.pdf` p.1 (arXiv 2610.32978), retrieved 2026-10-27]

> "Object navigation policies trained in these realistic scenes achieve a higher success rate in held-out real scans than those trained on an equal number of real training scans." [Source: `arxiv-2610.32978-scenebloom-agentic-indoor-environment-generation.pdf` p.1 (arXiv 2610.32978), retrieved 2026-10-27]
