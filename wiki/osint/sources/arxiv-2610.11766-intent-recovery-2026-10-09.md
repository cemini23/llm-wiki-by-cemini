---
title: "Intent recovery in LLM safety evaluation (arXiv 2610.11766)"
type: source
tags: [source, k287, arxiv, safety, eval]
keywords: [intent-recovery, operative-understanding, ASR, IRIS, k287]
related:
  - concepts/k287-arxiv-wave.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
read_status: read
---

## Relations

- @concepts/k287-arxiv-wave.md

## Raw Concept

| Title | Same Outcome, Different Evidence: Intent Recovery in LLM Safety Evaluation |
| Authors | Haitong Jiang, Chunlin Liu, Sihan Tang, Chan Wu, Xiaoqing Su, Yuhong Feng |
| Type | arXiv preprint |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.11766-same-outcome-different-evidence-intent-recovery.pdf` |
| Retrieved | 2026-10-09 |
| arXiv | 2610.11766v1 |
| Licence | CC BY 4.0 |
| read-status | read |

## Narrative

Attack success rate treats every non-harmful answer as one outcome. The paper splits that outcome. The model may recover the harmful task and refuse it, miss the task, or answer a different task.

Operative understanding rate asks whether the response names the evaluated task and treats it as the task to answer. Similar attack-success numbers can hide very different recovery rates. Code is named at `kevinjiang0121-cyber/IRIS`. This page does not install that repo and does not copy attack text.

## Snippets

> "Non-harmful outcomes are not equally informative about model safety." [Source: arxiv-2610.11766 PDF, abstract]
