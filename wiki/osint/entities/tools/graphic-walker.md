---
title: Kanaries/graphic-walker — embeddable visual-analytics component
type: entity
tags: [entity, tool, visualization, analytics, dashboard, duckdb, reference, k53]
keywords: [graphic-walker, kanaries, visual-analytics, tableau-alternative, grammar-of-graphics, duckdb, embeddable, react, apache-2.0, backtesting-dashboard]
related:
  - sources/multi-wiki-link-eval-41url-2026-05-18.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @sources/multi-wiki-link-eval-41url-2026-05-18.md — K53 eval URL 11; the source that surfaced it (and got its license wrong)

## Raw Concept

What prompted this page: K53 multi-wiki tool-eval URL 11, primary fit OSINT-wiki. The eval Rejected it as "NO LICENSE FOUND"; a GitHub API check (2026-05-18) corrects that — the repo is **Apache-2.0**. The page records the corrected verdict and the OSINT-side relevance.

## Narrative

`Kanaries/graphic-walker` — an **open-source, embeddable visual-analytics web component**, positioned as an "open-source alternative to Tableau." Verified 2026-05-18 (GitHub API): **Apache-2.0**, ~3,137★, actively maintained.

Architecture (per the eval):
- A **grammar-of-graphics** drag-and-drop UI — analysts explore data fluidly without writing SQL.
- A **DuckDB-based engine** for fast local/edge computation.
- Embeddable as a React/TypeScript component; warehouse pushdown to ClickHouse / Snowflake for large datasets.

### Verdict — corrected

The eval Rejected this on "NO LICENSE FOUND" despite calling its operational alignment "near-perfect." The license finding is **wrong** — graphic-walker is Apache-2.0 (verified), a 3.1k-star mature project. Reject retracted.

Corrected verdict: **Reference / Steal-from candidate.** Apache-2.0 is IP-sale-clean. Two genuine Cemini-side use cases:
- the **OSINT librarian interface** — an embeddable exploratory-analytics layer over indexed data;
- the **Cemini backtesting dashboard** — a grammar-of-graphics visualization layer over strategy results and risk metrics.

Not an immediate adoption (Cemini has no current dashboard workstream), but a strong, license-clean candidate to revisit when a visualization layer is scoped. Another K53 instance of the eval's "retrieval-gap → no-license" error — see @concepts/cemini-license-posture.md.

## Snippets

> "Graphic Walker operates as an embeddable, componentized visual analytics web element that leverages a specialized DuckDB-based engine to execute rapid local and edge computations ... an exceptionally powerful candidate for accelerating the OSINT librarian interface and driving the visualization layer of the /opt/cemini backtesting dashboard." [Source: Multi-Wiki Tool Evaluation.docx — URL 11]
