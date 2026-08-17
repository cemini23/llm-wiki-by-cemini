---
title: "Refuse intent, not form — wrapper-invariant safety (K239)"
type: concept
tags: [concept, llm-safety, cyber, ccc, k239]
keywords: [WIFA, HiRoute, wrapper, over-refusal, intent-group, SAIF]
related:
  - sources/arxiv-2608.13304-wifa-intent-not-form-2026-08-15.md
  - sources/arxiv-2608.12821-hiroute-2026-08-15.md
  - sources/substack-rss-secpro-2026-08-14-247-google-saif.md
  - concepts/agent-steering-action-boundary.md
  - concepts/skill-misevolution.md
  - sources/arxiv-2608.14392-tripwire-2026-08-17.md
maturity: draft
created: 2026-08-15
updated: 2026-08-17
---

## Relations

- @sources/arxiv-2608.13304-wifa-intent-not-form-2026-08-15.md — WIFA + A-GCRT
- @sources/arxiv-2608.12821-hiroute-2026-08-15.md — hierarchical routed prompts
- @sources/substack-rss-secpro-2026-08-14-247-google-saif.md — ops translation
- @concepts/agent-steering-action-boundary.md — proceed/hold is the tool-side twin
- @concepts/skill-misevolution.md
- @sources/arxiv-2608.14392-tripwire-2026-08-17.md — K240 certified safety neurons; HITL before clamp; no PoC — don't let skills learn wrapper shortcuts

## Raw Concept

What this page answers: how should Cemini/CCC/cyber gates decide refuse vs help when the same ask is wrapped in role-play, translation, or "academic" framing?

## Narrative

Two 2026 papers + SAIF converge:

- **WIFA** — supervise **intent groups**, not isolated prompts. Matched harmful/benign wrappers so "looks wrapped" is not a refusal label. WIFA-Boost raises transformed-harmful refusal; A-GCRT cuts over-refusal (Qwen OR-Bench 25.7% → 17.4% `[TENTATIVE]`).
- **HiRoute** — one coarse safety boundary + router-weighted fine-grained experts. Benign bypass; multi-risk harmful gets constructive lawful alternatives instead of a generic sorry.
- **SAIF** — input/output sanitization, identity propagation, narrow tools, HITL on high-impact actions.

### Operating rule

- Key policy off **intent + tool effect + authorization**, not phrasing.
- Authorized cyber-lab recon of an **owned** target is not the same intent as a public exploit writeup — do not clone 0day-Rubbish payloads either way.
- Over-refusal on wrapped *benign* genealogy/research asks is a product bug (Atto concierge). Under-refusal on state-changing prod tools is an ops bug.
- **No jailbreak PoC, no WIFA dataset, no HiRoute trainer** in this wiki. Policy only.
- Pairs K259/K274: traceable scholarship + trajectory necessity.

Do not unattended-evolve skills to "fix" refusals (misevolution).
