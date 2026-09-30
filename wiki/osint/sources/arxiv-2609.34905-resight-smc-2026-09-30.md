---
title: "ReSight-SMC: two-stage power sampling for LVLMs (2609.34905)"
type: source
tags: [source, k276, ood, inference, vlm]
keywords: [k276, smc, test-time, mit, no-clone]
related:
  - concepts/k276-ood-stub-wave.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: skimmed
---

## Relations

- @concepts/k276-ood-stub-wave.md

## Raw Concept

| File | `arxiv-2609.34905-resight-smc-two-stage-power-sampling-via-island.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.34905-resight-smc-two-stage-power-sampling-via-island.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `a528f65232cca9aeebf0a4e5dc6255620d15477a224bf5134735e674c5659d2c` |
| arXiv | 2609.34905 |
| Authors | Yaowen Zhang, Xiangyu Qiu, Zhi Lu, Wenwen Tian, Aoqin Wang, Junhai Luo, Zhenming Peng, Junyi Hu |
| Repo | `https://github.com/yaowenzhang1/resight-smc` |

## Narrative

ReSight-SMC is a verifier-free sampler for large vision-language models. It transfers Power-SMC to model decoding. It fixes two finite-particle weaknesses: genealogy collapse from global resampling, and trajectory-level sharpening.

Stage one runs ancestry-isolated island SMC. Stage two pools terminal importance mass by canonical answer, then samples an answer with a supporting trajectory.

The authors report wins on 18 of 20 benchmark results over Power-SMC. On an RTX 5090 latency rises from 4.11 s to 10.37 s.

The authors admit the readout cannot repair a wrong first-stage mode. Free-form answers that cannot merge deterministically fragment the mass and need an external judge. Logit access limits the method to open-weight models.

The word "genealogy" here means particle ancestry. It is unrelated to our genealogy work.

Repo license is MIT, 954 KB, 0 stars (gh api 2026-09-30). No clone. This is an inference-time sampler, not an agent harness. Do not wire it.
