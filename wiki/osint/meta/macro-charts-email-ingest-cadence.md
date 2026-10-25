---
title: Macro Charts email ingest cadence
type: concept
tags: [meta, automation, macro-charts, ingest, phase-2]
keywords: [gmail, rss, vinnyb64, macrocharts, inbox]
related:
  - sources/macro-charts-paid-forwards-vincent-2026-06-22-07-05.md
  - concepts/macro-charts-regime-signals.md
  - concepts/cemini-wiki-ingest-workflow.md
  - meta/substack-rss-ingest-cadence.md
  - sources/macro-charts-paid-forwards-vincent-2026-05-28-07-07.md
maturity: validated
created: 2026-07-05
updated: 2026-10-25
---

## Relations

- @sources/macro-charts-paid-forwards-vincent-2026-06-22-07-05.md — first K-batch from pipeline
- @concepts/cemini-wiki-ingest-workflow.md — Phase 2 inbox extension
- @meta/substack-rss-ingest-cadence.md — other finance Substack RSS feeds

## Raw Concept

Operator setup 2026-07-05: auto-capture Macro Charts Substack into `research to be indexed/` — RSS for free teasers, Gmail for Vincent (`vinnyb64@gmail.com`) paid forwards. Wiki writes remain Cursor human-gated.

## Narrative

| Lane | Script | Cadence | Output prefix |
|------|--------|---------|---------------|
| Free RSS (Macro Charts only) | `scripts/macro_charts_rss_poller.py` (wrapper) | via unified RSS agent | `macro-charts-rss-*` |
| All Substack RSS | `scripts/substack_rss_poller.py` | LaunchAgent 30 min | `substack-rss-*` + macro prefix |
| Paid email | `scripts/macro_charts_email_poller.py` | LaunchAgent 15 min | `macro-charts-paid-forward-*` |

Config: Gmail `config/macro-charts-ingest.yaml`; RSS list `config/substack-rss-ingest.yaml`. OAuth: `~/.cemini/gmail-oauth-{client,token}.json`. Setup: `bash scripts/setup_macro_charts_email_ingest.sh`.

**Dedup:** Same post URL — paid forward wins over RSS teaser (`.local/state/substack-rss-posts.json`).

**Backfill:** `python3 scripts/macro_charts_email_poller.py --backfill-days 14` (Gmail filters are not retroactive).

**Ingest:** Prefer `macro-charts-paid-forward-*` in Cursor K-batch; run standard preingest → wiki → egress archive ritual.
