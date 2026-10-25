---
title: "Sherry — Hardware-Efficient 1.25-Bit Ternary Quantization via Fine-grained Sparsification (Huang et al., Tencent + CityU HK + McGill, 2026)"
type: source
tags: [paper, quantization, ternary, edge-llm-deployment, hardware-efficient, simd-alignment, qat, llama-3-2, tencent-angelslim, refutation-premium, cemini-relevant, deep-read]
keywords: [sherry, hardware-efficient-ternary, 1-25-bit, three-four-sparsity, simd-friendly, lookup-table-engine, lut-based-execution, arenas-module, annealing-residual-synapse, gradient-homogenization, weight-trapping, sparse-absmean, qat, quantization-aware-training, llama-3-2-1b, llama-3-2-3b, intel-i7-14700hx, ultrafineweb, lm-evaluation-harness, piqa, arc-easy, arc-challenge, hellaswag, winogrande, bitnet-cpp, tequila, ternaryllm, paretoq, spectra, tencent-angelslim, hong-huang-cityuhk, dapeng-wu, edge-llm, cpu-inference]
related:
  - sources/agentic-harness-engineering.md
  - sources/incompressible-knowledge-probes-li-2026.md
  - sources/moe-efficiency-leverage-tian-2026.md
  - sources/moe-surpass-dense-equal-resource-li-2026.md
  - entities/infrastructure/deepseek-r1-14b.md
  - entities/infrastructure/hetzner.md
  - entities/infrastructure/localai.md
  - concepts/llm-agent-systems.md
  - concepts/high-signal-paper-patterns.md
maturity: validated
read_status: read
created: 2026-04-30
updated: 2026-08-20
---

## Relations

- @sources/agentic-harness-engineering.md — AHE is harness-side (orchestration); Sherry is substrate-side (hardware-efficient inference). Both reduce the operational cost of running LLMs without changing their reasoning capability.
- @sources/incompressible-knowledge-probes-li-2026.md — IKP shows factual capacity tracks `log(total params)`; Sherry shows you can preserve **task accuracy** at 1.25 bits (≤0.5% gap to BF16 on ARC-Challenge for 1B). Combined: ternary models keep reasoning capability per IKP while shrinking deployment footprint per Sherry. Both Tencent-adjacent in 2026.
- @sources/moe-efficiency-leverage-tian-2026.md — MoE-leverage paper is at the *training-economics* frontier; Sherry is at the *deployment-economics* frontier. Both reduce active-compute cost; complementary axes.
- @sources/moe-surpass-dense-equal-resource-li-2026.md — same complementarity: Sherry compresses the *weights*, MoE-Surpass reorganizes the *params*; both at strict-equal-resource frontier.
- @entities/infrastructure/deepseek-r1-14b.md — the **retracted local-weights path**. Sherry is the kind of technique that, *if applied to a DeepSeek-V4-Flash-base-distilled model* + *if Cemini ever obtained local-inference hardware*, would put a frontier-grade brain on a commodity CPU. Reactivates the local-deployment argument with much lower hardware bar.
- @entities/infrastructure/hetzner.md — the CPX21 host is CPU-only, 4 GB RAM. Sherry-quantized 1B-parameter LLaMA-class models fit comfortably in this envelope (estimated <300MB weights at 1.25-bit + scaling factors, well under the 4GB ceiling). **First** local-inference path that's actually feasible on the deployed box.
- @entities/infrastructure/localai.md — LocalAI exposes OpenAI-compatible chat-completions for local-weights LLMs. Sherry-quantized models loaded into BitNet.cpp could sit behind LocalAI; Cemini's existing client (`base_url="http://localai:8080"`) gets a local fallback at near-zero RAM cost.
- @concepts/llm-agent-systems.md — **adds depth to "Brain capacity / black-box evaluation" sub-topic** with a deployment-side complement to IKP/MoE-leverage/MoE-surpass. The four-paper set is now: capacity (IKP), training compute (MoE-leverage), strict-equal-resource (MoE-surpass), **deployment compression (Sherry)** — full lifecycle covered.
- @concepts/high-signal-paper-patterns.md — exemplar of "**hardware-aligned algorithmic refinement**" pattern. Sherry's refutation: the prior 1.67-bit ternary work claimed the bit-width / speed tradeoff was inevitable; Sherry shows it isn't (1.25-bit + faster + accuracy-matched). Rare for a quantization paper to refute on three axes simultaneously.

## Raw Concept

- **Original title**: Sherry: Hardware-Efficient 1.25-Bit Ternary Quantization via Fine-grained Sparsification
- **Authors**: Hong Huang* (City U HK), Decheng Wu (Tencent), Qiangqiang Hu (Tencent), Guanghua Yu (Tencent), Jinhai Yang (City U HK), Jianchen Zhu (Tencent), Xue Liu (McGill), Dapeng Wu (City U HK). * = work with Tencent.
- **Affiliations**: City University of Hong Kong + Tencent + McGill University
- **Type**: Research paper PDF, 17 pages
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Sherry- Hardware-Efficient 1.25-Bit Ternary Quantization via Fine-grained Sparsification.pdf`
- **Retrieved**: 2026-04-30 (laptop drop)
- **Read status**: read (full deep-read 2026-04-30)
- **arXiv**: `2601.07892`
- **Code/repo**: `github.com/Tencent/AngelSlim` (Tencent's open-source LLM compression toolkit)
- **License**: Apache-2.0 for AngelSlim toolkit, except third-party components listed in `LICENSE` (`gh api` 2026-08-20; GitHub SPDX field is `NOASSERTION`)
- **Test hardware**: Intel i7-14700HX CPU (commodity desktop)

## Narrative

**Thesis.** Existing ternary quantization implementations are forced to choose between two suboptimal hardware-execution strategies:

- **2-bit packing** — each weight in 2 bits (33% wastage vs theoretical 1.58-bit floor); SIMD-friendly but bloated.
- **1.67-bit packing** — three weights in 5 bits (closer to floor); SIMD-*hostile* (3-way grouping conflicts with power-of-two vector lanes), so slower despite smaller size.

Sherry refutes the bit-width-vs-speed tradeoff with a third option: **3:4 sparsity** that packs **four weights into five bits** (= **1.25 bits/weight**), restoring power-of-two SIMD alignment. The result: smaller AND faster AND accuracy-matched to 1.67-bit SOTA.

**The naïve 3:4 sparse training fails — Arenas fixes it.** Forcing exactly one zero per 4-weight block triggers **gradient homogenization**: zeros spread uniformly mimic a Hadamard transform; downstream gradients flatten; weights collapse into binary-like polarization (the "weight trapping" issue). Effective Rank of gradients drops below 750 in 4096-dim layers — a >5× collapse vs full-rank training, indicating massive loss of learning degrees of freedom.

**Arenas (Annealing Residual Synapse)** solves trapping by adding a residual full-precision bypass alongside the quantization path during training. The bypass injects heterogeneous gradients into latent weights; an annealing gate `λ_t` decays from 1 to 0 over training, so the bypass disappears at convergence. **No inference overhead** — Arenas is training-only.

### Method (the 3:4 sparsity formalization)

For weight matrix `W ∈ R^{d_in × d_out}`, ternary quantization is `Q(W) = T α` with `T ∈ {-1, 0, +1}^{d_in × d_out}`, scaling factors `α ∈ R^{d_out}`, thresholds `Δ`. The 3:4 constraint is enforced via:

```
∀ b ∈ {1, 5, ..., d_in - 4} : ‖T_{b:b+3, j}‖_0 = 3
```

i.e., exactly **3 non-zero values per 4-weight block** along input dimension. Solved greedily by **Sparse-AbsMean**:

- For each block `W_{b:b+3, j}`, prune the element with smallest |·| (set to 0); ternary-assign the other three by sign.
- Optimal scaling factor `α*_j = (4 / 3 d_in) · Σ_{i ∈ S_j} |W_{i,j}|` where `S_j = {i | T_{i,j} ≠ 0}`.

**Why 3:4 is the sweet spot** (per the paper):
1. **SIMD-friendly alignment** — `M = 4` matches power-of-two vector lanes.
2. **Bit-width near theoretical floor** — `1.25` vs `1.58` (log₂3) ternary lower bound.
3. **Lookup-table compatibility** — works inside BitNet.cpp's LUT engine.
4. **Avoids 1.67-bit's 3-way bit-shuffling overhead.**

### Arenas module (training-time fix for weight trapping)

```
Forward (during QAT):
  Y = X · (T α)        ← quantization path
    + λ_t · X · W       ← Arenas residual synapse path

Backward:
  ∂L/∂W ≈ X^T · ∂L/∂Y · (T α + λ_t W)^T

λ_t schedule: linear / cosine / exponential decay, with optional warmup
λ_t → 0 at end of training; auxiliary path is removed post-training
```

The residual path supplies heterogeneous gradients that maintain Effective Rank in the latent weights. Ablation (Fig. 6): Arenas adds **+2.67% (1-bit)**, **+4.59% (1.25-bit Sherry)**, **+2.98% (1.67-bit AbsMean)** average accuracy across the 5-task suite. Arenas helps even outside its primary use case (the 1.67-bit baseline gains too).

### Benchmark results

**Setup:** LLaMA-3.2 1B + 3B base architectures; 10B-token QAT on UltraFineWeb; group-wise quantization with group size 128; lm-evaluation-harness across PIQA / ARC-Easy / ARC-Challenge / HellaSwag / WinoGrande (zero-shot).

| Model | Method | Bit-width | ARC-e | ARC-c | HelS | PIQA | WinG | **Avg** |
|---|---|---|---|---|---|---|---|---|
| LLaMA3.2-1B | BF16 | 16 | 0.654 | 0.313 | 0.477 | 0.742 | 0.603 | **0.558** |
| LLaMA3.2-1B | Tequila (prior SOTA) | 1.67 | 0.645 | 0.305 | 0.391 | 0.710 | 0.542 | **0.519** |
| **LLaMA3.2-1B** | **Sherry** | **1.25** | 0.647 | 0.309 | 0.388 | 0.699 | 0.550 | **0.519** |
| LLaMA3.2-3B | BF16 | 16 | 0.745 | 0.422 | 0.552 | 0.768 | 0.691 | **0.636** |
| LLaMA3.2-3B | Tequila | 1.67 | 0.702 | 0.346 | 0.464 | 0.739 | 0.627 | **0.576** |
| **LLaMA3.2-3B** | **Sherry** | **1.25** | 0.688 | **0.364** | 0.452 | 0.736 | 0.593 | **0.567** |

Sherry **matches the average SOTA exactly at 1B** at 25% smaller bit-width, and is **0.009 below SOTA at 3B** while leading on ARC-Challenge (the hardest benchmark, +0.018 over Tequila). Notably narrows the BF16 gap to <0.5% on ARC-Challenge for 1B.

### Inference speed (Table 4, BitNet.cpp on Intel i7-14700HX)

- **3B model: 18% speedup** over 1.67-bit baseline (TL2), additional speedup over 2-bit (I2_S).
- **700M model**: similar pattern.
- Speed improvement attributed to power-of-two SIMD alignment + elimination of bit-shuffling overhead.

(Note: paper abstract claims "10% speedup" for 1B; Table 4 reports 18% for 3B. Likely model-size-dependent — abstract conservative figure may refer to 700M or 1B configuration.)

### Stability across granularity (Table 3)

| Granularity | Avg Acc ± Std |
|---|---|
| Per-tensor | 0.502 ± 0.010 |
| Per-channel | 0.513 ± 0.011 |
| Per-group | 0.519 ± 0.014 |

Per-group quantization (group=128) is the recommended default but the per-tensor degradation is only 1.7pt — robust deployment story.

## Cemini relevance

### Direct (operational, but conditional)

1. **First local-inference path actually feasible on the deployed Hetzner CPX21.** Sherry-quantized LLaMA-3.2-1B at 1.25 bits weighs **~0.16 GB** (1B params × 1.25 bits / 8 bits/byte ≈ 156 MB) plus per-group scaling factors — well under the CPX21's 4 GB RAM ceiling. Even the 3B variant (~470MB weights) fits comfortably alongside the existing services. **Activates** the previously-retracted local-weights path of `@entities/infrastructure/deepseek-r1-14b.md`, but with a **smaller** model.
2. **Hardware match**. Sherry's benchmarks are on **Intel i7-14700HX** (commodity desktop CPU). Hetzner's CPX21 is AMD x86_64 — not identical, but the SIMD-friendliness logic (power-of-two AVX2/AVX-512 lanes) carries across vendors; performance should generalize.
3. **AngelSlim is Tencent open-source.** `github.com/Tencent/AngelSlim` is the LLM-compression toolkit. **License `[CONFIRMED 2026-08-20]`:** Apache-2.0 except third-party components named in `LICENSE` (GitHub API SPDX `NOASSERTION` — read the file, do not trust the badge).

### Reservations / what it does NOT enable

4. **Cemini cannot apply Sherry to DeepSeek-V4-Flash directly.** Sherry is **QAT (Quantization-Aware Training)** — requires gradient-aware retraining on weights you control. Cemini's brain (`@entities/infrastructure/deepseek-api.md`) is **API-only**; the weights are not local. Sherry **only applies if** Cemini distills DeepSeek-V4-Flash → a smaller open-weight student model AND has training compute. Both are large lifts.
5. **The relevant upgrade path** is therefore: **distill or fine-tune** an open-weight base (LLaMA-3.2 / Qwen / DeepSeek-distilled-Qwen) → apply Sherry → deploy via BitNet.cpp + LocalAI on the Hetzner box. This is a multi-month project with non-trivial dependencies (training compute, eval harness, dataset selection, distillation supervision).
6. **Edge-device local LLM is not currently on Cemini's roadmap.** API-first is the deployment doctrine. Sherry is a **future-option** technique, not a near-term integration. File under the same drawer as `deepseek-r1-14b` retraction — wait for hardware capacity and operational need to converge.

### Indirect (theoretical / methodology)

7. **Arenas as a general "training trapping" pattern.** The annealing-residual-synapse trick (auxiliary path with decaying gate) is a clean example of a more general pattern: when a constrained optimization causes gradient pathology, add an unconstrained bypass with annealing schedule. Reusable mental model for any future training-time pathology Cemini encounters.
8. **3:4 sparsity = SIMD-friendliness as hardware co-design.** Sherry's framing — power-of-two alignment matters more than absolute bit-density — generalizes to any compute kernel design Cemini might build. If Cemini ever writes custom CUDA / SIMD ops for trade-signal generation, the same alignment discipline applies.

### Citation hygiene

- The paper aggressively positions against TernaryLLM, ParetoQ, LLM-QAT, BitNet (1.3B), Spectra, TequilaLLM. Comparison tables are reproducible (UltraFineWeb 10B QAT tokens, lm-evaluation-harness, three-seed averaging).
- Tencent first-author (Hong Huang) overlap with City U HK + McGill is consistent with the "industrial-academic Tencent hybrid" pattern.

## Snippets

### The SIMD-vs-bitwidth refutation framing (p. 1, abstract + Fig. 2 caption)

> "Most existing methods must choose between 2-bit aligned packing, which incurs significant bit wastage, or 1.67-bit irregular packing, which degrades inference speed. To resolve this tension, we propose Sherry, a hardware-efficient ternary quantization framework. Sherry introduces a 3:4 fine-grained sparsity that achieves a regularized 1.25-bit width by packing blocks of four weights into five bits, restoring power-of-two alignment."

### The weight-trapping discovery (p. 4-5)

> "Naive 3:4 sparse ternary training exhibits weight trapping, where values collapse into a binary-like polarization, leading to a significant accuracy gap compared to dense models. ... Our Sherry utilizes the Arenas module to achieve a trap-free distribution, bridging the performance gap to dense ternary models."

### Effective Rank diagnosis (p. 5)

> "The 3:4 sparse regime exhibits a low ER (ER < 750), a level of spectral collapse comparable to that of binary quantization, despite the gradient matrix having a total dimensionality of 4096. This indicates a significant loss of learning degrees of freedom in naive 3:4 ternary sparse training."

### Sparse-AbsMean optimal solution (p. 4, Eq. 4-5)

> "For each block i ∈ [b, b+3], the optimal ternary element T*_{i,j} is given by: T*_{i,j} = 0 if i = arg min |W_{i,j}|; sign(W_{i,j}) otherwise. Given this optimal ternary matrix T, the optimal scaling factor α*_j for the j-th output channel is calculated as the mean absolute value of the non-pruned weights: α*_j = (4 / 3 d_in) · Σ_{i ∈ S_j} |W_{i,j}|."

### Arenas annealing-gate principle (p. 5-6)

> "During the training phase, the output of a ternary linear layer is augmented by a residual synapse with an annealing gate λ_t. As λ_t decays to zero, the auxiliary path is completely removed post-training, without any inference overheads."

### Inference speedup attribution (p. 8)

> "For the 3B model, Sherry achieves a 18% speedup over the 1.67-bit baseline. This improvement is attributed to our 3:4 structured sparsity and hardware-aligned 5-bit packing, which maximizes SIMD vector lane utilization and eliminates the bit-shuffling overhead inherent in non-power-of-two packing schemes."

## Open questions / NEEDS VERIFICATION

- `[CONFIRMED 2026-08-20]` — Tencent/AngelSlim `LICENSE` is Apache-2.0 except listed third-party components. GitHub SPDX metadata is `NOASSERTION`; file text is authoritative.
- `[CONFIRMED 2026-08-20]` — repo is a compression **toolkit** (code + QAD configs, e.g. Qwen3 Sherry QAD yaml). No drop-in pre-quantized SherryLLM weights for LLaMA-3.2 1B / 3B found; LLaMA-3.2 paths appear as vLLM-patch comments. Adoption cost is train/QAT, not download-and-serve.
- `[OPEN QUESTION 2026-04-30]` — does BitNet.cpp run on the AMD x86_64 (CPX21) target? Benchmarks are on Intel i7; AMD compatibility likely but not verified.
- `[OPEN QUESTION 2026-04-30]` — does any DeepSeek-distilled small model (e.g. `deepseek-r1-distill-qwen-1.5b`) come with a working Sherry-style training recipe, or would Cemini need a custom QAT pipeline?
- Open extension: is there an MoE-friendly variant of Sherry? Cemini's brain is MoE (`deepseek-v4-flash`); ternary quantization on MoE-experts vs shared-router has open empirical questions.
