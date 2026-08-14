---

title: "Vero — repository-level verified code generation benchmark (Lean 4)"
type: entity
tags: [tool, formal-verification, lean4, benchmark, ccc, k237]
keywords: [Vero, Lean 4, verified code, benchmark, code-and-proof, proof-only, repository-level]
related:
  - sources/arxiv-2608.13522-vero-2026-08-14.md
  - concepts/ai-assisted-formal-verification.md
  - sources/eval-url-revenue-opportunity-2026-08-14.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14

---

## Relations

- @sources/arxiv-2608.13522-vero-2026-08-14.md — the paper (2608.13522)
- @concepts/ai-assisted-formal-verification.md — K233 umbrella, Vero is a major update

## Raw Concept

What prompted this page: K237 paper 2608.13522 describes Vero; Phase-0 verified `sunblaze-ucb/vero` via gh api: **Apache-2.0**, 1.9MB → cloned to `.local/adopts/vero` (14MB).

## Narrative

Vero is the first **repository-scale** benchmark for verified code generation in Lean 4: 43 instances from real-world repos (Python, Dafny, Verus, Coq → Lean 4), 743 APIs + 2,705 specs, with two evaluation modes (proof-only / code-and-proof), a formal audit mechanism (disprove_/unsat_/joint_unsat negative-evidence slots), and an anti-cheat grader (slot-scoped re-rendering, axiom allowlist, `@[implemented_by]`/typeclass-hollow screening). Runs agents via `vero run benchmark=<id> agent=claude mode=proof`.

### Steal-for-CCC / code-review skill

- Directly benchmarks Claude Code + Codex → usable as a **stress test for agent-harness changes** (tool access, reasoning effort, loop control).
- **Spec-to-verification review workflow** + negative-evidence checklist (code vs single-bad-spec vs mutually-inconsistent-specs).
- **Formal-methods vulnerability classes to scan for**: axiom injection / `sorry` leakage, `native_decide`, `@[implemented_by]` proof/runtime split, typeclass decidability laundering.
- Curation-as-skills pattern (discover/select/plan/translate/validate, human-gated).

Apache-2.0, small — clean to reference. Tier: `[TENTATIVE]`.
