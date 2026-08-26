---
title: "TrustDABench — LLM structured data analysis reliability (arXiv 2608.24145)"
type: source
tags: [arxiv, eval, k247, tabular]
keywords: [TrustDABench, structured-data, evidence-path, reliability, robustness]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/k247-agent-harness-wave.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
read_status: read
---

## Relations

- @concepts/wiki-tooling-evaluation.md — tabular K241 eval vocabulary; evidence-path refuse/clarify
- @concepts/k247-agent-harness-wave.md — diagnostic benchmark for agent tabular claims

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.24145, "TrustDABench: Benchmarking Reliability and Robustness of LLMs for Structured Data Analysis" |
| Authors | Boshen Shi, Yize Liu, Chen Zhao, Ce Chi, Zhendong Wang, Xing Wang, Junlan Feng |
| Retrieved | 2026-08-26 |
| File | `arxiv-2608.24145-trustdabench-benchmarking-reliability-and-robust.pdf` |
| sha256 | `14868741a096f8ce5194ebe78e1550a69e00d56bd2f6e6e7e247ff6e5b5bf9e5` |
| Dual-ID | **OSINT K247**. Wiki eval vocabulary; no runtime wire. |

## Narrative

Trustworthy spreadsheet/CSV analysis requires a valid path from user question to data evidence — not just a correct-looking answer. TrustDABench operationalizes **reliability** (refuse or clarify when no evidence path exists) and **robustness** (preserve correct analysis when the same evidence appears in different table forms).

The benchmark derives 19 perturbation operators via an Agentic-LLM generation framework and contains 2,340 human-verified perturbed instances. Use as eval vocabulary when auditing agent tabular claims in OSINT briefs — prefer solvers/tools over single-pass LLM table paste (pairs tabular K241).

## Snippets

> "A trustworthy result should be supported by a valid path from the user question to the relevant data evidence." [Source: arxiv-2608.24145-trustdabench-benchmarking-reliability-and-robust.pdf abstract]
