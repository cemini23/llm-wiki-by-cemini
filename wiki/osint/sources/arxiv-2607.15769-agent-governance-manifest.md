---
title: "arXiv 2607.15769 — Agent Governance Manifest (AGM) for OSS"
type: source
tags: [source, arxiv, agent-harness, governance, oss, k177, ccc]
keywords: [2607.15769, AGM, agent-governance-manifest, governability, OSS]
related:
  - concepts/agent-governance-manifest.md
  - entities/tools/agent-governance-manifest.md
  - concepts/code-as-agent-harness.md
maturity: draft
read_status: read
created: 2026-07-20
updated: 2026-07-20
clusters: [k177-ingest]
---

## Relations

- @concepts/agent-governance-manifest.md — synthesis
- @entities/tools/agent-governance-manifest.md — MIT GitHub Extract
- @concepts/code-as-agent-harness.md — readability/traceability layers

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | 2607.15769 |
| **sha256** | `0d395390794519b370837d8a918c08691408504772a949ac77214a29c46e9c60` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.15769-making-agent-mediated-contributions-governable-a.pdf` |

## Narrative

Theorizes **project-side governability** beyond agent-readability (AGENTS.md) and traceability: shared risk rules, evidence obligations, accountability states, review gates, maintainer decision rights. Audit of 50 GitHub repos finds fragmented AI-governance cues; none institutionalize full arrangement. Proposes **Agent Governance Manifest (AGM)** as bidirectional contract (contributor evidence ↔ maintainer verification). Reviewer eval: risk-label recovery 37/38 vs 15/37; support score 6.14 vs 3.27. **Steal:** CCC/federation — optional `.agm/` Extract for agent PR risk zones; human GO retained. Phase-0: MIT, ~1MB, Extract (not force-Integrate to prod CI).
