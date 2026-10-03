---
title: "TRACE: trajectory return attribution for multi-turn safety (2610.01323)"
type: source
tags: [source, k279, safety, training, attribution]
keywords: [k279, trace, multi-turn, credit-assignment, FILE]
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

| File | `arxiv-2610.01323-trace-trajectory-return-attribution-and-contrast.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.01323-trace-trajectory-return-attribution-and-contrast.pdf` |
| Archive | egress-fi 2026-10-03 |
| Retrieved | 2026-10-03 |
| sha256 | `1d863f635b7152e5ebdf590ba98d49b7ef2fb8a4679571eeccfce2ebdf362699` |
| Dual-ID | **OSINT K279** |
| arXiv | 2610.01323 |
| Authors | Fengpeng Li, Kemou Li, Qizhou Wang, Haiwei Wu, Jiantao Zhou, Di Wang (KAUST PRADA Lab; Univ. of Macau; RIKEN AIP; UESTC) |

## Narrative

A training method, not a tool. Included for one transferable idea.

The problem it names: models that refuse a harmful single-turn request will often comply when the same goal is spread across several turns. The authors call it trajectory fragility, and argue that response-level objectives cannot bound multi-turn risk.

The method adds two terms to training — a discounted-return weighting that lets later refusal evidence reach back to earlier tokens, and a risk-localised erasure on the rejected response — plus a gradient penalty in place of a retain set.

### Numbers

Mean multi-turn attack success fell from 52.81% to 28.98% across five models and seven attacks, the lowest rate in all 35 model-and-attack pairs. On one model against one attack, 86.79% to 33.96%. Standard benchmarks dropped by at most 1.23 points. Removing the trajectory-weighting term raised the mean attack success back from 27.14% to 50.37%, which is the ablation that shows the term is doing the work.

### The transferable idea

**Discounted-return credit assignment for attributing a late outcome to early steps.** The scheme weights each earlier token by how much later evidence depends on it.

That is a general pattern for any run with a long horizon: when the end result is wrong, which earlier choice caused it? It is the same question the process-evaluation paper answers with a dependency graph, approached from the opposite direction. Ours would be a diagnostic, not a training objective.

### Honest limits

One attack family stays hard at 53.96% mean success across five models. The default setting **over-refuses 17.23% of safe prompts**, against 5.48% originally — so the fix buys safety with refusals. The bound does not establish a reduction against the base model. Training needs a refusal-ablated checkpoint.

No code URL. No clone. No PoC.
