---
title: "Home Lab Hub (RaidOwl)"
type: entity
tags: [tool, visualization, cytoscape, self-hosted, graph-viz, k37]
keywords: [homelab, hub, steal-from, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
license_verified: MIT
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 18)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/RaidOwl/homelab-hub`
- **Tier (per source brief)**: **Steal-from**
- **License** [VERIFIED 2026-05-11]: **MIT** (clean for pattern extraction per Cemini license posture). Maturity: 541★ / last push 2026-03-14 / ~2.8 months old.

## Narrative

Self-hosted visualization + inventory management for personal server environments. Cytoscape.js-rendered depth-first graph maps hardware ↔ VM ↔ Docker container ↔ external service relationships.

### Integration vector

Steal-from: lift the **Cytoscape.js graph viz layer** for hierarchical-data → interactive-node translation. Repurpose for graphing wiki backlinks / entity-relation network. Discard the IT-asset CRUD layer entirely.

### Risks

Hub operates via manual CRUD; documented data guaranteed to drift from actual state without automated polling.

[Source: Evaluating Urls System Integration.docx, URL 18]
