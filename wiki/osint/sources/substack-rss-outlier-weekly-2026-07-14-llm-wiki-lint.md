---
title: "Outlier Weekly — LLM wiki lint / contribution rate (2026-07-14)"
type: source
tags: [source, wiki-ops, lint, wikilint, contribution-rate, k165]
keywords: [wikilint, orphans, bidirectional-gaps, contribution-rate, cemini23-wikilint]
related:
  - concepts/cemini-wiki-ingest-workflow.md
maturity: validated
read_status: deep-read
created: 2026-07-14
updated: 2026-07-14
clusters: [wiki-ops]
---

## Relations

- @concepts/cemini-wiki-ingest-workflow.md — matches OSINT lint + brief contribution rate posture
- Cross-wiki: CCC (harness CI) + SEO (voice/ops) as briefs if needed — **not** gambling despite RSS stub tags

## Raw Concept

- **Title**: Your LLM Wiki Will Rot Unless You Lint It
- **Author**: Outlier Weekly
- **URL**: https://outlierweekly.substack.com/p/your-llm-wiki-will-rot-unless-you
- **Retrieved**: 2026-07-14
- **Type**: Substack RSS (full body in drop)

## Narrative

Operator essay: agent-written wikis rot via orphans, dangling `@path`, one-way `related:`, stale `[NEEDS VERIFICATION]`. Metric = **contribution rate** (pages → briefs/log), not note count. Control = **wikilint on every PR** (`cemini23/wikilint`), not weekly vault rituals. Aligns with OSINT `wiki_lint.py` + `ingest_session_gate.py`.

Inbox stub incorrectly tagged `gambling-wiki` / prediction-markets — **corrected routing** to wiki-ops + CCC.

## Snippets

> “If your orphan count is rising while your brief count is flat, you are building a museum.”
