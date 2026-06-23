---
title: AOHP — Android Open Harness Project
type: entity
tags: [entity, tool, agent-harness, mobile, aosp, k127]
keywords: [aohp-os, AOHP, AOSP, Apache-2.0, agent-native OS]
related:
  - sources/arxiv-aohp-os-agent-harness-2606.23449-2026-06-23.md
  - concepts/aohp-os-level-agent-harness.md
  - concepts/code-as-agent-harness.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-06-23
updated: 2026-06-23
---

## Relations

- @sources/arxiv-aohp-os-agent-harness-2606.23449-2026-06-23.md — technical report + eval claims
- @concepts/aohp-os-level-agent-harness.md — pattern synthesis

## Raw Concept

GitHub: https://github.com/aohp-os/aohp — AOSP-based agent-native OS harness (Tsinghua/PKU/HKU).

## Narrative

**Phase-0 (2026-06-23):**

| Signal | Value |
|--------|-------|
| License | **Apache-2.0** |
| Stars | ~43 |
| Last push | 2026-06-23 |
| Substrate | AOSP fork — heavy build, not laptop default |

**Posture:** **CONDITIONAL-GO** — architecture reference for CCC secure-agent-interfaces brief. Do not flash devices or integrate into cemini-prod. Study docs + information-flow module design only.

## Snippets

> Source Code: https://github.com/aohp-os/aohp [Source: arXiv:2606.23449 (retrieved 2026-06-23)]

## Dead Ends

- Mobile OS research artifact ≠ Cemini trading stack.
- OpenClaw mobile eval substrate may not generalize to Cursor MCP.
