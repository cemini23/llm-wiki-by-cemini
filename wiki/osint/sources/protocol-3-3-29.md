---
title: "Rethinking Failure Attribution in Multi-Agent Systems: A Multi-Perspective Benchmark and Evaluation"
type: source
tags: [pdf, llm-agents, multi-agent-systems, failure-attribution, benchmark, evaluation, k49]
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

- **Original title**: Rethinking Failure Attribution in Multi-Agent Systems: A Multi-Perspective Benchmark and Evaluation (arXiv:2603.25001)
- **Author(s)**: Yeonjun In, Sangwu Park, Wonjoong Kim, Chanyoung Park (KAIST); Sungchul Kim, Md Mehrab Tanjim, Uttaran Bhattacharya, Somdeb Sarkhel, Jayakumar Subramanian (Adobe Research)
- **Type**: PDF (arXiv preprint)
- **Location**: research for cemini/protocol 3 3:29.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 14p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

**Problem.** Failure attribution — finding the failure-inducing step in a multi-agent system (MAS) execution trace — is essential for debugging, but every prior benchmark (Who&When, TracerTraj, Aegis, MAST) assumes a single *deterministic* root cause per failure. The authors argue this is wrong: because MAS admit many valid execution trajectories, a failed run genuinely has *multiple plausible attributions* depending on the observer's notion of a "correct" trajectory. Empirically, expert annotators disagree on the failure step in up to ~60% of cases.

**Method.** They propose **multi-perspective failure attribution** — predict a *set* of failure-inducing steps each with explicit rationale — and build **MP-Bench**, the first benchmark for it: 289 execution logs (169 hand-crafted via MagenticOne, 120 automated via CaptainAgent; tasks from GAIA and AssistantBench), each triple-annotated by rigorously screened Upwork experts (~346 expert-hours total). Annotations are consolidated into a consensus-rate ranking; evaluation uses **nDCG@K** for ranking alignment plus an LLM-as-judge for reasoning quality.

**Key results.** Only **16.2%** of failure steps have unanimous (3/3) consensus; 56.1% are flagged by just one annotator — confirming the multi-perspective thesis. Critically, when LLMs are sampled multiple times (N=3) at temperature τ=1, they recover diverse, human-aligned attributions far above random — **contradicting prior claims (e.g. Who&When) that LLMs perform near-randomly at failure attribution**. The limitation was the deterministic benchmark, not model capability. Claude-Sonnet-4.5 is the strongest single model; temperature τ=0 hurts (constrains output diversity); **multi-LLM ensembles across model families consistently beat single-model setups** because cross-family disagreement supplies genuinely complementary perspectives.

**Cemini relevance.** Directly applicable to debugging the conductor/librarian's multi-agent query pipeline: when a multi-step retrieval fails, attributing the fault is non-deterministic. The practical guidance — sample at τ>0, ensemble across model families, aggregate N runs — is a concrete recipe for any Cemini MAS diagnosis or self-evaluation loop.

## Snippets

> "In practice, the failure-inducing step of a MAS failure is often not deterministic and admits multiple plausible attributions ... even expert annotators exhibits perspective differences on the failure-inducing step in up to about 60% of cases."
> [Source: protocol 3 3:29.pdf p.1]

> "only 16.2% of steps are annotated as failure-inducing by all three annotators ... a substantial 56.1% are labeled as failures by only a single annotator."
> [Source: protocol 3 3:29.pdf p.6]

> "the limitations of LLMs in failure attribution observed in existing works stem not from insufficient model capability, but from biased evaluation assumptions that overlook the inherently multi-perspective nature of MAS failures."
> [Source: protocol 3 3:29.pdf p.2]
