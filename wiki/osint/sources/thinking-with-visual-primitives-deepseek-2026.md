---
title: "Thinking with Visual Primitives — DeepSeek-V4-Flash MLLM (Lu et al., 2026)"
type: source
tags: [paper, multimodal, deepseek, mllm, visual-grounding, system-2-reasoning, refutation-premium, deep-read]
keywords: [thinking-with-visual-primitives, twvp, deepseek-v4-flash, deepseek-vit, csa, compressed-sparse-attention, reference-gap, visual-primitives, bounding-boxes, points, maze-navigation, path-tracing, opd, on-policy-distillation, grpo, hai-llm, fp8, fp4, mxfp4, kv-cache-compression]
related:
  - sources/incompressible-knowledge-probes-li-2026.md
  - sources/agentic-harness-engineering.md
  - sources/training-free-grpo-cai-2025.md
  - sources/moe-efficiency-leverage-tian-2026.md
  - sources/moe-surpass-dense-equal-resource-li-2026.md
  - sources/platonic-representation-hypothesis-huh-2024.md
  - entities/infrastructure/deepseek-api.md
  - concepts/llm-agent-systems.md
  - concepts/high-signal-paper-patterns.md
maturity: validated
created: 2026-04-30
updated: 2026-08-20
read_status: read
---

## Relations

- @sources/incompressible-knowledge-probes-li-2026.md — IKP includes `deepseek-v4-flash` in its calibration panel; this paper is built **on** `deepseek-v4-flash` (284B total / 13B active MoE). Both anchor the same model in different research lenses (capacity probing vs capability extension).
- @sources/agentic-harness-engineering.md — AHE measures `+10.1pp` cross-family gain on `deepseek-v4-flash` (Terminal-Bench 2). This paper extends `deepseek-v4-flash` along an orthogonal axis (multimodal grounding, not harness optimization). Three independent 2026 papers now empirically grounded in `deepseek-v4-flash`.
- @sources/training-free-grpo-cai-2025.md — TF-GRPO froze policy weights and learned token-level experiential knowledge; this paper uses **GRPO + RFT + On-Policy Distillation** as the post-training stack on top of pretraining. Same RL family, different objective (token-experience-bank vs visual-primitive-grounding).
- @sources/moe-efficiency-leverage-tian-2026.md — Tian/MoE-leverage paper formalizes `total params >> active params` value; this paper's base (`284B-A13B`) confirms the formalization holds in production frontier multimodal models too.
- @sources/moe-surpass-dense-equal-resource-li-2026.md — StepFun/MoE-surpass paper at the **training-compute parity** frontier; complements `total≫active` MoE story underlying `deepseek-v4-flash`.
- @entities/infrastructure/deepseek-api.md — `deepseek-v4-flash` is Cemini's intended brain. If/when this paper's vision capability surfaces in the hosted DeepSeek API endpoint, Cemini gets multimodal reasoning **for free** (single API key, single rate-limit envelope). Even if not surfaced, validates the bus-factor robustness of the DeepSeek dependency.
- @concepts/llm-agent-systems.md — adds **Multimodal/Vision agents** sub-topic depth. Token-efficient multimodal substrate (90 KV entries vs 800-1100 frontier) directly relevant to agent-orchestration token budgets.
- @concepts/high-signal-paper-patterns.md — exemplifies refutation premium (the "Reference Gap" reframing of CoT bottleneck) + DeepSeek-bus-factor + frontier-benchmark superiority. Use as an annotated example in the rubric.

## Raw Concept

- **Original title**: Thinking with Visual Primitives
- **Authors**: Ruijie Lu (Peking U.), Yiyang Ma, Xiaokang Chen (project lead), Lingxiao Luo (Tsinghua), Zhiyu Wu, Zizheng Pan, Xingchao Liu, Yutong Lin, Hao Li, Wen Liu, Zhewen Hao, Xi Gao, Shaoheng Nie, Yixuan Wei, Zhenda Xie, Ting Chen (Tsinghua), Gang Zeng (PKU) — **DeepSeek-AI** + Peking University + Tsinghua
- **Type**: Research paper PDF, 25 pages
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Thinking_with_Visual_Primitives.pdf`
- **Retrieved**: 2026-04-30 (laptop drop)
- **Pages / length**: 25p
- **Read status**: read (full deep-read 2026-04-30)
- **Affiliations**: DeepSeek-AI (corporate research), Peking University, Tsinghua University
- **Foundation model**: `DeepSeek-V4-Flash` — 284B total / 13B active params, MoE, Compressed Sparse Attention (CSA)
- **Code/data**: not enumerated in the inbox copy; HAI-LLM training framework cited (High-flyer's lightweight distributed training tool)

## Narrative

**Thesis.** The dominant Multimodal LLM (MLLM) failure mode in complex reasoning is not the *Perception Gap* (recently mitigated by high-resolution cropping / "Thinking with Images" approaches) but the **Reference Gap**: natural language is too ambiguous to function as a precise pointer in continuous visual space. In dense counting or multi-step spatial deduction, the model's linguistic "thoughts" lose track of the visual entities they intend to reference, leading to cascading hallucinations.

The paper proposes a **paradigm shift**: visual primitives (bounding boxes, points) are elevated from post-hoc grounding artifacts to **"minimal units of thought"** — interleaved directly into the model's chain-of-reasoning. This mimics human deictic pointing (finger gestures while counting/navigating). The model can "point while it reasons", anchoring abstract linguistic thoughts onto concrete spatial coordinates.

**Why this is a refutation-premium pattern.** Prior work (cited refs 6, 12, 26, 27, 32) treats grounding as **post-hoc verification** — a perception-side check. This paper treats grounding as **the medium of reasoning** — a System-2 cognitive primitive. That's the kind of conceptual reframe @concepts/high-signal-paper-patterns.md flags as high-signal: same components, fundamentally different role. Empirically, the reframe shows up most starkly in topological reasoning (Maze Navigation +16.3pp over GPT-5.4; Path Tracing +10.2pp).

### Architecture (`DeepSeek-V4-Flash` substrate)

The model is built on `DeepSeek-V4-Flash` (284B total / 13B active MoE), with a custom in-house ViT (`DeepSeek-ViT`) for vision encoding. Architecture is structurally similar to LLaVA but compresses heavily:

1. Input image (e.g. `756×756` = 571,536 px) → ViT with 14×14 patches → 2,916 patch tokens
2. **3×3 spatial token compression** (channel-dimension stack of 9 adjacent patches) → 324 tokens fed to LLM during prefill
3. **Compressed Sparse Attention (CSA)** in the LLM compresses KV cache by 4× → **81 visual KV entries** in cache
4. **Overall pixel-to-KV-cache compression ratio: 7,056×**

This compression is the operational headline:

| Model | Tokens before compression | KV cache entries (800×800 image) |
|---|---|---|
| Gemma-4-31B | ~289 | ~289 |
| **Ours-284B-A13B** | **~361** | **~90** |
| Qwen3-VL-235B-A22B | ~660 | ~660 |
| GPT-5.4 | ~740 | ~740 |
| Claude-Sonnet-4.6 | ~870 | ~870 |
| Gemini-3-Flash | ~1100 | ~1100 |

The 90-entry KV cache is **~12× smaller** than Gemini-3-Flash's at frontier-comparable performance. Token efficiency at frontier capability is the deployment-side argument.

### Training pipeline (5 stages)

1. **Pretraining** — equips the model with foundational visual-primitive output capability (bounding boxes + points).
2. **Specialized SFT** — two cold-start specialists: `F_TwG` (thinking with grounding / boxes), `F_TwP` (thinking with pointing).
3. **Specialized RL (GRPO)** — produces `E_TwG` and `E_TwP` expert models. Reward Models (RM) are domain-specific:
   - **Counting**: rule-based RM with relative-error reward `1 - |ŷ-y|/(|y|+1)`, coefficients α=0.7, β=3.
   - **Spatial Reasoning / VQA**: LLM-based Generative RM (GRM) — feed thinking + final response + query + GT to GRM; reward = average of thinking-process score + response score.
   - **Maze Navigation**: rule-based RM with three components: causal exploration progress (1 - distance/path-length, truncated at first wall violation), exploration completeness (for unsolvable mazes), wall violation penalty.
   - **Path Tracing**: bidirectional poly-line distance + endpoint accuracy + trajectory continuity penalty + answer-correctness score.
   - **Difficulty filtering for RL data**: rollout `N` times pre-RL via SFT model; partition data into Easy (all correct), **Normal (1≤k<N correct — used for RL)**, Hard (all wrong). Only Normal-Level enters RL training, ensuring useful gradient signal.
4. **Unified RFT** — integrates `E_TwG` + `E_TwP` reasoning paradigms into a single unified model `F`.
5. **On-Policy Distillation (OPD)** — closes the gap between unified `F` and the experts via reverse-KL distillation: `L_OPD(θ) = Σ w_i · D_KL(π_θ ∥ π_{E_i})`, full-vocabulary logit distillation, two teachers (`E_TwG`, `E_TwP`).

**Training infra**: HAI-LLM framework (High-flyer's distributed training tool, same lab that ships DeepSeek). Pretraining at 64K seq-length FP8; post-training extends to **256K seq-length**. Specialized SFT/RL stages run in FP8; Unified RFT and OPD switch to **FP4 (MXFP4) quantization**.

### Data curation

- **97,984 box-grounding-related sources** scraped via Huggingface API filtering on "Object Detection" / "Grounding" tags, plus other websites (deduplicated).
- **Two-step filter pipeline**:
  1. **Semantic review (MLLM-driven)**: discard meaningless machine codes (numeric class IDs), ungeneralizable private entities (`MyRoommate`, `ID_Card_1`), ambiguous abbreviations (`OK`, `NG`).
  2. **Geometric filter** (further pages, not extracted in this read pass).
- **Bias toward boxes over points** (rationale): bounding boxes are deterministic (2-coordinate), task-generalizable (a box defines two points), and information-rich (encodes width/height as well as location). Points alone suffer ambiguity (any coordinate within an object boundary is "correct"), and ground-truth absence creates noisy reward signals.

### Benchmarks (Table 1, p. 17 — vs Gemini-3-Flash, GPT-5.4, Claude-Sonnet-4.6, Gemma-4-31B, Qwen3-VL-235B-A22B-Thinking)

| Category | Benchmark | Best frontier | Ours-284B-A13B | Δ |
|---|---|---|---|---|
| Counting | CountQA (EM) | 66.1 (Gemini-3-Flash) | 64.9 | -1.2 |
| Counting | CountQA (RA@10) | 75.1 (Gemini-3-Flash) | 74.1 | -1.0 |
| Counting | Pixmo-Count (EM) | 88.2 (Gemini-3-Flash) | **89.2** | **+1.0** |
| Counting | DS_Finegrained_Counting (EM) | 87.2 (Qwen3-VL) | **88.7** | **+1.5** |
| Spatial | MIHBench (ACC) | 83.5 (GPT-5.4) | **85.3** | **+1.8** |
| Spatial | SpatialMQA (ACC) | 67.0 (Gemini-3-Flash) | **69.4** | **+2.4** |
| Spatial | EmbSpatial (ACC) | 82.6 (Gemini-3-Flash) | **83.7** | **+1.1** (tie w/ Gemma-4) |
| Spatial | CV-Bench (ACC) | 88.6 (Gemini-3-Flash) | 88.4 | -0.2 |
| Spatial | OmniSpatial (ACC) | 59.6 (Gemini-3-Flash) | 59.5 | -0.1 |
| Spatial | DS_Spatial_Reasoning (ACC) | 97.2 (Claude-Sonnet-4.6) | **98.7** | **+1.5** |
| Topological | DS_Maze_Navigation (ACC) | 50.6 (GPT-5.4) | **66.9** | **+16.3** |
| Topological | DS_Path_Tracing (ACC) | 46.5 (GPT-5.4) | **56.7** | **+10.2** |

**Best/tie-best on 8 of 12 benchmarks; ≥+10pt on 2 of 12 (both topological)**. The topological reasoning gap is the headline — ~33% relative improvement over GPT-5.4 on Maze Navigation, ~22% on Path Tracing. These are the tasks where the Reference Gap matters most: dense spatial deduction over a structured layout where natural language pointers fail catastrophically.

### Limitations (per §4)

1. **Fine-grained perception still bottlenecked by input resolution** — the framework is complementary to "Thinking with Images" / cropping methods, not a substitute.
2. **Trigger-word activation** — the visual-primitive thinking mode requires explicit trigger words; auto-detection of when to invoke is future work.
3. **Cross-scenario generalization for points** — point-based topological reasoning is brittle outside in-domain training; broader applicability is open.

## Cemini relevance

### Direct (operational)

1. **DeepSeek-V4-Flash dependency stack thickens.** With AHE (+10.1pp harness gain) and IKP (calibration set inclusion) and now this paper (multimodal extension), three independent 2026 papers ground research on `deepseek-v4-flash`. Cemini's brain choice is the most-instrumented frontier MoE in the academic literature for FY2026. Bus-factor improves further.
2. **Token-efficient multimodal substrate.** If Cemini ever needs to ingest charts (technical analysis), spatial layouts (geo-OSINT for satellite imagery), or visual primitives (annotated docs), the `~90 KV-entry` cost vs 800-1100 for frontier alternatives is a 9-12× inference-cost reduction at frontier-comparable quality. The Spaceshift Sentinel-1 SAR pilot in @sources/spaceshift-sateais-api.md becomes more economical if/when the DeepSeek API surfaces this capability.
3. **Topological reasoning advantage = chart-pattern + spatial-data superpower.** +16.3pp Maze Navigation + +10.2pp Path Tracing translates to better head-and-shoulders / triangle / wedge detection on TradingView-style charts (where the pattern *is* the topology), better candidate-region tracing on satellite imagery, better pipeline-flow inference on schematic diagrams.

### Indirect (architectural)

4. **CSA + 3×3 token compression as a Cemini-internal pattern.** If Cemini ever needs to embed visual data into the analyst pipeline, the 7,056× pixel-to-KV-cache compression is a reference architecture for staying within the Hetzner CPX21 RAM envelope. The KV-cache discipline is the operative lesson — even text-only Cemini analysts could borrow CSA-flavored compression for long-context (256K) reasoning.
5. **Difficulty-filtered RL data (Easy/Normal/Hard split)**. The "only Normal-Level enters RL training" filter is reusable: when Cemini ever runs experiential-knowledge optimization (per @sources/training-free-grpo-cai-2025.md), pre-rollout-then-filter is a clean pattern for selecting useful gradient samples.
6. **OPD (On-Policy Distillation)** as a unification pattern. If Cemini ever splits an analyst into specialist + generalist nodes, OPD is the reference for re-merging without losing specialist capability.

### Reservations

- **Not yet API-surfaced.** This is research output; the `deepseek-v4-flash` API endpoint may or may not expose vision-language capability today. [NEEDS VERIFICATION 2026-04-30 — check DeepSeek API docs for vision endpoints + model names that include this work's capability]
- **`DS_*` benchmarks are in-house** (Maze, Path Tracing, Finegrained Counting, Spatial Reasoning). The +16pt Maze gap is on a benchmark this team built — possible (though they note manual verification + filtering) some benchmark-construction-bias inflates the gap. The public Pixmo-Count and SpatialMQA results (+1.0, +2.4 respectively over best frontier) are the more conservative read.
- **Code release status unclear** from the inbox copy — the paper cites HAI-LLM and references DeepSeek-V4 (DeepSeek-AI 2026 ref [3]) but no GitHub URL appears in the extracted text. Reproduction depends on DeepSeek's release cadence.

## Snippets

### "Reference Gap" definition (p. 1, abstract)

> "Despite the remarkable progress in Multimodal Large Language Models (MLLMs), the prevailing Chain-of-Thought (CoT) paradigms remain predominantly confined to the linguistic space. While recent advancements have focused on bridging the *Perception Gap* through high-resolution cropping (e.g., Thinking with Images), they overlook a more fundamental bottleneck: the *Reference Gap*. The inherent ambiguity of natural language often fails to provide precise, unambiguous pointers to complex spatial layouts, leading to logical collapse in tasks requiring rigorous grounding."

### Paradigm shift framing (p. 2)

> "We move beyond treating visual grounding as a secondary task or a final output. We elevate spatial markers—points and bounding boxes—to 'minimal units of thought' that are interleaved directly into the model's reasoning trajectory."

### Architecture compression numbers (p. 4)

> "To illustrate this pipeline, consider an input image of 756×756 resolution comprising 571,536 pixels. The patch embedding layer processes this into 2,916 image patch tokens for the ViT. Following the 3×3 compression, only 324 visual tokens are fed into the LLM during the prefilling stage. Ultimately, the CSA mechanism reduces this to a mere 81 visual KV entries in the KV cache. Throughout this entire process, from raw pixels to the final KV cache entries, the system achieves an overall compression ratio of 7,056×."

### Difficulty-filter for RL training data (p. 15)

> "Easy-Level: All N rollouts are correct. / Normal-Level: The number of correct rollouts k satisfies 1 ≤ k < N. / Hard-Level: All N rollouts are incorrect. We select samples from the 'Normal-Level' category for RL, ensuring that the model receives valuable supervisory signals during the GRPO training process."

### Maze navigation reward decomposition (p. 14)

> "The final reward is a weighted combination of: causal exploration progress (1 - distance/path-length, truncated at first wall violation) + exploration completeness (for unsolvable mazes) + wall violation penalty (1 - violations/legal-transitions). The score directly penalizes each incorrect connectivity judgment, ensuring the model maintains accurate spatial understanding throughout the trajectory."

### OPD objective (p. 16, eq. 2)

> "Given a set of N expert models {π_E1, π_E2, ..., π_EN}, the OPD objective function is defined as: L_OPD(θ) = Σᵢ wᵢ · D_KL(π_θ ∥ π_Eᵢ), where wᵢ denotes the weight assigned to each expert model, D_KL represents the reverse Kullback-Leibler (KL) divergence loss, and π_θ denotes the student model. We adopt full-vocabulary logit distillation for our OPD implementation."

## Open questions / NEEDS VERIFICATION

- `[CONFIRMED 2026-08-20]` — public DeepSeek API docs list **deepseek-v4-flash** and **deepseek-v4-pro** with text features (JSON, tools, FIM, thinking). No image/vision modality on https://api-docs.deepseek.com/quick_start/pricing. TwVP weights are not a hosted endpoint.
- `[CONFIRMED 2026-08-20]` — `github.com/deepseek-ai/Thinking-with-Visual-Primitives` returns **404**. Third-party mirrors exist; they are not an official weights drop. Paper/report only.
- `[OPEN QUESTION 2026-04-30]` — citation in DeepSeek-V4 base paper (ref [3]) — confirm `DeepSeek-V4` is the actual base, not just architectural lineage. The paper cites `DeepSeek-V4-Flash` consistently but the V4 reference [3] is internal. Public API model versions (as of this check): DeepSeek-V4-Flash-0731 / DeepSeek-V4-Pro-0813.
- Reproducibility: HAI-LLM is High-flyer's tool — public release status uncertain.
