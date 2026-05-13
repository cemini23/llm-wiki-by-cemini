# Hot — session-state cache

Ephemeral curator working memory. Read first on session start; rewritten at session end. Gitignored.

## Position (end of 2026-05-13 session — K41 ingest CLOSED, all 11 sources processed)

### K41 ingest (11 sources, 2026-05-13)

Single ingest batch from the May 12 inbox drop. All 11 raw sources:
- **Foundational LLM-agent papers (4)**: Toolformer (2302.04761 Meta Feb 2023) + ReAct (2210.03629 Princeton+Google ICLR 2023) + Generative Agents (2304.03442 Stanford UIST 2023) + LLMs-Get-Lost (2505.06120 MS+Salesforce May 2025)
- **Massif Capital 4Q2025 Letter to Investors** (Jan 16 2026): 15.6% net annualized since inception across 28 quarters
- **Weekly Wizdom newsletter (3)**: Issue #173 (Apr 7) + #175 (Apr 22) + #176 (Apr 29 FOMC)
- **Donny watchlist** (Apr 23): 39 positions, IREN +431% / SBSW +325% top performers
- **X.docx**: Polymarket bot (@AlterEgo_eth Gamma API technical breakdown) + CLAUDE.md 12-rule framework (Forrest Chang → Mnilax extension)
- **x 2.docx**: @theparuchh weather bot operational guide (V3 +45.9% ROI on $130 bankroll, anecdotal)

### K41 pages touched (45 total)

- **11 source pages NEW**: `wiki/sources/{toolformer-schick-2023,react-yao-2022,generative-agents-park-2023,llms-get-lost-multi-turn-laban-2025,massif-capital-4q2025-letter,ww-issue-173-2026-04-07,ww-issue-175-2026-04-22,ww-issue-176-2026-04-29,donny-watchlist-2026-04-23,x-docx-polymarket-claude-md-2026-04-23,x2-docx-polymarket-theparuchh-2026}.md`
- **5 concept pages NEW**: `wiki/concepts/{wicked-problems-capital-allocation,capital-cycle-theory,real-assets-investing-framework,critical-minerals-thesis,polymarket-weather-trading-strategy,claude-md-12-rule-template}.md` (6 new concepts; I miscounted in commit msg as 5)
- **13 entity stubs NEW**: companies (massif-capital + wizard-of-soho-llc) + organizations (weekly-wizdom-newsletter) + people (alteregoeth + theparuchh + mnilax + forrest-chang) + tickers (eqx + gmin + iren + sbsw + elvr + oklo + uec)
- **Updates to existing pages (14)**: open-meteo data-source entity + index.md + log.md + tradingagents.md (added generative-agents backlink) + 10 backlinks across rare-earth-supply-deficit-thesis / rlhf-critic-bias / verbalized-sampling-llm-diversity / agent-trajectory-triage-signals / reviewer-agent-inference-time-feedback / ensemble-weather-forecasting / macro-weather-regime / polymarket-bot-architecture / multi-agent-trading / claude-mem
- **Cross-wiki routing**: evaluated all 11 sources against image-gen/seo/3d-printing/cybersecurity wikis — verdict: all OSINT-domain only, no cross-wiki stubs created.

### K41 headline insights

- **Three-mode preference-data failure taxonomy now CLOSED**: typicality (K39 Verbalized Sampling) + asymmetric-penalty (K40 RLHF Critic Bias) + premature-commitment (K41 LLMs Get Lost: 39% drop sharded → multi-turn). All data-level, all survive perfect reward models, all have training-free inference-time mitigations. Cemini's existing layers (Conductor consolidation + claude-mem replay + reviewer-agent) align cleanly.
- **Foundational agent papers now formally in wiki**: ReAct + Toolformer + Generative Agents + LLMs-Get-Lost. These had been referenced across 46 pre-existing pages by name; K41 provides canonical source citations.
- **Massif Capital corpus introduction**: real-assets fund, 15.6% net annualized since inception (28 consecutive quarters). Wicked-problems framework + capital-cycle theory + assumption-triage discipline are quotable analytical primitives that generalize beyond finance to Cemini Phase-0 audit pattern.
- **Critical observation: Donny watchlist Apr 23 derives from WW #175 Apr 22 (one day later)** — 5+ exact ticker matches in active longs (ELVR, LAR, CRML, USAR/UGAR, METC). Treat Donny + WW as same-source for confirmation purposes; do NOT cite as independent confirmation.
- **Polymarket weather-trading is a portable strategy**: Gamma API two-endpoint pattern + 5 compounding edges. Reviewer-agent (K37) is a clean validation use case for entry decisions.
- **Three independent retail voices on supply-deficit thesis**: Massif (rare earths + nuclear + lithium + copper) + WW (USAR Apr 22 + lithium triplet ELVR/LAR/CRML) + Donny (RE-heavy watchlist) — but Donny derives from WW, so two independent voices. Worth a synthesis brief.

### K41 pending verification flags

- **Forrest Chang 41% → 3% mistake-rate claim** [NEEDS VERIFICATION 2026-05-13]: source-asserted only; no independent benchmark
- **Open-Meteo `bias_correction=true` parameter behavior** [NEEDS VERIFICATION 2026-05-13]: claimed +30-40% accuracy gain; flagged at @entities/data-sources/open-meteo.md
- **@theparuchh V3 +45.9% ROI** [NEEDS VERIFICATION 2026-05-13]: 3-day window, $130 bankroll, anecdotal P&L not independently verified
- **18% → 30% win-rate from 3-bin coverage** [NEEDS VERIFICATION 2026-05-13]: high frequency but low independent-event count

### K41 lint state

- **wiki_lint final pass**: 0 bidirectional gaps / 0 dangling related: / 0 @path body mentions to missing files. (Pre-K41 cleanup closed 376 bidirectional gaps + 20 pre-K40 issues earlier same morning.)
- **Pre-existing tech debt** unrelated to K41 ingest still surfaces: 4 orphans (counterexamples-cycle-factors, leetcode-maang-prep-siagian, 2 sweeps), 124 cited-unread source stubs, 108 stale [NEEDS VERIFICATION] tags ≥7 days old, 26 dangling cross-wiki @wiki-alias links.

### K41 raw-source disposition

All 11 unique raw sources SCPed to `cemini-librarian:/opt/cemini-bulk/research/` with canonical filenames (2 intra-inbox duplicates skipped: LLMs-Get-Lost v1 dup + WW #175 dup). Laptop copies removed. Inbox now empty except `.DS_Store`. Server-side verification: `ssh cemini-librarian "ls /opt/cemini-bulk/research/"` confirmed all 11 land with expected byte sizes 2026-05-13 12:04 UTC.

### Files at canonical paths (post-SCP)

- `2302.04761v1.pdf` (Toolformer)
- `2304.03442v2.pdf` (Generative Agents)
- `2505.06120v1.pdf` (LLMs-Get-Lost)
- `react-yao-2022.pdf` (renamed from `REAC T- SYNERGIZING...pdf`)
- `Massif+Capital+4Q2025+Letter+to+Investors.pdf`
- `WW-issue-173-macro-maneuvers-2026-04-07.pdf` (renamed from `WW - Macro Maneuver.pdf`)
- `WW-issue-175-this-is-how-we-do-it-2026-04-22.pdf` (renamed from `WW - This Is How We Do It.pdf`)
- `WW-issue-176-2026-04-29-fomc-powells-final-bow.pdf` (renamed from `WW_29apr2026.pdf`)
- `X-polymarket-claude-md-2026-04-23.docx` (renamed from `X.docx`)
- `x-2-theparuchh-polymarket-weather-bot-2026.docx` (renamed from `x 2.docx`)
- `donny-watchlist-2026-04-23.pdf` (renamed from `donny watchlist.pdf`)

### Git status (end of session)

- **Commit `e9728d7`**: "K41 ingest 2026-05-13 — 11 sources / 5 concepts / 13 entity stubs" (45 files / +2191 / -12) pushed to origin/main. Pre-commit hook `Detect secrets` PASSED.

### Next in recommended order

1. **Polymarket weather-trading Phase-0 audit** — verify Open-Meteo `bias_correction` API claim independently before any prototype build
2. **`real-assets supply-deficit consensus` brief candidate** — synthesize Massif + WW positions with capex-data verification (Donny filtered out as non-independent)
3. **`capex tracker` brief candidate** — pull Wood Mackenzie / S&P Global / company disclosure capex data for 5-7 sectors; independent audit of capital-cycle thesis
4. **CLAUDE.md audit pass** — current 322 lines exceeds Mnilax 200-line ceiling; bundle with broader workspace tech-debt sweep
5. **Forrest Chang repo stats verification** — Exa-resolution on 41% → 3% mistake-rate claim
6. **Step 83 live deployment** — still unblocked from prior session; server-Claude executes from prod-staged briefs

## Position (carried — end of 2026-05-12 session — K39 Phase-0 RED-FLAG queue CLOSED)

### K39 Phase-0 RED-FLAG batch (5 tools, 2026-05-12)

Single Explore subagent batch + parent spot-check verification. Verdicts:

- **meridian** (rynfar/meridian, 1,221★) — **NO-GO / REJECT 2026-05-12**. OAuth-grafting CONFIRMED at `src/proxy/tokenRefresh.ts:30` (reads `~/.claude/.credentials.json` + macOS Keychain `Claude Code-credentials` service directly) + `tokenRefresh.ts:27-28` (calls `https://platform.claude.com/v1/oauth/token` with hardcoded `OAUTH_CLIENT_ID = "9d1c250a-..."` — Claude Code's own ID reused) + `oauthUsage.ts:26-27` (private undocumented `api.anthropic.com/api/oauth/usage` with `anthropic-beta: oauth-2025-04-20`). README "No OAuth interception" claim **directly contradicted by code**. LICENSE file ABSENT despite README badge MIT (`gh api license.spdx_id` = null). K38 9router pattern verbatim repeat.
- **deepseek-tui** (Hmbown/DeepSeek-TUI, 26,403★ MIT) — **NO-GO 2026-05-12**. Tool legitimate; eval-brief mischaracterization on Claude Code drop-in framing. Cemini's MCP + skills + hooks investment is non-portable to a DeepSeek-only TUI.
- **obscura-headless-browser** (h4ckf0r0day/obscura, 11,945★ Apache-2.0) — **NO-GO 2026-05-12** (prod) / CONDITIONAL-CONSIDER (laptop pilot). Wholesale prod-stack replacement on 24/7 trading infra unjustified.
- **mac-code** (walter-grace/mac-code, 975★) — **REJECT 2026-05-12**. F_NOCACHE pervasive (22 source files matched) on hot-path inference. Projected 6-12mo SSD failure on irreplaceable soldered hardware. No LICENSE file (4th no-LICENSE in K39).
- **kepano-obsidian-skills** (kepano/obsidian-skills, 30,698★ MIT) — **CONDITIONAL-GO 2026-05-12**. First non-mischaracterization in K39 batch. Install only if user has separate Obsidian-vault workflow; otherwise pure token-overhead cost.

### Aggregates

- **Mischaracterization aggregate now**: **7 catches** total (K28 SwarmVault + K30 PageIndex + K30 Claude-OSINT + K38 9router + K38 guild + K38 Readme.skill + K39 meridian — same K38 9router OAuth-grafting pattern verbatim). Three formalized sub-modes: scope-creep (deepseek-tui, obscura, K28 SwarmVault) + TOS-landmine (meridian, 9router) + caveat-then-Adopt internal inconsistency (mac-code).
- **No-LICENSE-file pattern now**: **8 occurrences** total (K36 finance-skills + K38 Readme.skill + K38 AI-Trader + K39 virattt 58.6k★ + K39 19PINE-AI + K39 meridian + K39 mac-code + K39 gabagool). K39 alone surfaces 5 of 8.

## Monetization-priority directive (2026-05-06)

User: "license its going to be a bit before we sell but i need to start making money here with this soon so we need to do what we need to do."

Effects: license auto-rejects soften for non-prod-codebase use. Phase-0 audit rigor unchanged. Saved as project memory `monetization_priority_2026.md`. Re-confirm 2027+.

## Open follow-ups (K41 — NEW)

- **Polymarket weather-trading Phase-0 audit** — verify Open-Meteo `bias_correction` API claim independently before prototype build
- **`real-assets supply-deficit consensus` brief candidate** — Massif + WW cross-reference with capex-data verification (Donny filtered as non-independent)
- **`capex tracker` brief candidate** — public capex data for 5-7 sectors Massif covers
- **CLAUDE.md audit pass** — 322 lines vs Mnilax 200-line ceiling
- **Forrest Chang 41% → 3% verification** — Exa-resolution candidate
- **Future Massif letters tracking** — 28-quarter series, future ingest as appears

## Open follow-ups (K40 — carried)

- **AutoTS Phase-0 audit** + **voicemode laptop install** + **hunk laptop install** + **veloxdb laptop install** + **anthropic-harness-design adoption** — Phase-0 batch when chartered

## Open follow-ups (K39 — carried)

- ~~**VS Conductor integration Vector 1**~~ — **SHIPPED 2026-05-11** to prod
- **3 K39 UNAVAILABLE URLs** (opensourceprojects.dev) — Exa-resolution pass; Tier-1 gap detection will catch

## Open follow-ups (carried from prior sessions)

- **K37/K38 paper briefs**: 2 SHIPPED to `cemini-prod:/opt/cemini/briefs/` 2026-05-11
- **K37/K38 deferred Adopts**: weather pair (~$25/mo) + Perplexity MCP (pay-per-query) + Colab VSCode — DEFERRED on spend
- **claude-mem Phase 2** — PASS 2026-05-12 (with 2 anomalies characterized: v12.4.3→v13.0.1 migration artifact + version drift)
- **K36 picobot Phase 1 7-day soak** still pending
- **K35 laptop install verification** (5 of 6 installed; Phase 2 smoke tests pending)
- **Cemini-prod ttok install** — staged
- **Step 82 blockers: Redis + EMS** — RESOLVED 2026-05-12; Step 83 unblocked
- **Tier 2 arXiv sweep** — last 2026-05-09 (within 7-day cadence; next due ~2026-05-16)

## Key file locations (end of 2026-05-13)

- ROADMAP: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/ROADMAP.md` (K41 entry top of "Current state")
- log: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/log.md` (K41 entry top)
- index: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/index.md` (updated with 5 concepts + 13 entities)
- K41 sources (11): under `wiki/sources/` — see "K41 pages touched" above for full list
- K41 concepts (6 new — 5 reported + claude-md-12-rule-template): under `wiki/concepts/`
- K41 entity stubs (13): under `wiki/entities/{companies,organizations,people,tickers}/`
- Raw sources at librarian: all 11 at `cemini-librarian:/opt/cemini-bulk/research/` with canonical filenames (see "K41 raw-source disposition" above)
- scripts: `scripts/wiki_lint.py` (hub-page exemption added pre-K41; reached 0 bidirectional gaps 2026-05-13)

## Session-start ritual reminders

1. Read this file
2. Check `wiki/sweeps/*.md` mtime — last sweep 2026-05-09 (within 7-day cadence; next due ~2026-05-16)
3. Check `research to be indexed/` for new sources (currently empty after K41 ingest 2026-05-13; only `.DS_Store` present)
4. If prod desktop-app fails on first message after a Claude Code update: verify `ssh cemini-prod 'env | grep IS_SANDBOX'` returns `IS_SANDBOX=1`.
