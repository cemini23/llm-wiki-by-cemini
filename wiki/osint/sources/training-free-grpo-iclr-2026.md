---
title: "Training-Free GRPO: Token-Prior Approach for LLM Agent Optimization Without Parameter Updates"
type: source
tags: [source, llm-agents, grpo, training-free, token-prior, api-only-deployment, deepseek, conductor-relevant]
keywords: [training-free-grpo, token-prior, frozen-llm, agent-optimization, no-parameter-update, deepseek-v3, iclr-2026]
related:
  - concepts/llm-agent-systems.md
  - concepts/conductor-orchestrator.md
  - sources/mmgrpo-iclr-2026.md
  - sources/toolorchestra-2511.21689.md
  - sources/gigpo-neurips-2025.md
  - sources/training-free-grpo-cai-2025.md
maturity: validated
created: 2026-05-01
updated: 2026-05-01
---

## Relations

- @concepts/llm-agent-systems.md — Training-Free GRPO is the optimization method that fits Cemini's API-only deployment constraint.
- @concepts/conductor-orchestrator.md — Conductor is the synthesis concept; Training-Free GRPO is Optimization Method B (Path B: API-only token-prior deployment).
- @sources/mmgrpo-iclr-2026.md — MMGRPO requires parameter access; Training-Free GRPO achieves similar effects via token priors. Complementary approaches.
- @sources/toolorchestra-2511.21689.md — ToolOrchestra uses full RL training; Training-Free GRPO offers the API-only alternative path.
- @sources/gigpo-neurips-2025.md — GiGPO needs parameter access (full RL); Training-Free GRPO is the API-only alternative for multi-turn optimization.
- @sources/training-free-grpo-cai-2025.md — Earlier Training-Free GRPO paper (Cai et al., 2025) using experiential knowledge library E. This paper extends the approach with token priors.

## Raw Concept

- Original title: Training-Free Group Relative Policy Optimization (ICLR 2026 under review, anonymous)
- Author(s): Anonymous (ICLR 2026 double-blind under review)
- Type: ICLR 2026 under review
- Location: https://openreview.net/pdf/1e3ead46a63f8871129f105cec13c58c13d257e8.pdf
- Retrieved: 2026-05-01 (K25 Conductor sweep)
- Read status: deep-read

## Narrative

This paper argues that LLM agents can achieve GRPO-level output distribution shifts without costly parameter updates (SFT or RL). Instead, it introduces a **token prior** — a lightweight prefix that biases the frozen model's output distribution toward desired behaviors. This addresses two practical constraints: data scarcity (few dozen training samples sufficient) and overfitting (no weight modification = no catastrophic forgetting).

### Key insight

Parameter updates (SFT/GRPO) change the output distribution P(y|x) by modifying model weights. Token priors achieve the same effect by modifying the input: P(y|x, prior_token). If the prior is sufficiently well-constructed, the resulting distribution shift matches what GRPO would achieve — without touching model weights.

### Results

- Tested on **DeepSeek-V3.1** (predecessor to Cemini's V4-flash)
- With "just a few dozen training samples," Training-Free GRPO **outperforms fine-tuned small LLMs** and achieves competitive results with full GRPO
- Significantly improves out-of-domain performance (avoids overfitting that plagues fine-tuning)
- Code available (anonymous GitHub for review)

### Why this matters for Conductor

This is the optimization method that fits Cemini's deployment constraint: **API-only, no weight access.** Cemini uses DeepSeek via hosted API — it cannot fine-tune. Training-Free GRPO means Conductor can be optimized as a token-prior prefix rather than a trained router model.

Key deployment path:
1. Collect calibration data from Cemini analyst runs (correct vs. incorrect routing decisions)
2. Construct token priors that bias the routing decision toward correct model/tool selection
3. Ship token priors as prefix strings in the orchestrator prompt — no model changes needed

The fact that it was tested on DeepSeek-V3.1 (same model family as Cemini's brain) and uses only a few dozen samples makes this directly actionable.

Companion to the earlier `training-free-grpo-cai-2025.md` (experiential knowledge library E approach). This paper extends the concept with formal token-prior theory.

## Snippets

**S1 — Core argument**:
> "LLMs can achieve a similar effect on the output distribution by introducing a token prior, which is a far more lightweight approach that not only addresses practical data scarcity but also avoids the common issue of overfitting."

**S2 — DeepSeek results**:
> "Training-free GRPO, when applied to DeepSeek-V3.1, significantly improves out-of-domain performance. With just a few dozen training samples, Training-free GRPO outperforms fine-tuned small LLMs and achieves competitive results."

**S3 — Deployment implication**:
> "While methods like agentic reinforcement learning have been proposed, they typically rely on costly parameter updates such as SFT or GRPO to alter output distribution."

**S4 — Code availability**:
> "Our code is available at https://anon.github.io/[redacted]."
