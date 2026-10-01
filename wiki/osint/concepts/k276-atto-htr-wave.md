---
title: K276 Atto HTR Wave (Sep 2026)
type: concept
tags: [atto, htr, genealogy, k276]
keywords: [k276, transkribus, character-error, few-shot, FILE]
related:
  - concepts/k277-atto-htr-wave.md
  - concepts/k275-ood-stub-wave.md
  - sources/arxiv-2609.35473-htr-high-variance-2026-09-30.md
  - sources/arxiv-2609.37195-htr-icl-2026-09-30.md
  - sources/arxiv-2609.37755-papyrus-htr-tolerance-2026-09-30.md
maturity: draft
created: 2026-09-30
updated: 2026-10-01
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k277-atto-htr-wave.md
- @concepts/k275-ood-stub-wave.md
- @sources/arxiv-2609.35473-htr-high-variance-2026-09-30.md
- @sources/arxiv-2609.37195-htr-icl-2026-09-30.md
- @sources/arxiv-2609.37755-papyrus-htr-tolerance-2026-09-30.md

## Raw Concept

K276 HTR cluster hub for the **Atto** workstream (priority #1). Dual-ID **OSINT K276**.

## Narrative

Three handwritten-text-recognition papers. None of them changes the product HTR path. **Transkribus stays the only product HTR.**

| Source | Contribution | Posture |
|--------|--------------|---------|
| 2609.35473 high-variance subspace | Pixel-reconstruction pretraining beats other SSL on Latin historical sets | Method signal. No weights, no code |
| 2609.37195 in-context learning | Public VLMs transcribe from 2 to 16 examples, no fine-tuning | Possible in-house option. No clear win |
| 2609.37755 papyrus tolerance | Per-task character-error budgets for downstream use | Filing note. Greek only |

The two findings worth keeping:

1. **Set the error budget per task before buying a model.** The papyrus paper shows one character-error number is not enough. Its 90%-retention thresholds run from 3% for dating to 20% for genre classification. Retraining the downstream model on noisy text removes the collapse above 15% error. Lost lines are expensive: 30% of lines lost costs about as much as 5% character error.
2. **Few-shot is now real.** The in-context paper reaches 5.36% error on IAM at 16 demonstrations with no training. Historical sets stay harder, at about 18% to 21%.

What this does NOT support: a swap away from Transkribus. No paper here tests Transkribus. The best released artifact is a task-tolerance pipeline, not a recogniser.

**Cemini posture:** FILE and HITL only. No clone. No HTR swap. **0 product Integrate GO.**
