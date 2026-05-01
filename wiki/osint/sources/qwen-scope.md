---
title: "Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models"
type: source
tags: [mechanistic-interpretability, SAE, sparse-autoencoders, LLM-steering, qwen, model-evaluation, safety-post-training]
keywords: [sparse autoencoders, SAE, mechanistic interpretability, Qwen3, Qwen3.5, feature steering, benchmark redundancy, toxicity classification, safety data synthesis, code-switching, SASFT, repetition reduction]
clusters: [llm-agents, audit-security]
related:
  - concepts/emergent-misalignment.md
maturity: validated
created: 2026-04-30
updated: 2026-04-30
---

## Relations
- `@concepts/emergent-misalignment.md` — SAE-based steering and safety post-training directly relevant to alignment/EM mitigation
- Concept gap: no `@concepts/sparse-autoencoders.md` or `@concepts/mechanistic-interpretability.md` page exists yet (stub needed)

## Raw Concept
- Original title: Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models
- Author(s): Qwen Team (Alibaba) — Boyi Deng, Xu Wang, Yaoning Wang, Yu Wan, Yubo Ma, Baosong Yang + 14 contributors
- Type: PDF — technical report / open-source release
- Location: cemini-librarian:/opt/cemini-bulk/research/Qwen_Scope.pdf
- Retrieved: 2026-04-30
- Pages: 35p
- Read status: deep-read

## Narrative

Qwen-Scope is an open-source suite of sparse autoencoders (SAEs) built on the Qwen model family, providing layer-wise interpretable feature representations for both dense and mixture-of-experts (MoE) architectures. The release comprises **14 groups of SAEs across 7 model variants** from the Qwen3 and Qwen3.5 series.

**Architecture**: SAEs are trained on residual-stream activations at every transformer layer. Two width configurations per model family: standard (16× hidden size, L0=50) and wide (64×, L0=100) for MoE models. Models range from Qwen3-1.7B (28 layers, 2K hidden) to Qwen3.5-27B-Instruct (64 layers, 5K hidden).

**Four application categories demonstrated**:

1. **Inference-time steering** (Section 3): Two-step pipeline — contrastive feature identification (compare SAE activations on positive vs. negative example sets) → steering via h′ ← h + αd. Demonstrated on language mixing suppression, style transfer (modern → classical Chinese), and preference control. No weight modification needed.

2. **Evaluation analysis** (Section 4): SAE feature activations as a representation-level proxy for benchmark redundancy and capability coverage. Key findings: feature overlap correlates at ρ=68.4% (Pearson) with performance-based benchmark similarity; partialling out MMLU (general ability proxy) improves to 75.5%. GSM8K has 63% feature overlap with MATH — suggesting it can be dropped from eval suites. Low-overlap benchmarks flag capability gaps.

3. **Data-centric workflows** (Sections 5-6): Two sub-applications:
   - **Toxicity classification**: Rule-based classifier using SAE features achieves competitive multilingual toxicity detection with only 180 labeled examples. Cross-lingual transfer: English-discovered toxic features generalize to other languages.
   - **Safety data synthesis**: Feature-driven pipeline identifies uncovered safety-relevant SAE features → generates synthetic prompts targeting those features → representation-level verification → SFT. Results: feature-driven synthesis achieves 91.2% coverage of safety features at matched budget vs 56.1% for random sampling.

4. **Post-training optimization** (Sections 7-8): Two demonstrated uses:
   - **SASFT (SAE-Augmented SFT)**: Adds feature-direction ablation loss during SFT to suppress code-switching. Achieves 72-100% reduction in code-switching ratio across Qwen3-1.7B and Qwen3-8B for Chinese/Russian/Korean targets, while preserving benchmark performance.
   - **SAE-guided RL against repetition**: Injects SAE-steered repetitive rollouts as rare negative examples during RL training. Consistently reduces repetition ratio faster and further than vanilla RL across Qwen3-1.7B, 8B, and 30B-A3B.

**Relevance to Cemini**: SAE-based monitoring (Section 9.2) as lightweight internal signals for deception/jailbreak/hallucination detection is directly relevant to the conditional misalignment findings. SAE-feature-guided benchmark curation could inform evaluation suite design for Cemini's RL retrain pipeline. Open-source and built on Qwen3 family — same model lineage used in conditional misalignment experiments.

## Snippets

"We introduce Qwen-Scope, an open-source suite of SAEs built on the Qwen model family, comprising 14 groups of SAEs across 7 model variants from the Qwen3 and Qwen3.5 series, covering both dense and mixture-of-expert architectures." [Source: Qwen_Scope.pdf p.1]

"We demonstrated that Qwen-Scope is useful not only for post-hoc interpretation, but also for practical model-development workflows." [Source: Qwen_Scope.pdf p.29]

"SAE features may provide lightweight internal signals for risks that are difficult to detect from outputs alone, such as deception, hidden objectives, jailbreak susceptibility, and hallucination." [Source: Qwen_Scope.pdf p.29]

"Feature-driven synthesis nearly saturates the target feature set with a small budget, while natural sampling and random security-related synthesis leave substantial gaps." [Source: Qwen_Scope.pdf p.20]

"SASFT consistently outperforms the baselines, achieving over 50% reduction in most cases" for code-switching suppression. [Source: Qwen_Scope.pdf p.24]
