---
title: "A-SAW: the agentic software architecture workflow (arXiv 2610.13647)"
type: source
tags: [source, k289, arxiv, agents, architecture, documentation, c4, hitl]
keywords: [a-saw, architecture-as-code, c4-model, typed-element-catalog, human-review-gate, author-variance, design-science]
related:
  - concepts/k289-arxiv-wave.md
  - concepts/agentic-code-quality-gates.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
read_status: read
---

## Relations

- @concepts/k289-arxiv-wave.md
- @concepts/agentic-code-quality-gates.md

## Raw Concept

| Title | A-SAW: The Agentic Software Architecture Workflow |
| Authors | Finn Klatt (Liechtenstein), Luca Di Grazia (St. Gallen), Johannes Schneider (Liechtenstein) |
| Type | arXiv preprint (cs.SE) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.13647-a-saw-the-agentic-software-architecture-workflow.pdf` |
| Retrieved | 2026-10-12 |
| arXiv | 2610.13647v1 |
| read-status | read |

## Narrative

Extends **Architecture as Code** with a **persistent IDE agent that drafts architecture documentation** — from a version-controlled **C4 model**, a **typed element catalog**, and instrumented templates — **behind a mandatory human review gate**.

**Note what it is and is not:** a **process-level artifact**, not a tool. The agent writes **design and documentation, not code**.

### The study

Industrial case study: rubric assessment of **45 documents** (13 matched source→regeneration pairs) plus **13 task-anchored practitioner interviews** (design-science method).

### Results

- **Between-author variance collapses: SD 19.2 → 3.8** (ratio 5.0, 95% CI [2.9, 9.2]).
- **Intrinsic quality +19 points median** across matched pairs (p = 0.001, r = +0.97).
- Agent documents: **completeness 100%, consistency 93%, machine-readability 99%, traceability 79%.**
- **11 of 13 participants rejected unreviewed agent output** — trust is **conditional**.

### Why it matters here

Two useful numbers: **documentation quality improves most where human authors varied most** (variance collapse), and **traceability is the weak axis (79%)**. The last line is the doctrine the wiki already holds — **an agent-drafted artifact ships behind a review gate, not instead of one**. Route: CCC. **No `/route` swap.**

## Snippets

> "Between-author variance collapses (SD 19.2 → 3.8)." [Source: arxiv-2610.13647-a-saw-the-agentic-software-architecture-workflow.pdf]

> "11/13 participants rejected unreviewed agent output; trust described as conditional." [Source: arxiv-2610.13647-a-saw-the-agentic-software-architecture-workflow.pdf]
