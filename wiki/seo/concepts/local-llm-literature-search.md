---
title: Local LLM literature search: what the hardware actually buys
type: concept
maturity: draft
related:
  - sources/arxiv-local-llm-paper-search-2611.17929.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: what do you get from running a paper-search assistant on a workstation instead of a hosted API?

From arXiv 2611.17929 (Inria Bordeaux), against a Mac Studio and a dual-A100 server.

## Narrative

Three separate things are being bought, and they cost differently.

**Confidentiality.** Unpublished manuscripts and experimental data stay on the premises. That is a governance argument, not a performance one.

**Latency shape.** Inference cost grows with input context from 512 to 128k tokens. A GPU server wins on raw throughput; unified memory on a Mac Studio wins on model size, because it can hold models the tested GPU pair could not.

**Retrieval quality.** Across eight models and 70 papers, success depends on the model and on how specific the query is. A better model does not rescue a vague query.

The design conclusion the authors reach is that the harness — context construction, memory, tools, verification — is a major determinant of behaviour, comparable in importance to the model. A lab that cannot train a frontier model can still improve the system around an open-weight one.

[TENTATIVE] One preprint's abstract. The per-model retrieval results and the latency curves were not read.

## Snippets

> "Local LLM alone does not produce an effective scientific agent."
