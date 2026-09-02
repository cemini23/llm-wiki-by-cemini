---
title: "colophon-group/jobseek"
type: entity
tags: [tool, phase-0, k219, guruwatcher]
keywords: [jobseek, playwright, career-page-poll, CC-BY-NC, MIT]
related:
  - sources/eval-github-revenue-opportunity-url-2026-08-03.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/guruwatcher-newsletter-claim-ledger.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
harness_verb: FILE
---

## Relations

- @sources/eval-github-revenue-opportunity-url-2026-08-03.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/guruwatcher-newsletter-claim-ledger.md

## Narrative

| Field | Value |
|-------|--------|
| **Repo** | https://github.com/colophon-group/jobseek |
| **License** | **MIT** (code) + **CC BY-NC 4.0** (data) [CONFIRMED gh 2026-08-03] |
| **Verdict** | **GO Extract patterns only** |
| **Local** | `.local/adopts/jobseek` (~64MB) |
| **Route** | GuruWatcher |

Career-page poll pipeline (asyncio + Playwright fallback) → Discord alert analog for GuruWatcher UW/yfinance-style pollers. **Do not use job data commercially** without respecting CC BY-NC. Steal resilience patterns; do not vendor the job corpus into prod.
