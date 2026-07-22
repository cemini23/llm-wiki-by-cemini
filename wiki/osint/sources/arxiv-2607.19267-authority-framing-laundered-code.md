---
title: "arXiv 2607.19267 — Authority framing + laundered code in agentic CI/CD"
type: source
tags: [source, arxiv, security, agent-harness, ccc, cybersec, k182]
keywords: [2607.19267, authority-framing, laundered-PR, claimed-authorization, CI-CD]
related:
  - concepts/code-as-agent-harness.md
  - concepts/agent-reactive-bugs.md
maturity: draft
read_status: read
created: 2026-07-22
updated: 2026-07-22
clusters: [k182-ingest]
---

## Relations

- @concepts/code-as-agent-harness.md
- @concepts/agent-reactive-bugs.md

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | 2607.19267 |
| **sha256** | `3c63a1b3a3eb59b9cd9146c4038489dd7152bbcc1fe2707c86cf5066fd0dd512` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.19267-they-ll-verify-they-just-won-t-act-how-authority.pdf` |

## Narrative

Five-agent CI/CD (triage→dev→scan→review→deploy): authority-framed injection ("pre-approved SEC-2291") makes verifiers cite pre-approval and ship secret-exfil laundered as telemetry. Scanner passes ~80% laundered PRs; worst-case 55% compromise. Content scanners miss intent; provenance-aware entry control needed. **CCC / cybersec / TipDrop:** reinforce claimed-authorization + setup-instruction STOP. **Poker:** same class as claimed-authorization guard — no self-attested authority.
