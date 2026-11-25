---
title: "FOL-Proof: verifying LLM text-to-logic translations (no SEO link)"
type: source
related:
  - concepts/corpus-overflow-out-of-scope.md
updated: 2026-11-25
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | FOL-Proof: Verifying LLM Text-to-Logic Translations via Deterministic Semantics |
| **Author** | Yisrael Clark, Guy Katz (The Hebrew University of Jerusalem) |
| **Type** | arXiv preprint (cs.CL) |
| **arXiv ID** | 2611.33078 |
| **Location** | `research to be indexed/seo/arxiv-2611.33078-fol-proof-verifying-llm-text-to-logic-translatio.pdf` |
| **Retrieved** | 2026-11-25 |
| **Pages** | 38 |
| **Read status** | read |

## Narrative

**Honest relevance: none.** This is a formal-methods paper about checking LLM translations from natural language into first-order logic. It does not touch search, citations, rankings, local listings, or content. It is recorded for corpus honesty only.

**The problem it solves.** A neuro-symbolic pipeline uses an LLM to translate a sentence into logic, then gives the formula to a solver. If the translation is wrong, the solver reasons correctly on bad input. LLMs commonly mistranslate: wrong quantifier, wrong scope, dropped or inverted negation, invented clauses.

**The method.** FOL-Proof builds an independent linguistic reading of the source sentence with tools such as the English Resource Grammar and Minimal Recursion Semantics. It then uses an SMT solver to test each candidate reading for logical equivalence against the LLM's formula. A faithful formula passes. A bad one is rejected or repaired. The check is conservative: an incomplete search or an inconclusive result yields abstention, not a false rejection.

**A finding worth noting outside the domain.** A human audit of auto-formalisation corpora found up to 48% of sentences have legitimate linguistic multiplicity. More than one formal reading can be correct. Grading against a single ground truth is therefore wrong by design.

**Why it is here.** The item landed in the SEO inbox because it is an LLM paper. It has no SEO application. Keep the record and move on.

## Snippets

> "incomplete search, unsupported constructions, or inconclusive checks yield abstention rather than false rejection." [Source: arxiv-2611.33078-fol-proof-verifying-llm-text-to-logic-translatio.pdf p.1]
