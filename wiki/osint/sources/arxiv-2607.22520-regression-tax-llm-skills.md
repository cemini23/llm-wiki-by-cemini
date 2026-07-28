---
title: "The Regression Tax — why skills help and hurt LLM agents (arXiv 2607.22520)"
type: source
tags: [source, arxiv, agent-skills, harness, k196, ccc, atto]
keywords: [regression tax, agent skills, residual failure, office automation]
related:
  - concepts/skill-regression-tax.md
  - concepts/code-as-agent-harness.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/cemini-wiki-ingest-workflow.md
  - sources/arxiv-2607.22529-skill-self-play.md
maturity: draft
read_status: read
created: 2026-07-27
updated: 2026-07-27
clusters: [k196-ingest]
---

## Relations

- @concepts/skill-regression-tax.md
- @concepts/code-as-agent-harness.md
- @concepts/harness-updating-vs-benefit-nonmonotonic.md
- @concepts/cemini-wiki-ingest-workflow.md
- @sources/arxiv-2607.22529-skill-self-play.md — pair: co-evolve only behind regression gates

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `arxiv-2607.22520-the-regression-tax-decomposing-why-skills-help-a.pdf` |
| **sha256** | `576ca97fc29336b4b4c7374a55c53b5565592564552f2d45298d0863f2f2e278` |
| **arXiv** | [2607.22520](https://arxiv.org/abs/2607.22520) |
| **Repo** | https://github.com/sentient-agi/meta-skill-creator |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.22520-the-regression-tax-decomposing-why-skills-help-a.pdf` |

## Narrative

Across ~6k runs (2 office-automation benches × 3 harness stacks), skills create **regressions** (solved without skills, failed with) vs residual failures. Best skills win mainly by **regressing less**, not by unlocking more new solves. Average success hides the tax.

**Steal:** skill PRs / Cursor skills need before/after task matrices; Atto MCP allowlist and CCC harness skills should track regression suites, not only demo wins. Ties harness-updating non-monotonicity.

## Snippets

> "the best performing skills outperform others primarily by regressing less, not by gaining more"
