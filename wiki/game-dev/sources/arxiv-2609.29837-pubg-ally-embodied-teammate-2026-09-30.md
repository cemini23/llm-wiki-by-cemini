---
title: PUBG Ally — conversational embodied AI teammate (2026-09-30)
type: source
tags: [source, arxiv, npc, runtime, guardrails, llm]
keywords: [pubg-ally, embodied-teammate, on-device, memory-redaction, latency]
related:
  - concepts/llm-npc-runtime-ai-shelf.md
  - concepts/agentic-npc-design-guardrails.md
  - sources/krafton-pubg-ally-nvidia-ace-2026-06-25.md
  - sources/inbox-arxiv-reject-batch-2026-09-30.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.29837
maturity: validated
created: 2026-09-30
updated: 2026-09-30
---

## Raw Concept

**arXiv:2609.29837** — **PUBG Ally**. A voice-enabled AI teammate for PUBG: BATTLEGROUNDS. Ally reasons, acts autonomously, and plays alongside players. This is the full research paper behind the industry news already shelved in @sources/krafton-pubg-ally-nvidia-ace-2026-06-25.md.

Architecture [CONFIRMED]: an LLM agent uses a controlled tool interface. It inspects game information, interprets player speech, maintains context, decides what to say, and issues high-level action choices. Those choices steer a faster control layer for time-sensitive movement, combat, and recovery. Speech and action must stay synchronised under strict latency limits.

Data and evaluation [CONFIRMED]: the team collected data across nearly 39k sessions of real players playing alongside Ally. They recorded gameplay, player speech, agent decisions, tool use, actions, and player feedback. Evaluation uses player feedback and preference comparisons. The team found gaps between offline evaluation and real player preference, and refined the criteria iteratively.

Deployment [CONFIRMED]: on-device low-latency execution, model compression, context compaction, targeted safety training, runtime guardrails, and memory redaction. Players in 141 countries were surveyed. Among confirmed-in-record respondents, positive responses exceeded negative.

## Narrative

### castle-sim relevance [CONFIRMED]

- Shipped reference for the guardrail stack in @concepts/agentic-npc-design-guardrails.md. Note memory redaction, runtime guardrails, context compaction, and the split between a slow LLM decision layer and a fast control layer.
- Latency budget: a synchronous voice teammate needs a faster layer than the LLM. The LLM stays out of the tick loop.

### Indie gap [CONFIRMED]

- The stack is AAA/UE scale with proprietary infra. The useful steal is the guardrail and evaluation shape, not the system.
- castle-sim v0 has no LLM NPCs.

## Dead Ends

- Shipping a cloud LLM voice teammate in a hobby Godot RTS.
- Copying the eval loop without real player telemetry.
