# Roadmap

Companion to: `CLAUDE.md` (schema), `wiki/log.md` (backward-looking log), `LESSONS.md` (meta-lessons).

---

## Vision

CeminiSuite ships to an institutional buyer with a **verifiable execution-security architecture** (K19+K20+K22+K23), a **research-grounded market-making edge** (K24 ParlayMarket + Kalshi + K28 sports/healthcare prediction-market plumbing), and a **24/7 librarian MCP** serving the deployed brain. Each K-series deep-read adds one reusable architectural primitive. The wiki is the IP catalog.

## Current state (end of 2026-05-13)

- **K41 ingest COMPLETE 2026-05-13**: 11 sources / 5 concepts / 13 entity stubs ingested + cross-wiki routing checked (image-gen / seo / 3d-printing / cybersecurity all clear — sources OSINT-domain only). **Foundational agent papers landed**: Toolformer (2302.04761 Meta) + ReAct (2210.03629 Princeton+Google ICLR 2023) + Generative Agents (2304.03442 Stanford UIST 2023) + LLMs-Get-Lost (2505.06120 MS+Salesforce). LLMs-Get-Lost is the **third orthogonal data-level failure mode** completing the preference-data taxonomy (typicality K39 + asymmetric-penalty K40 + premature-commitment K41 — all training-free mitigations exist). **Massif Capital corpus introduction**: 4Q2025 Letter to Investors (15.6% net annualized since inception, 28 quarters) + 5 new concept pages (wicked-problems-capital-allocation, capital-cycle-theory, real-assets-investing-framework, critical-minerals-thesis, plus claude-md-12-rule-template). **Weekly Wizdom newsletter ingested** (Issues #173 Apr 7 / #175 Apr 22 / #176 Apr 29 FOMC) + Donny watchlist Apr 23 — **5+ exact ticker matches Apr 22-23 confirm Donny watchlist derives from WW recommendations** (treat as same-source for confirmation purposes). **Polymarket weather-trading strategy synthesized** from @AlterEgo_eth + @theparuchh sources: Gamma API two-endpoint pattern + 5 compounding edges (station-coordinate fix + Open-Meteo `bias_correction=true` + 3-model ICON+GFS+ECMWF ensemble + 3-bin coverage + 18-30hr entry window); reviewer-agent validation use case identified. **CLAUDE.md 12-rule template lineage** (Karpathy → Forrest Chang → Mnilax) documented with 41% → 3% claim flagged NEEDS VERIFICATION 2026-05-13. wiki_lint: **0 bidirectional gaps / 0 dangling related / 0 missing body mentions**. 11 raw sources SCPed to librarian with canonical filenames. Pre-K41 wiki structural cleanup (376 bidirectional gaps + 20 pre-K40 issues → 0) closed 2026-05-13 morning.

### K41 follow-ups (queue)

| Item | Action | Status |
|------|--------|--------|
| **Polymarket weather-trading Phase-0 audit** | Verify Open-Meteo `bias_correction=true` claim (NEEDS VERIFICATION); validate station coordinates for any deployed city; treat @theparuchh's V3 +45.9% ROI on $130 bankroll as anecdotal (3-day window). Strategy is portable to Cemini's prediction-market stack — adjacency to existing macro/sports market exposure | **PENDING** |
| **`real-assets supply-deficit consensus` brief candidate** | Cross-reference Massif's real-asset positions against WW newsletter calls (USAR Apr 22 + FSLR/ARRY/SHLS Apr 29) — multi-source supply-deficit thesis would be strong CONFIRMED signal. Donny watchlist filtered out (derives from WW). | **PENDING** — concept pages ready; brief candidate |
| **`capex tracker` brief candidate** | Pull public capex data for 5-7 sectors Massif covers (Wood Mackenzie / S&P Global / company disclosures) to independently audit capital-cycle thesis against underlying data. | **PENDING** — concept page ready; brief candidate |
| **CLAUDE.md audit pass** | Current CLAUDE.md is 322 lines, exceeds Mnilax 200-line ceiling. Candidate tech-debt task. | **PENDING** |
| **Forrest Chang repo stats verification** | 41% → 3% mistake-rate claim flagged NEEDS VERIFICATION 2026-05-13 in `wiki/concepts/claude-md-12-rule-template.md`. | **PENDING** Exa-resolution candidate |
| **Future Massif letters** | 28-quarter track record implies ~7-year letter series. Tracking-source candidate; ingest as future letters appear. | **TRACKING** |

## Current state (end of 2026-05-12)

- **K40 cross-wiki ingest COMPLETE 2026-05-12**: 6 new sources + multi-wiki Gemini eval prompt v2 deliverable. Cross-wiki batches shipped to cybersec (17 tools + 1 concept), image-gen (4), SEO (5). 37 new OSINT entity stubs + 4 new OSINT concepts. **User-flagged v1 prompt limitation corrected**: v2 prompt routes URLs through 7-surface fit grid (Cemini financial / OSINT / Cybersec / Image-gen / SEO / 3D-printing / Workflow); ready for next eval batch. **NPM supply-chain defense brief staged to `cemini-prod:/opt/cemini/briefs/2026-05-12_npm-supply-chain-defense.md`** per user request; workspace `package.json` confirmed pinned to exact versions. Tier headlines from K40: **AutoTS** + **voicemode** + **hunk** + **veloxdb** + **anthropic-harness-design** Adopt (Phase-0 pending). **Anthropic Planner/Generator/Evaluator trinity adopted as CEMINI orchestrator architecture** (replaces ad-hoc LangGraph routing). New license-pattern catches: 3× no-LICENSE (Karma + multi-model-redteam + Claude-Code-Projects-Index) → mode #1 count climbing; CC-BY-NC-4.0 IP-sale poison pill (pastebar-app rejected); CC-BY-SA-4.0 added to catalog (claude-code-ultimate-guide acceptable for study-only). **New concept pages**: `ralph-autonomous-agent-pattern.md`, `polymarket-bot-architecture.md`, `agent-cost-routing-orchestra.md`, `npm-supply-chain-defense.md`, plus cybersec wiki `llm-vulnerability-discovery.md`.

### K40 follow-ups (HIGH PRIORITY queue)

| Item | Action | Status |
|------|--------|--------|
| **AutoTS Phase-0 audit** | Phase-0 source audit before FastMCP integration: license (MIT confirmed), GPU MAPPO compat, dependency footprint vs Cemini 7GB Hetzner | **PENDING** — top-priority Adopt verdict |
| **voicemode laptop install** | Local Whisper.cpp + Kokoro voice I/O for Claude Code workflow | **PENDING** Phase-0 (single-dev bus-factor check) |
| **hunk laptop install** | Offline diff/patch UI; reduces LLM context bloat | **PENDING** Phase-0 (license + maturity) |
| **veloxdb laptop install** | Rust embedded KV for ingest pipeline caches | **PENDING** Phase-0 (Rust SBOM + license verification) |
| **anthropic-harness-design adoption** | Planner/Generator/Evaluator trinity → CEMINI orchestrator architecture (replaces ad-hoc LangGraph routing) | **PENDING** — sprint contract + Phase-0 audit + brief |
| **NPM supply-chain defense prod brief** | Brief at `cemini-prod:/opt/cemini/briefs/2026-05-12_npm-supply-chain-defense.md` | **SHIPPED 2026-05-12** — awaits server-Claude execution |
| **Multi-wiki Gemini eval prompt v2** | Available at `wiki/sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` Snippets section — copy-paste-ready | **READY for next eval batch** |
| **Cybersec wiki Phase-0 backlog** | 12+ cross-routed tools awaiting Phase-0 audits in cybersec wiki (openant, aisoc, bug-bounty-agents, idassist, airecon, etc.) | **DEFERRED to cybersec-wiki triage** |
| **Polymarket bot architecture brief** | 6-layer websocket bot architecture from @0x_Punisher → CEMINI deployment gap analysis brief | **PENDING** — concept page ready; brief candidate next sprint |
| **Cost-routing orchestra brief** | Kimi K2.6 + Hermes-4 + Opus 4.7 orchestra → Cemini cost-model brief; integrates with reviewer-agent + signals layers | **PENDING** — concept page ready; brief candidate |

## Current state (end of 2026-05-11)

- **Wiki**: 690 pages indexed (+2 K40 = 1 source + 1 concept; on top of +19 K39 and +45 K37/K38). K40 source `rlhf-critic-bias-al-zawahreh-2026.md` (Al-Zawahreh self-published April 2026 pre-print, **Reference/Steal-from tier, draft maturity**) + new concept `rlhf-critic-bias.md` housing the operational framework (5 patterns + 6-cat Rhetorical Catalog + 5-tell Forensic Scorecard + 4 mitigations). 5 backlinks added (reviewer-agent / VS / signals / tool-eval-framework / license-posture). K39 source `evaluating-project-links-stacks.md` (17-URL eval brief) plus paper-form `verbalized-sampling-mode-collapse.md` (training-free distribution-prompting paper). 1 new concept page captures the Verbalized Sampling pattern as third orthogonal training-free Conductor layer (alongside reviewer-agent + signals).
- **K-series**: **K40 (RLHF Critic Bias paper) complete 2026-05-11**. Single-source ingest, Reference/Steal-from tier, draft maturity. 1 new source + 1 new concept + 5 backlinks. Operational extraction: 5 patterns + 6-cat Rhetorical Catalog + 5-tell Forensic Scorecard + 4 mitigations. Phase-0 audit caught 4 structural signals (self-published / polemical / no-empirical / author-confirmation-bias-acknowledged) → posture is operational-primitives-only, not narrative-adoption. Follow-up brief candidate for `scripts/skill_audit.py --rlhf-tell-mode` flag DEFERRED (user-gated). K39 (17-URL link-eval brief + VS paper) complete 2026-05-11. K39 tier rollup: 6 Adopt + 2 Steal-from + 2 Reference-only + 3 Reject + 3 UNAVAILABLE + 1 duplicate. **5 Phase-0 RED FLAGS** carried forward (mischaracterization pattern continues — 6th aggregate catch across K28+K30+K36+K38). K37 (21-URL system-integration eval) + K38 (29-URL trading-stack eval) complete prior. K37 tier rollup: 3 Adopt + 6 Steal-from + 3 Reference + 1 Defer + 8 UNAVAILABLE. K38 tier rollup: 6 Adopt + 6 Steal-from + 5 Reference + 3 Defer + 5 Reject (Medusa AGPL + TokenSpeed + tropicaltidbits + D3Ext/WEF + ssh-keys-manager-stmol) + 4 UNAVAILABLE.
- **K-series prior**: K36 complete (17-URL trading-stack evaluation brief). Tier rollup: 4 Adopt (picobot, ctop, QuantMuse→NO-GO, Adala) + 4 Steal-from + 1 split (finance-skills) + 2 Reference/Defer + 3 Reject + 3 UNAVAILABLE.
- **K35 status**: complete (4-source eval batch, 55 tools across 3 surfaces). Three-surface evaluation methodology codified.
- **Inbox**: CLEAN (RLHF Critic Bias K40 paper moved to librarian 2026-05-11; K37/K38 sources + 3 papers moved to librarian 2026-05-11)
- **Step 81 — SSHD on Prod**: ✅ COMPLETE (2026-05-09). `openssh-server` installed + hardened `sshd_config` on `cemini-prod`. Verified end-to-end connectively from workspace laptop. Prereq for Step 82. Brief: `briefs/2026-05-09_step81-sshd-prod.md`.
- **Step 82 — Prod Smoke Test**: ✅ **FULL PASS** (Redis + EMS blockers resolved prod-side 2026-05-12 per user report). Conductor pipeline ✅, Stash ✅, Calibration ✅, Redis ✅, EMS ✅. See `briefs/2026-05-09_step82-production-smoke-test.md`.
- **Next**: **Step 83 (live deployment) unblocked.** Workspace-side cascade: (a) ✅ `briefs/2026-05-12_fastmcp-policy-hardening.md` **STAGED 2026-05-12** (K39 OpenShell extraction; Phase 1 workspace-laptop ≈1d / Phase 2 cemini-prod CONDITIONAL-GO ≈3-5d; audit 93.5/100 WARN); (b) ✅ **codeboarding Phase 2 first-pass STAGED 2026-05-12** at `/tmp/cemini-codeboarding-output/` — health report 91.4/100; 21 function-size warnings; 7 god classes (`TradingTools` 1,040 LOC worst); 669 unused-code findings (pyright); architectural stack inventory captured (MetaAgent). Full Phase-2 component diagrams not produced (macOS `/private/tmp/` symlink cache mismatch — follow-up run on prod-side directly); (c) ✅ **tech-debt-skill Phase 2 first audit STAGED 2026-05-12** at `briefs/2026-05-12_cemini-prod-tech-debt-audit.md` — 10 ranked findings + 1 codeboarding-derived candidate; remediation triage prioritized; **none block Step 83 deployment**; (d) ✅ **prod-brief re-stage verification CLOSED 2026-05-12** at `briefs/2026-05-12_prod-brief-restage-verification.md` (audit 100/100 PASS) — **11 of 11 active briefs STILL CURRENT**, zero stale, zero superseded. Step 82 PASS enables (does not invalidate) the assumed EMS/Redis-up posture every active brief relies on. Server-Claude can pick up any brief in priority order; recommended sequence: mcp-context-optimization → polymarket-onchain → pykalshi → polymarket-stack → conductor-audit-trail → remaining 6. **Tech-debt audit Finding #1 SHIPPED 2026-05-12**: `ssh cemini-prod rm -rf /opt/cemini/.claude/worktrees/` — 60 MB editor-scratch cleanup; `/opt/cemini/` went 1.3 GB → 1.2 GB; no collateral damage (other `.claude/` config preserved).
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

**K39 Phase-0 RED-FLAG queue CLOSED 2026-05-12** — 5 verdicts committed, all 5 entity pages upgraded `maturity: draft → validated`. 0 GO / 1 CONDITIONAL-GO / 3 NO-GO / 1 REJECT. Two new no-LICENSE pattern catches (meridian + mac-code) push total to 5 occurrences. Meridian OAuth-grafting is verbatim K38 9router pattern (7th mischaracterization aggregate catch). Eval-brief internal-inconsistency mode (mac-code caveat-then-Adopt) formalized in LESSONS.md as a third sub-mode alongside scope-creep + TOS-landmine.

**K39 ingest complete 2026-05-11**. 17-URL `Evaluating Project Links for Stacks.docx` eval brief + Verbalized Sampling paper (arXiv 2510.01171). **5 Phase-0 RED-FLAG queue** opened for Adopt-tier verdicts pending source audit before any install (meridian + deepseek-tui + obscura-headless-browser + mac-code; eval-brief's "production-ready" framing is the recurring tell). 11th license-catalog mode landed: **EUPL-1.2 = AGPL-3.0-equivalent + Article 14.3 IP-sale poison pill** (taranis-ai Reject 2026-05-11). 3rd no-LICENSE pattern occurrence in K39 (after K36 finance-skills + K38 AI-Trader) — none in K39 directly, but K39 surfaced license-claim mismatches the audit caught at Phase-0. **2nd Polymarket arb-bot pattern** confirmed (gabagool joins K38 cloddsbot). VS paper headline: 1.6-2.1× creative-writing diversity, +6.9 pts synthetic-math SFT, zero factuality/safety regression — third orthogonal training-free Conductor layer (with K37 reviewer-agent + signals).

**K37 + K38 ingest complete 2026-05-11**. **Steal-from license verification CLOSED 2026-05-11** (12 items: 11 GREEN MIT/Apache-2.0, 1 RED HKUDS/AI-Trader no-LICENSE-file — 3rd occurrence of pattern, downgraded to pseudocode-only). **K37/K38 Adopt-tier prod candidates** (highest-impact): Visual Crossing Weather + wethr.net (Kalshi/Polymarket weather contracts data stack), Perplexity MCP + 9router + guild MCP (MCP infrastructure cluster), Readme.skill + Google Colab VSCode (workflow). **2 prototype workstreams seeded by paper ingests**: (a) Reviewer-agent Conductor prototype — DeepSeek-R1 reviewer gating side-effecting tools, ~200-400 LOC Phase-0; (b) Signals audit-JSONL prototype — `signals` field on per-trajectory close-out, ~200-300 LOC Phase-0. Cross-wiki routes shipped (3 briefs): markdown-preview-pluk → image-gen-wiki + seo-wiki + 3d-printing-wiki (all markdown-based).

K36 ingest complete 2026-05-10. **Phase-0 audit queue** (before any K36 prod brief drafts): picobot (MCP-native Go gateway, MIT), QuantMuse (Python+C++ quant stack, MIT), Adala (Apache-2.0 data-labeling with reflection loop — 2.5-yr abandonment-risk flag). ctop + finance-skills are laptop-only adoptions (lower blast radius, audit deferred). Cross-wiki route shipped: URL 10 (digital-marketing-pro) → seo-wiki brief `2026-05-10_digital-marketing-pro-claude-ecosystem.md`.

K35 ingest complete 2026-05-10. **All 10 Adopt-tier briefs now staged** (4 prod-target + 6 workspace-laptop-target). Phase-0 audits for the 3 CONDITIONAL-GO items complete 2026-05-10 — all upgraded to **GO**. K35 follow-ups: (1) K35 Steal-from extractions (SPJ algorithm port, TPE sampling, Bradley-Terry, spec-kit template patterns) — still open; (2) **Brief-audit upgrade sprint: sequential ship — steps 1+2+3 SHIPPED 2026-05-10**. Step 1 (`scripts/skill_audit.py` v0.3) ported academic-paper-skills 35-pt framework: 10 checks, 3 new (`brief_completeness` + `risk_discipline` + `phasing`), ops/research-brief exemption gate. Step 2 (v0.4) ported research-paper-writing claim-evidence + abstract synthesis: 12 checks, 2 new (`check_claim_evidence` 0.06, `check_abstract_synthesis` 0.04) carved from citations + prose_quality weights; calibration verified on 7 briefs. Step 3 (v0.5) ported codex pressure-test 4-mode adversarial review prompts via opt-in `--llm-mode` flag (DeepSeek `deepseek-chat` single combined-call structured output) backed by NEW `scripts/_llm_retry.py` 3-tier retry helper (port of kytmanov/obsidian-llm-wiki-local `structured_output.py` Phase 2). Calibration on ARIS adoption brief: Tier 1 success in 15s no retries, REWORK verdict, 4 fatal flaws surfaced (2 HIGH + 2 MEDIUM, one per mode), competition-map correctly identified Cemini's existing stack as displacement. Sprint COMPLETE; hierarchical section optimization (3rd DR-named research-paper pattern) deferred — can plug into the same `--llm-mode` infrastructure later if needed; (3) Workspace-laptop install execution for the 6 K35 GO tools — still open.

### K39 follow-ups

**Phase-0 RED-FLAG queue — CLOSED 2026-05-12** (5 verdicts committed; 0 GO / 1 CONDITIONAL-GO / 3 NO-GO / 1 REJECT):

| Item | Verdict | Rationale (one line) |
|------|---------|----------------------|
| **meridian** | **NO-GO / REJECT 2026-05-12** | OAuth-grafting onto Claude Max credentials CONFIRMED via `tokenRefresh.ts` + `oauthUsage.ts` code audit; K38 9router pattern verbatim repeat. No LICENSE file (5th no-LICENSE occurrence). 7th mischaracterization catch. |
| **deepseek-tui** | **NO-GO 2026-05-12** | Tool legitimate (26,403★ MIT); eval brief mischaracterizes as Claude Code drop-in replacement. Cemini's MCP + skills + hooks investment is non-portable. |
| **obscura-headless-browser** | **NO-GO 2026-05-12** (prod) / CONDITIONAL-CONSIDER (laptop pilot) | Eval brief recommends wholesale 24/7 trading-stack replacement based on memory-savings claims alone, no soak-test/parity data. |
| **mac-code** | **REJECT 2026-05-12** | F_NOCACHE pervasive (22 source files matched) on hot-path inference; projected 6-12-month SSD failure on irreplaceable soldered hardware. No LICENSE file (4th no-LICENSE occurrence in K39). Caveat-then-Adopt eval brief inconsistency. |
| **kepano-obsidian-skills** | **CONDITIONAL-GO 2026-05-12** | First non-mischaracterization in batch (legitimate 30,698★ MIT). Install only if user has separate Obsidian-vault workflow; otherwise pure token-overhead cost (~10K tokens/invocation). |

Audit-clone dirs retained at `/tmp/{meridian,deepseek-tui,obscura,mac-code,kepano}-audit/`. Single Explore subagent batch + spot-check verification flipped meridian from GO → NO-GO (agent read README, code audit found contradiction).

| K39 cluster | Action | Status |
|------|--------|--------|
| **K39 Adopt — drift** | Single-dev Rust file-transfer (MIT), 254★, niche utility; bus-factor flag | **DEFERRED 2026-05-11** — single-dev maintenance risk; not chartered until clear use-case |
| **K39 Reject — taranis-ai** | EUPL-1.2 IP-sale poison pill + 16 GB hardware requirement | **REJECT 2026-05-11** — license catalog mode #11 |
| **K39 Reject — daybreak-openai** | OpenAI enterprise vendor lock-in (cost + family-A TOS risk) | **REJECT 2026-05-11** |
| **K39 Reject — ducky** | Desktop GUI for retired use case | **REJECT 2026-05-11** |
| **K39 Reference-only — open-notebook** | 3-5 GB RAM disqualifies CPX21 prod box | **REFERENCE-ONLY 2026-05-11** — Steal-from architecture only if local-laptop OK |
| **K39 Reference-only — x711** | Closed SaaS "The Hive"; cross-agent-memory pattern worth studying | **REFERENCE-ONLY 2026-05-11** — Steal-from pattern only |
| **K39 Steal-from — nvidia-openshell** | **PHASE-0 GO 2026-05-12** — Apache-2.0 + NVIDIA org verified; 5,852★; policy schemas standalone-portable | Extraction queued for `briefs/2026-MM-DD_fastmcp-policy-hardening.md` (gated on EMS/Redis Step 82 prod unblock). Files to lift: `crates/openshell-policy/src/lib.rs`, `proto/sandbox.proto`, 4 example YAML fixtures (`policy-advisor` closest match for Claude FastMCP container) |
| **K39 Steal-from — gabagool** | **PHASE-0 NO-GO 2026-05-12** — no LICENSE file (8th occurrence) + math duplicates K38 CloddsBot (5-factor risk + Kalshi-aware) | **DEFER-INDEFINITELY** — Kalshi adapter extracts from CloddsBot, skips gabagool |
| **K39 UNAVAILABLE — 3 stubs (opensourceprojects.dev)** | Exa-resolution pass; Tier-1 gap detection will catch as cited-unread | Deferred |
| **VS paper — Conductor integration (Vector 1 HIGH-fit)** | Synthetic trading-scenario generation prototype brief `briefs/2026-05-11_verbalized-sampling-synthetic-scenarios.md`. ~150-250 LOC Phase-0, 2-3 dev-days, ~$30/mo overhead. Feature-flagged + shadow-mode-gated rollout. Third orthogonal training-free Conductor layer with K37 reviewer-agent + signals briefs. | **SHIPPED to prod 2026-05-11** (skill_audit 99.5/100 PASS, SCP verified at `cemini-prod:/opt/cemini/briefs/`). Server-side Claude executes from here. |
| **VS paper — Vectors 2 & 4-5** | Hypothesis ideation (M-fit), prediction-market scenario sim (M-fit), persona/dialogue (LOW-fit) | DEFERRED — Phase 3 of Vector 1 brief covers reviewer-distribution extension (Vector 3); other vectors await Phase 2 stable metrics |

### K37/K38 follow-ups

| Item | Action | Status |
|------|--------|--------|
| **K37 Adopt — Visual Crossing Weather** | 50-yr historical weather depth for Kalshi/Polymarket weather contracts. Pair with K38 wethr.net | **CONDITIONAL-GO 2026-05-11 — DEFERRED 2026-05-11** (no spend now). Phase-0 verdict locked: adopt for backtesting/climatology only; interpolation gap excludes contract-resolution path. ~$0/mo at audited cadence — Free tier sufficient. Reactivate when Cemini begins Kalshi weather-contract backtest scope work. |
| **K37 Adopt — UI-TARS-desktop** | ~~Desktop AI agent; eval verdict Adopt for workflow laptop~~ | **NO-GO 2026-05-11 — REJECT**. Apache-2.0 + 32.9K★ but partially mischaracterized: VLM-inference client (not standalone automation), duplicates `mcp__computer-use__*` + `mcp__claude-in-chrome__*`, adds parallel Accessibility/Screen-Recording surface from ByteDance-domiciled Electron app, free remote operator deprecated. Activation: only if head-to-head benchmark vs Claude vision shows decisive advantage AND ByteDance ToS clears IP-sale-readiness posture. |
| **K37 Adopt — markdown-preview-pluk** | Native macOS .md previewer; cross-wiki briefs shipped to image-gen + seo + 3d-printing wikis | **INSTALLED 2026-05-11** — v0.0.21 DMG (Homebrew absent); /Applications/Markdown Preview.app, MIT, Apple-signed. Default-handler set pending (manual Finder action) |
| **K38 Adopt — wethr.net** | Singular weather Adopt for Kalshi/Polymarket weather contracts | **GO 2026-05-11 — DEFERRED 2026-05-11** (no spend now, $24.99/mo subscription gate). Phase-0 verdict locked: live Kalshi-resolution path. `logic=nws` (Kalshi) / `logic=wu` (Polymarket); station-direct, 30 US airports. Vendor-age <12 mo mitigated via NWS parallel-poll circuit breaker. Reactivate when first Kalshi weather strategy reaches paper-trade phase. |
| **K38 Adopt — Perplexity MCP** | Live-search gap closer (Sonar Pro / Deep Research / Reasoning Pro) | **GO 2026-05-11 — DEFERRED 2026-05-11** (no spend now, pay-per-query Perplexity API ~$5-20/M tokens Sonar Pro, $5-200+/run Deep Research). Phase-0 verdict locked: MIT, 2,181★, official vendor MCP, real `@modelcontextprotocol/sdk@^1.21.1`. Reactivate when workflow live-search need surfaces unaddressable by `mcp__exa__*` OR user clears a $50-200/mo Perplexity budget. |
| **K38 Adopt — 9router** | ~~Token-compressing proxy (~65% reduction claim); MCP infrastructure~~ | **NO-GO 2026-05-11 — DEFER-INDEFINITELY**. Eval-brief mischaracterization: actually a private Next.js 16 + React 19 dashboard, NOT a lean proxy; README claims 20-40% (not 65%); Family-C TOS landmine via OAuth-grafted free tiers. Existing lazy-tool (46% reduction validated) + claude-code-router cover the legitimate compression + routing roles at ~10× lower footprint, zero TOS exposure. |
| **K38 Adopt — guild MCP** | ~~BM25 + int8 ONNX hybrid retrieval — potential Ollama replacement on Hetzner CPX21~~ | **NO-GO 2026-05-11 as kb-server replacement**. Eval-brief mischaracterization: agent-coordination substrate (`quest`/`lore`/`oath`/`brief` primitives), NOT a generic retrieval MCP. Retrieval stack is internal to guild's schema, cannot serve flat wiki markdown. kb-server stays as serving layer (confirms 2026-05-05 decision). Possible CONDITIONAL-GO for separate analyst-session-handoff eval — not chartered. |
| **K38 Adopt — Readme.skill** | ~~Skill catalog discipline pattern~~ | **NO-GO 2026-05-11 — REJECT**. 6th eval-brief mischaracterization: actually a personal-Claude/Codex-usage **profile** generator (Chinese-language Markdown + SVG poster), NOT a repo-stats or skill-catalog tool. Zero overlap with `academic-paper-skills` / `research-paper-writing-skills` / `codex-startup-pressure-test-skill` / `scripts/skill_audit.py`. LICENSE-file missing despite README MIT claim (same blocking pattern as finance-skills K36). 10-dimension framework retained as Steal-from-with-trigger only if future workforce-analytics workstream chartered. |
| **K38 Adopt — Google Colab VSCode** | Workflow laptop integration; first-party Google extension Apache-2.0 | **CONDITIONAL-GO 2026-05-11 — DEFERRED 2026-05-11** (no spend now). Legitimate product, not mischaracterized — but cost-model bleed (free 30 GPU-hrs/wk exhausts in 2-3 days), data egress to GCP, Colab Secrets API not yet in VSCode extension (credential anti-pattern), feature-parity gaps vs web Colab. Activation: both (a) user clears $50-$200/mo budget OR GCP credit allocation, AND (b) scoped non-sensitive use case (no proprietary trading algo / credentials in notebooks). |
| **Conductor reviewer-agent prototype** | Apple Reinforced Agent pattern; DeepSeek-R1 reviewer + DeepSeek-V3 base; selective-trigger gating on `place_order`/`withdraw`. ~200-400 LOC Phase-0 prototype | Recommended next step |
| **Signals audit-JSONL prototype** | DigitalOcean Signals pattern; `signals` field on per-trajectory close-out. Phase 0 schema addition + dashboard filter; ~200-300 LOC | Recommended next step |
| **K37/K38 Steal-from license verification** | 12 items verified | **COMPLETE 2026-05-11** — 11 GREEN (MIT/Apache-2.0 clean for pattern extraction): claude-bootstrap MIT 621★, ASB MIT 247★, beever-atlas Apache-2.0 293★, homelab-hub MIT 541★, ebay-mcp MIT 61★, contextlattice Apache-2.0 102★, google-research Apache-2.0 37,889★, cloddsbot MIT 254★, megamemory MIT 166★, metatron-recon MIT 2,894★, hackers-arise (tutorial site — no GitHub repo, design-doc Steal only). 1 RED: **AI-Trader HKUDS** — NO LICENSE FILE despite README MIT claim (16,123★ project; root listing has zero LICENSE/COPYING file, GitHub `license` API returns null). 3rd occurrence of no-LICENSE pattern after `finance-skills` K36 + `Readme.skill` K38. AI-Trader Steal-from downgraded to **pseudocode-only pattern extraction** (clean-room reimplementation, no direct code copy); upstream-issue filing pending. `license_verified` field added to all 12 entity-page frontmatter; `maturity: validated`. LESSONS.md 2026-05-11 no-LICENSE-pattern entry added. |
| **K37 UNAVAILABLE URLs** (URLs 1, 6, 8, 10, 11, 12, 16, 19) | Exa-resolution pass; Tier 1 gap detection will catch as cited-unread stubs | Deferred |
| **K38 UNAVAILABLE URLs** (URLs 17, 20, 24, 25) | Same — Exa-resolution pass | Deferred |

### K36 follow-ups

| Item | Action | Status |
|------|--------|--------|
| **picobot Phase-0 audit** | MIT confirmed, v0.2.0 / 86 commits / 1.2k★ / last push 2026-03-28, pure-Go SQLite, stdio MCP per spec | **GO ✅ 2026-05-10** |
| **picobot prod adoption brief** | `briefs/2026-05-10_picobot-prod-adoption.md` — Phase 1 Telegram outbound only, soak 7d, then expand | **SHIPPED to prod 2026-05-10** (skill_audit 90/100) |
| **QuantMuse Phase-0 audit** | MIT confirmed BUT C++ engine is cosmetic (pybind11-wrapped Python with 100ms sleeps); 9 commits, 0 tags, 10-mo stale; VaR = `np.percentile` (same as Cemini); LangChain bloat | **NO-GO ❌ 2026-05-10** (downgrade from original Adopt verdict) |
| **Adala Phase-0 audit** | Apache-2.0 confirmed; abandonment claim DEBUNKED (677 commits, 113 in last 6mo, last main 2026-05-08); `LiteLLMChatRuntime.base_url` overridable; Python ≥3.10 CI green | **GO ✅ 2026-05-10** |
| **Adala prod adoption brief** | `briefs/2026-05-10_adala-prod-adoption.md` — Phase 1 sentiment + entity-extraction skills on GDELT, expand to SEC in Phase 2 | **SHIPPED to prod 2026-05-10** (skill_audit 100/100 v0.3); DeepSeek base_url live smoke test **PASS 2026-05-10** (`record_to_record()` returned `{'response': 'ack'}` from `api.deepseek.com` in 1.9 s, 0 mentions of `api.openai.com`) |
| **ctop laptop install** | `npm i -g ctop-claude` → `/Users/claudiobarone/.local/bin/ctop` (binary named `ctop`, not `ctop-claude`); MIT confirmed | **INSTALLED 2026-05-10** — pending interactive token-tracking verification with live Claude Code session |
| finance-skills laptop install | **INSTALLED 2026-05-10** via `npx plugins add himself65/finance-skills --target claude-code --scope user -y` (author's wrapper CLI; auto-registers `~/.claude/plugins/marketplaces/finance-skills` then runs `/plugin install` for each of 6 plugins / 24 skills). Requires Claude Code restart. LICENSE missing despite README MIT claim — upstream [issue #64](https://github.com/himself65/finance-skills/issues/64) filed; Steal-from half (Cemini-prod Python re-impl) BLOCKED pending clarification. | INSTALLED (laptop adopt half ✓ / prod steal-from BLOCKED) |
| mercury-agent Steal extract | Port permission-hardened shell-exec layer + SQLite FTS5 memory schema to Python/FastMCP | DEFERRED |
| Tmux-Orchestrator Steal extract | Port `schedule_with_note.sh` + 30-min auto-commit pattern | DEFERRED |
| digital-marketing-pro Steal extract | Port hallucination-detection + `evals.json` schema → `agents/orchestrator.py` pre-trade validation | DEFERRED |
| LLMops/data-processing Steal extract | Extract regex data-cleaning + LLM-as-judge prompts; skip ZenML/Ray/Trulens orchestration | DEFERRED |

### 0 — Workspace-laptop actionable (K32 + K33 + K35)

| Brief | What it ships | Status |
|-------|---------------|--------|
| `briefs/2026-05-06_obsidian-llm-wiki-local-steal-from.md` | Phase 1 ✓ / Phase 2 deferred | Phase 1 ✓ / Phase 2 deferred |
| `briefs/2026-05-07_regime-disclosure-brief-audit-gate.md` | **SHIPPED 2026-05-08** — `scripts/skill_audit.py` v0.2 with regime-disclosure veto gate | SHIPPED |
| `briefs/2026-05-08_rl-80k-btc-training-results.md` | RL 80K-frame BTC-USD training results, checkpoint for future 500K retrain | NEW |
| `briefs/2026-05-10_aris-adoption.md` (K35) | ARIS Markdown skill files for structured research workflow | **DEFERRED 2026-05-10** — Phase-0 re-audit revealed 78-skill scope (vs. 3 in eval brief); selective triage of workflow-aligned skills (research-wiki/idea-creator/experiment-plan + ~5 others) pending. Reference clone at `/tmp/aris-audit/` |
| `briefs/2026-05-10_github-spec-kit-adoption.md` (K35) | Spec-Driven Development CLI for wiki → production-code transitions | **INSTALLED 2026-05-10** — `uv tool install specify-cli` (`~/.local/bin/specify`); Phase 2 first wiki→code transition deferred until code project exists |
| `briefs/2026-05-10_tech-debt-skill-adoption.md` (K35) | Quarterly Cemini codebase technical-debt audits | **INSTALLED 2026-05-10** — skill file at `~/.claude/skills/tech-debt-audit.md` (12.8KB); Phase 2 first audit run gated by prod-snapshot rsync |
| `briefs/2026-05-10_claude-mem-adoption.md` (K35) | Cross-session persistent observation memory | **INSTALLED + PHASE 2 PASS 2026-05-12** — v13.0.1 worker stable (~2d uptime); 12 distinct sessions / 148 obs / 50-obs SessionStart injection verified cross-session retrieval; 2 anomalies flagged (single-day data window + worker v13.0.1 vs v13.2.0 plugin drift), non-blocking |
| `briefs/2026-05-10_revpdf-adoption.md` (K35) | 15MB offline PDF editor for research extraction | **INSTALLED 2026-05-05** — v4.0.0 at /Applications/; Phase 2 network-isolation smoke pending |
| `briefs/2026-05-10_codeboarding-adoption.md` (K35) | Auto-generated Cemini architecture diagrams | **INSTALLED 2026-05-10** — `uv tool install codeboarding` + 7 LSPs bootstrapped; Phase 2 first mapping run gated by prod-snapshot rsync |

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
| **K37/K38 weather-pair prod brief** (Visual Crossing + wethr.net, not yet drafted) | First Kalshi weather-contract strategy reaches paper-trade phase **OR** user explicitly clears the ~$25/mo subscription budget. Phase-0 verdicts already locked 2026-05-11; brief drafting is the only blocked step. |

The audit-trail subset (`2026-05-05_conductor-audit-trail-phase1.md` above) supersedes Phases 1+5 of the autoresearch brief and ships now.

### 3 — Recurring discipline

| Item | When |
|------|------|
| **License-pattern catalog (10 modes — K32 added License Drift)** apply on each new Gemini DR ingest | Every ingest |
| **post_ingest_workflow** memory rule: ROADMAP + briefs after every ingest commit-and-push | Every ingest |
| **Tier 2 arXiv sweep** — last 2026-05-09 (2 days fresh, within 7-day cadence) | When ≥7 days old |
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
| **2** — proactive Exa sweeps (user-gated) | Active; last sweep 2026-05-09 (within 7-day cadence) |
| **3** — fully autonomous outbound ingest | Rejected (drift / cost / trust grounds) |

---

## Done — 2026-05-11 K37 + K38 + 3-paper ingest (50-URL eval batch + 2 conductor-relevant concept extractions)

### K37 — Evaluating URLs for System Integration (21-URL)

- **Source**: `Evaluating Urls System Integration.docx` (~75 KB), ingested 2026-05-11 → moved to `cemini-librarian:/opt/cemini-bulk/research/`.
- **14 wiki pages**: 1 source (`evaluating-urls-system-integration.md`) + 13 entity stubs (8 reachable + 5 UNAVAILABLE).
- **Tier rollup**: 3 Adopt (Visual Crossing Weather, UI-TARS-desktop, markdown-preview-pluk) | 6 Steal-from (claude-bootstrap, ASB, Beever Atlas, homelab-hub, ebay-mcp, contextlattice) | 3 Reference-only | 1 Defer | 8 UNAVAILABLE.

### K38 — Link Evaluation Brief for Trading Stack (29-URL)

- **Source**: `Link Evaluation Brief for Trading Stack.docx` (~95 KB), ingested 2026-05-11 → moved to `cemini-librarian:/opt/cemini-bulk/research/`.
- **26 wiki pages**: 1 source (`link-evaluation-brief-trading-stack.md`) + 25 entity stubs.
- **Tier rollup**: 6 Adopt (Readme.skill, Perplexity MCP, Google Colab VSCode, 9router, guild MCP, wethr.net) | 6 Steal-from (google-research, CloddsBot, AI-Trader, MegaMemory, hackers-arise OSINT, METATRON) | 5 Reference-only | 3 Defer | 5 Reject (Medusa AGPL hard reject + TokenSpeed + tropicaltidbits + D3Ext/WEF + ssh-keys-manager-stmol) | 4 UNAVAILABLE.

### K37/K38 papers (3 PDFs)

- **Reinforced Agent** (Apple, arXiv 2604.27233v1) → `wiki/sources/reinforced-agent-tool-calling-feedback.md` + concept page `wiki/concepts/reviewer-agent-inference-time-feedback.md`. **HIGH-fit Conductor**. Reviewer agent gates provisional tool calls pre-execution. +5.5% BFCL irrelevance, +7.1% τ²-Bench, o3-mini 3:1 benefit-risk, GEPA +1.5-2.8%. Latency: 6.2× single-turn / 2.4× multi-turn (Cemini multi-turn trading regime amortizes favorably).
- **Signals** (DigitalOcean, arXiv 2604.00356v1) → `wiki/sources/signals-trajectory-triage.md` + concept page `wiki/concepts/agent-trajectory-triage-signals.md`. **HIGH-fit Conductor**. Cheap non-LLM signals (interaction/execution/environment families) attached to every trajectory. 82% informativeness vs 74% heuristic / 54% random. ~200-300 LOC drop-in on top of audit JSONL.
- **ODINI** (BGU 2018, air-gap magnetic-field exfil) → `wiki/sources/odini-air-gap-magnetic-field.md`. Reference-only context (intentional orphan; not adoption-eligible).

### Cross-wiki routes (3)

- `wiki/entities/tools/markdown-preview-pluk.md` routed as briefs to:
  - `image-gen-wiki/briefs/2026-05-11_2026-05-11_markdown-preview-pluk-cross-wiki.md`
  - `seo-wiki/briefs/2026-05-11_2026-05-11_markdown-preview-pluk-cross-wiki.md`
  - `3d-printing-wiki/briefs/2026-05-11_2026-05-11_markdown-preview-pluk-cross-wiki.md`
- All 3 target wikis are markdown-based; macOS native previewer with LaTeX+Mermaid benefits each. Briefs preferred over stubs to avoid maintenance burden in target wikis.

### Lint baseline

- `python3 scripts/wiki_lint.py` post-ingest: **0 cross-wiki dangling**. Other counts (orphans 11, bidir gaps 266, dangling 13, stale tags 110) at pre-existing baseline; no new issues introduced.
- Cross-wiki routing convention learned: briefs live outside `wiki/` (repo-root level), so do NOT use `@wiki-alias/path` syntax in entity Relations sections (lint resolver assumes wiki-relative paths). Use prose mention instead. Applied fix to `wiki/entities/tools/markdown-preview-pluk.md`.

### Pairing observations

- **Reviewer-agent + Signals are architecturally complementary**: reviewer is inline-time (gates risky tool calls before execution); signals are post-hoc triage (attribute trajectories for downstream learning/debugging). Concept pages cross-reference each other. A complete Conductor v2 design uses both in parallel.
- **K37 Visual Crossing + K38 wethr.net = full weather-strategy stack** for Kalshi/Polymarket weather contracts (50-yr historical depth + free current-data API).
- **K38 MCP infrastructure cluster** (Perplexity + 9router + guild) addresses the live-search gap + token-compression + retrieval-engine layers in one ingest pass.

### Pages touched

45 new (5 source + 38 entity + 2 concept). `index.md` + `log.md` updated. `hot.md` rewritten with session-end position cache.

---

## Done — 2026-05-10 skill_audit v0.5 ship (codex pressure-test 4-mode adversarial review + `_llm_retry.py` Phase 2)

### Brief-audit upgrade sprint — step 3 SHIPPED (sprint COMPLETE for the K32 batch)

- Ported `Kappaemme-git/codex-startup-pressure-test-skill` 4 prompt patterns into `scripts/skill_audit.py` v0.5 via opt-in `--llm-mode` flag. Re-styled for brief-audit (tool-adoption) context:
  - `pressure-test` — "find fatal flaws in adopting this tool" (was: find fatal flaws in this startup idea)
  - `problem-validation` — "is the Cemini pain this brief addresses real, or imagined?" (was: is the problem this startup solves real?)
  - `competition-map` — "does Cemini's existing stack already cover this?" (kept the discipline that current behavior is always a competitor)
  - `mvp-plan` — "what is the smallest test that proves/kills the adoption?" (was: 2-week MVP plan for the startup idea)
  - NOT ported: `first-10-customers` (we're not selling), `full` (just runs all the others, redundant with combined-call architecture).
- **Architecture: single combined-call structured output**. One DeepSeek `deepseek-chat` API call per brief returning a Pydantic v2 schema (`FatalFlaw[]` + `verdict` + `competition_check` + `summary` + `model` + `latency_ms`). Aligns with olw's small-flat-schema discipline; keeps API cost to 1 call per `--llm-mode` invocation.
- **Advisory by default**: dynamic findings render alongside static checks but do NOT change the static score. Veto gates (regime-disclosure, Operational Stability, Scientific Integrity) take precedence. `--strict-dynamic` flag upgrades a dynamic "reject" verdict to top-level REJECT iff no static veto gates already fired.
- **NEW infrastructure: `scripts/_llm_retry.py`** (~280 lines). Phase 2 port of `kytmanov/obsidian-llm-wiki-local/src/obsidian_llm_wiki/structured_output.py`. 3-tier retry: Tier 1 (DeepSeek `response_format={"type":"json_object"}` + fill-in-template system prompt + `_unwrap` post-processor) → Tier 2 (regex `_extract_json`: ` ```json` fence → bare ` ``` ` → first `{...}`) → Tier 3 (re-prompt with error feedback, up to `max_retries=2`). Ollama-specific bits stripped. Telemetry reduced to single stderr log line per call.
- **Calibration result** (2026-05-10, `briefs/2026-05-10_aris-adoption.md`):
  - Tier 1 success in 14805ms on first try (no retries triggered)
  - Dynamic verdict: **REWORK** (signal-bearing, not noise — static checks had passed at 99.5/100; dynamic check caught the strategic flaw the static checks couldn't see)
  - 4 fatal flaws surfaced: [HIGH/pressure-test] 78-skill triage deferred without methodology; [HIGH/problem-validation] existing pipelines not demonstrated to fail, pain point unvalidated; [MEDIUM/competition-map] ARIS duplicates DeepSeek + wiki scripts + LangGraph; [MEDIUM/mvp-plan] Phase 1 plan vague, should be single-day test of one ARIS skill
  - Competition check correctly named Cemini's existing stack: "DeepSeek for synthesis, wiki scripts for structured output, LangGraph for multi-step workflows, kb-server for knowledge management"
  - Telemetry: `[_llm_retry] stage=skill_audit_dynamic model=deepseek-chat tier=1 retries=0 latency_ms=14805 status=ok`
- **Updated entities**:
  - `wiki/entities/tools/codex-startup-pressure-test-skill.md` → `maturity: validated`, new `adopted_as: scripts/skill_audit.py v0.5 (2026-05-10)` field, full adoption-status block replacing pending-Phase-1 placeholder.
  - `wiki/entities/tools/obsidian-llm-wiki-local.md` → `maturity: validated`, new `phase2_ported_as: scripts/_llm_retry.py (2026-05-10)` field. Phase 1 + Phase 2 both DONE; Phases 3-4 (orphan suggestion + bidirectional wikilink auto-rewrite in `wiki_lint.py`) deferred — pain-driven, no current need.
- **Sprint COMPLETE**: K32 batch yielded 4 patterns into `skill_audit.py` across v0.3 / v0.4 / v0.5. Hierarchical section optimization (3rd DR-named research-paper pattern) deferred — can plug into `--llm-mode` infrastructure when a real need arises.
- **Anti-pattern avoided**: build-on-demand discipline. The decision to defer `_llm_retry.py` from 2026-05-06 to 2026-05-10 was correct — the helper's API shape (e.g., `stage=` parameter for telemetry tagging) was driven by `skill_audit.py`'s actual needs, not invented.

---

## Done — 2026-05-10 skill_audit v0.4 ship (research-paper-writing claim-evidence + abstract synthesis)

### Brief-audit upgrade sprint — step 2 SHIPPED

- Ported `master-cai/Research-Paper-Writing-Skills` two K32-DR-named domain-portable patterns into `scripts/skill_audit.py` v0.4. Pattern source is abandoned (4 commits / 0 releases) — re-styled as deterministic Python static checks rather than DeepSeek prompts (LLM-as-judge dynamic version deferred to pressure-test step).
- **2 new static checks** added on top of v0.3's 10, bringing v0.4 to 12 checks summing to 1.00:
  - `check_claim_evidence` (weight 0.06) — detects 4 claim labels in adoption-class briefs (license/version/stars/commits); each must co-locate with a verification anchor within ±240 chars (`VERIFIED YYYY-MM-DD`, `Phase-0 audit`, `[Source:`, `[NEEDS VERIFICATION`, `[CONFIRMED]`/`[TENTATIVE]`/`[RETRACTED]`). Duplicate claims deduped via canonical-value grouping (claim anchored if ANY occurrence has anchor nearby). Coverage thresholds: ≥90% full (0.06), ≥70% (0.04), ≥50% (0.02).
  - `check_abstract_synthesis` (weight 0.04) — `## Summary` section quality: length 50-400 words + effort estimate present + verdict-flavored opener (`Adopt`/`Steal-from`/`Reject`/`Reference`/`Defer`/`Install`/`GO`/`NO-GO`/`CONDITIONAL-GO`). 3/3 full (0.04), 2/3 (0.025), 1/3 (0.01).
- **Weight rebalance**: 0.10 carved out of `check_citations` (0.15 → 0.10) and `check_prose_quality` (0.10 → 0.05). Sum still 1.00.
- **Adoption-class gate** `_is_adoption_brief()` (already in v0.3) exempts ops/research briefs from both new checks. Renderer line updated to "12 static checks".
- **Calibration verified 2026-05-10** against 7 representative briefs:
  - K35 fresh adoption (aris, spec-kit, codeboarding, tech-debt): 99.5/100 PASS — initial ARIS run WARN at 98.5 due to verdict-line regex (asterisks wrapping extra text); fixed by tightening to `**GO** — selective adoption deferred 2026-05-10.`
  - Anchoring gaps caught: claude-mem 97.5 WARN (un-anchored `v13.0.1` outside Phase-0 context), revpdf 94.5 WARN (`Proprietary (free)` not co-located with verification)
  - Older adoption briefs WARN at expected gaps: hftbacktest 90.5, polymarket-stack 90.5, picobot-prod 96.0, adala-prod 98.5, guidance-ai 94.5
  - Ops/research briefs properly exempt: step81-sshd 85.0 N/A, polymarket-onchain 100/100 N/A
- **Anti-pattern fix during calibration**: initial `check_claim_evidence` over-counted 4 MIT mentions in ARIS brief as 4 separate claims (1/4 anchored = 25%). Fixed by deduplicating: group occurrences by `(label, canonical_value)` lowercased + whitespace/hyphen-stripped; claim is anchored if any occurrence has anchor nearby. Re-test PASS at `1/1 claims anchored (100%)`.
- **Hierarchical section optimization** (third DR-named pattern from research-paper-writing) NOT ported in v0.4 — requires LLM judgment. Bundled with codex pressure-test step under upcoming `_llm_retry.py` infrastructure.
- Updated `wiki/entities/tools/research-paper-writing-skills.md` to `maturity: validated` + `adopted_as: scripts/skill_audit.py v0.4` + `adopted` tag. Mirrors the v0.3 pattern previously used on `wiki/entities/tools/academic-paper-skills.md`.

---

## Done — 2026-05-10 K35 laptop adoption batch (5 tools installed + ARIS deferred)

### Laptop adoption installs

| Tool | Install | Verification |
|------|---------|--------------|
| `revpdf` v4.0.0 build 53 | One-time $30 purchase at `/Applications/RevPDF Editor.app` (pre-dated K35 eval; install 2026-05-05) | App opens; offline-capable per source claim; Phase 2 network-isolation smoke pending |
| `specify-cli` | `uv tool install specify-cli` → `~/.local/bin/specify` | `specify --version` confirms install; Phase 2 first wiki→code transition deferred until code project exists to scaffold |
| `codeboarding` | `uv tool install codeboarding` → `~/.local/bin/codeboarding`; `codeboarding-setup` bootstrapped 7 LSPs to `~/.codeboarding/servers/` | python/typescript/javascript/php/java/go/rust ready; csharp skipped (dotnet absent — acceptable, Cemini is Python-only). Phase 2 first mapping run gated by prod-snapshot rsync (active session) |
| `tech-debt-skill` | Skill file at `~/.claude/skills/tech-debt-audit.md` (12.8KB) | Slash command `/tech-debt-audit` available in skill catalog; Phase 2 first audit run gated by prod-snapshot rsync |
| `claude-mem` v13.0.1 | (already installed 2026-05-10 earlier in session) | (already documented in 2026-05-10 post-K36 Done) |

### ARIS Phase-0 re-audit deferral
- Cloned `wanshuiyin/Auto-claude-code-research-in-sleep` → `/tmp/aris-audit/` for inspection.
- Discovered **78 SKILL.md files**, not 3 as the original eval brief claimed.
- Two clusters: workflow-aligned (research-wiki/idea-creator/experiment-plan/experiment-audit + ~5 others) vs. academic-LaTeX/patent toolkit (paper-write with REVIEWER_MODEL=gpt-5.4 TARGET_VENUE=ICLR; proof-checker; specification-writing).
- Decision: defer wholesale install on scope mismatch. Selective triage of workflow-aligned skills (~5-10 of 78) is its own workstream.
- Updated `wiki/entities/tools/auto-claude-code-research-in-sleep.md` with `deferred` tag + `phase_0_reaudit` frontmatter field. `briefs/2026-05-10_aris-adoption.md` verdict shifts to "GO — selective adoption deferred".

### Brief restructuring (5 briefs updated)
- All 5 laptop adoption briefs (claude-mem, revpdf, github-spec-kit, codeboarding, tech-debt-skill, aris) restructured to Phase 0/1/2/3 format with explicit success criteria + bare `**GO**` verdict line.
- All 5 PASS skill_audit v0.3 at 99.5-100/100. Architecture section + risk_discipline table + phasing all clean.

---

## Done — 2026-05-10 post-K36 (Adala smoke + skill_audit v0.3 + claude-mem install + 3d-wiki sync)

### Adala DeepSeek live smoke test
- Built `/tmp/adala-smoke/smoke.py` harness using `LiteLLMChatRuntime(model="deepseek/deepseek-chat", base_url="https://api.deepseek.com/v1", api_key=os.environ["DEEPSEEK_API_KEY"])` with Pydantic `AckResponse` response model.
- Result: **PASS** — `record_to_record()` returned `{'response': 'ack'}` in 1.9 s; verbose litellm logs show 3 hits on `api.deepseek.com`, 0 on `api.openai.com`. base_url override holds in practice.
- Updated `wiki/entities/tools/adala.md` adoption gate to `[x] VERIFIED 2026-05-10`. Re-SCPed updated `briefs/2026-05-10_adala-prod-adoption.md` to `cemini-prod:/opt/cemini/briefs/`.

### Brief-audit upgrade sprint — step 1 SHIPPED
- Ported `lishix520/academic-paper-skills` 35-pt / 7-dimension peer-review framework into `scripts/skill_audit.py` v0.3.
- Added 3 new static checks consuming the 0.10 weight headroom: `check_brief_completeness` (5-item checklist, 0.05), `check_risk_discipline` (table format full credit, bullet-list partial credit, 0.03), `check_phasing` (Phase 1 minimum + success_criteria full credit, 0.02). Max static score now 100/100 (10 checks).
- Added `_is_adoption_brief()` gate exempting ops/research briefs from new checks.
- Calibration verified on 7 representative briefs: K36 fresh (picobot 99.5, adala 100) PASS; ops/research (step81-sshd, polymarket-onchain) 82-100 with N/A; older adoption (hftbacktest, guidance-ai, polymarket-stack) 98.0 WARN flagging legitimate gaps (no `**GO**` verdict line, bullet-format risks).
- Updated `wiki/entities/tools/academic-paper-skills.md` to `maturity: validated` + `adopted_as: scripts/skill_audit.py v0.3`.

### claude-mem laptop install
- `npx claude-mem install` ran cleanly — v13.0.1 installed at `~/.claude/plugins/marketplaces/thedotmack`, data dir `~/.claude-mem` populated, worker + ChromaDB MCP supervisor processes running.
- Production defaults verified in `dist/npx-cli/index.js`: `SEMANTIC_INJECT=false` (lazy), `SEMANTIC_INJECT_LIMIT=5`, `CONTEXT_OBSERVATIONS=50`, `SKIP_TOOLS` excludes meta-noise (TodoWrite, Skill, etc).
- Caveat: Claude Desktop OAuth token stale (`~/.claude-mem/oauth-stale.marker`) — worker functional, re-login refreshes the marker.
- Updated `wiki/entities/tools/claude-mem.md` to `maturity: validated` + `laptop_install: VERIFIED 2026-05-10 (v13.0.1)`. Updated `briefs/2026-05-10_claude-mem-adoption.md` GO/NO-GO to `GO — INSTALLED 2026-05-10`.
- Phase 1 3-session smoke test pending 2026-05-11+ at `http://localhost:37702`.

### 3d-printing-wiki librarian sync
- `rsync -avz "/Users/claudiobarone/Desktop/projects/3d printing/wiki/" cemini-librarian:/opt/cemini-wiki/3d-printing-wiki/wiki/` — 57 files, 169 KB sent (95.95× compression).
- `kb ingest /opt/cemini-wiki/3d-printing-wiki/wiki` — 46 docs ingested, 2 skipped.
- All 4 wikis (osint / image-gen / seo-geo / 3d-printing) now queryable via `conductor_query` unified search.

### LESSONS.md addition
- New 2026-05-10 entry: "Two-layer memory: hot.md is curated state, claude-mem is passive observation" — hierarchy (`ROADMAP.md` > `hot.md` > `claude-mem`), trust rules, top-N cap sanity gate.

---

## Done — 2026-05-10 K36 ingest

### Evaluating Code for Trading Stacks (17-URL three-surface batch)
- **Source**: `Evaluating Code for Trading Stacks.docx` (75 KB), ingested 2026-05-10 → moved to `cemini-librarian:/opt/cemini-bulk/research/`.
- **17 wiki pages created**: 1 source (`evaluating-code-for-trading-stacks.md`) + 14 tool entities + 2 concept pages.
- **Tier rollup**: 4 Adopt (picobot, ctop, QuantMuse, Adala) | 4 Steal-from (mercury-agent, Tmux-Orchestrator, digital-marketing-pro, LLMops) | 1 split (finance-skills: Steal-for-Cemini + Adopt-for-workflow) | 2 Reference/Defer (terax-ai, data-formulator) | 3 Reject (AppFlowy AGPL-3.0, dflash CUDA-only, floci AWS-emulator) | 3 UNAVAILABLE.
- **Concept patterns extracted**: `concepts/cross-channel-agent-gateway.md` (picobot + mercury-agent → Telegram/Discord/Slack/WhatsApp routing on MCP) + `concepts/declarative-data-labeling-skills.md` (Adala + finance-skills → 5-element skill definition with reflection loop).
- **Highest-impact Adopt for Cemini prod**: QuantMuse (Python factor analysis + C++17 low-latency core; strip LangChain bloat; CMake/Alpine build). Picobot second-highest (single 9 MB binary retires need for `python-telegram-bot` embedded in orchestrator).
- **Cross-wiki route**: URL 10 (digital-marketing-pro) → seo-wiki brief `2026-05-10_digital-marketing-pro-claude-ecosystem.md` (115 cmds + 67 MCP servers + 5-layer memory + A+→F grading scripts; relevant to local SEO/GEO content authoring workflow).
- **Phase-0 audit queue**: picobot, QuantMuse, Adala (prod blast radius); ctop + finance-skills laptop-only (verification deferred).

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
