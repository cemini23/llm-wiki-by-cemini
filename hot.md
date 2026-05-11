# Hot — session-state cache

Ephemeral curator working memory. Read first on session start; rewritten at session end. Gitignored.

## Position (end of 2026-05-10 session — K36 complete on top of K35 + cross-wiki route to seo-wiki)

- **K-series K36 (NEW)**: 17-URL trading-stack evaluation brief ingested. 17 wiki pages: 1 source + 14 tool entities + 2 concepts. Tier rollup: 4 Adopt (picobot, ctop, QuantMuse, Adala) + 4 Steal-from (mercury-agent, Tmux-Orchestrator, digital-marketing-pro, LLMops) + 1 split (finance-skills) + 2 Reference/Defer (terax-ai, data-formulator) + 3 Reject (AppFlowy AGPL-3.0, dflash CUDA, floci AWS-emulator) + 3 UNAVAILABLE. Concept patterns extracted: `cross-channel-agent-gateway.md` (picobot + mercury) + `declarative-data-labeling-skills.md` (Adala + finance-skills).
- **K36 cross-wiki route**: URL 10 digital-marketing-pro → seo-wiki brief `2026-05-10_digital-marketing-pro-claude-ecosystem.md` (115 cmds + 67 MCP servers + 5-layer memory + A+→F grading scripts for local SEO/GEO content authoring).
- **K36 Phase-0 audit queue**: picobot, QuantMuse, Adala (prod blast radius); ctop + finance-skills laptop-only (lower blast radius, audit deferred).
- **K36 prod-Adopt rank**: QuantMuse #1 (Python+C++17 core stack, strip LangChain bloat). picobot #2 (single 9 MB MCP-native Go gateway, retires need for `python-telegram-bot` in orchestrator).
- **K-series K35**: 4-source eval batch (55 tools + 1 paper, SSRN 4943355). 32 wiki pages. Three-surface methodology codified. SPJ bias-correction extracted.
- **Cross-wiki paths**: All 4 CLAUDE.md cross-wiki alias tables converted to relative paths (portable between machines).
- **K35 brief queue**: 10 of 10 Adopt-tier briefs staged. 4 prod (tradingview-mcp GO, pandas-ta-classic CONDITIONAL-GO, polymarket-paper-trader GO, chaosblade GO) + 6 workspace-laptop (aris, github-spec-kit, tech-debt-skill, claude-mem, revpdf, codeboarding — all GO).
- **K35 Phase-0 verifications COMPLETE 2026-05-10**: claude-mem (Apache-2.0), github-spec-kit (MIT, Claude integration upstream), codeboarding (MIT, Node 20.18.1 auto-bootstrap) — all 3 upgraded from CONDITIONAL-GO to GO.
- **Wiki**: 624 pages indexed (+17 K36). Lint: PASS, 0 cross-wiki dangling.
- **Raw sources moved** → `cemini-librarian:/opt/cemini-bulk/research/`; local copies removed.
- **Inbox**: CLEAN.
- **Step 81**: ✅ sshd installed + hardened on `cemini-prod`.
- **Step 82**: PARTIAL PASS — Conductor pipeline ✅, Stash ✅, Calibration ✅. Redis/EMS ❌.

## Monetization-priority directive (2026-05-06)

User: "license its going to be a bit before we sell but i need to start making money here with this soon so we need to do what we need to do."

Effects: license auto-rejects soften for non-prod-codebase use. Phase-0 audit rigor unchanged. Saved as project memory `monetization_priority_2026.md`. Re-confirm 2027+.

## Current state — Step 81 complete, Step 82 partial pass awaiting Redis + EMS

Step 81 (sshd) and Step 82 (Conductor smoke test) both ran during the prior session window. Step 81 completed cleanly. Step 82 blocked by Redis + EMS (both missing on prod).

### Shipped workspace-laptop briefs

| Brief | Status |
|-------|--------|
| `briefs/2026-05-06_obsidian-llm-wiki-local-steal-from.md` | Phase 1 ✓ / Phase 2 deferred (bundles with brief-audit-upgrade sprint) |
| `briefs/2026-05-07_regime-disclosure-brief-audit-gate.md` | **SHIPPED 2026-05-08** — `scripts/skill_audit.py` v0.2 with regime-disclosure veto gate, all tests PASS |
| `briefs/2026-05-09_step81-sshd-prod.md` | **SHIPPED 2026-05-09** — sshd installed + hardened on `cemini-prod` |

skill_audit v0.2: 7 checks, regime-disclosure is a veto gate (Scientific Integrity). Static score weights rebalanced: required_sections 0.25, crosslinks 0.15, citations 0.15, needs_verification 0.10, prose_quality 0.10, frontmatter 0.05, regime_disclosure 0.10.

### Bundled brief-audit upgrade sprint (NOT YET DRAFTED)

K32+K33 surfaced 4 STEAL-FROM/concept-driven upgrades that all touch `scripts/skill_audit.py`:
- `academic-paper-skills` 35-point peer-review framework (K32, highest priority — 4-6 hr port)
- `research-paper-writing-skills` claim-evidence + abstract synthesis (K32, 2-3 hr port)
- `codex-startup-pressure-test-skill` adversarial review prompts (K32, 1-2 hr port)
- **Regime-disclosure gate** (K33, SHIPPED 2026-05-08) — 1-2 hr, independent-shippable
- **Plus `_llm_retry.py` helper** (Phase 2 of obsidian brief) — bundles with sprint

Decision pending: bundle as one combined `brief-audit-upgrade-sprint.md` (~13 hr) OR ship sequentially.

### 16 active prod briefs at `cemini-prod:/opt/cemini/briefs/` (12 existing + 4 new K35 Adopt)

| Brief | What it ships |
|-------|---------------|
| `2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md` | Tennis Elo math + commercial-data sourcing |
| `2026-05-04_quant-libs-fastmcp-integration.md` | Riskfolio-Lib + FinanceToolkit + FinanceDatabase (K30-updated) |
| `2026-05-04_probablyprofit-pattern-extraction.md` | Kelly + ensemble + kill-switch |
| `2026-05-05_polymarket-stack-adoption.md` | Polymarket Agents + python-order-utils + py-clob-client + polymarket-mcp-server |
| `2026-05-05_pykalashi-adoption.md` | pykalashi replaces bloated official Kalshi SDK |
| `2026-05-05_conductor-audit-trail-phase1.md` | Conductor fitness function + audit JSONL + git-tracked config commits |
| `2026-05-06_hftbacktest-adoption.md` (K31) | Microsecond-tick HFT backtester |
| `2026-05-06_guidance-ai-adoption.md` (K31) | Microsoft structured-generation library |
| `2026-05-06_ttok-prod-install.md` (K31) | ttok Pipfile addition + pre-call audit hook |
| **`2026-05-09_step81-sshd-prod.md`** | OpenSSH hardening on `cemini-prod` — **COMPLETE** ✅ |
| *`2026-05-09_polymarket-onchain-data-pipeline.md`* | Polymarket on-chain data pipeline — **GO** ✅ |
| *`2026-05-09_sabr-geometry-aware-calibration.md`* | SABR GeoResNN calibration — **CONDITIONAL-GO** (audit first) |
| *`2026-05-09_mcp-context-optimization-stack.md`* (K34) | 4-layer MCP optimization (lazy-tool + claude-code-router + client opts + OpenRouter caching) — **GO** ✅ |
| **`2026-05-10_tradingview-mcp-adoption.md`** (K35 NEW) | TradingView MCP sidecar — 130+ technical analysis tools → LangGraph — **GO** (license pending) |
| **`2026-05-10_pandas-ta-classic-adoption.md`** (K35 NEW) | 252 indicators + 62 candlestick patterns → orchestrator calc nodes — **CONDITIONAL-GO** (license + bridge latency) |
| **`2026-05-10_polymarket-paper-trader-adoption.md`** (K35 NEW) | 26 MCP tools, paper trading sandbox for LLM strategy forward-testing — **GO** |
| **`2026-05-10_chaosblade-adoption.md`** (K35 NEW) | Docker Compose chaos engineering, time-gated to maintenance windows — **GO** |

### 6 K35 workspace-laptop briefs (NEW 2026-05-10)

| Brief | What it ships | Verdict |
|-------|---------------|---------|
| `briefs/2026-05-10_aris-adoption.md` | ARIS Markdown skill files for `/idea` → `/experiment` → `/paper` workflow | GO |
| `briefs/2026-05-10_github-spec-kit-adoption.md` | Spec-Driven Development CLI for wiki → production code transitions | GO (Phase-0 verified 2026-05-10: MIT, Claude integration ships upstream) |
| `briefs/2026-05-10_tech-debt-skill-adoption.md` | Quarterly Cemini codebase technical-debt audits | GO |
| `briefs/2026-05-10_claude-mem-adoption.md` | Cross-session persistent observation memory | GO (Phase-0 verified 2026-05-10: Apache-2.0, configurable inject limit default 5) |
| `briefs/2026-05-10_revpdf-adoption.md` | 15MB offline PDF editor for research extraction | GO |
| `briefs/2026-05-10_codeboarding-adoption.md` | Auto-generated Cemini architecture diagrams | GO (Phase-0 verified 2026-05-10: MIT, Node 20.18.1 auto-bootstrap, macOS CI passing) |

### 2 deferred-with-triggers prod briefs (unchanged)

| Brief | Trigger |
|-------|---------|
| `2026-05-04_autoresearch-conductor-evolution.md` (Phases 2-6) | traffic ≥ 3,500 Conductor decisions/week sustained ≥ 2 weeks AND explicit buyer/research signal |
| `2026-05-04_xskill-cross-rollout-critique-conductor.md` | same |

## Open follow-ups

- **K36 Phase-0 audits** (queued): picobot, QuantMuse, Adala. Order of priority follows production blast radius — verify license/maturity/build-on-target before drafting prod adoption briefs.
- **K36 laptop-only installs** (low-friction): `ctop` via `npm i -g ctop-claude` or Homebrew; `finance-skills` via `npx plugins add himself65/finance-skills`. Verify on next session start.
- **K36 Steal-from extractions** (DEFERRED, no rush): mercury-agent shell-exec + SQLite FTS5; Tmux-Orchestrator `schedule_with_note.sh` + auto-commit pattern; digital-marketing-pro hallucination-detection + evals.json schema; LLMops regex cleaning + LLM-as-judge prompts.
- **Brief-audit upgrade sprint decision** — bundle vs sequential. Regime-disclosure gate (K33) already shipped standalone; remaining 3 STEAL-FROMs + `_llm_retry.py` await decision.
- **Phase 4 of obsidian-llm-wiki-local** — `wiki_lint.py --fix-bidirectional` mode is standalone-shippable (~30 min). Low priority.
- **Cemini-prod ttok install** — staged; awaits prod-side execution (single Pipfile addition).
- **hftbacktest Phase 0 audit** — GO (MIT license, Production/Stable v2.4.4, wheel install on Hetzner confirmed). Brief `2026-05-06_hftbacktest-adoption.md` updated and ready for prod staging. Phase 1 sandbox replication is next.
- **Step 82 blockers: Redis + EMS** — must be resolved before Step 83 live deployment
- **Sakana 2026-04-27 NV tags Exa-resolution** — **DONE 2026-05-10**. 11 tags across 4 pages: 3 resolved, 1 partially resolved, 6 re-dated (Fugu commercial details still undisclosed), 1 re-tagged as NEEDS FOUNDER INPUT (§174 R&E spend). Key finding: Conductor codebase NOT open source (arXiv v5 dropped the v2 promise; TechieTricks confirms). Trinity worker pool confirmed (7 models). Log entry at `wiki/log.md`.
- **Tier 2 arXiv sweep** — last 2026-05-01; due ~2026-05-08 per 7-day cadence.
- **Storage compaction** — disk 88% full; market-dataset Parquet conversion + research-corpus SQLite FTS index.

## Key file locations (end of 2026-05-10)

- ROADMAP: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/ROADMAP.md`
- log: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/log.md`
- index: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/index.md`
- license catalog: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/concepts/cemini-license-posture.md`
- staged brief: `briefs/2026-05-09_step81-sshd-prod.md` (SHIPPED)
- step 82 brief: `briefs/2026-05-09_step82-production-smoke-test.md` (PARTIAL PASS)
- scripts: `scripts/skill_audit.py` v0.2 (regime-disclosure gate shipped)
- raw source: `cemini-librarian:/opt/cemini-bulk/research/5_6 links.docx` (K31), `Evaluating Code for Trading Stacks.docx` (K36)
- prod ccd-cli: `cemini-prod:/root/.claude/remote/ccd-cli/{2.1.111,2.1.128}`
- rewind config: stored in rewind's own keystore; `rewind config show` to see redacted state
- laptop `.env`: contains `DEEPSEEK_API_KEY`, `LIBRARIAN_API_KEY`, `GROQ_API_KEY`, `GEMINI_API_KEY`

## Session-start ritual reminders

1. Read this file
2. Check `wiki/sweeps/*.md` mtime — sweep due ~2026-05-08
3. Check `research to be indexed/` for new sources (currently empty)
4. If prod desktop-app fails on first message after a Claude Code update: verify `ssh cemini-prod 'env | grep IS_SANDBOX'` returns `IS_SANDBOX=1`.
