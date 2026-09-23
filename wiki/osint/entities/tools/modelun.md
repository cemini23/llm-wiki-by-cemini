---
title: modelun (SPDX null — NO-CLONE)
type: entity
tags: [tool, k270, harness, FILE]
keywords: [modelun, SPDX-null, size-skip]
related:
  - concepts/k270-harness-evolution-wave.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
phase_0_verdict: FILE NO-CLONE
harness_verb: FILE
wire_status: wont_wire
wire_note: SPDX null. About 21MB. No clone. 0 Integrate GO.
---

## Relations

- @concepts/k270-harness-evolution-wave.md

## Raw Concept

K270 Phase-0 — `gh api` on 2026-09-23. SPDX license field is **null**. Size is about **21MB**.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | modelun |
| **License** | **SPDX null** |
| **Size** | about 21MB |
| **Local** | none — **no clone** |
| **Verdict** | **FILE NO-CLONE. `wont_wire`.** |

**Posture:** a null SPDX field blocks a clone under `cemini-license-posture`. Never trust an eval SPDX claim. Do not clone. Do not vendor. **0 product Integrate GO. Never `npx github:`.**
