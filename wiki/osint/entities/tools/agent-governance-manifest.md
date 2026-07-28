---
title: Agent Governance Manifest (GitHub)
type: entity
tags: [entity, tool, agent-harness, governance, k177]
keywords: [AGM, agent-governance-manifest, MIT, .agm]
related:
  - concepts/agent-governance-manifest.md
  - sources/arxiv-2607.15769-agent-governance-manifest.md
  - entities/tools/agent-governance-toolkit.md
maturity: draft
created: 2026-07-20
updated: 2026-07-28
---

## Relations

- @entities/tools/agent-governance-toolkit.md — K198 Microsoft toolkit (distinct)

- @concepts/agent-governance-manifest.md
- @sources/arxiv-2607.15769-agent-governance-manifest.md

## Raw Concept

Phase-0 K177 Extract of https://github.com/agent-governance-manifest/agent-governance-manifest (MIT, ~79KB remote size, 7★, pushed 2026-06-25).

## Narrative

| Field | Value |
|-------|-------|
| **License** | MIT `[CONFIRMED]` via `gh api` |
| **Local adopt** | `.local/adopts/agent-governance-manifest` (~1MB shallow) |
| **Homepage** | https://agent-governance-manifest.github.io/agent-governance-manifest/ |
| **Tier** | Extract — schemas / validators / review packets |
| **NO-GO** | Auto-merge into prod CI; treating AGM as AI detector |

Failure mode: projects confuse AGM with AGENTS.md readability. Keep human maintainer authority explicit.
