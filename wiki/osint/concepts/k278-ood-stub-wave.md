---
title: K278 OOD Stub Wave (Oct 2026)
type: concept
tags: [ood, k278, eval]
keywords: [k278, eval-docx, license-drift, methodology, no-clone]
related:
  - concepts/k279-dfs-parlays-wave.md
  - concepts/k279-ood-stub-wave.md
  - concepts/k277-ood-stub-wave.md
  - sources/eval-repo-revenue-2026-10-02.md
  - sources/substack-rss-klement-2026-10-02-smoke-this-study-2026-10-02.md
maturity: draft
created: 2026-10-02
updated: 2026-10-03
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k279-dfs-parlays-wave.md
- @concepts/k279-ood-stub-wave.md
- @concepts/k277-ood-stub-wave.md
- @sources/eval-repo-revenue-2026-10-02.md
- @sources/substack-rss-klement-2026-10-02-smoke-this-study-2026-10-02.md

## Raw Concept

K278 cluster hub. Dual-ID **OSINT K278**. Prior @concepts/k277-ood-stub-wave.md.

## Narrative

Two items. Both are about **claim verification**, from opposite ends.

### The eval docx: four of twenty license claims failed

The wave's docx evaluated 20 repositories. Every license was then checked with `gh api` on 2026-10-02. Four claims did not survive:

| Repo | Docx claim | `gh api` |
|------|-----------|----------|
| sdcb/SimdPaddleOCR | MIT (claimed via dependency chain) | **Apache-2.0** |
| mksglu/context-mode | Elastic License 2.0 | **NOASSERTION** |
| getsentry/sentry | FSL-1.1-Apache-2.0 | **NOASSERTION** |
| cursor/plugins | MIT / Apache-2.0 (claimed) | **null** |

Two more rows carry a null or NOASSERTION SPDX with no docx claim. **A null SPDX records the pattern only.**

Four big repos were also size-skipped: impeccable 379 MB, hyperframes 488 MB, sentry 952 MB, three-gpu-pathtracer 954 MB.

This is the fourth wave where the eval overstated a license. The invariant stands: **never trust eval SPDX — `gh api` every adopt.**

### The Klement post: how a weak study is built

A study claimed a UK No Smoking Day stock-market anomaly. The tells, in order: a result significant only at the **10%** level, a structural break dated to **1991** and chosen from the same data, and significance rising to **5%** only after three controls were added.

**A significance level chosen after the fact is not evidence.** Three separate moves here should each stop a claim. Both items land on the same rule from different directions: verify the claim against the artifact, not against the claim itself.

**Cemini posture:** FILE. Zero clones. **0 product Integrate GO.**
