---
title: liberu-genealogy / genealogy-laravel
type: entity
tags: [tool, genealogy, dna, k157, extract]
keywords: [php-dna, Laravel, Filament, MIT, privacy]
related:
  - sources/eval-multi-wiki-link-evaluation-genealogy-agent-2026-07-10.md
  - concepts/computational-genealogy-archival-automation.md
maturity: draft
created: 2026-07-10
updated: 2026-07-10
---

## Relations

- @concepts/computational-genealogy-archival-automation.md — DNA module extract only
- @sources/eval-multi-wiki-link-evaluation-genealogy-agent-2026-07-10.md — K157 Extract

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [liberu-genealogy/genealogy-laravel](https://github.com/liberu-genealogy/genealogy-laravel) |
| **License** | MIT (~183★) [CONFIRMED Phase-0] |
| **Verdict** | **Extract** — isolate `php-dna` triangulation logic; **no** wholesale Laravel migration |
| **Risk** | Raw genomic data → strict local privacy; never commit DNA to wiki/git |

Full-stack genealogy app (Laravel 13 / Filament 5). Existing stack already uses Gramps/GEDCOM truth layer — extract DNA segment analysis modules only when paper-trail hypotheses need mathematical confirmation.

## Snippets

> "Extracting modules from genealogy-laravel introduces robust DNA segment analysis" [Source: eval docx URL 18 — paraphrase]
