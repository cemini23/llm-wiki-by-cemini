## 1. OpenSpec + wiki

- [x] 1.1 Create OpenSpec change `cemini-backtest-report-kit` (proposal, design, specs, tasks)
- [x] 1.2 Add `wiki/concepts/cemini-backtest-report-kit.md` with relations + narrative
- [x] 1.3 Add `wiki/meta/pm-lp-backtest-cadence.md` and ritual hook in `CLAUDE.md` §3

## 2. Shared report kit (Phase 0)

- [x] 2.1 `scripts/cemini_backtest_report/report.py` — `ReportConfig`, `generate_report()`
- [x] 2.2 `scripts/cemini_backtest_report/__init__.py` exports

## 3. PM LP pilot

- [x] 3.1 `scripts/pm_lp_backtest/fetch.py` — Gamma markets + CLOB history + cache
- [x] 3.2 `scripts/pm_lp_backtest/engine.py` — hourly LP simulation
- [x] 3.3 `scripts/pm_lp_backtest/sweep.py` — parameter grid
- [x] 3.4 `scripts/pm_lp_backtest/run.py` — CLI + report emission
- [x] 3.5 `scripts/run_pm_lp_backtest.sh` — one-shot runner

## 4. Ship + document

- [x] 4.1 Run pilot; verify `.local/reports/pm-lp-backtest-*.html` opens
- [x] 4.2 Update `wiki/index.md`, `wiki/log.md`; run `wiki_lint.py`
- [x] 4.3 User: commit/push when ready (not agent-initiated)

## 5. Phase 1 — Kalshi LP pilot

- [x] 5.1 `scripts/kalshi_lp_backtest/` + runner + cadence check
- [x] 5.2 OpenSpec spec `kalshi-lp-backtest-pilot`
- [x] 5.3 Run report; wiki + `CLAUDE.md` §5
