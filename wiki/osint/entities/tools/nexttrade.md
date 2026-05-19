---
title: NextTrade — UI-driven algorithmic trading + backtesting framework
type: entity
tags: [entity, tool, algorithmic-trading, backtesting, cemini-financial, reference, k54]
keywords: [nexttrade, austin-starks, no-code-trading, backtesting-framework, mit-license, typescript, stack-misidentification]
related:
  - sources/multi-wiki-tool-eval-26url-2026-05-19.md
  - concepts/quant-finance.md
maturity: draft
created: 2026-05-19
updated: 2026-05-19
---

## Relations

- @sources/multi-wiki-tool-eval-26url-2026-05-19.md — K54 eval URL 21; the source that surfaced this tool
- @concepts/quant-finance.md — the domain NextTrade operates in

## Raw Concept

What prompted this page: K54 multi-wiki tool-eval URL 21, tier **Adopt**, primary fit Cemini-financial. The eval is **partly wrong about it** — this page records the verified facts and downgrades the practical verdict to reference-grade.

## Narrative

`austin-starks/NextTrade` — a system for **algorithmic trading**: a UI-driven framework for building, backtesting, and deploying strategies without hand-coding each one. Verified 2026-05-19 (GitHub API): **MIT**, **1,741★**, 0 open issues.

### Two eval errors corrected

1. **Stack** — the eval claims "Python, presumed NumPy/Pandas integration layer." The repo's primary language is **TypeScript**. The eval's whole NEEDS VERIFICATION about connecting "NextTrade's engine with Cemini's existing PostgreSQL and Redis Streams event pipeline" assumes a Python engine that does not exist. A TS framework is a far poorer drop-in for the Python `/opt/cemini` stack than the eval implies.
2. **Maturity** — last push **2025-05-15**, i.e. roughly **one year stale** as of this ingest. The eval reports no commit date and treats the repo as current. A year of no commits against fast-moving brokerage/market-data APIs is a meaningful staleness signal.

### Verdict — Reference, not Adopt

License is clean (MIT, IP-sale-safe) and the star count is respectable. But between the TypeScript stack mismatch and the ~1-year staleness, NextTrade is **not** an Adopt candidate for the Cemini trading stack. It is worth reading as a **reference** for one specific idea: collapsing strategy definition into a UI/declarative form so a simple crossover does not need 200 lines of boilerplate. That design idea is portable; the codebase is not. No Phase-0 audit warranted — the stack mismatch already disqualifies integration.

## Snippets

> "NextTrade directly targets and eliminates the traditional algorithmic trading barriers by bridging complex Python and Pandas logic into a highly actionable, generative AI-assisted framework." [Source: Tool Evaluation and Wiki Fit.docx — URL 21] — note: the "Python and Pandas" characterization is wrong; the repo is TypeScript.
