---
title: "Formal verification — faithfulness, validity, completeness"
type: concept
related:
  - sources/arxiv-turing-agent-formal-verification-mathematics-2611.21299.md
  - sources/newsletter-rss-latent-space-2026-11-20-the-war-against-slop-and-an-emerging-weapon-to-f.md
  - sources/newsletter-rss-latent-space-2026-11-21-ainews-riemann-hypothesis-provedtwice-independen.md
  - entities/tools/turing-agent.md
  - concepts/agent-completion-verification-gates.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: a proof checker accepted the artifact. What is still unverified?

Synthesised from three sources: `@sources/arxiv-turing-agent-formal-verification-mathematics-2611.21299.md` (2611.21299), the Latent Space formal-verification survey (2026-11-20), and the Riemann Hypothesis AINews issue (2026-11-21).

## Narrative

The Turing Agent paper splits automated formal verification into three failure conditions. The split generalises to any verifier, not just Lean.

1. **Faithfulness** — the formal statement must preserve the natural-language claim.
2. **Validity** — the code must pass the checker's syntax and type rules.
3. **Completeness** — the proof must discharge every obligation, with no `sorry` or equivalent bypass.

A harness that reports "verified" from a passing kernel check has tested validity and, at best, completeness. Faithfulness is a separate check against intent.

### The evidence for the gap

- The 2026-11 Latent Space survey of formal-verification vendors (Harmonic, Theorem, Axiom Math, &Truth) describes the SMT solver as the engine. A solver proves a property of an encoded model. The encoding is authored, so it can be wrong.
- The Riemann Hypothesis pair is the sharpest case. One proof was a Claude-driven Lean submission of about 1.3 GB; the other was a 940-page human proof. A Lean bug is judged unlikely, so a clean compile is probably correct — yet no human will read all of it. Correctness here means the statement that was checked is the statement intended, and almost nobody can confirm that by reading.
- The counter-example is OpenAI's September Navier-Stokes claim, criticised because the Lean proof did not match the natural-language result.

### Operating rule

For any verified artifact, record three things: the checker, the statement, and who confirmed the statement. A green check without the statement is half a verification.

Caveat: the Riemann and Navier-Stokes cases are news reports, not peer-reviewed findings. [NEEDS VERIFICATION 2026-11-22]

## Snippets

> "Faithfulness: The Lean statement may not faithfully capture the natural-language claim." [Source: arxiv-2611.21299-turing-agent-agentic-formal-verification-for-mat.pdf p.2]

> "If it finishes compiling with no extra axioms, it is probably correct, and no human will ever have read all of it." [Source: newsletter-rss-latent-space-2026-11-21-ainews-riemann-hypothesis-provedtwice-independen.md]
