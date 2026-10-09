---
title: open-code-review — Alibaba code review (Apache-2.0)
type: entity
tags: [tool, k262, ccc, apache]
keywords: [open-code-review, Alibaba, FILE]
related:
  - concepts/k262-eval-github-wave.md
  - concepts/k262-ccc-harness-wave.md
  - sources/eval-repository-revenue-2026-09-16.md
  - sources/eval-multi-repo-revenue-2026-10-09.md
maturity: draft
created: 2026-09-16
updated: 2026-10-09
phase_0_verdict: GO REFERENCE
harness_verb: FILE
wire_status: wont_wire
wire_note: REFERENCE clone. CCC FILE. Do not swap /route.
---

## Relations

- @concepts/k262-eval-github-wave.md
- @concepts/k262-ccc-harness-wave.md
- @sources/eval-repository-revenue-2026-09-16.md
- @sources/eval-multi-repo-revenue-2026-10-09.md — K287 refresh. Pattern is not new. No brief.

## Raw Concept

K262 Phase-0 on [alibaba/open-code-review](https://github.com/alibaba/open-code-review).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/alibaba/open-code-review |
| **License** | Apache-2.0 `[CONFIRMED]` gh api 2026-09-16 |
| **Local** | `.local/adopts/open-code-review` |
| **Stars** | 30,479 (2026-09-16). **45,129** on 2026-10-09. Last push 2026-10-08. |
| **Size** | ~52MB git |
| **Verdict** | **GO REFERENCE** FILE. **0 Integrate GO.** |

CCC FILE. Do not swap `/route`.

### K287 refresh (2026-10-09)

Phase-0 clone is `/tmp/k287-phase0/open-code-review` only. `gh api` still reports **Apache-2.0**. The docx tier is Extract. The pattern (deterministic filter, then an LLM comment) is already this page. No new brief. `wire_status` stays `wont_wire`. No install.
