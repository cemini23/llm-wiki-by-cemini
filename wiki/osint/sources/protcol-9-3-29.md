---
title: Efficient Benchmarking of AI Agents (Ndzomga, 2026)
type: source
tags: [pdf, llm-agents, agent-evaluation, benchmarking, k49]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — LLM-agents corpus index — efficient AI-agent benchmarking methodology

## Raw Concept

- **Original title**: Efficient Benchmarking of AI Agents
- **Author(s)**: Franck Ndzomga (ndzomgafs@gmail.com)
- **Type**: PDF — arXiv preprint 2603.23749v1, cs.AI, 24 March 2026
- **Location**: research for cemini/protcol 9 3:29.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 22p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

**Problem.** Comprehensive AI-agent benchmarks are expensive: each evaluation needs full interactive rollouts with tool use and multi-step reasoning. The Holistic Agent Leaderboard cost roughly $40,000 for nine benchmarks despite only one run per scaffold–model pairing. This blocks independent researchers and small labs from statistically robust evaluation. The paper asks whether small task subsets can preserve agent *rankings* at much lower cost.

**Method.** Unlike static LM benchmarks, agent evaluation suffers **scaffold-driven distribution shift** — performance depends on the harness wrapping the model (tool use, memory, retry logic, execution flow), not just the model. Across 8 benchmarks, 33 agent scaffolds, and 70+ model configurations, the author measures how well a reduced task set predicts absolute scores (R²) versus rank order (Spearman ρ) under temporal, scaffold, and random shift, using nested cross-validation.

**Key findings.** A robust asymmetry emerges: absolute-score prediction degrades sharply under scaffold/temporal shift (R² gap ≈ 0.38), but **rank-order prediction stays stable**. Exploiting this, the paper proposes the **Mid-Range Difficulty Filter (MR)** — an optimization-free rule keeping only tasks with 30–70% historical pass rates, motivated by Item Response Theory (tasks near 50% pass rate carry the most discriminative signal about latent agent ability). MR cuts evaluation tasks by **44–70%** while keeping high rank fidelity, beats high-variance random sampling, and outperforms greedy selection under shift. Reliable leaderboard ranking therefore does not require full-benchmark evaluation.

**Cemini relevance.** Directly informs eval discipline: when ranking CeminiSuite agent scaffolds or model swaps, a deterministic mid-difficulty task filter gives reliable comparative ranking at a fraction of the rollout cost, and the scaffold-shift warning cautions against trusting absolute scores across harness changes.

## Snippets

> "Across eight benchmarks, 33 agent scaffolds, and 70+ model configurations, we find that absolute score prediction degrades under this shift, while rank-order prediction remains stable." [Source: protcol 9 3:29.pdf p.1]

> "This mid-range difficulty filter, motivated by Item Response Theory, reduces the number of evaluation tasks by 44–70% while maintaining high rank fidelity under scaffold and temporal shifts." [Source: protcol 9 3:29.pdf p.1]

> "The Holistic Agent Leaderboard (Kapoor et al., 2026)—one of the most comprehensive standardized evaluation efforts for AI agents—required roughly $40,000 to evaluate agents on nine benchmarks, despite considering at most two scaffolds per benchmark and only one run per scaffold–model configuration." [Source: protcol 9 3:29.pdf p.1]
