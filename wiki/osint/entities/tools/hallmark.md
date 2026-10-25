---
title: Hallmark (Nutlope) — anti-AI-slop design skill
type: entity
tags: [tool, design-skill, tipdrop, david, k163, adopt]
keywords: [hallmark, slop-test, Cursor skill, Claude Code skill]
related:
  - sources/eval-github-repo-revenue-evaluation-2026-07-14.md
  - concepts/wiki-tooling-evaluation.md
  - sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
maturity: draft
created: 2026-07-14
updated: 2026-10-25
---

## Relations

- @sources/eval-github-repo-revenue-evaluation-2026-07-14.md — K163 Extract → Adopt

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) |
| **License** | MIT (~5.7k★) |
| **Verdict** | **Adopt** — design skill for TipDrop/David UI (57 slop gates) |
| **Install** | `npx skills add nutlope/hallmark` (tiny) |

Verbs: build / `audit` / `redesign` / `study`. Complements taste-skill (K146); does not replace compliance-copy gates.

## Phase-0 re-audit — 2026-10-25

Re-evaluated as URL 2 of @sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md, tier **Integrate** (atto high, basgiath medium).

| Field | Value |
|-------|-------|
| **License** | MIT `[CONFIRMED]` by clone 2026-10-25 |
| **Last commit** | 2026-10-22 |
| **Size** | 122 MB / 820 files |
| **Stars** | 11.1k per report |
| **Verdict** | **GO** |

Structural check: `skills/hallmark/` holds `SKILL.md` plus about 18 reference files (`gates.md`, `responsive.md`, `texture.md`, …). `skills/hallmark/scripts/sloplint.mjs` and `sloplint-render.mjs` are both present. The photo catalog `skills/hallmark/scripts/photos.json` holds exactly 755 entries, confirming the report's figure.

**Correction to the report:** it cites the linter as `scripts/sloplint.mjs`. The real path is `skills/hallmark/scripts/sloplint.mjs`. A verification command built from the report's path would fail.

**Note:** the K163 verdict above names TipDrop/David. TipDrop is retired. The current target is Atto's customer portals, playbook pages (40/mo), kit (899), and concierge (>=$2,500), plus Basgiath showcase pages.

**PII guard:** when pointing the Puppeteer capture at a local Atto dev server, load only synthetic Rossi / 900-series SSN fixtures. Never capture `~/AttoVault/` or `Desktop/family/` into agent context.
