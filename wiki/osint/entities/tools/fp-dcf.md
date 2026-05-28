---
title: FP-DCF — first-principles DCF skill for LLM agents
type: entity
tags: [entity, tool, valuation, dcf, reference-only, no-license, k75]
keywords: [fp-dcf, tiejiang8, fcff, wacc, market-implied-growth, sensitivity, agent-valuation]
related:
  - concepts/equity-fair-value-evaluation.md
  - concepts/pnl-attribution-versioning.md
  - entities/tools/financetoolkit.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/equity-fair-value-evaluation.md — prod uses FMP-weighted synthesizer; FP-DCF is external methodology reference only
- @concepts/pnl-attribution-versioning.md — any ported logic requires `brain_equity` version bump
- @entities/tools/financetoolkit.md — complementary standardized metrics layer
- @concepts/cemini-license-posture.md — no LICENSE file → default copyright

## Raw Concept

K75 Phase-0 (2026-05-28) on equity-valuation extension candidates cited in @concepts/equity-fair-value-evaluation.md. Repo: `github.com/tiejiang8/fp-dcf`.

## Narrative

- **URL**: https://github.com/tiejiang8/fp-dcf
- **License**: **No LICENSE file**; `pyproject.toml` has no `license` field; GitHub API `license.spdx_id` = null [CONFIRMED 2026-05-28]
- **Stars**: 0; last push 2026-04-24
- **Stack**: Python ≥3.10; yfinance + AkShare + BaoStock; CLI `fp-dcf`; JSON valuation contracts + WACC×terminal-growth sensitivity charts

### Why it matters architecturally

Strong fit for **agent-readable valuation JSON**: explicit `requested_valuation_model` / `effective_valuation_model`, `market_implied_growth`, diagnostics block — closer to audit-trail requirements than opaque single-number DCF. Overlaps conceptually with prod `core/equity_valuation.py` but uses different data vendors (not FMP stable API).

### Phase-0 verdict (2026-05-28)

| Gate | Result |
|------|--------|
| G0 Repo | PASS |
| G2 License | **FAIL** — no LICENSE |
| G3 Overlap | PARTIAL — prod already ships FMP synthesizer |
| G4 Maturity | LOW — 0★, solo maintainer |

**Verdict: REFERENCE ONLY / NO-GO Adopt** — read `contracts/` + `SKILL.md` for schema ideas; do not pip install on prod until SPDX license lands. Prefer stealing JSON schema shape into prod with FMP data path, not vendoring package.

## Snippets

> "First-principles DCF skill and valuation engine for LLM agents and quantitative research workflows." [Source: GitHub repo description, retrieved 2026-05-28]

## Dead Ends

- **Adopt on prod** — blocked by missing LICENSE under @concepts/cemini-license-posture.md.
