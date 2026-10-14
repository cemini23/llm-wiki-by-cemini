---
title: Prompted identity degrades multi-agent LLM cooperation (2026-09-30)
type: source
tags: [source, arxiv, agents, harness, multi-agent]
keywords: [factionalism, identity-labels, cooperation, token-overhead, mitigation]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/ai-assisted-game-dev-workflows.md
  - sources/arxiv-2609.37658-enterprisebench-strategic-agents-2026-09-30.md
  - sources/inbox-arxiv-reject-batch-2026-09-30.md
  - sources/arxiv-2610.01514-audit-rule-faithful-explanations-2026-10-03.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.35928
maturity: validated
created: 2026-09-30
updated: 2026-09-30
---

## Raw Concept

**arXiv:2609.35928** — Prompted identity degrades cooperation in multi-agent LLM systems. Multi-agent LLM systems increasingly mix models from several providers. The paper shows that exposing each agent's underlying model family to its peers significantly impairs cooperation. When agents know each other's model family, the group splits into clusters whose members prefer interacting with agents carrying the same label, even though nothing in the task rewards such a split. The authors call this factionalism and argue the label itself causes it.

## Narrative

### Measurement [CONFIRMED]

The authors use two cooperative games plus a reasoning benchmark, with nine to twenty-five agents drawn from up to five open-weight model families. When the announced families are shuffled, or replaced by arbitrary labels, the factions still follow the announced information. When the label is removed, the behaviour disappears. In strictly cooperative tasks, labelled groups spend on average 30% more rounds and 55% more tokens to reach a decision. The success rate drops from 96% to 81%. The effect replicates across tasks, group sizes, and model families. Withholding identity labels from agents is a simple and effective mitigation. Authors are at Sapienza University of Rome.

### castle-sim / harness relevance [CONFIRMED]

This affects the mixed-vendor agent swarm described in @concepts/agent-harness-castle-project.md, where the planner is one model and the executor swarm another. The actionable rule is to withhold model-family identity metadata from agent prompts when agents must cooperate. Flag the cost: 55% more tokens is a direct usage cost in a hobby, budgeted workflow. See also @concepts/ai-assisted-game-dev-workflows.md.

### Caveat [TENTATIVE]

The study uses open-weight model families in game-like cooperative tasks. Whether a coding swarm shows the same effect is untested.

## Dead Ends

- Putting "you are model X" labels in shared multi-agent context.
- Reading the result as a model-quality ranking.
