---
title: "FLOX — modular polyglot trading-system framework (MIT)"
type: entity
tags: [entity, tool, trading-framework, adopt-eligible, mit, k57]
keywords: [flox, flox-foundation, trading-system-framework, polyglot-strategies]
related:
  - sources/tool-eval-70urls-k57-2026-05-22.md
  - concepts/polymarket-bot-architecture.md
  - concepts/laptop-prod-research-split.md
  - sources/cemini-laptop-prod-research-handoff-2026-05-23.md
maturity: validated
created: 2026-05-22
updated: 2026-05-24
---

## Relations

- @sources/tool-eval-70urls-k57-2026-05-22.md — URL 10 Adopt (eval); license verified MIT via GitHub API 2026-05-22
- @concepts/polymarket-bot-architecture.md — potential strategy-binding layer for prediction-market bots

## Raw Concept

K57 multi-wiki tool eval URL 10 — `FLOX-Foundation/flox`. Modular framework for building trading systems with polyglot strategy bindings.

## Narrative

- **Repo**: `github.com/FLOX-Foundation/flox`
- **License**: MIT (`license.spdx_id` verified 2026-05-22) [CONFIRMED]
- **Stars**: ~206 (low community vs eval prose)
- **Posture**: **CONDITIONAL-GO (Phase-0 complete 2026-05-22)** — MIT verified; real C++ framework with optional Polymarket connector build flag. **Not a drop-in** for `/opt/cemini` Python/LangGraph core; recommend 1-week architecture spike (backtest-only) before any live wiring.

### Phase-0 audit (2026-05-22)

| Gate | Verdict |
|------|---------|
| G1 License | **PASS** — MIT file + GitHub API |
| G2 Maturity | **PASS** — 206★, CI, PyPI, docs |
| G3 Domain fit | **PARTIAL** — Polymarket in `connectors/` but build optional; heavy C++ toolchain |
| G4 Secrets | **PASS** — env-based live templates |
| G5 IP-sale | **PASS** |

**Verdict: CONDITIONAL-GO** — reference Polymarket connector + backtest path only; no prod execution swap without benchmark.

### Step 197 — Phase 1 build (2026-05-23)

| Host | Result |
|------|--------|
| **macOS laptop** | cmake **FAIL** — no OpenSSL dev headers (LibreSSL-only) |
| **cemini-librarian** | **PASS** — `libflox-connectors.a` built with **polymarket** connector (executor OFF) |

Phase 1a = compile verification (librarian **PASS**). Phase 1b = Polymarket market-channel WS soak **PASS** on librarian (60s, Gamma high-volume token): Python 1 book update vs FLOX 3 `BookUpdateEvent`s; both `first_book_ms` ~300–410. Scripts: `scripts/flox_phase1b_*`. macOS cmake still needs Homebrew `openssl@3`. Brief: `briefs/2026-05-23_flox-phase1b-polymarket-ws-benchmark.md`. See @concepts/laptop-prod-research-split.md.

## Snippets

> "Modular framework for building trading systems with polyglot strategy bindings" [Source: GitHub API description, 2026-05-22]
