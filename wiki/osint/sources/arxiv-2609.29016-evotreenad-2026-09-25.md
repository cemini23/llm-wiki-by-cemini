---
title: "EvoTreeNAD: Genealogy-Guided Evolution for Neural Architecture Discovery"
type: source
tags: [arxiv, source, k272, harness]
keywords: [k272, EvoTreeNAD, neural-architecture, not-Atto, not-HTR]
related:
  - concepts/k272-harness-evolution-wave.md
maturity: validated
created: 2026-09-25
updated: 2026-09-25
read_status: deep-read
---

## Relations

- @concepts/k272-harness-evolution-wave.md

## Raw Concept

| Paper | arXiv:2609.29016 |
| File | `arxiv-2609.29016-evotreenad-genealogy-guided-evolution-for-llm-dr.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.29016-evotreenad-genealogy-guided-evolution-for-llm-dr.pdf` |
| Archive | egress-fi 2026-09-25 |
| Authors | Lishan Yu, Derek Jiu, Qizhen Lan, Xiaoqian Jiang (UTHealth Houston) |
| Retrieved | 2026-09-25 |
| Pages | 31 |
| Dual-ID | **OSINT K272** |
| sha256 | `b7234e46e7be007677c9ea3c9e65f142f6902d15a15ff41427c9fbe299fb94a3` |
| Code | No GitHub repo in the PDF |

## Narrative

EvoTreeNAD grows a tree of neural architectures. The root is empty. Each node is one complete architecture. The search uses the top percentile of a node and its descendants to pick a lineage. A language model then reads that design history. The paper supplies no seed architecture and no hand-built search space. An Idea Agent proposes a variant and a Code Agent implements it. Each evaluated variant becomes a child node, expanding the genealogy while providing evidence for subsequent lineage selection. The paper reports CIFAR-10 test error of 2.05±0.06% and CIFAR-100 test error of 15.09±0.22%. On all six MedMNIST-v2 tasks, the discovered architectures surpass the strongest listed baselines. Controlled CIFAR-10 studies show EvoTreeNAD outperforms direct generation, best-of-N greedy continuation, and full-family-mean routing. The word genealogy in the title is an architecture tree. It is **not** civil-record genealogy. It is **not** HTR. It is **not** Atto. EvoTreeNAD is not an Atto genealogy product. Phylodynamic inference is not Atto and not HTR.

**Cemini posture:** FILE. No clone. **0 product Integrate GO.** Transkribus stays the only product HTR. Never auto-evolve skills.

## Snippets

> "Starting from an empty root, it constructs architectures without a supplied seed architecture or hand-specified search space." [Source: https://arxiv.org/html/2609.29016 (retrieved 2026-09-25)]

> "EvoTreeNAD discovers architectures that outperform the listed NAS and NAD methods, achieving test errors of 2.05±0.06% on CIFAR-10 and 15.09±0.22% on CIFAR-100." [Source: https://arxiv.org/html/2609.29016 (retrieved 2026-09-25)]