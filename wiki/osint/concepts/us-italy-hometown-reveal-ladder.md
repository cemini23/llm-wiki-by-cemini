---
title: US→Italy hometown reveal ladder
type: concept
tags: [concept, genealogy, us-italy, immigration, k180, draft]
keywords: [comune, Ellis, Steve Morse, naturalization, draft card, SS-5, USCIS, IGG, deep-link]
related:
  - sources/gemini-italian-american-genealogy-sources-2026-07-21.md
  - sources/gemini-italian-place-name-resolution-2026-07-21.md
  - concepts/antenati-deep-link-grammar.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - entities/tools/steve-morse-census-tools.md
maturity: draft
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- @sources/gemini-italian-american-genealogy-sources-2026-07-21.md — primary DR (K180)
- @sources/gemini-italian-place-name-resolution-2026-07-21.md — phonetic / soppressi after string found
- @concepts/antenati-deep-link-grammar.md — next hop once comune known
- @entities/tools/steve-morse-census-tools.md — One-Step forms
- @concepts/italian-regional-genealogy-archive-playbook.md — Italian archive routing
- @concepts/computational-genealogy-archival-automation.md — US staging step
- @concepts/gpuology-genealogy-agent-kit.md — Atto FIND checklist copy

## Raw Concept

Ranked browser-pointer ladder to turn “Italy” / anglicized names into an exact *comune* string — for privacy-first local kits (open URL only; no PII to external AI).

## Narrative

### Ordered steps (done-when = exact town)

| Rank | Source class | Why | Watch failure modes |
|------|--------------|-----|---------------------|
| 1 | Passenger (post-1906) + Steve Morse White/Gold | Birthplace + 1907+ page-2 relative | Pre-1906 last residence ≠ birth; page-2 miss; maiden names |
| 2 | Naturalization Declaration then Petition (post-1906) | Standardized birthplace | Pre-1906 vague; never naturalized; derivative citizenship |
| 3 | WWI draft / WWII Old Man’s Draft (1942) | Captures non-citizens | Phonetic contortion of town names |
| 4 | SS-5 / Numident FOIA | Hometown on application | Delay / fee; living-person care |
| 5 | USCIS Genealogy / A-files | Consolidated immigration file | Request latency |
| 6 | NYC/NJ vitals (IGG etc.) | Local indexes when metro | Not national |

### Product rule

Deep links + checklist only. Operator browses; tool organizes notes. Exact comune → @concepts/antenati-deep-link-grammar.md → vault intake → human Approve.
