---
title: "Eval — NFL Data Revenue Evaluation (K274)"
type: source
tags: [source, k274, eval, nfl, gambling]
keywords: [k274, CSOE, wind-penalty, closing-line, nfldata, FILE]
related:
  - concepts/k274-gambling-pm-wave.md
maturity: draft
created: 2026-09-27
updated: 2026-09-27
read_status: read
---

## Relations

- @concepts/k274-gambling-pm-wave.md

## Raw Concept

| File | `GitHub Repository Revenue Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repository Revenue Evaluation.docx` |
| Archive | egress-fi 2026-09-27 |
| Retrieved | 2026-09-27 |
| Dual-ID | **OSINT K274** |
| sha256 | `8b5ba32328a535d2f49f2e7b2ee4999ddd5b82cf5c39ba0f1999b1f11783aca8` |
| Theme | NFL data. Extracts: a CSOE name, a wind penalty, and closing lines |

gh api 2026-09-27 is the license source. The docx is not. The nflverse Integrate line is overridden. A null SPDX still records the pattern. No tree is cloned. **0 product Integrate GO.**

## Narrative

The operator override keeps the pattern and leaves each tree uncloned.

| Repo | SPDX | KB | Stars | Pattern to keep | Clone |
|------|------|----|-------|-----------------|-------|
| JorgeAcin/nfl-closing-speed-csoe | MIT | 6704 | 0 | Name: closing speed and CSOE as a projection adjustment. Formula unverified | no (size) |
| dfsstartinglineups/weathernfl | null | 12248 | 0 | Already K273. Add: wind penalty on passing and totals. Skip indoor and closed retractable games | no |
| nflverse/nfldata | null | 8258438 | 364 | Docx said Integrate. Override: null and huge. Pattern: schedule, games, closing spread, total | no |
| aschlafhauser/nfl-betting-data | null | 1211 | 2 | Historical closing spreads and totals for copula calibration | no |

A human still types the Hard Rock or FanDuel ticket. No auto-submit.

**Cemini posture:** these extracts sit on the gambling hub. FILE and HITL only. **0 product Integrate GO.**

## Snippets

> nflverse Integrate is overridden. SPDX is null and the tree is huge. The pattern is schedule, games, closing spread, and total. gh api 2026-09-27 overrides the docx. [Source: GitHub Repository Revenue Evaluation.docx; gh api 2026-09-27]
