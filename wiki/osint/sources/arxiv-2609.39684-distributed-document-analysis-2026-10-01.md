---
title: "Unapologetically distributed: decentralized document analysis (2609.39684)"
type: source
tags: [source, k277, atto, htr, federated]
keywords: [k277, model-merging, htr, ood, FILE]
related:
  - concepts/k277-atto-htr-wave.md
maturity: draft
created: 2026-10-01
updated: 2026-10-01
read_status: skimmed
---

## Relations

- @concepts/k277-atto-htr-wave.md

## Raw Concept

| File | `arxiv-2609.39684-unapologetically-distributed-a-call-for-decentra.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.39684-unapologetically-distributed-a-call-for-decentra.pdf` |
| Archive | egress-fi 2026-10-01 |
| Retrieved | 2026-10-01 |
| Dual-ID | **OSINT K277** |
| sha256 | `533accf8d6327678a8dc69e40670c9db2c531480feb6c0ce57e68bb98e4db41a` |
| arXiv | 2609.39684 |
| Authors | Adria Molina, Oriol Ramos Terrades, Josep Llados (CVC / UAB) |

## Narrative

A position paper with measurements. The claim is that decentralized training is not only a privacy cost. Across many document-analysis tasks, single-round model merging improves generalization over centralized pre-training, especially in low-resource and out-of-distribution settings.

The method is simple. Independent models train on separate institutions' data, then their weights are averaged. Three fine-tuning strategies are tested: cross-modal distillation for word spotting, layer-wise personalization for handwriting on unseen alphabets, and end-to-end graph-based table recognition. Both arms use the same data and step count.

Results. Word spotting mean average precision was 0.363 distributed against 0.313 centralized. Gains were 11.58% in-domain, 36.68% out-of-distribution on Latin script, and 104.02% on unseen alphabets. **Handwriting transfer improved by a best case of 1.62 times.** The result was significant: a Wilcoxon test gave p = 8.8e-6 over 70 comparisons.

The authors are candid about the limits. Distributed learning is not universal. It degrades in-domain and under full end-to-end fine-tuning. Only single-round merging is tested. They report the negative in-domain result as a deliberate finding, not a failure.

The dataset list is directly relevant to Atto: IAM, Esposalles, George Washington, Parzival, and several historical ciphers including Copiale and Borg.

Result for Atto: the useful question is whether several small archives can be merged instead of pooled. That is a method signal for a future M-phase, not a product change. **Transkribus stays the only product HTR.** No code URL found; the private M96 dataset is to be anonymised. No clone. FILE only.
