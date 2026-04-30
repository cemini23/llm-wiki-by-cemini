---
title: "Towards Greater Leverage — Scaling Laws for Efficient Mixture-of-Experts Language Models (arXiv 2507.17702, Tian et al, Ant Group Ling Team, ICLR 2026)"
type: source
tags: [paper, mixture-of-experts, scaling-laws, llm-architecture, efficiency-leverage, ant-group, ling-team, deepseek-relevant, cemini-relevant, iclr-2026, preprint, workflow-a-find]
keywords: [efficiency-leverage, el-metric, moe-scaling-law, expert-activation-ratio, expert-granularity, compute-budget, ling-mini-beta, ant-group, jul-2025-revised-iclr-2026, three-stage-methodology, power-law-relationships, 300-models, ant-group-ling-team, tian, kunlong-chen, jia-liu, ziqi-liu, zhiqiang-zhang, jun-zhou]
clusters: [llm-agents, infrastructure]
related:
  - concepts/llm-agent-systems.md
  - concepts/high-signal-paper-patterns.md
  - entities/infrastructure/deepseek-api.md
  - sources/incompressible-knowledge-probes-li-2026.md
  - sources/moe-surpass-dense-equal-resource-li-2026.md
maturity: validated
read_status: read
created: 2026-04-29
updated: 2026-04-29
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub; this paper provides the most rigorous MoE-architecture-design scaling law in the corpus, paired with @sources/moe-surpass-dense-equal-resource-li-2026.md for the strict-equal-resource framing.
- @concepts/high-signal-paper-patterns.md — Workflow A find (2026-04-29 sweep): rubric-validated catch from the ICLR 2026 deadline cluster. Score 5/6 quality + 3/3 operational. Cited by Workflow A as "directly Cemini-relevant for DeepSeek-V4 MoE deployment economics."
- @entities/infrastructure/deepseek-api.md — DeepSeek-V4 (Cemini's brain) is an MoE architecture; this paper's Efficiency Leverage scaling law directly informs "what's the compute-cost story behind DeepSeek-V4-flash vs the proprietary alternatives" — pairs with IKP's parameter-count estimate to give Cemini a quantitative deployment-economics picture of its own brain.
- @sources/incompressible-knowledge-probes-li-2026.md — sibling 2026-04 ICLR-cycle MoE paper; IKP measures the **knowledge-storage** side of MoE economics (total params predict knowledge, not active); this paper measures the **compute-cost** side (activation ratio drives Efficiency Leverage). Together they form the "MoE economics for Cemini" pairing.
- @sources/moe-surpass-dense-equal-resource-li-2026.md — companion paper from the same ICLR 2026 cohort: where this paper derives the Efficiency Leverage scaling law for MoE-vs-dense, the companion paper shows that MoE > dense even at strictly-equal N/C/D. The two papers are complementary halves of the "should you ever deploy dense?" debate.

## Raw Concept

- **Original title**: "Towards Greater Leverage: Scaling Laws for Efficient Mixture-of-Experts Language Models"
- **Authors**: Changxin Tian, Kunlong Chen, Jia Liu, Ziqi Liu, Zhiqiang Zhang*, Jun Zhou (Ling Team, Ant Group; * corresponding)
- **Type**: arXiv preprint → ICLR 2026 Poster (peer-reviewed, P3-#1912 Apr 23 2026)
- **arXiv ID**: 2507.17702v4
- **DOI**: 10.48550/arXiv.2507.17702
- **Submitted**: July 20, 2025; revised October 21, 2025 (v4)
- **License**: arXiv non-exclusive distribution license 1.0 (paper)
- **PDF location**: cemini-librarian:/opt/cemini-bulk/research/moe-efficiency-leverage-tian-2026.pdf (post-ingest scp)
- **Read status**: read (pages 1-3 covering abstract + intro + key insights; methodology details + Ling-mini-beta validation in pages 4+ noted but not deep-read in this pass)
- **Discovered via**: Workflow A Tier-2 Exa sweep 2026-04-29, query "MoE / scaling / parameter-estimation"
- **Primary cluster**: llm-agents (LLM architecture/scaling)
- **All clusters**: llm-agents, infrastructure (since deployment-economics-relevant)

### Recency note (per high-signal-paper-patterns rubric Filter 2)

This paper is older as a preprint (July 2025) but is being **freshly conference-accepted** at ICLR 2026 (poster Apr 23 2026). Per the rubric: "30–90 days acceptable if Filter 3 hits hard (Cemini-domain overlap is direct + concrete deployment surface is obvious)." The paper hits Filter 3 hard via DeepSeek-V4 MoE architecture relevance, so the recency tolerance is justified. The Workflow A sweep correctly caught the ICLR 2026 deadline cluster.

## Narrative

### What it claims

The MoE architecture decouples total parameters from per-token compute cost, but this **decouples capacity prediction**: neither total nor activated parameter count alone is a reliable proxy for performance. The paper introduces **Efficiency Leverage (EL)**, a single metric that quantifies how much compute an MoE configuration saves vs a dense model achieving the same loss:

```
EL(X_MoE | X_dense) = C_dense / C_moe
```

EL = 2 means the MoE reaches the same loss with half the FLOPs as dense.

### Methodology

**Three-stage approach**:
1. **Establish optimal hyperparameters and model-data allocation** for both dense and MoE so all comparisons are between "well-trained" models.
2. **Deconstruct MoE into design dimensions**: expert activation ratio, expert granularity, shared expert ratio, etc.; analyze each dimension's impact on EL.
3. **Integrate empirical findings into a unified scaling law** predicting EL from configuration.

**Scale**: 300+ trained models, up to 28B parameters.

### Key empirical insights (4 principles governing MoE EL)

1. **Activation ratio drives EL** (primary). Stable power law: as activation ratio decreases (sparser MoE), EL increases. Sparsely-activated pathways yield consistent, predictable efficiency gains.

2. **Expert granularity is a non-linear modulator** (log-polynomial). Identified **optimal range: 8 to 12 experts**. This effect is independent of compute budget. Granularity outside this range pays an EL penalty.

3. **Compute-budget amplification**. EL is not static — it scales (power law) with the training compute budget. The advantage of MoE grows as compute resources expand. **Implication**: bigger pre-training runs give MoE relatively more advantage vs dense.

4. **Other architectural factors are secondary**. Shared experts, layer arrangements: small EL impact, can be set to broadly-applicable near-optimal values without much tuning.

### The unified scaling law + validation

The paper derives a unified scaling law for EL combining compute budget, activation ratio, and expert granularity (Eq. 13). To validate it:

- **Predict**: an MoE with **3.1% activation ratio + granularity 12** at compute budget 1e22 FLOPs should achieve **EL > 7×**.
- **Build**: "Ling-mini-beta" — pilot model for the Ling-2.0 series.
  - **0.85B activated parameters / 17.5B total parameters** (3.4% activation ratio in practice; granularity 12)
  - Trained on identical 1T-token high-quality dataset alongside a 6.1B dense baseline.
- **Result**: Ling-mini-beta achieves **lower final training loss** AND **slight downstream-task advantage** vs the 6.1B dense, while consuming **>7× fewer computational resources**. ✅ scaling-law prediction confirmed.

### Why this matters for Cemini

1. **Cemini's brain is MoE**. DeepSeek-V4 family (deepseek-v4-flash, deepseek-v4-pro-think) is MoE. This paper provides the quantitative framework to reason about **how much computational efficiency Cemini's brain provides over a dense alternative at the same total parameter count** — i.e. why DeepSeek-V4-flash is the right choice over a hypothetical dense same-N alternative.

2. **Pairs cleanly with IKP**. IKP showed that MoE total parameters predict knowledge (R²=0.79) far better than active parameters (R²=0.51). This paper shows that activation ratio drives efficiency. **Combined**: Cemini gets a model whose **knowledge capacity is bounded by total params** AND whose **compute cost is bounded by activated params** — a strictly better deal than dense at the same total-N.

3. **Activation-ratio sweet spot for vendor selection**. If Cemini ever evaluates alternative MoE vendors (Sakana Fugu, Mistral Large, etc.), the optimal-AR + optimal-granularity findings give Cemini a vendor-procurement filter: "is this vendor's MoE configured close to the EL optimum or are they leaving compute on the table?"

4. **Ant Group's Ling-2.0 series is a credible competitor**. The Ling-mini-beta proof point (0.85B active matching 6.1B dense at 7× less compute) suggests Ant Group's series will be a serious contender for Cemini's brain procurement decision over the next 12-18 months. Track the series.

### Risks & open questions

1. **License-on-derived-models** [NEEDS VERIFICATION 2026-04-29] — Ling-mini-beta release license? If publicly available under permissive terms, Cemini could use it as a fallback brain (validation of cross-vendor pattern from IKP). Check Hugging Face / Ant Group GitHub.
2. **Optimum granularity range (8-12) was found with standard load-balancing loss** — alternative routing/loss functions might shift this. Cemini's specific deployment may not honor the assumption (we're consumers, not trainers).
3. **The 7× efficiency gain at 1e22 FLOPs may not translate at smaller scales** — the compute-budget power law means EL grows with C. Smaller-scale fine-tunes (which Cemini might consider for analyst specialization) get less of the benefit.
4. **Ant Group affiliation = potential vendor bias** — though the methodology is rigorous and the math doesn't depend on Ant-internal infrastructure.

### Cemini-side adoption assessment

**Decision: Read + cross-reference**, not Adopt-as-tooling. This is methodology that informs procurement and architectural reasoning, not deployable code. Concrete next-steps:

1. **Read methodology section** (§3-4) for the unified scaling law parameters in detail. ~45 min.
2. **Apply EL framework to DeepSeek-V4-flash vs alternatives** when next evaluating brain choice. The arithmetic is reproducible from the published EL formula.
3. **Track Ling-2.0 series** as a future Cemini brain candidate. Check `https://github.com/inclusionAI/Ling` (Ant Group's Ling-team org) every 60 days.

### Citation

> Tian, C., Chen, K., Liu, J., Liu, Z., Zhang, Z., & Zhou, J. (2025). *Towards Greater Leverage: Scaling Laws for Efficient Mixture-of-Experts Language Models*. arXiv:2507.17702 [cs.CL]. https://arxiv.org/abs/2507.17702 (ICLR 2026 Poster)

## Snippets

> **The Efficiency Leverage definition — the load-bearing concept**
>
> "We introduce Efficiency Leverage (EL), a metric quantifying the computational advantage of an MoE model over a dense equivalent. … An EL of 2 indicates the MoE model requires only half the computational cost to reach the same performance as the dense baseline." [Source: arXiv 2507.17702 §1, p.2]

> **The four governing principles**
>
> "1. Activation ratio as the primary driver of efficiency. … 2. Expert granularity as a non-linear modulator [optimum 8-12]. … 3. Amplifying effect of the compute budget [EL scales as a power law]. … 4. Secondary impact of other architectural factors." [Source: arXiv 2507.17702 §1 key insights, p.3]

> **The validation result — 7× efficiency demonstrated**
>
> "We predict that an MoE model with a 3.1% activation ratio and an expert granularity of 12 will achieve over 7x computational efficiency under a 1e22 FLOPs compute budget. … Ling-mini-beta, with 0.85B activated parameters and 17.5B total parameters … matched the performance of the 6.1B dense model while consuming over 7x fewer computational resources." [Source: arXiv 2507.17702 §1, p.3]
