---
title: "arXiv:2605.30621 — Harness updating is not harness benefit"
type: source
tags: [source, arxiv, agent-harness, llm-agents, k93]
keywords: [2605.30621, harness-self-evolution, harness-updating, harness-benefit, mid-tier-agents]
related:
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - sources/arxiv-continual-harness-self-improving-agents-2605.09998.md
  - concepts/cemini-wiki-ingest-workflow.md
maturity: validated
read_status: read
created: 2026-06-01
updated: 2026-06-01
clusters: [agent-harness, papers]
---

## Relations

- @concepts/harness-updating-vs-benefit-nonmonotonic.md
- @sources/arxiv-continual-harness-self-improving-agents-2605.09998.md — prior harness evolution paper (K72)
- @concepts/cemini-wiki-ingest-workflow.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents |
| Authors | Lin, Wu, Wang, et al. (Penn State, UCSC, Amazon, Emory, UIUC, Northeastern) |
| arXiv | 2605.30621 |
| Location | `research to be indexed/2605.30621v1.pdf` → librarian bulk |
| Retrieved | 2026-06-01 |
| Read | read (abstract + findings) |

## Narrative

Defines **harness self-evolution** as updating external harness artifacts (prompts, skills, memories, tools) without weight changes. Disentangles two capabilities:

1. **Harness-updating** — quality of edits from execution evidence.
2. **Harness-benefit** — task performance after edits are applied.

**Finding 1:** harness-updating is **flat in base model capability** — even small models' updates yield gains comparable to frontier evolvers. **Finding 2:** harness-benefit is **non-monotonic** — weak models gain little; mid-tier gain most; strong tier gains less than mid-tier (activation + instruction-following failure modes at weak tier).

**Cemini implication:** invest capability budget in the **task-solving agent** more than a separate "evolver" model; train/practice harness **invocation** and long-horizon instruction following. Complements K72 continual-harness paper — both argue harness layer is first-class, not a side effect of base LM scale.

## Snippets

> "Harness-updating is flat in base capability… even Qwen3.5-9B's updates yield gains comparable to those of Claude Opus 4.6." [Source: 2605.30621v1.pdf abstract]

> "Harness-benefit is non-monotonic… mid-tier models benefit most." [Source: 2605.30621v1.pdf abstract]
