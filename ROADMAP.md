# Roadmap

Companion to: `CLAUDE.md` (schema), `wiki/log.md` (backward-looking log), `LESSONS.md` (meta-lessons).

---

## Vision

CeminiSuite ships to an institutional buyer with a **verifiable execution-security architecture** (K19+K20+K22+K23), a **research-grounded market-making edge** (K24 ParlayMarket + Kalshi + K28 sports/healthcare prediction-market plumbing), and a **24/7 librarian MCP** serving the deployed brain. Each K-series deep-read adds one reusable architectural primitive. The wiki is the IP catalog.

## Current state (end of 2026-05-10)

- **Wiki**: 607 pages indexed (564 + 32 K35 4-source eval batch + 11 misc from prior ingest). K35 adds 25 tool entities + 2 concepts (tool-evaluation-framework, SPJ) + 4 sources. 55 tools evaluated across 3 deployment surfaces.
- **K-series**: K35 complete (4-source evaluation brief batch — 55 tools, 1 academic paper). Three-surface evaluation methodology codified. Verdict distribution: 10 Adopt, 9 Steal-from, 3 Defer, 5 Reference-only, 25 Reject, 4 Unavailable.
- **Inbox**: CLEAN (4 sources ingested + moved to librarian 2026-05-10)
- **Step 81 — SSHD on Prod**: ✅ COMPLETE (2026-05-09). `openssh-server` installed + hardened `sshd_config` on `cemini-prod`. Verified end-to-end connectively from workspace laptop. Prereq for Step 82. Brief: `briefs/2026-05-09_step81-sshd-prod.md`.
- **Step 82 — Prod Smoke Test**: PARTIAL PASS (2026-05-09). Conductor pipeline ✅, Stash ✅, Calibration ✅. Redis/EMS ❌ blockers. See `briefs/2026-05-09_step82-production-smoke-test.md`.
- **Next**: Resolving Redis + EMS blockers before Step 83 (live deployment). 3 K34 adoption briefs reviewed: 2 GO (polymarket-onchain-data-pipeline, mcp-context-optimization-stack) + 1 CONDITIONAL-GO (sabr-geometry-aware-calibration: audit SABR usage first).
- **Active prod briefs**: 9 at `cemini-prod:/opt/cemini/briefs/` awaiting prod-side execution (6 from K28-K30 + 3 K31). **No new K33 prod briefs** — K33's adoption is workspace-laptop-side (brief-audit `regime-disclosure` gate + downstream listwise-ranking instrumentation deferred)
- **Active workspace-laptop briefs**: 3 staged
  - `briefs/2026-05-06_obsidian-llm-wiki-local-steal-from.md` (port 4 wiki-maintenance patterns into `scripts/wiki_lint.py`; Phase 1 ✓ / Phase 2 deferred, bundles with brief-audit-upgrade sprint)
  - `briefs/2026-05-07_regime-disclosure-brief-audit-gate.md` — **SHIPPED 2026-05-08** — `scripts/skill_audit.py` v0.2: regime-disclosure veto gate implemented, all 4 test briefs PASS, no false positives on K28-K30 adoption briefs.
  - `briefs/2026-05-09_mcp-context-optimization-stack.md` — **NEW K34** — 4-layer MCP context optimization stack (lazy-tool + claude-code-router + client optimizations + OpenRouter caching). skill_audit PASS 90/100. **GO** (2026-05-09). Solves #1 architectural blocker; 80-95% cost reduction. Awaiting scp to prod.
  - `briefs/2026-05-09_polymarket-onchain-data-pipeline.md` — **NEW K34** — Polymarket on-chain data pipeline (Dubach polydata.onchain integration as Layer 1 harvester). skill_audit PASS 90/100. **GO** (2026-05-09). Single most important data-infrastructure gap. Awaiting scp to prod.
  - `briefs/2026-05-09_sabr-geometry-aware-calibration.md` — **NEW K34** — SABR GeoResNN calibration (hybrid ML-analytical vol surface). skill_audit PASS 90/100. **CONDITIONAL-GO** (2026-05-09). Discovery brief: audit Cemini SABR usage first; implement only if in use. Awaiting scp to prod.
- **Deferred prod briefs (with activation triggers)**: 2 (autoresearch + XSKILL Conductor evolution)
- **Laptop-side K31 adoptions**: ttok 0.3 + git-rewind 1.1.4 INSTALLED 2026-05-06; 2 upstream issues filed against Chronos778/git-rewind ([#1](https://github.com/Chronos778/git-rewind/issues/1) install.sh checksum bug, [#2](https://github.com/Chronos778/git-rewind/issues/2) missing LICENSE file). User adopting **Groq** for rewind LLM backend (free tier).
- **Monetization-priority stance** (2026-05-06): revenue first, IP-sale exit later-stage. License auto-rejects soften for non-prod-codebase use; Phase-0 audit rigor unchanged. See `~/.claude/projects/.../memory/monetization_priority_2026.md`.
- **Prod ccd-cli auto-update protection**: `IS_SANDBOX=1` in `/etc/environment` (Option A permanent fix). Applied + verified end-to-end 2026-05-06.
- **Inbox**: CLEAN (4 sources ingested + moved to librarian 2026-05-10)

## Next — actually pending action

K35 ingest complete 2026-05-10. **All 10 Adopt-tier briefs now staged** (4 prod-target + 6 workspace-laptop-target). Next priorities: (1) Phase-0 audits + license verifications for the CONDITIONAL-GO items (claude-mem injection limits, codeboarding license, github-spec-kit license); (2) K35 Steal-from extractions (SPJ algorithm port, TPE sampling, Bradley-Terry); (3) Bundled brief-audit upgrade sprint decision (3 K32 STEAL-FROMs + `_llm_retry.py`).

### 0 — Workspace-laptop actionable (K32 + K33 + K35)

| Brief | What it ships | Status |
|-------|---------------|--------|
| `briefs/2026-05-06_obsidian-llm-wiki-local-steal-from.md` | Phase 1 ✓ / Phase 2 deferred | Phase 1 ✓ / Phase 2 deferred |
| `briefs/2026-05-07_regime-disclosure-brief-audit-gate.md` | **SHIPPED 2026-05-08** — `scripts/skill_audit.py` v0.2 with regime-disclosure veto gate | SHIPPED |
| `briefs/2026-05-08_rl-80k-btc-training-results.md` | RL 80K-frame BTC-USD training results, checkpoint for future 500K retrain | NEW |
| `briefs/2026-05-10_aris-adoption.md` (K35) | ARIS Markdown skill files for structured research workflow | NEW — GO |
| `briefs/2026-05-10_github-spec-kit-adoption.md` (K35) | Spec-Driven Development CLI for wiki → production-code transitions | NEW — GO (license verify pending) |
| `briefs/2026-05-10_tech-debt-skill-adoption.md` (K35) | Quarterly Cemini codebase technical-debt audits | NEW — GO |
| `briefs/2026-05-10_claude-mem-adoption.md` (K35) | Cross-session persistent observation memory | NEW — CONDITIONAL-GO (injection limits) |
| `briefs/2026-05-10_revpdf-adoption.md` (K35) | 15MB offline PDF editor for research extraction | NEW — GO |
| `briefs/2026-05-10_codeboarding-adoption.md` (K35) | Auto-generated Cemini architecture diagrams | NEW — CONDITIONAL-GO (license + Node.js compat) |

### 1 — Awaiting prod-side execution (no workspace action)

9 briefs at `cemini-prod:/opt/cemini/briefs/`:

| Brief | What it ships |
|-------|---------------|
| `2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md` | Tennis Elo math extraction + commercial-data sourcing |
| `2026-05-04_quant-libs-fastmcp-integration.md` | Riskfolio-Lib + FinanceToolkit + FinanceDatabase wrappers (K30-updated) |
| `2026-05-04_probablyprofit-pattern-extraction.md` | Kelly + LLM ensemble + multi-vector kill switch |
| `2026-05-05_polymarket-stack-adoption.md` | Polymarket Agents + python-order-utils + py-clob-client + polymarket-mcp-server |
| `2026-05-05_pykalshi-adoption.md` | pykalshi replaces bloated official Kalshi SDK |
| `2026-05-05_conductor-audit-trail-phase1.md` | Conductor fitness function + audit JSONL + git-tracked config commits (no LLM mutation engine) |
| `2026-05-06_hftbacktest-adoption.md` (NEW K31) | Microsecond-tick HFT backtester for Polymarket/Kalshi MM + cross-venue arb threshold tuning. Sister to quant-libs (daily-bar) — fills the execution-resolution gap. |
| `2026-05-06_guidance-ai-adoption.md` (NEW K31) | Microsoft structured-generation library wrapping DeepSeek calls; eliminates parsing-error tail in LangGraph + FastMCP `@mcp.tool` pipeline. |
| `2026-05-06_ttok-prod-install.md` (NEW K31) | Single Pipfile addition (`ttok==0.3`); pre-call audit hook in DeepSeek wrapper. Apache-2.0. Tiny standalone brief. |

Plus prod-originated: `2026-05-04_step124-phase1-verification.md`.

### 2 — Deferred-with-triggers (do not delete)

Both briefs retained intact at `cemini-prod:/opt/cemini/briefs/` with DEFERRED top-of-file headers; reactivate when **both** triggers fire:

| Brief | Activation triggers |
|-------|---------------------|
| `2026-05-04_autoresearch-conductor-evolution.md` (Phases 2-6) | Traffic ≥ 3,500 Conductor decisions/week sustained ≥ 2 weeks **AND** explicit buyer/research signal pulls for the "automated self-proposing" capability |
| `2026-05-04_xskill-cross-rollout-critique-conductor.md` (entirely) | Same triggers as above; ships together with autoresearch |

The audit-trail subset (`2026-05-05_conductor-audit-trail-phase1.md` above) supersedes Phases 1+5 of the autoresearch brief and ships now.

### 3 — Recurring discipline

| Item | When |
|------|------|
| **License-pattern catalog (10 modes — K32 added License Drift)** apply on each new Gemini DR ingest | Every ingest |
| **post_ingest_workflow** memory rule: ROADMAP + briefs after every ingest commit-and-push | Every ingest |
| **Tier 2 arXiv sweep** — last 2026-05-01 (5 days fresh, within 7-day cadence) | When ≥7 days old |
| **wiki_gap_detect.py rerun** — last 2026-05-04 (clean baseline) | After next ingest or weekly |

## Decisions — open

### Which LLM brain? ✅ DECIDED

DeepSeek hosted API is the operative path (`deepseek-v4-flash` for analyst nodes, `deepseek-v4-pro` for final-decision synthesizer). Local options hardware-gated (7 GB RAM). Per `wiki/entities/infrastructure/deepseek-api.md` (refreshed 2026-05-04 with verified model IDs).

### Which conductor? ✅ DECIDED 2026-05-02 + REFINED 2026-05-05

In-house Conductor build (v0.1.1 in shadow mode). 48.2% cost savings vs always-reasoner baseline.

**Evolution path (refined 2026-05-05 after codex independent review):**

- **Audit-trail subset (Phases 1+5)** ships now via `2026-05-05_conductor-audit-trail-phase1.md` — fitness function + audit JSONL + git-tracked config commits. ~2-4 days prod-side, ~$0/week ongoing. Captures ~85% of IP-sale "self-improvement-capability" narrative.
- **Full autoresearch loop (Phases 2-6 + XSKILL companion)** deferred until both activation triggers fire (see "Deferred-with-triggers" above).

### Wiki tooling ✅ DECIDED 2026-05-05

**Default: kb-server stays as serving layer.** After three Phase-0 audits (K28 SwarmVault, K30 PageIndex, K30 Claude-OSINT), the Karpathy-pattern alternative search has eliminated all credible-looking candidates for Cemini's nested-wiki use case.

| Candidate | 2026-05-05 status |
|-----------|-------------------|
| **kb-server** | DEPLOYED on librarian |
| llm-wiki-compiler v0.4.0 | DEPLOYMENT-BLOCKED (hardcoded flat-layout) |
| SwarmVault | NO-GO 2026-05-04 (same flat-layout disease) |
| PageIndex | NO-GO 2026-05-05 (single-file API + agentic cost + lost graph/metadata) |
| Claude-OSINT skills | NO-PORT 2026-05-05 (wrong domain — red-team OSINT, not curator workflow) |
| **Deep GraphRAG** | Deferred — only remaining alternative on file. Re-evaluate IF wiki develops cross-link graph density flat retrieval can't handle, OR user decides graph-aware retrieval is worth the operational complexity. |

### Librarian server — phases ✅ COMPLETE

| Phase | Status |
|-------|--------|
| 0–3.5 Provision, sync, kb-server, allowlist, cron | Done |
| 4 Brain → librarian MCP | Done 2026-05-01 (E2E verified) |
| 5 Sync cron | Done (folded into 3.5) |
| 6 Monitoring + tuning | Done |
| 7 Stash episodic memory | Done 2026-05-02 (alash3al/stash v0.2.9) |

## Eventually (no urgency, no specific trigger)

- **Storage compaction** — disk 88% full. Market dataset → Parquet; research corpus → SQLite FTS index.
- **Bootstrap full PDF content index** — 230 stubs done. Full deep-read at K-series pace (~12 months).
- **Cited-unread backlog** — 99 stubs. Organic reduction via K-series ingests.
- **Workspace ↔ server reconciliation rhythm** — periodic page-count / slug-parity checks.
- **Test suite for scripts** — `wiki_lint.py` / `skill_audit.py` / `preingest_check.py` / `wiki_gap_detect.py` / `bootstrap_inbox.py` have no test coverage.
- **Tier 2.5 `/autoresearch` loop** — Steal-from from claude-obsidian. Port multi-round Exa loop into Path 2.
- **Cross-doc duplicate detection** — hash H2 titles across link-aggregate docs.
- **MCP-tool inventory consolidation** — 130 tools discovered (vs 22 documented). Single canonical inventory.
- **agentic-soc-platform pattern adoption** — Redis Stream + LangGraph state-management patterns for `agents/orchestrator.py` hardening (architectural reference, defer wholesale deployment).
- **Periodic lint as session-start ritual** — already documented in CLAUDE.md session-start ritual; mostly automatic.
- **Sakana 2026-04-27 NV tags Exa-resolution** — 12 stale `[NEEDS VERIFICATION 2026-04-27]` tags pending focused Exa-cross-check pass.

## Gap detection (3-tier)

| Tier | Status |
|------|--------|
| **0** — pre-ingest dup check (`preingest_check.py`) | Active; runs on every ingest |
| **1** — gap-detection lint (`wiki_gap_detect.py`) | Last run 2026-05-04 (clean baseline) |
| **2** — proactive Exa sweeps (user-gated) | Active; last sweep 2026-05-01 (within 7-day cadence) |
| **3** — fully autonomous outbound ingest | Rejected (drift / cost / trust grounds) |

---

## Done — 2026-05-09 Donny ingest + K34 brief GO/NO-GO review

### Donny Market Thoughts ingest
- **Source**: Donny.PDF (5 pages, multi-topic market research note), ingested 2026-05-09. 7 wiki pages: 1 source (`donny-market-thoughts-2026-05-09.md`), 1 concept (`rare-earth-supply-deficit-thesis.md`), 5 ticker stubs (TEAM, FANG, NET, TOST, REA).
- **Key thesis**: Heavy rare earth (DyTb) structural supply deficit — China+Myanmar >90% supply, April 2025 export restrictions, humanoid robotics demand driver (~70K tpa REO by 2040). Adamas Intelligence forecasts 100%+ price increases by 2040.
- PDF moved to `cemini-librarian:/opt/cemini-bulk/research/Donny.PDF`.

### K34 brief adoption verdicts (3 briefs reviewed)
- `polymarket-onchain-data-pipeline.md` → **GO**. #1 data-infrastructure gap; every downstream workstream blocked on it. Integrates Dubach's polydata.onchain as Layer 1 harvester.
- `mcp-context-optimization-stack.md` → **GO**. #1 architectural blocker (MCP eager-loading → 30K-75K tokens). 80-95% cost reduction; all MIT/Apache-2.0.
- `sabr-geometry-aware-calibration.md` → **CONDITIONAL-GO**. Discovery brief: audit Cemini SABR usage first; implement GeoResNN only if SABR is in use.

## Done — 2026-05-06 session

### K31 wrap-up (continued from 2026-05-05)
- **K31 ttok prod brief shipped** — `2026-05-06_ttok-prod-install.md` (commit `f414000`). Tiny standalone: single Pipfile addition + optional pre-call audit hook in DeepSeek wrapper. skill_audit PASS 100/100.
- **K31 laptop-side adoptions** (commit `7635a67`) — ttok 0.3 (Apache-2.0) and git-rewind 1.1.4 (MIT per Cargo.toml; CONDITIONAL — no LICENSE artifact) installed under `~/.local/bin/`. rewind configured with Groq + Gemini API keys via `rewind config set`. End-to-end smoke test PASS.
- **First-ever upstream issues filed** — [Chronos778/git-rewind#1](https://github.com/Chronos778/git-rewind/issues/1) (install.sh checksum-handling bug: 404 .sha256 → "Not Found" parsed as expected hash) + [#2](https://github.com/Chronos778/git-rewind/issues/2) (missing LICENSE file).
- **K31-eval correction recorded** — rewind isn't Ollama-only; `OPENAI_API_BASE` override supports any OpenAI-compatible endpoint (DeepSeek, Groq, Gemini, OpenAI, Ollama).

### Prod ccd-cli auto-update fix → permanent
- **Recurrence event** — Desktop-app auto-updated ccd-cli to 2.1.128 at 13:18 UTC, deploying raw 248MB ELF binary at `/root/.claude/remote/ccd-cli/2.1.128` (no wrapper). Crashed every desktop-app session attempt (process.spawn → drainStdin → exit 1).
- **Wrapper pattern re-applied 13:36 UTC** — same recipe as 2026-05-04 (move binary to `2.1.128.real`, create wrapper exec'ing with `IS_SANDBOX=1`). Restored desktop-app connectivity.
- **Permanent fix Option A applied** — added `IS_SANDBOX=1` to `/etc/environment`. Verified PAM `pam_env.so` propagates env through fresh SSH login → ccd-cli (raw or wrapped) inherits the var → safety check skips root refusal. Reverted 2.1.128 wrapper to test cleanly; user confirmed via desktop-app session: "i messaged in desktop app to server and it worked." Eliminates per-auto-update wrapper-reapply cycle.
- **Cleanup** — wrapper artifact `2.1.128.wrapper-saved` removed. ccd-cli dir contains only raw binaries (2.1.111 + 2.1.128). Memory file `prod_ccd_cli_root_fix.md` rewritten to document Option A as the live mechanism.

---

## Done — 2026-05-05 session (the big one)

### Ingests
- **K30 Polymarket-readiness wave** — 4 Gemini DR docx batches (102 tools) + Deep GraphRAG arXiv 2601.11144 + Murphy RL Overview arXiv 2412.05265v5. 13 wiki pages (6 source + 7 entity stubs) + license-posture 8 → 9 patterns (added ELv2 source-available). 1 prod brief staged: `2026-05-05_polymarket-stack-adoption.md`.
- **K31 JPM portfolio paper + 5_5 moarrr Gemini DR batch (19 tools)** — 7 wiki pages (2 source + 5 entity stubs: hftbacktest, guidance-ai, letta-memgpt, ttok, git-rewind). License-posture catalog unchanged (9 modes stable). 2 standalone briefs shipped to prod 2026-05-06: `2026-05-06_hftbacktest-adoption.md` + `2026-05-06_guidance-ai-adoption.md` (both PASS skill_audit at 100/100). ttok = no-brief universal install (pending laptop + Cemini-prod Pipfile addition). JPM paper indexed reference-only (off-domain methodology with transfer value).
- **K33 Polymarket NBA arb paper 2605.00864** — 1 source page: `wiki/sources/polymarket-nba-arbitrage-2605.00864.md` (deep-read, validated). Updated `market-microstructure.md` concept hub + `index.md`. PDF scp'd to librarian. Key finding: combinatorial arb feasible but depth-capped at ~14.8 shares; Middle jackpot never realized.

### Adoption verdicts (3 audits + multiple briefs shipped)
- **#11 PageIndex Phase 0** → NO-GO. Single-file API + agentic cost + lost graph/metadata. Wrong tool for flat wiki.
- **#12 pykalshi** → brief shipped. Verified `github.com/ArshKA/pykalshi` MIT, 85★, 30 commits, v1.0.6.
- **#13 Kalshi llms.txt** → ingested as `wiki/concepts/kalshi-api-reference.md` (33 KB, ~150 endpoints).
- **#14 FinanceDatabase** → folded into K28 quant-libs brief; new `ticker_universe.py` wrapper section.
- **#15 Claude-OSINT skill merge** → NO-PORT. Wrong domain (red-team OSINT, not curator workflow). `curator-skills.md` stays empty by design.
- **#6/#6b autoresearch + XSKILL** → codex-reviewed scope reduction. Phases 1+5 ship as new brief #6c (`2026-05-05_conductor-audit-trail-phase1.md`); Phases 2-6 + XSKILL deferred-with-triggers.

### K30-derived wiki-side workstreams (all 9 closed: #16-#24)
- `concepts/polymarket-market-making-architectures.md` — 5-posture comparison + 5-layer Cemini reference
- `concepts/cross-venue-arbitrage-pattern.md` — 6-step arb loop + 6 risk caveats
- `concepts/prediction-market-historical-analysis.md` — 5-layer historical-data stack
- `concepts/autoresearch-loop-pattern.md` — extended 4 → 5 instantiations (DW-GRPO added)
- `concepts/conductor-orchestrator.md` — extended with planned `prediction_market_polymarket` taxonomy class + Conductor-evolution candidates section
- `concepts/wiki-tooling-evaluation.md` — extended with K28+K30 candidate landscape table
- `entities/platforms/polymarket.md` — K30 transitive-dependencies table
- `sources/rl-overview-murphy-2412-05265.md` — chapter-promotion discipline section
- `concepts/curator-skills.md` — NEW stub accumulator (populates with #15 if/when it activates; currently empty by design)

### Prod briefs scp'd (4 active + 2 deferred-with-triggers re-scp'd with DEFERRED headers)
- `2026-05-05_polymarket-stack-adoption.md` (NEW K30, 11.2 KB)
- `2026-05-05_pykalshi-adoption.md` (NEW K30, 10.4 KB)
- `2026-05-05_conductor-audit-trail-phase1.md` (NEW codex-reviewed subset, 14.4 KB)
- `2026-05-04_quant-libs-fastmcp-integration.md` (UPDATED with FinanceDatabase, 14.7 KB; was 10.2 KB)
- `2026-05-04_autoresearch-conductor-evolution.md` (DEFERRED header added; re-scp'd)
- `2026-05-04_xskill-cross-rollout-critique-conductor.md` (DEFERRED header added; re-scp'd)

### Methodology lessons logged
- Codex independent review pattern works: dispatch codex/Plan/code-reviewer for any brief with substantial engineering + operational commitments before user GO/NO-GO sign-off.
- Phase 0 audit pattern shipped 3 clean rejections of credible-looking but wrong-fit tools across K28+K30. Discipline saves estimated 2-4 hours of misaligned implementation per audit.
- Future Gemini DR sweeps should ask "how many distinct skills" alongside "how many lines" when evaluating skill libraries (eval-quality lesson from Claude-OSINT misframing).

### Total: 21+ commits this session arc (`d74d061..42053ad`)

## Done — 2026-05-04 session

- **K28 5_4 sweep ingest** — 3 sources (4 docx-batches + Gemini Sci Research methodology) + 15 wiki pages + license-posture catalog 5 → 8 patterns
- **K29 XSKILL ingest** — XSKILL paper (arXiv 2603.12056) + LeetCode off-domain stub. 1 prod brief staged.
- **codegraph + leaf laptop install** — npm prefix=~/.local; .gitignore patterns added; entity pages validated.
- **MedSkillAudit veto-gate port** — `scripts/skill_audit.py` v0.1 shipped with 6 static checks + 2 veto gates.
- **MITRE ATLAS taxonomy synthesis** — `concepts/mitre-atlas-taxonomy.md` covering ATLAS v5.6.0 (16 tactics × 170 techniques × 35 mitigations × 57 case studies). License correction: Apache-2.0 not CC BY 4.0.
- **SwarmVault Phase 0 NO-GO** — same flat-layout disease as llm-wiki-compiler.
- **DeepSeek model-IDs refresh** — 5 edits across 3 files; `[NEEDS VERIFICATION 2026-04-28]` → `[VERIFIED 2026-05-04]`.
- **Prod ccd-cli error-code-1 fix** — IS_SANDBOX=1 wrapper at `/root/.claude/remote/ccd-cli/2.1.121`.
- **wiki-share zip refresh** — `wiki-share-2026-05-04.zip` (3.2 MB, 591 files, sanitized).
- **Memory updates** — `prediction_market_scope`, `post_ingest_workflow`, `prod_ccd_cli_root_fix`, `npm_global_prefix`.

## Done — 2026-05-02 session

- **K25 Conductor sweep** — 7 papers ingested. `concepts/conductor-orchestrator.md` synthesis page.
- **K26 ToolOrchestra deep-read** — 8B orchestrator beats GPT-5 on HLE at 2.5× efficiency.
- **K27 9-source batch** — ARA paper + 4 pattern adoptions + Conductor v0.1.1 committed (17 files, 2,011 lines) + Phase 4 brief staged.
- **Cross-doc dedup Pass 3** — 0 new duplicates.
- **Stale NEEDS-VERIFICATION sweep** — 17 tags resolved across 4 pages.
- **Conductor in-house decision finalized.**
- **Stash episodic memory deployed** — alash3al/stash v0.2.9 on librarian.

## Done — 2026-05-01 session

- **Phase 4 — brain → librarian MCP** — Audit trail deployed on cemini-prod. E2E verified.
- **K19-K24** — SAE / OpenClaw / STOCKBENCH / RSM / Nomotic AI / ParlayMarket deep-reads + concept pages.
- **Cross-cluster synthesis** — `concepts/agent-authorization-stack.md` + execution-security-architecture brief.

## Done — prior sessions (highlights)

- **Librarian server** — CPX21 provisioned, kb-server on :3838, 397 docs indexed, sync cron active.
- **Wiki tooling evaluation** — `concepts/wiki-tooling-evaluation.md` + 6 source pages.
- **Wave 5** — 4 Adopt (polymarket-mcp, claude-obsidian, alash3al/stash, Kronos tokenizer).
- **K8–K18** — Cemini-internal queue exhausted.
- **CI/CD** — `lint.yml` + `links.yml` + pre-commit hook.
