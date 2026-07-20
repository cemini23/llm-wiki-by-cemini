---
title: Agent Governance Manifest (AGM) — project-side governability
type: concept
tags: [concept, agent-harness, governance, oss, k177, ccc]
keywords: [AGM, governability, evidence-package, risk-zones, maintainer-authority]
related:
  - sources/arxiv-2607.15769-agent-governance-manifest.md
  - entities/tools/agent-governance-manifest.md
  - concepts/code-as-agent-harness.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- @sources/arxiv-2607.15769-agent-governance-manifest.md — paper
- @entities/tools/agent-governance-manifest.md — MIT prototype
- @concepts/code-as-agent-harness.md — readability / traceability siblings

## Raw Concept

Three layers: **agent-readability** (instructions) → **traceability** (disclosure/provenance) → **governability** (risk/evidence/review gates with maintainer decision rights).

## Narrative

AGM instantiates governability as a repo-hosted `.agm/` contract: contributor agents prepare evidence packages; maintainers verify against declared risk zones. Not a merge bot / AI detector / AGENTS.md replacement. **Cemini posture:** Extract schemas + review-packet patterns for CCC federation agent PRs; **no** forced Integrate into cemini-prod CI without operator GO. Local shallow clone ~1MB under `.local/adopts/`.
