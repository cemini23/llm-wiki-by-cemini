---
title: PyBroker — ML-Backtesting Framework (Apache-2.0 + Commons Clause poison pill)
type: entity
tags: [tool, backtesting, numba, ml-trading, apache-2-license, commons-clause, reject-tier, ip-poison-pill]
keywords: [pybroker, edtechre, commons-clause, apache-2-poison-pill, walkforward-analysis, numba-jit, alpaca-yfinance-akshare]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/cemini-license-posture.md
  - entities/tools/hftbacktest.md
  - entities/infrastructure/cemini-stack.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-6-links-eval-batch.md — origin source: K32 Gemini DR eval URL 2, **REJECT** tier — license is the primary kill, redundancy w/ existing stack is the secondary kill
- @concepts/cemini-license-posture.md — Apache-2.0 + Commons Clause = poison-pill mode (catalog mode #5-family). The Commons Clause modifies an otherwise-permissive Apache-2.0 license to forbid commercial use of derivative works
- @entities/tools/hftbacktest.md — Cemini's microsecond-tick backtester (K31 Adopt-tier, brief at `cemini-prod:/opt/cemini/briefs/2026-05-06_hftbacktest-adoption.md`); pybroker would compete for the same role at lower resolution and higher IP risk
- @entities/infrastructure/cemini-stack.md — Cemini already uses Polars (lazy evaluation, Arrow-backed memory) which provides the dataframe acceleration pybroker offers via Numba; architectural redundancy

## Raw Concept

edtechre/pybroker is a specialized algorithmic trading framework engineered specifically for developing, backtesting, and fine-tuning trading rules utilizing machine learning models. Numba-accelerated (LLVM-compiled NumPy) for backtesting speed.

K32 DR verdict: **REJECT**. The Commons Clause amendment to its Apache-2.0 base license forbids selling the software or offering it as a commercial service — this is a poison pill for IP-sale-bound code. Operationally, Cemini's existing Polars + hftbacktest combo already covers pybroker's value-add at higher resolution.

## Narrative

- **URL**: `https://github.com/edtechre/pybroker` ✓ DR-cited
- **License**: Apache-2.0 + Commons Clause (per `https://www.pybroker.com/en/latest/license.html`)
- **Stack**: Python; Numba (LLVM JIT compilation of NumPy loops for accelerated backtesting); built-in adapters for Alpaca, Yahoo Finance, AKShare
- **Capabilities**: walkforward analysis, bootstrapping methodologies, ML-model-driven trading signal generation
- **Maturity**: established project, but not surfaced in DR

### Why the Commons Clause is poison pill for IP sale

Apache-2.0 alone is fully clean (mode #1 of "safe" buckets in license catalog). The **Commons Clause** is a non-OSI-approved amendment that modifies any license to forbid:

> "the right to Sell the Software"

Where "Sell" is defined to include offering the software (or substantial derivatives) as a paid service. Critically:

- Even **studying the source code** with intent to mirror algorithms creates IP-taint risk for the resulting derivative
- LLM coding agents reading Commons-Clause source and emitting similar code may produce derivative works
- An acquirer's M&A due diligence will flag any Commons-Clause dependency in the codebase as a commercial-monetization restriction

Per `monetization_priority_2026.md` memory: license auto-rejects soften for non-prod use. But this case isn't softened because:

1. **There's no laptop-only use case** for pybroker that doesn't ultimately influence prod-stack code (Cemini's research-to-production pipeline is tight)
2. **Architectural redundancy makes the code-study path unattractive**: Polars + hftbacktest already cover the value-add
3. **Clean alternatives exist**: hftbacktest (K31 Adopt) + Polars (already deployed) achieve the same backtesting goals with permissive licenses

### Architectural redundancy with existing Cemini stack

| pybroker offering | Cemini equivalent | Status |
|-------------------|-------------------|--------|
| Numba-JIT NumPy loop acceleration | Polars (Arrow-backed, lazy evaluation, Rust-native) | Already deployed |
| Walkforward backtesting | hftbacktest (microsecond-tick) | K31 Adopt brief staged |
| Yahoo Finance + Alpaca adapters | yfinance EOD fallback (per polygon_not_authorized_doctrine) + future Alpaca if needed | Already deployed |
| Bootstrapping for parameter robustness | Riskfolio-Lib (K30 brief) | Adoption brief staged |
| ML-model integration | DeepSeek API + future custom factor models | Already deployed |

Adopting pybroker would introduce architectural redundancy + Numba JIT compilation overhead + Commons Clause IP taint, with no unique capability vs the existing/staged stack.

### Open questions

- ⚠ Exact RAM envelope for executing walkforward analysis over extended historical datasets via Numba (DR-flagged unknown; not pursued because reject stands regardless)

### Adoption status — REJECT (license + redundancy)

Not adopted. Not under evaluation. License-pattern catalog reinforcement; operational redundancy reinforcement.

## Snippets

### Commons Clause framing (DR direct quote)

> "The repository operates under an Apache-2.0 license severely restricted by the Commons Clause, which explicitly prohibits selling the software or offering it as a commercial service. This modification transforms an otherwise permissive license into a poison pill. Any direct integration, or even deep study that leads to subconscious mirroring of its proprietary algorithms, poses a critical intellectual property taint risk for an acquirer." [Source: 5_6 links.docx URL 2]

### Why architectural redundancy is the secondary kill

> "Operationally, the Cemini stack already utilizes Polars, which relies on lazy evaluation and Arrow-backed memory to achieve high performance. Introducing Numba-compiled NumPy loops introduces architectural redundancy and cognitive overhead for future maintainers without providing a unique operational capability." [Source: 5_6 links.docx URL 2]
