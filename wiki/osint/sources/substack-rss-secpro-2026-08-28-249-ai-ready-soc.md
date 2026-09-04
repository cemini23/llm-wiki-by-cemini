---
title: "SecPro #249 — building an AI-ready SOC, part II (architecture)"
type: source
tags: [cyber, soc, rag, agents, k249]
keywords: [AI-ready-SOC, six-layer, RAG, gather-not-decide, SAIF, ATLAS]
related:
  - concepts/k249-cyber-agent-safety-wave.md
  - concepts/agent-runtime-identity-adr.md
  - sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md
  - sources/substack-rss-secpro-2026-09-04-ai-ready-soc-part-iii-2026-09-04.md
  - concepts/k255-cybersec-wave.md
updated: 2026-09-04
read_status: read
---

## Relations

- @concepts/k249-cyber-agent-safety-wave.md — K249 cyber cluster
- @concepts/agent-runtime-identity-adr.md — agent-as-identity + gather-not-decide already on this page
- @sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md — part 1 foundations (LIKELY sequel, not a duplicate)

## Raw Concept

| Field | Value |
|-------|--------|
| Title | #249: Building an AI-Ready SOC, part II |
| Author | Packt SecPro |
| Type | Substack essay |
| File | `substack-rss-secpro-2026-08-28-249-building-an-ai-ready-soc-part-ii.md` |
| sha256 | `67a7df9ceb0aa2927f02640e7dee941c53faaa165e4f64826492cb2f51d9f87f` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-secpro-2026-08-28-249-building-an-ai-ready-soc-part-ii.md` |
| URL | https://secpro.substack.com/p/249-building-an-ai-ready-soc-part |
| Retrieved | 2026-08-28 |
| Dual-ID | **OSINT K249** = this inbox |
| Preingest | LIKELY vs #248 (Jaccard 0.55) — sequel, ingest as new page |

## Narrative

Part 2 of the AI-ready SOC series. An AI SOC is not a SIEM plus a chatbot. Six interdependent layers:

1. **Data** — SIEM / EDR / NDR / IdP / cloud / vuln / DNS / app logs. One asset-ID map. APIs and aligned timestamps.
2. **Knowledge** — ATT&CK, inventories, past incidents, runbooks. RAG over **approved** repos. Stale docs poison recommendations.
3. **Intelligence** — route models by task (small classifier vs large investigation). Evaluate per task, not one universal LLM.
4. **Agents** — goal-directed investigation sequences. Treat each agent as an identity with least privilege. Read-only EDR ≠ isolate-host write.
5. **Action** — SOAR / EDR / IdP / tickets / firewall / cloud APIs. Automate gather; HITL on disable-account / isolate-prod.
6. **Governance** — SAIF + NIST AI RMF. Who can send telemetry to an external model? How are prompts and tool calls logged?

Orchestration sits between reasoning and APIs so agents do not get raw enterprise endpoints. RAG integrity is a control: poisoned knowledge bases change later investigations.

Build incrementally: SIEM assistant → RAG → read-only EDR/identity → then actions. Measure MTT-investigate, alert throughput, FP, IR time, hunts/month. Part 3 promised on prompt injection, RAG poisoning, excessive permissions.

Steal: same as #248 plus **model routing**, **controlled action interface**, **knowledge-base provenance**. No new runtime wire this wave.

## Snippets

> "an AI-ready SOC is not simply a SIEM with a chatbot attached to it." [Source: https://secpro.substack.com/p/249-building-an-ai-ready-soc-part (retrieved 2026-08-28)]

> "An agent with read-only access to EDR telemetry presents a different risk from an agent capable of isolating endpoints, disabling accounts or modifying firewall rules." [Source: same]
