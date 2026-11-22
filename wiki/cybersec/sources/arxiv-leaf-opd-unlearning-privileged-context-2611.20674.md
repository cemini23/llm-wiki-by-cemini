---
title: "LEAF-OPD — learning to forget from privileged contexts via on-policy distillation (2611.20674)"
type: source
maturity: draft
related:
  - concepts/machine-unlearning-privileged-context.md
  - concepts/recognition-refusal-gap.md
updated: 2026-11-22
---

## Raw Concept

- **Title:** LEAF-OPD: Learning to Forget from Privileged Contexts via On-Policy Distillation
- **Authors:** Zirui Pang, Zhijie Deng, Yuancheng Wang, Qihan Yu, Xin Li, Jiaheng Wei, Zixin Zhong (HKUST Guangzhou; CUHK Shenzhen)
- **Type:** arXiv preprint (cs.CL)
- **Location:** `research to be indexed/cybersec/arxiv-2611.20674-leaf-opd-learning-to-forget-from-privileged-cont.pdf`
- **Retrieved:** 2026-11-17
- **arXiv:** 2611.20674v1, 16 November 2026
- **Read status:** read — 8 of 23 pages extracted 2026-11-22

## Narrative

LLM unlearning tries to remove target knowledge and keep utility. Gradient ascent, the common baseline, only pushes the model away from the forget data. It does not teach the model what to do when the question arrives.

LEAF-OPD uses a frozen teacher policy and a student policy. On forget data, the teacher sees a privileged context: extra instructions not to reveal the forget target. The teacher gives token-level supervision on trajectories that the student generated. On retain data, the same teacher supervises without the privileged context, so the student keeps the teacher's normal responses. The student never sees the privileged context.

The key problem is supervision collapse. The teacher often corrects only the first few tokens. After the refusal prefix, its supervision signal vanishes, and the student drifts into confusion. The paper measures this with the Supervision Signal (SS) over a token interval. SS1 covers the full trajectory. SS0.5 covers the second half, so it tests whether late-stage correction persists.

When the signal is weak, LEAF-OPD applies light SFT to strengthen the teacher's context-conditioned refusal. This raises both SS1 and SS0.5. The authors call this turning a bad teacher into a good teacher.

Results on TOFU, RWKU, and MUSE-News: LEAF-OPD has the best Forget Quality, Model Utility, and Forget ROUGE-L on TOFU. On RWKU it beats the second-best method by 34% in Forget Quality, with competitive Retain Quality.

The defensive lesson: unlearning that only suppresses knowledge can leave a model that still answers from a reworded probe. Teaching the refusal behaviour on-policy is the difference between suppressed and removed.

[Source: arxiv-2611.20674-leaf-opd-learning-to-forget-from-privileged-cont.pdf]

## Snippets

> "Instead of simply pushing the model away from the forget data distribution, LEAF-OPD explicitly teaches the student how to behave when encountering knowledge that should be forgotten."
[Source: arXiv:2611.20674v1 abstract]

## Dead Ends

- **Partial-read note (2026-11-22):** 8 of 23 pages read. Full ablation tables are in the unread pages. [Source: arxiv-2611.20674-leaf-opd-learning-to-forget-from-privileged-cont.pdf]
