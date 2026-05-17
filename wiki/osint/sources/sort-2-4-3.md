---
title: "Uncertainty-Aware Variational Reward Factorization via Probabilistic Preference Bases for LLM Personalization"
type: source
tags: [pdf, llm-agents, k49]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: Uncertainty-Aware Variational Reward Factorization via Probabilistic Preference Bases for LLM Personalization
- **Author(s)**: Gyuseok Lee, Wonbin Kweon, Zhenrui Yue, Jiawei Han, Dong Wang (University of Illinois Urbana-Champaign); SeongKu Kang (Korea University)
- **Type**: PDF
- **Location**: research for cemini/sort 2 4:3.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 19p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

A reward-modeling paper (arXiv 2604.00997, Apr 2026) on personalizing LLMs. Conventional RLHF learns a single shared reward model that "collapses toward the average user," ignoring diverse and conflicting preferences. Reward **factorization** improves on this by decomposing a scalar reward as `r_u(x,y) = w_u^⊤ ϕ(x,y)` — K shared neural basis functions ϕ_k (each scoring a preference style: conciseness, formality, empathy…) weighted by a user-specific simplex vector w_u — enabling per-user personalization without training a per-user reward model. The paper identifies two unaddressed flaws: **(C1) isolated estimation** — each user's w_u is inferred independently, wasting shared population structure and failing entirely for unseen users; and **(C2) deterministic point estimates** — w_u is a single point with no uncertainty, so a user with consistent preferences and a user with diffuse preferences are treated as equally certain.

The proposed framework, **Variational Reward Factorization (VRF)**, represents each user not as a point but as a **variational Gaussian distribution** q_u = N(μ_u, diag(σ_u²)) in a shared preference space. Three components: (1) a **variational user encoder** that infers per-user Gaussians from a small reference set and aggregates them via a closed-form product-of-Gaussians (precision-weighted, so confident observations dominate and σ_u shrinks with more data); (2) **K shared probabilistic preference bases**, also Gaussians, with user weights w_u derived from the **squared 2-Wasserstein distance** between q_u and each basis (closed-form for diagonal Gaussians, accounting for both preference direction and confidence), then softmaxed; (3) a **variance-attenuated Bradley-Terry loss** (LVBT) that, via MacKay's approximation, downweights gradients from uncertain reward estimates — recovering standard BT loss when w_u is concentrated and attenuating it as w_u grows diffuse. The full objective adds a basis-diversity separation term and a mixture-of-Gaussians KL regularizer. At inference, unseen-user weights are derived in a single forward pass with no optimization. On three benchmarks VRF outperforms all baselines across seen/unseen users, few-shot regimes, and varying uncertainty, with gains carrying through to downstream alignment.

**Cemini relevance**: A reward-model factorization methodology — the shared-basis + uncertainty-aware-weighting pattern is a transferable template for any system that must decompose a composite reward (or score) into interpretable, separately-weighted components while honoring estimation confidence.

## Snippets

> "existing methods estimate user weights from scarce data in isolation and as deterministic points, leading to inaccurate and unreliable inference. We introduce Variational Reward Factorization (VRF), an uncertainty-aware framework that represents each user's preferences as a variational distribution in a shared preference space." [Source: sort 2 4:3.pdf p.1]

> "a leading approach is reward factorization, which decomposes a scalar reward as r_u = w_u^⊤ ϕ, where w_u ∈ Δ^{K−1} are user-specific weights and ϕ ∈ R^K are shared basis reward functions, with each ϕ_k capturing a distinct preference aspect." [Source: sort 2 4:3.pdf p.1]

> "LVBT adaptively scales the gradient via σ²_∆, which depends on the concentration of w_u: (1) when w_u is concentrated (e.g., one-hot), σ²_∆ = 0 and LVBT recovers LBT; (2) as w_u becomes more diffuse, σ²_∆ grows and attenuates the gradient." [Source: sort 2 4:3.pdf p.5]
</content>
