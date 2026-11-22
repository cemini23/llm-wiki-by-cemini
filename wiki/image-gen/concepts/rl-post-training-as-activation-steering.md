---
title: RL post-training as activation steering
type: concept
related:
  - sources/arxiv-2611-26627-rl-post-training-activation-steering.md
  - concepts/grpo-i2v-post-training.md
  - concepts/lora-taxonomy.md
  - concepts/activation-steering-video-generation.md
  - concepts/cross-model-safety-steering.md
  - entities/models/sd3-deprecated.md
  - entities/models/flux-1-dev.md
  - entities/models/flux-2-klein.md
  - entities/models/wan-2-2.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: when reward tuning improves a diffusion transformer, what does it actually change, and how much of the gain needs input-dependent weights?

From arXiv 2611.26627 (Virginia Tech, fal, Georgia Tech, IBM).

## Narrative

### The result

RL post-training of diffusion transformers raises text rendering, composition, and preference scores. The usual view: the gain needs input-dependent transformations, so the weights must change per prompt.

The paper tests a constant alternative. Add a fixed set of steering vectors to block outputs of the **frozen** base model. The same vector applies to every prompt, every token, and every seed. Fit the vectors to match the RL-tuned model's velocity predictions. Put no reward in the loss.

Recovery of the RL-tuned model's reward gain:

| RL-tuned model | Share recovered |
|----------------|-----------------|
| Six image models (SD3.5-M, FLUX.1-dev; LoRA and full FT; OCR, PickScore, HPSv2.1, GenEval) | 90.0–96.3% |
| Wan2.1-1.3B (HPSv3) | 89.8% |
| Wan2.2-5B (rule score) | 111.9% |

On SD3.5-M the full vector set holds 0.29M parameters against 18.8M in the rank-32 RL-tuned LoRA: 65× smaller.

### RL on the vectors alone

Freeze SD3.5-M and run Flow-GRPO with only the steering vectors trainable, from zero. Now the training sees the reward but not the RL-tuned model. The vectors reach 104.6% (OCR) and 103.6% (PickScore) of the RL-tuned models' gain. A 50-user study rates them on par. So the constant form reaches the gain by itself; the shortfall in the fit comes from the fitting target, not the form.

### How a constant becomes prompt-specific

The frozen transformer does the prompt-specific work. Joint attention mixes the constant shift with text and image tokens.

On SD3.5-M:

- **The gain favours the conditional pass, early steps, and the text stream.** Conditional-pass vectors alone beat the full set. Unconditional-pass vectors alone hurt, because guidance subtracts the unconditional pass. A restricted 35,328-parameter set (0.19% of the LoRA) keeps 89.5% of the OCR gain and 73.7% of the PickScore gain.
- **The gain reaches the image through what image tokens read from text.** Swap the text keys and values that image queries read with the unsteered base's, and the vectors keep only 20.5% (OCR) and 10.5% (PickScore) of their gain. RL-tuned models lose a similar share under the same swap. Both use one route.

### When it does not apply

- **Supervised fine-tuning.** On DreamBooth identity, the vectors recover 68–83% (six fictional people) and 73–95% (four public LoRAs). A same-size LoRA does better. So subject identity is not a constant shift.
- **Same-size LoRA on RL.** An input-dependent LoRA with the same parameter count shows no detected advantage over the vectors on three of four tested models (SD3.5-M, VBVR-Pro, FLUX.1-dev). On Wan2.1 the LoRA is worse.

### Why this matters for a persona stack

Split adaptation into two kinds:

| Kind | Mechanism | Best tool |
|------|-----------|-----------|
| Reward or style tuning (preference, text rendering, aesthetic) | Mostly a constant shift | Small vector set |
| Subject or identity learning (a new person) | Needs input dependence | LoRA |

This gives a cheap test. If a reward-tuned checkpoint's gain is a constant shift, a 0.29M-parameter vector file can stand in for the full model at inference. Vectors are per model and per reward, so they are not portable.

The paper reports no vector-file release `[OPEN QUESTION 2026-11-22]`.

## Snippets

> "A constant shift thus suffices for most of the gain of policy-gradient RL post-training." [Source: arxiv-2611.26627 p.1]

> "Without new input-dependent transformations, it steers the pretrained generator toward what it can already compute." [Source: arxiv-2611.26627 p.1]
