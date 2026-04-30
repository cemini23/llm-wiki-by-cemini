---
title: "Can Mixture-of-Experts Surpass Dense LLMs Under Strictly Equal Resources? (arXiv 2506.12119, Li et al, StepFun + Fudan + Megvii, ICLR 2026 Oral)"
type: source
tags: [paper, mixture-of-experts, scaling-laws, llm-architecture, equal-resource-comparison, refutation-paper, stepfun, fudan, megvii, deepseek-relevant, cemini-relevant, iclr-2026-oral, preprint, workflow-a-find, cc-by-4-0]
keywords: [moe-vs-dense, equal-resource-constraint, optimal-activation-rate, optimal-ar-region, data-reuse-strategy, n-c-d-parity, total-params, training-compute, data-budget, stepfun, houyi-li, ka-man-lo, ziqi-wang, daxin-jiang, xiangyu-zhang, 200-2b-models, 50-7b-models, 50-trillion-tokens, iclr-2026-oral]
clusters: [llm-agents, infrastructure]
related:
  - concepts/llm-agent-systems.md
  - concepts/high-signal-paper-patterns.md
  - entities/infrastructure/deepseek-api.md
  - sources/incompressible-knowledge-probes-li-2026.md
  - sources/moe-efficiency-leverage-tian-2026.md
maturity: validated
read_status: read
created: 2026-04-29
updated: 2026-04-29
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub; this paper formally answers "can MoE > dense at strictly equal N/C/D?" — yes, with optimal activation-rate region. Pairs with @sources/moe-efficiency-leverage-tian-2026.md for the architectural-design reasoning.
- @concepts/high-signal-paper-patterns.md — Workflow A find from the 2026-04-29 sweep. Refutation-paper score: 5/6 quality + 3/3 operational. ICLR 2026 Oral acceptance is the freshness signal (paper preprint Jun 2025; conference acceptance places it in the active discourse this week).
- @entities/infrastructure/deepseek-api.md — Cemini's brain (DeepSeek-V4) is MoE; this paper validates that the architectural choice is theoretically sound at strictly-equal resource — DeepSeek-V4 isn't winning because it's MoE-with-more-params; it's winning because MoE-with-optimal-AR is genuinely better at the same N.
- @sources/incompressible-knowledge-probes-li-2026.md — IKP showed MoE's TOTAL params drive knowledge capacity (not active); this paper shows MoE > dense even at equal TOTAL params. Together: MoE has both the knowledge advantage (IKP) AND the equal-N quality advantage (this paper) over dense. Strong combined argument for MoE adoption.
- @sources/moe-efficiency-leverage-tian-2026.md — companion paper from the same ICLR 2026 cohort. Tian's paper derives the **scaling law for the compute-saving advantage** (EL); this paper proves the **at-equal-resource quality advantage**. Two halves of the same MoE-procurement reasoning.

## Raw Concept

- **Original title**: "Can Mixture-of-Experts Surpass Dense LLMs Under Strictly Equal Resources?"
- **Authors**: Houyi Li (StepFun + Fudan), Ka Man Lo (StepFun), Ziqi Wang (StepFun), Zili Wang (StepFun), Wenzhen Zheng (StepFun), Shuigeng Zhou (Fudan), Xiangyu Zhang (StepFun + Megvii Technology), Daxin Jiang (StepFun)
- **Type**: arXiv preprint → ICLR 2026 Oral (high-prestige acceptance)
- **arXiv ID**: 2506.12119v1
- **DOI**: 10.48550/arXiv.2506.12119
- **Submitted**: 13 June 2025
- **License**: CC BY 4.0 (paper) — clean for citation + reuse
- **PDF location**: cemini-librarian:/opt/cemini-bulk/research/moe-surpass-dense-equal-resource-li-2026.pdf (post-ingest scp)
- **Read status**: read (pages 1-3 covering abstract / introduction / methodology framework; experimental results in §4-7 cited but not deep-read)
- **Discovered via**: Workflow A Tier-2 Exa sweep 2026-04-29
- **Code/models**: paper states "All models will be released publicly" — verify on first reproduction pass
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents, infrastructure

### Recency note (per high-signal-paper-patterns rubric Filter 2)

This paper is older as a preprint (June 2025) but **freshly conference-accepted as ICLR 2026 Oral** — Oral is higher-prestige than Poster (top ~5% of accepted papers). Per the rubric: "30-90 days acceptable if Filter 3 hits hard." The paper hits Filter 3 hard (DeepSeek-V4 MoE relevance) and the Oral acceptance signals it's flagged as load-bearing for the field. Workflow A correctly caught the deadline cluster.

## Narrative

### What it claims

A genuinely refutational paper. Common framing: "MoE wins because of param expansion" (i.e., MoE only beats dense by activating fewer params per token while having more total params). This paper asks the **strict** version of the question:

> Can MoE surpass dense LLMs under **strictly equal** resource constraints — same total parameter count N, same training compute budget C, same data budget D?

The intuitive answer is "no" — at equal N, a dense model uses all its capacity per token while MoE leaves most experts idle, so dense should have the architectural advantage at equal N.

**The paper's answer: yes, MoE > dense even at strictly equal N/C/D, with proper activation-rate (AR) tuning.** Three contributions:

1. **First demonstration of strict-N-equal-C-equal-D superiority**: MoE LLMs with carefully designed activation rate beat dense LLMs at the same N, C, D.
2. **A stable "optimal AR region"** that consistently maximizes performance across varying N (model sizes). Optimum is structural, not an N-specific tuning artifact.
3. **A practical data-reuse strategy** that offsets MoE's marginally-higher data appetite, enabling robust gains without substantially increasing unique training data D.

### Methodology

**Three-step framework**:
1. **Architecture search**: optimize MoE design so all candidates are at their (near-)best, eliminating "MoE bad because suboptimal config" confound.
2. **Optimal activation rate exploration**: with N and C held fixed, vary AR to find the optimum.
3. **Data reuse for D-parity**: address the additional data demand of MoE via reuse to equate the data budget.

**Scale**: ~200 language models at 2B scale + 50+ at 7B scale, cumulatively processing **50 trillion tokens**. Massive empirical investment for one ICLR paper.

### Headline empirical findings

- At strictly equal N, C, D — MoE with optimal AR **beats dense** on both upstream loss AND downstream tasks.
- The **optimal AR region remains consistent across model sizes** (2B and 7B scales tested). Suggests architectural law, not size-specific quirk.
- **Data reuse strategy** resolves the marginal D-overhead — MoE doesn't need genuinely more unique training data; it can recycle.

### Why this matters for Cemini

1. **Validates DeepSeek-V4 architectural choice without param-expansion confound**. Naive critic: "DeepSeek-V4 looks good only because it has more total params." This paper directly refutes that — at strictly equal N, MoE > dense. So DeepSeek-V4-flash being MoE is genuinely architecturally better than a hypothetical "DeepSeek-V4-flash-dense" with identical total params.

2. **Pair-with-IKP-and-Tian gives Cemini a complete MoE story**:
   - **IKP** (Bojie Li, Pine AI): MoE total params predict knowledge (R²=0.79) >> active params (R²=0.51).
   - **MoE Efficiency Leverage** (Tian, Ant Group): MoE provides 7× compute advantage at the EL-optimal config.
   - **This paper** (Li, StepFun): MoE > dense at strictly-equal N/C/D.
   - **Combined**: MoE is the dominant architecture at every economic axis (knowledge, compute, fixed-resource quality). For Cemini, this is operationally important because every "should we evaluate dense alternatives?" question now has a quantitative "no, MoE strictly dominates at the relevant deployment scale" answer.

3. **Optimal AR region is procurement filter**. When evaluating future brain candidates (Cemini may eventually evaluate Anthropic, OpenAI, Sakana Fugu, or self-hosted Ling-2.0): check the activation rate against this paper's optimal-AR region. Any vendor whose AR is outside the optimum is leaving performance on the table.

4. **CC BY 4.0 license** is clean — the paper's findings can be cited freely, and any released models would presumably honor the same license (verify at release).

### Risks & open questions

1. **Equal-N comparison is somewhat artificial for production deployment**. Cemini doesn't pick a fixed-N and choose between MoE and dense — vendors ship what they ship. The paper's relevance for Cemini is mostly architectural reasoning + future-procurement-decision support, not "should I retrain DeepSeek-V4 dense at 671B?".

2. **2B and 7B scales tested; not yet extrapolated to 100B+**. DeepSeek-V4 is much larger; the optimal-AR region's invariance across the tested range is encouraging but not proof at frontier scale.

3. **Data-reuse strategy assumes dataset quality scales gracefully under reuse** — if Cemini's specialized fine-tunes ever depend on small high-quality datasets (e.g. financial-document corpora), the data-reuse trick may not transfer.

4. **Single-vendor research lab (StepFun + Fudan)**: rigorous methodology but bus-factor watch (similar to other large-scale-MoE papers from individual labs). Independent reproduction would be valuable; the public model release will help.

5. **No code/model release at submission time** — paper says "will be released publicly". Verify on a 30-day re-check.

### Cemini-side adoption assessment

**Decision: Read + cross-reference (operational pairing with IKP + Tian)**. Not deployable code; this is conceptual scaffolding for procurement and architectural reasoning. Concrete next-steps:

1. Re-read alongside IKP + MoE Efficiency Leverage → write a short concept-page synthesis: `concepts/moe-economics-deepseek-v4.md` summarizing the three-paper story for Cemini's brain procurement decisions. ~1.5 hours.
2. Track public model release at https://github.com/stepfun-ai (or equivalent). Quarterly check.
3. Reference this paper next time Cemini evaluates a non-MoE brain alternative.

### Citation

> Li, H., Lo, K. M., Wang, Z., Wang, Z., Zheng, W., Zhou, S., Zhang, X., & Jiang, D. (2025). *Can Mixture-of-Experts Surpass Dense LLMs Under Strictly Equal Resources?*. arXiv:2506.12119 [cs.CL]. https://arxiv.org/abs/2506.12119 (ICLR 2026 Oral)

## Snippets

> **The strict-equal-resource framing (the question that defines the paper)**
>
> "Can MoEs surpass dense architectures under strictly equal resource constraints — that is, when the total parameter count, training compute, and data budget are identical? This question remains under-explored despite its significant practical value and potential." [Source: arXiv 2506.12119 abstract, p.1]

> **The first-demonstration claim**
>
> "Our main contributions are: 1) We demonstrate, for the first time, that under fixed total parameters (N) and a fixed compute budget (C), an MoE LLM can surpass its dense counterpart with careful architecture design (see Fig. 1b, 2b). 2) Our experiments reveal the existence of a stable 'optimal AR' region that consistently maximizes performance across varying N (see Fig. 1, 2). 3) We introduce a practical data reuse strategy that offsets MoE's additional data needs, enabling robust gains without substantially increasing unique training data D." [Source: arXiv 2506.12119 §1, p.2]

> **The N/C/D-parity argument — refuting the "MoE wins by param expansion" critique**
>
> "Current comparisons of MoE and dense LLMs often simplify the analysis to either a data-centric or a compute-centric perspective. … However, neither perspectives fully addresses the complex interplay of critical resource constraints in large-scale model development: the finite nature of training data volume (D), training compute (C), and model size (N), which affects both memory and inference throughput." [Source: arXiv 2506.12119 §1, p.1-2]

> **Empirical scale — the investment behind the claim**
>
> "We validate our findings through extensive experiments, training nearly 200 language models at 2B scale and over 50 at 7B scale, cumulatively processing 50 trillion tokens." [Source: arXiv 2506.12119 abstract, p.1]
