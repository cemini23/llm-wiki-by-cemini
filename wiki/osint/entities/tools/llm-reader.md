---
title: "m92vyas/llm-reader"
type: entity
tags: [tool, phase-0, k221, guruwatcher]
keywords: [llm-reader, url-to-markdown, MIT, alert-research]
related:
  - sources/eval-github-revenue-evaluation-docuscan-reader-2026-08-03.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/guruwatcher-newsletter-claim-ledger.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
harness_verb: FILE
---

## Relations

- @sources/eval-github-revenue-evaluation-docuscan-reader-2026-08-03.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/guruwatcher-newsletter-claim-ledger.md

## Narrative

| Field | Value |
|-------|--------|
| **Repo** | https://github.com/m92vyas/llm-reader |
| **License** | **MIT** [CONFIRMED gh 2026-08-03] |
| **Verdict** | **GO Integrate** |
| **Local** | `.local/adopts/llm-reader` (~192KB) |
| **Route** | GuruWatcher |
| **wire_status** | `pending` |

URL→markdown reader for alert / newsletter research pipelines. Integrate as a local fetch→clean-text step before claim-ledger extraction; prefer local-first over SaaS readers for PII-adjacent GuruWatcher ops.
