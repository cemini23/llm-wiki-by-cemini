---
title: "TestPrism (arXiv 2610.12289)"
type: source
tags: [source, k287, arxiv, tests, agents]
keywords: [testprism, joint-success-function, testhelix, k287]
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

| Title | TestPrism: Rethinking Test Evaluation Beyond a Single Reference |
| Authors | Han Li, Lingxiang Hu, Jiacheng Huang, Ziqian Jiang, Jingkai Luo, Wei Gao, Yunfan Tan, Zun Wang, Jiaheng Liu |
| Type | arXiv preprint |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.12289-testprism-rethinking-test-evaluation-beyond-a-si.pdf` |
| Retrieved | 2026-10-09 |
| arXiv | 2610.12289v1 |
| Licence | CC BY 4.0 |
| read-status | read |

## Narrative

TestPrism has 300 test tasks from 17 sources and 3,000 candidate implementations, half valid and half invalid. Joint Success Function requires the tests to fail on the start state, accept every valid candidate, and reject every invalid candidate.

Across fourteen agent setups, Joint Success Function is 28.00 percent. Single-reference success is 59.67 percent. TestHelix adds 8.67 to 9.00 percentage points on two models in the paper's own comparison.

A single gold patch is a weak test of a test. That is a measurement note. It does not change a desk rule.

## Snippets

> "Joint Success Function reaches only 28.00%, whereas single reference success reaches 59.67%." [Source: arxiv-2610.12289 PDF, abstract]
