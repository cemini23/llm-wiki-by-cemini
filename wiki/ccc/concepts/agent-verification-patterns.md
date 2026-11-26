---
title: "Agent verification patterns — property, differential, and mechanical audit ledgers"
type: concept
related:
  - sources/arxiv-scientific-coding-finite-element-analysis-2611.21176.md
  - concepts/self-verification-failure-taxonomy.md
  - "@osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - concepts/agent-completion-verification-gates.md
  - "@game-dev-wiki/entities/tools/fast-anything.md"
  - "@game-dev-wiki/entities/tools/landmines-lint.md"
  - concepts/agent-runtime-tooling-2026-11.md
  - concepts/prompt-engineering-evidence-discipline.md
updated: 2026-11-22
maturity: draft
---

Two sources from the 2026-11-17 batch describe how to check an agent's work without
reading all of it: a Claude Code team blog post, and a defect-discovery procedure from
the muse agent operations kit. The question this page answers: **what verification
catches an error that a passing test suite does not?**

Source: @osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md.

## Narrative

### Four patterns that catch different failures

**1. Property tests.** Instead of asserting one input gives one output, assert a
property that must hold for all inputs: encode-then-decode returns the original,
applying an operation twice equals applying it once, a cache never changes a result.

The highest-value form is **naive-versus-optimised equivalence** — write the slow
obvious version as the oracle, and assert the fast version agrees on random inputs.
That catches the optimisation bug, which is the one that ships.

Tooling: `fast-check` (JS), `Hypothesis` (Python), `proptest` (Rust).

**2. Differential testing.** Run the old implementation and the new one on the same
input and compare. The legacy code is the oracle. This is the cheapest way to refactor
something whose specification nobody wrote down.

**3. Base-branch-locked review.** An agent reviews against the base branch, not just
the diff in isolation. A diff that looks correct can break a caller three files away,
and the isolation is what hides it.

**4. Mechanical audit ledgers.** The muse defect protocol (Steps 0–7) requires:

- a **pre-read expectation model** — state what you expect the code to do *before*
  reading it, so a surprise is visible
- a **dependency ledger** and a **changed-function ledger** — enumerate, do not recall
- **value round-trip checks** across scope, process, and clock boundaries — what enters
  a queue, a child process, or a timer must come back unchanged
- **abnormal-input verification** — empty, enormous, negative, concurrent

### Why the expectation model is the strongest idea

Most review failure is not missing a line. It is reading the code and accepting
whatever it does as correct, because the reading creates the expectation. Writing the
expectation *first* turns review from "does this look right" into "does this match what
I said it would do", which is a real test.

That costs one sentence per function and catches the class of bug where the code is
internally consistent and wrong.

### Where these apply here

- **CeminiDFS** — property tests are the natural fit for a calibration or surface
  pipeline: round-trip and idempotency invariants are checkable without a reference
  price.
- **Collectibles** — value round-trip across the manifest boundary: an item that enters
  a grading run must come out with the same identity and grade.
- **game-time** — naive-versus-optimised equivalence on the tick loop.

### The `.cursor/rules` and CLAUDE.md angle

`disinfeqt/rulebook` (22 stars, MIT) is a small macOS app to find and edit CLAUDE.md
rules. It is a file editor, not a verification tool, but it points at the same problem
as @concepts/repeated-correction-mining.md: the rules file is unmanaged.

### Why nothing is queued

The blog is prose and the protocol is prose. Neither installs anything, so neither is
blocked — and neither needed a queue entry. They are reference, and they are complete
as reference.

## Snippets

> Property tests for round-trip encoding, invariants, idempotency, and
> naive-versus-optimised equivalence.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 17]

> A pre-read expectation model, dependency and changed-function ledgers, value
> round-trip checks across scope, process, and clock boundaries.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 6]

## Dead Ends

- **Reviewing a diff without stating an expectation first.** The expectation becomes
  whatever the code does.
- **Asserting example inputs only.** They pass, and the optimisation bug stays.
