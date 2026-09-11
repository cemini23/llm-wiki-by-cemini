---
title: "From Fixed Keys to Readable Schemas: Small Language Models for Vehicle Agent Function Calls (arXiv:2609.09476)"
type: source
tags: [arxiv, source, k259, harness]
keywords: [k259, SIP, Functional-Token, SLM, refuse]
related:
  - concepts/k259-harness-evolution-wave.md
  - concepts/k259-ood-stub-wave.md
maturity: draft
created: 2026-09-11
updated: 2026-09-11
read_status: skimmed
---

## Relations

- @concepts/k259-harness-evolution-wave.md
- @concepts/k259-ood-stub-wave.md

## Raw Concept

| File | `arxiv-2609.09476-from-fixed-keys-to-readable-schemas-small-langua.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.09476-from-fixed-keys-to-readable-schemas-small-langua.pdf` |
| Retrieved | 2026-09-11 |
| Dual-ID | **OSINT K259** |
| sha256 | `902dfa78b786ec40cba7051cd48f2c248cd08aab25be7be7873792d356fbdd53` |

## Narrative

Huawei Noah: 9,822 vehicle function-call examples, 79 Android Automotive functions. Schema-in-Prompt generalizes to held-out functions and refuses OOS; Functional Tokens hit zero on unseen and can invoke unavailable trained tokens. Scale helps SIP, not FT. OOD for Atto. CCC steal: offer schemas and allow refuse. FILE. 0 Integrate GO.

## Snippets

> On held-out functions, FT achieves zero accuracy by construction, whereas SIP generalizes. On out-of-scope requests, FT can invoke an unavailable function it was trained to emit, while SIP more reliably refuses. [Source: arxiv-2609.09476-from-fixed-keys-to-readable-schemas-small-langua.pdf]
