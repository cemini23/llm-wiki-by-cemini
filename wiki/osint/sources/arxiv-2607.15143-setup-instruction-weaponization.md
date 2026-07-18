---
title: "arXiv 2607.15143 — Weaponizing Setup Instructions Against AI Coding Agents"
type: source
tags: [source, arxiv, security, k173]
keywords: [supply-chain, README, coding-agent, 2607.15143, k173]
related:
  - concepts/agent-setup-instruction-supply-chain.md
maturity: draft
read_status: read
created: 2026-07-18
updated: 2026-07-18
clusters: [k173-ingest]
---

## Relations

- @concepts/agent-setup-instruction-supply-chain.md

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | 2607.15143 |
| **sha256** | `793017a12f9844b2cc6a6776c00dea4c355e1ca3f43911120813ef258575b5bd` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.15143-setup-complete-now-you-are-compromised-weaponizi.pdf` |

## Narrative

First systematic eval of package-install-time supply-chain attacks delivered through ordinary project-setup docs (README / requirements / Makefile). Agents install listed deps without verifying names, registries, or known CVEs — documentation becomes a code-execution vector. **Routing:** CCC harness hardening + cybersec brief + TipDrop/David STOP on blind `npm/pip install` from untrusted READMEs.
