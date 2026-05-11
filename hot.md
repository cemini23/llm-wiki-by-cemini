# Hot — session-state cache

Ephemeral curator working memory. Read first on session start; rewritten at session end. Gitignored.

## Position (end of 2026-05-11 session — K37 + K38 ingest COMPLETE + markdown-preview-pluk INSTALLED + Weather-pair Phase-0 VERDICTS RECORDED)

- **K37/K38 follow-ups closed 2026-05-11**:
  - **markdown-preview-pluk INSTALLED**: v0.0.21 via direct DMG (Homebrew not present on this Mac); `/Applications/Markdown Preview.app`; MIT license + Apple Developer-ID signed (TeamID `5P3TSMNV42`); 632★ / 20 releases in 13 days / pre-1.0. Entity bumped `maturity: validated`. Default-handler set deferred (user manual action — `duti` not installed).
  - **Visual Crossing Weather Phase-0 CONDITIONAL-GO**: adopt for backtesting/climatology only. Vendor 2003-founded (~23 yrs), 99.9% SLA, commercial-use rights on all 4 plans, 50-yr historical depth verified. **Critical interpolation gap** — historical data is grid-interpolated NOT station-direct; excludes from contract-resolution path. Free tier ($0/mo) sufficient at 5 airports × 15-min cadence (480 records/day under 1K cap).
  - **wethr.net Phase-0 GO**: adopt for live Kalshi/Polymarket-resolution path. Built explicitly for those markets; 30 US airports (full Kalshi roster); **explicit `logic=nws` vs `logic=wu` parameter** for contract-resolution alignment; station-direct (not interpolated). Pro $24.99/mo. Vendor-age <12 mo (open beta 2025-05-14) is dominant risk, mitigated via NWS parallel-poll circuit breaker.
  - **Pair verdict: GO on both** — non-overlapping roles (VC = backtesting depth; wethr.net = live resolution truth). Combined ~$25/mo at audited cadence. Bidirectional backlinks added on `nws-weather-gov.md` + `open-meteo.md`.
  - **Weather pair DEFERRED 2026-05-11** (no spend now per user). Phase-0 verdicts locked; prod brief drafting awaits activation trigger: first Kalshi weather strategy reaches paper-trade phase OR user clears $24.99/mo wethr.net Pro subscription. Filed in `ROADMAP.md` Deferred-with-triggers section. Both entity pages carry `adoption_status: DEFERRED` frontmatter.

## Position (mid-2026-05-11 session — K37 + K38 + 3-paper ingest COMPLETE)

- **K-series K37 (NEW)**: 21-URL "Evaluating URLs for System Integration" eval brief ingested. 14 pages: 1 source + 13 entity stubs (8 reachable + 5 UNAVAILABLE stubs). Tier rollup: 3 Adopt (Visual Crossing Weather, UI-TARS-desktop, markdown-preview-pluk), 6 Steal-from (claude-bootstrap, ASB, Beever Atlas, homelab-hub, ebay-mcp, contextlattice), 3 Reference-only, 1 Defer, 8 UNAVAILABLE.
- **K-series K38 (NEW)**: 29-URL "Link Evaluation Brief for Trading Stack" eval brief ingested. 26 pages: 1 source + 25 entity stubs. Tier rollup: 6 Adopt (Readme.skill, Perplexity MCP, Google Colab VSCode, 9router, guild MCP, wethr.net), 6 Steal-from (google-research, CloddsBot, AI-Trader, MegaMemory, hackers-arise OSINT, METATRON), 5 Reference-only, 3 Defer, 5 Reject (Medusa AGPL hard reject + TokenSpeed + tropicaltidbits + D3Ext/WEF + ssh-keys-manager-stmol), 4 UNAVAILABLE.
- **K37/K38 papers (NEW)**: 3 PDFs ingested alongside the eval briefs.
  - **Reinforced Agent** (Apple, arXiv 2604.27233v1) — **HIGH-fit Conductor**. Reviewer agent gates provisional tool calls pre-execution. +5.5% BFCL irrelevance, +7.1% τ²-Bench, o3-mini 3:1 benefit-risk, GEPA +1.5-2.8%. Latency: 6.2× single-turn / 2.4× multi-turn (Cemini multi-turn trading regime is the favorable amortization side).
  - **Signals** (DigitalOcean, arXiv 2604.00356v1) — **HIGH-fit Conductor**. Cheap non-LLM signals (interaction/execution/environment families) attached to every trajectory. 82% informativeness vs 74% heuristic / 54% random. ~200-300 LOC drop-in on top of audit JSONL.
  - **ODINI** (BGU 2018, air-gap magnetic-field exfil) — Reference-only context.
- **2 new concept pages**: `concepts/reviewer-agent-inference-time-feedback.md` + `concepts/agent-trajectory-triage-signals.md`. Architectural complement — reviewer is inline-time, signals are post-hoc.
- **Cross-wiki routes (3)**: `markdown-preview-pluk` routed as briefs to image-gen-wiki + seo-wiki + 3d-printing-wiki. All 3 wikis are markdown-based; macOS native previewer with LaTeX+Mermaid benefits each.
- **Pages touched this session**: 45 new (5 source + 38 entity + 2 concept). index.md + log.md updated. wiki/sources/ has K37+K38 source pages with full Tier rollups.
- **Wiki**: 669 pages indexed (+45 K37/K38). Lint: 0 cross-wiki dangling; all other counts at baseline (pre-existing orphans/bidir-gaps/etc).
- **Raw sources moved** → `cemini-librarian:/opt/cemini-bulk/research/` 2026-05-11; local copies removed.
- **Inbox**: CLEAN.

## Position (end of prior 2026-05-10 session — K36 Phase-0 + 2 prod briefs SHIPPED + 5-tool laptop adoption batch INSTALLED + ARIS deferred + skill_audit v0.5 SHIPPED w/ DeepSeek LLM-as-judge)

- **K-series K36**: 17-URL trading-stack evaluation brief ingested. 17 wiki pages: 1 source + 14 tool entities + 2 concepts. Tier rollup: 4 Adopt (picobot, ctop, QuantMuse, Adala) + 4 Steal-from (mercury-agent, Tmux-Orchestrator, digital-marketing-pro, LLMops) + 1 split (finance-skills) + 2 Reference/Defer (terax-ai, data-formulator) + 3 Reject (AppFlowy AGPL-3.0, dflash CUDA, floci AWS-emulator) + 3 UNAVAILABLE. Concept patterns extracted: `cross-channel-agent-gateway.md` (picobot + mercury) + `declarative-data-labeling-skills.md` (Adala + finance-skills).
- **K36 cross-wiki route**: URL 10 digital-marketing-pro → seo-wiki brief `2026-05-10_digital-marketing-pro-claude-ecosystem.md`.
- **K36 Phase-0 audits COMPLETE 2026-05-10**: picobot GO ✅, QuantMuse NO-GO ❌, Adala GO ✅. Both GOs shipped to prod as adoption briefs.
- **K36 prod briefs SHIPPED 2026-05-10**: `picobot-prod-adoption.md` + `adala-prod-adoption.md` (both 90+/100 skill_audit PASS, SCPed to `cemini-prod:/opt/cemini/briefs/`).
- **K36 laptop installs**: `ctop` INSTALLED 2026-05-10; finance-skills DONE 2026-05-10 (6 plugins / 24 skills); LICENSE missing → upstream issue #64 filed.
- **K35 laptop installs (5 of 6 done 2026-05-10)**: claude-mem, revpdf, specify-cli, codeboarding, tech-debt-skill. Phase 2 smoke tests pending.
- **ARIS DEFERRED 2026-05-10**: 78-skill scope (vs 3 in eval brief); deferred selective triage.
- **skill_audit v0.5 SHIPPED 2026-05-10**: opt-in `--llm-mode` flag, DeepSeek-backed 4-mode pressure-test, 3-tier retry helper `_llm_retry.py`. Sprint COMPLETE for K32 batch.
- **Step 81 (sshd)**: ✅ COMPLETE. **Step 82 (smoke test)**: PARTIAL PASS — Redis + EMS still blockers.

## Monetization-priority directive (2026-05-06)

User: "license its going to be a bit before we sell but i need to start making money here with this soon so we need to do what we need to do."

Effects: license auto-rejects soften for non-prod-codebase use. Phase-0 audit rigor unchanged. Saved as project memory `monetization_priority_2026.md`. Re-confirm 2027+.

## Open follow-ups (K37/K38 — NEW)

- **K37/K38 Phase-0 audits queue** — license verification pending for the 12+ Steal-from items (CloddsBot, AI-Trader, MegaMemory, ebay-mcp, Beever Atlas, contextlattice, METATRON, hackers-arise tutorial, ASB, homelab-hub, claude-bootstrap, google-research subfolders). All low-risk (patterns/algorithms only, no code lift) but should be checked before any actual extraction.
- **Conductor reviewer-agent prototype** — Reinforced Agent pattern fits Cemini's Conductor architecture directly. DeepSeek-R1 reviewer + DeepSeek-V3 base. Selective-trigger gating discipline (always-review on `place_order`/`withdraw`; skip-review on read-only) recovers single-turn latency. Recommended next step: ~200-400 LOC Phase-0 prototype.
- **Signals audit-JSONL prototype** — DigitalOcean Signals pattern is the smallest possible win (~200-300 LOC). Phase 0: add `signals` field to audit JSONL schema; Phase 1: operator dashboard filter; Phase 2: claude-mem observation prioritization; Phase 3: future preference-data pipeline.
- **K38 Adopt cluster — weather/prediction-markets**: wethr.net is the singular weather Adopt for Kalshi/Polymarket weather contracts. Pair with K37 Adopt Visual Crossing Weather (50-yr historical depth) for full weather strategy stack.
- **K38 Adopt cluster — MCP infrastructure**: Perplexity MCP (live-search gap closer), 9router (token-compressing proxy, ~65% reduction claim), guild MCP (Go binary, BM25 + int8 ONNX hybrid retrieval — potential Ollama replacement on Hetzner CPX21).
- **8 UNAVAILABLE URLs from K37** (URLs 1, 6, 8, 10, 11, 12, 16, 19) — flagged for Exa-resolution in a follow-up pass. Tier 1 gap detection will catch as cited-unread stubs.
- **4 UNAVAILABLE URLs from K38** (URLs 17, 20, 24, 25) — same.

## Open follow-ups (carried from 2026-05-10)

- **claude-mem Phase 1 verification** — DUE 2026-05-11+: 3 sessions over 2-3 days. Track via `http://localhost:37702`.
- **K36 live-test gates**: picobot Phase 1 7-day RAM/CPU soak still pending (<25 MB resident target).
- **K36 Steal-from extractions** (DEFERRED): mercury shell-exec + SQLite FTS5; Tmux-Orchestrator `schedule_with_note.sh` + auto-commit; digital-marketing-pro hallucination-detection + evals.json schema; LLMops regex cleaning + LLM-as-judge prompts.
- **Cemini-prod ttok install** — staged; awaits prod-side execution.
- **Step 82 blockers: Redis + EMS** — must resolve before Step 83 live deployment.
- **Tier 2 arXiv sweep** — last 2026-05-01; **DUE — 10 days overdue per 7-day cadence**.

## Key file locations (end of 2026-05-11)

- ROADMAP: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/ROADMAP.md`
- log: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/log.md`
- index: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/index.md`
- license catalog: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/concepts/cemini-license-posture.md`
- new sources (5): `wiki/sources/{evaluating-urls-system-integration,link-evaluation-brief-trading-stack,odini-air-gap-magnetic-field,reinforced-agent-tool-calling-feedback,signals-trajectory-triage}.md`
- new concepts (2): `wiki/concepts/{reviewer-agent-inference-time-feedback,agent-trajectory-triage-signals}.md`
- cross-wiki briefs (3): `../projects/{Image gen,SEO:GEO B&M Business,3d printing}/briefs/2026-05-11_2026-05-11_markdown-preview-pluk-cross-wiki.md`
- raw sources at librarian: `cemini-librarian:/opt/cemini-bulk/research/{Evaluating URLs for System Integration.docx,Link Evaluation Brief for Trading Stack.docx,ODINI*.pdf,Reinforced Agent*.pdf,Signals*.pdf}`
- scripts: `scripts/skill_audit.py` v0.5 + `scripts/_llm_retry.py` + `scripts/wiki_lint.py` + `scripts/cross_wiki_route.py`

## Session-start ritual reminders

1. Read this file
2. Check `wiki/sweeps/*.md` mtime — sweep is **OVERDUE** (last 2026-05-01)
3. Check `research to be indexed/` for new sources (currently empty)
4. If prod desktop-app fails on first message after a Claude Code update: verify `ssh cemini-prod 'env | grep IS_SANDBOX'` returns `IS_SANDBOX=1`.
