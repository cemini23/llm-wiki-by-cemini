---
title: "Bidirectional HAI skill evolution (BiHAA / ArtAnno)"
type: concept
tags: [skills, hai, k252, k225, atto, federation]
keywords: [BiHAA, ArtAnno, skill distillation, operator trajectories, AFTER]
related:
  - sources/arxiv-2608.05026-artanno-bihaa-2026-08-06.md
  - entities/tools/book-to-skill.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/verification-gated-persist-pivot-runtime.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
---

## Relations

- @sources/arxiv-2608.05026-artanno-bihaa-2026-08-06.md
- @entities/tools/book-to-skill.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/verification-gated-persist-pivot-runtime.md

## Raw Concept

K252 policy wire (federation) — OSINT copy emphasizes **Atto + wiki skill distillation**: operator research trajectories feed back into skills/KB, not one-way book→skill export. ArtAnno product **wont_wire** (art OOD).

## Narrative

**Problem:** One-way skill generation (`book-to-skill`, manual `/goal` exports) misses corrections discovered during real Atto sessions (PII gates, parish format edge cases, failed HTR paths).

**BiHAA loop:**

1. Operator executes task with agent + tools.
2. Failures/successes annotated inline (claim + locator, K233).
3. Reviewer gate admits distilled skill fragments (pairs K253 Argus reviewer — pattern only, no Argus clone).
4. Federation sync propagates vetted skills CCC ↔ OSINT (skill vetting / AFTER).

**Contrast:** `book-to-skill` = bulk corpus → skills; BiHAA = **trajectory-conditioned** refinement. Wire target: Atto regression-tax on any admitted skill; `@cybersecurity-wiki/` for lab-only offensive skills separately.

**Phase-1:** policy_wired in `cemini-phase1-policy-wires.mdc` K252 — no ArtAnno product install.

## Snippets

> Close the loop: operator trajectories distill into skills/KB — not one-way AI assist. [Policy K252]
