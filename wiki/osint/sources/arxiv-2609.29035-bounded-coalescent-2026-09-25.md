---
title: "Phylodynamic Inference with the Bounded Coalescent"
type: source
tags: [arxiv, source, k272, ood]
keywords: [k272, bounded-coalescent, phylodyn, not-Atto]
related:
  - concepts/k272-ood-stub-wave.md
maturity: validated
created: 2026-09-25
updated: 2026-09-25
read_status: deep-read
---

## Relations

- @concepts/k272-ood-stub-wave.md

## Raw Concept

| Paper | arXiv:2609.29035 |
| File | `arxiv-2609.29035-phylodynamic-inference-with-the-bounded-coalesce.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.29035-phylodynamic-inference-with-the-bounded-coalesce.pdf` |
| Archive | egress-fi 2026-09-25 |
| Authors | Bingjing Tang, Shuangping Li, Julia A. Palacios |
| Retrieved | 2026-09-25 |
| Pages | 37 |
| Dual-ID | **OSINT K272** |
| sha256 | `aa3536c38ef1ee905f90523f3f495574fb970398d1f7313efef874bfb48283f6` |
| Code | phylodyn SPDX null; boundedcoal 404 |

## Narrative

The bounded coalescent is a statistical model of population size. It keeps the time to the most recent common ancestor under a fixed upper bound. The paper treats that estimation problem as an intensity function of an inhomogeneous point process. The stated settings are infectious-disease timing and synthetic barcoding. A transformed Gaussian process prior is placed on the effective population size trajectory. A Markov chain Monte Carlo procedure is developed for posterior inference that avoids discretization of the likelihood integrals. An efficient simulation algorithm combines time transformation and thinning to propose events via a time-varying upper bound on the coalescent intensity. The method is illustrated using SARS-CoV-2 sequence data from Washington State. This paper is **not Atto**. It is not civil records. It is not HTR. No lab steps are recorded. Phylodynamic inference is not Atto and not HTR.

| Repo | gh api 2026-09-25 | Verdict |
|------|-------------------|---------|
| JuliaPalacios/phylodyn | SPDX null, 1986 KB | **NO-CLONE** |
| bingjingle/boundedcoal | 404 | **NO-CLONE** |

**Cemini posture:** FILE. No clone. **0 product Integrate GO.** Transkribus stays the only product HTR.

## Snippets

> "The bounded coalescent conditions genealogies on the time to the most recent common ancestor being bounded above by a fixed time." [Source: https://arxiv.org/html/2609.29035 (retrieved 2026-09-25)]

> "We provide an efficient algorithm for coalescent simulation under the bounded coalescent using point process methods, retaining the exactness of naive rejection sampling while substantially reducing computational cost." [Source: https://arxiv.org/html/2609.29035 (retrieved 2026-09-25)]