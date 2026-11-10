---
title: Mechanical Engineering Skills — Open Agent Skill Library (BaratiLab)
type: entity
related:
  - sources/arxiv-mechanical-engineering-skills-2611.05758.md
  - concepts/agent-skill-libraries-mechanical-engineering.md
  - concepts/self-improving-cad-generation-agents.md
  - concepts/extrusion-control.md
maturity: draft
updated: 2026-11-10
---

## Raw Concept

Created on the 2026-11-10 ingest of @sources/arxiv-mechanical-engineering-skills-2611.05758.md. The page exists because the library is an installable artefact with a public repository, not only a paper.

## Narrative

| Field | Value |
|---|---|
| Name | Mechanical Engineering Skills |
| Owner | Barati Farimani Lab, Carnegie Mellon University |
| Repository | https://github.com/BaratiLab/mechanical-engineering-skills |
| Install | `npx skills add BaratiLab/mechanical-engineering-skills` |
| Size | 33 skills (19 package lab papers, 14 core engineering tasks) |
| Hosts | Claude Code, Claude.ai, and other Agent Skills hosts |
| Licence | [NEEDS VERIFICATION 2026-11-10] The paper does not state a licence for the library |
| Maturity | Research release, November 2026 |

### Skill anatomy

Each skill is one directory:

- `SKILL.md` — a description that drives routing, then a workflow of four to six steps with the judgement calls an engineer would make.
- `scripts/` — command-line Python with JSON output.
- `references/` — paper notes and data provenance, loaded only on demand.
- `tests/` — exact cases and paper numbers for regression.

### Skills a print farm could use

| Skill | Use |
|---|---|
| `agentscad-fdm-dfam` | Reorient a STEP part and add teardrop holes and chamfers for FDM |
| `image2gcode` | Photo or sketch to G-code for 2D and 2.5D parts |
| `lattice-inverse-design` | Target stiffness to a printable TPMS cell plus a tiled STL |
| `llm-3d-print-monitor` | Per-layer camera inspection with bounded correction on Klipper |
| `dfm-review` | Manufacture review across machining, sheet metal, moulding, and AM |
| `am-literature-rag` | Page-cited answers over a local additive-manufacturing paper set |

### What it does not do

The install copies folders only. It does not install or license the solvers underneath. A missing CAD kernel, solver, or thermodynamic database makes a skill fall back to a validator, an analytical estimate, or rehearsal data, and the skill reports the fallback. Any number from a fallback is not a validated result.

No benchmark compares an agent with skills against an agent without them. The efficiency claim is untested. [TENTATIVE]

## Snippets

> "The library is available at https://github.com/BaratiLab/mechanical-engineering-skills." [Source: arxiv-2611.05758-mechanical-engineering-skills-an-open-library-of.pdf p.1]
