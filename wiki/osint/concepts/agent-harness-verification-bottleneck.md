---
title: Agent harness verification bottleneck
type: concept
tags: [concept, harness, verification, route, k234]
keywords: [harness, verification, evals, code-review, cattle, charity-majors, route]
related:
  - sources/newsletter-pragmatic-engineer-charity-majors-ai-2026-08-12.md
  - concepts/agent-toolkit-routing-research-backlog.md
  - concepts/agentic-legacy-code-modernization.md
  - concepts/socratic-answer-withholding-contract.md
  - sources/arxiv-2608.12249-hpc-modernization-agentic-2026-08-13.md
  - sources/arxiv-2608.12292-tutor-withhold-answer-2026-08-13.md
  - sources/arxiv-2608.13560-autodesign-2026-08-14.md
maturity: draft
created: 2026-08-12
updated: 2026-08-14
---

## Relations

- @sources/newsletter-pragmatic-engineer-charity-majors-ai-2026-08-12.md
- @concepts/agentic-legacy-code-modernization.md — oracle-bound delegation (K235)
- @concepts/socratic-answer-withholding-contract.md — enforced contract recipe (K235)
- @sources/arxiv-2608.12249-hpc-modernization-agentic-2026-08-13.md
- @sources/arxiv-2608.12292-tutor-withhold-answer-2026-08-13.md
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept

What this page answers: why agent/coding harnesses increasingly matter more than raw model jumps, and why verification (not code review of AI output) is the scarce resource — for Cemini `/route` + SIP/verify gates.

## Narrative

From Charity Majors via Pragmatic Engineer (2026-08-12): the Nov 2025 inflection was as much **Claude Code as harness infrastructure** as Opus 4.5. Cheap generation pushes the bottleneck to **tests, evals, conformance** — the systems that let you ship with confidence when you did not personally author every line.

Cemini mapping:

| Claim | Harness implication |
|-------|---------------------|
| Harness > model for generational shift | Keep investing in `/route`, SIP, always-approve executors, WorkDir hygiene — not only model swaps |
| Verification bottleneck | Post-implement `## Verify` gate + claim-safe `_route_runs/` evidence is the product; status-only "done" is a bug |
| Pets → cattle for code | Prefer regenerate+verify over endless hand-patch of agent output when verify fails |
| Code review overrated for correctness | Prefer deterministic verify commands over LLM-as-judge of diffs (pairs K162 / K242) |
| More discipline under non-determinism | Never weaken NEVER/LIVE OK / secret deny when speeding lanes |

HITL only for harness evolution (pairs SHE / K268). CCC brief: `../Cemini claude code CCC/briefs/2026-08-12_k234-charity-majors-harness-verify.md`.

[Source: Pragmatic Engineer / Charity Majors 2026-08-12]
