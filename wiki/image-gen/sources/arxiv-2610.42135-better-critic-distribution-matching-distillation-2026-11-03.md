---
title: "A better critic matters for distribution matching distillation"
type: source
tags: [source, arxiv, diffusion, distillation, few-step, critic]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Better Critic Matters for Distribution Matching Distillation |
| Authors | Zongze Wu, Xianbang Wang, Zhengyang Geng, Mingdeng Cao, Zhoutong Zhang, Richard Zhang, Eli Shechtman, Ruiming Cao (Adobe, MIT) |
| arXiv | 2610.42135 |
| Pages | 35 |
| Read status | skimmed (abstract) |

## Narrative

Distribution Matching Distillation trains a few-step student using the gap between a teacher's score and an online critic's estimate of the student's score. The paper asks what the **critic** actually needs — in capacity and in information.

### Capacity — the collapse finding

Controlled experiments across **seven SiT model sizes on ImageNet**: increasing the teacher while holding a small critic fixed **degrades student quality and can collapse training**.

Scaling the critic alongside the teacher — they call it **joint scaling** — prevents the collapse and lets the student benefit from a larger teacher.

That is a concrete, counter-intuitive result: **a bigger teacher can make a distilled student worse**, because the critic is the bottleneck and nobody scaled it.

### Information — the step-aware critic

Instead of forcing the critic to model a step-agnostic mixture of student outputs, they introduce **STAC**, a step-aware critic conditioned on the student's generation step, estimating step-specific scores.

### Where it lands

Together, joint scaling and STAC improve few-step distillation across class-conditional ImageNet, text-to-image with **SDXL and FLUX.2**, and text-to-video with **Wan2.1**.

**Why it matters for a local generation stack.** Few-step distillation is the main lever that makes local generation affordable. The finding that the critic, not the teacher, gates the result points at a specific thing to check when a distillation underperforms.

**Caveat.** Abstract only. No FID or speedup figures reproduced.

## Snippets

> "Increasing teacher size while keeping a small critic fixed can degrade student quality and cause training collapse. Scaling the critic alongside the teacher, a strategy we call joint scaling, prevents collapse in our experiments and allows the student to benefit from larger teachers." [Source: arxiv-2610.42135 p.1]

## Dead Ends

- **Assuming a bigger teacher always distils better.** It can collapse with a fixed critic.
