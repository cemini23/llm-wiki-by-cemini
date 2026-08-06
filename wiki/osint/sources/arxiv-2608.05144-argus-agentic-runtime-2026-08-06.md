---
title: "arXiv 2608.05144 — Argus agentic runtime (K253)"
type: source
tags: [arxiv, agents, memory, k253, k225, no-go]
keywords: [Argus, persist, pivot, verification-gated, lbx154]
related:
  - concepts/verification-gated-persist-pivot-runtime.md
  - sources/arxiv-2608.05026-artanno-bihaa-2026-08-06.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
read_status: skimmed
---

## Relations

- @concepts/verification-gated-persist-pivot-runtime.md
- @sources/arxiv-2608.05026-artanno-bihaa-2026-08-06.md — complementary skill loop (K252)

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Argus: A General-Purpose Agentic Runtime for Long-Horizon Tasks |
| arXiv | 2608.05144 |
| Repo | https://github.com/lbx154/Argus |
| gh SPDX | **NULL** (pyproject MIT claim insufficient) |
| sha256 | `f0be39ca1b9d658c2acb7eaf6b0193cbbe6b05f046888f6d4cb5a6bd0d90ac8f` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.05144-argus-a-general-purpose-agentic-runtime-for-long.pdf` |
| retrieved | 2026-08-06 |
| read_status | skimmed |

## Narrative

**Argus** separates Manager/Planner/Engineer from an independent Reviewer; admits memories/skills only after review; **persist while evidence supports, pivot on measured failure** — K253 policy wire in `.cursor/rules/cemini-phase1-policy-wires.mdc`.

**Clone verdict: NO-GO** — `lbx154/Argus` has **NULL SPDX** on GitHub; do not clone until LICENSE/SPDX present. Steal pattern into `@concepts/verification-gated-persist-pivot-runtime.md` and federation `/goal` sessions only.

## Snippets

> Verification-gated admission of durable state across long-horizon agent runs. [Source: arxiv-2608.05144-argus-a-general-purpose-agentic-runtime-for-long.pdf — skim]

> **NO-GO clone:** gh api confirms NULL license on lbx154/Argus — wont_wire runtime. [Phase-0 K225]
