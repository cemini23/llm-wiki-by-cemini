---
title: "Continuous process-level evaluation for evolving agent skills (2610.01833)"
type: source
tags: [source, k279, agents, evaluation, harness]
keywords: [k279, process-eval, trace, regression, FILE]
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

| File | `arxiv-2610.01833-continuous-process-level-evaluation-for-evolving.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.01833-continuous-process-level-evaluation-for-evolving.pdf` |
| Archive | egress-fi 2026-10-03 |
| Retrieved | 2026-10-03 |
| sha256 | `07743dbff2f0a3e697546b0fc9e6b659d543a2c7f6a1030dcccb31d8ff4b0b78` |
| Dual-ID | **OSINT K279** |
| arXiv | 2610.01833 |
| Authors | Ngoc Phuoc An Vo, Vadim Sheinin (IBM); Aarya Doshi (Georgia Tech) |
| Venue | NeurIPS 2026 workshop CLEA |

## Narrative

The strongest paper in this wave. It measures how much a passing final result hides.

The setting is enterprise agent skills that get revised continuously — tool APIs change, specs change, the model version changes, the harness changes. The authors argue that checking only the final output misses behavioural drift inside the run.

The method is a five-stage pipeline that runs **independently of the agent**:

1. Capture and parse the tool-call trace.
2. Compute ground truth by calling the **same real APIs separately**.
3. Materialise template tests whose placeholders resolve at runtime from that ground truth.
4. Evaluate outcome and process — tool selection, arguments, ordering, scope, database integrity — with rule-based checks plus a narrow LLM judge.
5. Attribute root failures through a dependency graph.

### The numbers

| Measure | Result |
|---------|--------|
| Runs passing all final numerical checks | 175 |
| Of those, runs that still had at least one process deviation | **162 (92.6%)** |
| Under seven final-state checks, passing runs that violated a trajectory check | 151 of 164 (92.1%) |
| Runs failing at least one check, overall | 227 of 240 (94.6%) |
| Root-cause compression | mean 6.34 failed checks reduced to 2.65 roots (58%) |
| Recorded cost | $859.34 total, $3.58 per run |

**Read the first two rows together.** A final-output check passed 175 runs. A process check then found that 162 of those same runs had a deviation anyway. If you only score the answer, you certify roughly 93% of runs that took a wrong path.

That is the fourth independent confirmation this quarter of the same rule, arriving from a different direction. K276 found it in traces. K277 found it in summaries. K278 found it in state. This one finds it in tool-call trajectories.

### The transferable machinery

Three design choices are worth copying:

1. **Ground truth comes from an independent call to the same API**, not from the agent's account of what it did.
2. **Template tests resolve their placeholders at runtime**, so they survive API changes without a rewrite.
3. **Dependency attribution** collapses a pile of failed checks into a few root causes. That is what makes the output actionable rather than a wall of red.

The authors admit the limits. One system, two related skills, 10 trials per cell. The aggregate score encodes no severity. 83 of 240 runs contain an execution error. The live-API ground truth can drift between the run and the evaluation. And their judge model is also one of the models under test — a possible self-preference bias, which they flag themselves.

The framework diagnoses but does not repair.

No code URL. No clone. This is the design reference for our own gate work.
