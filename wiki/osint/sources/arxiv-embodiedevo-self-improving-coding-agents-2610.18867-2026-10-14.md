---
title: "EmbodiedEvo — Self-improving Coding Agents for Physical Intelligence"
type: source
tags: [arxiv, agent, coding-agent, skill-evolution, harness]
keywords: [coding agent, Skills and Lessons, experience reuse, RoboDojo, harness freeze, execution cost]
related:
  - concepts/k291-osint-wave.md
  - concepts/agent-skill-rl-extraction.md
  - concepts/agent-skills-procedural-anchoring.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-osint-wave.md — K291 osint wave hub
- @concepts/agent-skill-rl-extraction.md — extracting reusable skills from agent experience
- @concepts/agent-skills-procedural-anchoring.md — skills as procedural memory

## Raw Concept

Title: EmbodiedEvo — Self-improving Coding Agents for Physical Intelligence
Authors: Wenyi Li et al. (Navers Lab, Einsia.AI; Tsinghua University)
Type: arXiv preprint (2610.18867)
Location: `research to be indexed/osint/arxiv-2610.18867-embodiedevo-self-improving-coding-agents-for-phy.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The framing worth keeping:** code is not only a policy representation, it is **the workspace in which the agent solves the task**. Rather than following a prescribed plan→execute→verify workflow, the agent inspects state, revises and runs code, and lets feedback pick the next step — the SWE loop, extended to physical tasks.

**EmbodiedEvo** evolves reusable **Skills and Lessons** from feedback on a **single** Playground scene, then **freezes the harness** for new scenes.

### Results

| Metric | Value |
|---|---|
| RoboDojo-Sim average score | 44.48 |
| RoboDojo-Sim success rate | 37.82% |
| vs official verified results | surpasses all |
| Largest gains | memory-dependent tasks |
| Weak spot | fine contact control |
| Cost vs raw interaction history | **53.0% lower execution cost at comparable performance** |

**Cross-model transfer:** experience harvested from a stronger model improves weaker executors — Astra's experience raised Sol and Luna by **+8.86** and **+5.50** points.

### Why it is filed here

The **53% cost reduction at comparable performance** is the headline for this wiki's agent-harness lane: the same task performance from distilled Skills and Lessons rather than raw history. That is a context-budget result, not a capability result.

**No install, no wire.**

## Snippets

> "Code can serve not only as a policy representation but also as the workspace in which the agent solves a task." [Source: arxiv-2610.18867 p.1]

> "Compared with raw interaction history, Skills and Lessons achieve comparable task performance at 53.0% lower execution cost." [Source: arxiv-2610.18867 p.1]

> "Experience from stronger models also improves weaker executors: Astra's experience raises Sol and Luna's success rates by 8.86 and 5.50 percentage points over no experience." [Source: arxiv-2610.18867 p.1]

## Dead Ends

- Reading the 53% cost figure as a capability gain. Task performance is *comparable*, not higher; the gain is in execution cost.
- Assuming the harness transfers unchanged. EmbodiedEvo **freezes** its harness per Playground scene before applying it to new ones.
