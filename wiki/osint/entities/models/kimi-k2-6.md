---
title: Kimi K2.6 — auxiliary-routing LLM (cost-optimized assistant tier)
type: entity
tags: [entity, llm, kimi, moonshot, auxiliary-routing, cost-optimized, cemini-eval]
keywords: [kimi k2.6, moonshot, auxiliary llm, cost routing, agent orchestra]
related:
  - sources/x-kimi-k2.6-hermes-routing-playbook-2026-05.md
  - sources/x-kirillk-kimi-agent-swarm-guide-2026-05-24.md
  - entities/tools/kimi-agent-swarm.md
  - concepts/kimi-agent-swarm-vs-claude-agent-teams.md
  - concepts/agent-cost-routing-model-orchestra.md
maturity: draft
created: 2026-05-12
updated: 2026-05-24
---

## Relations

- `@sources/x-kimi-k2.6-hermes-routing-playbook-2026-05.md` — origin playbook (auxiliary-routing pattern)
- `@concepts/agent-cost-routing-model-orchestra.md` — host concept (multi-model cost cascade)
- `@sources/x-kirillk-kimi-agent-swarm-guide-2026-05-24.md` — K65: K2.6 as **Agent Swarm coordinator** (decompose / synthesize)
- `@entities/tools/kimi-agent-swarm.md` — product using K2.6 at up to 300 sub-agents [vendor claim]

## Raw Concept

What prompted this page: K40 ingest of the X-post playbook describing a model orchestra that fans Opus-grade prompts down to Kimi K2.6 / Hermes-4 for the cheap-but-good auxiliary tier. K65 adds Moonshot **Agent Swarm** coordinator role.

## Narrative

Kimi K2.6 (Moonshot AI) — auxiliary-tier LLM in @concepts/agent-cost-routing-model-orchestra.md (cheap fan-out, scope-lock) **and** coordinator for @entities/tools/kimi-agent-swarm.md (mass parallel sub-agents + merge). Same model, different products: routing playbook vs vendor swarm UI.

See @concepts/kimi-agent-swarm-vs-claude-agent-teams.md for Anthropic Agent Teams contrast. Cemini does not host K2.6 on prod silicon — reference only.
