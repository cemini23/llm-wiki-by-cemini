---
title: Reverse quant engineering — what 13F and public filings cannot show
type: concept
tags: [concept, quant, hedge-funds, 13f, osint, k67, zostaff]
keywords: [13f-limitations, form-adv, confidential-treatment, swap-positions, jane-street-sebi, zostaff-repo]
related:
  - sources/trading-posts-compilation-38-2026-05-26.md
  - concepts/hedge-fund-open-source-tooling.md
maturity: draft
created: 2026-05-26
updated: 2026-05-26
---

## Relations

- @sources/trading-posts-compilation-38-2026-05-26.md — Post 34 (@zostaff)
- @concepts/hedge-fund-open-source-tooling.md — adjacent OSS tooling theme

## Raw Concept

@zostaff (K67) argues **13F is a lagged, long-only mask** — no shorts, swaps as notionals only, 45-day delay, confidential treatment, window dressing. Real "reverse quant" uses **second-order traces**: ADV language shifts, hiring, patents, cross-jurisdiction filings. Open repo cited on GitHub (`zostaff`) [NEEDS VERIFICATION 2026-05-26].

## Narrative

### Structural blind spots

- Archegos-style exposure via TRS invisible in 13F
- Form SHO delay (K67 cites push to 2028) leaves short data gap
- LLM on 13F alone → "beautiful hallucination" of public mask

### Methodology sketch

Six techniques + monitoring + pattern propagation (per post); Jane Street vs **SEBI** 105-page leak as case study.

### Cemini relevance

- OSINT tradecraft for **fundamental/institutional** research track — not Polymarket execution.
- Warn any agent pipeline that ingests 13F without limitation preamble.

## Snippets

> "If your analyst still thinks a 13F is a portfolio snapshot, fire the analyst." [Source: Posts.docx K67 Post 34, @zostaff]
