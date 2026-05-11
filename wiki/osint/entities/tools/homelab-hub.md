---
title: "Home Lab Hub (RaidOwl)"
type: entity
tags: [tool, visualization, cytoscape, self-hosted, graph-viz, k37]
keywords: [homelab, hub, steal-from, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 18)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/RaidOwl/homelab-hub`
- **Tier (per source brief)**: **Steal-from**
- **License**: [NEEDS VERIFICATION 2026-05-11] License needs verification.

## Narrative

Self-hosted visualization + inventory management for personal server environments. Cytoscape.js-rendered depth-first graph maps hardware ↔ VM ↔ Docker container ↔ external service relationships.

### Integration vector

Steal-from: lift the **Cytoscape.js graph viz layer** for hierarchical-data → interactive-node translation. Repurpose for graphing wiki backlinks / entity-relation network. Discard the IT-asset CRUD layer entirely.

### Risks

Hub operates via manual CRUD; documented data guaranteed to drift from actual state without automated polling.

[Source: Evaluating Urls System Integration.docx, URL 18]
