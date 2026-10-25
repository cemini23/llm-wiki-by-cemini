---
title: Verifier–deployment gap (self-authored tests fail)
type: concept
tags: [concept, harness, verification, k198, ccc, poker]
keywords: [self-authored verification, heuristic rewrite, regression tax]
related:
  - sources/arxiv-2607.24300-self-authored-verification.md
  - sources/arxiv-2607.24663-aps-rag.md
  - concepts/skill-regression-tax.md
  - concepts/code-as-agent-harness.md
  - concepts/swap-regret-attention-fictitious-play.md
  - entities/tools/agent-governance-toolkit.md
  - concepts/document-processing-pipeline-scale-patterns.md
maturity: draft
created: 2026-07-28
updated: 2026-10-25
---

## Relations

- @entities/tools/agent-governance-toolkit.md — K198 backlink

- @sources/arxiv-2607.24300-self-authored-verification.md
- @sources/arxiv-2607.24663-aps-rag.md — operations-grounded eval contrast
- @concepts/skill-regression-tax.md
- @concepts/code-as-agent-harness.md
- @concepts/swap-regret-attention-fictitious-play.md

## Raw Concept

When the agent authors both the policy and the accept test, scores can stay green while deployment fails.

## Narrative

arXiv 2607.24300 formalizes the **verifier–deployment gap** for heuristic self-improving agents. Same pattern as skill regression tax and play-adequacy vs prediction-accuracy. Ops rule: promotions need **external** gates (APS-Bench-style gold nuggets, HU sandbox yardsticks, human gates) — never self-authored unit tests alone.
