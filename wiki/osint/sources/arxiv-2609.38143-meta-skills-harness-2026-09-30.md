---
title: "Learning meta-skills for agent harness design (2609.38143)"
type: source
tags: [source, k276, agents, harness, meta-skills]
keywords: [k276, meta-skills, builder-target, FILE]
related:
  - concepts/k276-harness-evolution-wave.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: skimmed
---

## Relations

- @concepts/k276-harness-evolution-wave.md

## Raw Concept

| File | `arxiv-2609.38143-learning-meta-skills-for-agent-harness-design-in.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.38143-learning-meta-skills-for-agent-harness-design-in.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `d65734122be476dfc6715c8b827847da8fbadc778c291276fffe1fc6656758bc` |
| arXiv | 2609.38143 |
| Authors | Cheng Qian, Kunlun Zhu, Beibin Li, Zhenhailong Wang, Heng Ji (Apodex; UIUC) |
| Repo | `https://github.com/qiancheng-apodex/MetaSkill-AI4AI` |

## Narrative

The paper studies test-time AI-for-AI. One model, the Builder, constructs the execution environment for another, the Target. Both sets of weights stay fixed.

The contribution is the idea of a meta-skill: a principle that says when support is needed and what resource to provide. The Builder learns these principles from the Target's execution feedback on a development set. It then uses the frozen skill bank to build harnesses for unseen tasks.

Results: a full meta-skill bank improves macro-average performance by 8.95 percentage points over building with no skills, and by 12.02 points over giving the same bank straight to the Target. The authors note that gains when one model plays both roles suggest a path to system-level self-improvement.

The distinction worth keeping: a task skill tells you how to do the work; a meta-skill tells you how to build the environment. That split matches our own skill-versus-rule separation.

The authors admit the study uses one main Builder, two benchmarks, and one run per condition. Cross-Builder transfer intervals include zero, and revised guidance can become over-specific.

Repo SPDX is **null**, 466 KB, 1 star (gh api 2026-09-30). A null SPDX records the pattern only. No clone. Do not auto-evolve our skill bank from this paper. FILE only.
