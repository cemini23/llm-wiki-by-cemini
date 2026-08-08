---
title: "Eval — URL Revenue Opportunity Analysis 2026-08-08"
type: source
tags: [eval, phase-0, k227, atto, ccc, cyber]
keywords: [the-startup, sherlock, gosearch, omniparse, CyberStrike]
related:
  - entities/tools/the-startup.md
  - entities/tools/sherlock.md
  - entities/tools/gosearch.md
  - entities/tools/omniparse.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/active-project-research-routing.md
maturity: draft
created: 2026-08-08
updated: 2026-08-08
read_status: read
---

## Relations

- @entities/tools/the-startup.md
- @entities/tools/sherlock.md
- @entities/tools/gosearch.md
- @entities/tools/omniparse.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/active-project-research-routing.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | URL Revenue Opportunity Analysis.docx |
| sha256 | `4900f2236de209d1b0668fe97af22f775c825d26f5d1d2532f67ffbbb9f1c00f` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/URL Revenue Opportunity Analysis.docx` |
| retrieved | 2026-08-08 |
| read_status | read |

19-URL batch. **Never trust eval SPDX** — `gh api` overrides. TipDrop retired.

## Narrative

| # | Repo / URL | gh SPDX | Eval tier | Cemini verdict |
|---|------------|---------|-----------|----------------|
| 1–4 | flutter_roadmap / kotlin4noobs / Front-End-Checklist / realworld | MIT / … / **NOASSERTION** | Pass | **Pass** — no adopt. |
| 5,10–11,13–15,18–19 | LocalLLM / omni / deepwiki-rs / chatpack / taste-skill / pi-bifrost / soundshuman / floci | — | UNAVAILABLE | **Skip** — 404 / unavailable. |
| 6 | oyildirim/CyberStrike-OffSec-35B (HF) | model card | Extract → lab | **Watch / no download** — GGUF/VRAM; ethics floor; no HF blob into `.local/adopts/`. |
| 7 | sherlock-project/sherlock | **MIT** | Extract → OSINT/Atto | **GO Extract** — username footprinting for FIND deep-links. ~2.5MB. ToS/rate-limit caution. |
| 8 | rsmdt/the-startup | **MIT** | Integrate → CCC | **GO Integrate** — Claude Code SDD skills/commands. ~2.6MB. |
| 9 | ibnaleem/gosearch | **GPL-3.0** | Extract → Atto | **CONDITIONAL Extract** — GPL isolate; combo with sherlock for FIND. ~1.0MB. |
| 12 | hackers-arise OSINT guide | N/A | Context | **Context** — wiki-only. |
| 16 | freebuff.com | Proprietary | Context → CCC | **Skip** — proprietary file-export risk. |
| 17 | adithya-s-k/omniparse | **GPL-3.0** | Watch | **Watch REFERENCE** — GPL isolate; no product vendor. ~1.0MB. |

**Phase-0 ~7MB:** `the-startup`, `sherlock`, `gosearch`, `omniparse`. **Combo:** sherlock + gosearch → Atto FIND (human-gated; no mass ToS abuse).

## Snippets

> Integrate: rsmdt/the-startup. Extract: CyberStrike (HF), sherlock, gosearch. Combo: sherlock + gosearch → Atto FIND. [Source: URL Revenue Opportunity Analysis.docx]
