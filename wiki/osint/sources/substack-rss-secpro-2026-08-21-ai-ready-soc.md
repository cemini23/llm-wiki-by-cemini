---
title: "SecPro #248 — building an AI-ready SOC, part 1 (foundations)"
type: source
tags: [cyber, soc, telemetry, identity, rag]
keywords: [AI-ready-SOC, asset-ID-map, agent-as-identity, RAG-runbooks, gather-not-decide]
related:
  - concepts/agent-runtime-identity-adr.md
  - concepts/agent-safety-executable-evaluation.md
  - sources/substack-rss-secpro-2026-08-28-249-ai-ready-soc.md
maturity: draft
created: 2026-08-21
updated: 2026-08-29
read_status: skimmed
---

## Relations
- @concepts/agent-runtime-identity-adr.md
- @concepts/agent-safety-executable-evaluation.md
- @sources/substack-rss-secpro-2026-08-28-249-ai-ready-soc.md — part 2 architecture (K249 sequel)

## Raw Concept
- **title:** #248: Building an AI-Ready SOC, part 1
- **author:** Packt SecPro
- **type:** Substack essay
- **location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-secpro-2026-08-21-248-building-an-ai-ready-soc-part-1.md`
- **retrieved:** 2026-08-21
- **pages:** full part-1 (ignore MCP-summit / finance-cert ads)
- **read-status:** skimmed

## Narrative
Buying an “AI SOC” on top of a weak SIEM fails: AI exposes bad telemetry, identity, and IR process.

**Foundations:**
1. Complete-enough telemetry (endpoint, identity, cloud, DNS/firewall, app logs) with APIs, aligned timestamps, and **one asset identifier mapping**. More logs ≠ better; dump-everything raises cost and noise.
2. Normalise schemas. Do not rely on the LLM to paper over vendor field chaos — agents cannot improvise like analysts.
3. Identity: users, service accounts, machines, apps, **and the AI agents themselves**. No shared god-mode SOC service account. Agents authenticate, get least privilege (e.g. EDR read, no config write), and are logged.
4. Knowledge: RAG over runbooks, past incidents, naming conventions, known service accounts, detection logic, threat intel. Automating a broken eight-step workflow just makes a faster mess.
5. Automate **gathering** (logs, intel, timelines, summaries) before **decisions** (disable exec account, isolate prod).
6. Start narrow: alert triage (retrieve endpoint+identity, related events, intel → summary; human closes/escalates). Measure baseline MTT-investigate, alert throughput, FP escalations, report time, hunts/month — then re-measure.
7. Analysts need AI literacy (hallucination, prompt injection, RAG) without dropping Windows/network/auth skills. Part 2 promised on stacking telemetry/knowledge/models/agents/response.

Steal: treat every Cemini/SOC agent as a least-privilege identity; RAG the wiki/runbooks; automate evidence gathering only. Complements tldrsec Figma/Uber (the deployed layer) with the foundation layer. Pairs with SPIFFE `act=agent` and ADR telemetry.

## Snippets
> AI cannot compensate for poor telemetry, fragmented systems or weak security processes. … An AI agent cannot correlate events effectively if one platform identifies a machine by hostname, another by IP address and another by an internal asset identifier that nobody has mapped correctly. [Source: https://secpro.substack.com/p/248-building-an-ai-ready-soc-part (retrieved 2026-08-21)]

> The better approach is to treat AI systems as identities within the security architecture. They should authenticate, receive narrowly defined permissions and have their activity logged. [Source: https://secpro.substack.com/p/248-building-an-ai-ready-soc-part (retrieved 2026-08-21)]

> A useful rule is to automate information gathering before decision-making. … Deciding whether to disable an executive’s account or isolate a critical production server is a different matter. [Source: https://secpro.substack.com/p/248-building-an-ai-ready-soc-part (retrieved 2026-08-21)]
