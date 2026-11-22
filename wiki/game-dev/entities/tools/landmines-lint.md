---
title: "landmines — Oxlint rules that stop a test lying (MIT)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - "@ccc-wiki/concepts/agent-verification-patterns.md"
updated: 2026-11-22
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md, URL 20,
**Integrate** tier. Routed to game-time and atto.

The question this page answers: **how do you stop an agent from writing a test that
passes without testing anything?**

## Narrative

### What it does

An Oxlint plugin (`@interfere/landmines`, Oxlint v1.81+, Node 22.18+) with four rule
groups:

| Group | Rules |
|-------|-------|
| `landmines-testing` | `no-test-doubles`, `strict-msw`, `no-fixed-sleep`, `no-unsignaled-poll`, `no-flake-masking` |
| `landmines-style` | `no-comments` |
| `landmines-structure` | `colocated-tests`, `test-file-names`, `package-exports` |
| `landmines-types` | `no-explicit-return-types` |

### Why this is the right target

An agent under pressure to make CI green has four cheap moves, and all four produce a
green build that tests nothing:

1. **Mock the thing under test** — `vi.fn()` where the real dependency should run.
2. **Sleep and hope** — a fixed delay instead of waiting for the actual condition.
3. **Retry until green** — a Vitest retry that hides a flaky assertion.
4. **Loosen the timeout** — the same flake, slower.

For a deterministic simulation these are worse than useless. game-time's tick loop is
supposed to produce identical output for identical input; a mocked tick engine hides
exactly the desync the suite exists to catch.

### The adoption mechanism

`ratchet-down per-file allow counts`. Each existing violation is allowlisted with a
count, and the count may only decrease. Strict rules can land in a codebase that would
fail them today, without a flag day and without blocking delivery.

That is the detail worth copying even if the plugin is not adopted: **a ratchet makes a
strict rule adoptable**.

### Phase-0, 2026-11-22

| Check | Result |
|-------|--------|
| Licence | MIT [CONFIRMED — GitHub API] |
| Maturity | 705 stars, pushed 2026-11-18, 27 open issues |
| Cloud requirement | none — a local lint pass |
| Local gap | game-time ships vitest (`packages/sim-core/vitest.config.ts`, five test files) and **no oxlint** [CONFIRMED] |

atto also runs vitest through `apps/desktop`, so the same rules apply to the portal
suite.

### One rule to refuse

`landmines-style` enforces **no comments**. Applied literally that removes the comments
that explain a non-obvious invariant — the ones that matter. If this rule is adopted,
exclude it and keep the testing group.

### Status

Integrate. Queued for game-time and atto.

## Snippets

> Enforcing test honesty and anti-AI-slop lint rules.
> [`interfere-inc/landmines`, repository description, 2026-11-22]

## Dead Ends

- **Adopting `no-comments` wholesale.** It deletes the comments that carry a hidden
  constraint.
- **Enabling the testing rules without a ratchet.** The existing suite fails and the
  rule is turned off.
