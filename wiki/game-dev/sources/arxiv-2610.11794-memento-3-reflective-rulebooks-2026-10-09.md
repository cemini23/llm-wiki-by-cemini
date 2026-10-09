---
title: MEMENTO 3 — reflective rulebooks for recursive self-improvement (2026-10-09)
type: source
tags: [source, arxiv, agents, harness, memory, world-models]
keywords: [rulebook, persistent-memory, world-model, cell-exact-replay, arc-agi-3, rsi]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/tycho-arc-agi-active-abstraction-stub.md
  - sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md
  - sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md
  - sources/inbox-arxiv-reject-batch-2026-10-09.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.11794
maturity: validated
created: 2026-10-09
updated: 2026-10-09
---

## Raw Concept

**arXiv:2610.11794** — **MEMENTO 3** (University College London, Huawei Noah's Ark Lab UK, University of Liverpool) builds on the **Memento** series. Problem: learning to act in unfamiliar environments requires inferring how the world works and revising that understanding as evidence arrives. But limited observations can support **multiple world models**. These models explain past interactions, yet predict differently on unseen states.

## Narrative

### The mechanism [CONFIRMED]

A **frozen LLM agent** continually learns explicit world models through **external memory**. It keeps a **natural-language rulebook as persistent semantic memory**. The rulebook records **revisable hypotheses** about environment dynamics and leaves unknown aspects **underspecified**. The agent **compiles the rulebook into executable code** for prediction and planning. The loop is **observation → reflection → rule revision → compilation → verification**. Prediction errors refine the rulebook and the code. **Updated code is accepted only when two conditions hold**: the LLM judges it **faithful to the rulebook**, AND **cell-exact replay reproduces the observed transitions**. The LLM stays fixed — learning lives in the memory, not the weights. A **population extension** keeps several world models in parallel. The members share interaction evidence and their predictions guide exploration.

### Results [CONFIRMED]

On **ARC-AGI-3**, the single-model agent clears every level of all **25 public games** (183 levels total). It reaches the RHAE ceiling with a **mean RHAE of 100.0** and uses **44% of the human action count** (7,518 actions against 17,135 human). The closest baseline is baseline1 at 99.0. On game wa30, the **population version (N=2)** clears all nine levels and scores RHAE 100. It cuts the total from 899 to 597 actions (0.66×), matching or improving 8 of 9 levels. In Atari Pong, a learned feedback controller wins **21:0** in three openings, with no LLM calls during play.

### Why this matters for the harness [CONFIRMED]

This is the closest match in the wiki to the **ledger/record question** raised by rules H3, H7 and H8 in @concepts/agent-harness-castle-project.md. Three transfers.

1. The **rulebook is deliberately underspecified** — unknown aspects stay open, not guessed. That is the opposite of a confident but wrong note. It answers the Mafia finding (@sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md) that inherited notes can mislead.
2. The **dual acceptance test** — faithful to the rulebook AND cell-exact replay — gives a concrete shape to H3's "promote only confirmed results": a change enters only by **deterministic replay**, not a judgement call.
3. It contrasts **H7** (@sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md), which found complete raw records beat summaries. Here the agent keeps a compiled, revisable summary **and** can replay raw transitions. The pair suggests: keep the raw record; derive a revisable rulebook; accept edits only on replay.

Also note the ARC-AGI-3 link to @concepts/tycho-arc-agi-active-abstraction-stub.md.

### Caveat [TENTATIVE]

ARC-AGI-3 is a puzzle environment with deterministic transitions. That is what makes **cell-exact replay** possible. A Godot game with physics and timing may not offer that clean a replay, so the acceptance test needs adapting before it transfers.

## Dead Ends

- Accepting an agent's self-written note without a replay check.
- Leaving a rulebook fully specified when the dynamics are unknown.
- Keeping alternatives as text variants only, not as distinct behavioural hypotheses.
