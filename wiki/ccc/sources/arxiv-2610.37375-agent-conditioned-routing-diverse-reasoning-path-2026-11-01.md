---
title: "Agent-Conditioned Routing: Diverse Paths in One Frozen Model"
type: source
tags: [source, arxiv, mixture-of-experts, inference-routing, reasoning-diversity]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Agent-Conditioned Routing: Diverse Reasoning Paths Within One Frozen Model |
| Authors | Ananth Kalyanasundaram et al., QpiAI |
| arXiv | 2610.37375 |
| File | `arxiv-2610.37375-agent-conditioned-routing-diverse-reasoning-path.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.37375 |
| Read status | skimmed (abstract + intro) |

## Narrative

Additional trajectories often paraphrase one dominant approach. The authors ask whether a frozen sparse mixture-of-experts (MoE) model can supply diverse methods from one problem prompt. The setup uses no user-assigned roles, prescribed methods, fine-tuning, or model copies. The measured outcome is correct method diversity. Four trajectories must yield at least two distinct primary solution methods with correct conclusions, under a fixed generation budget.

Agent-Conditioned Routing (ACR) assigns m parallel trajectories persistent, untrained shared/private expert-eligibility masks. The learned, input-dependent token router remains in place. That router still selects its top-k experts inside each eligible set. ACR runs m=4 route-conditioned trajectories on one frozen Qwen3.6-35B-A3B instance, in one batched request. In this paper, an agent is a route-conditioned trajectory. Every trajectory receives the same prompt and uses deterministic decoding. The run uses no role prompts, role generation, updates, communication, or model copies. A seeded construction assigns each trajectory its mask. The mechanism is training-free.

The benchmark is a screened set of 126 multi-mode mathematics and physics questions. Model judges read the reported derivations in full. The count is the number of problems with at least two distinct primary methods among soft-correct solutions in four trajectories. The paper reports that ACR reaches approximately twice as many such problems as the strongest temperature setting under GLM 5.3 (37.3 versus 18.7), and 1.67 times as many under GPT-5.6 Sol (45.00 versus 27.00), at matched output budgets. Both counts are single-source claims from this paper.

A blinded four-expert audit on a stratified sample of 30 problems finds more multi-method solutions with ACR on both backbones, with lower correctness. Matched-eligibility ablations show modest multi-method count advantages for ACR. Token-resampled masks attain higher correctness. An informed sequential prompt elicits more diversity still. That prompt uses previous solutions and explicit requests for alternative methods. These comparisons are single-source claims from this paper.

ACR adds about 160 KiB of mask state. In a three-problem microbenchmark capped at 1,024 tokens, latency and peak VRAM usage remain within 3% of batched temperature sampling. Both overhead figures are single-source claims from this paper. For a harness that draws several attempts from one frozen MoE, the paper claims that eligibility masks can change the derivation inside one batch. The same paper reports lower correctness in the blinded audit, and higher diversity from a sequential prompt that can read earlier solutions.

## Snippets

> "ACR reaches approximately twice as many such problems as the strongest temperature setting under GLM 5.3 (37.3 versus 18.7), and 1.67 times as many under GPT-5.6 Sol (45.00 versus 27.00), at matched output budgets. A blinded four-expert audit on a stratified sample of 30 problems also finds more multi-method solutions with ACR on both backbones, with lower correctness." [Source: `arxiv-2610.37375-agent-conditioned-routing-diverse-reasoning-path.pdf` p.1 (arXiv 2610.37375), retrieved 2026-11-01]
