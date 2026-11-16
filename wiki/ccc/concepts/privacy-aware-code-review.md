---
title: Privacy-aware code review by coding agents
type: concept
maturity: draft
related:
  - sources/arxiv-privacypr-privacy-fixes-dataset-2611.18293.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: can a coding agent catch privacy defects in code review, and what changes the result?

From PrivacyPR (arXiv 2611.18293).

## Narrative

Detection is possible but intent-dependent. On a 100-plus-100 evaluation subset, two coding agents found only 42-51% of reintroduced privacy defects under a generic "review this code" prompt. Told explicitly to check privacy, the same agents found 88-91%. They flagged 11-15% of non-fix pull requests as problems either way.

Two practical consequences.

First, a general review prompt is not a privacy control. If privacy is a requirement, it must be an explicit instruction in the review step, not an expected side effect of "review".

Second, the false-positive rate is a real cost. Roughly one in seven clean changes gets flagged, so a privacy gate needs a triage path or it will train reviewers to ignore it.

Method note worth copying: the benchmark reverts an accepted fix to reintroduce the defect, so detection is measured against a known-introduced bug rather than a curated example.

[TENTATIVE] Figures from one paper's abstract on one dataset family (GDPR-oriented, public GitHub Python/JS-style repositories). Transfer to other codebases is untested.

## Snippets

> "detection depends strongly on review intent and comes with false alarms."
