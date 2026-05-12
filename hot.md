# Hot — session-state cache

Ephemeral curator working memory. Read first on session start; rewritten at session end. Gitignored.

## Position (end of 2026-05-11 session — K39 ingest COMPLETE)

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
- **VS Conductor integration**: 3 vectors flagged in `concepts/verbalized-sampling-llm-diversity.md` (HIGH-fit synthetic trading-scenario generation, MEDIUM-fit hypothesis ideation, MEDIUM-fit reviewer-agent distribution-of-verdicts extension). Combines with K37 reviewer-agent + signals prototypes that already shipped briefs to `cemini-prod:/opt/cemini/briefs/`.
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
- **VS Conductor integration**: 3 vectors flagged; HIGH-fit synthetic trading-scenario generation is the strongest candidate for a paired-with-reviewer-agent prototype. DEFERRED.
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
