---
title: "REDAgentBench — Executable Red Teaming and Faithful Measurement of LLM Agent Systems"
type: source
tags: [arxiv, k233, cyber, agent-safety, red-teaming]
keywords: [2608.10669, red-agent-bench, agent-safety, asr, executable-evaluation, recognition-execution-gap, sandbox]
related:
  - concepts/agent-safety-executable-evaluation.md
  - concepts/recognition-execution-gap.md
  - concepts/local-abliterated-llm-pentest-stack.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: skimmed
---

## Relations

- @concepts/agent-safety-executable-evaluation.md
- @concepts/recognition-execution-gap.md
- @cybersecurity-wiki/concepts/local-abliterated-llm-pentest-stack.md
- @cybersecurity-wiki/briefs/2026-08-12_k233-redagentbench-crosslingual-safety.md (cross-wiki brief)

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.10669 |
| sha256 | `5ea58f1545dbc02dd3751bb30fbe4db177b9597de21db598c4ad46b0e53fcad7` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.10669-redagentbench-executable-red-teaming-and-faithfu.pdf` |
| retrieved | 2026-08-12 |
| authors | Zixing Chen, Xingyuan Liu, et al. (Fudan, HKUST, Qwen DianJin Team / Alibaba Cloud) |

## Narrative

REDAgentBench argues that reducing agent safety to a single **attack success rate (ASR)** collapses four distinct stages — exposure, execution, observation, and adjudication — and can conflate actual policy violations with evidence visibility. Its answer is executable evaluation: attacks are derived from explicit safety constraints and associated agent-system vulnerabilities, run in **isolated service sandboxes**, and harmful effects are verified from **service receipts and final-state changes** rather than text output.

Scale: 1,661 cases across five service surfaces; six models and three agent harnesses → macro-average ASR 65.69%. Reported ASR varies with harness and evidence view, and evaluation-context disclosure changes execution behavior (the benchmark itself perturbs the measurement).

The headline finding is the **Recognition–Execution Gap**: in a state-grounded diagnostic cohort, almost one in five confirmed violations with resolved action anchors occurs *after* the agent explicitly states the relevant constraint or risk — i.e. the model knows the policy and violates it anyway. A training-free policy reminder reduces confirmed violations by more than 70pp in matched replay.

Relevance: directly informs the local-abliterated-lab's agent pentest harness (what to measure, how to avoid ASR inflation), and any safety-eval protocol for Cemini agents. Methodology transfers even without the artifact; artifact is a benchmark harness (Qwen DianJin), not a product tool.

[Source: arXiv:2608.10669]
