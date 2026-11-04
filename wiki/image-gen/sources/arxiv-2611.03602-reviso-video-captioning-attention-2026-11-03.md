---
title: "Reviso — not all visual evidence deserves equal attention in video captioning"
type: source
tags: [source, arxiv, video, captioning, multimodal, attention]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Reviso: Not All Visual Evidence Deserves Equal Attention in Video Captioning |
| Authors | Tengfei Liu, Yang Shi, Yuran Wang, Yuqi Tang, Yizhuo Jia, Zhuoran Zhang, Qixun Wang, Shujie Li, Xuanyu Zhu, Xinyu Liu, Minghui Guo, Shixuan Liu, Haotian Wang, Yuanxing Zhang, Pengfei Wan (PKU, KlingAI Research, HKUST, FDU, HKU, NUS, THU) |
| arXiv | 2611.03602 |
| Pages | 13 |
| Read status | skimmed (abstract) |

## Narrative

Multimodal models can caption video in detail, and they frequently **overemphasise minor details while missing essential context and key events**. The paper's premise: not all visual evidence deserves equal attention, and what matters depends on the video's content.

**Reviso** is an agentic captioning framework that **learns what to observe and how to gather the relevant evidence**. From a low-frame-rate global preview it builds a hierarchical context, then decides where to look.

### Why the two-stage design is the point

Uniform frame sampling treats a static conversation and a fast action sequence identically, and it is the standard approach. A global preview first, then selective attention, is the same economy as a resolver that reads a skeleton before descending into a subtree.

The failure it fixes is diagnosable: a caption that names the background objects and misses the event is a symptom of the model having seen everything equally.

### Relevance here

Video captioning is a step in any clip-generation review loop — Basgiath promo clips, game-time assets, collectibles listings. A caption that misses the event is worse than a short one.

**Caveat.** Abstract only. No benchmark figure reproduced.

## Snippets

> "We argue that not all visual evidence deserves equal attention, as the importance of visual information depends on the content of each video." [Source: arxiv-2611.03602 p.1]

## Dead Ends

- **Citing a captioning score.** Abstract only.
