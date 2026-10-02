---
title: K277 Atto HTR Wave (Oct 2026)
type: concept
tags: [atto, htr, genealogy, k277]
keywords: [k277, model-merging, federated, transkribus, FILE]
related:
  - concepts/k278-atto-htr-wave.md
  - concepts/k276-atto-htr-wave.md
  - sources/arxiv-2609.39684-distributed-document-analysis-2026-10-01.md
maturity: draft
created: 2026-10-01
updated: 2026-10-02
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k278-atto-htr-wave.md
- @concepts/k276-atto-htr-wave.md
- @sources/arxiv-2609.39684-distributed-document-analysis-2026-10-01.md

## Raw Concept

K277 HTR cluster hub for the **Atto** workstream (priority #1). Dual-ID **OSINT K277**. Prior @concepts/k276-atto-htr-wave.md.

## Narrative

One paper. It does not touch the product HTR path. **Transkribus stays the only product HTR.**

The paper is a position piece with measurements, and it argues the opposite of the usual privacy trade-off. Independent models trained on separate archives, then merged by averaging weights in a single round, **generalized better** than one model trained on pooled data.

The numbers that matter for us:

| Setting | Result |
|---------|--------|
| Word spotting, mean average precision | 0.363 distributed vs 0.313 centralized |
| Out-of-distribution, Latin script | +36.68% |
| Out-of-distribution, unseen alphabet | +104.02% |
| **Handwriting transfer, best case** | **x1.62** |
| Significance | Wilcoxon p = 8.8e-6 over 70 comparisons |

The authors are candid. The gain is not universal: it disappears in-domain and under full end-to-end fine-tuning. Only single-round merging was tested. They report the in-domain loss as a finding rather than hiding it.

Why this matters for Atto. The Atto model is a set of small regional archives, not one large corpus: Abruzzo, Calabria, Trentino, and the parish registers. This paper says those can be trained separately and merged, which fits both the data shape and the privacy posture. It is a method candidate for a future M-phase, not a change now.

The dataset list is a useful index in its own right: IAM, Esposalles, George Washington, Parzival, and the historical ciphers Copiale and Borg.

**Cemini posture:** FILE and HITL only. No clone. No HTR swap. No `truth.ged` merge. No Barone PII. **0 product Integrate GO.**
