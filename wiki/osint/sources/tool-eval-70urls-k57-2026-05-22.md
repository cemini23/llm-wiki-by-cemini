---
title: "Multi-wiki tool eval (35 URLs) — K57 Gemini DR batch"
type: source
tags: [source, tool-eval, multi-wiki, license-verification, k57]
keywords: [tool-evaluation, open-design, flox, osiris, the-architect, no-license-found, agpl-poison]
related:
  - entities/tools/flox.md
  - entities/tools/osiris.md
  - concepts/cemini-license-posture.md
  - sources/more-links-5-2-arch-eval.md
maturity: draft
created: 2026-05-22
updated: 2026-05-22
---

## Relations

- @entities/tools/flox.md — URL 10 Adopt (MIT verified)
- @entities/tools/osiris.md — URL 21 eval Adopt **downgraded to Reject** after license re-check
- @sources/more-links-5-2-arch-eval.md — prior open-design steal-from note
- @concepts/cemini-license-posture.md — NO LICENSE FOUND false-positive pattern
- @sources/more-links-5-2-arch-eval.md — prior open-design steal-from note

## Raw Concept

- **Title**: Tool Evaluation and Wiki Fit.docx
- **Author**: Gemini Deep Research (multi-wiki eval)
- **Type**: tool-evaluation report
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/tool-eval-35urls-k57-2026-05-22.docx`
- **Retrieved**: 2026-05-22
- **Read status**: read

**Note:** Report title claims 70 URLs; extracted body contains **35 URL blocks** (URLs 1–35).

## Narrative

### Tier rollup (35 URLs in file)

| Tier | Count | OSINT action |
|------|-------|----------------|
| Adopt (eval) | 4 | 1 OSINT entity (`flox`); 3 cross-wiki only (`open-design`, `the-architect` → ccc; `osiris` **rejected** after verification) |
| Steal-from | 5 | Aggregate + cross-wiki briefs (no per-tool stub farm) |
| Reference-only | 1 | `lcso` (BlackRock, dormant) — mention only |
| Reject | 25 | Aggregated appendix below |

### License verification (2026-05-22, GitHub API)

| URL | Repo | Eval license | Verified |
|-----|------|--------------|----------|
| 4 | `nexu-io/open-design` | Apache-2.0 | **CONFIRMED** — CCC steal-from/adopt patterns |
| 10 | `FLOX-Foundation/flox` | MIT | **CONFIRMED** — OSINT Adopt-eligible |
| 21 | `simplifaisoul/osiris` | MIT | **RETRACTED** — `license: null`, no LICENSE file (same as K51) |
| 26 | `Hainrixz/the-architect` | MIT | **CONFIRMED** — CCC meta-agent brief |

### Adopt / Steal-from routing (no reject-stub farm)

**OSINT financial**

- `flox` — `@entities/tools/flox.md` (Phase-0 pending)

**CCC wiki** (briefs)

- `open-design` — modular skills / BYOK agent wiring (49k★)
- `the-architect` — Claude Code meta-agent blueprints
- `rag-from-scratch` — steal-from MIT tutorials

**Image-gen wiki** (brief)

- `Fooocus`, `PhotoGIMP` — GPL-3.0 steal-from patterns only

**Cybersec wiki** (brief)

- `sqlmap`, `NoSQLMap`, `Galaxy-Bugbounty-Checklist`, `open-source-web-scanners`, etc. — Reject/UNVERIFIED aggregate for methodology refs only

**Steal-from (financial, no entity stub)**

- `corral` (Hudson River Trading MIT) — concurrency patterns for async Python
- `Qbot` (UFund-Me MIT) — quant bot reference only

### Reject discipline

25 Rejects (AGPL/GPL poison, NO LICENSE FOUND, UNVERIFIED, Anna's Archive legal, duplicate `perspective` URL 15, etc.) are **not** given individual entity stubs. Re-verify any future Adopt interest via `gh api repos/{owner}/{repo}` before Phase-0.

## Snippets

> "Despite the eval's MIT claim, GitHub API returns license: null for simplifaisoul/osiris with no LICENSE file — K51 rejection stands." [Source: license verification 2026-05-22]
