---
title: "TinyAstral — transferring evolved harnesses to small generalist agents"
type: source
tags: [source, arxiv, agents, harness, distillation, robotics]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents |
| Authors | Kehong Gong, Xiaoxu Zheng, Guanli Hou, Seunghun Lee, Mengqi Guo, Runjia Tan, Zhengyu Wen, Qi Wang, Xiaoyu He, Mingyuan Zhang, Michael Bi Mi |
| Affiliations | Huawei; Huawei Noah Research Institute |
| arXiv | 2610.41216 |
| Pages | 16 |
| Read status | skimmed (title page and result figure) |

## Narrative

The claim: a **harness evolved by a large teacher can be transferred to a small student**, rather than evolved separately for each model size.

Reported figures from the results page — RoboTwin-50 success:

| Configuration | Success |
|---------------|---------|
| Teacher (180B, DeepSeek-V4.1) | **63.6** |
| Qwen3.5-4B, untrained | 14.6 |
| TinyAstral-4B, distilled | **62.8** |
| untrained baseline | 41.2 |

Plus gains quoted of **+21.6 pp distilled**, **+30.2 teacher**, **+26.6 untrained**, and a six-benchmark spread reaching 93.6 on one suite.

### What the result would mean

If a harness evolved against a large model transfers to a 4B model and keeps most of the gain, then **harness evolution is a reusable asset** rather than a per-model tuning exercise. That would make the harness the durable thing and the model the swappable thing — which is the same conclusion CLEO reaches from the pruning direction.

The 62.8 against 63.6 is the number that carries the claim: at 4B it is within about a point of the 180B teacher.

### Caveats

- **Title page and figure only.** No method details, no ablation, no statement of what "distilled" covers — weights, harness, or both.
- The benchmarks are robotic manipulation. Transfer to text or code harnesses is untested here.
- Numbers are read off a results figure, not from a table.

## Snippets

> "harness evolution (H1 → H*)" with RoboTwin-50 success: teacher 63.6, TinyAstral-4B distilled 62.8 [Source: arxiv-2610.41216 p.1 figure]

## Dead Ends

- **Reading these numbers as a table.** They are off a figure.
- **Assuming text-domain transfer.** Manipulation benchmarks only.
