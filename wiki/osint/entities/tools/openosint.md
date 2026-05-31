---
title: "OpenOSINT — real-time OSINT dashboard (Palantir-style)"
type: entity
tags: [tool, adopt-candidate, osint, geospatial, webgl, k88, phase-0-pending]
keywords: [openosint, gdelt, aircraft, satellites, dashboard, mcp]
related:
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - concepts/librarian-server-architecture.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
phase_0_verdict: PENDING — K88 Adopt; MIT confirmed
---

## Relations

- @sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md — K88 v5 Adopt (OSINT-primary)
- @concepts/librarian-server-architecture.md — compare vs kb-server + conductor serving path

## Raw Concept

- **Repo**: `github.com/OpenOSINT/OpenOSINT`
- **License**: MIT `[CONFIRMED 2026-05-31]` (LICENSE file in repo per eval)
- **Prompted by**: K88 eval — 60fps WebGL map aggregating aircraft, satellite, GDELT feeds

## Narrative

Production-grade OSINT dashboard pitched as Palantir alternative. **Gap-fill check required:** does not duplicate conductor/kb-server RAG; may complement geospatial entity pages. Phase-0 audit: hardcoded data sources, deploy footprint on librarian vs laptop-only.
