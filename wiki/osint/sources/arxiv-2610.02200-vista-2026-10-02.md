---
title: "VISTA: a visual harness for reasoning (2610.02200)"
type: source
tags: [source, k278, harness, agents, vision]
keywords: [k278, vista, visual-memory, arc-agi-3, no-clone]
related:
  - concepts/k278-harness-wave.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
read_status: skimmed
---

## Relations

- @concepts/k278-harness-wave.md

## Raw Concept

| File | `arxiv-2610.02200-vista-a-visual-harness-for-reasoning-in-an-inter.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.02200-vista-a-visual-harness-for-reasoning-in-an-inter.pdf` |
| Archive | egress-fi 2026-10-02 |
| Retrieved | 2026-10-02 |
| sha256 | `40c95e5ebed5f50fe696462177a2561352027ef85fd28293dbd5e2cc221e838a` |
| Dual-ID | **OSINT K278** |
| arXiv | 2610.02200 |
| Authors | Qiushi Han, Keya Hu, Linlu Qiu, Cathy Wu, Kaiming He (MIT) |
| Repo | `https://github.com/joshhhhhan/VISTA` |

## Narrative

The claim is that multimodal models already reason well, and a suitable harness unlocks that ability in interactive visual environments.

VISTA is a purely mechanical harness with **no trained model**. It renders observations for the model, stores every returned frame at full resolution in an addressable memory, and exposes tools to zoom into a region, retrieve a past frame, and read pixels. The model reasons in free-form language and calls one action per turn. The author calls this giving a model long-horizon vision.

Evaluated on 25 public ARC-AGI-3 games, plus three other environments.

| Setting | Result |
|---------|--------|
| VISTA with one frontier model | Perfect 100.00 relative human action efficiency, 7,302 actions |
| Human reference | 17,135 actions |
| Same model, official no-program baseline | 40.68 |
| Ablation, minimal to full harness | 13.33 to 47.32 to 99.00 |
| Second frontier model, VISTA | 99.00 |
| Open-weight model, official then VISTA | 1.89 then 66.93 |
| Token cost, image observations vs text grids | 30.7M vs 71.9M per game |

Two findings stand out. First, the harness alone moved an open-weight model from 1.89 to 66.93 without any change to the model. Second, image observations used **less than half the tokens** of text grids at a similar score.

The authors admit the obvious confound. The models postdate the public benchmarks, so training-data contamination cannot be ruled out. Evaluation on novel or private games would be a stronger test. They also state that model capability remains the key factor; the harness only elicits it.

This is the strongest harness result in the wave, and it pairs with the coherence paper: VISTA owns **visual memory**, the coherence paper argues the harness must own **state**. Different state, same principle.

License not yet checked by `gh api`. No clone. Do not swap `/route`.
