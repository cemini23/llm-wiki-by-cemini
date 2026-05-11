# Hot — session-state cache

Ephemeral curator working memory. Read first on session start; rewritten at session end. Gitignored.

## Position (end of 2026-05-10 session — K36 Phase-0 + 2 prod briefs SHIPPED + claude-mem INSTALLED + 3d-wiki SYNCED + skill_audit v0.3 SHIPPED)

- **K-series K36 (NEW)**: 17-URL trading-stack evaluation brief ingested. 17 wiki pages: 1 source + 14 tool entities + 2 concepts. Tier rollup: 4 Adopt (picobot, ctop, QuantMuse, Adala) + 4 Steal-from (mercury-agent, Tmux-Orchestrator, digital-marketing-pro, LLMops) + 1 split (finance-skills) + 2 Reference/Defer (terax-ai, data-formulator) + 3 Reject (AppFlowy AGPL-3.0, dflash CUDA, floci AWS-emulator) + 3 UNAVAILABLE. Concept patterns extracted: `cross-channel-agent-gateway.md` (picobot + mercury) + `declarative-data-labeling-skills.md` (Adala + finance-skills).
- **K36 cross-wiki route**: URL 10 digital-marketing-pro → seo-wiki brief `2026-05-10_digital-marketing-pro-claude-ecosystem.md` (115 cmds + 67 MCP servers + 5-layer memory + A+→F grading scripts for local SEO/GEO content authoring).
- **K36 Phase-0 audits COMPLETE 2026-05-10**:
  - **picobot GO ✅** — MIT, 86 commits, v0.2.0, pure-Go SQLite (`modernc.org/sqlite v1.46.1`), stdio MCP per spec at `internal/mcp/client.go:34-50`
  - **QuantMuse NO-GO ❌ (downgrade from K36 source brief Adopt #1)** — "C++ engine" is cosmetic pybind11-wrapped Python with 100 ms sleep loops; VaR is just `np.percentile(returns, 5)`; 9 commits / 0 tags / 10mo stale; no Hyperliquid adapter; 36 KB LangChain bloat. **Anti-pattern caught**: Phase-0 audits must read source files, not directory structure or README claims, when verifying performance-critical adoptions.
  - **Adala GO ✅** — Apache-2.0, abandonment-risk DEBUNKED (last main commit 2026-05-08, 677 total, 113 in last 6 months; project is unreleased-dev since v0.0.4 NOT abandoned). DeepSeek `base_url` override CONFIRMED via `LiteLLMChatRuntime` (line 134, 140). Strongest K36 ingest-side asset.
- **K36 prod briefs SHIPPED 2026-05-10**:
  - `briefs/2026-05-10_picobot-prod-adoption.md` (7917 bytes, skill_audit 90/100 PASS) → SCPed to `cemini-prod:/opt/cemini/briefs/`
  - `briefs/2026-05-10_adala-prod-adoption.md` (9963 bytes, skill_audit 90/100 PASS) → SCPed to `cemini-prod:/opt/cemini/briefs/`
- **K36 laptop installs**: `ctop` INSTALLED 2026-05-10 (npm i -g ctop-claude → binary at `/Users/claudiobarone/.local/bin/ctop`, MIT confirmed). finance-skills install path still unclear (`npx plugins add` syntax unverified).
- **K35 laptop installs**: `claude-mem` v13.0.1 INSTALLED 2026-05-10 (`npx claude-mem install`, Apache-2.0). Worker + ChromaDB MCP supervisor running. Defaults verified: `SEMANTIC_INJECT_LIMIT=5`, lazy injection (`SEMANTIC_INJECT=false`), `~/.claude-mem` data dir. Claude Desktop OAuth token stale per `oauth-stale.marker` — re-login to refresh (worker functional regardless). Phase 1 3-session smoke test pending 2026-05-11+.
- **Librarian infra**: `3d-printing-wiki` SYNCED to `cemini-librarian:/opt/cemini-wiki/3d-printing-wiki/` 2026-05-10, kb-server reindex `46 ingested / 2 skipped`. All 4 wikis (osint/image-gen/seo-geo/3d-printing) now queryable via `conductor_query` unified search.
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

### Brief-audit upgrade sprint — SEQUENTIAL, step 1 SHIPPED 2026-05-10

Decision: sequential ship. Step 1 done.

- **academic-paper-skills 35-pt framework (K32) — SHIPPED 2026-05-10** as `scripts/skill_audit.py` v0.3. 10 static checks total; 3 new ones (`brief_completeness` + `risk_discipline` + `phasing`) consume the 0.10 weight headroom left by v0.2, bringing max static score to 100. Adoption-class gate `_is_adoption_brief()` exempts ops/research briefs from new checks. Calibration verified on 7 briefs: K36 fresh (picobot 99.5, adala 100) PASS, ops briefs PASS-with-N/A, older adoption briefs (hftbacktest, guidance-ai) WARN at 98/100 flagging genuine gaps (no explicit `**GO**` verdict, bullet-format risks vs tables).
- `research-paper-writing-skills` claim-evidence + abstract synthesis (K32, ~2-3 hr) — **NEXT SEQUENTIAL**
- `codex-startup-pressure-test-skill` adversarial review prompts (K32, ~1-2 hr) — pulls in `_llm_retry.py` helper for first dynamic check
- **Regime-disclosure gate** (K33) — SHIPPED 2026-05-08 (v0.2)
- LLM-as-judge dynamic checks deferred until `_llm_retry.py` (Phase 2 of obsidian brief) ships

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
| **`2026-05-10_picobot-prod-adoption.md`** (K36 NEW) | Cross-channel agent gateway (Telegram/Discord/Slack/WhatsApp ↔ FastMCP) — **GO** (Phase-0: MIT, pure-Go, v0.2.0 + 86 commits) |
| **`2026-05-10_adala-prod-adoption.md`** (K36 NEW) | Declarative data-labeling framework retires hand-rolled DeepSeek loops in GDELT/SEC ingest — **GO** (Phase-0: Apache-2.0, active dev, DeepSeek base_url override verified) |

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

- **K36 Phase-0 audits**: COMPLETE 2026-05-10 — picobot GO + brief SHIPPED, Adala GO + brief SHIPPED, QuantMuse NO-GO downgrade (cosmetic C++ engine caught via source-file read).
- **K36 live-test gates**: Adala DeepSeek smoke **PASSED 2026-05-10** (`LiteLLMChatRuntime(base_url=...)` returned `{'response': 'ack'}` from DeepSeek in 1.9 s; 3 hits on `api.deepseek.com`, 0 on `api.openai.com`). All Adala adoption gates cleared. picobot Phase 1 7-day RAM/CPU soak still pending (target <25 MB resident).
- **K36 laptop-only installs**: `ctop` INSTALLED 2026-05-10 (`/Users/claudiobarone/.local/bin/ctop`, MIT confirmed); pending interactive verification alongside live Claude Code session. `finance-skills` install path still unclear (`npx plugins add` may not be a real Claude Code command).
- **claude-mem Phase 1 verification** — DUE 2026-05-11+: run 3 sessions over 2-3 days, verify (a) observations persist across sessions, (b) `SessionStart` injection content is relevant, (c) injection stays within top-5 cap. Track via `http://localhost:37702`. If false-positive rate >20% or token-budget drift observable, downgrade to reference-only.
- **K36 Steal-from extractions** (DEFERRED, no rush): mercury-agent shell-exec + SQLite FTS5; Tmux-Orchestrator `schedule_with_note.sh` + auto-commit pattern; digital-marketing-pro hallucination-detection + evals.json schema; LLMops regex cleaning + LLM-as-judge prompts.
- **Brief-audit upgrade sprint** — sequential, step 1 (academic-paper-skills 35-pt) **SHIPPED 2026-05-10 as skill_audit.py v0.3**. Next sequential: research-paper-writing claim-evidence (K32, ~2-3 hr), then codex pressure-test prompts + `_llm_retry.py` (~3 hr combined).
- **Phase 4 of obsidian-llm-wiki-local** — `wiki_lint.py --fix-bidirectional` mode is standalone-shippable (~30 min). Low priority.
- **Cemini-prod ttok install** — staged; awaits prod-side execution (single Pipfile addition).
- **hftbacktest Phase 0 audit** — GO (MIT license, Production/Stable v2.4.4, wheel install on Hetzner confirmed). Brief `2026-05-06_hftbacktest-adoption.md` updated and ready for prod staging. Phase 1 sandbox replication is next.
- **Step 82 blockers: Redis + EMS** — must be resolved before Step 83 live deployment
- **Sakana 2026-04-27 NV tags Exa-resolution** — **DONE 2026-05-10**. 11 tags across 4 pages: 3 resolved, 1 partially resolved, 6 re-dated (Fugu commercial details still undisclosed), 1 re-tagged as NEEDS FOUNDER INPUT (§174 R&E spend). Key finding: Conductor codebase NOT open source (arXiv v5 dropped the v2 promise; TechieTricks confirms). Trinity worker pool confirmed (7 models). Log entry at `wiki/log.md`.
- **Tier 2 arXiv sweep** — last 2026-05-01; due ~2026-05-08 per 7-day cadence.
- **Storage compaction** — claim of "disk 88% full" needs re-verification; recent `df` snapshot showed `/dev/sda1` at 22%. May be stale carryover from earlier session.

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
