---
title: "Model versus harness variance — when each one moves the score"
type: concept
related:
  - sources/arxiv-shellbench-model-vs-harness-2611.32946.md
  - sources/arxiv-2610.32483-when-agents-fail-model-or-harness-who-s-to-blame-2026-10-27.md
  - sources/newsletter-rss-latent-space-2026-11-24-ainews-jensen-is-back-and-openai-shows-its-pretr.md
  - sources/newsletter-rss-latent-space-2026-11-25-ainews-gemini-4-neon-marks-gdms-full-return-as-a.md
  - sources/newsletter-rss-latent-space-2026-11-25-ainews-math-proofs-are-landing-faster-than-we-ca.md
  - concepts/agent-harness-operational-definition.md
  - concepts/model-harness-six-responsibilities.md
updated: 2026-11-26
maturity: draft
---

## Raw Concept

Question this page answers: for a given task class, how much of the score comes from the model and how much from the harness? Synthesised from ShellBench (2611.32946), the "When Agents Fail" framework (2610.32483), and two Latent Space digests.

## Narrative

The workspace has carried a strong "harness over model" claim, taken mostly from coding benchmarks. The newer evidence splits by task class.

**Everyday tasks: model dominates.** ShellBench runs 12 models across 5 harnesses on 100 household-level tasks. Harness means sit in a 3-point band: 42.87 to 45.23. Model scores span 18.8 to 62.5. Model choice explains most of the variance. The paper states this directly.

**Coding and tool-heavy tasks: harness can dominate.** Artificial Analysis reports a within-model spread of about 13 points across harnesses on one coding benchmark. GLM scores best in Claude Code and worst in Codex. The "When Agents Fail" framework (2610.32483) ranks harnesses by cross-model fit with gaps of more than 20 points, from OpenCode at 87.5 to Deep Agents at 64.2.

**Per-pair effects are real even when means are flat.** In ShellBench, DeepSeek V4.1 Flash loses about 10 points between Claude Code and Codex. Claude Fable 5.2 loses 5 points between Hermes and OpenClaw. A flat harness mean hides these pairs.

**A second coding datum, 2026-11-25.** A community benchmark ran 7 local Qwen 3.8 builds fully
autonomously on one RTX 5090. The author reports OpenCode at about 50% on FrontierHarness against
DSH Creator at about 63%, and calls those numbers a floor rather than a best case. That is a 13-point
harness gap on a coding task class, from a source that is not the harness vendor. It matches the
workspace's own verdict on OpenCode: rejected for a `/route` mid-lane swap.

**Harness co-evolution pays.** CoEvoBench reports that model-harness pairs improve mostly through harness edits, not training. Qwen3.8-27B adapted to the Pi harness gained 16 points on Terminal-Bench 2.1 at half the tokens.

**Reading rule.** Ask which task class before trusting either extreme. For everyday assistant work, pick the model. For long tool loops, the harness and the model-harness pair decide the result. Report the pair, not the model alone.

**Status.** ShellBench is one paper by an author group that also ships one of the harnesses under test. The Artificial Analysis and CoEvoBench items are newsletter reports, not papers read here. [TENTATIVE]

## Snippets

> "Model scores account for most of the variation across the full comparison, but some harnesses change individual model scores substantially." [Source: `arxiv-2611.32946-shellbench-what-matters-more-for-ai-agents-model.pdf` p.1, retrieved 2026-11-25]
