# Hot — session-state cache

Ephemeral curator working memory. Read first on session start; rewritten at session end. Gitignored.

## Position (end of 2026-05-11 session — K40 RLHF Critic Bias ingest COMPLETE + K39 ingest + Tier-1 gap closure)

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
