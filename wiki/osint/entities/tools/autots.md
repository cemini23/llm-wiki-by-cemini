---
title: "AutoTS — automated time-series forecasting (Adopt, Cemini analyst-node)"
type: entity
tags: [tool, time-series, forecasting, financial-prediction, mcp-compatible, scikit-learn, gemini-eval-doc1, phase-0-adopt-candidate]
keywords: [autots, automated forecasting, m6 competition, scikit-learn, mcp, winedarksea, analyst-node, prediction-layer]
related:
  - sources/evaluating-github-repos-trading-stack-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - meta/internal-benchmark-deployment-map.md
maturity: draft
created: 2026-05-12
updated: 2026-05-30
gemini_eval_doc1_url: 9
phase_0_verdict: CONDITIONAL-GO 2026-05-17 (MIT verified, MCP server real; laptop resource benchmark PASS 2026-05-30; install `[mcp]` only)
adoption_status: PHASE-0-COMPLETE 2026-05-17
---

## Relations

- `@sources/evaluating-github-repos-trading-stack-2026-05-12.md` — source eval (URL 9)
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — corrected multi-wiki prompt
- `@concepts/tool-evaluation-framework.md` — three-surface methodology
- `@concepts/cemini-license-posture.md` — MIT-clean license posture
- `@meta/internal-benchmark-deployment-map.md` — laptop benchmark routing

## Raw Concept

- **Repo**: `github.com/winedarksea/AutoTS`
- **License** **`[CONFIRMED 2026-05-29]`** — GitHub API **MIT** (`winedarksea/AutoTS`, ~1.4k★).
- **Stars** [per Gemini eval]: ~1,400
- **Tier**: Adopt
- **Primary fit**: Cemini financial (analyst-node prediction layer)

## Narrative

Automated time-series forecasting library; **`[CONFIRMED 2026-05-29]`** author paper in-repo (`docs/catlin_m6_paper.tex`) documents AutoTS deployment in the **M6 Competition** and claims **won the investment decision challenge** (probabilistic monthly stock-basket forecasting). MCP-compatible with scikit-learn API idioms. Direct integration target for Cemini's analyst-node prediction layer.

### Integration vector

Schedule Phase-0 audit (license verification, runtime resource profile, MCP server compatibility check against existing FastMCP container hardening from K39 OpenShell extraction). If clean: file Cemini-prod adoption brief with concrete `agents/orchestrator.py` integration plan.

### Open questions

- Resource footprint (RAM + CPU per forecast batch) vs Cemini analyst-node budget
- MCP compatibility tier (full MCP server vs callable-from-MCP-container)
- M6 placement claim — **`[CONFIRMED 2026-05-29]`** via maintainer paper in repo (investment-decision challenge win); cite `catlin_m6_paper.tex` for external material, not Gemini eval alone

## Phase-0 Audit (2026-05-17)

Repo cloned to `/tmp/ph0-autots/` (shallow); maturity data via `gh api`.

### License — claim vs actual

- **Claim** (Gemini eval): MIT
- **Actual**: **MIT, CONFIRMED.** `LICENSE` file present, verbatim MIT text, "Copyright (c) 2024 Colin Catlin". `gh api` reports SPDX `MIT`; `setup.py` classifier `License :: OSI Approved :: MIT License`. SPDX: **MIT**. No copyleft — IP-sale-safe for production embedding. `[CONFIRMED]`

### Maturity — observed vs claimed (2026-05-17)

| Metric | Claimed (eval) | Observed | Note |
|--------|----------------|----------|------|
| Stars | ~1,400 | **1,409** | Accurate, no inflation |
| Forks | — | 123 | Healthy |
| Open issues | — | 24 | Low — well-tended |
| Last commit | — | **2026-04-15** (~32d) | Active; not abandoned-after-pump |
| Created | — | 2019-11-26 | **~6.5-yr project** — mature, long-lived |
| Contributors | — | 1 (`gh` reports 1; anon count 1) | Single-maintainer bus factor |
| Latest version | — | 1.0.3 (Apr 2026) | Tagged release cadence active |

Maturity is the inverse of the aulekator failure pattern: a 6.5-year-old project with a recent 1.0.3 release and active version cadence. The one real flag is **single-maintainer bus factor** (Colin Catlin) — not disqualifying for an MIT lib (fork-safe), but worth noting.

### Failure-mode probe — license / GPU-MAPPO / dependency footprint

**1. License** — passes (see above).

**2. GPU / MAPPO compatibility signals.** AutoTS is **not** an RL framework — no MAPPO, no `gymnasium`, no `stable-baselines`. It is a scikit-learn-idiom AutoML search over classical forecasters (statsmodels, prophet, xgboost, lightgbm). PyTorch appears **only** in the optional `autots/evaluator/tva/` module (TVA — "Time Variant Architecture", a neural forecasting graph) and is import-guarded (`raise ImportError("BifrostOptimizer requires PyTorch.")`). `torch` is **not** in `install_requires` nor in any `extras_require` group — the core install is pure CPU. Code respects `torch.device(...)` so GPU is supported if torch is installed, but **GPU is never required**. For a CeminiSuite analyst-node on a small Hetzner box, run core + classical models only; the TVA/torch path is opt-in and should be left disabled.

**3. Dependency footprint — light core, heavy extras.** `install_requires` is **only 4 packages**: `numpy`, `pandas`, `statsmodels`, `scikit-learn` — all already standard in any quant Python env. This is a genuinely small core, well-suited to a small Hetzner box. The weight is opt-in via `extras_require`:
- `additional` — pulls `tensorflow`, `xgboost`, `lightgbm`, `prophet`, `scipy`, etc. **`tensorflow` is the heavy item** (~1GB+ install).
- `mcp` — notably **excludes `tensorflow`** but keeps `lightgbm`/`scipy`/`yfinance`/`matplotlib` + `mcp>=1.0.0`. This is the relevant install group for Cemini.

**4. MCP integration — real, first-class.** Earlier eval open question ("full MCP server vs callable-from-container") is resolved: AutoTS ships a **full first-class MCP server**. `console_scripts` entry point `autots-mcp = autots.mcp.server:serve`; a complete `autots/mcp/` package (server, handlers, schemas, cache, data_utils); declares `mcp>=1.0.0` in the `mcp` extra. This is a real MCP server, not a thin wrapper — directly compatible with FastMCP-style container hardening (K39 OpenShell pattern). Repo is 40MB / 113 py files.

### Comparison vs existing Cemini coverage

Cemini's analyst-node currently has no dedicated automated-forecasting layer — the `three-formula-system` (`@concepts/three-formula-system-polymarket-rare-events.md`) is a rare-event sizing model, not a general time-series forecaster, and the NautilusTrader thread is execution/backtest infrastructure. AutoTS fills a genuine gap (general-purpose ticker/series forecasting) rather than duplicating existing coverage. The `extras['mcp']` group is the natural install target — it pairs the forecasting core with a ready MCP surface and deliberately omits TensorFlow.

### Laptop resource benchmark (2026-05-30)

**Laptop job** — `bash scripts/run_autots_benchmark.sh` on the OSINT workspace (yfinance panel; no librarian SSH). Report: `.local/reports/autots-laptop-benchmark-2026-05-30.md`.

| Scenario | Symbols | Rows | Elapsed | Max RSS | Config |
|----------|---------|------|---------|---------|--------|
| single_spy | 1 | 501 | 6.2 s | 309 MB | `model_list=superfast`, `max_generations=1` |
| panel_7 | 7 | 501 | 6.6 s | 312 MB | SPY, AAPL, MSFT, NVDA, XOM, TLT, GLD · 2y daily |

Platform: macOS arm64 · AutoTS **1.0.3** · `pip install autots[mcp]` (no torch/TVA). Template eval errors in stdout are normal AutoML search noise; runs complete. **`[CONFIRMED 2026-05-30]`** — `superfast` batch fits analyst-node budget on a small box for occasional forecasts; cap `model_list` in prod.

### Decision — CONDITIONAL-GO

MIT-clean, mature (6.5 yr, 1,409★, active 1.0.3 release), light 4-package core, and a real first-class MCP server. No copyleft, no abandoned-after-pump signal, no forced GPU/heavy-dep burden. Conditions before a Cemini-prod adoption brief:

1. **Install via the `mcp` extra only** (`pip install autots[mcp]`) — never `[additional]`. The `mcp` group already excludes TensorFlow; do not pull `torch` (TVA path stays disabled on the Hetzner box).
2. **Benchmark resource footprint** — **`[CONFIRMED 2026-05-30]`** laptop PASS (~310 MB RSS, ~7 s per `superfast` batch on 7-symbol panel). Re-benchmark if `model_list` or generation count increases in prod.
3. **Verify the M6 2023 competition-placement claim** before citing it in any external Cemini material — **`[CONFIRMED 2026-05-29]`** via in-repo `docs/catlin_m6_paper.tex` (investment decision challenge). Not a blocker for internal adoption.
4. Single-maintainer bus factor: acceptable for an MIT lib (fork-safe), no mitigation required beyond pinning a known-good version.
