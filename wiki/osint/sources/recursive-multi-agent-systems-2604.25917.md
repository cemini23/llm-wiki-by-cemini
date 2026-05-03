---
title: "RecursiveMAS — Scaling Multi-Agent Systems Through Latent-Space Recursion"
type: source
tags: [llm-agents, ml-methods, multi-agent-systems, latent-reasoning, system-optimization]
keywords: [RecursiveMAS, RecursiveLink, latent-thoughts, inner-outer-loop, multi-agent-collaboration, system-recursion, RLMs, agent-training]
related:
  - concepts/recursive-multi-agent-systems.md
  - concepts/latent-thought.md
  - concepts/conductor-orchestrator.md
  - concepts/policy-distillation.md
maturity: validated
read_status: deep-read
created: 2026-05-02
updated: 2026-05-02
---

## Raw Concept
- Original title: Recursive Multi-Agent Systems
- Author(s): Xiyuan Yang, Jiaru Zou (equal contribution, project lead), Rui Pan, Ruizhong Qiu, Pan Lu, Shizhe Diao, Jindong Jiang, Hanghang Tong, Tong Zhang, Markus J. Buehler, Jingrui He, James Zou (UIUC, Stanford, NVIDIA, MIT)
- Type: PDF (arXiv)
- Location: cemini-librarian:/opt/cemini-bulk/research/Recursive Multi-Agent Systems.pdf
- arXiv: 2604.25917
- Retrieved: 2026-05-02
- Pages: 36
- Read status: deep-read

## Narrative

Extends the recursive computation paradigm from single models (RLMs like LoopLM) to entire multi-agent systems. The central question: if a single Transformer can scale reasoning by looping over shared layers in latent space, can a *system* of heterogeneous agents scale collaboration the same way?

RecursiveMAS answers yes. It connects agents through a lightweight **RecursiveLink** — a 2-layer residual MLP that transmits latent states between agents — and optimizes the entire system as one recursive loop via **inner-outer loop training**. Only the RecursiveLinks are trained (0.31% of parameters); all LLM weights are frozen.

**Inner loop**: Each agent's inner RecursiveLink learns to generate latent thoughts aligned with ground-truth semantics, using cosine similarity loss against the ground-truth answer embedding. This replaces explicit text decoding with continuous-space generation.

**Outer loop**: The full system is unrolled for n recursion rounds. After the final textual prediction, cross-entropy loss backpropagates through all outer RecursiveLinks, giving each link a shared credit signal based on its global contribution.

Four collaboration patterns validated: Sequential (Planner→Critic→Solver), Mixture (parallel specialists + Summarizer), Distillation (Expert→Learner), and Deliberation (Reflector↔Tool-Caller). Works across Qwen, Llama, Gemma, and Mistral model families.

Results across 9 benchmarks (MATH500, AIME2025/2026, GPQA-Diamond, MedQA, LiveCodeBench, MBPP+, HotpotQA, Bamboogle): +8.3% avg accuracy, 1.2×–2.4× inference speedup, 34.6%–75.6% token reduction. Performance advantage widens with recursion depth: +20.2% over text-based MAS at r=3. Outperforms single-agent SFT, Mixture-of-Agents, TextGrad, LoopLM, and Recursive-TextMAS. Training cost is 56% cheaper than LoRA ($4.27 vs $6.64) with 3.7× fewer parameters.

For this workspace: RecursiveMAS is the training-based counterpart to Conductor's text-based routing. The RecursiveLink pattern — lightweight trainable connector modules, not full model updates — mirrors Conductor's token-prior approach (lightweight prefix, not weight modification). The inner-outer loop training provides a blueprint for Conductor Path C: gradient-based credit assignment across pipeline stages. [Sources: Recursive Multi-Agent Systems.pdf pp.1-13]

## Snippets

- "Recursive or looped language models have recently emerged as a new scaling axis by iteratively refining the same model computation over latent states to deepen reasoning. We extend such scaling principle from a single model to multi-agent systems, and ask: Can agent collaboration itself be scaled through recursion?" [p.1]
- "Instead of improving each agent's capabilities as a standalone component, we adopt a higher-level learning perspective and aim to co-evolve and scale the entire system as an integrated whole. We recast agent collaboration through the lens of recursive language models (RLMs), where a shared set of layers is iteratively applied and optimized within a continuous latent space." [p.2]
- "Without updating all model parameters, agents are connected and iteratively optimized solely via the lightweight RecursiveLink, a two-layer residual projection module for latent states transmission and refinement." [p.2]
- Inner RecursiveLink: `Rin(h) = h + W2 σ(W1 h)` — residual connection preserves original latent semantics, GELU activation, linear layers handle distributional shift. [p.5]
- Outer RecursiveLink: `Rout(h) = W3 h + W2 σ(W1 h)` — additional linear layer W3 maps between heterogeneous embedding dimensions. [p.5]
- "The residual branch largely preserves the original semantics of the input, allowing the RecursiveLink network to focus on aligning distributional differences rather than learning the full projection from scratch." [p.5]
- Proposition 3.1: "Text-based Recursive MAS requires Θ(N(m|V|dh + (t+m)d²h + (t+m)²dh)); RecursiveMAS achieves Θ(N(md²h + (t+m)d²h + (t+m)²dh)). Since dh ≪ |V| in practice, RecursiveMAS replaces the expensive per-step vocabulary-space decoding cost m|V|dh with a much more efficient latent-space transformation md²h." [p.6]
- Inner-loop objective: `Lin = 1 − cos(Rin(H), Emb_θi(y))` — cosine similarity between inner-link-transformed latent thoughts and ground-truth embedding. [p.7]
- Outer-loop objective: `Lout = CE(S^(n)(S^(n−1)(…S^(1)(x))), y)` — cross-entropy loss backpropagated through full recursive unrolling, with "gradient backpropagation assigns each outer link a shared credit signal according to its global contribution to the final prediction." [p.7]
- Training cost: RecursiveMAS uses 15.29 GB GPU memory, 13.12M trainable params (0.31%), $4.27 estimated cost, 74.9% avg accuracy — vs LoRA at 21.67 GB / 15.92M / $6.64 / 66.9% and Full-SFT at 41.40 GB / 4.21B / $9.67 / 68.6%. [p.13, Table 5]
- Main results (r=3): RecursiveMAS 88.0% on MATH500 vs 85.8% Recursive-TextMAS; 86.7% on AIME2025 vs 73.3% (+13.4pp); 86.7% on AIME2026 vs 73.3% (+13.4pp); 66.2% on GPQA-Diamond vs 61.6% (+4.6pp); 42.9% on LiveCodeBench vs 38.7%; 79.3% on MedQA vs 77.0%. [p.10, Table 3]
- "When compared with the text-based recursion, RecursiveMAS consistently improves over the baseline by an average of 8.1% at r=1, 19.6% at r=2, and 20.2% at r=3, with performance advantage more pronounced as the recursion deepens." [p.10]
- Efficiency: "RecursiveMAS delivers steadily increasing efficiency gains across recursion rounds, accelerating end-to-end inference time from 1.2× to 2.4× while reducing output tokens from 34.6% to 75.6%." [p.10]
- Scaling law: "Increasing inference depth continues to improve systems trained with fewer rounds, while deeper training shifts the entire performance frontier upward… training recursion progressively teaches the system to form refinement-ready latent states, and subsequent inference recursion translates this learned recursive structure into additional test-time gains." [p.10]
- RecursiveLink design ablation: Res+2-Layer (theirs) = 88.0/66.2/42.9 on MATH500/GPQA-D/LiveCodeBench vs 1-Layer 84.4/63.2/40.1. Residual connection delivers improvement even on single-layer designs (86.7 vs 84.4). [p.12, Table 4]
- Latent thoughts length: "Increasing m improves performance in the early regime. Once m reaches a moderate scale (around m=80), performance is stabilized across all benchmarks… RecursiveMAS enables effective agent reasoning and interaction with only a modest latent-thought budget, in sharp contrast to text-based collaboration that typically requires longer CoT and costly token generation." [p.13]
- Semantic refinement: "The generated answers at r=1 remain visibly shifted from the ground-truth distribution, but this discrepancy progressively narrows as depth increases, with the two distributions becoming largely aligned by r=3." [p.12]
- "While existing methods in agentic AI primarily focus on recursion inside a single language model, RecursiveMAS exhibits the first attempt to extend the recursive scaling paradigm to system-level." [p.14]
