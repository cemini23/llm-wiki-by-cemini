---
title: K279 OOD Stub Wave (Oct 2026)
type: concept
tags: [ood, k279, eval]
keywords: [k279, eval-docx, false-positive, recycled-title, no-clone]
related:
  - concepts/k280-ood-stub-wave.md
  - concepts/k278-ood-stub-wave.md
  - sources/eval-multi-repo-revenue-2026-10-03.md
  - sources/eval-repo-opportunity-2026-10-03.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k280-ood-stub-wave.md
- @concepts/k278-ood-stub-wave.md
- @sources/eval-multi-repo-revenue-2026-10-03.md
- @sources/eval-repo-opportunity-2026-10-03.md

## Raw Concept

K279 cluster hub. Dual-ID **OSINT K279**. Prior @concepts/k278-ood-stub-wave.md.

## Narrative

Two eval docs, 40 rows, and one tooling bug found.

### A false-positive duplicate in the checker

`preingest_check.py` flagged a Latent Space item as **DUPLICATE** by matching on **title alone** against two older pages. It is not a duplicate. Latent Space reuses the title "[AINews] not much happened today" for every slow news day, so title-only matching collides on a recurring feed.

The fix belongs in the checker: for a recurring-title feed, match on **URL or date**, not title. Until then, a title-only verdict on a newsletter needs a second look before it is trusted.

### The operator directive for this wave

Per the operator: stop auditing licenses row by row, and extract the technique. That is recorded here because it changes what these pages contain — the rows are now judged on **what is usable**, not on what the SPDX field says.

The judgement that matters is narrower and has not changed: if something is **vendored verbatim into shipped product code**, note it. Pattern extraction is unaffected.

### Where the useful rows landed

Most of the 40 rows were noise. The two that matter are filed on @concepts/k279-dfs-parlays-wave.md: the pick'em breakeven table and property-based testing of the de-vig and copula maths.

A third worth noting for other surfaces: **`pingdotgg/t3code`**, an agent control surface that isolates runs in git worktrees with remote approval before merge. Same shape as `/route`, with a review gate we do not have.

### Boundary

Zero clones. No installs. Nothing vendored.

**Cemini posture:** FILE. **0 product Integrate GO.**
