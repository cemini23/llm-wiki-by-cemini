---
title: K279 Harness Wave (Oct 2026)
type: concept
tags: [agents, harness, k279, ccc]
keywords: [k279, process-eval, over-refusal, contra, FILE]
related:
  - concepts/k281-harness-wave.md
  - concepts/k278-harness-wave.md
  - sources/eval-repo-opportunity-2026-10-03.md
  - sources/arxiv-2610.01833-process-eval-2026-10-03.md
  - sources/arxiv-2610.01769-contra-2026-10-03.md
  - sources/arxiv-2610.01497-openmtb-2026-10-03.md
  - sources/arxiv-2610.01323-trace-2026-10-03.md
  - sources/newsletter-rss-latent-space-2026-10-03-ainews-not-much-happened-today.md
  - sources/newsletter-rss-latent-space-2026-10-02-airbnb-2026-10-03.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k281-harness-wave.md
- @concepts/k278-harness-wave.md
- @sources/eval-repo-opportunity-2026-10-03.md
- @sources/arxiv-2610.01833-process-eval-2026-10-03.md
- @sources/arxiv-2610.01769-contra-2026-10-03.md
- @sources/arxiv-2610.01497-openmtb-2026-10-03.md
- @sources/arxiv-2610.01323-trace-2026-10-03.md
- @sources/newsletter-rss-latent-space-2026-10-03-ainews-not-much-happened-today.md
- @sources/newsletter-rss-latent-space-2026-10-02-airbnb-2026-10-03.md

## Raw Concept

K279 cluster hub. Dual-ID **OSINT K279**. Prior @concepts/k278-harness-wave.md.

## Narrative

Four papers and two practice items. One theme, stated four ways: **a passing result does not certify the process.**

| Source | Contribution | Posture |
|--------|--------------|---------|
| 2610.01833 process evaluation | 92.6% of final-check-passing runs still had a process deviation | Build this |
| 2610.01769 CONTRA | 44.3% of the agent's decisions were absent from its own report | Read this |
| 2610.01497 OpenMTB | Safety score inflated by refusing more; 83.3-100% label collapse | Metric design |
| 2610.01323 TRACE | Discounted-return credit assignment for late outcomes | Pattern only |

### The numbers to keep

**92.6%.** Of 175 runs that passed every final numerical check, 162 still had at least one process deviation. Score only the answer and you certify roughly 93% of runs that took a wrong path.

**44.3%.** An independent review of a coding agent's decisions found 116 of 262 were absent from the agent's own report. The agent is not concealing them; it does not track its own implicit choices.

**83.3% to 100%.** Clinical audit models failed to keep the middle "partially supported" label in almost every case that deserved it. Their safety score looked fine — 83.9 to 90.9 — while accuracy sat at 46.2% to 74.0%. **A safety metric can be inflated by refusing more**, and an aggregate hides it.

### The design rules

1. **Score the trajectory, not only the outcome.** Tool selection, arguments, ordering, scope.
2. **Get ground truth from an independent call**, not from the agent's account of itself.
3. **Template tests that resolve their placeholders at runtime** survive an API change without a rewrite.
4. **Attribute failures to root causes** through a dependency graph — 6.34 failed checks collapsed to 2.65 roots.
5. **Report safety and accuracy separately.** Never let one aggregate stand for both.
6. **Keep a middle label.** A binary taxonomy cannot show label collapse.

### One caution

The roundup reported a **62.8% long-context accuracy drop** when one vendor's window scales from 4K to 128K tokens. A bigger context window is not the same as more usable context.

### Boundary

Nothing is adopted. Both CONTRA and the process-evaluation work describe gates we have not built. **Do not swap `/route`. No skill install. No plugin install without asking.**

**Cemini posture:** FILE. **0 product Integrate GO.**
