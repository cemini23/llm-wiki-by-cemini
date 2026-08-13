---
title: benchflow-artifacts — local repo audit/verify/scrub utilities
type: entity
tags: [entity, tool, code-audit, agpl, cyber, k235, extract-isolate]
keywords: [benchflow, repo-report, repo-verify, repo-scrub, PR-regression, credential-sweep]
related:
  - sources/deep-research-url-evaluation-2026-08-13.md
  - concepts/cemini-license-posture.md
  - entities/tools/smolvm.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @sources/deep-research-url-evaluation-2026-08-13.md — K235 eval: Extract (local-abliterated-lab)
- @concepts/cemini-license-posture.md — AGPL isolate precedent
- @entities/tools/smolvm.md — combo: run scrubs inside the microVM boundary

## Raw Concept

Repo `benchflow-ai/artifacts` (18★, stdlib-only Python). Three offline utilities: `repo-report` (complexity metrics, test-to-code ratios), `repo-verify` (PR regression verification — expects fail-to-pass transitions), `repo-scrub` (leaked credentials / missing license sweep). Phase-0: **AGPL-3.0 verified** via gh api (docx claim confirmed).

## Narrative

**Verdict: GO Extract — isolate pattern (local-abliterated-lab).** AGPL-3.0 is viral for proprietary orchestration → run as an **isolated external binary inside a microVM** (smolvm candidate), never merged into lab/proprietary code. Value: automated auditing of agent-generated artifacts (Claude/Cursor PRs) before ingest into the lab — pairs with smolvm for sanitizing untrusted repo payloads.

Extract scope: the credential-sweep + fail-to-pass regression methodology; the regex complexity estimation scaling on large batches is unverified (docx NEEDS VERIFICATION carried forward).

[Source: benchflow-ai/artifacts (retrieved 2026-08-13)]
