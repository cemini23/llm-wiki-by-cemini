---
title: "Agentic Harness Engineering Beta — requirement-centered harness evolution"
type: source
related:
  - concepts/requirement-centered-harness-evolution.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/failed-trajectory-harness-repair.md
  - entities/tools/claude-code.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent Harnesses |
| Author | Jiahang Lin, Jiahao Chen, Yiding Wang et al. (Fudan, PKU, RUC) |
| Type | arXiv paper (cs.SE), 2611.24924 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.24924-agentic-harness-engineering-beta-requirement-cen.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 47 |
| Read status | read |

## Narrative

AHE-Beta treats harness evolution as a requirement-management loop, not a score-chasing loop. The authors argue that single-agent evolution plus benchmark selection produces narrow patches and benchmark-specific local optima.

The loop has three steps:

1. **User-driven evaluation** — 50 simulated personas (read, competent, expert) work with the harness over multi-turn sessions in a Gitea repository. They raise requirements as issues and rate the process, not the completion.
2. **Team-based modification** — Triage, Architect, PM and Developer roles turn admitted requirements into generalizable changes. A PRD is produced, then ordered tasks, then a PR.
3. **Requirement-driven selection** — a change merges only when it resolves a verified requirement and passes review. No verifier runs during evolution; benchmark scores are computed only afterwards.

Reported results: pass@1 rises from 21.9% to 33.3% on held-out tasks, with 40.8% fewer tokens than the base harness. The authors report a higher pass@1 than Claude Code, Meta-Harness and AHE. A blind human A/B test prefers AHE-Beta in 31 of 48 valid pairs and rates it higher on all five dimensions. Gains transfer without further evolution to GLM-5.3 (+15.8%) and DeepSeek-V4.1-Flash (+5.3%). [TENTATIVE] single source; all numbers are author-reported.

The transfer result is the one that matters for Cemini. A harness evolved against requirement evidence, not against the benchmark, still helps on another model. This is the same discipline `/route` needs: merge a harness change when it fixes a stated requirement, and measure the benchmark after the fact.

## Snippets

> "Requirement-driven selection merges a change only when it resolves a verified requirement and passes review." [Source: arxiv-2611.24924-agentic-harness-engineering-beta-requirement-cen.pdf p.1]

> "Without further evolution, the gains transfer to GLM-5.3 and DeepSeek-V4.1-Flash with pass@1 improvements of 15.8% and 5.3% over Base Harness." [Source: arxiv-2611.24924-agentic-harness-engineering-beta-requirement-cen.pdf p.1]
