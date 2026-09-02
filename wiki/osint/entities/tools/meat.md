---
title: "boldsoftware/meat"
type: entity
tags: [tool, phase-0, k220, ccc]
keywords: [meat, reading-diff, agent-review, apache-2.0]
related:
  - sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
harness_verb: FILE
---

## Relations

- @sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md — K220 eval parent
- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md — LICENSE file Apache-2.0 overrides API NOASSERTION

## Narrative

| Field | Value |
|-------|--------|
| **Repo** | https://github.com/boldsoftware/meat |
| **License** | **Apache-2.0** (LICENSE file; gh API NOASSERTION) [CONFIRMED 2026-08-03] |
| **Verdict** | **GO Extract** |
| **Local** | `.local/adopts/meat` (~1.2MB) |
| **Route** | CCC (ops time for Atto/GuruWatcher agent PR review) |
| **Stars / push** | ~579 / 2026-08-03 |

Go CLI that abridges git diffs into concept-level “reading diffs” for reviewing agent-written code. Steal into CCC review loop; scrub secrets/PII before sending Atto vault-adjacent diffs to any model backend.
