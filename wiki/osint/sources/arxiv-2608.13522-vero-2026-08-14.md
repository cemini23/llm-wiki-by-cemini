---
title: "Vero — Can AI Agents Build Formally Verified Software Repositories? (arXiv 2608.13522)"
type: source
tags: [arxiv, formal-verification, lean4, agent-benchmark, ccc, code-review, k237]
keywords: [Vero, Lean 4, verified code generation, repository-level benchmark, code-and-proof, proof-only, anti-reward-hacking]
related:
  - concepts/ai-assisted-formal-verification.md
  - concepts/generator-verifier-inference-time-steering.md
  - entities/tools/vero.md
  - sources/arxiv-2608.13560-autodesign-2026-08-14.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
read_status: read
---

## Relations

- @concepts/ai-assisted-formal-verification.md — K233 umbrella, Vero is a major update
- @concepts/generator-verifier-inference-time-steering.md — verification-as-feedback lineage
- @entities/tools/vero.md — Phase-0 clone (Apache-2.0, 1.9MB)
- @sources/arxiv-2608.13560-autodesign-2026-08-14.md — harness-optimization sibling

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.13522, "Vero: Can AI Agents Build Formally Verified Software Repositories?" |
| Authors | Zhe Ye, Hantao Lou, ..., Dawn Song (UC Berkeley, U Chicago, Caltech, Stanford, Apodex, AWS) |
| Retrieved | 2026-08-14 |
| File | `arxiv-2608.13522-vero-can-ai-agents-build-formally-verified-softw.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` |
| Type | cs.LG preprint, 31pp |

## Narrative

First **repository-scale** benchmark for verified code generation in Lean 4: agents jointly implement APIs AND prove machine-checked specs across real multi-module codebases. 43 instances from real-world repos (Python, Dafny, Verus, Coq → translated to Lean 4), **743 scored APIs, 2,705 scored specs**. Two modes: **proof-only** (reference impl supplied, agent proves every spec) and **code-and-proof** (agent writes impl + proof). Anti-cheat: slot-scoped re-rendering at grade time, axiom allowlist (only Classical.choice / propext / Quot.sound), `sorry`/`native_decide`/`@[implemented_by]` rejection.

### Key results

- GPT-5.5 (xhigh) solves **27/43** code-and-proof, 25/43 proof-only; Claude Opus 4.8: 8/10; **10 instances resist all eight configs** — frontier-resistant.
- Per-spec coverage high (87.3% cp) but does NOT imply repository completion.
- **Helper-chain depth predicts failure**: no-helper specs pass 83.9% (cp), depth-4+ drop to 50.6%. Agent-written helpers carry median 73.6% of proof lines in full solves.
- Implementation freedom helps only the strongest: 5 audited pairs where agent substituted a simpler algorithm closed all 250 specs vs 201 (munkres 409-line Hungarian → 164-line permutation enumeration). Full solve certifies spec compliance, **not complexity**.
- Costs: GPT-5.5 xhigh ~$2,865 total, **$106/full solve**; xhigh ×3.1 spend → ×13.5 full solves. 23% of spend went to the 10 unsolved instances. Ensemble buys nothing at repo level.
- Audit mechanism found 38 adjudicated spec defects across 9 instances during curation (47.4% mistranslation, 44.7% missing domain condition); second auditor added only 5 cases.
- **Harness-loop lesson**: agents commit to an implementation early and grind on proofs; when a bridging lemma repeatedly fails, the loop never revisits the implementation. A harness that reconsidered the definition rather than the tactic would collapse 16 attempts into one edit.

### Steal-for-CCC / code-review skill

- **Spec-to-verification review workflow**: check impl against spec AND cross-module coherence ("revising an implementation can invalidate proofs throughout the repository"). Flag local proofs of global properties (existence-and-coverage specs fail 47.1%).
- **Negative-evidence checklist** from the audit mechanism: when a spec can't be proved, is it the code, a single bad spec, or a mutually inconsistent spec set? (disprove_ / unsat_ / joint_unsat).
- **Vulnerability classes to scan for**: axiom injection / `sorry` leakage, `native_decide` (compiler-evaluated vs kernel-checked), `@[implemented_by]` splitting proof target from runtime, hollow/priority-shadowed typeclass instances, decidability laundering.
- **Curation-as-skills**: multi-stage LLM pipeline (discover/select/plan/translate/validate) built from modular agent skills with human gates — reusable CCC skill-design pattern.

**Briefs:** CCC `/route` (Vero + AutoDesign + skill misevolution). Tier: `[TENTATIVE]` — preprint, but benchmark + anti-cheat layer are concrete and reusable.
