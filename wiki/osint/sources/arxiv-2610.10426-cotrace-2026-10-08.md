---
title: "CoTrace: data recipes for training terminal agents (arXiv 2610.10426)"
type: source
tags: [source, k285, arxiv, agents, terminal, harness, rl, data]
keywords: [cotrace, terminal-agent, harness-model-co-evolution, dppo, provenance-matching, swe-bench, terminal-bench]
related:
  - concepts/k285-arxiv-wave.md
  - concepts/agent-harness-auditing-a2e.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-arxiv-wave.md
- @concepts/agent-harness-auditing-a2e.md

## Raw Concept

| Title | CoTrace: Data Recipes for Training Terminal Agents with Harness–Model Co-Evolution |
| Authors | Jixuan Chen, Jiaxin Zhang, Qinyuan Ye, Yada Pruksachatkun, Haoxiang Zhang et al. (UCSD; Salesforce AI Research; UW) |
| Type | arXiv preprint (cs.CL) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.10426-cotrace-data-recipes-for-training-terminal-agent.pdf` |
| Retrieved | 2026-10-08 |
| arXiv | 2610.10426v1 |
| read-status | read |

## Narrative

A **harness-aware data recipe** for terminal agents. The central claim: a trajectory's **training value depends on which harness produced it** — so pooling all search trajectories **disconnects policy training from the deployed runtime**.

### Method

Alternating **harness–model co-evolution** with component-wise promotion: each update is attributed to either the harness or the policy in isolation. CoTrace governs **trajectory routing**, **provenance matching** (harness fingerprint φ(H_{t+1})), **fresh top-up rollouts**, and **curriculum refresh**. SFT uses LoRA; RL uses **DPPO** (PPO-style, group-relative advantage, binary total-variation trust region).

### Results (Qwen3.5-9B, Tmax 102-task promotion split)

- **78 → 88** (CoTrace-SFT) → **90** (CoTrace-RL); mixed-siblings 86; harness-only 81.
- **30–50 trajectories/iteration** vs 149–308 for mixed siblings — cheaper *and* better.
- **OOD caveat:** on Terminal-Bench 2.1 and SWE-bench Lite the gains **largely vanish under a foreign runtime** (mini-swe-agent).

### Why it matters here

The **OOD caveat is the useful part**: a harness-tuned agent does not transfer to another harness. That is a direct caution for the wiki's `/route` and harness work — **the harness is part of the model**. Pairs with K285's Stacklok "separate the loop from execution" and K283's interpreter-over-tool-loop. **No code stated.** Route: CCC.

## Snippets

> "A trajectory's training value depends on which harness generated it; pooling all search trajectories can disconnect policy training from the deployed runtime." [Source: arxiv-2610.10426-cotrace-data-recipes-for-training-terminal-agent.pdf]

> "OOD: gains largely vanish under a foreign runtime (mini-swe-agent)." [Source: arxiv-2610.10426-cotrace-data-recipes-for-training-terminal-agent.pdf]
