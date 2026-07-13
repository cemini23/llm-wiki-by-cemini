---
title: SecEng Weekly — Agentic AI Security Fundamentals (2026-07-13)
type: source
tags: [source, security, agentic-ai, k162]
keywords: [prompt injection, instructions vs data, Schneier, agent security]
clusters: [k162-ingest, cybersec]
related:
  - concepts/generator-verifier-inference-time-steering.md
maturity: validated
read_status: deep-read
created: 2026-07-13
updated: 2026-07-13
---

## Raw Concept

| Field | Value |
|-------|-------|
| **URL** | https://secengweekly.substack.com/p/agentic-ai-security-fundamentals |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-seceng-weekly-2026-07-13-agentic-ai-security-fundamentals.md` |
| **Cross-wiki** | → cybersecurity-wiki brief |

## Narrative

Core claim: LLMs cannot separate instructions from data — web pages, issues, emails, uploads all enter the same token stream. Once agents can act (files/APIs/commands), that becomes attack surface. Schneier cited: zero agentic systems secure against these attacks; industry denial. Steal for CCC/poker harness: treat tool outputs / opponent messages / Arena JSON as **untrusted data** (already in poker AGENTS.md) — extend same hygiene to TipDrop/operator agents.

**Not a David ComfyUI adoption** — security process brief for cybersec + CCC.

## Relations

- @concepts/generator-verifier-inference-time-steering.md — process verification adjacency
