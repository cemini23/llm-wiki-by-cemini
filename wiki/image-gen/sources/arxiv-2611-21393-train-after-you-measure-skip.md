---
title: "Train After You Measure: pre-registered LoRA learning curve (arXiv:2611.21393)"
type: source
related:
  - concepts/lora-taxonomy.md
  - concepts/local-likeness-lora-lessons.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Train After You Measure: a Pre-Registered Learning Curve for Fine-Tuning Typed Decision Models on One User's Labels |
| Authors | Federico Lucca (independent researcher, Trento, Italy) |
| Type | arXiv preprint, cs.CL |
| arXiv | 2611.21393v1, 16 Nov 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.21393-train-after-you-measure-a-pre-registered-learnin.pdf` |
| URL | https://arxiv.org/abs/2611.21393 |
| Retrieved | 2026-11-22 |
| Pages | 9 |
| Read status | read |
| Domain fit | **Peripheral. SKIP for content.** Text classification of email with LoRA. The only transferable part is evaluation method. |

## Narrative

### What it does

The author fine-tunes small **typed decision models** on one user's email labels. A typed decision model returns a distribution over the options of a typed question. The five fields are message type, urgency, needs-reply, action-48h, and is-noise.

The work is **pre-registered**: the hypotheses and thresholds were committed before any fine-tuning result existed. The main study uses:

- A fixed test set of 135 emails, never used for selection.
- LoRA adapters (rank 16, α = 32, all linear layers) on Tev1-0.8B and Tev1-4B.
- Nested label budgets from 50 to 587, two seeds.
- A free Kaggle T4 GPU in fp16.

The baseline is a TF-IDF (word 1–2-grams plus char 3–5-grams) with class-balanced logistic regression.

### Results

| Field | Baseline | Tev1-4B (all labels) | Tev1-0.8B (all labels) |
|-------|----------|----------------------|-------------------------|
| Type accuracy | 0.733 | +3.3 points | +0.7 points |
| Type macro-F1 | 0.406 | 0.581 | — |
| Three action switches (mean) | 0.931 | 0.899 | 0.904 |
| Latency per question | under 1 ms | 1,681 ms | 306 ms |

Four of five registered hypotheses are refuted, two in the fine-tunes' favour. The 4B model misses the registered 3-point margin at 400 labels (+2.6) and passes it at 587 (+3.3). One email is 0.74 points, and the 95% interval is about 15 points wide. The fine-tunes lose on all three action switches at every budget. The baseline never predicts the two rarest classes (7 offers, 8 spam); the fine-tunes find spam in some seeds only.

The 0.8B type curve gains 36.3 points per 100 labels at the start, then 3.0, 7.4, 0.7, and finally −2.4. It does not saturate; it falls.

### Why it is skipped for content

Email triage with a text classifier has no link to image generation. The LoRA adapters are on a language model, not a diffusion model. The label counts and the rewards are unrelated to image or video work.

### The one transferable idea

The evaluation design is worth copying for any small-data fine-tune, including a persona LoRA. The author fixes a test set before training, registers numeric thresholds in advance, and reports refuted hypotheses in full. The result is a clean statement of what the labels do and do not buy. Two details matter:

- Rare classes vanish from the baseline and appear only inconsistently in the fine-tune. Small-data gains often sit in the rare classes, and the headline accuracy hides this.
- A wide interval on a small test set means a few points of gain are inside noise. The 135-email test makes one email worth 0.74 points.

Held at TENTATIVE: for a persona LoRA, pre-register the metric, keep a held-out prompt set, and report the per-class result, not only the mean.

## Snippets

> "Four of its five hypotheses are refuted—two in the fine-tunes' favour—and one is confirmed for one model." [Source: arxiv-2611.21393 p.1]

> "On the three action switches the baseline is ahead at every label budget for both models." [Source: arxiv-2611.21393 p.1]

## Dead Ends

Re-tagging this source as an image-gen paper would be wrong. It is a methods and evaluation paper with a weak topical link.
