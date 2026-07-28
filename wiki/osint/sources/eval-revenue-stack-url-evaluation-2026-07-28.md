---
title: "Revenue Stack URL Evaluation — 2026-07-28"
type: source
tags: [source, tool-eval, k198, revenue, atto]
keywords: [book-to-skill, aisuite, agent-governance-toolkit, GeoLibre, Mapbox]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/active-project-research-routing.md
  - entities/tools/book-to-skill.md
  - entities/tools/aisuite.md
  - entities/tools/agent-governance-toolkit.md
  - entities/tools/geolibre.md
maturity: draft
read_status: read
created: 2026-07-28
updated: 2026-07-28
clusters: [k198-ingest]
---

## Relations

- @concepts/wiki-tooling-evaluation.md
- @concepts/gpuology-genealogy-agent-kit.md
- @concepts/active-project-research-routing.md
- @entities/tools/book-to-skill.md
- @entities/tools/aisuite.md
- @entities/tools/agent-governance-toolkit.md
- @entities/tools/geolibre.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `Revenue Stack URL Evaluation.docx` |
| **sha256** | `738bb8658ae52c68d7f928dcb8990635ee5b1f9db3989d50c16380360ab7d66a` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Revenue Stack URL Evaluation.docx` |
| **License spot-check** | `.local/reports/license-spot-check-2026-07-28-0816.txt` |
| **Theme** | AI agent frameworks, governance, local models, geospatial, systematic trading |

## Narrative

20-URL revenue+fit eval (Priority #1 Atto · #2 GuruWatcher). **License overrides (gh api — do not trust eval SPDX):**

| Eval tier | Repo | Verified license | Operator action |
|-----------|------|------------------|-----------------|
| **Integrate** | virgiliojr94/book-to-skill | MIT `[CONFIRMED]` | Phase-0 `.local/adopts/book-to-skill` (~1MB) → Atto playbook→SKILL.md |
| **Extract** | andrewyng/aisuite | MIT `[CONFIRMED]` | Already adopted K195 (~11MB); Atto/GuruWatcher multi-provider failover |
| **Extract** | microsoft/agent-governance-toolkit | MIT `[CONFIRMED]` | Phase-0 ~85MB — distinct from AGM paper/`agent-governance-manifest` |
| **Extract** | opengeos/GeoLibre | MIT `[CONFIRMED]` | Phase-0 ~36MB — Atto place/map FOSS stack |
| **Watch** | fermionresearch.com/models | N/A (site) | Local/edge model catalog — no clone |
| **Watch** | Mapbox Places API | Proprietary | Combo with GeoLibre; paid API only |
| **Context** | moeru-ai/airi | MIT | Browser WebGPU inference pattern (CCC notes) |
| **Context** | paperswithbacktest/awesome-systematic-trading | null | List only; wangzhe3224 fork MIT |
| **Context** | img2threejs | Apache-2.0 | Game/3d cross-wiki brief only |
| **Pass** | pascalorg/editor, jenkins, superfile, uscode, dco, baton, artillery, CrisperWhisper, founden, power-atlas | various | Aggregated — **no stub farm** |

**License corrections vs eval:** artillery = **MPL-2.0** (eval said BSL); jenkins = **MIT** (eval NOT FOUND); paperswithbacktest SPDX null; CrisperWhisper NOASSERTION.

**Phase-0 total:** book-to-skill + agent-governance-toolkit + GeoLibre ≈ **122MB** ≪ 500MB. Script: `scripts/adopt_k198_phase0.sh`.

## Snippets

> book-to-skill → atto: structured SKILL.md from methodology books — core IP for kit SKU.
