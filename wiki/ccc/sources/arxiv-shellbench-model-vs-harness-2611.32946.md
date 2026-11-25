---
title: "ShellBench — what matters more for everyday agent tasks, model or harness (2611.32946)"
type: source
related:
  - concepts/model-vs-harness-performance-variance.md
  - concepts/agent-harness-operational-definition.md
  - entities/skills/route.md
  - sources/arxiv-2610.32483-when-agents-fail-model-or-harness-who-s-to-blame-2026-10-27.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ShellBench: What Matters More for AI Agents, Models, or Harness for Everyday Tasks |
| Author | Vincent Koc et al. (OpenClaw Foundation, Parsewave, Hugging Face, Paradigm, UC Berkeley, Columbia, Red Hat, NVIDIA) |
| Type | arXiv preprint (cs.AI) |
| ID | 2611.32946v1, 24 Nov 2026 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.32946-shellbench-what-matters-more-for-ai-agents-model.pdfarxiv-2611.32946-shellbench-what-matters-more-for-ai-agents-model.pdf
| Retrieved | 2026-11-25 |
| File | `arxiv-2611.32946-shellbench-what-matters-more-for-ai-agents-model.pdf` |
| Pages | 17 |
| Read status | read (abstract, intro, task design) |

## Narrative

ShellBench measures everyday tasks, not coding tasks. The authors built 100 tasks from 10,456,576 anonymized user queries. They embedded the queries, clustered them with K-means, and kept the largest coherent clusters. Developers then built realistic workspaces with messy files and competing sources. Workspaces hold files, email, calendars, spreadsheets, saved pages, chat logs, receipts, PDFs, and simulated apps. Some hold phishing emails and stale data.

The design crosses 12 models, 5 harnesses, and 3 reasoning levels. Total rollouts: 53,100. Each task is graded for correctness and safety. 90 tasks are judge-graded and 10 are code-tested.

Main results:

- **Model choice matters more than harness choice.** But the top three models differ by only 1.1 points.
- GPT-6 Astra leads at 62.5% overall. GPT-6.1 Sol reaches 61.4% at about one-sixth of Astra's estimated token cost per attempt.
- Harness means sit in a tight band: OpenClaw 45.23, Pi 45.22, Hermes 45.11, Codex 45.04, Claude Code 42.87. Pass@1 ranges 42.9 to 45.2.
- Harness effect is small on average but large for some model pairs. DeepSeek V4.1 Flash scores 43.8 in Claude Code and 34.1 in Codex. Claude Fable 5.2 scores 65.3 in Hermes and 60.0 in OpenClaw.
- Harness choice had little effect on safety.

**Why it matters.** This is a direct test of the "harness, not model" thesis for general tasks. For everyday household work, the harness shifts a score by a few points. It does not move 40 points. That contrasts with coding benchmarks, where harness differences are large.

Caveats. The authors built the benchmark and the OpenClaw harness. The top harness by mean is OpenClaw, their own. The query dataset is private and cannot be released. Results come from one paper. [TENTATIVE]

## Snippets

> "We find that model choice impacts performance more than harness choice, but the three leading models differ by only 1.1 percentage points." [Source: `arxiv-2611.32946-shellbench-what-matters-more-for-ai-agents-model.pdf` p.1, retrieved 2026-11-25]

> "Harness mean (11 models): 45.23 OpenClaw, 45.22 Pi, 45.11 Hermes, 45.04 Codex, 42.87 Claude Code." [Source: `arxiv-2611.32946-shellbench-what-matters-more-for-ai-agents-model.pdf` p.1 Table 1, retrieved 2026-11-25]
