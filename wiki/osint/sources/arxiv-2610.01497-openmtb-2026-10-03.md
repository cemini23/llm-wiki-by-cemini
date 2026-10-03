---
title: "OpenMTB-Audit: over-refusal in clinical safety evaluation (2610.01497)"
type: source
tags: [source, k279, evaluation, safety, verifier]
keywords: [k279, over-refusal, label-collapse, audit, no-poc]
related:
  - concepts/k279-harness-wave.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
read_status: skimmed
---

## Relations

- @concepts/k279-harness-wave.md

## Raw Concept

| File | `arxiv-2610.01497-openmtb-audit-exposing-over-refusal-and-clinical.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.01497-openmtb-audit-exposing-over-refusal-and-clinical.pdf` |
| Archive | egress-fi 2026-10-03 |
| Retrieved | 2026-10-03 |
| sha256 | `a91786248bcabe239e8c26514898a4b0ce98f0d758590a2bde619d79b49a7eed` |
| Dual-ID | **OSINT K279** |
| arXiv | 2610.01497 |
| Authors | Negin Ashrafi, Jia Luo, Stacey M. Frumm, Roxana Daneshjou (Stanford; Dana-Farber/Harvard) |
| Repo | `https://github.com/Negiiinx/OpenMTB-Audit` |
| Venue | PSB 2027, oral |

## Narrative

A clinical safety-audit paper with a measurement technique that transfers well beyond medicine.

The setting is LLMs that audit molecular tumour board recommendations. The paper names a failure it calls **clinical over-refusal**: the model will not keep the middle label, "Partially Supported." It collapses to a binary safe-or-unsafe call.

### Why that matters

Here is the trap, in the authors' own numbers:

| Configuration | Safety Score | Accuracy |
|---------------|--------------|----------|
| Structured LLM baselines | 83.9 to 90.9 | 46.2% to 74.0% |
| Deterministic rule pipeline | 92.4 | 91.2% |

The LLM baselines score high on **safety** while scoring poorly on **accuracy**, because refusing or collapsing to the safe label inflates the safety metric. Across all LLM configurations, they failed to retain the middle label in **83.3% to 100%** of the cases that truly deserved it.

**A safety score can be gamed by refusing more.** If your eval has a safety axis and an accuracy axis, a degenerate answer can win one while losing the other, and an aggregate can hide that.

The deterministic seven-module pipeline, which makes no LLM calls, beat every LLM configuration on both axes. Its ablation shows where the value sits: removing the evidence-verifier module dropped the safety score by **55.0 points**.

### The transferable techniques

1. **Track the middle label.** A taxonomy with an "insufficient information" category catches label collapse that a binary does not.
2. **Report safety and accuracy separately.** Never let one aggregate number stand for both.
3. **A deterministic pipeline can beat an LLM judge on a well-specified task.** Worth reaching for before adding a model to a gate.

### Honest limits

The authors are careful. NSCLC only, 15 molecular profiles. Two models tested. The 50-case expert subset informed refinement, so concordance is post-refinement, not held-out. Labels, knowledge base, and decision rules share design provenance, so this is not independent clinical validation. Safety-score weights are harm judgements needing recalibration.

Harmful-request categories are named only, at headline level. Nothing operational appears on this page. **No PoC.**

Repo license not checked — operator directive for this wave. No clone.
