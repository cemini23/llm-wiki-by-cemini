---
title: "Continual Harness — online self-improving foundation agents (arXiv:2605.09998)"
type: source
tags: [source, arxiv, agent-harness, embodied-agents, self-improvement, rl]
keywords: [continual-harness, gemini-plays-pokemon, online-prompt-optimization, process-reward, reset-free-harness]
related:
  - concepts/continual-harness-online-self-improvement.md
  - concepts/code-as-agent-harness.md
  - concepts/llm-agent-systems.md
  - sources/arxiv-code-as-agent-harness-survey-2605.18747.md
  - sources/agentic-harness-engineering.md
maturity: validated
read_status: deep-read
created: 2026-05-27
updated: 2026-05-27
clusters: [llm-agents, rl-marl]
---

## Relations

- @concepts/continual-harness-online-self-improvement.md — synthesized concept
- @concepts/code-as-agent-harness.md — coding harnesses are the motivating contrast; Continual Harness targets embodied long-horizon POMDPs
- @concepts/llm-agent-systems.md — parent cluster
- @sources/arxiv-code-as-agent-harness-survey-2605.18747.md — static harness survey (May 2026)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Continual Harness: Online Adaptation for Self-Improving Foundation Agents |
| Authors | Seth Karten, Joel Zhang, Tersoo Upaa Jr, Ruirong Feng, Wenzhe Li, Chengshuai Shi, Chi Jin (Princeton); Joel Zhang (ARISE); Kiran Vodrahalli (Google DeepMind) |
| arXiv | [2605.09998](https://arxiv.org/abs/2605.09998) (v1, 11 May 2026) |
| Pages | 28 |
| Location | `research to be indexed/2605.09998v1.pdf` → `cemini-librarian:/opt/cemini-bulk/research/2605.09998v1.pdf` |
| Read | 2026-05-27, deep-read (abstract + intro + results framing) |

## Narrative

Princeton / DeepMind work on **reset-free harness self-improvement** for embodied agents (Pokémon Red/Emerald), motivated by the gap between mature **coding harnesses** (Claude Code, OpenHands, OpenClaw) and absent equivalents for long-horizon partial-observability control.

**Gemini Plays Pokémon (GPP)** — with human-in-the-loop harness refinement, frontier models completed Pokémon Blue, Yellow (hard mode), and Crystal without a lost battle; in hardest stages the agent iterated strategy via long-context memory (emergent self-improvement signal).

**Continual Harness** formalizes and automates that loop: starting from a **minimal environment interface only**, the agent alternates acting and refining its own prompt, sub-agents, skills, and memory using **any past trajectory** — unlike prompt-optimization methods that require episode resets. Reported gains: substantially lower button-press cost vs minimalist baseline on Red/Emerald; recovers majority of gap to hand-engineered expert harness despite no curated tools or domain scaffolding.

**Co-learning extension:** online process-reward loop — open-source agent rollouts relabeled by frontier teacher → weight updates → sustained milestone progress on Red **without environment reset between training iterations**.

**Cemini relevance:** not a trading paper — maps to **harness evolution** for conductor / server-Claude / multi-step research agents (online refinement from trajectories, not batch prompt-tuning). Distinct from Cemini's code-as-harness + MCP stack but informs **self-improving operator loops** and reviewer/refiner automation. See @ccc-wiki/concepts/continual-harness-online-self-improvement.md for workflow posts routed from K72 Posts batch.

## Snippets

> "Coding harnesses such as Claude Code and OpenHands wrap foundation models with tools, memory, and planning, but no equivalent exists for embodied agents' long-horizon partial-observability decision-making." [Source: 2605.09998v1.pdf p.1]

> "Continual Harness removes the human fully from this loop: a reset-free self-improving harness for embodied agents." [Source: 2605.09998v1.pdf p.1]
