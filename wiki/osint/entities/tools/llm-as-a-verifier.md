---
title: "llm-as-a-verifier — self-verification (Extract)"
type: entity
tags: [tool, guruwatcher, k241, mit, extract]
keywords: [llm-as-a-verifier, claim-ledger, self-verification]
related:
  - sources/eval-multi-wiki-revenue-plan-2026-08-18.md
  - sources/substack-rss-capital-flows-2026-08-18-next-stage-macro.md
  - concepts/guruwatcher-newsletter-claim-ledger.md
  - concepts/cemini-license-posture.md
  - concepts/atto-genealogy-agent-kit.md
  - entities/tools/google-sam.md
  - concepts/sovereign-agent-mesh-biscuit.md
  - sources/arxiv-2610.06829-clift-web-agent-verification-2026-10-06.md
maturity: draft
created: 2026-08-18
updated: 2026-10-25
harness_verb: FILE
---

## Relations

- @sources/eval-multi-wiki-revenue-plan-2026-08-18.md — K241 eval
- @sources/substack-rss-capital-flows-2026-08-18-next-stage-macro.md — GW verifier-loop steal
- @concepts/guruwatcher-newsletter-claim-ledger.md — claim vs exhibit
- @concepts/cemini-license-posture.md
- @concepts/atto-genealogy-agent-kit.md — PII-safe verifier; no Barone vitals
- @entities/tools/google-sam.md — same-batch Extract
- @concepts/sovereign-agent-mesh-biscuit.md — scoped call then verify

## Raw Concept

K241 Phase-0 Extract. Clone `.local/adopts/llm-as-a-verifier` (411MB, depth-1; GitHub API size was ~67MB — clone includes extras but stays under 500MB). MIT confirmed via `gh api` 2026-08-18.

## Narrative

| Field | Value |
|-------|--------|
| Repo | https://github.com/llm-as-a-verifier/llm-as-a-verifier |
| License | **MIT** [CONFIRMED gh 2026-08-18] |
| Local | `.local/adopts/llm-as-a-verifier` (411MB) |
| Verdict | **GO Extract** — self-verification / claim-ledger pattern |
| wire_status | `policy_wired` |

Steal the self-check loop for GuruWatcher claim ledgers and Atto exhibit-vs-claim. Never put living-person PII in verifier fixtures. **Alert-only** on GW — never orders.

## Snippets

> Verdict: GO Extract (MIT). [Source: `.local/reports/license-k241-2026-08-18.md`]
