---
title: "Never the Number: Structural Abstention for AI Systems Whose Answers Are Consumed as Fact (arXiv 2608.13926)"
type: source
tags: [arxiv, reliability, abstention, k240, guruwatcher, atto]
keywords: [structural-abstention, trusted-kernel, generative-shell, text-to-sql, fact-consumed]
related:
  - concepts/structural-abstention-trusted-kernel.md
  - concepts/guruwatcher-macro-watches.md
  - concepts/counterfactual-prompting-baselines.md
  - sources/arxiv-2608.14036-demystifying-agent-skills-2026-08-17.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
read_status: read
---

## Relations

- @concepts/structural-abstention-trusted-kernel.md — synthesized invariant
- @concepts/guruwatcher-macro-watches.md — dashboards must not return a fabricated number
- @concepts/counterfactual-prompting-baselines.md — K259 claim-validation pair (do not treat a fluent number as evidence)
- @sources/arxiv-2608.14036-demystifying-agent-skills-2026-08-17.md — same-day K240 skills paper

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.13926, "Never the Number: Structural Abstention for AI Systems Whose Answers Are Consumed as Fact" |
| Authors | Zhelun (Allen) Wu |
| Retrieved | 2026-08-17 |
| File | `arxiv-2608.13926-never-the-number-structural-abstention-for-ai-sy.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.13926-never-the-number-structural-abstention-for-ai-sy.pdf` |
| Type | cs.AI preprint, 26pp |
| Dual-ID | **OSINT K240** ingest. **CCC K240** = MixedComplementarityProblems.jl (old). Resolve by file+wiki. |

## Narrative

LLM text-to-SQL and dashboard agents fail in a way that matters at the point of use: a hallucinated column or a mis-aggregated total arrives as a fluent number that is indistinguishable from a correct one. Accuracy alone is insufficient because nothing marks which answers to distrust. The paper treats this as a **reliability** problem before it is an accuracy problem.

**Steal — perimeter invariant:** a component that can fabricate may influence *which question* the system answers, never *which value* it returns. A generative shell interprets underspecified input and phrases replies. A deterministic kernel matches a fully specified question against a bounded set of answerable shapes and compiles it. The two meet at a confirmation the user (or operator) reads before any value is computed. Requests the kernel cannot express are **declined**, not approximated. That is **structural abstention**: unanswerable = unrepresentable. No confidence estimate is required.

### Steal for Cemini

- **GuruWatcher / prod dashboards / tool-using agents** that return numbers consumed as fact must not let a generative shell pick the value.
- Confirm the question shape before compute. Decline unrepresentable questions.
- Extends from returned values to executed actions: a component that can fabricate may propose *which* action, never *which* action is executed.
- Pairs K259 claim-validation: a fluent number is not evidence.

Tier: `[TENTATIVE]` — single-author production case study (Apple 2021–2024 disclosure). Methodology is directly actionable even if the two-year case numbers are not independently audited.

## Snippets

> "A component that can fabricate may influence which question the system answers. It may never influence which value the system returns." [Source: arxiv-2608.13926 p.2]

> "Refusal here needs no confidence estimate, because unanswerable requests are unrepresentable." [Source: arxiv-2608.13926 abstract]
