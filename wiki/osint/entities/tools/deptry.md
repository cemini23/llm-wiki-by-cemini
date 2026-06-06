---
title: osprey-oss/deptry — Python dependency hygiene CLI
type: entity
tags: [entity, tool, osint, python, adopt, k93]
keywords: [deptry, python-deps, unused-dependencies, mit]
related:
  - sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md
  - sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
  - concepts/cemini-wiki-ingest-workflow.md
maturity: validated
created: 2026-06-01
updated: 2026-06-06
phase_0_verdict: GO
license_verified: MIT
---

## Relations

- @sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md
- @concepts/cemini-wiki-ingest-workflow.md

## Raw Concept

K93 v5 Adopt; MIT verified 2026-06-01.

## Narrative

Finds unused/missing Python dependencies in `pyproject.toml` / requirements trees. **OSINT scripts/** hygiene during ingest gates — run in CI or pre-commit optional, not prod trading path.

**Phase-0 (K102):** K102 eval Defer (NO LICENSE claim) overturned — **MIT** confirmed; **1.4k★**, active Jun 2026. **GO** for `pip install deptry` on laptop + optional pre-commit on `scripts/`.

**Tier: Adopt** (laptop dev hygiene).
