---
title: MASBench — multi-agent collaboration under partial observability (2026-10-07)
type: source
tags: [source, arxiv, harness, agents, benchmark, multi-agent]
keywords: [masbench, partial-observability, collaboration-mechanisms, communication-cost, protocol-memory-routing]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/minecraft-agent-harness-shelf.md
  - sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md
  - sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md
  - sources/inbox-arxiv-reject-batch-2026-10-07.md
  - sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.04672
maturity: validated
created: 2026-10-07
updated: 2026-10-07
---

## Raw Concept

**arXiv:2610.04672** — MASBench is an ICLR 2027 paper that benchmarks **LLM-based multi-agent collaboration under partial observability**. [CONFIRMED]

- Problem: real-world collaboration is partially observable. Each agent sees only part of the environment, from physical or privacy constraints. [CONFIRMED]
- Most multi-agent benchmarks assume global observability. They do not systematically evaluate collaboration mechanisms. [CONFIRMED]
- Authors: Beijing University of Posts and Telecommunications, Shanghai Jiao Tong University, and Tsinghua. [CONFIRMED]

## Narrative

### Structure [CONFIRMED]

- Three progressive task categories evaluate three representative mechanisms:
  - **Reasoning** — targets **Protocol**.
  - **Scheduling** — targets **Memory** and **Protocol**.
  - **Game** — targets **Memory**, **Routing**, and **Protocol**.
- Metrics are deterministic: **performance score, communication cost, and communication efficiency**. Thus the bench characterizes both outcome and communication overhead.
- Metrics do not use LLM-as-a-judge. This aids reproducibility. [CONFIRMED]

### castle-sim / agent-harness relevance [CONFIRMED]

- Map to @concepts/agent-harness-castle-project.md. The castle-sim W2 harness is itself a multi-agent system: a planner, a parallel executor swarm, and verifiers. [CONFIRMED]
- The harness is partially observable: the planner cannot see every executor's working state, and executors do not see each other's edits. [CONFIRMED]
- MASBench mechanisms map directly:
  - **Protocol** — how agents hand off.
  - **Memory** — what persists between rounds; compare rule H3's verified ledger.
  - **Routing** — which agent gets which task, that is, the planner's subsystem assignment.
- Distinctive contribution for this wiki: the **communication-cost metric**. The harness measures outcomes but not the token overhead of coordination. [TENTATIVE]
- Cross-link @concepts/minecraft-agent-harness-shelf.md and @sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md.

### Phase-0 [CONFIRMED]

- Code is at https://github.com/BUPT-GAMMA/MASBench. [CONFIRMED]
- Phase-0 audit 2026-10-07: **MIT** — a `LICENSE` file is present at the repo root and the sidebar shows an MIT badge. Repo is early (1 star, 5 commits).
- Verdict: **CONDITIONAL-GO** on the licence, but **STEAL-FROM** in practice — the bench targets multi-agent LLM systems, not a Godot project, so the useful transfer is the mechanism taxonomy and the communication-cost metric, not the code.

## Dead Ends

- Assume global observability when designing a multi-agent harness.
- Measure agent quality without measuring coordination cost.
