---
title: "A low similarity score does not show independence after agent rewriting"
type: source
related:
  - concepts/similarity-score-not-independence.md
  - concepts/tool-eval-license-skepticism-patterns.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Low Similarity Score Does Not Show Independence after Source-Conditioned Repository Rewriting |
| Author | Micheline Benedicte Moumoula, Serge Lionel Nikiema, Tailia Malloy, Abdoul Kader Kabore, Jacques Klein, Tegawende F. Bissyande (University of Luxembourg) |
| Type | arXiv paper (cs.SE), 2611.07887 |
| Location | `research to be indexed/ccc/arxiv-2611.07887-a-low-similarity-score-does-not-show-independenc.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 20 |
| Read status | read |

## Narrative

The setting is **source-conditioned rewriting**. A coding agent keeps the original project in its workspace, rewrites the repository, and iterates until a fixed behavioural test harness passes. No human edits the code.

The study covers 69 rewrites of six copyleft Python projects with five agents.

Findings:

- **Rewriting is cheap.** Every controlled rewrite passed the harness after agent-only repair. The median initial rewrite took 18 minutes.
- **Low scores are common.** Median JPlag similarity was 64% under a layout-preserving prompt and 22% under a ground-up prompt. Of 54 ground-up rewrites, 42 scored below 25%, and six below 5%.
- **Low scores are not reproducible.** Nine rewrites of one project spread over 14 to 75 percentage points. Repeating the identical configuration accounted for 61% of the variance. Project accounted for 14% and agent under 1%. In 7 of 18 project-agent configurations, three identical runs straddled the 25% threshold.
- **Two signals that look like provenance are not specific.** Rewrites kept 54% of the original's external imports and 48% of its fingerprint facts. Hand-written independent implementations kept almost as much. Neither signal separated the two groups: AUC 0.45 for imports and 0.40 for fingerprints.

The conclusion is stated plainly: a similarity score from one rewrite is a single draw from a wide distribution. A low value does not show independence, and it does not predict that the next run scores low.

This matters beyond licensing. Any Cemini claim of the form "this page was written fresh, it does not derive from that source" has the same defect. One sample of overlap proves little. Report repeated generations, and compare against an independent implementation of the same task, not against an unrelated project.

## Snippets

> "Thus a low score on one rewrite is weak evidence of independence: another run of the same agent may score high." [Source: arxiv-2611.07887-a-low-similarity-score-does-not-show-independenc.pdf p.1]

> "Repeating an identical configuration accounts for 61% of the variance, against 14% for the project and under 1% for the agent." [Source: arxiv-2611.07887-a-low-similarity-score-does-not-show-independenc.pdf p.2]
