---
title: jev-browser — Jev browser recorder (MIT)
type: entity
tags: [tool, k264, atto, mit, browser]
keywords: [jev-browser, HITL, cassette, Antenati]
related:
  - concepts/k264-atto-wave.md
  - concepts/k264-eval-github-wave.md
  - sources/eval-deep-research-url-stack-2026-09-18.md
  - entities/tools/jev-ultrafast.md
maturity: draft
created: 2026-09-18
updated: 2026-09-18
phase_0_verdict: GO REFERENCE
harness_verb: FILE
wire_status: wont_wire
wire_note: REFERENCE clone ~10MB. HITL browser cassette only. No unattended portal scrape. No Antenati mass scrape.
---

## Relations

- @concepts/k264-atto-wave.md
- @concepts/k264-eval-github-wave.md
- @sources/eval-deep-research-url-stack-2026-09-18.md
- @entities/tools/jev-ultrafast.md

## Raw Concept

K264 Phase-0 on [jkudish/jev-browser](https://github.com/jkudish/jev-browser). SPDX timed out during the parent pass; a live `gh api` retry on 2026-09-18 returned MIT. Clone proceeded after that confirmation.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/jkudish/jev-browser |
| **License** | MIT `[CONFIRMED]` gh api 2026-09-18 (live retry) |
| **Local** | `.local/adopts/jev-browser` |
| **Stars** | 57 (2026-09-18) |
| **Size** | ~10MB git |
| **Verdict** | **GO REFERENCE** FILE. HITL cassette only. **No unattended portal scrape. No Antenati mass scrape. 0 product Integrate.** |

Same family as @entities/tools/jev-ultrafast.md: browser automation for human-in-the-loop cassettes. Never run unattended against a genealogy portal.
