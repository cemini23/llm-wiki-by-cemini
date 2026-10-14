---
title: Prompt framing governs LLM default following in collective-action settings (2026-10-05)
type: source
tags: [source, arxiv, agents, guardrails, llm, decision-making]
keywords: [default-deference, prompt-framing, common-pool-resource, public-good, choice-architecture]
related:
  - concepts/agentic-npc-design-guardrails.md
  - concepts/agent-harness-castle-project.md
  - concepts/minecraft-agent-harness-shelf.md
  - sources/arxiv-2609.35928-prompted-identity-factionalism-2026-09-30.md
  - sources/inbox-arxiv-reject-batch-2026-10-05.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.03253
maturity: validated
created: 2026-10-05
updated: 2026-10-05
---

## Raw Concept

**arXiv:2610.03253** — The paper studies **default deference** in LLM agents. A default is a value that is pre-selected unless the agent overrides it. The study asks whether the model treats a pre-filled default as merely informational, or as a suggestion that changes its choice. It uses two one-shot social dilemmas: a **common-pool resource (CPR) extraction game** and a **threshold public-good (TPG) contribution game**. Authors: Eladio Montero-Porras, Axel Abels, Tom Lenaerts (Université Libre de Bruxelles, Vrije Universiteit Brussel, FARI, ELLIS Alicante, UC Berkeley).

## Narrative

### Findings [CONFIRMED]

- Pre-filled defaults pull probability mass toward the default value in both games.
- The magnitude depends strongly on wording. The same model can show high pull under one formulation and near-zero pull under another.
- **Permission-style wording reduces default pull** in both games. The reduction is stronger in CPR than in TPG.
- Default pull is **weaker in coarse action spaces**.
- **Conflict defaults attract more mass than agreement defaults**.
- The authors conclude that default deference depends on the model, the wording of the interface, and the structure of available choices.

### Why this matters for agentic systems [CONFIRMED]

- The paper's own stated implication: for agentic systems, evaluating model behaviour without controlling the surrounding **choice architecture** misses an important source of behavioural variation.
- This is a warning about evaluation validity. A benchmark result measured without a default present may not predict behaviour when the interface supplies one.

### castle-sim / harness relevance [CONFIRMED]

- Maps to @concepts/agent-harness-castle-project.md and @concepts/agentic-npc-design-guardrails.md.
- First reading: for any in-game LLM advisor or lord, the UI default is a control surface. Pre-filling "raise taxes" pulls the model toward it. Where the design wants a neutral recommendation, use permission-style wording and do not pre-fill.
- Second reading: **coarse action spaces reduce default pull**. An agent given a small set of high-level verbs is less swayed by a pre-filled value than one given a fine-grained list. This supports the harness rule of named high-level operations.
- Cross-link @concepts/minecraft-agent-harness-shelf.md for the related tool-granularity finding, and @sources/arxiv-2609.35928-prompted-identity-factionalism-2026-09-30.md for another case where an incidental prompt detail changes cooperative behaviour.

### Caveat [TENTATIVE]

- The games are one-shot and deliberately abstract. The settings are social dilemmas, not a castle sim. The transfer is a design caution, not a measured effect in a game.

## Dead Ends

- Benchmarking an agent's choices without controlling the defaults present at decision time.
- Assuming a model's preference is stable across interface wordings.
