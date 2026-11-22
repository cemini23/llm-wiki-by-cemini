---
title: "Machine unlearning from privileged context — teach the refusal, do not just suppress the memory"
type: concept
maturity: draft
related:
  - sources/arxiv-leaf-opd-unlearning-privileged-context-2611.20674.md
  - concepts/recognition-refusal-gap.md
  - concepts/refusal-and-abstention-direction-geometry.md
updated: 2026-11-22
---

## Raw Concept

What this page answers: how do you remove a piece of knowledge from a model so that a reworded probe does not recover it? LEAF-OPD (2611.20674) supplies one method and one failure mode.

## Narrative

Gradient ascent is the common unlearning baseline. It lowers the probability of the forget data. It does not teach the model what to say when the question arrives, and it degrades utility.

LEAF-OPD uses a frozen teacher and a student. On forget data the teacher sees a privileged context: an instruction not to reveal the target. On retain data the teacher sees no privileged context. The student never sees it. The student is trained by token-level on-policy distillation on its own trajectories.

The failure mode is supervision collapse. The teacher corrects only the first few tokens, then its signal fades and the student drifts. The paper measures this with the Supervision Signal over the full trajectory (SS1) and the second half (SS0.5). When the signal is weak, light SFT on the teacher's refusal raises both. The authors call this turning a bad teacher into a good teacher.

Results: best Forget Quality, Model Utility, and Forget ROUGE-L on TOFU. On RWKU, 34% better Forget Quality than the second-best method, with competitive Retain Quality.

**Lab rule.** Verify unlearning with reworded and indirect probes. A model that only learned to suppress the direct question will fail them. Check utility on retain data at the same time, because suppression methods pay for forgetting with capability loss.

This pairs with the recognition-refusal gap. A model can recognize the forbidden knowledge and still emit it. Unlearning that teaches behaviour handles both. Unlearning that only pushes the distribution handles neither.

[Source: arxiv-2611.20674-leaf-opd-learning-to-forget-from-privileged-cont.pdf]

## Snippets

> "The teacher usually provides effective supervision only at the first few tokens along the student's trajectories."
[Source: arXiv:2611.20674v1 abstract]
