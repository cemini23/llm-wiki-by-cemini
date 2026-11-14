---
title: "Silent error rate: the metric for parsed output that reaches the customer"
type: concept
related:
  - sources/arxiv-parsed-plausible-wrong-output-format-2611.17169.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - sources/arxiv-nfr-to-hyperparameter-quantum-2611.16902.md
  - concepts/provider-refusal-measurement-contamination.md
updated: 2026-11-14
---

## Raw Concept

Question: **which metric should rank a parser that acts on machine output?** From arXiv 2611.17169 (ITMO University).

## Narrative

A structured-output parser has two failure modes that look the same to a benchmark and completely different to a caller. One produces output that does not parse. The other produces output that parses into a plausible but wrong value. The first is visible. The second is silent.

### The four-way split

Every item ends in exactly one of four outcomes. The split should be reported for every parser evaluation:

| Symbol | Outcome | Who absorbs it |
|---|---|---|
| A | Correct | — |
| S | **Silent** — parses, wrong | **Nobody: it ships** |
| D_parse | Does not parse | Retry loop |
| D_refuse | Refuses valid input | Human fallback |

`A + S + D_parse + D_refuse = 1`. Exact match alone hides `S` inside its complement.

### Why exact match misranks

A format that always parses converts its errors into silent ones. A format that fails to parse converts the same errors into visible ones. Two formats can have equal exact match and very different deployment risk.

Measured on PIZZA with two sub-billion models:

| Metric | Symbolic native format | Plain-words format |
|---|---|---|
| Exact match | 85.8% | 87.5% |
| Silent rate | 10.3% | 4.5% |
| Unparseable | 0.6% | 4.6% |

The plain-words format has 2.3× fewer silent errors and pays with more visible parse failures. The paper treats this as the right trade, because the retry loop catches the visible class and nothing catches the silent class.

### Surface form beats length

The intuitive rule — fewer output tokens, fewer errors — fails. A length ladder from 44.3 to 10.9 tokens is not monotone. Renaming constructors to single letters costs 10.6 accuracy points. Two matched-length pairs isolate the mechanism: writing the target in ordinary words helps, and shortening does not.

The reason is pretraining. Markers such as `+cheese` split into more subwords than `extra cheese`, so natural words reuse more of what the model already learned.

### Refusal has a price

A strict refusal guardrail refuses 2.1–10.1% of genuine input. The refused items are mostly polite human phrasing absent from the training grammar. Refusal is a legitimate control, but its cost belongs in the same table as its benefit.

### Rules for agent tooling

1. Report all four outcomes. Never report exact match alone for a shipped parser.
2. Measure the silent rate separately for the error class that matters. In this benchmark, negation carries most of the gap.
3. Validate the value against the request, not only the schema. Constrained decoding removes parse errors and cannot touch silent errors.
4. Count refusals of valid input as a cost line, not as an error.

The same logic applies to function calls from an agent. A tool call with a valid signature and a wrong argument is the dangerous case, because the harness has no signal to retry.

### Limits

One benchmark, two small models, one task. The four-way split is portable. The size of the format effect is not yet established on larger models.

## Snippets

> "A format with higher A but higher S ships more wrong orders." [Source: arxiv-2611.17169-parsed-plausible-wrong-output-format-controls-si.pdf p.6]

> "WORDS has the lowest S: 4.5% against 10.3% for EXR on Qwen, a ratio of 2.3." [Source: arxiv-2611.17169-parsed-plausible-wrong-output-format-controls-si.pdf p.4]
