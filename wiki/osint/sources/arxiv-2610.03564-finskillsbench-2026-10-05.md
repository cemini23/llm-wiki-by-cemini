---
title: "Knowledge or Calculator? — decomposing the skill premium in financial agent workflows"
type: source
tags: [arxiv, agents, finance, evaluation]
keywords: [2610.03564, finskillsbench, agent-skills, financial-agents, silent-competence]
related:
  - concepts/k282-agent-eval-wave.md
maturity: draft
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- @concepts/k282-agent-eval-wave.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Knowledge or Calculator? Decomposing the Skill Premium in Verifiable Financial Agent Workflows |
| Authors | Jermyn Zhen Yong Bek (Independent), Zhuang Qiang Bok (Deep Insight Labs), Zhongtian Sun (University of Kent; University of Cambridge) |
| Type | arXiv paper |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.03564-knowledge-or-calculator-decomposing-the-skill-pr.pdf` |
| Retrieved | 2026-10-05 |
| arXiv | 2610.03564 |
| read-status | read |

## Narrative

The paper introduces FinSkillBench, a controlled benchmark for financial agent
workflows. It holds 2,603 point-in-time episodes across 12 subtasks in portfolio
construction, risk management, and fundamental analysis. Ground truth is hidden
and regenerable, with deterministic verifiers. The intervention is skill
availability: no-skill, curated (human-authored skills and tools), self-generated,
docs-only, and tools-only.

Across 17,820 episodes, 9 models, and 3 resource conditions, curated skill
packages raise mean scores by +16.2 points (0.366 to 0.528). Self-generated skills
add only +0.5 points, while using more tokens and turns. The premium decomposes:
documents alone add +5.6 points, executable tools alone add +19.5 points, and the
combination is subadditive. The source of the gain is workflow-dependent: tools
dominate numeric workflows, documents matter when taxonomy or schema guidance is the
bottleneck. A second harness (Hermes) reproduces the direction, with magnitudes that
depend on how tools and data are exposed. A composed nine-stage mandate-delivery
probe finds "silent competence": running on its own handoffs, the agent delivers a
near-optimal book (optimality 0.934) that is never mandate-adherent (0 of 33), while
every per-stage control reports success.

For this workspace: this is central to the financial agent workflow domain and to
the workspace's own agent-skill tooling. It shows that curated skills are mostly a
tool-execution effect, not a knowledge effect. The "silent competence" failure is a
direct warning for multi-stage financial pipelines and for CeminiSuite-style
mandate workflows.

[Source: arXiv:2610.03564]

## Snippets

> "curated skill packages raise mean scores by +16.2 points (0.366 to 0.528), whereas skills generated within a single episode add only +0.5 points while consuming more tokens and turns."
[Source: arxiv-2610.03564-knowledge-or-calculator-decomposing-the-skill-pr.pdf p.1]

> "documents alone add +5.6 points, tools alone add +19.5 points, and their combination is subadditive."
[Source: arxiv-2610.03564-knowledge-or-calculator-decomposing-the-skill-pr.pdf p.1]

> "an agent running on its own handoffs delivers a near-optimal but never mandate-adherent book (optimality 0.934, adherence 0/33) while every per-stage control reports success."
[Source: arxiv-2610.03564-knowledge-or-calculator-decomposing-the-skill-pr.pdf p.1]

> "The breach surfaces only at the terminal gate, which is scored against the immutable canonical mandate rather than the agent's own parse."
[Source: arxiv-2610.03564-knowledge-or-calculator-decomposing-the-skill-pr.pdf p.8]

> "a measured 'skill premium' is a property of the full model, resource, and harness system rather than of the underlying model alone."
[Source: arxiv-2610.03564-knowledge-or-calculator-decomposing-the-skill-pr.pdf p.1]
