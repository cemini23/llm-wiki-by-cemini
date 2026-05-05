# Roadmap

Companion to: `CLAUDE.md` (schema), `wiki/log.md` (backward-looking log), `LESSONS.md` (meta-lessons).

---

## Vision

CeminiSuite ships to an institutional buyer with a **verifiable execution-security architecture** (K19+K20+K22+K23), a **research-grounded market-making edge** (K24 ParlayMarket + Kalshi + K28 sports/healthcare prediction-market plumbing), and a **24/7 librarian MCP** serving the deployed brain. Each K-series deep-read adds one reusable architectural primitive. The wiki is the IP catalog.

## Active — this session (2026-05-05)

- **K30 Polymarket-readiness wave** — 4 Gemini DR docx batches (102 tools) + Deep GraphRAG arXiv 2601.11144 + Murphy RL Overview arXiv 2412.05265v5. 13 wiki pages (6 source + 7 entity stubs) + license-posture 8 → 9 patterns (added ELv2). 1 prod brief staged: `briefs/2026-05-05_polymarket-stack-adoption.md` (Polymarket Agents + python-order-utils + py-clob-client + polymarket-mcp-server unified adoption).
- **K29 XSKILL ingest (carryover)** — completed 2026-05-04. 1 prod brief at `briefs/2026-05-04_xskill-cross-rollout-critique-conductor.md`.
- **K28 5_4 sweep (carryover)** — 33-tool eval batch + Gemini Sci Research methodology paper. 4 prod briefs staged. Adoption work complete (SwarmVault NO-GO, codegraph + leaf installed, skill_audit.py shipped, MITRE ATLAS synthesized).
- **Post-ingest brief staging** — 6 prod briefs in `briefs/` total (5 K28+K29 + 1 K30). Per `post_ingest_workflow` memory rule.
- **Server-side error-code-1 triage** — DONE (IS_SANDBOX=1 wrapper at `/root/.claude/remote/ccd-cli/2.1.121` — verified working).

## Next — queued (K28-driven adoption work, in priority order)

| # | Item | Surface | Notes |
|---|------|---------|-------|
| ~~1~~ | ~~SwarmVault Phase 0 source audit~~ | ~~laptop~~ | **DONE 2026-05-04 — VERDICT: NO-GO.** Same architectural disease as llm-wiki-compiler (hardcoded flat layout in `vault.ts:2781-2787`); also uses `[[wikilink]]` syntax incompatible with our 3,249 `@path` cross-links. Adaptation cost (rename 99 nested entity files + rewrite 3k cross-links + lose category-as-directory) exceeds marginal benefit over kb-server. Stay on kb-server. See `wiki/entities/tools/swarmvault.md` for full audit. |
| 1 | **codegraph + leaf laptop install** | laptop | Both Adopt-tier MIT-licensed. `npm install -g codegraph`, `cargo install leaf` (or AUR/npm). `.gitignore` codegraph SQLite indices. (Promoted to #1 after SwarmVault NO-GO.) |
| 3 | **Klaassen-Magnus Elo math extraction** | prod (brief) | `briefs/2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md`. Math extraction + commercial-data sourcing decision. **Direct prediction-market application** (Kalshi/Polymarket tennis contracts). |
| 4 | **Riskfolio-Lib + FinanceToolkit FastMCP wiring** | prod (brief) | `briefs/2026-05-04_quant-libs-fastmcp-integration.md`. Position-sizing math (HRP, Kelly, Black-Litterman) + 150 financial metrics → `@mcp.tool` decorators in `services/llm_analyst/`. |
| 5 | **probablyprofit pattern extraction** | prod (brief) | `briefs/2026-05-04_probablyprofit-pattern-extraction.md`. Kelly + LLM ensemble consensus + multi-vector kill switch. Networking layer is Polymarket-specific (rewrite for Kalshi). |
| 6 | **atlas-gic autoresearch loop clean-room** | prod (brief) | `briefs/2026-05-04_autoresearch-conductor-evolution.md`. Conductor v0.1.1 evolution candidate. Shadow-mode-first rollout to bound token cost. |
| 6b | **XSKILL cross-rollout critique** (companion to #6) | prod (brief) | `briefs/2026-05-04_xskill-cross-rollout-critique-conductor.md`. Plugs MLLM-judged critique into atlas-gic's promote/revert pipeline as second proposal source. License-audit Phase 0 gates implementation. Ships together with #6. |
| 10 | **Polymarket Stack Adoption** | prod (brief) | `briefs/2026-05-05_polymarket-stack-adoption.md`. Coherent 4-component stack: Polymarket Agents + python-order-utils + py-clob-client + polymarket-mcp-server (all MIT). Adds Polymarket as Cemini's secondary prediction-market venue. |
| 11 | **PageIndex Phase 0 audit** | laptop | Vectorless reasoning-based RAG candidate (MIT). Phase-0 audit similar to K28 SwarmVault. Watch for flat-layout disease before getting excited. |
| 12 | **pykalshi adoption** | prod (brief candidate) | Replace bloated official Kalshi SDK with pykalshi (MIT, "completely replaces"). Could be folded into Polymarket Stack brief as a sister "Kalshi Stack Refresh", or staged separately. |
| 13 | **Kalshi llms.txt ingest** | librarian (cron) | Kalshi publishes llms.txt for LLM consumption. Cron-pull → `wiki/concepts/kalshi-api-reference.md` synthesis page → kb-server indexes. Refresh monthly. |
| 14 | **FinanceDatabase + FinanceToolkit FastMCP integration** | prod (brief) | Folds into existing K28 quant-libs brief OR stages separately. 300k symbol catalog + 150 metrics together = full ticker-research toolchain. |
| 15 | **Claude-OSINT skill merge** | laptop | Workspace-side: 5,500 lines of OSINT SKILL.md. Selectively port relevant skills into ~/.claude/skills/. Phase-0 inspection first. |
| 7 | **MedSkillAudit veto-gate port** | laptop | Refactor framework to `scripts/skill_audit.py` for financial-prompt validation (40% static / 60% dynamic / Veto Gates). |
| 8 | **MITRE ATLAS taxonomy ingestion** | wiki (separate workstream) | 16 tactics × 170 techniques × 35 mitigations × 57 case studies → wiki layer. Attribution requirement: verbatim MITRE copyright reproduction. |
| 9 | **License-pattern catalog (9 modes)** | next sweep | Apply explicit checklist to next Gemini DR eval ingest: NO-LICENSE, AGPL Docker-defeat, GPL derivative-work, CC-BY-NC training-data contamination, dual-license MIT-vs-GPL, namespace confusion, LGPL dynamic-linking, dual-licensing enterprise-tier gating, **+ ELv2 source-available with use-restrictions (added K30)**. |

### K30-derived wiki-side workstreams (synthesis pages + concept extensions)

| # | Item | Surface | Notes |
|---|------|---------|-------|
| 16 | **Polymarket market-making architecture synthesis** | wiki concept | New `concepts/polymarket-market-making-architectures.md` synthesizing the 5 Polymarket MM Steal-from impls (poly-market-maker, poly-maker, polymarket-market-maker, Polymarket Trading Bot v3.1, Polymarket-BTC-15-min). Comparable runtime patterns; pick reference architecture when Cemini begins MM work. Stage similar to K20's `openclaw-security-taxonomy.md`. |
| 17 | **Cross-venue arbitrage architecture pattern** | wiki concept | New `concepts/cross-venue-arbitrage-pattern.md`. Polymarket-Kalshi BTC arb is the K30 cross-doc duplicate (5_5-links-2 URL 8 + links-3-5_4 URL 17 — same pattern, two independent Steal-from verdicts). Document the architectural signal so future Cemini arb work has a baseline. |
| 18 | **DW-GRPO promotion to autoresearch concept** | wiki concept | Update `concepts/autoresearch-loop-pattern.md` to add **5th instantiation**: Deep GraphRAG's DW-GRPO (Dynamic Weighting Reward GRPO balancing relevance/faithfulness/conciseness). 4 instantiations after K29 (math, atlas-gic, claude-obsidian, XSKILL); DW-GRPO is the RL-trained variant. |
| 19 | **Conductor concept page extension** | wiki concept | Update `concepts/conductor-orchestrator.md` to record planned `prediction_market_polymarket` taxonomy class (per K30 brief). Add cross-link from Conductor → polymarket integration stack. |
| 20 | **Deep GraphRAG architectural eval as librarian alternative** | wiki concept | If PageIndex Phase 0 (#11) fails, Deep GraphRAG's hierarchical retrieval (inter-community → community-refine → entity-fine) is a 3rd librarian-tooling candidate beyond kb-server (current) and PageIndex. Update `concepts/wiki-tooling-evaluation.md` candidate list. Keep below-the-fold until PageIndex audit lands. |
| 21 | **prediction-market-analysis Steal-from synthesis** | wiki concept | New `concepts/prediction-market-historical-analysis.md` (or extend existing). Lift the indexing/aggregation patterns from `5_5-links-2` URL 6 Steal-from for Cemini's eventual prediction-market backtest pipeline. |
| 22 | **Polymarket Reference-only catalog** | wiki note | The 11 Reference-only items in `polymarket-5-5-tool-eval.md` (py-clob-client, polymarket-subgraph, clob-client, etc.) are Polymarket-internal libraries we'd hit transitively when building the integration. Brief inline note in `entities/platforms/polymarket.md` cross-linking them as "transitive dependencies, not direct adoption targets." |
| 23 | **RL Overview chapter promotion discipline** | wiki meta | When future ingest cites a Murphy chapter (e.g., §5 multi-agent RL when MAPPO becomes operationally relevant), promote that chapter to deep-read in `sources/rl-overview-murphy-2412-05265.md` and add a `## Snippets` block. Discipline note for future curator sessions. |
| 24 | **Curator-skills concept page** (companion to #15) | wiki concept | When Claude-OSINT skills are merged into `~/.claude/skills/`, document which ones got merged + why in a new `concepts/curator-skills.md`. Cross-link from `entities/tools/claude-osint.md`. Don't merge skills without this trail. |

## Decisions — open

### Which LLM brain?

DeepSeek hosted API is the operative path. Local options hardware-gated (7 GB RAM).

### Which conductor? (Fugu vs Trinity vs Conductor) ✅ DECIDED 2026-05-02

**In-house Conductor build.** GRPO maintains policy stability; Training-Free GRPO path enables API-only deployment (no weight access needed). 7 papers already ingested (K25). v0.1.1 deployed in shadow mode.

**K28 follow-on**: atlas-gic autoresearch loop is the Conductor-evolution candidate (clean-room implementation gated on user authorization). Brief #6 above.

### Wiki tooling

**Serving layer: kb-server** — deployed on librarian CPX21, active, 397 docs indexed. llm-wiki-compiler v0.4.0 retained on disk for potential future compile-mode use (nested-path bug blocks query/serve).

**K28 update**: SwarmVault is the first credible MIT-licensed Karpathy-pattern alternative. Phase 0 source audit is Next #1 — outcome will resolve this decision.

### Librarian server — remaining phases

| Phase | Item | Status |
|---|---|---|
| 0–3.5 | Provision, sync, kb-server, allowlist, cron | Done |
| 4 | Wire production brain → librarian MCP | Done 2026-05-01 (audit trail E2E verified) |
| 5 | Sync cron | Done (folded into 3.5) |
| 6 | Monitoring + tuning | Done (workspace-side); brief shipped to cemini-prod |
| 7 | Stash episodic memory | Done 2026-05-02 (alash3al/stash v0.2.9 deployed, MCP wired across all 3 contexts) |

## Eventually

- **Storage compaction** — disk 88% full. Market dataset → Parquet; research corpus → SQLite FTS index.
- **Bootstrap full PDF content index** — 230 stubs done. Full deep-read at K-series pace (~12 months).
- **Cited-unread backlog** — 99 stubs (was 133, K28 added a small increment). Organic reduction via K-series.
- **Periodic lint as session-start ritual** — low friction, high signal.
- **Workspace ↔ server reconciliation rhythm** — compare page counts / slug parity periodically.
- **Test suite for scripts** — `wiki_lint.py` / `bootstrap_inbox.py` have no coverage.
- **Tier 2.5 `/autoresearch` loop** — Steal-from from claude-obsidian. Port multi-round Exa loop into Path 2.
- **Cross-doc duplicate detection** — hash H2 titles across link-aggregate docs.
- **MCP-tool inventory consolidation** — 130 tools discovered (vs 22 documented). Single canonical inventory.
- **agentic-soc-platform pattern adoption** — Redis Stream + LangGraph state-management patterns for `agents/orchestrator.py` hardening (architectural reference, defer wholesale deployment).
- **Conductor `--build-priors` automation** — weekly cron already gated to 30+ new decisions; replace with autoresearch-driven mutation if Brief #6 (atlas-gic clean-room) ships and shadow-mode succeeds.
- **DeepSeek model IDs** — confirm `deepseek-chat` vs `deepseek-v4-flash` model IDs against current API docs.

## Gap detection (3-tier)

| Tier | Status |
|---|---|
| **0** — pre-ingest dup check (`preingest_check.py`) | Done; ran 2026-05-04 K28 (3 NEW, 0 duplicates) |
| **1** — gap-detection lint (`wiki_gap_detect.py`) | Last run 2026-05-02; due for fresh run |
| **2** — proactive Exa sweeps (user-gated) | Active (Path 1: session-driven). Last sweep 2026-05-01 — 3 days old, within 7-day cadence |
| **3** — fully autonomous outbound ingest | Rejected |

## Done — 2026-05-04 session

- **K28 5_4 sweep ingest** — 3 sources + 15 wiki pages + license-posture catalog 5→8 patterns. Pushed.
- **Memory updates** — `prediction_market_scope.md` + `post_ingest_workflow.md` saved.

## Done — 2026-05-02 session

- **K25 Conductor sweep** — 7 papers ingested. `concepts/conductor-orchestrator.md` synthesis page.
- **K26 ToolOrchestra deep-read** — 8B orchestrator beats GPT-5 on HLE at 2.5× efficiency.
- **K27 9-source batch** — ARA paper + 4 pattern adoptions + Conductor v0.1.1 committed (17 files, 2,011 lines) + Phase 4 brief staged.
- **Cross-doc dedup Pass 3** — H3-heading fuzzy matching. 0 new duplicates.
- **Stale NEEDS-VERIFICATION sweep** — 17 tags resolved across 4 pages.
- **Conductor in-house decision** — finalized.
- **Wiki-tooling smoke test re-run** — llmwiki v0.6.0, nested-path bug confirmed.
- **Stash episodic memory deployed** — alash3al/stash v0.2.9 on librarian. Two-layer memory architecture (kb-server + stash). Phase 7 complete.

## Done — 2026-05-01 session

- **Phase 4 — brain → librarian MCP** — Audit trail deployed on cemini-prod. E2E verified.
- **K24** — ParlayMarket deep-read + `concepts/parlay-market-making.md` + kalshi.md extension
- **K23** — Nomotic AI deep-read + nomotic-ai.md primary-source confirmation + six principles
- **K22** — Reasoning Safety Monitor deep-read + `concepts/reasoning-safety-monitor.md`
- **K21** — STOCKBENCH deep-read + stockbench.md correction
- **K20** — OpenClaw deep-read + `concepts/openclaw-security-taxonomy.md`
- **K19** — SAE deep-read + `concepts/sae-execution-contract.md`
- **Cross-cluster synthesis** — `concepts/agent-authorization-stack.md` + `briefs/2026-05-01_execution-security-architecture.md`
- **Infra** — gitignore Node.js, preingest_check.py arXiv scoping fix.

## Done — prior sessions (highlights)

- **Librarian server** — CPX21 provisioned, kb-server on :3838, 397 docs indexed, sync cron active. Phases 0–3.5 shipped.
- **Wiki tooling evaluation** — `concepts/wiki-tooling-evaluation.md`, 6 source pages, llm-wiki-compiler adoption recommendation.
- **Wave 5** — 4 Adopt (polymarket-mcp, claude-obsidian, alash3al/stash, Kronos tokenizer). 10 source pages. 2 Cemini-prod briefs.
- **K8–K18** — Cemini-internal queue exhausted. K8 strongest stale-snapshot find (128 GB → 7 GB). K13 ES-vs-GRPO evidence. Trinity + Fugu + Conductor lineage closed.
- **CI/CD** — `lint.yml` (push + weekly), `links.yml` (monthly), pre-commit hook (blocks secrets/IPs).
