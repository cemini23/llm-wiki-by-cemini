---
title: "Eval — GitHub Repository Evaluation Plan 2026-08-10"
type: source
tags: [eval, phase-0, k230, atto, guruwatcher, ccc, cyber]
keywords: [diagram-design, weathernext, t3code, code-graph-rag, CLIProxyAPI, tookie-osint]
related:
  - entities/tools/ruview.md
  - entities/tools/ileapp.md
  - entities/tools/dopamine-jailbreak.md
  - concepts/agent-harness-auditing-a2e.md
  - concepts/intent-bound-tool-gates.md
  - entities/tools/diagram-design.md
  - entities/tools/weathernext.md
  - entities/tools/code-graph-rag.md
  - entities/tools/t3code.md
  - entities/tools/cliproxyapi.md
  - entities/tools/tookie-osint.md
  - entities/tools/lifeos.md
  - entities/tools/epicstaff.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/active-project-research-routing.md
  - sources/arxiv-2608.06651-cyberllm-automotive-2026-08-10.md
  - sources/arxiv-2608.06909-trajectory-attribution-2026-08-10.md
  - sources/arxiv-2608.07051-yolo-peft-2026-08-10.md
  - sources/arxiv-2608.07147-didpo-coding-agent-2026-08-10.md
  - sources/arxiv-2608.07167-niyamai-intent-bound-2026-08-10.md
  - sources/arxiv-2608.07346-a2e-agent-auditing-2026-08-10.md
maturity: draft
created: 2026-08-10
updated: 2026-08-10
read_status: read
---

## Relations
- @concepts/intent-bound-tool-gates.md
- @concepts/agent-harness-auditing-a2e.md
- @entities/tools/dopamine-jailbreak.md
- @entities/tools/ileapp.md
- @entities/tools/ruview.md

- @entities/tools/diagram-design.md
- @entities/tools/weathernext.md
- @entities/tools/code-graph-rag.md
- @entities/tools/t3code.md
- @entities/tools/cliproxyapi.md
- @entities/tools/tookie-osint.md
- @entities/tools/lifeos.md — reaffirm Extract (already K229)
- @entities/tools/epicstaff.md — NOASSERTION NO-GO reaffirm
- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/active-project-research-routing.md
- @sources/arxiv-2608.06651-cyberllm-automotive-2026-08-10.md
- @sources/arxiv-2608.06909-trajectory-attribution-2026-08-10.md
- @sources/arxiv-2608.07051-yolo-peft-2026-08-10.md
- @sources/arxiv-2608.07147-didpo-coding-agent-2026-08-10.md
- @sources/arxiv-2608.07167-niyamai-intent-bound-2026-08-10.md
- @sources/arxiv-2608.07346-a2e-agent-auditing-2026-08-10.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | GitHub Repository Evaluation Plan.docx (+ identical `(1)` copy) |
| sha256 | `5a6ac5968253a47a81e0bf8d5afe74a7b903751b14055b17e3a968b58a960bc4` |
| sha256 (1) | `99bbe5c01999607319c63d53cf816e723aaf4e9c97a37f648f4aa3b6ef3a2c08` (same text body; different zip container) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repository Evaluation Plan.docx` |
| retrieved | 2026-08-10 |

20-URL agent-orchestration / edge / macro batch. **Never trust eval SPDX** — `gh api` + LICENSE override.

## Narrative

| # | Repo | gh SPDX | Tier | Verdict |
|---|------|---------|------|---------|
| 1 | cathrynlavery/diagram-design | **MIT** | Integrate | **GO Integrate** ~10MB → Atto |
| 2 | ruvnet/RuView | **MIT** | Watch | **Size-hold** (~185MB) |
| 3 | google-deepmind/weathernext | **Apache-2.0** | Extract | **GO Extract** ~11MB → GW |
| 4 | vitali87/code-graph-rag | **MIT** | Integrate | **GO Integrate** ~41MB → CCC |
| 5 | pingdotgg/t3code | **MIT** | Integrate | **GO Integrate** ~316MB → CCC |
| 6 | opa334/Dopamine | **MIT** | Watch | **No-clone** (jailbreak ethics) |
| 8 | abrignoni/iLEAPP | **MIT** | Extract | **Size-hold** (~236MB) |
| 10 | danielmiessler/LifeOS | **MIT** | Extract | **Reaffirm** (K229 clone) |
| 11 | EpicStaff/EpicStaff | **NOASSERTION** | Watch | **NO-GO** reaffirm |
| 13 | router-for-me/CLIProxyAPI | **MIT** | Integrate | **GO Integrate** ~23MB → CCC |
| 16 | Alfredredbird/tookie-osint | **MIT** | Extract | **GO Extract** ~1.7MB → Atto FIND |
| 7,9 | Pass | — | Skip |
| 12,17 | Context | — | image-gen / cyber briefs |
| 14–15,18–20 | UNAVAILABLE | — | Skip |

Phase-0: `scripts/adopt_k230_phase0.sh` → `.local/adopts/` (~402MB).

## Snippets

> Integrate: diagram-design, code-graph-rag, t3code, CLIProxyAPI. Extract: weathernext, LifeOS, tookie-osint, iLEAPP. [Source: GitHub Repository Evaluation Plan.docx]
