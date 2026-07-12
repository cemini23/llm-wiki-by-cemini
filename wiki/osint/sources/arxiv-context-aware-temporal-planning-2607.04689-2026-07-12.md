---
title: Reliable context-aware temporal planning for autonomous driving (2607.04689)
type: source
tags: [source, arxiv, robotics, perception, k160]
keywords: [RCT-AD, BEV, quality-gated memory, nuScenes, temporal planning]
related:
  - concepts/tool-evaluation-framework.md
maturity: draft
read_status: skimmed
created: 2026-07-12
updated: 2026-07-12
---

## Relations

- @concepts/tool-evaluation-framework.md — REFERENCE only; no co-primary brief route

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.04689](https://arxiv.org/abs/2607.04689) |
| **Title** | A Reliable Context-Aware and Temporal Planning Framework for Autonomous Driving (RCT-AD) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.04689-2607-04689v1-a-reliable-context-aware-and-tempor.pdf` |
| **Verdict** | **REFERENCE** — autonomous driving BEV; weak hook to castle-sim / poker / PM co-primary lanes |

## Narrative

End-to-end BEV perception-planning with **reliability-gated temporal fusion**: per-frame quality scores + FILO memory retain trustworthy features; corrupted camera frames reconstructed from reliable history before trajectory planning. Joint detection-segmentation head feeds semantic/motion cues. nuScenes benchmarks reported (NDS 61.5, mAP 52.9, mIoU 52.3).

**Cemini posture:** wiki-only. Tangential pattern steal for any future **multi-agent sim replay** quality gating (discard degraded observations before state commit) — not sufficient for castle-sim brief unless RTS sensor-fusion research reopens.

## Snippets

> "When degraded observations are aggregated indiscriminately over time, trajectory planning becomes unstable" [Source: arXiv:2607.04689 abstract — paraphrase]

> "Quality-gated First-In-Last-Out (FILO) memory mechanism" [Source: arXiv:2607.04689 abstract]
