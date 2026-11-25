---
title: "Evaluating Large Language Models for Scientific Paper Search (2611.17929)"
type: source
maturity: draft
related:
  - concepts/local-llm-literature-search.md
updated: 2026-11-16
read_status: read
---

## Raw Concept

- **Title:** Evaluating Large Language Models for Scientific Paper Search: Retrieval Success and Inference Latency on Mac Studio and NVIDIA A100
- **Authors:** Frederic Andriantseheno Rakoto, Yannis Bendi-Ouis, Xavier Hinaut (Mnemosyne, Inria Bordeaux)
- **Type:** arXiv preprint
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2611.17929-evaluating-large-language-models-for-scientific.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.17929
- **Read status:** full — 9 pages extracted 2026-11-16

## Narrative

Question: can open-weight models support web-assisted paper retrieval inside a lab, on hardware a lab actually owns?

Two measurements. First, inference latency as input context grows from 512 to 128k tokens on a Mac Studio and on a server with two A100s. Second, retrieval success for eight models on 70 papers from seven repositories, with queries at three levels of domain knowledge.

Findings: retrieval success depends strongly on the model and on query specificity. A100s are generally faster, but the Mac Studio's unified memory allowed models that could not fit the tested GPU configuration.

The paper's framing is the transferable part: a local model alone is not an agent. Behaviour depends on the harness — the layer that builds context, manages memory, exposes tools and verifies results. A lab cannot train a frontier model, but it can inspect and control the system around an open-weight one.

No SEO lane. Recorded here because it was dropped in the seo inbox; the content is local-inference cost and retrieval, not search-engine optimisation.

[Source: arxiv-2611.17929-evaluating-large-language-models-for-scientific.pdf]

## Snippets

> "retrieval success depends strongly on the selected model and the specificity of the query."

> "A100 GPUs are generally faster than the Mac Studio, but its unified memory allows larger models that could not be loaded in the tested GPU configuration."

## Dead Ends

- **Full-read note (2026-11-16):** Discussion and Conclusion: local LLM execution is a practical basis for web-assisted paper search **only while results remain subject to human verification**. [Source: arxiv-local-llm-paper-search-2611.17929.md full text, 9pp]
