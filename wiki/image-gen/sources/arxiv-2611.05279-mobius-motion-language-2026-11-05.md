---
title: "MÖBIUS — one motion model for understanding, generation, completion and editing"
type: source
tags: [source, arxiv, motion, multimodal, generation, editing]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | MÖBIUS: A Unified Motion-Language Model Bridging Understanding and Generation |
| Authors | Jiazhi Shu, Chengfeng Zhao, Jinyi Wang, Yubo Zhao, Zhiyang Dou, Ronghui Li, Yu Lu, Xinwei Jiang, Zijiao Zeng, Yuan Liu (HKUST, Tencent Games Motus, MIT) |
| arXiv | 2611.05279 |
| Pages | 21 |
| Read status | skimmed (abstract and figure page) |

## Narrative

A unified **motion-language model** that handles four tasks in one system: generation, completion, editing, and understanding.

The example interactions on the title page are the clearest description:

| Task | Exchange |
|------|----------|
| **Generation** | "A soldier on a battlefield — what might he do?" → "He might run forward while holding a firearm. Let me generate this motion." |
| **Completion** | "Can you turn this into a more complete motion sequence?" → rappel, run, crouch, fire |
| **Editing** | "Suppose there is a crater at frame 230. How would the soldier react?" → "I'll add a jumping and landing sequence between frames 200–260." |
| **Understanding** | "Describe the final motion" → a full sequence description |

### The design point

Generation and understanding are usually separate models with a motion representation between them. Here the **same representation serves both directions**, so editing at a specific frame and describing the result are the same kind of operation.

The frame-level editing — a crater at frame 230 produces a jump inserted at 200–260 — is the concrete capability. It is **conditional motion insertion with a time window**, which is what a shot-construction workflow actually needs.

### Relevance

For game and clip production, the useful capability is targeted: change one moment in a motion sequence without regenerating the whole thing. That is the same economy as keyframe editing versus full re-render.

**Caveat.** Abstract and figure page only. No quality metric reproduced.

## Snippets

> "Suppose there is a crater at frame 230. How would the soldier react?" → "He would jump over it. I'll add a jumping and landing sequence between frames 200–260." [Source: arxiv-2611.05279 p.1]

## Dead Ends

- **Citing a motion-quality metric.** Figure page only.
