---
title: "CONTRA: behaviour-changing questions for selective clarification (2610.01769)"
type: source
tags: [source, k279, agents, verification, harness]
keywords: [k279, contra, clarification, self-report-gap, no-clone]
related:
  - concepts/k279-harness-wave.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
read_status: skimmed
---

## Relations

- @concepts/k279-harness-wave.md

## Raw Concept

| File | `arxiv-2610.01769-contra-discovering-and-qualifying-behavior-chang.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.01769-contra-discovering-and-qualifying-behavior-chang.pdf` |
| Archive | egress-fi 2026-10-03 |
| Retrieved | 2026-10-03 |
| sha256 | `d6d8b0ee61b1ff5964a4cbfc3a88d63c63539ff3845d2216ea2540c2236901aa` |
| Dual-ID | **OSINT K279** |
| arXiv | 2610.01769 |
| Authors | Zheng Fang, Yongmin Li, Yichang Zhang, Dongming Jin, Haoyu Wang, Shuai Wang, Ge Li (Peking University); Zhi Jin (Wuhan University) |
| Repo | `https://github.com/fangz-cs/Contra` |

## Narrative

Coding agents silently resolve underspecified requirements. The code looks right and does not match intent. Asking the developer early fixes this, but asking too much wastes their time.

The method is training-free, in three stages. **Discovery** generates candidate questions and merges duplicates, each with two plausible answers. **Qualification** keeps only the questions that are relevant, not already settled by the requirement, and **behaviourally verified** — it generates three programs per answer, runs them on shared inputs, and keeps the question only when the two answer groups produce stable, *differing* outputs. **Selection** uses the interaction history to ask the next useful question or stop.

### The number that matters here

As a Claude Code plugin, an independent review found that **116 of 262 reported decisions (44.3%) were absent from the agent's own report.** Reporting "all three elements" rose from 2.9% to 46.3% with the plugin.

That is the same rule again, from the software-engineering side. **The agent's account of what it decided is incomplete by nearly half.** It is not lying; it does not track its own implicit decisions. You need an outside check that reads the artifact.

### Other results

Macro-average F1 of 41.20% and TKQR of 38.32%, beating the best baseline by 13.88 and 12.33 points. With one model, F1 19.86% against 9.63% for a production coding agent and 10.61% for another. False-positive rate 5.00%. A "Flash" variant cuts qualification evaluations by 65.7% to 96.0%.

The behavioural-verification step is the transferable technique: generate two implementations from the two candidate answers, run them on the same inputs, and keep the question only if the outputs actually diverge. That turns "is this question worth asking" into a measurement rather than a judgement.

The authors admit downstream pass@1 gains are modest (0.61 to 1.22 points), the benchmark data is unreleased, and a failed behavioural check does not prove equivalence.

Repo license not checked — operator directive for this wave is to skip the license sweep. No clone. Do not install the plugin without asking.
