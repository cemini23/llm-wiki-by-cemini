---
title: Intent-governed tool authorization (IGAC)
type: concept
tags: [concept, agent-security, authorization, mcp, least-privilege, igac]
keywords: [igac, intent certificate, manifest filtering, openport, session narrowing, 2606.22916]
related:
  - concepts/nomos-compiled-policy-enforcement.md
  - sources/arxiv-2610-11030-nomos-compiled-policy-tool-gate.md
  - concepts/cross-service-agent-compositional-harm.md
  - sources/arxiv-2610-13886-x-agentred-cross-service-redteam.md
  - sources/arxiv-2606-22916-intent-governed-tool-authorization-igac.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/chaincaps.md
  - entities/tools/airguard.md
  - sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md
  - sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md
  - concepts/mcp-execution-control-invariants.md
  - entities/tools/handle-capability-protocol.md
  - sources/arxiv-2607-03510-cage-1-enterprise-agent-governance.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/task-conditioned-excess-authority.md
  - concepts/intent-contract-planner-tool-separation.md
  - sources/arxiv-intent-contracts-tools-away-2611.24025.md
  - concepts/aws-abac-authorization-traps.md
maturity: draft
created: 2026-06-24
updated: 2026-11-22
wire_status: wont_wire
wire_target: "REFERENCE — IGAC artifact pending"
---

## Relations

- @concepts/nomos-compiled-policy-enforcement.md — K288 inbound brief / 2026-10-12
- @sources/arxiv-2610-11030-nomos-compiled-policy-tool-gate.md — K288 inbound brief / 2026-10-12
- @concepts/cross-service-agent-compositional-harm.md — K418-K424 ingest / 2026-10-12
- @sources/arxiv-2610-13886-x-agentred-cross-service-redteam.md — K418-K424 ingest / 2026-10-12
- @sources/arxiv-2606-22916-intent-governed-tool-authorization-igac.md — IGAC paper (2606.22916)
- @concepts/mcp-security-posture.md — admission layer complement

## Raw Concept

Ingest 2026-06-24: arXiv:2606.22916 — **Intent-Governed Access Control** for server-side agent tool authorization.

## Narrative

### Authorization gap

| Question | Traditional OAuth/MCP scope | IGAC adds |
|----------|----------------------------|-----------|
| Can credential call tool? | ✓ | — |
| Is call justified by **current user request**? | — | ✓ |

Example: read+export integration authorized statically — user asks for summary only → export tools should be **filtered from manifest** and export payloads rejected.

### Components

1. **Intent certificates** — session-scoped authority ceiling from parsed user goal
2. **Monotone narrowing** — intent can only shrink static grants
3. **Intent-aware manifest filtering** — planner sees reduced tool surface
4. **Intent–tool–payload consistency** — arg-level check before invoke

Mapped to **OpenPort** substrate in paper. Pilot: static auth still allowed **85.71%** of high-risk requests immediately — IGAC layering required.

### prod-mcp positioning

Sits **above** attested admission (2605.24248) and **before** planner:
- Admission: which servers/tools enter catalog
- **IGAC:** which subset matches current user intent
- AIRGuard/ChainCaps: runtime execution/composition

See `briefs/2026-06-24_igac-intent-governed-tool-auth-handoff.md`.

`[TENTATIVE]` — OpenPort pilot; Claude Code / lazy-tool mapping not lab-tested.

### Intent contracts do not reduce unauthorized actions (2026-11-22)

Intent Contracts (2611.24025) takes the idea further: the planner holds no tools, and a trusted model writes every call from a validated goal plus a verbatim user quotation. The code properties are real: every executed call is written by the trusted model, and a logged contract precedes it.

The measured security result is negative. Contracts did not reduce unauthorized actions and were indistinguishable from blind review. Every state-changing condition hit a wrong target in 40 to 49% of runs, because the planner chose the wrong object for an ambiguous reference and no trusted model could see the environment. Contracts did complete more tasks than a whole-command reviewer (27/30 against 16/30).

Rule: use intent contracts for audit evidence, not as a proven authorization control. See @concepts/intent-contract-planner-tool-separation.md.

## Snippets

> "User intent may only reduce the authority granted by static integration credentials."

[Source: arxiv-2606.22916]
