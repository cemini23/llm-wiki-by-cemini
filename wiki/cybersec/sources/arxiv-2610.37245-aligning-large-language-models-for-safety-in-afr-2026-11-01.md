---
title: "Hausa Safety Alignment for Large Language Models"
type: source
tags: [source, arxiv, llm-safety, hausa, preference-alignment]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Aligning Large Language Models for Safety in African Languages: A Case Study of Hausa |
| Authors | Valdini Douglace Lemofouet et al., African Institute for Mathematical Sciences (AIMS), Cameroon |
| arXiv | 2610.37245 |
| File | `arxiv-2610.37245-aligning-large-language-models-for-safety-in-afr.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.37245 |
| Read status | skimmed (abstract + intro) |

## Narrative

Safety alignment research for large language models stays concentrated on high-resource languages. The authors study how current alignment methods behave for Hausa. The abstract states that more than 200 million people speak Hausa across West Africa. The introduction states that over 200 million people speak Hausa, primarily in Northern Nigeria, Niger, and Ghana. Both speaker figures come from this paper alone.

The authors introduce HausaSafeLM. They call it one of the first Hausa safety preference datasets. The paper states that the set contains 10,000 prompts derived from PKU-SafeRLHF. It states that 3,000 examples are human-corrected gold data and 7,000 examples are machine-translated silver data. The prompts span six harm macro-categories. These counts come from this paper alone.

The authors align Qwen2.5-7B-Instruct. They compare supervised fine-tuning (SFT) with SFT followed by Direct Preference Optimization (DPO). They run both methods on the gold data and on the silver data. Evaluation uses 500 harmful Hausa prompts and 200 benign Hausa prompts. These evaluation sizes come from this paper alone.

The paper reports that the untuned base model appears highly safe when the metric is refusal rate. The authors attribute that score to limited Hausa generation ability. They state that the refusals are almost uniformly low quality. SFT improves refusal fluency and refusal precision. SFT benefits substantially from the larger, noisier silver-tier data. DPO sharpens refusal precision. DPO also imposes a steep cost on linguistic quality, and that cost stays largely the same across the two data regimes. The authors state that no single configuration jointly maximizes safety, helpfulness, and fluency.

The authors conclude that current alignment techniques teach a model when to refuse more readily than how to refuse fluently in an underrepresented language. They state that refusal rate alone is an unreliable signal of safety in a low-resource setting. For a defensive security and AI-safety reader, the claim matters because a high refusal rate can mask weak generation in the target language. The introduction also reports prior results in which a harmful prompt translated into a low-resource language bypasses safety filters trained mainly on English, and in which code-switching or a synthetic language can drop safety constraints without adversarial fine-tuning.

## Snippets

> "We find that the untuned base model appears highly safe by refusal-rate metrics alone, but this reflects limited Hausa generation ability rather than genuine alignment: its refusals are almost uniformly low quality. SFT improves both refusal fluency and precision and benefits substantially from the larger, noisier silver-tier data, while DPO sharpens refusal precision but comes at a steep, largely data-invariant cost to linguistic quality." [Source: `arxiv-2610.37245-aligning-large-language-models-for-safety-in-afr.pdf` p.1 (arXiv 2610.37245), retrieved 2026-11-01]
