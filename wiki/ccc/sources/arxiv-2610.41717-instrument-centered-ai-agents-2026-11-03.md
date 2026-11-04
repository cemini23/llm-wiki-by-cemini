---
title: "Evaluating instrument-centred AI agents for table-top science"
type: source
tags: [source, arxiv, agents, evaluation, instrumentation]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Evaluating Instrument-Centered AI Agents for Table-Top Science Experiments |
| Authors | Jiaqi Cai, Siyu Cheng, William S. Huxter, Li-Qiao Xia, Shuwen Sun, and others (MIT, University of Washington, Boston College) |
| arXiv | 2610.41717 |
| Pages | 36 |
| Read status | skimmed (title page) |

## Narrative

The problem stated: evaluating agents for table-top science is hard because **live instruments are hard to reset and share at scale**. An experiment that takes an hour to set up cannot be run a thousand times to score a model.

The paper proposes an instrument-centred evaluation — the agent is judged on driving real laboratory hardware, with the availability constraint handled by the design rather than ignored.

**Relevance here is methodological, not practical.** This workspace does not drive lab instruments. But the constraint is the same one that makes agent evaluation hard everywhere: **the environment is expensive to reset**. That is why the workspace's own agent work is gated by hand-labelled sets built once and reused, rather than by repeated live runs.

**Caveat.** Only the title page was read. No benchmark, task count, or result is established here.

## Snippets

> "Reliable evaluation of AI agents for table-top science experiments has remained elusive because live instruments are hard to reset and share at scale…" [Source: arxiv-2610.41717 p.1]

## Dead Ends

- **Citing a result.** Title page only.
