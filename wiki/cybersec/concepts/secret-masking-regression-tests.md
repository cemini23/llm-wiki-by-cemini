---
title: "Secret-masking regression tests — proving a redactor does not leak its own fixtures"
type: concept
related:
  - "@osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - concepts/api-security-audit-rubric.md
updated: 2026-11-24
maturity: draft
---

## Raw Concept

`safe-anything` (MIT) was graded Context in the 2026-11-24 batch for one specific idea:
how to test a secret-masking tool without the test itself becoming a leak. The question
this page answers: **what does a passing redaction test actually prove?**

Source: @osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md.

## Narrative

### The two failure modes

A redactor that hides secrets has two ways to be wrong, and they fail in opposite
directions:

- **Under-masking** — a real secret survives into the output. This is the one everyone
  tests.
- **Fixture leakage** — the test's own fake secrets look real enough to trip the
  rules, or trip a secret scanner in CI, or get committed.

The second is quieter and more common than it sounds. A test fixture containing a
well-formed AWS key is functionally a leaked-looking key: scanners flag it, reviewers
learn to ignore the scanner, and eventually a real one is missed.

### The design `safe-anything` encodes

1. **Assert no rule output leaks a fixture secret.** Every redaction rule gets a test
   that puts a fixture secret through it and checks the output.
2. **Build fake test tokens dynamically at runtime** — concatenate the pieces rather
   than writing a whole token in the source. A scanner reading the file sees fragments,
   not a key.

Step 2 is a two-line technique that costs nothing and removes a persistent source of
scanner noise.

### Where to apply it

Any project that handles credentials. For the federation the candidates are the
operator lab, Atto's Access-share path (which encrypts payloads and must never log a
key), and the CeminiParlays controls code that handles venue API keys.

The rule generalizes past secrets: **a test fixture must not trigger the alarms that
protect production.**

## Snippets

> Asserting no rule output leaks fixture secrets and building fake test tokens
> dynamically at runtime so fixtures avoid triggering scanners.
> [Source: Multi-Wiki Link Revenue Evaluation.docx, URL 20]

## Dead Ends

- **Writing a realistic key into a fixture.** It trains everyone to ignore the scanner.
