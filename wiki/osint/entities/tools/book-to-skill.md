---

title: "book-to-skill — book corpus → Claude skill pipeline"
type: entity
tags: [tool, integrate, mit, k198, k225, atto, ccc]
keywords: [book-to-skill, virgiliojr94, skill generation, Atto]
related:
  - sources/eval-revenue-stack-url-evaluation-2026-07-28.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - sources/eval-url-batch-agentic-osint-integrations-2026-08-06.md
  - entities/tools/skill-seekers.md
  - entities/tools/sie-superlinked.md
  - entities/tools/pi-llm-wiki.md
  - concepts/historical-document-kg-query-inference.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/bidirectional-hai-skill-evolution.md
  - entities/tools/aisuite.md
  - entities/tools/ai-sales-team-claude.md
  - sources/arxiv-2608.05026-artanno-bihaa-2026-08-06.md
  - sources/eval-tech-stack-opportunity-2026-08-06.md
maturity: draft
created: 2026-05-31
updated: 2026-08-06
phase_0_verdict: INTEGRATE — K198/K225 MIT shallow adopt (~2.5MB)
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc
---

## Relations

- @entities/tools/aisuite.md — K198 backlink
- @sources/eval-revenue-stack-url-evaluation-2026-07-28.md — K198 Integrate
- @sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md — K88 Adopt (pending then)
- @sources/eval-url-batch-agentic-osint-integrations-2026-08-06.md — K225 reaffirm Integrate
- @entities/tools/skill-seekers.md
- @entities/tools/sie-superlinked.md — K225 semantic index combo
- @entities/tools/pi-llm-wiki.md — K225 local wiki RAG combo
- @concepts/historical-document-kg-query-inference.md
- @concepts/gpuology-genealogy-agent-kit.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/bidirectional-hai-skill-evolution.md — BiHAA closes the loop after book→skill export

## Raw Concept

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/virgiliojr94/book-to-skill |
| **License** | MIT `[CONFIRMED]` gh api K225 |
| **Local** | `.local/adopts/book-to-skill` (~2.5MB) |
| **Stars** | ~17.5k (2026-08-06) |

## Narrative

Converts book-length methodology into Claude Code `SKILL.md` modules. **K198/K225 Integrate for Atto:** Italian civil/parish playbooks → on-demand skills (copyright: internal agent use only; never redistribute raw copyrighted book text). Combo with `sie` (semantic entity index) + `pi-llm-wiki` (local RAG) + BiHAA trajectory distillation. Regression-tax gate any generated skills before kit ship.
