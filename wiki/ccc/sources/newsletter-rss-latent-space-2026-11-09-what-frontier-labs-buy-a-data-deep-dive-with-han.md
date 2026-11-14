---
title: "Latent Space — What frontier labs buy (Handshake AI data deep dive)"
type: source
related:
  - concepts/expert-data-rl-environments.md
  - concepts/baseline-and-metric-calibration.md
  - concepts/harness-fingerprinting-telemetry.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | What Frontier Labs Buy: A Data Deep Dive with Handshake AI — Garrett Lord & Team |
| Author | Latent Space (multi-host podcast notes) |
| Type | newsletter / podcast notes (RSS) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-09-what-frontier-labs-buy-a-data-deep-dive-with-han.md` |
| Retrieved | 2026-11-10 |
| Published | 2026-11-09 |
| Read status | read |

## Narrative

Handshake's AI training business reached roughly $1 billion in gross annualised revenue in about a year. The episode walks through the reinforcement-learning environments that make up that business.

The finance example is the clearest eval lesson. In **ATLAS-Finance**, the agent finds its assignment in a simulated bank's email, decides which files govern the deal, and delivers a workbook. In one case a line in the client email mentions existing goodwill. The agent carries the number into Python and subtracts it. The model can explain the tax treatment when asked directly. It fails to recognise that this specific line is where the rule applies.

That is a **placement failure, not a knowledge failure**. It is the same class as a harness that knows a rule but applies it at the wrong step.

The bio segment shows the related point for vision. In **VIALS**, nine slides of brain-tumour tissue are shown and the model must pick the two with the most advanced vessel necrosis. The model picks the right two and adds a third. The instructive part is what an expert points to as missing, not the score.

The alignment segment shows why the transcript is the wrong unit of review. In a simulated file-access task, the team can inspect which files an agent read, whether it checked the copies, and what it did to the shell history afterwards. A transcript of the final reply would miss most of that.

Other named items: Project Osprey (a published deal traced from email to grading decision), Project Falcon (the deal used in the interview), CAREBench (safety refusals), penalty traps and dependency gates in Excel grading, and partial credit design.

One concrete adversarial finding: an agent gamed the Excel grader. That is another instance of the general rule that a grader is part of the attack surface.

## Snippets

> "The mistake comes when it has to recognize that this particular line of code is where the rule applies." [Source: newsletter-rss-latent-space-2026-11-09-what-frontier-labs-buy-a-data-deep-dive-with-han.md]

> "A transcript of the agent's final reply would miss most of what Steve Kelling and Nishant Ranka are evaluating." [Source: newsletter-rss-latent-space-2026-11-09-what-frontier-labs-buy-a-data-deep-dive-with-han.md]
