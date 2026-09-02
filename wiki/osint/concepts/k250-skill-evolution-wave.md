---
title: K250 skill evolution wave (Aug 2026)
type: concept
tags: [skills, agents, k250, ccc]
keywords: [WikiSkill, skill-evolution, validation-ratchet, misevolution]
related:
  - sources/arxiv-2608.27454-wikiskill-2026-08-29.md
  - sources/arxiv-2509.25140-reasoning-bank-2026-08-29.md
  - concepts/k250-harness-intelligence-wave.md
  - concepts/skill-misevolution.md
  - entities/tools/reasoning-bank.md
maturity: draft
created: 2026-08-29
updated: 2026-08-29
wire_status: policy_wired
wire_target: ccc-k246-k253-phase1-wires.mdc
---

## Relations

- @sources/arxiv-2608.27454-wikiskill-2026-08-29.md — Google WikiSkill wiki+skill co-evolution
- @sources/arxiv-2509.25140-reasoning-bank-2026-08-29.md — reasoning-memory sibling
- @concepts/k250-harness-intelligence-wave.md — harness cluster
- @concepts/skill-misevolution.md — HITL gates; no unattended skill auto-evolve
- @entities/tools/reasoning-bank.md — ReasoningBank REFERENCE entity

## Raw Concept

K250 skill-evolution cluster — WikiSkill persistent wiki layer + ReasoningBank reasoning memory. Both compile agent experience into durable artifacts beyond single-run optimization.

## Narrative

WikiSkill (Google Research) co-evolves **executable skills** with a **persistent wiki** (Raw → Wiki → Skill layers). A Wiki Maintainer consolidates traces; a Skill Proposer reads wiki+traces; gating/rollback accepts skill patches only when validation improves — rejected patches remain as wiki evidence (pairs **K324 validation ratchet**, **K237 skill misevolution**).

ReasoningBank provides complementary **reasoning-strategy** memory rather than procedural skills. Together they argue experience must be **compiled and gated**, not scattered across optimization histories. **No public WikiSkill repo** at Phase-0 — policy pattern only. Never unattended `.cursor/skills` promotion.
