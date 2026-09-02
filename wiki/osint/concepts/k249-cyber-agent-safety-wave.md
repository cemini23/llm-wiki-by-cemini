---
title: K249 cyber agent safety wave (Aug 2026)
type: concept
tags: [cyber, llm-security, k249, agents, soc]
keywords: [rule-memory, CautiousBench, name-superstition, AI-ready-SOC, HARD]
related:
  - sources/arxiv-2608.26008-self-evolving-jailbreak-defense-2026-08-29.md
  - sources/arxiv-2608.27009-guard-that-cried-wolf-2026-08-29.md
  - sources/substack-rss-secpro-2026-08-28-249-ai-ready-soc.md
  - concepts/self-evolving-runtime-defense.md
  - concepts/intent-not-form-refusal.md
  - concepts/agent-runtime-identity-adr.md
maturity: draft
created: 2026-08-29
updated: 2026-08-29
wire_status: policy_wired
wire_target: cyber-k246-k253-phase1-wires.mdc
---

## Relations

- @sources/arxiv-2608.26008-self-evolving-jailbreak-defense-2026-08-29.md — black-box method-level rule memory
- @sources/arxiv-2608.27009-guard-that-cried-wolf-2026-08-29.md — CautiousBench name-superstition; NC-SA no clone
- @sources/substack-rss-secpro-2026-08-28-249-ai-ready-soc.md — six-layer AI SOC
- @concepts/self-evolving-runtime-defense.md — HARD sibling
- @concepts/intent-not-form-refusal.md — intent + authorization, not scary words
- @concepts/agent-runtime-identity-adr.md — agent identity + gather-not-decide

## Raw Concept

K249 cyber cluster — self-evolving jailbreak rule memory (2608.26008), over-safety name-superstition (2608.27009), SecPro #249 AI-SOC architecture.

## Narrative

Three complementary controls:

1. **Memory, not weights.** 2608.26008 stores wrapper-level refusal rules after a successful jailbreak. No fine-tune. Pair with HARD (K237): HARD evolves harness policy/gate; this paper evolves external memory. Do not unattended-evolve skills.
2. **Authorization, not names.** 2608.27009 shows execution-safety guards refuse authorized actions more when the object name looks scary. Gate on role/scope/consent/precondition/provenance. Atto: do not refuse an authorized stato-civile fetch because the register is named death.
3. **Layered SOC.** SecPro #249: data → knowledge (RAG) → intelligence (model routing) → agents-as-identities → action HITL → SAIF/NIST governance. Continue gather-not-decide.

**Phase-0:** 0 Integrate GO. No public CautiousBench repo (`gh search` 2026-08-29). Paper license CC BY-NC-SA 4.0 → **NO-GO clone**. 2608.26008 CC BY 4.0, no GitHub in PDF → no clone this wave.

**Forbidden:** jailbreak PoCs, CautiousBench corpus, LIVE Discord, prod SOC auto-contain.

## Snippets

> "wrapper-level rule memory + name-superstition over-refusal + six-layer AI SOC — policy only, no PoC." [Sources: 2608.26008, 2608.27009, SecPro #249]
