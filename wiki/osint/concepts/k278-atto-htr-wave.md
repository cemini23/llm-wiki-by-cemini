---
title: K278 Atto HTR Wave (Oct 2026)
type: concept
tags: [atto, htr, genealogy, k278]
keywords: [k278, pypottery, constraint-split, transkribus, FILE]
related:
  - concepts/k277-atto-htr-wave.md
  - sources/arxiv-2610.02072-pypottery-2026-10-02.md
  - sources/arxiv-2610.00633-genealogy-db-constraints-2026-10-02.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k277-atto-htr-wave.md
- @sources/arxiv-2610.02072-pypottery-2026-10-02.md
- @sources/arxiv-2610.00633-genealogy-db-constraints-2026-10-02.md

## Raw Concept

K278 Atto cluster hub for the **Atto** workstream (priority #1). Dual-ID **OSINT K278**. Prior @concepts/k277-atto-htr-wave.md.

## Narrative

Two papers. Neither replaces the product HTR path. **Transkribus stays the only product HTR.** Zero clones.

| Source | Contribution | Posture |
|--------|--------------|---------|
| 2610.02072 PyPottery | Cursive handwriting OCR plus few-shot field parsing, end to end | Closest analogue so far |
| 2610.00633 genealogy DB constraints | 19 of 210 business rules do not fit the schema; a validated front end carries them | Pattern note |

### The PyPottery numbers are useful planning figures

It runs the same two stages Atto needs: OCR over hand-drawn records, then parsing into structured fields.

| Measure | Result |
|---------|--------|
| OCR character error rate on cursive archaeology records | 6.2% |
| Parsing exact-match at 1 example | 13.56% |
| Parsing exact-match at 3 examples | 52.63% |
| Parsing exact-match at 10 examples | 67.60% |

**Read the few-shot curve before scoping any parsing work.** One example is nearly useless; the result roughly quadruples by three examples and needs about ten before it is dependable.

Its authors admit the same limits we would face: 300 DPI scans required, legible handwriting required, complex views still fail, and the source drawings cannot be released, so results are auditable but not re-runnable.

### The constraint split is the other durable idea

The genealogy database paper measured the problem. Of **210** business rules, **19** could not be enforced by the database engine. A validated front end carried **55** of them, split 17 relational and 38 non-relational.

That is the same shape as the Atto human-gated truth layer: a schema holds what it can, and a validated front end holds the rest. Two rules from that paper are directly reusable as a checklist class — lifespan bounds, and spouses alive together for at least one day.

**Cemini posture:** FILE and HITL only. No clone. No HTR swap. No `truth.ged` merge. No Barone PII. **0 product Integrate GO.**
