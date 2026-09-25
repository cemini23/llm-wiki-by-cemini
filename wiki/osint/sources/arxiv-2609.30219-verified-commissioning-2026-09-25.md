---
title: "Requirement-Bound Verified Commissioning"
type: source
tags: [arxiv, source, k272, harness]
keywords: [k272, verified-commissioning, external-gate, release-authority]
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

| Paper | arXiv:2609.30219 |
| File | `arxiv-2609.30219-requirement-bound-verified-commissioning-a-froze.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.30219-requirement-bound-verified-commissioning-a-froze.pdf` |
| Archive | egress-fi 2026-09-25 |
| Authors | Mehmet İşcan (PythaLab, Yıldız Technical University) |
| Retrieved | 2026-09-25 |
| Pages | 42 |
| Dual-ID | **OSINT K272** |
| sha256 | `1072fbd9bab2307731424a9db827832865e622e6a125fe2ed06e0ba33c8cd27d` |
| Code | No GitHub repo in the PDF |

## Narrative

The protocol splits candidate generation from release authority. A frozen local model with four billion parameters may draft a plan. An external gate releases the plan only when it can derive the facts under a sealed grammar. On the reported run, fabricated ready plans on 21 of 22 routed unanswerable tasks were rejected. The same 83 releases were reproduced with no model call. A false-release upper bound under a sealed criterion: a one-sided Clopper–Pearson upper bound of 0.0354 was obtained as a diagnostic under an i.i.d. assumption, below the sealed 5% threshold. However, one false release was subsequently recorded among 146 releases outside the benchmark at seed 0. Protection against incorrect user answers was characterized: both facts were bound from the original text on 13 of 96 answerable tasks. Incorrect answers were released in 169 of 431 pairings on the remaining tasks, including failures involving coordinate exclusion. A deployable questioning policy was not tested because eligibility was determined from the answer key. Gate sensitivity and real user behavior were not measured. No repo is in the PDF. **Do not rewrite Verify.**

**Cemini posture:** FILE. The external gate holds release authority. **0 product Integrate GO.** Never auto-evolve skills.

## Snippets

> "A plan is released by a deterministic entailment gate only when both facts can be derived from the text under the sealed first version of the requirement grammar, referred to as grammar V1." [Source: https://arxiv.org/html/2609.30219 (retrieved 2026-09-25)]

> "The same 83 releases were reproduced without model calls." [Source: https://arxiv.org/html/2609.30219 (retrieved 2026-09-25)]