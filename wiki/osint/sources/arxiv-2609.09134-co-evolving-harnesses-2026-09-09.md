---
title: "Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails (arXiv:2609.09134)"
type: source
tags: [arxiv, source, k258, harness]
keywords: [k258, harness-evolution, on-policy, LoRA]
related:
  - concepts/k258-harness-evolution-wave.md
maturity: draft
created: 2026-09-09
updated: 2026-09-09
read_status: skimmed
---

## Relations

- @concepts/k258-harness-evolution-wave.md

## Raw Concept

| File | `arxiv-2609.09134-co-evolving-harnesses-and-models-on-policy-corre.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.09134-co-evolving-harnesses-and-models-on-policy-corre.pdf` |
| Retrieved | 2026-09-09 |
| Dual-ID | **OSINT K258** |
| sha256 | `ae8b8973f7964fca32b192fe3166ac66edb1afb78ad2b5212ec33b892a25cc34` |

## Narrative

Salesforce: after harness evolution, imitating an expert under that harness regresses the weaker model (minus 4 to minus 30 points). The weaker model copies expert planning without competence and loses fit to the harness evolved around its native style. Fix: on-policy expert correction of the failing turn only. Do not SFT-imitate experts into /route or skills. FILE. 0 Integrate GO.

## Snippets

> Imitating the expert causes the weaker model to regress on all seven tasks. The weaker model adopts the expert's planning strategy without the competence to execute it. [Source: arxiv-2609.09134-co-evolving-harnesses-and-models-on-policy-corre.pdf]
