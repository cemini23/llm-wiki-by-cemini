---
title: Learn2Play Bench — how well LLM agents learn from experience (2026-10-07)
type: source
tags: [source, arxiv, harness, agents, benchmark, memory]
keywords: [learn2play, experience-retention, text-games, counter-intuitive-rules, agent-memory]
related:
  - concepts/agent-harness-castle-project.md
  - sources/arxiv-2610.04672-masbench-partial-observability-2026-10-07.md
  - entities/tools/gamedevbench.md
  - sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md
  - sources/inbox-arxiv-reject-batch-2026-10-07.md
  - sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md
  - sources/arxiv-2610.11794-memento-3-reflective-rulebooks-2026-10-09.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.08215
maturity: validated
created: 2026-10-07
updated: 2026-10-07
---

## Raw Concept

**arXiv:2610.08215** — **Learn2Play Bench**, from the National University of Singapore. It is a benchmark of newly designed text-based games whose rules are novel or counter-intuitive. Agents must acquire knowledge through interaction, not rely on pretrained knowledge. [CONFIRMED]

Existing benchmarks mostly use tasks whose rules are given in the instructions or already familiar. This makes it hard to separate learning from interaction from reasoning with existing knowledge. [CONFIRMED]

The games give reproducible feedback and automatic scoring. The bench varies game instances to test whether agents apply what they learned to new situations. [CONFIRMED]

## Narrative

### Findings [CONFIRMED]

- **Experience retention** — retaining complete records of actions and feedback supports more effective learning than summarizing those experiences into rules or strategies.
- **Human–agent gap** — top human players reach higher peak scores than the evaluated agents, and humans explore more.
- **Harness matters** — with the backbone fixed, changing the harness can improve performance while reducing estimated inference cost.

The bench evaluates how backbone models, self-evolving methods, and agent harnesses each affect an agent's learning ability. [CONFIRMED]

### castle-sim / agent-harness relevance [CONFIRMED]

This is one of the strongest harness findings in the recent batch. **Complete records beat summaries** is directly actionable. It argues against compressing an executor's history into a tidy rule list before handing it to the next agent. Keep the raw action-and-feedback log retrievable. [CONFIRMED]

Compare rule **H3** in @concepts/agent-harness-castle-project.md (promote only confirmed results into a durable ledger). H3 governs what is *promoted*. This finding says the underlying raw record should still be kept. Cross-link @sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md (the record/ledger split) and @entities/tools/gamedevbench.md (the existing Godot agent bench).

### Caveat [TENTATIVE]

The games are text-based and purpose-built, not a 3D engine harness. The transfer is a design principle, not a measured effect on a Godot swarm.

## Dead Ends

- Summarizing an agent's history before it has learned from it.
- Assuming a strong backbone model implies strong learning from experience.
