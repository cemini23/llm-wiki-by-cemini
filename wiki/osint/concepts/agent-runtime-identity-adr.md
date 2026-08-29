---
title: Agent runtime identity + ADR — SPIFFE, tool-layer safety, gather-not-decide
type: concept
tags: [cyber, identity, detection, soc]
keywords: [SPIFFE, JWT-SVID, act-agent, Uber-ADR, Figma-tool-layer, Trust-Ratchet, asset-ID-map]
related:
  - sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md
  - sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md
  - sources/arxiv-2608.19857-inadvertent-context-leakage.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/inadvertent-context-leakage.md
  - sources/substack-rss-secpro-2026-08-28-249-ai-ready-soc.md
  - sources/arxiv-2608.27009-guard-that-cried-wolf-2026-08-29.md
  - concepts/k249-cyber-agent-safety-wave.md
maturity: draft
created: 2026-08-21
updated: 2026-08-29
---

## Relations
- @sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md
- @sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md
- @sources/arxiv-2608.19857-inadvertent-context-leakage.md
- @concepts/agent-safety-executable-evaluation.md
- @concepts/inadvertent-context-leakage.md
- @sources/substack-rss-secpro-2026-08-28-249-ai-ready-soc.md — part 2 six-layer stack + RAG provenance
- @sources/arxiv-2608.27009-guard-that-cried-wolf-2026-08-29.md — tool-layer refuse must read policy, not the object name
- @concepts/k249-cyber-agent-safety-wave.md — K249 cluster

## Raw Concept
An agent is an identity, not a shared SOC login and not “the human’s API key on disk.” Short-lived SPIFFE JWT-SVIDs with `sub=human` / `act=agent`; safety at the **tool layer**; telemetry + two-tier detection (ADR); one asset-ID map; automate gather, not decide.

## Narrative
Three complementary 2026-08-20/21 writeups:

| Layer | Pattern | Source |
|---|---|---|
| Identity | OS code-sign → Enclave/TPM SVID; OAuth Txn tokens; no standing secrets | 1Password via tl;dr sec #342 |
| Access | Task-scoped grants, mediation, irreversible Trust Ratchet | Cloudflare AAM |
| Detection | Prompt/MCP/trace/tool sensor + two-tier detector; ADR-Bench | Uber ADR |
| Action bounds | Tool-layer allowlists; draft-only PRs; three memories (case/steering/procedural) | Figma Panther |
| Foundations | Telemetry APIs, one asset ID, agent least privilege, RAG runbooks | SecPro #248 |
| Architecture | Data / knowledge / intelligence / agents / action / governance; model routing; controlled action interface | SecPro #249 |

Leakage paper adds: even a well-identified agent’s *benign text* is a covert channel if secrets sat in context. So identity+ADR is necessary, not sufficient — keep secrets out of the prompt.

Cemini/SOC steal (propose-only SPIFFE): every local agent authenticates as `act=agent`; EDR-read not config-write; log tool calls; draft PRs; human closes triage. No scp.

## Snippets
See @sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md and @sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md.
