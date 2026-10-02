---
title: K277 Harness Evolution Wave (Oct 2026)
type: concept
tags: [agents, harness, k277, ccc]
keywords: [k277, minimal-harness, turbo-harness, scholarevolve, FILE]
related:
  - concepts/k278-harness-wave.md
  - concepts/k276-harness-evolution-wave.md
  - sources/arxiv-2609.40303-minimal-harness-2026-10-01.md
  - sources/arxiv-2609.40306-dynaharness-2026-10-01.md
  - sources/arxiv-2609.40330-turbo-harness-2026-10-01.md
  - sources/arxiv-2609.40169-scholarevolve-2026-10-01.md
  - sources/arxiv-2609.40324-cogentic-2026-10-01.md
  - sources/substack-rss-klement-2026-10-01-flippin-heck.md
  - sources/newsletter-rss-latent-space-2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-ope.md
  - sources/newsletter-rss-latent-space-2026-10-01-ainews-gemini-4-argon-gdms-answer-to-astrafable.md
maturity: draft
created: 2026-10-01
updated: 2026-10-02
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k278-harness-wave.md
- @concepts/k276-harness-evolution-wave.md
- @sources/arxiv-2609.40303-minimal-harness-2026-10-01.md
- @sources/arxiv-2609.40306-dynaharness-2026-10-01.md
- @sources/arxiv-2609.40330-turbo-harness-2026-10-01.md
- @sources/arxiv-2609.40169-scholarevolve-2026-10-01.md
- @sources/arxiv-2609.40324-cogentic-2026-10-01.md
- @sources/substack-rss-klement-2026-10-01-flippin-heck.md
- @sources/newsletter-rss-latent-space-2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-ope.md
- @sources/newsletter-rss-latent-space-2026-10-01-ainews-gemini-4-argon-gdms-answer-to-astrafable.md

## Raw Concept

K277 cluster hub. Dual-ID **OSINT K277**. Prior @concepts/k276-harness-evolution-wave.md.

## Narrative

Five papers and three tooling items. Three of the five papers rewrite the harness. Zero clones. No skill install.

| Source | Contribution | Posture |
|--------|--------------|---------|
| 2609.40303 minimal harness | The coding environment is the big effect; extra machinery was not significant | Do not add harness bulk |
| 2609.40306 DynaHarness | Paired regression gate on every self-revision | Keep the gate pattern |
| 2609.40330 Turbo Harness | Per-instance harness editing from a playbook | Do not auto-evolve |
| 2609.40169 ScholarEvolve | Literature-guided harness evolution | Do not auto-evolve |
| 2609.40324 Cogentic | Adversarial verifiers plus a persistent verified ledger | Keep the split |

Four findings are worth acting on inside our own gates:

1. **The coding environment carries the gain.** The minimal-harness paper found that giving the agent an execution environment was the single largest measured effect, and that search, autonomy, and multi-agent scaffolding added nothing significant under an equal time budget. When a harness underperforms, check the environment before adding machinery.
2. **Self-selection is not selection.** The same paper measured a 6.832 percentage-point gap between letting the model pick its best answer and an oracle picking. This is the K276 trace finding in a second form. Score with an outside check.
3. **Every self-revision needs a paired regression gate.** DynaHarness admits a capability change only after a paired check. ScholarEvolve gates mutations on a held-out validation split and stresses disjoint splits. Both are the same rule.
4. **Split verification from production, and keep a ledger of only-confirmed work.** Cogentic runs adversarial verifiers over each draft and moves confirmed fragments into a persistent ledger. Provers see summaries, not the full history.

**A summary is not the document.** The Klement item measured it on real filings: agent summaries flipped a buy or sell call in one case in four to one in three.

Three claims we do not adopt. Turbo Harness, ScholarEvolve, and the harness-learning line from K276 all rewrite the harness itself. **Never auto-evolve our skills or rules from a paper.** Do not swap `/route`.

**Cemini posture:** FILE and HITL only. **0 product Integrate GO.**
