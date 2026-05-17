---
title: "MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination"
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

- **Original title**: MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination
- **Author(s)**: Zhuo Li, Yupeng Zhang, Pengyu Cheng, Jiajun Song, Mengyu Zhou, Hao Li, Shujie Hu, Yu Qin, Erchao Zhao, Xiaoxi Jiang, Guanjun Jiang (Qwen Large Model Application Team, Alibaba; CUHK-Shenzhen)
- **Type**: PDF
- **Location**: research for cemini/agents9.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 26p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

Hallucination is a critical bottleneck for LLM reliability, especially in Retrieval-Augmented Generation (RAG). Existing detection uses LLM-as-a-judge to verify outputs against retrieved evidence, but suffers **confirmation bias**: the verifier, exposed simultaneously to query, documents, and generated response, validates internal coherence rather than objective grounding, endorsing erroneous claims. The paper introduces **MARCH** (Multi-Agent Reinforced self-Check for Hallucination), which enforces factual alignment through deliberate information asymmetry.

MARCH orchestrates three specialized agents instantiated from the *same* base policy: a **Solver** generates a RAG response; a **Proposer** atomizes that response into discrete claim-level question-answer pairs; a **Checker** re-answers each question using *only* the retrieved documents, strictly blinded to the Solver's output. This asymmetry transforms verification from circular self-confirmation into rigorous cross-examination. The pipeline is trained end-to-end with multi-agent reinforcement learning (PPO) so the agents co-evolve. A **Zero-Tolerance Reward** assigns success only if *every* asserted claim matches the Checker's independent grounding (any single hallucinated claim invalidates the whole trajectory); multi-sampling with majority voting stabilizes the Checker's consensus answer.

MARCH substantially reduces hallucination rates without human annotation or external fact-checkers. Notably, an 8B-parameter LLM equipped with MARCH reaches performance parity with leading closed-source models on multiple hallucination benchmarks while also improving general RAG-QA.

For Cemini, MARCH is directly relevant to **librarian/RAG reliability**: the blinded-Checker information-asymmetry pattern is a concrete recipe for reducing context-conflicting hallucination when the wiki RAG layer serves quantitative trading research where misquoted figures are unacceptable.

## Snippets

> "We introduce Multi-Agent Reinforced self-Check for Hallucination (MARCH), a framework that enforces rigorous factual alignment by leveraging deliberate information asymmetry."
> [Source: agents9.pdf p.1]

> "In the RAG context, we posit that any single hallucinated claim within the response invalidates the entire reasoning chain. Therefore, a trajectory is assigned a successful score only if every claim asserted by the Solver achieves an identity match with the consensus answer extracted by the Checker."
> [Source: agents9.pdf p.4]

> "Notably, an 8B-parameter LLM equipped with MARCH achieves performance competitive with powerful closed-source models. MARCH paves a scalable path for factual self-improvement of LLMs through co-evolution."
> [Source: agents9.pdf p.1]
