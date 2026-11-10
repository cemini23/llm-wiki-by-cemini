---
title: "A low similarity score is not evidence of independent work"
type: concept
related:
  - sources/arxiv-low-similarity-independence-rewrites-2611.07887.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - concepts/harness-supply-chain-defects.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: when someone claims an agent-assisted rewrite is independent of the original, what does a token-similarity score prove?

Synthesised from `@sources/arxiv-low-similarity-independence-rewrites-2611.07887.md`.

## Narrative

The setting is **source-conditioned rewriting**. The agent keeps the original project in its workspace, rewrites it, and iterates until a behavioural harness passes. No human edits the code.

The study covers 69 rewrites of six copyleft Python projects with five agents. Findings:

- Rewriting is cheap. Every controlled rewrite passed the harness after agent-only repair, with a median initial rewrite time of 18 minutes.
- Low scores are common. 42 of 54 ground-up rewrites scored below 25% JPlag similarity, and six scored below 5%.
- Low scores are not reproducible. Run-to-run variation accounted for 61% of the variance, project 14%, and agent under 1%. In 7 of 18 project-agent configurations, three identical runs straddled the 25% threshold.
- Two provenance-like signals are not specific. Retained imports and fingerprint facts did not separate rewrites from hand-written independent implementations: AUC 0.45 and 0.40.

The rule that follows: **one similarity score is one draw from a distribution.** Report repeated generations, and compare against an independent implementation of the same task.

### Why this belongs in a harness wiki

The same defect appears in any claim of the form "this artifact does not derive from that source":

- A page claimed to be written fresh from a digest when it was rewritten from a summary.
- A skill claimed to be original when it was paraphrased from an existing SKILL.md.
- A licence-clean reimplementation claimed on one comparison run.

A single detector pass cannot carry any of these claims. Recurrence is not convergence, and one low score is not independence.

### Practically

If Cemini ever republishes or re-licenses a tool or page, record three runs and one independent baseline. Report the spread, not the minimum.

## Snippets

> "Repeating an identical configuration accounts for 61% of the variance, against 14% for the project and under 1% for the agent, and in 7 of the 18 project-agent configurations three identical runs fall on both sides of the 25% threshold." [Source: arxiv-2611.07887-a-low-similarity-score-does-not-show-independenc.pdf p.2]
