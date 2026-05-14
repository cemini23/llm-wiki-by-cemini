---
title: "bukosabino/ta — Python Technical Analysis Library"
type: entity
tags: [tool, technical-analysis, python-library, mit, no-go-phase-0-2026-05-13, 43-indicators, github-eval-2026-05-13, parallel-impl-rejected]
keywords: [bukosabino-ta, technical-analysis-library, ta, python-ta, 43-indicators, rsi-macd-bollinger, mit-license, 5100-stars, no-go-parallel-impl, pandas-ta-classic-duplicate]
related:
  - sources/eval-github-repos-2026-05-13.md
  - concepts/polymarket-bot-architecture.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
  - entities/platforms/polymarket.md
  - entities/tools/tradingview-mcp-atilaahmettaner.md
maturity: validated
created: 2026-05-13
updated: 2026-05-14
---

## Relations

- @sources/eval-github-repos-2026-05-13.md — Phase-0 eval source (ADOPT verdict, May 13 2026 — superseded by Phase-0 audit below)
- @concepts/polymarket-bot-architecture.md — bot playbook explicitly flags layered indicator stacks as failure mode; this is the tool, discipline is the user
- @concepts/multi-wiki-eval-doc-level-vs-phase-0.md — canonical K43-failure example powering the two-gate pattern formalization
- @entities/platforms/polymarket.md — typical consumer venue
- @entities/tools/tradingview-mcp-atilaahmettaner.md — adjacent TA tooling; also NO-GO Phase-0 (TOS gate)

**Brief references (informational; not `related:` per wiki schema)**:
- `briefs/2026-05-10_pandas-ta-classic-adoption.md` — canonical TA library that supersedes this NO-GO verdict

## Raw Concept

What prompted this page: Phase-0 eval verdict (May 13 2026) flagged bukosabino/ta as ADOPT-tier. MIT-licensed, 5.1k stars, 43 indicators in pure Python. Direct adoption candidate for any Cemini strategy module that needs canonical technical-analysis primitives.

## Narrative

### Identity

- **Repo**: `bukosabino/ta` (GitHub)
- **License**: **MIT**
- **Stars**: 5,100+
- **Language**: Python
- **Dependency**: numpy + pandas only
- **Coverage**: 43 technical-analysis indicators

### Indicators included (selected)

| Category | Indicators |
|----------|------------|
| Momentum | RSI, Stochastic, Williams %R, Awesome Oscillator, KAMA, Stochastic RSI, TSI, Ultimate Oscillator, ROC |
| Volatility | Bollinger Bands, Average True Range (ATR), Donchian Channels, Keltner Channels, Ulcer Index |
| Trend | MACD, Aroon, ADX, CCI, DPO, KST, Mass Index, Parabolic SAR, Trix, Vortex |
| Volume | OBV, Chaikin Money Flow, Force Index, Money Flow Index, Negative Volume Index, On Balance Volume, VWAP, Volume Price Trend, Volume Weighted Average Price |
| Others | Daily Return, Daily Log Return, Cumulative Return |

### Adoption posture

**NO-GO 2026-05-13** (Phase-0 source audit revised the source-doc-level ADOPT verdict). See `## Phase-0 audit verdict` below.

### Phase-0 audit verdict (2026-05-13)

| Dimension | Finding | Status |
|-----------|---------|--------|
| License | MIT (verified in LICENSE; Copyright 2020 Darío López Padial) | PASS |
| Maturity (stars / commits / contributors) | 5,062 / 663 over 8.1 yrs / 35 | PASS |
| Last commit | 2026-03-18 (README edit only; library frozen since ~2023) | DRIFT |
| Indicator coverage | 43 claimed → 43 verified | PASS |
| Dependencies | `pandas==1.3.5` + `numpy==1.21.5` pinned (both EOL: pandas Aug 2021, numpy Nov 2022) | FAIL |
| Python 3.12 compat | Issues #340, #348 confirm failures; setup.py supports only ≤3.7 | FAIL |
| Pandas 2.x compat | Issue #357 documents `FutureWarning` from positional indexing deprecations; will break on pandas 2.1+ | FAIL |
| **Parallel-impl check vs `pandas-ta-classic`** (already K30-adopted: see `@briefs/2026-05-10_pandas-ta-classic-adoption.md`) | **Identical 43-indicator set; identical class-based API shape; column-naming overlap; zero novel coverage** | **FAIL — duplicate** |

**Verdict: NO-GO**. Rationale: Cemini already adopted `pandas-ta-classic` for the same 43-indicator coverage. `bukosabino/ta` adds zero novel indicators, ships on stale + EOL pandas/numpy pins, breaks on Python 3.12 and pandas 2.x, and would create either (a) import-namespace conflict, or (b) maintenance burden with no upside.

The K43 source-doc-level ADOPT verdict (5 of 5 ADOPTs MIT-licensed) was a license + indicator-coverage filter only. The Phase-0 audit catches what the doc-level filter missed: **parallel-implementation with an already-adopted tool**.

### Cemini integration target

**None.** `pandas-ta-classic` remains the canonical TA library. See `@briefs/2026-05-10_pandas-ta-classic-adoption.md`.

If a future-state reconsideration becomes warranted (e.g. `pandas-ta-classic` ages out without a maintained successor), the gates are:
1. Upstream modernization to `pandas>=2.1`, `numpy>=1.26`, Python 3.11+ tests green
2. Differentiation: at least one novel indicator or algorithmic improvement not in `pandas-ta-classic`
3. Maintenance cadence proof: ≤6-month SLA on compat updates demonstrated over ≥2 release cycles

### Important caveat — strategy discipline

`@concepts/polymarket-bot-architecture.md` (citing @0x_Punisher's playbook) explicitly flags **layered indicator stacks** (RSI + MACD + divergence) as a documented failure mode:

> "Avoid: layered indicator stacks (RSI + MACD + divergence). Every indicator adds a failure surface."

bukosabino/ta is the **tool**. The discipline is the user's responsibility. The library makes it easy to compute 5 indicators and worship the result; resist.

### Why MIT matters here

Per `@concepts/cemini-license-posture.md`, MIT is the cleanest license for IP-sale-readiness — no copyleft, no notice-on-distribution beyond attribution. Adopting MIT-licensed dependencies means the eventual buyer-of-Cemini-codebase inherits no licensing land mines.

## Snippets

> "5 of 5 ADOPTs are MIT-licensed. License-posture filter eliminates most candidates before maturity even matters." [Source: eval-github-repos-2026-05-13.docx]

## Dead Ends

- **Adopting `bukosabino/ta` alongside `pandas-ta-classic`** (2026-05-13 Phase-0 NO-GO) — identical 43-indicator coverage, no novel indicators, EOL `pandas==1.3.5` + `numpy==1.21.5` pins, fails on Python 3.12 and pandas 2.x. Source-doc ADOPT verdict was MIT-license-filter-only; Phase-0 caught the duplicate. `pandas-ta-classic` retained as canonical.
- **Stacking 5+ indicators from this library into a single strategy** — see above. The library doesn't enforce discipline; the strategy code does. (Inherited caveat — applies equally to `pandas-ta-classic`.)
- **Forking and modifying upstream** — unnecessary even for the canonical TA library. MIT lets you keep a wrapper layer in Cemini and depend on upstream as-is. Forking creates a maintenance burden with no upside.
