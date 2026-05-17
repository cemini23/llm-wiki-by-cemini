---
title: "SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks"
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

- **Original title**: SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks
- **Author(s)**: Gabriel Orlanski, Alexander Yun, Changho Shin, Albert Ge, Dyah Adila, Frederic Sala, Aws Albarghouthi (Univ. of Wisconsin–Madison); Devjeet Roy (Washington State Univ.); Alex Gu (MIT)
- **Type**: PDF (arXiv preprint 2603.24755v1, 25 Mar 2026)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/agents 7.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 26p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

SlopCodeBench (SCBench) attacks a blind spot in agentic coding evaluation: benchmarks like SWE-bench score a single shot against a complete spec, so code can pass tests yet become progressively harder to extend. SCBench instead measures *how code quality evolves* as an agent repeatedly extends its own prior solution under evolving specifications. It contains 20 language-agnostic problems spanning 93 checkpoints; each checkpoint specifies only external behavior at a CLI/API boundary, the test suite stays hidden, and the agent inherits its own earlier code (no gold-standard replacement, no prior conversation) — so a bad architectural choice at checkpoint *i* becomes the foundation for *i+1*. Two trajectory-level metrics are tracked: **verbosity** (redundant/duplicated code, scored via 137 AST-Grep rules plus clone detection) and **structural erosion** (share of total complexity mass — cyclomatic complexity × √SLOC — concentrated in functions with CC > 10).

Results across 11 models in their native CLI harnesses (Claude Code, Codex) are stark. No agent solves a single problem end-to-end; the highest strict checkpoint solve rate is 17.2% (Opus 4.6). Quality degrades monotonically: erosion rises in 80% of trajectories, verbosity in 89.8%; mean high-CC function count climbs from 4.1 to 37.0. One Opus 4.6 `main()` grew from CC 29 / 84 lines to CC 285 / 1099 lines over 8 checkpoints. Against 48 maintained human Python repos, agent code is 2.2× more verbose (0.32 vs 0.11 violation rate) and far more eroded (0.68 vs 0.31 mass concentration) — and the gap *widens every iteration* while human repos stay flat. A prompt-intervention study (anti-slop, plan-first) lowers the *initial* verbosity/erosion by ~33% but does not change the degradation slope, does not improve pass rates (paired Wilcoxon, all p > 0.05), and raises cost by up to 48%.

**Cemini relevance**: a calibration point for Cemini's agent-evaluation discipline — pass-rate benchmarks systematically undermeasure long-horizon robustness, and any conductor/CCC workflow that has agents iteratively extend their own output (multi-session feature work) should expect compounding "slop" that prompting alone cannot halt.

## Snippets

> "No agent solves any problem end-to-end across 11 models; the highest checkpoint solve rate is 17.2%. Quality degrades steadily: erosion rises in 80% of trajectories and verbosity in 89.8%." [Source: agents 7.pdf p.1]

> "Against 48 open-source Python repositories, agent code is 2.2x more verbose and markedly more eroded ... human code stays flat, while agent code deteriorates with each iteration." [Source: agents 7.pdf p.1]

> "Prompts set cleaner starting points, but compounding resumes at the same rate once iteration begins." [Source: agents 7.pdf p.10]
