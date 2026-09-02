---
title: "Aliens_eye — username OSINT classifier (MIT Extract)"
type: entity
tags: [tool, osint, k242, mit, extract]
keywords: [aliens-eye, username, sherlock, osint]
related:
  - sources/eval-project-revenue-url-2026-08-19.md
  - concepts/cemini-license-posture.md
  - entities/tools/sherlock.md
maturity: draft
created: 2026-08-19
updated: 2026-08-19
harness_verb: FILE
wire_note: Human-gated username OSINT; ToS; no Barone PII
---

## Relations

- @sources/eval-project-revenue-url-2026-08-19.md — K242 eval
- @concepts/cemini-license-posture.md
- @entities/tools/sherlock.md — username sibling (K227/K241)

## Raw Concept

K242 Phase-0 Extract. Clone `.local/adopts/Aliens_eye` (~1.3MB). https://github.com/arxhr007/Aliens_eye

## Narrative

| Field | Value |
|-------|--------|
| License | **MIT** [CONFIRMED gh 2026-08-19] |
| Local | `.local/adopts/Aliens_eye` |
| Verdict | **Extract** |
| wire_status | `policy_wired` |

Username presence checker that uses DOM / OpenGraph features plus a classifier rather than HTTP status codes alone. Authorized whitehat / FIND-style lookups only. Human-gated. Respect platform ToS and rate limits. Never put Barone or living-person handles in git fixtures.

## Snippets

> Aliens_eye MIT Extract. Human-gated. [Source: `.local/reports/license-k242-2026-08-19.md`]
