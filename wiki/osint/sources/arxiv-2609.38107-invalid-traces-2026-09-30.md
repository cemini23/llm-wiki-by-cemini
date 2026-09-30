---
title: "Correct answers, invalid traces (2609.38107)"
type: source
tags: [source, k276, agents, verification, chain-of-thought]
keywords: [k276, cot, trace-validity, auditing, FILE]
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

| File | `arxiv-2609.38107-correct-answers-invalid-traces-what-verifiable-g.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.38107-correct-answers-invalid-traces-what-verifiable-g.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `0d9c1341f5d067089c2e667ae19f2c5a599ce56984274c920b6d4b8c2225389d` |
| arXiv | 2609.38107 |
| Authors | Ratish Puduppully, Pranabendu Misra, Paarth Iyer, Durgesh Kalwar, Vardhan Palod, Subbarao Kambhampati |
| Repo | `https://github.com/ratishsp/igsm-trace-validity` |
| Weights | `https://huggingface.co/ratishsp/igsm-trace-validity` |

## Narrative

The paper tests a common assumption: that a chain-of-thought trace records how the model reached its answer. It uses iGSM, a synthetic grade-school math benchmark that exposes the exact quantities and dependencies a correct solution must use. That makes each trace checkable step by step.

The headline result: on the hardest instances, 31.6% of correct answers have invalid traces. Over half of those invalid traces pass every syntactic and arithmetic check. They fail the semantic dependency check.

Two more results matter for auditing. Non-minimal training traces produce non-minimal outputs. Shuffling tokens in 10% of the training trace sentences keeps near-clean accuracy, even out of distribution, while no trace passes verification. So accuracy survives a broken trace.

The authors state the implication directly: a trace is weak evidence for AI-safety monitoring and interpretation.

The authors admit the models are small (124M parameters) and the data is synthetic. They state that direct extrapolation to frontier systems is not warranted, and they do not measure causal faithfulness.

This is the most useful paper in the wave for our own verification gates. It gives a measured reason not to treat a visible trace as proof of the process.

Repo SPDX is MIT, 95 KB, 1 star (gh api 2026-09-30). Weights are on Hugging Face. No clone. FILE only.
