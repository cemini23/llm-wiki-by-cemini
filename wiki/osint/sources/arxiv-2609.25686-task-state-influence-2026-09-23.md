---
title: "How Strongly Should Task State Influence an LLM Agent?"
type: source
tags: [arxiv, source, k270, agents, harness]
keywords: [k270, task-state, state-machine, enforcement-gate, PM-Bench]
related:
  - concepts/k270-harness-evolution-wave.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
read_status: skimmed
---

## Relations

- @concepts/k270-harness-evolution-wave.md

## Raw Concept

| Paper | arXiv:2609.25686 |
| File | `arxiv-2609.25686-how-strongly-should-task-state-influence-an-llm.pdf` |
| Location | `local inbox (archive blocked 2026-09-23): research to be indexed/arxiv-2609.25686-how-strongly-should-task-state-influence-an-llm.pdf` |
| Authors | Chenyu Zhang (University of Waterloo), Wonbin Kweon (Sungkyunkwan University), Jiawei Han (University of Illinois Urbana-Champaign) |
| Retrieved | 2026-09-23 |
| Pages | 43 |
| Dual-ID | **OSINT K270** |
| sha256 | `582244b09256873eb54d205683e803597f01c1294824cf3c2bb6f9152f74ebef` |

## Narrative

Long-horizon assigned work requires an agent to track task state: which steps are done, blocked, cancelled, or open to repetition. Agent systems either keep this state as text in the prompt, or move the state into a module that enforces it. Each system is evaluated as a whole, so no one knows how much reliability comes from the state being **shown, told, or enforced**.

The paper fixes the task rules, the model, and paired episodes. It varies only how strongly task state reaches the agent. Four rungs:

| Rung | How state reaches the agent |
|------|------------------------------|
| 1 | Raw transcript |
| 2 | Exact checklist |
| 3 | Per-turn directives from a state machine compiled from the brief, advanced only by execution receipts |
| 4 | Enforcement gate on that machine that refuses state-violating actions |

Every episode is scored by exact payload matching against dynamic ground truth. Across three models, two reasoning regimes, and two domains, four findings hold without per-turn reasoning:

1. Displaying accurate state is **unreliable**.
2. An unverified ledger the agent writes itself **beats** an accurate checklist it is shown.
3. Directives help in proportion to the model's **obedience**.
4. Enforcement needs no obedience, but is **bounded** by the correctness of its state and by the matcher that maps requests to steps.

Per-turn reasoning at a 235B agent compresses these separations. It does not repair the text rungs. The same gate, compiled from τ 2-bench's airline policy, raises a 235B agent's pass1 from **0.39 to 0.54**, and changes nothing for a 35B agent that rarely violates the policy. On PM-Bench, where acting turns on recognising a state, results differ.

**Cemini relevance:** agent-harness design pattern only. **FILE only. 0 product Integrate GO. Do not swap `/route`. Never auto-evolve `.cursor/skills`.**
