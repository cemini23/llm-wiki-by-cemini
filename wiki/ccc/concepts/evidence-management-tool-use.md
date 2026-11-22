---
title: "Evidence management — tool use is not enough"
type: concept
related:
  - sources/arxiv-tune-medical-evidence-management-2611.25840.md
  - concepts/lossless-visual-memory-harness.md
  - concepts/harness-attribution-multimodal-eval.md
  - concepts/claim-centered-retrieval-with-provenance.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: once a tool returns the right artifact, what still has to happen before the answer improves?

Synthesised from one source: `@sources/arxiv-tune-medical-evidence-management-2611.25840.md` (TUNE, 2611.25840).

## Narrative

Most tool-use work optimises acquisition: call the right tool, get the right mask, the right search hit, the right diff. The TUNE paper argues acquisition is not the end. A harness must also manage what happens to the evidence.

Its benchmark, Mask-Evidence MedVQA, holds the mask fixed and varies only its rendering. Two effects appear:

- **Presentation changes behaviour.** The same correct mask, drawn differently, produces different answers.
- **Masks trade off.** A highlight can expose evidence the model missed and also create a wrong association. A ground-truth mask can fix one answer and break another.

TUNE therefore does three things: choose what evidence to acquire, choose how to present it, and decide whether to accept the answer update. It beats direct tool use by 9.1 points on average across seven benchmarks.

### Generalised rule

After any tool call, the harness owns three decisions:

1. **What** to fetch.
2. **How** to show it — full artifact, excerpt, summary, or nothing.
3. **Whether** the model may change its answer because of it.

For Cemini, a grep returns a file slice and a web search returns a snippet. Both are renderings. A bad rendering can make a correct retrieval harmful.

Caveat: one medical-imaging source. The transfer to text tools is an argument, not a measurement. [TENTATIVE]

## Snippets

> "Acquiring the right mask is not enough; an agent must also decide how to present the evidence and whether it should change the answer." [Source: arxiv-2611.25840-harnessing-medical-visual-language-models-with-a.pdf p.1]

> "Even a ground-truth mask can correct some answers while turning initially correct ones into incorrect ones." [Source: arxiv-2611.25840-harnessing-medical-visual-language-models-with-a.pdf p.1]
