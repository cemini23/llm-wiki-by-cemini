---
title: K276 Harness Evolution Wave (Sep 2026)
type: concept
tags: [agents, harness, k276, ccc]
keywords: [k276, harness-learning, trace-validity, plan-gap, FILE]
related:
  - concepts/k277-harness-evolution-wave.md
  - concepts/k275-harness-evolution-wave.md
  - sources/arxiv-2609.35738-harness-learning-2026-09-30.md
  - sources/arxiv-2609.38107-invalid-traces-2026-09-30.md
  - sources/arxiv-2609.38108-plan-execution-gap-2026-09-30.md
  - sources/arxiv-2609.38143-meta-skills-harness-2026-09-30.md
  - sources/arxiv-2609.38147-meta-reasoning-2026-09-30.md
  - sources/arxiv-2609.31473-game-arena-2026-09-30.md
  - sources/substack-rss-addy-osmani-2026-09-28-the-code-nobody-reads.md
  - sources/newsletter-rss-latent-space-2026-09-29-claude-codes-next-era-thariq-shihipar-anthropic.md
  - sources/newsletter-rss-latent-space-2026-09-29-ainews-amd-buys-world-labs-for-82b-as-atlas-solv.md
  - sources/newsletter-rss-latent-space-2026-09-29-ainews-opus-55-is-good-at-explainer-videos.md
  - sources/newsletter-rss-latent-space-2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultrafast.md
maturity: draft
created: 2026-09-30
updated: 2026-10-01
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k277-harness-evolution-wave.md
- @sources/newsletter-rss-latent-space-2026-09-29-ainews-amd-buys-world-labs-for-82b-as-atlas-solv.md
- @sources/newsletter-rss-latent-space-2026-09-29-ainews-opus-55-is-good-at-explainer-videos.md
- @sources/newsletter-rss-latent-space-2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultrafast.md
- @concepts/k275-harness-evolution-wave.md
- @sources/arxiv-2609.35738-harness-learning-2026-09-30.md
- @sources/arxiv-2609.38107-invalid-traces-2026-09-30.md
- @sources/arxiv-2609.38108-plan-execution-gap-2026-09-30.md
- @sources/arxiv-2609.38143-meta-skills-harness-2026-09-30.md
- @sources/arxiv-2609.38147-meta-reasoning-2026-09-30.md
- @sources/arxiv-2609.31473-game-arena-2026-09-30.md
- @sources/substack-rss-addy-osmani-2026-09-28-the-code-nobody-reads.md
- @sources/newsletter-rss-latent-space-2026-09-29-claude-codes-next-era-thariq-shihipar-anthropic.md

## Raw Concept

K276 cluster hub. Dual-ID **OSINT K276**. Prior @concepts/k275-harness-evolution-wave.md.

## Narrative

The strongest harness cluster so far. Six papers, four model-release items, one essay. Zero clones. No skill install.

| Source | Contribution | Posture |
|--------|--------------|---------|
| 2609.35738 harness learning | Train a proposer to revise the harness from execution feedback | Method note. No auto-evolve |
| 2609.38107 invalid traces | 31.6% of correct answers carry invalid traces on hard cases | Gate design. Use it |
| 2609.38108 plan-execution gap | 22-45% of runs keep the declared plan; pattern executors lift success | Pattern note. Do not swap `/route` |
| 2609.38143 meta-skills | A Builder learns support principles; +8.95 pp over no-skill | Split note. No auto-evolve |
| 2609.38147 meta-reasoning | Controller plus workers, bounded controller context | Design note |
| 2609.31473 game arena | Head-to-head games resist benchmark saturation | Eval note. Poker retired |

Three findings are worth acting on inside our own gates:

1. **A visible trace is not proof of the process.** The invalid-traces paper measures it. On the hardest instances, 31.6% of correct answers have invalid traces, and over half of those pass arithmetic checks but fail a dependency check. Accuracy even survives shuffled training traces. A gate that reads the trace is weaker than a gate that re-runs the check.
2. **Declare the pattern, then route to an executor that enforces it.** The plan-execution-gap paper shows most runs drift from the declared plan. Pattern-specific executors fix execution, not selection. This matches our `/route` design. Keep it. Do not swap `/route`.
3. **Keep the controller context bounded.** The meta-reasoning paper carries a compact run summary instead of replaying history, and gains 3.6 to 4.2 points.

Two claims we do not adopt. The harness-learning paper trains a proposer to rewrite its own harness, and the meta-skills paper learns a Builder that writes environments. Both are self-modification paths. **Never auto-evolve our skills or rules from a paper.**

The Addy Osmani essay and the Thariq podcast carry the same theme as the invalid-traces paper: the check, not the model, carries authority. Both are FILE. Do not swap `/route`. No skill install.

**Cemini posture:** FILE and HITL only. **0 product Integrate GO.**
