---
title: "Eval — Project Portfolio URL Analysis 2026-08-08"
type: source
tags: [eval, phase-0, k228, atto, cyber]
keywords: [pdf-inspector, Codex-Orchestration, FUXA, godoxy]
related:
  - entities/tools/pdf-inspector.md
  - entities/tools/codex-orchestration.md
  - entities/tools/bugbounty-lab101.md
  - entities/tools/opennews-mcp.md
  - entities/tools/pi-earendil.md
  - entities/tools/pi-peer.md
  - entities/tools/ai-website-cloner-template.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/active-project-research-routing.md
maturity: draft
created: 2026-08-08
updated: 2026-08-08
read_status: read
---

## Relations

- @entities/tools/pdf-inspector.md
- @entities/tools/codex-orchestration.md
- @entities/tools/bugbounty-lab101.md
- @entities/tools/opennews-mcp.md
- @entities/tools/pi-earendil.md
- @entities/tools/pi-peer.md
- @entities/tools/ai-website-cloner-template.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/active-project-research-routing.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Project Portfolio URL Analysis.docx |
| sha256 | `1b310f989a1d9bea7b2fc93e064b17ba8fae84ef7e6eca534bc5690ae62d98a9` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Project Portfolio URL Analysis.docx` |
| retrieved | 2026-08-08 |

20-URL portfolio batch. **Never trust eval SPDX** — `gh api` overrides.

## Narrative

| # | Repo | gh SPDX | Tier | Verdict |
|---|------|---------|------|---------|
| 3 | firecrawl/pdf-inspector | **MIT** | Integrate → Atto | **Reaffirm Integrate** — already cloned K218; scanned-vs-text PDF routing. |
| 6 | Cjbuilds/Codex-Orchestration | **MIT** | Extract → lab | **GO Extract** ~1.6MB. |
| 8 | yusing/godoxy | **NOASSERTION** | Watch | **NO-GO clone** (eval MIT wrong). |
| 9 | frangoteam/FUXA | **MIT** | Extract | **Size-skip** (~600MB shallow). Patterns-only ICS/SCADA. |
| 11 | bannedbook/fanqiang | GPL-3.0 | Context | **Context** — no clone. |
| 12 | RustPython | MIT | Watch | **Size-skip**. |
| others | Pass/UNAVAILABLE | — | Skip |

## Snippets

> Integrate: pdf-inspector. Extract: Codex-Orchestration, FUXA. [Source: Project Portfolio URL Analysis.docx]
