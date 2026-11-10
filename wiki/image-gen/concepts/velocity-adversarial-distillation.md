---
title: Velocity adversarial distillation (few-step students without a score estimator)
type: concept
tags: [concept, distillation, few-step, diffusion, video-generation, technique]
keywords: [VAD, VA-TDM, velocity field, A-form, B-form, critic, trajectory distribution matching, score distillation, moment matching, 4-NFE]
related:
  - sources/arxiv-va-tdm-velocity-adversarial-distillation-2611.06796.md
  - concepts/adversarial-distribution-matching-distillation.md
  - concepts/score-gradient-matching-video-distillation.md
  - concepts/one-step-autoregressive-video-distillation.md
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

The question this page answers: how do you supervise a few-step student at intermediate steps without tracking the student's score? Synthesized from arXiv:2611.06796 (VA-TDM) and the wiki's existing distillation coverage.

## Narrative

**The problem.** Distillation methods that supervise intermediate steps need the score of the student's current perturbed distribution. That score must be estimated online. Inside a few-step student the estimator is bad, because two things are correlated that a clean-target estimator assumes are independent:

- the student's clean prediction
- the residual it keeps from the transition

Perturbing the intermediate output is therefore not the same as adding fresh Gaussian noise to the clean prediction. A clean-target estimator scores a different distribution than the one the generator update uses. VA-TDM names this the TDM mismatch.

**The move.** Supervise a *velocity* field instead of a score. A velocity target can be built from a path with a coupled endpoint, so it can carry the dependency the student actually has. Two constructions:

| Form | Definition | Equivalent to |
|---|---|---|
| A-form | rectified velocity of the expected clean prediction given a perturbed sample | conditional moment matching |
| B-form | score-equivalent Gaussian velocity of the student's perturbed distribution | reverse-KL score distillation, Fisher field matching |

A learned vector-valued critic compares the chosen student field against the teacher field at the same point. The generator learns from the critic's disagreement signal. This is the adversarial part: no target distribution is regressed, only the gap to the teacher is turned into feedback.

**What the framework buys.** One derivation covers score distillation, Fisher-based matching and moment matching as special cases. It also explains the heuristic MMD update used in prior work and derives a corrected surrogate that recovers the exact gradient of MMD's intended objective.

**The practical variant.** VA-TDM keeps TDM's intermediate supervision and runs both forms together, sharing one auxiliary backbone. Field estimation is conditioned on which student transition produced the sample, because samples from different student steps can differ even at the same noise level.

**Where it sits beside the wiki's other distillation concepts.**

| Concept | What is matched | Needs an online critic |
|---|---|---|
| `@concepts/adversarial-distribution-matching-distillation.md` | discriminator logits, proven equal to DMD's gradient | yes, two heads |
| `@concepts/score-gradient-matching-video-distillation.md` | score gradients across sampled timesteps | no |
| `@concepts/one-step-autoregressive-video-distillation.md` | one transition only, adversarial | yes, discriminator |
| This page | velocity fields along the student path | yes, one vector critic |

**Reported numbers.** Four-step gains on SD3.5-Medium (GenEval 0.61 → 0.67), FLUX.2 Klein 4B (GenEval 0.78 → 0.80; OCR 0.64 → 0.69), and MiniMax-H3 33B (61.33% human preference against Fast-H3 at the same 4 NFE; 45.53% against the 100-NFE teacher).

**Operator caveats.** Training needs a teacher plus a critic in the same run, so this is not locally trainable. No released weights were checked [NEEDS VERIFICATION 2026-11-10]. The reported gains are on models that are already good at four steps, so the practical delta is small in absolute terms.

## Snippets

[Source: arxiv-2611.06796 p.1 — "VAD unifies score distillation, Fisher-based matching, and moment matching, also explaining existing heuristic MMD updates and delivering new training objectives."]
