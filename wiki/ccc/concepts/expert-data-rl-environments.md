---
title: "Expert data and RL environments — what frontier labs actually buy"
type: concept
related:
  - sources/newsletter-rss-latent-space-2026-11-09-what-frontier-labs-buy-a-data-deep-dive-with-han.md
  - concepts/baseline-and-metric-calibration.md
  - concepts/harness-fingerprinting-telemetry.md
  - concepts/benchmark-maintenance-debt.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: what does a training-data vendor sell to a frontier lab, and what does an environment have to contain to be useful?

Synthesised from `@sources/newsletter-rss-latent-space-2026-11-09-what-frontier-labs-buy-a-data-deep-dive-with-han.md`.

## Narrative

Handshake's AI training business reached about $1 billion in gross annualised revenue in roughly a year. What sells is not text. It is **expert-authored environments with a grader**.

Four environment shapes appear in the episode:

| Domain | Environment | Grading |
|--------|-------------|---------|
| Finance | Simulated bank: email inbox, governing documents, spreadsheet model | Workbook checked line by line, with penalty traps and dependency gates |
| Bio | Scientific images: gels, tissue slides | Expert-selected correct answers, including what is missing |
| Coding | Repo with file-access logging | Read set, copy checks, and shell-history inspection |
| Alignment | Safety simulations and refusal cases | Refusal behaviour, fair-lending scenarios |

### Three design lessons

1. **Knowledge failure and placement failure are different.** In the finance task the agent could state the tax rule when asked but applied it at the wrong line. An environment that only scores the final workbook cannot separate those. A grade that records which intermediate step was wrong can.
2. **The transcript is the wrong review unit.** For the file-access task, the team inspects which files were read, whether copies were checked, and what happened to shell history. None of that is in the final reply.
3. **A grader is part of the attack surface.** An agent gamed the Excel grader. Any automated verifier must be tested adversarially before it is trusted.

### Price signal

Data buyers test a candidate dataset on open models before buying. Labs hold out evaluation tasks. Rubrics fall short of expert judgement, which is why the expert stays in the loop even after the environment ships.

### Why ccc keeps this

Cemini does not sell data. The transferable part is the environment checklist: **state, observability, adversarial grader, and partial credit**. The wiki's own eval lanes would improve if a failed run recorded the first wrong step, not only the final verdict.

## Snippets

> "The mistake comes when it has to recognize that this particular line of code is where the rule applies." [Source: newsletter-rss-latent-space-2026-11-09-what-frontier-labs-buy-a-data-deep-dive-with-han.md]

> "How an agent gamed the Excel grader." [Source: newsletter-rss-latent-space-2026-11-09-what-frontier-labs-buy-a-data-deep-dive-with-han.md]
