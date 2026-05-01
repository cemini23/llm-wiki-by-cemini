---
title: "When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models (ReaLM-Retrieve)"
type: source
tags: [RAG, reasoning-models, adaptive-retrieval, multi-hop-QA, uncertainty-quantification, chain-of-thought]
keywords: [ReaLM-Retrieve, retrieval-augmented generation, DeepSeek-R1, reasoning-step uncertainty, RSUS, IRCoT, multi-hop QA, SIGIR 2026]
clusters: [llm-agents]
related: []
maturity: validated
created: 2026-04-30
updated: 2026-04-30
---

## Relations
- Concept gap: no `@concepts/retrieval-augmented-generation.md` or `@concepts/reasoning-models.md` page exists (stubs needed)

## Raw Concept
- Original title: When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models
- Author(s): Dongxin Guo (HKU + Brain Investing Limited), Jikun Wu (Stellaris AI + Brain Investing Limited), Siu Ming Yiu (HKU + Brain Investing Limited)
- Type: PDF — conference paper (SIGIR 2026, Melbourne)
- Location: cemini-librarian:/opt/cemini-bulk/research/When to Retrieve During Reasoning- Adaptive Retrieval for Large Reasoning Models.pdf
- Retrieved: 2026-04-30
- Pages: 12p
- Read status: deep-read
- License: CC BY 4.0
- DOI: 10.1145/3805712.3809722

## Narrative

ReaLM-Retrieve addresses the temporal mismatch between standard RAG (retrieve once before generation) and large reasoning models (which need evidence injection during multi-step chains spanning 12K-25K tokens). Three innovations:

**1. Step-Level Uncertainty Detection (RSUS)** — Reasoning Step Uncertainty Score combines three signals: verbalized confidence (U_verb, via prompting or learned proxy for completion-only APIs), entity entropy (U_ent, corpus coverage of named entities via BM25), and consistency (U_cons, agreement across k=3 alternative continuations). RSUS identifies knowledge gaps at reasoning-step granularity — the logical inference unit, not token or sentence level. Computed with only 8% overhead vs 500-2000% for full semantic entropy. [Source: ReaLM-Retrieve.pdf pp.3-5]

**2. Learned Retrieval Intervention Policy** — Contextual bandit problem: state includes query, reasoning prefix, RSUS, retrieval history. Policy π_θ decides retrieve/don't-retrieve + query formulation. Trained via REINFORCE with reward = F1 − λ_1·n_ret − λ_2·t_latency. Curriculum learning: start with high retrieval penalty, gradually decrease. QueryGen formulates information-need queries (not reasoning-step queries). [Source: ReaLM-Retrieve.pdf p.5]

**3. Efficiency-Optimized Integration** — Segmented generation with context re-feeding (not single-pass mid-generation prompting). Implicit compression retains 27% of retrieved content while preserving 96% of relevant information. Speculative caching + KV-preservation. Per-retrieval overhead: 0.66s vs 2.10s naive (3.2× reduction). [Source: ReaLM-Retrieve.pdf pp.5-6]

**Experiments**: MuSiQue (2-4 hop), HotpotQA, 2WikiMultiHopQA. Models: DeepSeek-R1-Distill-Qwen-32B (ablation), DeepSeek-R1-671B (headline), QwQ-32B-Preview (generalization). Retrieval: ColBERTv2 + PLAID engine, k=5 passages.

Key results (Table 2, R1-32B): MuSiQue F1 71.2% (vs IRCoT 65.4%, Search-R1 66.8%), HotpotQA F1 71.8% (vs IRCoT 67.9%), 2WikiMHQA F1 69.7% (vs IRCoT 66.2%). Average retrieval calls: 1.8 vs IRCoT's 3.4-4.1 (47% reduction). R1-671B: MuSiQue F1 77.8%, HotpotQA 78.4%, 2WikiMHQA 76.5%. [Source: ReaLM-Retrieve.pdf pp.6-7]

Efficiency (Table 4): 14.1s E2E latency vs IRCoT's 18.7s (1.33× faster), 9,489 reasoning tokens vs 11,284 (16% reduction — well-timed retrieval resolves uncertainty that would require extended exploration). F1/Call: 39.6 vs IRCoT's 19.2 (2.1× efficiency). [Source: ReaLM-Retrieve.pdf p.7]

Ablation (Table 6): Largest single contributor is RSUS (random → -8.5% F1). Verbalized uncertainty contributes -2.8%, entity entropy -2.1%, consistency -0.9%. Learned threshold outperforms fixed threshold by 2.3% F1. [Source: ReaLM-Retrieve.pdf p.8]

Cross-model generalization (Table 8): QwQ-32B-Preview achieves +5.2% F1 over IRCoT with 47% fewer calls — policy depends on observable reasoning behavior, not model-specific internals. Cross-benchmark: HotpotQA-trained policy transfers to MuSiQue at 68.9% F1 (only 2.3% below in-domain). [Source: ReaLM-Retrieve.pdf pp.8-9]

Scaling with hops (Figure 2): Gains grow with reasoning complexity — +3.2% on 2-hop, +5.8% on 3-hop, +8.4% on 4-hop vs IRCoT. [Source: ReaLM-Retrieve.pdf p.8]

**Completion-only API support**: For o1-class endpoints that don't expose mid-generation prompting, a 2-layer MLP proxy (hidden dim 128) trained on surface features + SBERT embeddings substitutes for U_verb. Performance is 2-3% F1 lower than open-weight models (68.9% vs 71.2% on MuSiQue). This proxy architecture is directly relevant to API-only deployments like Cemini's DeepSeek-V4-flash. [Source: ReaLM-Retrieve.pdf p.4]

**Relevance to Cemini**: (1) DeepSeek-R1 is the primary test model — directly in Cemini's model family. (2) The completion-only API proxy pattern (learned uncertainty without token logprobs) maps exactly to Cemini's API-only constraint (DeepSeek-V4-flash via hosted API). (3) The adaptive retrieval policy (fewer, better-timed calls) is cost-relevant: each DeepSeek-R1-671B query costs $0.018-0.034 in output tokens. (4) Brain Investing Limited affiliation suggests finance-domain motivation. (5) The step-level granularity approach could generalize from multi-hop QA to multi-step financial analysis chains.

## Snippets

"Current RAG systems optimize for providing context before reasoning begins, while reasoning models require evidence injection during multi-step inference chains." [Source: ReaLM-Retrieve.pdf p.1]

"On MuSiQue, we achieve 71.2% F1 with 1.8 average retrieval calls compared to IRCoT's 65.4% F1 with 3.4 calls." [Source: ReaLM-Retrieve.pdf p.2]

"RSUS computation adds only 8% overhead to reasoning inference, compared to 500–2000% for full semantic entropy computation." [Source: ReaLM-Retrieve.pdf p.5]

"Per-retrieval overhead reduced by 3.2× compared to naive integration (from 2.1s to 0.66s per call)." [Source: ReaLM-Retrieve.pdf p.2]

"Policy depends on observable reasoning behavior rather than model-specific internals." [Source: ReaLM-Retrieve.pdf p.8, cross-model generalization result]
