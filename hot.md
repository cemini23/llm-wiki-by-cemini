# Hot — session-state cache

Ephemeral curator working memory. Read first on session start; rewritten at session end. Gitignored.

## Position (end of 2026-05-12 session — K39 Phase-0 RED-FLAG queue CLOSED)

### K39 Phase-0 RED-FLAG batch (5 tools, 2026-05-12)

Single Explore subagent batch + parent spot-check verification. Verdicts:

- **meridian** (rynfar/meridian, 1,221★) — **NO-GO / REJECT 2026-05-12**. OAuth-grafting CONFIRMED at `src/proxy/tokenRefresh.ts:30` (reads `~/.claude/.credentials.json` + macOS Keychain `Claude Code-credentials` service directly) + `tokenRefresh.ts:27-28` (calls `https://platform.claude.com/v1/oauth/token` with hardcoded `OAUTH_CLIENT_ID = "9d1c250a-..."` — Claude Code's own ID reused) + `oauthUsage.ts:26-27` (private undocumented `api.anthropic.com/api/oauth/usage` with `anthropic-beta: oauth-2025-04-20`). README "No OAuth interception" claim **directly contradicted by code**. LICENSE file ABSENT despite README badge MIT (`gh api license.spdx_id` = null). K38 9router pattern verbatim repeat.
- **deepseek-tui** (Hmbown/DeepSeek-TUI, 26,403★ MIT) — **NO-GO 2026-05-12**. Tool legitimate; eval-brief mischaracterization on Claude Code drop-in framing. Cemini's MCP + skills + hooks investment is non-portable to a DeepSeek-only TUI.
- **obscura-headless-browser** (h4ckf0r0day/obscura, 11,945★ Apache-2.0) — **NO-GO 2026-05-12** (prod) / CONDITIONAL-CONSIDER (laptop pilot). Wholesale prod-stack replacement on 24/7 trading infra unjustified.
- **mac-code** (walter-grace/mac-code, 975★) — **REJECT 2026-05-12**. F_NOCACHE pervasive (22 source files matched) on hot-path inference. Projected 6-12mo SSD failure on irreplaceable soldered hardware. No LICENSE file (4th no-LICENSE in K39).
- **kepano-obsidian-skills** (kepano/obsidian-skills, 30,698★ MIT) — **CONDITIONAL-GO 2026-05-12**. First non-mischaracterization in K39 batch. Install only if user has separate Obsidian-vault workflow; otherwise pure token-overhead cost.

### Aggregates

- **Mischaracterization aggregate now**: **7 catches** total (K28 SwarmVault + K30 PageIndex + K30 Claude-OSINT + K38 9router + K38 guild + K38 Readme.skill + K39 meridian — same K38 9router OAuth-grafting pattern verbatim). Three formalized sub-modes: scope-creep (deepseek-tui, obscura, K28 SwarmVault) + TOS-landmine (meridian, 9router) + caveat-then-Adopt internal inconsistency (mac-code).
- **No-LICENSE-file pattern now**: **5 occurrences** total (K36 finance-skills + K38 Readme.skill + K38 AI-Trader + K39 meridian + K39 mac-code). Both K39 meridian + mac-code had README badges/footers claiming MIT, contradicted by `gh api license.spdx_id` = null. Catalog mode #1 occurrence count in `concepts/cemini-license-posture.md` updated to 7+ (incl. earlier K39 virattt + 19PINE-AI).
- **Process win**: Phase-0 batch caught the meridian flip that the Explore subagent's initial reading missed (agent reported "delegated to SDK" based on README; spot-check of `tokenRefresh.ts` + `oauthUsage.ts` flipped GO → NO-GO). Validates Trust-but-verify discipline.

### Files touched 2026-05-12 (commit pending)

- 5 entity pages: `wiki/entities/tools/{meridian,deepseek-tui,obscura-headless-browser,mac-code,kepano-obsidian-skills}.md` (`phase_0_audit:` + `license_verified:` + `maturity: draft → validated` + body audit findings)
- `wiki/log.md` — new entry on top (2026-05-12 Phase-0 audit batch)
- `LESSONS.md` — new entry on top (2026-05-12 K39 Phase-0 batch + 7th mischaracterization aggregate + 5th no-LICENSE pattern)
- `wiki/concepts/cemini-license-posture.md` — catalog mode #1 row updated 5+ → 7+; K39 Phase-0 batch addendum snippet added; `updated: 2026-05-12`
- `ROADMAP.md` — K39 RED-FLAG queue table closed (all 5 verdicts) + "Next" line updated
- `hot.md` — this file
- Audit-clone dirs retained at `/tmp/{meridian,deepseek-tui,obscura,mac-code,kepano}-audit/`

### Next in recommended order (after this commit)

1. ~~5 K39 Phase-0 RED-FLAG audits~~ — **CLOSED 2026-05-12**
2. ~~claude-mem Phase 2 verification~~ — **PASS 2026-05-12 (with 2 caveats; see below)**
3. ~~K39 Steal-from extractions~~ — **CLOSED 2026-05-12** (1 GO openshell + 1 NO-GO gabagool; see below)
4. ~~Step 82 Redis/EMS blockers~~ — **PROD-SIDE RESOLVED 2026-05-12** (user-reported); Step 83 deployment unblocked.

### Step 82 unblock cascade (workspace-side, 2026-05-12)

Items previously gated on EMS/Redis prod readiness now actionable:

a. ~~`briefs/2026-MM-DD_fastmcp-policy-hardening.md`~~ — **STAGED 2026-05-12 at `briefs/2026-05-12_fastmcp-policy-hardening.md`**. Two-phase plan: Phase 1 (workspace-laptop ≈1d) Pydantic v2 port of `openshell-policy/src/lib.rs` + YAML loader + 4 upstream fixtures + derived `fastmcp-claude.yaml` (Anthropic-only egress). Phase 2 (cemini-prod ≈3-5d) CONDITIONAL-GO — Landlock + network-namespace enforcement, gated on FastMCP traffic inventory. Audit 93.5/100 WARN (all veto-gates clean). Apache-2.0 NOTICE preservation specified at fileheader level.
b. ~~**codeboarding Phase 2** — first prod-snapshot mapping run~~ — **STAGED 2026-05-12 at `/tmp/cemini-codeboarding-output/`**. Health pass complete (`health/health_report.json` overall 91.4/100; 21 function-size warnings; 7 god classes incl. `polymarket_mcp.tools.trading.TradingTools` 1,040 LOC; 669 unused-code findings; component cohesion 100%; no circ-deps surfaced). MetaAgent captured architectural stack (Python 3.12+/FastAPI/Uvicorn/Streamlit/PyTorch/LangGraph/FastMCP/TimescaleDB/Redis Streams; patterns: Microservices/Event-Driven/Pipeline/Layered/Agent-Based/Risk-Gated/CQRS/Strangler Fig/Circuit Breaker/Cryptographic Audit Trail). Full Phase-2 component decomposition diagrams *not* produced — agent hit `/private/tmp/` vs `/tmp/` symlink cache mismatch on macOS, exited in startup. Follow-up run on prod-side directly (or symlink-fix on laptop) would harvest the diagrams. Cross-referenced into tech-debt brief.
c. ~~**tech-debt-skill Phase 2** — first prod-snapshot audit run~~ — **STAGED 2026-05-12 at `briefs/2026-05-12_cemini-prod-tech-debt-audit.md`**. 10 ranked findings (HIGH 4 / MEDIUM 4 / LOW 2) + 1 codeboarding-derived candidate (#11 unused-code). HIGH list: (1) `.claude/worktrees/` 58 MB on prod 30-min fix; (2) `cemini_mcp/server.py` 2,764 LOC god file w/ highest-fan-in functions; (3) HTTP-client rot 69 requests + 81 httpx + 6 aiohttp; (4) kalshi_rest 4-copy 645 LOC near-dup; (4b) `polymarket_mcp/tools/portfolio.py` 1,607 LOC second god file (codeboarding confirms `TradingTools` 1,040 + `WebSocketManager` 774 + `CeminiAutopilot` 513 as additional god classes). Remediation triage prioritized by impact × effort. **None block Step 83 deployment.**
d. **9 staged prod briefs at `cemini-prod:/opt/cemini/briefs/` re-verification** — confirm still current vs. post-EMS/Redis prod state (6 K28-K30 + 3 K31). Stale-brief detection. **Pending** — user did not request in "do b and c" turn; queue for next session.

### K39 Steal-from batch (2 audits, 2026-05-12)

- **NVIDIA/OpenShell** (5,852★ Apache-2.0 NVIDIA-org-owned) — **GO 2026-05-12**. Policy schemas (filesystem read_only/read_write + L4/L7 network endpoints+binaries+method-allowlists + Landlock compatibility) are standalone-portable to FastMCP Python hardening. Extract `crates/openshell-policy/src/lib.rs` (Serde types → Pydantic), `proto/sandbox.proto`, 4 example YAML fixtures. `policy-advisor` example = closest match for Claude FastMCP container. No GPU/CUDA/Docker-socket coupling. **First non-mischaracterized, non-rejected K39 audit verdict**. Extraction queued for separate brief gated on EMS/Redis Step 82 prod unblock.
- **gabagool** (`strongca22-cpu/gabagool`, 180★, README MIT claim) — **NO-GO 2026-05-12**. Two independent blockers: (1) `gh api license.spdx_id` = null = **8th no-LICENSE occurrence**; (2) risk/arb math subset re-implementation of K38-confirmed CloddsBot. Specific overlap: `src/risk_manager.py:110-165` (static thresholds) vs CloddsBot `src/opportunity/risk.ts:374-410` (5-factor weighted decomposition + Kalshi-aware `PLATFORM_RISK_SCORES`). Profit-margin formula identical. Kalshi adapter extracts from CloddsBot, skips gabagool.

### Aggregates after K39 closure

- **K39 batch fully closed**: 17-URL ingest → 7 Phase-0 audits total (5 RED-FLAG + 2 Steal-from). Net: 1 GO (OpenShell), 1 CONDITIONAL-GO (kepano-obsidian-skills), 4 NO-GO (deepseek-tui + obscura + meridian + gabagool), 1 REJECT (mac-code).
- **No-LICENSE-file pattern**: **8 occurrences** total (K36 finance-skills + K38 Readme.skill + K38 AI-Trader + K39 virattt 58.6k★ + K39 19PINE-AI + K39 meridian + K39 mac-code + K39 gabagool). K39 alone surfaces 5 of 8.
- **New observation codified in `wiki/concepts/cemini-license-posture.md`**: Steal-from intent ≠ license-bypass. Pattern extraction requires clean upstream LICENSE for IP-sale-readiness; the no-LICENSE blocker applies symmetrically to Adopt and Steal-from.

### Files touched 2026-05-12 (K39 Steal-from closure commit pending)

- `wiki/entities/tools/nvidia-openshell.md` — frontmatter GO + Phase-0 findings body + extraction plan + `maturity: draft → validated`
- `wiki/entities/tools/gabagool.md` — frontmatter NO-GO + cross-ref-vs-CloddsBot table body + `maturity: draft → validated`
- `wiki/concepts/cemini-license-posture.md` — mode #1 count 7+ → 8+ + new K39 Steal-from addendum snippet
- `wiki/log.md` — new entry on top
- `ROADMAP.md` — K39 Steal-from rows updated with verdict + extraction path
- `hot.md` — this file

### claude-mem Phase 2 verdict (2026-05-12)

**PASS** on all 3 brief success criteria:
- ≥1 high-relevance injection per session: **EXCEEDED** — 50-obs injection this session, all in active topic cluster (K39 / claude-mem / KB-server).
- 0 token-budget overruns: **CONFIRMED** — `CONTEXT_OBSERVATIONS=50` cap held; 22,897t / 50 obs ≈ 458t/obs amortized.
- False-positive injection rate <20%: **CONFIRMED** subjectively — injected obs matched current work; no off-topic noise.
- Cross-session retrieval: **PROVEN** — 12 distinct `memory_session_id` values across 16 SDK sessions; this session received cross-session injection at start.
- Worker health: **STABLE** — PID 99184 v13.0.1, ~2d uptime; dashboard HTTP 200 at localhost:37702; supervisor.json clean; 20 MB data dir.

**Two anomalies investigated 2026-05-12 — both characterized**:
1. **Single-day data window — ROOT CAUSE FOUND**: 45 `[DB] FK fix` events in claude-mem-2026-05-11.log vs 0 on May 12. v12.4.3 → v13.0.1 migration repeatedly rewrote `sdk_sessions.memory_session_id` and orphaned/cascade-deleted in-flight observations. SDK sessions 1-11 show 0 obs in DB; sessions 12-16 retained obs cleanly. **Migration artifact, not steady-state bug** — multi-day retention will work going forward.
2. **Version drift — RESOLUTION PATH IDENTIFIED**: `npx claude-mem --version` resolves to 13.2.0 (npx fetches latest); worker daemon PID 99184 still on v13.0.1 because it started 2026-05-11T02:24:49, pre-v13.2.0. Fix: stop worker → `npx claude-mem install --upgrade` → restart. Deferred to next clean session boundary (don't disrupt live SDK session 15).

Verdict written to `briefs/2026-05-10_claude-mem-adoption.md` Phase 2 section + `wiki/entities/tools/claude-mem.md` Phase 2 section.

## Position (carried — end of 2026-05-11 session — K40 RLHF Critic Bias ingest COMPLETE + K39 ingest + Tier-1 gap closure)

### K40 ingest (RLHF Critic Bias, single source, 2026-05-11)

- **Source**: `rlhf_critic_bias.pdf` — Al-Zawahreh, ARK Research Division, April 2026 self-published pre-print (no arXiv/DOI), 23 pp, sha256 `2544116c5582ca80...`. Moved to `cemini-librarian:/opt/cemini-bulk/research/rlhf_critic_bias.pdf` (verified 319272 bytes); laptop copy removed; inbox empty.
- **Tier**: Reference / Steal-from. **Maturity**: draft.
- **Phase-0 caught 4 structural signals**: (1) self-published (no arXiv/DOI; "ARK Research Division" no independent web presence — flagged NV 2026-05-11), (2) polemical tone (Ghost Committee / automated stagnation engine / Patent Clerk Test), (3) no empirical study (§11 Limitation #1: explicit), (4) author self-acknowledged confirmation bias (§11 Limitation #4: explicit). Posture: operational primitives port; rhetoric does not.
- **Operational extraction**: 5 output patterns (Interesting But / Credentialing Prior / Unfalsifiable Objection / Invention of Flaws / Double Standard) + 6-category Rhetorical Catalog (Diplomatic Opening / Scope Deflation / Generalizability / Authority Challenge / Methodological Hedge / Terminal Unfalsifiable) + 5-tell Forensic Scorecard (content-independence / evidence-contradiction / catalog-match / prompt-contingent reproducibility / absence-of-novel-insight) + 4 mitigations (symmetric reward training / evaluative stance disclosure / evidence-weighted evaluation / anti-laundering watermarks). Asymmetric-penalty equation `E_q[r(criticize,q)] > E_q[r(endorse,q)] ∀ P(q)` is distribution-independent (load-bearing formal anchor).
- **Pages touched (7 total)**: 2 new + 5 edits. NEW: `wiki/sources/rlhf-critic-bias-al-zawahreh-2026.md` + `wiki/concepts/rlhf-critic-bias.md`. EDITED: reviewer-agent + VS + signals + tool-eval-framework + license-posture (each gets 1 inline backlink + 2 frontmatter entries).
- **Cemini relevance**: (a) reviewer-agent (K37) is Mitigation 3+4 in miniature → structural justification; (b) `scripts/skill_audit.py --rlhf-tell-mode` opt-in flag is a steal-candidate (FOLLOW-UP brief, user-gated, **deferred**); (c) mirror failure mode (eval-brief endorsement direction) provides structural explanation for K28+K30+K38's 6 mischaracterization catches.
- **Three-mode preference-data failure taxonomy now codified**: typicality (VS / K39) + asymmetric-penalty (this / K40) + sycophancy (Sharma 2024). All data-level, all survive perfect reward models, all have training-free inference-time mitigations.
- **NEEDS VERIFICATION 2026-05-11**: (1) "ARK Research Division" affiliation; (2) Pangram Labs Nov 2025 21%-AI-generated-ICLR-2026-reviews figure (load-bearing for weaponization argument; original Pangram report not in wiki).
- **Dead Ends documented**: Patent Clerk Test is unfalsifiable counterfactual; Ghost Committee framings are stylistic-not-analytic — do NOT import into wiki narrative voice.

### Tier-1 gap closure (2026-05-11)

- **Type E (thin concept)**: 1 of 1 closed. `concepts/kalshi-api-reference.md` got `## Narrative` section orienting readers to 175-endpoint API by cluster (market data / historical / orders V2 / FIX / WebSocket / portfolio / order groups / RFQ) + SDK posture (pykalshi over official Python SDK).
- **Type D license-batch**: 13 of 44 stale `[NEEDS VERIFICATION 2026-04-29]` tags resolved via `gh api repos/<owner>/<repo> --jq '.license.spdx_id'`. Results:
  - **9 GREEN MIT/Apache** — last30days-skill, mcp-etherscan-server, mcp-server-ccxt, polymarket-trade-engine, agentic-harness-engineering, agent-browser, IRONSIGHT, sightline, metabigor, Ling.
  - **2 NEW NOLICENSE RED** — `virattt/ai-hedge-fund` (**58.6k★** — popularity ≠ license) + `19PINE-AI/ikp` (69★). Catalog mode #1 occurrence count → 5+ across K27/K36/K38/K39. IKP silent-swap-detector adoption blocked at code level.
  - **2 NOASSERTION manual-review** — `h9zdev/GeoSentinel` + `7onez/cti-expert` (custom LICENSE files).
- **Remaining 31 of 44 NV 2026-04-29 tags**: operational/empirical questions (memory leak resistance, accessibility-tree truncation, shadow-account persistence, etc.) — NOT `gh api`-resolvable. Persist until empirical work happens.
- **Catalog impact**: `concepts/cemini-license-posture.md` mode #1 + new Snippets entry documenting `gh api` canonical-source pattern over `crawling_exa` against LICENSE URLs.

### K39 ingest (carried from earlier 2026-05-11)


K39 = 17-URL `Evaluating Project Links for Stacks.docx` eval brief + Verbalized Sampling paper (arXiv 2510.01171).

- **K39 ingest pages touched**: 19 new (2 source + 16 entity + 1 concept).
  - Source pages: `wiki/sources/evaluating-project-links-stacks.md` + `wiki/sources/verbalized-sampling-mode-collapse.md`
  - 13 evaluated entity stubs + 3 UNAVAILABLE `opensourceprojects-dev-*.md` stubs (URL 9, URL 13 noted dup of URL 15, URL 14)
  - 1 concept page: `wiki/concepts/verbalized-sampling-llm-diversity.md` (third orthogonal training-free Conductor layer)
- **Tier rollup**: 6 Adopt + 2 Steal-from + 2 Reference-only + 3 Reject + 3 UNAVAILABLE + 1 noted duplicate = 17 URLs.
- **Raw sources moved**: both `.docx` + `.pdf` SCPed to `cemini-librarian:/opt/cemini-bulk/research/`; laptop copies removed 2026-05-11.
- **Lint**: K39 bidirectional gaps fixed (8 K39-specific edges closed; remaining 292 are pre-existing workspace-wide patterns on `tool-evaluation-framework` + `cemini-license-posture` that pre-date K39).

### K39 Phase-0 RED-FLAG queue (5 items — `phase_0_audit: PENDING` frontmatter)

Eval brief framed each as Adopt, but Phase-0 source-audit discipline (established K28+K30 + reinforced K36+K38) flagged each on pre-audit signals:

1. **meridian** — Family-C TOS-suspect: OAuth-grafting on vendor credentials pattern (K38 9router landmine signature).
2. **deepseek-tui** — Aggressive workflow-migration framing in README; proposes replacing Claude Code as primary interface.
3. **obscura-headless-browser** — Aggressive prod-replacement framing for `mcp__claude-in-chrome__*` + computer-use.
4. **mac-code** — SSD-wear concern via `F_NOCACHE` usage on hot-path workflows.
5. **kepano-obsidian-skills** — CommonMark-vs-Obsidian-flavor uncertainty (wiki uses GitHub-flavored MD; skill portability TBD).

**Mischaracterization aggregate now**: K28 SwarmVault + K30 PageIndex + K30 Claude-OSINT + K38 9router + K38 guild + K38 Readme.skill = 6 catches across K28/K30/K38. K39's RED-FLAG queue is **prevention-mode** — not yet "caught," but flagged before commit.

### K39 license-catalog landing

**11th license-pattern landed: EUPL-1.2 IP-sale poison pill** (taranis-ai Reject 2026-05-11). EU Public License v1.2 = AGPL-3.0-equivalent for network deployments + Article 14.3 binds successors-in-interest (any future Cemini IP-sale acquirer inherits source-disclosure obligation). Default-Reject for production. Reference-only allowed.

### K39 cross-pattern findings

- **2nd Polymarket arb-bot pattern**: gabagool joins K38 cloddsbot. Both MIT, both production trading bots — Cemini's Polymarket arb work has 2 reference implementations now (with overlapping signal patterns worth comparison).
- **VS paper architectural fit**: Verbalized Sampling = third orthogonal training-free Conductor layer (with K37 reviewer-agent + K37 signals). VS at *generation time*, reviewer-agent at *inline call gating*, signals at *post-hoc trajectory triage*. All three sit on the same prompt-and-orchestration substrate, no model retraining. VS headlines: 1.6-2.1× creative-writing diversity, +6.9 pts on synthetic-math SFT, zero factuality/safety regression, stronger-models-benefit-more scaling.

### K39 next steps (deferred — no spend, no Phase-0 burns this session)

- **5 Phase-0 RED FLAG audits** (one per pending entity) — should batch as a single Explore subagent sweep when next chartered.
- **VS Conductor integration Vector 1 SHIPPED 2026-05-11**: `briefs/2026-05-11_verbalized-sampling-synthetic-scenarios.md` (18 KB, skill_audit 99.5/100 PASS) SCPed to `cemini-prod:/opt/cemini/briefs/`. ~150-250 LOC Phase-0, 2-3 dev-days, $30/mo overhead, feature-flagged + shadow-mode rollout, third orthogonal training-free Conductor layer (with K37 reviewer-agent + signals already shipped). Vectors 2/4/5 deferred; Vector 3 (reviewer-distribution) is Phase 3 of the Vector 1 brief (gated on K37 reviewer Phase 1 + this brief Phase 2 stable).
- **3 K39 UNAVAILABLE URLs** (opensourceprojects.dev stubs URL 9 / URL 13 / URL 14) — Exa-resolution pass deferred; Tier-1 gap detection will catch as cited-unread stubs.

## Position (carried — prior session, K37/K38 ingest COMPLETE)

K37/K38 Adopt-tier queue CLOSED 2026-05-11. 6 of 6 Phase-0 audits complete:
- markdown-preview-pluk INSTALLED
- Visual Crossing Weather CONDITIONAL-GO-DEFERRED + wethr.net GO-DEFERRED (weather pair, ~$25/mo deferred on spend)
- Perplexity MCP GO-DEFERRED (pay-per-query, deferred on spend)
- 9router NO-GO DEFER-INDEFINITELY (eval-brief mischaracterization + Family-C TOS)
- guild NO-GO as kb-server replacement (eval-brief mischaracterization)
- UI-TARS-desktop NO-GO (Reject; duplicates `mcp__computer-use__*` + ByteDance IP-sale-readiness concern)
- Readme.skill NO-GO (Reject; eval-brief mischaracterization + no-LICENSE-file)
- Google Colab VSCode CONDITIONAL-GO-DEFERRED (cost-bleed + data-egress to GCP)

K37/K38 Steal-from license verification CLOSED 2026-05-11 (12 items: 11 GREEN MIT/Apache-2.0, 1 RED HKUDS/AI-Trader no-LICENSE-file → pseudocode-only). 3rd occurrence of no-LICENSE pattern (after K36 finance-skills + K38 Readme.skill).

K37/K38 paper briefs SHIPPED 2026-05-11 to `cemini-prod:/opt/cemini/briefs/`:
- `2026-05-11_conductor-reviewer-agent-prototype.md` (Apple Reinforced Agent pattern; DeepSeek-R1 reviewer + DeepSeek-V3 base; selective trigger on side-effecting tools; ~200-400 LOC Phase-0; skill_audit 99.5/100)
- `2026-05-11_signals-audit-jsonl-prototype.md` (DigitalOcean Signals pattern; `signals` field on per-trajectory close-out; ~200-300 LOC Phase-0; skill_audit 99.5/100)

## Position (carried — prior session, K36 ingest COMPLETE)

K36 17-URL trading-stack eval ingested 2026-05-10. Tier rollup: 4 Adopt + 4 Steal-from + 1 split + 2 Reference/Defer + 3 Reject + 3 UNAVAILABLE. Concept extractions: `cross-channel-agent-gateway.md` + `declarative-data-labeling-skills.md`. picobot + Adala prod briefs SHIPPED. QuantMuse Adopt downgraded to NO-GO (Phase-0 caught cosmetic C++ engine).

## Monetization-priority directive (2026-05-06)

User: "license its going to be a bit before we sell but i need to start making money here with this soon so we need to do what we need to do."

Effects: license auto-rejects soften for non-prod-codebase use. Phase-0 audit rigor unchanged. Saved as project memory `monetization_priority_2026.md`. Re-confirm 2027+.

## Open follow-ups (K39 — NEW)

- **5 K39 Phase-0 RED-FLAG audits** queued (meridian + deepseek-tui + obscura-headless-browser + mac-code + kepano-obsidian-skills). Single Explore-subagent batch when chartered.
- **2 K39 Steal-from pattern extractions**: nvidia-openshell policy schemas + gabagool Polymarket arb signals (cross-reference vs cloddsbot). Both DEFERRED.
- ~~**VS Conductor integration Vector 1**~~ — **SHIPPED 2026-05-11** to `cemini-prod:/opt/cemini/briefs/2026-05-11_verbalized-sampling-synthetic-scenarios.md` (18 KB, skill_audit 99.5/100). Server-side Claude executes from here. Vectors 2/4/5 deferred; Vector 3 = Phase 3 of Vector 1 brief.
- **3 K39 UNAVAILABLE URLs** (opensourceprojects.dev) — Exa-resolution pass; Tier-1 gap detection will catch.

## Open follow-ups (carried from prior sessions)

- **K37/K38 paper briefs**: 2 SHIPPED to `cemini-prod:/opt/cemini/briefs/` 2026-05-11. Server-side Claude executes from here.
- **K37/K38 deferred Adopts**: weather pair (~$25/mo) + Perplexity MCP (pay-per-query) + Colab VSCode (cost-model) — DEFERRED on spend. Activation triggers in ROADMAP.
- **claude-mem Phase 1 verification** — DUE 2026-05-11+: 3 sessions over 2-3 days. Track via `http://localhost:37702`.
- **K36 picobot Phase 1 7-day soak** still pending (<25 MB resident target).
- **K36 Steal-from extractions** (DEFERRED): mercury shell-exec + SQLite FTS5; Tmux-Orchestrator scheduling; digital-marketing-pro hallucination-detection; LLMops regex + LLM-as-judge.
- **K37 + K38 + K39 UNAVAILABLE URLs** — combined Exa-resolution pass when chartered.
- **K35 laptop install verification** (5 of 6 installed; Phase 2 smoke tests pending).
- **Cemini-prod ttok install** — staged; awaits prod-side execution.
- **Step 82 blockers: Redis + EMS** — must resolve before Step 83 live deployment.
- **Tier 2 arXiv sweep** — last 2026-05-09 (within 7-day cadence; next due ~2026-05-16).

## Key file locations (end of 2026-05-11)

- ROADMAP: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/ROADMAP.md`
- log: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/log.md` (K39 entry prepended on top of K37/K38 close-out)
- index: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/index.md` (320 canonical stubs after K39 = 197 PDF + 97 docx + 19 md + 5 arxiv-only/deployed)
- license catalog: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/concepts/cemini-license-posture.md` (11th mode = EUPL-1.2 added 2026-05-11)
- new K39 sources (2): `wiki/sources/{evaluating-project-links-stacks,verbalized-sampling-mode-collapse}.md`
- new K39 concept (1): `wiki/concepts/verbalized-sampling-llm-diversity.md`
- new K39 entities (16): `wiki/entities/tools/{drift,kepano-obsidian-skills,open-notebook,nvidia-openshell,taranis-ai,x711,daybreak-openai,gabagool,ducky,meridian,deepseek-tui,obscura-headless-browser,mac-code,opensourceprojects-dev-99aca206,opensourceprojects-dev-1a77fca0,opensourceprojects-dev-c4a3cfc9}.md`
- prior session K37/K38 sources (5) + concepts (2) — see above
- raw sources at librarian: `cemini-librarian:/opt/cemini-bulk/research/{Evaluating Project Links for Stacks.docx,VERBALIZED SAMPLING- HOW TO MITIGATE MODE COLLAPSE AND UNLOCK LLM DIVERSITY.pdf}` (K39) + K37/K38 sources from prior session
- scripts: `scripts/skill_audit.py` v0.5 + `scripts/_llm_retry.py` + `scripts/wiki_lint.py` + `scripts/cross_wiki_route.py` + `scripts/cross_wiki_route.py`

## Session-start ritual reminders

1. Read this file
2. Check `wiki/sweeps/*.md` mtime — last sweep 2026-05-09 (within 7-day cadence; next due ~2026-05-16)
3. Check `research to be indexed/` for new sources (currently empty after K39 ingest 2026-05-11)
4. If prod desktop-app fails on first message after a Claude Code update: verify `ssh cemini-prod 'env | grep IS_SANDBOX'` returns `IS_SANDBOX=1`.
