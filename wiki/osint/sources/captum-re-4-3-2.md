---
title: "SHARPEN: Shapley-Guided Neural Repair Approach via Derivative-Free Optimization"
type: source
tags: [pdf, ml-methods, interpretability, shapley, cma-es, neural-repair, backdoor]
clusters: [options-derivatives, ml-methods]
related:
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @entities/components/kelly-cvar-risk-engine.md — risk engine covering options-derivatives and portfolio-strategy concepts

## Raw Concept

- **Original title**: SHARPEN: Shapley-Guided Neural Repair Approach via Derivative-Free Optimization
- **Author(s)**: Xinyu Sun, Wanwei Liu (corresponding), Haoang Chi, Tingyu Chen, Xiaoguang Mao, Shangwen Wang (NUDT); Lei Bu (Nanjing U); Jingyi Wang (Zhejiang U); Yang Tan, Zhenyi Qi (NUDT)
- **Type**: PDF (software engineering / ML security venue)
- **Location**: research for cemini/Captum re 4:3 2.pdf
- **Length**: 13p
- **Retrieved**: 2026-04-23
- **Read status**: read-skim
- **Primary cluster**: ml-methods (home is options-derivatives per partition — see flags, misclustered)
- **All clusters**: options-derivatives, ml-methods

## Narrative

SHARPEN is a neural network repair framework for fixing defects (backdoors, adversarial vulnerabilities, unfairness) in pre-trained DNNs without retraining. It has two stages:

(1) **Interpretable fault localization** via Deep SHAP-based hierarchical white-box analysis. Computes marginal contributions of each layer and neuron to erroneous outputs, ranks layers by aggregated impact, then locates faulty neurons/convolutional filters by comparing activation divergence between property-violating and benign states.

(2) **Derivative-free repair** via CMA-ES (Covariance Matrix Adaptation Evolution Strategy). Applied to the identified neurons, it performs gradient-free parameter search that captures variable dependencies via the covariance matrix. This sidesteps the standard limitation of gradient-based repair (which assumes specific activations like ReLU) and preserves interpretability of both the localization and repair steps — unlike pure search-based approaches.

Relevant to Cemini only indirectly. The partition assigned this as `options-derivatives` home cluster, almost certainly because "Captum" is in the filename — but the paper has nothing to do with options or derivatives. It is a neural-repair / ML-security paper. The connection to Cemini is thin: (a) SHAP-based fault localization is a pattern that could be applied to the MAPPO ensemble if interpretability for backdoor detection becomes relevant, (b) CMA-ES is explicitly cited as a gradient-free alternative to PPO in some related RL research — may be an option if the MAPPO training loop encounters pathological gradients. Honest limit: out of direct scope for the Cemini options/prediction-markets thesis.

## Key findings

- **FLAG: MISCLUSTERED** — partition-assigned home cluster `options-derivatives` is clearly wrong; the paper is about neural network repair, not derivatives.
- SHARPEN = Deep SHAP-based fault localization + CMA-ES-based derivative-free repair of targeted neurons.
- Gradient-free repair → applicable to non-ReLU activations (tanh, GELU, etc.) where gradient-based repair fails.
- Hierarchical coarse-to-fine localization: rank layers → locate faulty neurons/filters via activation divergence between property-violating and benign inputs.
- CMA-ES covariance matrix captures variable dependencies → coordinated parameter search across the identified faulty neurons.
- Addresses backdoors, adversarial attacks, unfairness without retraining the full network.
- Tangential relevance to Cemini: (1) if MAPPO interpretability requires SHAP over agents, (2) if CMA-ES is adopted for non-differentiable parts of the RL loop.

## Snippets

- **p.1 (abstract)** — "SHARPEN introduces a Deep SHAP-based white-box fault localization strategy that systematically quantifies the marginal contribution of each layer and neuron to erroneous outputs."
- **p.1 (abstract)** — "SHARPEN incorporates the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) to repair the identified neurons. CMA-ES leverages a covariance matrix to capture dependencies among variables, enabling gradient-free parameter search and coordinated [updates]."
- **p.1 (motivation)** — "most existing repair methods either rely on gradient calculations, restricting their applicability to networks with specific activation functions (e.g., ReLU), or use search algorithms whose localization and repair steps are often uninterpretable."
