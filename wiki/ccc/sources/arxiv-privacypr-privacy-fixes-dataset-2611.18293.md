---
title: "PrivacyPR: A Dataset of Real-World Privacy Fixes for Benchmarking Privacy-Aware Code Review (2611.18293)"
type: source
maturity: draft
related:
  - concepts/privacy-aware-code-review.md
updated: 2026-11-16
read_status: read
---

## Raw Concept

- **Title:** PrivacyPR: A Dataset of Real-World Privacy Fixes for Benchmarking Privacy-Aware Code Review
- **Authors:** Hua Yang, Aditya Bhardwaj, Shidong Pan, Bowen Xu (NC State)
- **Type:** arXiv preprint, cs.SE
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.18293-privacypr-a-dataset-of-real-world-privacy-fixes.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18293
- **Read status:** full — 5 pages extracted 2026-11-16

## Narrative

The premise: coding agents now review code, but whether they catch the privacy defects that GDPR-type law requires is largely untested, because few datasets link a real privacy defect to the fix that was accepted.

The dataset: 4,131 merged pull requests from 1,469 repositories (June 2018 to January 2024), each with commits, diffs, review discussion and LLM-generated labels for privacy relevance, fix type and GDPR principle. It provides 1,169 high-confidence privacy fixes, 1,643 non-fix PRs, a manually checked Verified split of 250 plus 250, and a Small split of 100 plus 100. On Verified, both annotators endorsed 72% of the model's GDPR-principle assignments.

The evaluation harness reverts each fix to reintroduce the defect. That is the reusable design: the benchmark tests detection against a known-introduced bug, not against a curated example.

Numbers: on Small, two coding agents detect only 42-51% of defects under a generic review prompt, but 88-91% when explicitly asked to check privacy, while flagging 11-15% of non-fix PRs. Detection is possible; it depends heavily on review intent and it comes with false positives.

[Source: arxiv-2611.18293-privacypr-a-dataset-of-real-world-privacy-fixes.pdf]

## Snippets

> "two coding agents detect only 42–51% of defects under a generic review prompt, but 88–91% when explicitly asked to check privacy, while flagging 11–15% of non-fix PRs."

## Dead Ends

- **Full-read note (2026-11-16):** Scope is public GitHub pull requests; the 99% in-browser fidelity figure applies to the PIZZA matcher, not to general code review. [Source: arxiv-privacypr-privacy-fixes-dataset-2611.18293.md full text, 5pp]
