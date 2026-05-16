---
title: Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning
type: source
tags: [pdf, rl-marl, multi-agent, llm-debate, reasoning, evaluation]
keywords: [multi-agent debate, MAD, logical reasoning, Knight-Knave-Spy, agent heterogeneity, majority pressure, controlled study, collective reasoning]
related:
  - concepts/rl-marl-research.md
  - concepts/multi-agent-trading.md
  - concepts/recursive-multi-agent-systems.md
  - concepts/regime-conditioned-evaluation.md
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus
- @concepts/multi-agent-trading.md — debate is a core coordination pattern for LLM agent teams; this paper stress-tests when it actually works
- @concepts/recursive-multi-agent-systems.md — multi-agent reasoning systems; debate is one inter-agent collaboration topology
- @concepts/regime-conditioned-evaluation.md — shares the controlled-evaluation / disentangle-the-factors methodology Cemini applies to strategy evidence

## Raw Concept

- **Original title**: Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning
- **Author(s)**: Haolun Wu (McGill / Mila), Zhenkun Li, Lingyao Li (University of South Florida) — arXiv:2511.07784v1, 11 Nov 2025
- **Type**: PDF
- **Location**: research for cemini/Controlled Study of Multi-Agent Debate in Logical Reasoning.pdf
- **Retrieved**: 2026-04-27
- **Length**: 20p
- **Read status**: deep-read
- **Cluster**: rl-marl

## Narrative

The paper interrogates whether multi-agent debate (MAD) among LLMs produces *genuine* deliberative reasoning or merely the statistical effect of ensembling and majority voting. To get a clean answer the authors build a controlled testbed on the Knight–Knave–Spy logic puzzle: a deductive task with unambiguous ground truth, stepwise structure, and tunable difficulty. The dataset spans puzzle sizes 4–9 players (1,800 puzzles total). Their MAD framework runs an initial-proposal phase, a player-by-player debate loop (debate sub-phase + self-adjustment sub-phase), and a final majority-vote decision with a supervisor agent breaking ties.

Two research questions are addressed. RQ1 (outcome) varies six controllable factors against a default anchor — agent team size, team composition (homogeneous vs heterogeneous), confidence visibility, debate order, debate depth, and task difficulty. RQ2 (process) defines three desiderata for effective debate (inclusive deliberation, rationale over assertion, advancement of understanding) and measures whether agents actually exhibit them.

Key findings: debate reliably improves accuracy within a task (e.g. +52% instance accuracy on size-4 puzzles), but **the ceiling is bounded by the strongest participant** — intrinsic model reasoning strength and group diversity are the dominant drivers. Structural knobs (order, confidence visibility, extra depth) offer negligible gain; regression shows initial accuracy (β=0.600) and agent count are the strongest predictors, while task difficulty hurts. Process analysis reveals majority pressure suppresses independent correction (weak models correct an incorrect majority in only ~3.6% of cases), a "minority correction asymmetry" (agents defend correct minority views more readily than they fix incorrect ones), and that rare majority-reversal transitions contribute most to final accuracy. Rational, validity-aligned reasoning predicts correction success far better than rhetorical confidence.

Relevance for Cemini: directly applicable to the conductor / multi-agent orchestration layer and any debate-style trading-agent ensemble. The core lesson — coordination mechanisms cannot rescue weak base reasoners, and homogeneous agent pools risk echo-chamber consensus — argues for genuine model heterogeneity in agent teams and for treating "the debate improved accuracy" claims with the same controlled-study skepticism Cemini applies to strategy backtests.

## Snippets

> "Our results show that intrinsic reasoning strength and group diversity are the dominant drivers of debate success, while structural parameters such as order or confidence visibility offer limited gains." [Source: Controlled Study of Multi-Agent Debate in Logical Reasoning.pdf p.1]

> "Overall, performance remains bounded by the strongest reasoner available, and while diversity provides modest gains, it cannot make up for a team composed entirely of weak agents." [Source: Controlled Study of Multi-Agent Debate in Logical Reasoning.pdf p.7]

> "When an agent starts within a correct majority (MaC), its position is exceptionally stable, with all models achieving over 97% correction rates. However, facing an incorrect majority (MaW) exposes a clear performance gap. ... weaker models are almost entirely swayed by the group, with gemini-2.5-flash-lite (mix_A) correcting itself in only 3.6% of such cases." [Source: Controlled Study of Multi-Agent Debate in Logical Reasoning.pdf p.9]
