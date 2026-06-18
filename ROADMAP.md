# Roadmap

Companion to: `CLAUDE.md` (schema), `wiki/log.md` (backward-looking log), `LESSONS.md` (meta-lessons).

---

## Vision

CeminiSuite ships to an institutional buyer with a **verifiable execution-security architecture** (K19+K20+K22+K23), a **research-grounded market-making edge** (K24 ParlayMarket + Kalshi + K28 sports/healthcare prediction-market plumbing), and a **laptop-curated wiki IP catalog**. Each K-series deep-read adds one reusable architectural primitive. Live fleet: **prod + egress-fi only** (librarian deleted 2026-06-14).

## Active workstreams (2026-06-18 — researcher track pivot)

Research digest + ingest briefs target these first (`scripts/active_project_brief_targets.yaml`):

| Priority | Project | Brief home | Prod scp |
|----------|---------|------------|----------|
| 1 | **castle-sim** — Godot RTS slice, playtest parity | `../projects/castle-sim/briefs/` | No |
| 2 | **Poker Arena — dev.fun Researcher Round** | `agents/devfun-poker-arena/briefs/` | sandbox + rsync |
| 3 | **XSP killer bot** — Lane A/B Robinhood monitors | `briefs/xsp-*` | cemini-prod |
| 4 | **PM / Kalshi retail bot** — exploratory botting | `briefs/pm-*` | cemini-prod when bot-touching |

**Poker focus (Jun 18):** Accepted **researcher track** — optimize for **6-max Researcher Round** sandbox LB (500h benchmark assumed, trajectory + multi-axis). Playground S3 continues for optional HUD intel. See `@concepts/devfun-poker-agent-challenge-2026.md`.

## Active workstreams (2026-06-17 — operator pivot)

Research digest + ingest briefs target these first (`scripts/active_project_brief_targets.yaml`):

| Priority | Project | Brief home | Prod scp |
|----------|---------|------------|----------|
| 1 | **castle-sim** — Godot RTS slice, playtest parity | `../projects/castle-sim/briefs/` | No |
| 2 | **Poker Arena** — tournament / HL analyst loop | `agents/devfun-poker-arena/briefs/` | rsync only |
| 3 | **XSP killer bot** — Lane A/B Robinhood monitors | `briefs/xsp-*` | cemini-prod |
| 4 | **PM / Kalshi retail bot** — exploratory botting | `briefs/pm-*` | cemini-prod when bot-touching |

**Deprioritized for auto-briefs:** legacy CeminiSuite MAPPO equity, Riskfolio ladder, conductor harness KPIs — wiki-only unless explicitly reopened.

## Current state (2026-06-17 — K120)

- **K120 ingest (2026-06-17)** — Daily digest full ingest: 2 arXiv from inbox. **2 sources + 2 concepts + 6 updates.** Ensemble RL + classifiers (2502.17518) CONDITIONAL-GO — MIT repro + TradeMaster DJ30 smoke; HPO theory (2606.12612) REFERENCE — GRS/optimality-map steal for Riskfolio ladder. **Phase-0:** `adopt_k120_phase0.sh`. **Prod briefs scp'd (2):** classifier variance-gating; HPO allocation ladder diagnostics. Archive → egress-fi; inbox cleared.

## Current state (2026-06-16 — K119)

- **K119 ingest (2026-06-16)** — Tier-2 sweep + full ingest: 3 arXiv from sweep triage. **3 sources + 2 concepts + 1 entity + 8 updates.** Claw-SWE-Bench (2606.12344) CONDITIONAL-GO — MIT harness attribution benchmark; HarnessFix (2606.06324) REFERENCE — CCC deep-read exists; PRFS (2606.08228) REFERENCE — rejection audit methodology. **Phase-0:** `adopt_k119_phase0.sh`. **Prod briefs scp'd (2):** Claw harness attribution smoke; PRFS filter audit discipline. Archive → egress-fi; inbox cleared.

## Current state (2026-06-16 — K118)

- **K118 ingest (2026-06-16)** — Daily digest full ingest: 4 arXiv from inbox. **4 sources + 4 concepts + 1 entity + 8 updates.** DPG time-inconsistent equilibrium (2606.11798) REFERENCE; Agents All the Way Down (2606.11869) REFERENCE — P4/P5 steal; Orch-RM (2606.13598) REFERENCE — repo 404; tokenized FI admissibility (2606.13822) REFERENCE — 1/4 products informative. **Phase-0:** `adopt_k118_phase0.sh`. **Prod briefs scp'd (2):** Orch-RM conductor BoN design; agent-tests-agent MCP eval layer. **Cross-wiki:** CCC agents-all-the-way-down handoff. Archive → egress-fi; inbox cleared.

## Current state (2026-06-15 — K117)

- **K117 ingest (2026-06-15)** — Daily digest full ingest: 2 arXiv from inbox. **2 sources + 1 concept + 4 updates.** Particle partial-observation control (2606.09055) REFERENCE; regime vol + return prediction CSI 300 (2606.09478) REFERENCE — low-vol gating steal. **Phase-0:** `adopt_k117_phase0.sh`. **Prod briefs scp'd (2):** regime vol gating equity signals; SciConBench clean-room eval (K114 backlog). Archive → laptop `.local/archives/research/`; inbox cleared. **Also committed:** K114 GEO/SciConBench + K116 XSP + librarian decommission backlog.

## Current state (2026-06-14 — K116)

- **XSP wiki (2026-06-14)** — thesis + four-lane framework; **Lane B prod brief** staged (LEAPS inventory + put-hedge alerts).
- **Librarian decommission (2026-06-14)** — Hetzner `cemini-librarian` **deleted**.

## Current state (2026-06-13 — K115)

- **K115 game-dev-wiki bootstrap (2026-06-13)** — New public federation wiki for hobby castle/RTS research + agent harness. **Repo:** `cemini23/Game-Dev-wiki`. Wired: `sync_wiki_to_librarian.sh`, federated daily digest (`game-dev`), federation hub paths, OSINT `@concepts/game-dev-wiki-federation.md`, CCC eval v7 surface 9. Phase 0 research only — no `castle-sim` code repo yet.

## Current state (2026-06-13 — K114)

- **K114 federation ingest (2026-06-13)** — Full wave across 5 wikis + OSINT inbox (7 files). **OSINT:** GEO investigative cluster + SciConBench. **CCC:** 4 arXiv harness/KG. **Cybersec:** VATS + containment gap. **Gambling:** Nous PM + K102–K108 brief close-out. **Image gen:** MentisOculi. **Phase-0:** `adopt_k114_phase0.sh`. **Prod briefs scp'd (3):** VATS MCP error-path; containment gap memory integrity; SciConBench clean-room eval.

## Current state (2026-06-12 — K112)

- **K112 ingest (2026-06-12)** — Posts.docx (8) + 3 arXiv. **4 sources + 3 concepts + 5 updates + 2 tool entities.** CFD provenance-gap attacks; AgentBeats AAA eval; PandaAI neuro-symbolic REFERENCE; Gustafsson log-vs-chain reconciliation. **Phase-0:** `adopt_k112_phase0.sh` (AgentBeats CONDITIONAL-GO). **Prod briefs scp'd (2):** PM UpDown reconciliation telemetry; MCP artifact provenance CFD. Raw → librarian; inbox cleared.

## Current state (2026-06-11 — K111)

- **K111 ingest (2026-06-11)** — Full inbox: 7 PDFs (4 digest arXiv + 3 backlog). **7 sources + 1 concept + 3 updates + 2 tool entities.** AS/CJ ϕ–γ forcing (2606.01477); GIFT + FPQC-SAC FinRL cluster (NO-GO repos); WeaveBench + SIGA agent eval/adapter patterns; ReSA-ConvLSTM weather bias; MIT HFT process thesis. **Poker:** gin-style S1 lane (`2785b1d`). **Phase-0:** `adopt_k111_phase0.sh` (GIFT + FPQC-SAC NO-GO). **Prod briefs scp'd (2):** gin-style S1 deploy; WC kickoff LP safety + cross-venue refresh. Raw → librarian; inbox cleared.

## Current state (2026-06-10 — K110)

- **K110 ingest (2026-06-10)** — Daily digest full ingest: 3 arXiv from inbox. **3 sources + 1 concept + 8 updates.** Instrumental probability / capacity layer (2606.08209); TT-DAC-PS equity execution RL (2606.08379); MCP context prune+summary (2606.10209). **Brief staged (1):** context pruning for conductor/kb-server (REFERENCE). No prod scp. Raw → librarian; inbox cleared.

## Current state (2026-06-09 — K109)

- **K109 ingest (2026-06-09)** — WC prediction markets DR docx (sha `ee93a59a…`) + GS Eq positioning PDF (equity skim). **2 sources + 4 concept/entity updates.** Full PM/Kalshi inventory, `REJ_01`–`04` semantic blocklist, `wc_market_registry.json` vendoring spec. **Prod briefs scp'd (2):** K109 cross-venue scanner recommendations; K108 retail hygiene bot posture. Raw → librarian; inbox cleared.

## Current state (2026-06-09 — K108)

- **K108 ingest (2026-06-09)** — `Posts.docx` (6 posts, sha `b7956893…`). **1 source + 1 concept + 3 entities + 4 updates.** WC retail hygiene (@GodEyeDotFun); Arrakis HL lead-lag; omnifs/42.space stubs. **Phase-0:** omnifs **CONDITIONAL-GO** (Apache-2.0; laptop CCC eval only). **Cross-wiki:** CCC THE HIVE + /ship brief; gambling WC checklist. SEO style pass. K108 WC bot posture brief staged with K109.

## Current state (2026-06-09 — K107)

- **K107 ingest (2026-06-09)** — Full inbox: Posts.docx (17) + 4 arXiv from daily digest. **5 sources + 3 concepts + 1 entity + 3 updates.** Phase-0: AARRI-bench **NO-GO** (no license). **Prod briefs scp'd (4):** LP farming window, covariance-regret audit REFERENCE, WC inflows posture, poker S1 super-audit handoff. **Cross-wiki:** CCC dynamic workflows/skills brief. **Poker:** open-spot PFR audit. Raw → librarian; inbox cleared.

## Current state (2026-06-08 — K106)

- **K106 ingest (2026-06-08)** — `Posts.docx` (6 posts, sha `76b26ee5…`). **1 source + 1 concept + 3 entities + 5 updates.** AS production adaptations (@RuujSs); PM alert SaaS REFERENCE (@whydeso); DexScreener MCP laptop tooling. SEO style pass; CCC brief on disk. No prod scp. Raw → librarian; inbox cleared.

## Current state (2026-06-08 — K105)

- **K105 ingest (2026-06-08)** — Daily digest full ingest: RocketSmith arXiv 2606.00097 + Playground S1 bb snapshot. **1 source + 1 entity + 4 updates** (OSINT); gambling-wiki S1 close (chip #1, adj bb/100 #3 at ≥400h). RocketSmith **REFERENCE** — steal subagent/skill/MCP patterns. Brief staged; no prod scp. Raw → librarian; inbox cleared.

## Current state (2026-06-07 — K104)

- **K104 ingest (2026-06-07)** — `gr4.pdf` (Stanford 2017 ML order-book MM). **1 source + 1 concept + 6 updates.** OBP+RF slight edge vs naive; SVM/SGD underperform; missing news layer = tail risk. **REFERENCE** for PM LP — pair with informedness regime. Brief on disk; no prod scp. Raw → librarian; inbox cleared.

## Current state (2026-06-07 — K103)

- **K103 ingest (2026-06-07)** — Full inbox: Posts.docx (13) + 63-URL tool eval + arXiv 2606.05900 + SSRN 4619084. **4 sources + 4 concepts + 7 entities + 3 updates.** Phase-0 before briefs: pydantic-ai GO; pmxt/asm/Polymarket_data CONDITIONAL-GO; application-skills + Poker-Query-Language NO-GO. **Prod scp'd:** K103 pmxt/pydantic brief + **server-Claude sequence handoff** (K102 WC Module 7 → then K103). `adopt_k103_phase0.sh`. Raw → librarian; inbox cleared.

## Current state (2026-06-06 — K102)

- **K102 ingest (2026-06-06)** — `Tool Evaluation Prompt Analysis.docx` (50 URL, NEW sha256). **1 source + 5 entities + 4 updates.** License batch overturned 12 eval claims; **28 UNAVAILABLE repos resolved** (mostly no-license WC spam). **Phase-0:** harness/typst/defending-code CONDITIONAL-GO; deptry GO; Polymarket-bot STEAL → **WC Module 7 brief**. **Briefs (5)** + prod scp; `adopt_k102_phase0.sh`. Raw → librarian; inbox cleared.

## Current state (2026-06-06 — K101)

- **K101 ingest + deep-read (2026-06-06)** — Federation morning inbox (3 arXiv) + follow-up. **ALE:** 5-task `business_finance/` slice deep-read (repo task cards); mini-ALE harness mapping. **ADK Arena:** Phase-0 **NO-GO** entity (MIT, steal MCP-Atlas GTFA only). NeuroLog → cybersec handoff stub. **Cross-wiki:** CCC ADK Arena stub. Raw → librarian; inbox cleared.
- **MCP smoke matrix (2026-06-06)** — 3-task lazy-tool run; mean GTFA **0.89 PASS**. Report: `.local/reports/mcp-smoke-2026-06-06.md`. **Fixed:** `lazy_tool_enrich_prod_health.sh` (FTS aliases); federation YAML quoting (`fix_cross_wiki_yaml_frontmatter.py`, 28→0 kb errors); scaffold intermediate-state slug rule.

## Current state (2026-06-05 — K100)

- **K100 federation ingest (2026-06-05)** — Morning digest backlog across 6 wikis. **OSINT:** 2606.05882 market informedness + MAVEN REFERENCE + PM-v1 DB REFERENCE; NeuroLog → cybersec. **Siblings:** CCC 3 papers, SEO 2, cybersec 5, gambling 1, image-gen 3. Raw → librarian; inboxes cleared.
- **AutoMEM handoff (2026-06-05)** — Prod brief `2026-06-05_automem-memory-cross-scenario-osint-handoff.md` → OSINT `agent-memory-cross-scenario-generality` + 2606.04315 source. **Verdict:** REFERENCE; CONDITIONAL-GO five-scenario stash/conductor audit before AutoMEM tooling.

## Current state (2026-06-04 — K99)

- **K99 ingest (2026-06-04)** — CCC handoff: arXiv 2606.01886 InKH (financial knowledge harness). **1 source + 1 concept + 7 updates**. Posture: REFERENCE for prod temporal-graph memory until EMS/RBAC review. Brief on disk: `briefs/2026-06-04_inkh-financial-knowledge-harness-osint-handoff.md`. Raw → librarian.

## Current state (2026-06-04 — K98)

- **K98 ingest (2026-06-04)** — Full inbox: `Posts.docx` (13 posts, sha `32400c1f…`) + 3 arXiv + `gr5.pdf`. **5 sources + 7 concepts + 6 updates**. PM: Binance/PM fusion + pre-open queue priority. Agent: five-gate org chart; SeClaw + NEMO REFERENCE. **Briefs:** CCC/cybersec/SEO on disk; **prod brief scp'd** `2026-06-04_k98-pm-latency-fusion-queue-telemetry-cemini-prod.md`. **world-cup-bot:** ROADMAP K98 scope boundary only (no module changes). Raw → librarian; inbox cleared.

## Current state (2026-06-03 — K97)

- **K97 ingest (2026-06-03)** — `Posts.docx` (17 posts, sha `bf5682b3…`). **1 source + 8 page updates**; harness cluster → CCC brief; Roh Posts 15–17 (polytope + FIFA re-share = K94). **Prod brief scp'd:** `2026-06-03_k97-gustafssonkotte-tape-speed-telemetry-cemini-prod.md` (read-only telemetry). SEO style pass K97.

## Current state (2026-06-03 — K96)

- **K96 ingest (2026-06-03)** — Friend CeminiSuite code audit (`Errors in code .docx`) + digest arXiv 2606.00579. **2 sources + `ems-execution-security-gaps` concept**; blind-spot row #14. **Prod brief scp'd:** `2026-06-03_cemini-external-audit-remediation-cemini-prod.md` (P0: Kalshi EMS bypass, PositionGate, RBAC fail-open).

## Current state (2026-06-03 — K95)

- **K95 ingest (2026-06-03)** — Daily digest catch-up (Jun 2–3 LaunchAgent FDA gap; manual run all 7 wikis). **OSINT:** 3 arXiv (AlphaEval, trustworthy-AI fintech, CLI-Anything) + 3 concepts; **CCC:** 5 arXiv harness papers + CLI-Anything cross-wiki; **Image gen:** 6 arXiv; **Cybersec:** skill-injection cluster (3); **Gambling:** opponent modeling + DevFun S28 tournament brief; **3D:** self-improving CAD agents; **SEO:** K88/K90 brief pages ingested. **Prod briefs scp'd:** AlphaEval/governance, WC S28 shock recovery, SkillGuard permission steal. Federation hub sweep `2026-06-03`.

## Current state (2026-06-01 — K93)

- **K93 ingest (2026-06-01)** — 4 inbox files: monokern.docx + arXiv 2605.30621 + v5 tool eval (34 URL) + Posts.docx (31). **5 sources + 3 concepts + federation digest kit + 4 tool pages.** Monokern weekly pipeline in `daily_research_config.yaml`. **Cross-wiki briefs on disk** (6 wikis). Prod brief → cemini-prod. Inbox cleared.

## Current state (2026-06-01 — K92)

- **K92 ingest (2026-06-01)** — 4 inbox files: 2 arXiv (daily digest fetch) + Posts.docx (12) + GitHub eval (90 URLs, casino/poker/stake). **5 sources + 2 concepts** on OSINT; **gambling-wiki** eval slice + WagerBrain/Bovada bot entities; CCC/SEO cross-wiki. Raw → librarian; inbox cleared.
- **K92 Phase-0 adoptions (2026-06-01)** — **Installed:** claude-trading-skills (5 no-API skills), obsidian-second-brain (wiki vault), rlcard venv (`.local/venv-gambling-research`). **Steal-from wired:** WagerBrain → gambling `bankroll-management`; casino-server WS/Redis → `polymarket-sports-lp-operating-rules`. **Skipped:** memory-os (Hermes-only), all NO-GO repos. Re-run: `bash scripts/adopt_k92_phase0.sh`.

## Current state (2026-05-31 — K91)

- **K91 ingest (2026-05-31)** — World Cup DR pair (`Tournament Phase Router Design.docx`, `World Cup Bot Conviction Audit.docx`). **2 new source pages + World Cup concept/entity backlink updates.** Router spec deepens FSM transition-gating + elimination-pruning/test posture; conviction audit flags stale-team downgrade candidates and mode-precedence discipline (`fade_watch` over bilateral in conflict windows). Raw docs moved to librarian; inbox cleared.

## Current state (2026-05-31 — K90)

- **K90 ingest (2026-05-31)** — v6 multi-wiki eval (41 URLs, first **gambling-wiki** surface) + Posts.docx (16 posts + Macro Charts opener). **2 sources + 2 tool stubs + 1 concept.** License spot-check via `gh api`. **Cross-wiki briefs on disk:** gambling-wiki, ccc-wiki, seo-wiki. **Prod brief staged:** `briefs/2026-05-31_k90-multi-wiki-ingest-cemini.md`. Raw docx → librarian; inbox cleared.

## Current state (2026-05-31 — K88)

- **K88 ingest (2026-05-31)** — v5 multi-wiki eval (29 URLs) + Posts.docx (42 posts). **2 sources + 6 tool stubs + 3 concepts.** finance-skills MIT overturn. **Phase-0 done:** SkillSpector **CONDITIONAL-GO** (laptop preingest static scan); OpenOSINT **NO-GO** (eval product mismatch). Prod brief on `/opt/cemini/briefs/`. **Cross-wiki briefs on disk** — user sessions: ccc, cybersec, seo.

## Current state (2026-05-30 — K86)

- **K86 ingest (2026-05-30)** — Gemini DR **10** (tournament phase router) + **targeted GitHub sports/PM landscape**. **2 sources + 4 page updates.** DR 08–10 research chain **complete**; **Module 1b PR1+PR2 shipped** (`922a171`); PR3 replay/FIFA gates remain. **Open:** Phase-0 audit `GastonDeMichele/Polymarket-Sports-Bot`; LP safety DR **2026-06-06**; shadow soak (gate Mon 6/2).

## Current state (2026-05-30 — K84)

- **K84 ingest (2026-05-30)** — 8 inbox items. **Workflow gaps closed** (Obsidian vault, cadences, canvas, LaunchAgents, v5 prompt in CCC). conviction v4 live on prod. **Open:** LP safety re-run 2026-06-06.

## Current state (2026-05-30 — World Cup Bot)

- **Build + automation (2026-05-31)** — [cemini23/world-cup-bot](https://github.com/cemini23/world-cup-bot) main (post knowledge audit). **K88/K89 audit:** negative-filter telemetry + venue CSV reconcile shipped. **167 pytest**.
- **Prod briefs (2026-05-30–31)** — deploy, PR3 reconcile, Phase C exec; **`2026-05-31_wc-prod-knowledge-audit-pull.md`** (pull @ `3d1f045`)
- **Next:** SHADOW Phase 1 soak; LP safety DR **2026-06-06**; K89 Wave 3b wiki enforcement on prod WC executors

## Current state (2026-05-29 — K83)

- **K83 ingest (2026-05-29)** — **4× Gemini DR** World Cup reports (Group B LP, third-place math, cross-venue arbitrage, **live market-gap verification**). **4 sources + 3 concept updates + world-cup-bot entity**. **Bot config:** `conviction.yaml` v3 (Canada/IVC $2500, Bosnia/Qatar fade_watch, DR Congo skip), `cross_venue.yaml` (group-winner + 15 advance cohort pairs; full advance map blocked until PM slugs firm). **Closed:** DeadBall Group B gap; K82 ticker map partial; Module 6 scanner code; prod monitor brief. **Open:** advance-pair refresh when PM lists markets; Gemini report #5 full ticker map (optional).

## Current state (2026-05-29 — K82)

- **K82 ingest (2026-05-29)** — World Cup advance-market bot research wave. **4× Gemini DR + 35 YouTube videos** (DeadBall TV, B Wade, LP-farming, cross-venue). **5 sources + 4 concepts + 8 page updates**. Headline concept: `world-cup-advance-market-bot-v1` — dual deliverable (public MIT OSS + Cemini module); conviction LP + fill handler + alert-only PM↔Kalshi scanner; **all prices from Gamma/CLOB at runtime**. **Public repo:** [cemini23/world-cup-bot](https://github.com/cemini23/world-cup-bot). **Build:** shipped 2026-05-30 (see World Cup Bot section above). **Marketing:** Outlier Weekly Issue 3 — **2026-06-03**. **Open:** CeminiSuite module import (post shadow gate); DeadBall Group B live validation during tournament window.

## Current state (2026-05-29 — K79)

- **K79 ingest (2026-05-29)** — SMB Capital YouTube batches 1–10 (**30 videos**). Batch 10: hidden RS, gap mistakes, drawdown cure. Prod brief updated + shipped.
- **K80 ingest (2026-05-29)** — **Batch 1–2:** 11 PM/Kalshi bot videos. Prod brief shipped. **Complete (bot cluster).**
- **K81 ingest (2026-05-29)** — **Batch 3:** 6 macro/allocator podcasts (McKeown, Burry, Rowan, Coatue, Compound, Meldrum). **1 source + 3 people + 1 company**; PLTR backlink. Transcripts on librarian.

## Current state (2026-05-28 — K76)

- **K76 ingest (2026-05-28)** — four inbox docs (3 engineering syntheses + 2-post `Posts.docx`). **OSINT: 4 sources + 5 concepts + 1 tool entity (REJECT) + 8 page updates**. Concepts: shadow→live transition, zero-trade diagnostics, LP promotion gates, macro rotation watchlist, Skills.md workflow stub. **Phase-0:** `kvrancic/algorithmic-trading-bot` REJECT (no LICENSE). **Prod brief:** `2026-05-28_k76-live-transition-zero-trade-lp-promotion-cemini.md` → `cemini-prod`. **Cross-wiki:** ccc brief for Skills.md/CLAUDE.md expansion. **Adoption:** OTel span workflow on prod ingest path (no new packages). Inbox emptied after librarian SCP.

## Current state (2026-05-28 — K75)

- **K75 prod-audit wiki cluster (2026-05-28)** — SSH read-only audit of cemini-prod PnL + valuation + UI layers. **5 new concept pages**: PnL `logic_version` registry (`pnl-attribution-versioning`), slow-discovery checklist (`production-trading-blind-spots`), prod `core/equity_valuation.py` (`equity-fair-value-evaluation`), logging discipline (`trading-bot-logging-discipline`), `cemini_mcp` `/api/*` wiring (`trading-dashboard-api-wiring`). Captures months-long PnL version-mixing lesson + today's equities fair-value deploy. **No prod brief staged** — wiki-only; brief optional if server-Claude needs registry bump SOP.

## Current state (2026-05-27 — K72)

- **K72 ingest (2026-05-27)** — three inbox sources. **OSINT: 3 sources + 3 concepts + 3 entities + 8 updates**. (1) **arXiv:2605.09998** Continual Harness — online reset-free harness self-improvement (CCC pattern; not prod code). (2) **NBER w10504** Wolfers & Zitzewitz 2004 prediction-markets efficiency survey → `prediction-markets-efficiency-wolfers-zitzewitz` **core** concept. (3) **Posts.docx** 25 posts (`76ccaaa8…`) — ZeroCortex PM throughput pipeline, `hl-funding-sniper` reference, DextersSolab copy-trading refresh. **Prod brief:** `2026-05-27_k72-full-ingest-cemini.md` → `cemini-prod`. **Cross-wiki:** ccc + seo briefs on disk. **No new adoptions.** Inbox emptied after librarian SCP.

## Current state (2026-05-23 — K46–K60)

- **K68 ingest (2026-05-26)** — two inbox docs: `LoMacKinlay1988.pdf` + `Tool Evaluation Prompt Analysis.docx` (22 URLs). **OSINT: 2 new sources + 1 new concept + 5 tool entities + 1 entity update**. Added canonical Lo–MacKinlay variance-ratio source + method page (`lo-mackinlay-variance-ratio-test`) as a pre-ARIMA/GARCH diagnostic primitive. Tool-eval license re-verification caught one overturn: `MadAppGang/claudish` eval-MIT claim → **no LICENSE** (reject). `OpenKB`/`reclip` tracked as doc-level adopt pending Phase-0. **Prod brief:** `2026-05-26_k68-variance-ratio-and-tooling-license-corrections-cemini.md` → `cemini-prod:/opt/cemini/briefs/` (skill_audit PASS). **Cross-wiki briefs (3):** cybersec + ccc + seo. Inbox emptied after librarian SCP.

- **K60 ingest (2026-05-23)** — `GitHub Repo Evaluation for Cemini.docx` (20 URLs, v4). **OSINT: 1 source + 5 tool entities** (kaligpt, trademaster, pentest-ai, **suislanchez**, **polyweather**) + concept updates. License corrections on non-weather URLs. **Weather re-audit (2026-05-24):** suislanchez Steal-from CONDITIONAL-GO (~403★, Kalshi+Poly); PolyWeather AGPL methodology reference; weatherbot reaffirmed MIT canonical. **Prod briefs:** TradeMaster + **`2026-05-24_k60-weather-steal-from-cemini.md`** → `cemini-prod:/opt/cemini/briefs/`. Inbox empty. Lint clean.

- **FLOX + ArcticDB ops (2026-05-23)** — FLOX Phase 1 **compile PASS** on librarian (`libflox-connectors.a`, Polymarket connector in build); Mac blocked (OpenSSL). **market-dataset → ArcticDB** migrated: `lmdb:///opt/cemini-bulk/arctic-market-dataset` / `equity_bars`, **8,507** symbols, ~536 MB; CSV tree kept as fallback. **Prod not rewired** — briefs on `cemini-prod:/opt/cemini/briefs/`. Scripts: `migrate_market_dataset_to_arcticdb.py`.

- **Prod handoff ingested (2026-05-23)** — `cemini-librarian:/opt/cemini-bulk/research/cemini-handoff/`. OSINT wiki: `laptop-prod-research-split` concept + handoff source. **Kronos prompt A/B on prod: REJECT** (do not enable token block). **ArcticDB live benchmark:** tail-1000 0.011s vs pandas 0.109s. **FLOX Step 197:** laptop/cmake only. **Prod→librarian SSH:** use `10.0.0.2` from prod.

- **K59-2 ingest (2026-05-23)** — companion **arXiv:2605.00459** (ILSdl population scale, 12,708 markets). **1 new source**; **4 updated** (ILS concept + ForesightFlow source + microstructure + insider-tracker). **Brief:** `2026-05-23_k59-2-ils-population-scope-discovery-cemini.md` → prod. **Posture:** market-level ILS not prod-ready (~12 interpretable markets); wallet-level surveillance remains primary. Librarian PDF + wiki sync.

- **K59 ingest (2026-05-23)** — Tier-2 arXiv sweep `wiki/sweeps/2026-05-23.md`. **3 papers:** ForesightFlow ILS (2605.00493, Tier-A OSINT) + SkillRAE (2605.10114) + GraphFlow (2605.14968) → ccc brief. **OSINT: 6 new pages** (3 sources + 3 concepts). **5 updated.** **Briefs:** `2026-05-23_k59-foresightflow-ils-pm-surveillance-cemini.md` → prod; local + librarian adoption briefs. **Cross-wiki:** `ccc-wiki/briefs/2026-05-23_k59-skillrae-graphflow-from-osint.md` — **user session needed** to expand stubs to ccc pages. **No egress adoption.** Inbox empty after librarian SCP.

- **K58 ingest (2026-05-23)** — `Machine-Learning-Approach-to-Regime-Modeling_.pdf` (Two Sigma Street View 2021, Botte & Bao). **GMM** on 17-factor U.S. Factor Lens → **Crisis / Steady State / Inflation / WOI**; stress-test + allocation framing; **not predictive**. **OSINT: 2 new pages** (1 source + 1 concept). **6 updated** (Markov regime, regime-conditioned eval, quant-finance, macro-weather, LOB regime source, hedge-fund OSS). **Brief:** `2026-05-23_k58-gmm-regime-stress-test-reference-cemini.md` (skill_audit PASS). Inbox empty.

- **K57 ingest (2026-05-22)** — three inbox sources. **Shipped:** wiki `5fc0b06`, librarian sync (1849 docs), 5 briefs on `cemini-prod:/opt/cemini/briefs/`, Phase-0 complete (flox + near-resolution-bot CONDITIONAL-GO). Cross-wiki briefs on disk in sibling repos (`briefs/` gitignored there — expand in per-wiki sessions). (1) **Posts.docx** — 7 posts: @TheAhmadOsman LLMs 101 + @Gustafssonkotte quadrant/blacklist/micro-trend (day 8) + @0xKiyoro AI influencer playbook + @vorty2797 retail PM discipline + @Suryanshti777 AI OS essay + @polydao Kimi weather revision workflow + @spottr_trade hybrid CLOB copy latency. (2) **Tool Evaluation and Wiki Fit.docx** — **35 URLs** (title says 70): 4 Adopt / 5 Steal-from / 25 Reject / 1 Reference. **License corrections:** `osiris` eval MIT → **still unlicensed** (K51 upheld); `flox` MIT confirmed; `open-design` Apache-2.0 + `the-architect` MIT → ccc briefs. (3) **BowTied Bull newsletter** — Part 1 high-ticket SMB lead-gen (→ seo-wiki); Part 2 macro/crypto [TENTATIVE]. **OSINT: 11 new/updated pages** (3 sources, 4 concepts, 3 people, 1 tool, 4 concept updates). **cemini-prod brief:** `2026-05-22_k57-polymarket-operator-refinements-cemini.md`. **Cross-wiki briefs (4).** Inbox empty. Lint clean (2026-05-22).

- **K55-2 ingest (2026-05-21, late session)** — two inbox sources. (1) **Post.docx** — 5 X-posts: @morpphhhaw perps funding-carry bot **[DUPLICATE — already covered in K55-1; reference-only entry on @entities/people/morpphhhaw.md]**; @ridark_eth "50 GitHub Repos AI Cashflow 2026" (multi-wiki — finance #11-15 + #46 OpenStock + algo/MEV; ccc-fit #2/#16-20/#21/#36/#38/#41/#47; image-gen #7/#22/#24; seo #40/#43-45); **@crptAtlas Oil-on-Polymarket CME settlement vs daily-high vs active-month-roll mechanics** — highest-signal post for prediction-market mechanics, closes a gap in `@concepts/polymarket-bot-architecture.md`; @trq212/Thariq "Unreasonable Effectiveness of HTML" (Claude Blog, cross-routed to ccc-wiki as full concept page); @Cbb0fe +$50M 2020-2021 Uniswap+BSC mempool-sniping memoir — historical MEV reference. (2) **Tool Evaluation for Cemini Wiki.docx** — 50-URL Gemini DR v4 multi-wiki eval; 1 Adopt (`gamma-trade-lab/Polymarket-Near-Resolution-Bot` MIT, the only clean license) / 31 Reject (all NO LICENSE FOUND — known K53/K54 false-negative reproduced again at scale, incl. in-batch error on URL 48 = K52-verified MIT `prediction-market-analysis`) / 17 Unavailable. **OSINT-side: 9 new pages** — 2 source pages, 1 tool entity (polymarket-near-resolution-bot — Adopt-eligible / Phase-0 pending), 4 person entities (@ridark-eth / @crpt-atlas / @thariq-trq212 / @cbb0fe), 2 concept pages (`cme-settlement-mechanics-for-prediction-markets` from @crptAtlas + `dex-mempool-sniping-2020-2021` historical reference from @Cbb0fe). **1 existing entity updated**: @morpphhhaw with K55-2 duplicate-source backlink. **Cross-wiki briefs (4)**: ccc-wiki (full concept page for Thariq HTML essay + brief for ridark-eth CCC-relevant repos), image-gen-wiki (flux/VAR/Qwen3-TTS/VoxCPM/PersonaLive subset), seo-wiki (SaaS-Boilerplate + akaunting/faveo/laracom + FreeDomain PBN-flag), cybersec-wiki (6 cybersec-fit tool-eval entries — CF-Hero/reconftw/LLM4Pentest/jadx-ai-mcp/Awesome-Hacking/open-source-web-scanners). **Reject discipline**: 31 Tool Eval Rejects aggregated on the source page; **no per-tool reject-stub farm**; 9 entries flagged for manual `gh api` license re-verification if adoption interest arises. **No cemini-prod brief** — the single Adopt is a tiny untested micro-repo; Phase-0 audit comes first if/when integration is scoped. **No local or librarian adoptions** — the only Adopt is server-side. **Lint clean** (0 orphans / 0 bidirectional gaps / 0 dangling / 0 missing). Inbox empty. **Server-Claude follow-up**: none requested — Phase-0 audit of `polymarket-near-resolution-bot` is the only forward action, and it can wait for a Cemini-side decision that the niche (late-resolution CLOB mid-price scan) is worth pursuing.
- **K48 ingest (2026-05-21)** — Tier-2 arXiv sweep batch (4 papers): Code-as-Agent-Harness survey (2605.18747) + SAC portfolio WFO (2605.17307) + inference-scaling reasoning LLMs (2605.19775) + self-healing agents (2605.06737). **5 new wiki pages** (4 sources + `code-as-agent-harness` concept). **cemini-prod brief** `2026-05-21_k48-arxiv-sweep-harness-portfolio-rl-inference-cemini.md` (skill_audit PASS). **CCC cross-wiki brief** `2026-05-21_k48-code-as-harness-and-self-healing-from-osint.md`. **Adoptions:** egress-fi API-only reasoning posture (2605.19775); no new packages on laptop/librarian. Wiki synced to librarian. Lint: 0 dangling.
- **K56 ingest (2026-05-21)** — three inbox sources, one K-batch. (1) **Posts.docx** — 9 X-posts (separator "Next Post:"): @Alexo_0x neural-nets-on-Polymarket event-based ML rejection criteria; **anonymous LP-farming live test on Polymarket Drake "Iceman" market** ($50→$18 in 48h / Top 15% LP rank / $300-600 boosted-rewards confirmed → promotes K55 [TENTATIVE] → [CONFIRMED]); @igor_mikerin Pretracer copy-trading promo; @DextersSolab KreoPolyBot 6-figs copy-trading deep-dive with **hedge-leg-trap insight**; @_avichawla Karpathy system-prompt-learning (→ ccc-wiki brief); @phosphenq Monte Carlo Permutation Test per Timothy Masters 2020; @0xDepressionn Karpathy CLAUDE.md (→ ccc); @cyrilXBT Obsidian-as-OS (→ ccc); Post 8 = K55 RohOnChain dup. (2) **Analyzing GitHub Projects and Articles.docx** — 58k-char synthesis report (~14 projects, ~81 citations); OSINT-critical: pmxt 1TB orderbook open-source dataset (~0.25TB/day growth) + utility-marketing playbook; NoFxAiOS/Hackgate cautionary (SlowMist 2025-11-17, zero-auth + hardcoded JWT secrets); Freqtrade/OpenTrader legacy-vs-modern. Cross-wiki routing: cybersec (reverse-eng protocols + reconftw + LLM4Pentest + evilsocket/audit + offensive-claude) + ccc (arkon + Alephant + OpenPipe ART + audit pipeline + presenton + tiptop). (3) **ssrn-5140015.pdf** — Yifan Guo "Applications of Time Series Analysis in Quantitative Finance" (Jan 2025, 21 pages). Academic foundation for K55 time-series ARIMA/GARCH concept page; canonical 4-reference bibliography (Box-Jenkins / Hamilton / Engle / Breiman). **OSINT-side: 17 new pages** — 3 source pages, 3 concept pages (`event-based-prediction-market-ml`, `polymarket-copy-trading-strategy`, `monte-carlo-permutation-test-mcpt`), 6 tool entities (Pretracer NO-AUDIT, KreoPolyBot NO-AUDIT, polymarketanalytics-com USE-AS-INPUT, NOFX REJECT cautionary, Freqtrade REFERENCE-ONLY, OpenTrader REFERENCE-ELIGIBLE), 5 people entities (Alexo_0x / igor_mikerin / DextersSolab / phosphenq / Yifan Guo). **5 existing pages updated**: `polymarket-lp-rewards-farming` (K56 live-test section, $300-600 boosted-rewards [CONFIRMED]), `time-series-arima-garch-framework` (SSRN academic foundation), `pmxt` (1TB orderbook + utility-marketing), `rohonchain` (K56 backlink), `index.md` (K56 sub-sections). **cemini-prod brief**: `briefs/2026-05-21_k56-lp-rewards-confirmation-and-copy-trading-adversary-modeling.md` — LP-farming live-test confirmation, copy-trading adversary modeling, event-based ML caveats for any future Cemini Polymarket directional bot. **Cross-wiki briefs** (2): ccc-wiki (agentic-infra synthesis) + cybersec-wiki (offensive-security tooling). **No local or librarian adoptions** — copy-trading bots are NO-AUDIT; Freqtrade/OpenTrader are reference-only/eligible without active scope; pmxt 1TB dataset is adoption-eligible but deferred to librarian operator. **Lint clean**. Inbox empty. **Server-Claude follow-up**: review the K56 cemini-prod brief — LP-rewards numbers are now concrete enough to size the K55 LP-bot Phase-0 design; copy-trading adversary modeling is a pre-deployment design input for any Polymarket directional bot.

## Current state (2026-05-20 — K46–K55)

- **K55 ingest (2026-05-20)** — five inbox sources, one K-batch. (1) **Posts.docx** — 6 X-posts: @morpphhhaw perps DEX market-neutral funding-carry bot; **@MatiasScalbi Polymarket LP-rewards farming + $POLY airdrop guide** (Spanish) — **user-flagged provide-liquidity idea**; @zostaff Python algo prediction-market guide; @stacyonchain Claude sports-consensus agent (Firecrawl + 5-source tier-weighted); @polysuccubus Top-7 weather traders (ColdMath/Clawdbot #1 +$124K); @gippp69 Shopify-Claude (→ seo-wiki brief). (2) **Posts 2.docx** — 4 X-posts: @RohOnChain Time-Series ARIMA/GARCH framework (companion to K49 Markov post); @AlphaSignalAI deep-dive on @senamakel's OpenHuman v0.54.0 (+20k stars, Product Hunt #1, agentmemory bridge — → ccc-wiki brief); @Gustafssonkotte "Deleted half my bot's code" Polymarket BTC bot rewrite with multi-module conflict-detector (41→60% WR); @MatiasScalbi 21 tactical LP-rewards tips. (3) **1405.1948v2.pdf** — Kakushadze "Phynance" 111-page Ph.D. lecture notes (stochastic calculus + derivative pricing in path-integral language; Spring-2002 Stony Brook YITP). (4) **ssrn-4668072.pdf** — Jim Simons interview (JIC Masters Series V22N1 2023; primary-source operational philosophy: math-not-finance hiring, one-model-continuously-improved, "we stick to the math", data mining endorsed). (5) **Multi-Wiki Tool Evaluation Prompt.docx** — 19-URL eval (v4): 3 Adopt (ai-polymarket-agent / DeLive / src-hunter-skill) / 4 Steal-from / 2 Defer / 4 Reference / 3 Reject (Scalar Field YC SaaS, **CentPRO = the @stacyonchain promoted bot**, CF-Hero) / 1 UNAVAILABLE. **Fifth tool-eval batch re-making the NO-LICENSE-FOUND retrieval-gap pattern** — 6 items need GitHub-API spot-check (license-check follow-up deferred to next session per K53/K54 precedent). **OSINT-side: 20 new pages** — 5 source pages, 7 concept pages (incl. user-flagged `polymarket-lp-rewards-farming`, plus `perps-dex-funding-carry-strategy` / `sports-prediction-consensus-agent` / `time-series-arima-garch-framework` / `multi-module-bot-conflict-detector-pattern` / `stochastic-calculus-foundations` / `hiring-quant-talent-philosophy`), 8 people entities, 1 company (Renaissance Technologies), 1 organization (Quantigic Solutions), 7 tool entities (ai-polymarket-agent Adopt-eligible / CentPRO Reject / Scalar Field Reject / Clawdbot Defer / Parity Defer / Firecrawl Defer / Chainlink Data Streams Conditional-Adopt). **15 existing pages updated** with K55 backlinks. **cemini-prod brief delivered**: `briefs/2026-05-20_k55-polymarket-lp-rewards-and-bot-lessons-cemini.md` (skill_audit PASS 100/100) → `cemini-prod:/opt/cemini/briefs/`. **Cross-wiki briefs** (4): seo-wiki (Gipp Shopify-Claude), ccc-wiki (OpenHuman v0.54 + ai-polymarket-agent + DeLive + src-hunter-skill + catalog items), cybersecurity-wiki (10 items: src-hunter / tugarecon / bluehood / H4X-Tools / super-SPR / CF-Hero / +others), image-gen-wiki (DeLive ASR for persona-ops). **No local or librarian adoptions** — all K55 Adopt-eligibles require Phase-0 audits on the appropriate server/CCC side. **Lint clean** (0 orphans / 0 bidirectional gaps / 0 dangling / 0 missing). Inbox empty. **Server-Claude follow-up**: review the K55 cemini-prod brief — the LP-rewards-farming workstream is the headline (maker-side, distinct from every existing taker-side Polymarket workstream); conflict-detector pattern is portable to every multi-signal strategy; ai-polymarket-agent Phase-0 audit comparison against existing `caiovicentino-polymarket-mcp-server`.

## Current state (2026-05-19 — K46–K54)

- **K54 ingest (2026-05-19)** — two inbox sources, one K-batch. (1) **@AlterEgo_eth Polymarket Bridge API** (`Post.docx`) — a sixth Polymarket API surface (`bridge.polymarket.com`, wallet funding): `/deposit` (multi-chain EVM/SVM/BTC) · `/supported-assets` · `/quote` · `/status` · `/withdraw`; all deposits auto-convert to pUSD on Polygon; the flow must end with a CLOB `/balance-allowance/update` call or the balance is invisible to the order layer. New `polymarket-bridge-api` entity stub + `alterego-eth-polymarket-bridge-api` source; `polymarket-api-reference` upgraded five-surface → six-surface. (2) **26-URL multi-wiki tool eval** (`Tool Evaluation and Wiki Fit.docx`) — 6 Adopt / 1 Steal-from / 5 Reference / 11 Reject / 3 UNAVAILABLE. **Ingested with verification corrections — the eval's license layer was wrong on 9 of 26**, the worst rate yet: 8 false "NO LICENSE FOUND" *plus* a fabricated AGPL-3.0 for MoneyPrinter (verified MIT). 3 OSINT entity pages (QuantDinger Apache-2.0 Adopt-eligible/Phase-0-pending; NextTrade MIT but eval Adopt **downgraded** — TypeScript not Python, ~1yr stale; yt-dlp Unlicense-source Adopt) + poly-arbitrage-bot re-confirmed (MIT — eval's K53 false-negative reproduced). 4 cross-wiki briefs (CCC/Cybersec/Image-gen/SEO). **cemini-prod brief delivered** — `briefs/2026-05-19_k54-polymarket-tooling-cemini.md` (skill_audit PASS 100/100) → `cemini-prod:/opt/cemini/briefs/`: Bridge API funding flow + QuantDinger Phase-0 recommendation + NextTrade downgrade. **Local adoption**: yt-dlp 2026.3.17 installed on the laptop (source-build, Unlicense). No librarian adoption (QuantDinger is server-side/Phase-0-pending). Lint clean (0 orphans / 0 bidirectional gaps / 0 dangling). Inbox empty. **Lesson reinforced**: re-verify *every* eval license claim — positive and negative — not just no-license Rejects (a fabricated AGPL discards a clean tool just as a missed MIT does); recorded in `cemini-license-posture.md`. **Server-Claude follow-up**: review the K54 brief — run a QuantDinger Phase-0 (parallel-implementation check vs the existing `/opt/cemini` engine) before any adoption; Bridge API is documentation-only until autonomous treasury management is scoped.
- **Cemini AI — architecture research (2026-05-19)** — user proposal: add "Cemini AI", a user-facing conversational assistant over DeepSeek + the wiki RAG. Architecture-of-record: `concepts/cemini-ai-assistant.md`. Finding: ~80% of the brain already exists (DeepSeek-V4, kb-server, stash, conductor, 130+ MCP tools) — only the chat surface is new. **Scope (user)**: internal-first (no external users yet), answer + propose-actions with a human confirm gate, finance + cybersecurity wikis. **New infra surfaced**: a third Hetzner server that egresses Polymarket + Hyperliquid orders; near-idle (2 vCPU / 4 GB / 75 GB, load 0.00), recommended host for the internal-phase assistant gateway. Originally provisioned at Falkenstein 2026-05-19 (hostname `cemini-poly-proxy`); **rebuilt at Helsinki 2026-05-20** (hostname `cemini-egress-fi`, IP `204.168.139.190`) after the user verified both PM and HL accept Finnish egress. Entity page `entities/infrastructure/cemini-egress-fi.md`; `.local/server.md` updated with `cemini-egress-fi` SSH alias (jump-host via cemini-prod). **Brief** `briefs/2026-05-19_cemini-ai-assistant.md` → cemini-prod (refresh on Helsinki swap pending). **Server-Claude follow-up**: review the brief — the build is a new FastAPI gateway on `cemini-egress-fi` wiring kb-server + stash + DeepSeek, plus the propose-action confirm gate. Deferred to a pre-external-launch phase: wiki public/internal confidentiality split, per-user stash scoping, prompt-injection hardening, auth/rate-limit/cost quotas. Open: regulatory posture of "propose financial actions" for paying customers.
- **K53 ingest (2026-05-18)** — `Multi-Wiki Tool Evaluation.docx`, a 41-URL multi-wiki tool-eval (v3). 8 Adopt / 1 Steal-from / 6 Reference / 22 Reject / 4 UNAVAILABLE. **Ingested with verification corrections**: the eval's "NO LICENSE FOUND" layer is systematically unreliable — GitHub-API spot-checks flipped 3 Rejects to clean-licensed (poly-arbitrage-bot MIT, polymarket-websocket-client MIT, graphic-walker Apache-2.0), and the ArcticDB BSL-reject was superseded by K52. 5 new OSINT pages (source + gridex/discountifu-polymarket-trading-bot Adopt-eligible + poly-arbitrage-bot/graphic-walker Reference); 4 cross-wiki briefs (CCC/Cybersec/SEO/Image-gen). Inbox now empty. **Lesson reinforced**: never transcribe an LLM eval's no-license rejects — re-verify via GitHub API (recorded in `cemini-license-posture.md`).
- **K53 adoptions (2026-05-18)** — **Librarian**: ArcticDB 6.17.0 installed + smoke-tested on `cemini-librarian` (`/opt/cemini-bulk/.venv`); the market-dataset migration is the remaining operator-gated step. **Local**: gridex deferred — no macOS build published (Windows-only release). **cemini-prod brief shipped** — `briefs/2026-05-18_k53-polymarket-tooling-cemini.md` (skill_audit PASS 100/100) → `cemini-prod:/opt/cemini/briefs/`: discountifu/polymarket-trading-bot review, ArcticDB migration decision, poly-arbitrage-bot + graphic-walker references. **Server-Claude follow-up**: review the K53 brief; decide on the ArcticDB market-dataset migration (benchmark-first) and whether to lift from discountifu/polymarket-trading-bot.
- **K52 ingest (2026-05-18)** — `posts.docx`, 6 X posts. New: `hedge-fund-open-source-tooling` (22 quant-firm OSS repos, @zostaff), `polymarket-updown-bot-taxonomy` (6 microstructure bot types, @RetroValix), `prediction-market-statistical-arbitrage` (cointegration/OU + OBI/micro-price, @ridark_eth), `arcticdb` entity (Man Group BSL tick store — **Phase-0 pending**, license-gated), `hermes-agent` entity (Nous Research runtime — not a Cemini adoption). Updated `polymarket-bot-architecture` (@adiix_official = 3rd independent operator corroboration + battle-tested Type-1 bot prompt) + `polymarket-weather-trading-strategy` (Hermes deploy path). Post 3 (@timbidefi UGC monetization) cross-routed to seo-wiki as a brief. **Follow-ups resolved (2026-05-18)**: (a) @ridark_eth repo verified — `Jon-Becker/prediction-market-analysis` is real (MIT, 3.4k★) but Post 4 misrepresented it (trades/markets dataset, not L2 order book); new entity page, `[RETRACTED]` the L2 claim, Method 2 marked un-backtestable. (b) ArcticDB BSL verified — Additional Use Grant permits Cemini's internal use for free; verdict upgraded Phase-0-pending → **Adopt-eligible**. Both adoptions are server-side (market-dataset layer); **cemini-prod brief shipped** — `briefs/2026-05-18_polymarket-bot-edges-cemini.md` (skill_audit PASS 100/100) → `cemini-prod:/opt/cemini/briefs/`. No laptop-local adoptions (deployment boundary — both candidates are server-side). **Server-Claude follow-up**: review the K52 brief — Up/Down strategy taxonomy, stat-arb Method 1, 3-operator build-discipline audit, ArcticDB + prediction-market-analysis data-layer candidates.
- **K51 ingests (2026-05-18)** — two inbox items. (1) **@AlterEgo_eth Polymarket endpoint cheat sheet** — full five-surface API inventory; new `polymarket-api-reference` concept + Data-API / LB-API / WebSocket entity stubs; endpoint brief shipped to `cemini-prod:/opt/cemini/briefs/`. Resolved a CLOB auth contradiction by direct test (`/book` + `/midpoint` confirmed public, HTTP 200 unauth — cheat sheet's "auth required" claim retracted). (2) **Multi-Wiki Tool Evaluation (36-repo batch)** — **0 Adopt** (no-license epidemic: 24 NO-LICENSE + 9 UNVERIFIED, 1 clean MIT, 1 AGPL); 4 OSINT/finance entity stubs, ~83% cross-routed to cybersec/CCC/image-gen/SEO via 4 destination briefs. **No Phase-0 audits triggered** (nothing reached Adopt); **no local adoptions** (Steal-from ≠ install). License check (2026-05-18) on the 4 license-unverified items: `fd` clean (MIT+Apache — eval's reject was a data artifact, cybersec-primary), `indicator` **AGPL-3.0** (Defer → hard Reject, license-drift poison pill), `osiris` + `mlfinlab` rejects verified (genuinely unlicensed / non-OSS commercial).
- **Cited-unread-stub deep-read campaign COMPLETE** — 98 → 0 genuine unread-stubs across 9 batches (2026-05-16/17). ~64 source pages turned from metadata shells into real deep-read syntheses; ~26 triaged out-of-scope into `@concepts/corpus-overflow-out-of-scope.md`. Spun off 2 promoted concept pages (`rl-retrain-pipeline-hardening`, `marl-trading-architecture`) + 3 cemini-prod briefs.
- **K49 ingest** — tool-eval v3 (46-repo batch) + 3 trading posts + SANA-WM video-world-model (routed to image-gen). 4 OSINT Adopt-tier tool pages (pmxt / PolyTerm / polymarket-insider-tracker / socid-extractor); cross-wiki routing to cybersec / CCC / 3d-printing; K49 prediction-market brief shipped to cemini-prod.
- **Phase-0 audit backlog CLEARED.** Every K44 + K40 queued Phase-0 audit is done (reconciled tables below). K49 added 8 (pmxt CONDITIONAL-GO, PolyTerm GO, Osmedeus GO, jadx-mcp-server GO, socid-extractor GO, SkillKit CONDITIONAL-GO, claude-for-legal STEAL-FROM, Polymarket-Insider-Tracker NO-GO — no LICENSE). Final tail audited 2026-05-17: autots CONDITIONAL-GO, voicemode GO, hunk GO, veloxdb CONDITIONAL-GO.
- **Stale [NEEDS VERIFICATION] sweep** — Exa-cross-checked the backlog: 20 → [CONFIRMED], 3 → [RETRACTED] (PTA paper is 2023/24 not 2026; Zeroboot no egress roadmap; obsidian-bases no nested-formula validation), 3 → [TENTATIVE]; ~38 INTERNAL/empirical tags honestly left un-re-dated. Lint stale-count 144 → 117.
- **gbrain — RETIRED 2026-05-18.** Adopted but unused: a third retrieval layer redundant with kb-server (full-text, bot-facing) + direct file reads (always current). Never load-bearing in real work, and its git-based sync conflicted with the rsync wiki-sync. Removed from `.mcp.json` (both `local` + `librarian` envs). Install still on cemini-librarian (`/opt/gbrain` 328M + `/root/.gbrain` 277M) — purge if disk is ever needed. See `@wiki/entities/tools/gbrain.md`.
- **Librarian wiki-sync FIXED** — the hourly cron had never run (macOS TCC blocks scheduled jobs from `~/Desktop`); replaced with a git `post-commit` hook (primary), the hourly cron restored as a backstop after cron got Full Disk Access, plus a single-run lock on the sync script.
- **K46–K48** — weekly arXiv sweeps + Q1-2026 13F ingest + K47/K48 tool evals + local adoptions (fingerprint-suite, LEANN, socid-extractor). See `wiki/log.md`.
- Wiki health: 0 orphans / 0 bidirectional gaps / 0 dangling / **0 cited-unread stubs**. All 6 wikis committed + pushed.

**Genuinely still pending** (everything in the dated sections below is DONE or superseded unless echoed here):
- **Operator-side**: "The Tail" newsletter 14-day launch (Substack / Stripe / Twitter / static-site host — all operator hands-on; the LLM payload was staged 2026-05-14).
- **Backtests**: three-formula synthesis backtest + insider-detection 3σ backtest — both blocked on historical Polymarket orderbook data.
- **Capex-tracker brief** — awaits user green-light.
- **Server-Claude scope**: review the K47–K50 + MARL-architecture + rl-retrain-hardening briefs in `/opt/cemini/briefs/`; pmxt CONDITIONAL-GO integration conditions (drop baozi adapter, vendor-pin venue SDKs, fork-and-pin); `@pmxt/mcp` needs its own Phase-0.
- **Minor**: counterfactual-prompting claim-discipline CLAUDE.md update (awaits user OK); `cross_wiki_route.py` cosmetic cleanups (brief double-dating, eval-github @path prefix).

## Current state (end of 2026-05-14)

- **K45 sprint OPEN 2026-05-14** (mid-morning → ≈10:20a EDT): **"The Tail" Polymarket rare-event newsletter — 14-day revenue MVP launch.** Driven by `/goal` directive: paid weekly newsletter staged from canonical `briefs/2026-05-14_30day-revenue-launch-plan.md` Track B + `2026-05-14_tier1-monetization-comparison.md` decision; methodology anchored on `@concepts/three-formula-system-polymarket-rare-events.md` (40 % Poisson + 35 % Shannon/KL + 25 % Taleb); landing/About copy GEO/AEO-treated per `@seo-wiki/sources/aggarwal-2024-geo-paper.md` (Quotation Addition / Statistics Addition / Fluency Optimization / Cite Sources). **Full 14-day LLM payload staged: 8 launch-asset briefs, all skill_audit PASS 100/100.** **P1 (Days 1-3) — Brand + infra**: `2026-05-14_the-tail-landing-page.md` (hero + JSON-LD FAQPage schema, Aggarwal-treated) / `2026-05-14_the-tail-about-page.md` (E-E-A-T anchor + public-wiki link) / `2026-05-14_the-tail-public-wiki-mirror.md` (public methodology mirror — paste-ready, Path A static-site recommended over Path B kb-server). **P1 / P2 — Market selection**: `2026-05-14_the-tail-issue1-market-candidates.md` (5 hard filters + 3 soft preferences + 3 illustrative candidates incl. recommended primary Anthropic-Pentagon June-30 with CoI footnote). **P2 (Days 4-7) — Issue 1 worked example**: `2026-05-14_the-tail-issue1-draft.md` (paste-ready ~2,800-word free issue, Anthropic-Pentagon three-formula end-to-end → 0.81% NO weighted output; CoI footnote at section-4 opener; Day-5/6 refresh sidebar). **P3 (Days 8-14) — Launch + distribution**: `2026-05-14_the-tail-twitter-launch-thread.md` (8-tweet character-counted thread) + `2026-05-14_the-tail-issue2-draft.md` (paste-ready ~2,400-word paywalled issue, BTC-ATH August-1 three-formula end-to-end → 3.14% YES weighted output demonstrating the compounding case vs Issue 1; Day-12 refresh sidebar). **P4 (Days 15-30) — Compound**: `2026-05-14_the-tail-linkedin-issue1-repost.md` (~1,400-word LinkedIn Article repost, condensed math + LinkedIn-tuned hashtags) + `2026-05-14_the-tail-issue1-wiki-crosspost.md` (filing-instructions brief for cross-posting Issue 1 worked example as new OSINT wiki concept page + 5 bidirectional backlink patches). **Day-30 success target**: Substack live + Issue 1 (free) + Issue 2 (paid) shipped + ≥30 free signups + ≥10 founders' subs ($19/mo, cap 100) = $190+ MRR (stretch $400+) + public methodology wiki linked. **LLM-side P1-P4 queue is exhausted; remaining 14-day execution is operator hands-on Substack/Stripe/Twitter/static-site-host.** Track A (GEO/AEO local outreach) runs in parallel per the 30-day plan but not staged in this K-series.

### K45 follow-ups (14-day MVP schedule)

| Day | Item | Owner | Status |
|-----|------|-------|--------|
| 1   | Lock Substack handle (`thetail` → fallbacks `outlierweekly` / `asymmetric` / `edgegeometry`) | User | **PENDING** |
| 1   | Connect Stripe + configure founders' ($19/mo, cap 100) + standard ($39/mo) tiers | User | **PENDING** |
| 1-2 | Paste landing-page brief copy into Substack About + headline; inject JSON-LD FAQ via custom HTML or static-site mirror | User | **PENDING** — assets STAGED 2026-05-14 |
| 2-3 | Paste About-page copy; replace `[your-public-wiki-host]` with live URL; configure header nav link | User | **PENDING** — assets STAGED 2026-05-14 |
| 2-3 | Publish public-wiki mirror of `@concepts/three-formula-system-polymarket-rare-events.md` (+ 4 component concept pages) on static host or kb-server public-DNS | User | **PENDING** — host-decision needed |
| 4   | Re-run market screening per `briefs/2026-05-14_the-tail-issue1-market-candidates.md` framework; pick Issue 1 worked-example market | User / fresh LLM session | **PENDING** — framework STAGED |
| 5-7 | Run three-formula model end-to-end on chosen market; draft Issue 1 (2,500-3,000 words, 7-section outline) | User / LLM | **DRAFT STAGED 2026-05-14** in `briefs/2026-05-14_the-tail-issue1-draft.md` (Anthropic-Pentagon default); Day-5/6 refresh sidebar built in |
| 8   | Twitter launch thread goes live (per `briefs/2026-05-14_the-tail-twitter-launch-thread.md`); pin to profile | User | **PENDING** — thread STAGED 2026-05-14 |
| 9   | Issue 1 ships free; forward-track entry filed | User | **PENDING** |
| 10-11 | Reply-burst to every thread response; engagement compounds | User | **PENDING** |
| 12  | Open founders' tier; email all free subs | User | **PENDING** |
| 13  | Draft Issue 2 (paywalled, different market, same methodology) | User / LLM | **DRAFT STAGED 2026-05-14** in `briefs/2026-05-14_the-tail-issue2-draft.md` (BTC-ATH August-1 default); Day-12 refresh sidebar built in |
| 14  | "Founders' tier live — N/100 spots left" push to free list; **Gate review: ≥30 free signups?** If <30 → pivot to Polymarket Discord / r/PredictionMarkets / podcast guesting | User | **GATE** |
| 21  | **Gate review: ≥5 founders' subs?** If <5 → tighten niche to one category (crypto rare-events only) | User | **GATE** |
| 30  | **Gate review: ≥$200 MRR?** If <$200 → re-evaluate; not a 30-day market | User | **GATE** |

**K45 LLM-staged assets summary**: **11 briefs**, all skill_audit PASS 100/100, ready to paste at publish-time. No prod-side execution required (laptop-only workspace). **P1** brand+infra (landing-page + about-page + public-wiki-mirror) + market-selection framework (issue1-market-candidates) = 4. **P2** Issue-1 draft (issue1-draft) = 1. **P3** Twitter thread + Issue-2 draft = 2. **P4** LinkedIn repost + wiki cross-post staging = 2. **Operator-handoff supporting tier**: handoff playbook (consolidated 14-day walkthrough) + email payloads (welcome / Day-9 ship / Day-12 founders'-open / Day-13 ship / Day-14 gate push / optional gate-miss email) + Day-14 fallback distribution assets (Polymarket Discord intro + r/PredictionMarkets self-post + podcast-pitch template) = 3. **LLM-side P1-P4 queue exhausted plus operator-handoff + email + fallback-distribution supporting tier complete; remaining 14-day execution is operator hands-on Substack/Stripe/Twitter/static-site-host.**

- **K45 ingest COMPLETE 2026-05-14** (late night, ≈11:30pm): 3 sources from `research to be indexed/` — **TiDAR** (NVIDIA 2511.08923, hybrid diffusion-autoregressive LLM decoding with free-token-slot parallel drafting, 4.71-5.91× throughput) / **Counterfactual Prompting Baselines** (2605.01048, Northeastern/Bar-Ilan/Allen AI — paraphrase-null distributions required for valid LLM counterfactual studies; 14.9% gender-swap flip rate = 14.1% paraphrase baseline) / **Multi-Wiki Tool Evaluation v3** (26-tool batch audit across all 6 Cemini wikis — 6 Adopt + 7 Steal-from + 3 Reference + 6 Reject + 4 UNAVAILABLE). **2 new concept pages**: `tidar-hybrid-diffusion-ar.md` (free-token-slot architecture + context-economics relevance) + `counterfactual-prompting-baselines.md` (paraphrase-null framework, upgrades `[CONFIRMED]` claim-discipline — paraphrase baseline now a requirement before confirming LLM-behavior claims). **13 new tool entity stubs** from multi-wiki eval: 6 Adopt (visual-explainer / deepeval / voicebox / openusage / apktool-mcp-server / OmniVoice) + 7 Steal-from (tpotce GPL-3.0 poison pill / MyIP / claude_code_agent_farm / Decepticon / Fusion / Open-Generative-AI / tracer — highest-ROI extraction). **1 existing page updated**: codegraph.md (K45 v3 reconfirmation backlink). **License poison pills caught (5)**: tpotce GPL-3.0, minimalfirewall AGPL-3.0, Stable-Diffusion GPL-3.0, red-run GPL-3.0, iii ELv2. **12 of 13 tools have non-OSINT primary fits** (ccc-wiki 4 / cybersec 3 / image-gen 3 / Cemini financial 1 / OSINT 2) — cross-wiki stubs deferred to user direction. **2 bidirectional gaps fixed** (multi-wiki-tool-evaluation-v3 expanded to list all 13 tools; counterfactual-prompting-baselines ↔ deepeval). wiki_lint: 0 K45-specific issues. All 3 raw sources SCPed to librarian; laptop inbox clean. 21 files committed + pushed (18 new + 3 modified) as 74a06b2.

### K45 follow-ups (queue)

| Item | Action | Status |
|------|--------|--------|
| **Operational adoption briefs from multi-wiki tool eval** | Per user directive: create separate operational briefs for actionable Adopt + Steal-from tools. Source page documents tiers; briefs are the executable adoption deliverables. | **PENDING** |
| **Cross-wiki stubs/briefs for 12 non-OSINT tools** | ccc-wiki: visual-explainer, openusage, claude_code_agent_farm, Fusion. cybersec: apktool-mcp-server, tpotce, Decepticon. image-gen: voicebox, OmniVoice, Open-Generative-AI. Cemini financial: tracer. Create stubs or briefs in secondary wikis per `cross_wiki_route.py`. | **PENDING** — deferred to user direction |
| **TiDAR follow-up** | Track NVIDIA repo release; evaluate context-economics implications for Cemini's LLM stack when implementation available. | **TRACKING** |
| **Counterfactual prompting — upgrade claim-discipline** | `[CONFIRMED]` tag now requires paraphrase-baseline-controlled counterfactuals per concept page. Update CLAUDE.md citation discipline if user approves. | **PENDING** |

- **K44 ingest COMPLETE 2026-05-14** (morning): Gemini Deep Research v3 multi-wiki tool eval ("Tool Evaluation for Cemini Wiki Integration.docx", 28 URLs). Verdict rollup: **7 Adopt + 7 Steal-from + 1 Defer + 3 Reference + 3 Reject + 7 UNAVAILABLE**. **New largest cross-wiki routing event** — supersedes K43; all 6 sibling wikis touched with 14 actionable items spanning 4 destination wikis. **1 source + 1 concept + 7 OSINT entity stubs + 17 cross-wiki entries** committed across 5 git repos. **Key formalization**: `@concepts/multi-wiki-eval-doc-level-vs-phase-0.md` codifies the K43 two-gate lesson (doc-level eval is necessary but not sufficient — Phase-0 source audit required for all Adopt/Steal-from verdicts before promotion to `validated`). **Highest-priority Adopt items**: `betterleaks.md` (deep page, cybersec — pre-IP-sale codebase audit critical; CEL filtering + BPE tokenization for false-positive reduction) + `aulekator-polymarket-btc-bot.md` (NautilusTrader 15-min BTC, direct K43 Polymarket-integration follow-up). **Cross-wiki convergence finding**: `geo-seo-claude` already adopted by seo-wiki 2026-05-07 (Phase-0 GO retained as authoritative); K44 independent reconfirmation elevates signal quality (two evals converged on same GO). **Star-inflation skepticism flagged**: jcode (6.1k★ solo) + geo-seo-claude (7.2k★ solo) — Phase-0 G1 (gh api star/fork ratio verification) required. **License posture clarifications**: czkawka dual-license isolation (czkawka_core MIT extractable, GUI GPL-3.0 poison via `cargo tree` verification) / red-run + cariddi GPL-3.0 patterns-only / ai-infra-guard Apache-2.0 with restrictive attribution clauses. All Adopt/Steal-from verdicts treated as `doc-level-pending-phase-0` maturity. wiki_lint: **0 K44 bidirectional gaps** (5 patched: polymarket-clob-api + polymarket-gamma-api + three-formula-system + bukosabino-ta + tradingview-mcp-atilaahmettaner + eval-github-repos-2026-05-13 + awesome-polymarket-tools). Raw source SCPed to librarian; laptop inbox clean.

### K44 follow-ups (queue) — ✅ ALL AUDITED (reconciled 2026-05-17)

The 14-tool Phase-0 audit queue was completed in the K44 campaign (2026-05-14); the verdicts were never marked back here, so a 2026-05-17 batch re-confirmed every entity page already carried a verdict. Resolved:

| Item | Verdict | Audited |
|------|---------|---------|
| betterleaks Phase-0 | audited (see entity page) | 2026-05-15 |
| aulekator-polymarket-btc-bot Phase-0 | **NO-GO** bot / **STEAL-FROM** adapter — no LICENSE file; G3 adapter uses blessed py-clob-client+Gamma path | 2026-05-14 |
| alumnium Phase-0 | **GO** — MIT, healthy multi-contributor; real MCP stdio contract | 2026-05-14 |
| optillm Phase-0 | **GO** (IP-sale caveats) — Apache-2.0; Z3 integration confirmed real | 2026-05-14 |
| adamsreview Phase-0 | **CONDITIONAL-GO** — divergent from K37 reviewer-agent spec, do NOT rebase | 2026-05-14 |
| gtm-agents Phase-0 | **SKIP** — supplement-only vs `marketingskills.md` | 2026-05-14 |
| supavec Phase-0 | **STEAL-FROM-GO** — Apache-2.0; PLpgSQL match_documents portable, ~18-28h port | 2026-05-14 |
| LAP Phase-0 | **STEAL-FROM-CONDITIONAL** — K44 OpenAPI→MCP use case invalid (compiles to `@lap` grammar, not MCP) | 2026-05-14 |
| thuki Phase-0 | **SKIP** — mis-described in queue; Tauri Ollama-overlay app, no extraction target | 2026-05-14 |
| jcode Phase-0 | **STEAL-FROM-CONDITIONAL** — MIT; 6.1k★ verified **organic**, not inflated; it's a Claude Code competitor | 2026-05-14 |
| ai-infra-guard Phase-0 | **CONDITIONAL-GO** — external Docker only; Apache-2.0 NOTICE has mandatory-attribution poison if embedded | 2026-05-14 |
| cariddi Phase-0 | **STEAL-FROM-PATTERNS-ONLY** — GPL-3.0; clean-room re-impl only | 2026-05-14 |
| czkawka Phase-0 | **STEAL-FROM-CONDITIONAL** — Python clean-room port (Rust core drags LGPL/MPL transitively) | 2026-05-14 |
| red-run Phase-0 | **REFERENCE-ONLY** — GPL-3.0; architectural patterns only | 2026-05-14 |
| gym-anything (Defer) | CMU-L3 MIT 211★ — low maturity | **TRACKING** — re-evaluate quarterly |
| geo-seo-claude reconfirmation | seo-wiki 2026-05-07 Phase-0 GO authoritative | **CLOSED 2026-05-14** |
| Awesome-Polymarket-Tools (CC0) | Reference-only discovery layer | **TRACKING** |

## Current state (end of 2026-05-13)

- **K41 ingest COMPLETE 2026-05-13**: 11 sources / 5 concepts / 13 entity stubs ingested + cross-wiki routing checked (image-gen / seo / 3d-printing / cybersecurity all clear — sources OSINT-domain only). **Foundational agent papers landed**: Toolformer (2302.04761 Meta) + ReAct (2210.03629 Princeton+Google ICLR 2023) + Generative Agents (2304.03442 Stanford UIST 2023) + LLMs-Get-Lost (2505.06120 MS+Salesforce). LLMs-Get-Lost is the **third orthogonal data-level failure mode** completing the preference-data taxonomy (typicality K39 + asymmetric-penalty K40 + premature-commitment K41 — all training-free mitigations exist). **Massif Capital corpus introduction**: 4Q2025 Letter to Investors (15.6% net annualized since inception, 28 quarters) + 5 new concept pages (wicked-problems-capital-allocation, capital-cycle-theory, real-assets-investing-framework, critical-minerals-thesis, plus claude-md-12-rule-template). **Weekly Wizdom newsletter ingested** (Issues #173 Apr 7 / #175 Apr 22 / #176 Apr 29 FOMC) + Donny watchlist Apr 23 — **5+ exact ticker matches Apr 22-23 confirm Donny watchlist derives from WW recommendations** (treat as same-source for confirmation purposes). **Polymarket weather-trading strategy synthesized** from @AlterEgo_eth + @theparuchh sources: Gamma API two-endpoint pattern + 5 compounding edges (station-coordinate fix + Open-Meteo `bias_correction=true` + 3-model ICON+GFS+ECMWF ensemble + 3-bin coverage + 18-30hr entry window); reviewer-agent validation use case identified. **CLAUDE.md 12-rule template lineage** (Karpathy → Forrest Chang → Mnilax) documented with 41% → 3% claim flagged NEEDS VERIFICATION 2026-05-13. wiki_lint: **0 bidirectional gaps / 0 dangling related / 0 missing body mentions**. 11 raw sources SCPed to librarian with canonical filenames. Pre-K41 wiki structural cleanup (376 bidirectional gaps + 20 pre-K40 issues → 0) closed 2026-05-13 morning.

### K41 follow-ups (queue)

| Item | Action | Status |
|------|--------|--------|
| **Polymarket weather-trading Phase-0 audit** | Verdict CONDITIONAL-GO; Open-Meteo `bias_correction=true` **FALSIFIED** via API docs (Seasonal Forecast API explicit: "currently provided without bias adjustment"); structural edges (station-coord fix, 3-model ensemble) sound; @theparuchh V3 ROI treated as anecdotal; 3 Hard NOs; Phase 1 paper-trade pilot proposed. | **SHIPPED 2026-05-13** to `cemini-prod:/opt/cemini/briefs/2026-05-13_polymarket-weather-trading-phase-0-audit.md`; skill_audit PASS 100/100; awaits server-Claude execution |
| **Real-assets supply-deficit synthesis brief** | Filtered Donny as derived-from-WW (effective 2 independent sources: Massif + WW/Donny composite). Multi-source confirmed: lithium / REE / O&G. Single-source novel: solar (FSLR/ARRY/SHLS) / uranium / AI infra. Primary-only: gold (EQX) / copper. Cross-source disagreements flagged on USAR Serra Verde + 2026 oil timing. | **SHIPPED locally 2026-05-13** at `briefs/2026-05-13_real-assets-supply-deficit-synthesis.md`; ready for user-copy to claude.ai |
| **LLMs-Get-Lost mitigation audit** | Cemini stack coverage map against Laban et al.'s three failure modes (premature commitment / answer bloat / lost-middle). Conductor + reviewer-agent + claude-mem = 6.5/9 coverage; intra-session lost-middle is residual gap; no new arch work warranted yet. | **SHIPPED 2026-05-13** as `@concepts/llms-get-lost-mitigation-audit.md` (local concept page, informational); commit e949d40 |
| **CLAUDE.md cut-diff proposal** | 12 cuts totaling ~113 lines proposed; 4-phase application order (A: low-risk 49 lines / A+B+C+D: hits ~200). 8 in-place compressions + 4 content relocations to LESSONS.md / new concept pages. No load-bearing rule removed. | **SHIPPED locally 2026-05-13** at `briefs/2026-05-13_claude-md-cut-diff-proposal.md`; awaits user review before any edits land |
| **Capex tracker brief candidate** | Pull public capex data for 5-7 sectors Massif covers (IEA + EIA + Wood Mackenzie + S&P + company disclosures) to independently audit capital-cycle thesis against underlying data. Surfaced as next workstream in real-assets brief §6. | **PENDING** — awaits user green-light |
| **Forrest Chang repo stats verification** | The tagged claim was the "120k stars by May 2026" figure in `forrest-chang.md` + `claude-md-12-rule-template.md` (the 41%→3% mistake-rate table is Mnilax's, already caveated as author-asserted — not under a NEEDS VERIFICATION tag). | **DONE 2026-05-15** — star claim [CONFIRMED] via live GitHub API (~130,900 stars) + trade-press coverage; repo = `forrestchang/andrej-karpathy-skills`. forrest-chang.md `maturity → validated`. |
| **Future Massif letters** | 28-quarter track record implies ~7-year letter series. Tracking-source candidate; ingest as future letters appear. | **TRACKING** |
| **`@concepts/phase-0-audit-pattern.md` extraction** | New concept page proposed in CLAUDE.md cut-diff §3 cut 9; would house the Phase-0 audit doctrine currently inline in CLAUDE.md lines 237-251. | **PENDING** — depends on CLAUDE.md cut-diff acceptance |

- **K42 ingest COMPLETE 2026-05-13** (afternoon): 3 Gemini DR link-evaluation docx files ingested as a single batch (Doc 1 `evaluating-urls-cemini-project` 33 URLs / Doc 2 `multi-wiki-link-eval-prompt` 37 URLs / Doc 3 `tool-evaluation-wiki-fit` 34 URLs = 104 total URL evaluations). **29 new entity stubs + 2 new concept pages**: `@concepts/paradigm-vs-license-inverse-correlation.md` (license-as-moat thesis across K40+K41+K42, ~110 URLs evidence) + `@concepts/threat-intel-saas-cluster.md` (9-platform batch-Reject Shodan/FullHunt/ONYPHE/SOCRadar/Pulsedive/IntelX/Hunter/PublicWWW/Coalitioninc — cybersec routing). **4 existing-page updates** (pageindex / claude-mem / gitnexus / idassist with K42 cross-refs). **2 cross-wiki briefs shipped**: `@cybersecurity-wiki/briefs/2026-05-13_k42-cybersec-routing.md` (15 items in 3 tables) + `@seo-wiki/briefs/2026-05-13_k42-seo-routing.md` (open-seo + marketingskills + n8n-workflows). Tier headlines: **PraisonAI** (Doom-Loop Detection + Shadow Git Checkpoints, MIT) Adopt-candidate for Conductor replacement; **Mirage** (unified VFS Apache-2.0) Steal-from; **OpenSpec** (47.6k stars, SDD discipline) Adopt; **n8n-workflows** (4,343 production scripts, MIT) Adopt; **tabularis** (MCP-native PG/SQLite client, Apache-2.0) Adopt; **syncthing** (file sync, MPL-2.0) Adopt. License-pattern: **inverse-correlation confirmed** — most architecturally novel tools cluster in poison-licensed repos (GitNexus PolyForm / Frona BSL / OpenHuman GPL-3.0 / Markra AGPL); permissive licenses correlate with conventional scope. wiki_lint: **0 bidirectional gaps / 0 dangling related / 0 missing body mentions**. 3 raw docx SCPed to librarian as `k42-*.docx`.

### K42 follow-ups (queue)

| Item | Action | Status |
|------|--------|--------|
| **PraisonAI Phase-0 audit** | Verify Doom-Loop Detection + Shadow Git Checkpoints implementation; benchmark against current LangGraph Conductor; license MIT confirms clean adoption surface; potential full LangGraph replacement candidate. | **CONDITIONAL-GO 2026-05-13** — Doom-Loop Detection real (heuristic state-graph, no LLM); Shadow Git orthogonal-skip. Brief SHIPPED to `cemini-prod:/opt/cemini/briefs/2026-05-13_praisonai-phase-0-adoption.md`. Solo-maintainer 90.7% (Top-1 risk). 1-week cycle-detector port spike pending. |
| **Mirage Phase-0 audit** | Verify unified VFS POSIX-mount mechanics across MongoDB/Redis/S3/GDrive backends; Apache-2.0 + Steal-from tier; potential `/opt/cemini` data-substrate simplification. | **STEAL-FROM-CONFIRMED 2026-05-13** — Apache-2.0; `BaseResource` + `Accessor` + `@op` registry pattern portable; experimental MongoDB/GDrive/Gmail backends skipped. Methodology brief SHIPPED to `cemini-prod:/opt/cemini/briefs/2026-05-13_mirage-methodology-steal-from.md`. 1-week Polymarket-adapter spike pending. |
| **OpenSpec adoption** | Spec-Driven Development methodology for deterministic Python module generation in `/opt/cemini`; install + integrate proposal.md/specs/design.md artifact pattern; tuned for Opus 4.5/GPT 5.2. | **Phase-2 SPRINTS 1-4 LANDED + SPRINT 5 DEFERRED + PILOT MEASUREMENT COMPLETE 2026-05-13** — Phase-1 PASS both tiers (Opus + Sonnet, validate first try). Canonical bundle: **Opus** (safer missing-confidence-escalates; K37-aligned). **Sprints 1-4** (105/105 tests pass, end-to-end smoke verified): `trigger_policy.py` classifier + `policy_loader.py` + `policy.yaml` + `cost_telemetry.py` + `cost_aggregator.py` + `harmfulness_audit.py` + 105 unit tests. **Sprint 5 (rollout) DEFERRED** — read-only SSH probe of `/opt/cemini/conductor/` (commit f37749f follow-up) revealed production `ToolOrchestrator` dispatches only `kb_search` + `stash_recall`, both read-only. None of the 8 Polymarket tools the spec enumerates (`place_order`, `withdraw`, etc.) exist in production yet. Deploying middleware that gates nothing would be dead infrastructure + confidence trap. K37 code stays at `conductor/reviewer/` as pilot deliverable; OpenSpec change marked `DEFERRED` with re-open trigger documented in `openspec/changes/reviewer-agent-selective-trigger/DEFERRED.md`; tasks 5.1-5.5 explicitly marked deferred with reason. **OpenSpec pilot measurement objective is COMPLETE** — Opus 4.7 vs Sonnet 4.6 comparative pass; both first-try-validated; methodology gap captured in `LESSONS.md` 2026-05-13 (specs need a `## Production reality check` grounding step before runtime-wiring tasks). Re-opens when Polymarket integration brief lands. |
| **n8n-workflows AI-BOM scanner extraction** | 4,343 production scripts MIT-licensed; Trusera scanner detects hardcoded API keys + MCP exposure + RCE risk in Code Execution → HTTP Request node chains. Extract as cybersec methodology to `@cybersecurity-wiki/concepts/ai-bom-scanner.md`. | **CONDITIONAL-GO 2026-05-13** — 54.4k stars (not 4,343 — that was script count); AI-BOM scanner external at `Trusera/ai-bom`. 3 of 5 heuristics portable. Brief SHIPPED to `cemini-prod:/opt/cemini/briefs/2026-05-13_n8n-workflows-ai-bom-scanner.md`. 3-5 day port to `/opt/cemini/scripts/ai_bom_scan.py` pending. |
| **tabularis MCP-PG integration** | MCP-native PostgreSQL/SQLite client (Apache-2.0, Rust/Tauri v2) for AI-assisted SQL on `/opt/cemini` PG instances; replace ad-hoc psql workflows. | **CONDITIONAL-GO 2026-05-13** — Apache-2.0 v0.10.3; STDIO JSON-RPC 2.0 MCP server verified; destructive-query gating verified. Brief SHIPPED to `cemini-prod:/opt/cemini/briefs/2026-05-13_tabularis-mcp-adoption.md`. 3-5 day deployment (read-only mode, audit-schema only) pending. |
| **syncthing laptop↔analyst-machine state replication** | MPL-2.0 v2.1.0 file sync for Claude Code state + MCP server artifacts across analyst machines; potential laptop↔librarian backup channel. | **Phase-1 LAPTOP DONE / SERVER BRIEF STAGED 2026-05-13** — Laptop: v2.1.0 binary at `~/.local/bin/syncthing` (direct GitHub install), daemon running, device ID `V6EKWDC-…-RKI3QA7`, `.stignore` authored in `research to be indexed/`. Server-side install + folder-pair brief staged at `briefs/2026-05-13_syncthing-hetzner-install.md` (skill_audit PASS 100/100) — execute via server-Claude session or user-direct per CLAUDE.md scope discipline (this workspace cannot SSH `apt install`). Folder pair Option B locked: `research to be indexed/` ↔ `/opt/cemini-bulk/research/drafts/`. Scoping note: `briefs/2026-05-13_syncthing-poc-launch-scope.md`. |
| **agent-skills Phase-0 audit** | Doc 1 K42 Adopt; structural skills framework — Phase-0 against `agent-skills-eval` framework to confirm wiki-fit before integration. | **Phase-1 COMPLETE 2026-05-13** — SKILL.md frontmatter applied to `~/.claude/skills/tech-debt-audit.md` (license + metadata.author + metadata.version); Cemini spec stance pinned in `LESSONS.md` 2026-05-13 entry. Compliance template: `briefs/2026-05-13_skillmd-compliance-tech-debt-audit.md`. `scripts/skill_audit.py --mode skillmd` extension DEFERRED. |
| **claude-obsidian parallel-impl audit** | K42 raised as parallel implementation surface alongside claude-mem; clarify scope distinction (session vs vault reasoning layer) before any port. | **DO NOT ADOPT 2026-05-13** — SessionStart hook collision with claude-mem v13.0.1 confirmed; `[!contradiction]` vs `[NEEDS VERIFICATION]` 200+ file migration cost; Obsidian-Desktop lock-in. Dead Ends entry recorded at `@entities/tools/claude-obsidian.md`. No brief. |
| **FuzzyAI extraction (cybersec)** | PAIR + Crescendo adversarial-prompt taxonomy; cross-wiki route handled (`@cybersecurity-wiki/briefs/2026-05-13_k42-cybersec-routing.md`); follow-up: enrich `@concepts/verbalized-sampling-llm-diversity.md` with adversarial diversity vector. | **GO cybersec Phase-0 2026-05-13** — Apache-2.0; CyberArk Labs backing; PAIR + Crescendo + 16 other attacks; NO defensive-detection library (separate workstream needed). Cybersec brief at `@cybersecurity-wiki/briefs/2026-05-13_fuzzyai-adoption.md`. OSINT Vector 5 snippet pending. |
| **cua / pentest-ai-agents extraction (cybersec)** | Autonomous pentest agents (Doc 1 K42); cross-wiki routing brief includes; consider as reviewer-agent test corpus once Phase-0 audit lands. | **GO cybersec Phase-0 2026-05-13** — cua MIT 16,381 stars (Lume Apple-Virtualization); pentest-ai-agents MIT 1,100+ stars (wraps 80+ pentest tools, solo 0xSteph). Separate briefs at `@cybersecurity-wiki/briefs/2026-05-13_cua-adoption.md` + `@cybersecurity-wiki/briefs/2026-05-13_pentest-ai-agents-adoption.md`. |
| **whale Phase-0 audit** | Cybersec-primary entity; defer to cybersec-wiki Phase-0 lead. | **Phase-0 COMPLETE 2026-05-13 — NO BRIEF** — MIT verified (not cybersec, actually OSINT-workflow); direct DeepSeek API bypass breaks Cemini OpenRouter routing; 6-day-old project. Reference architecture only; not an integration vector. |
| **PYDNS-Scanner extraction (cybersec)** | Async DNS recon TUI (MIT, Python); cybersec-wiki primary; minimal cross-route value to OSINT/Cemini. | **CONDITIONAL-GO cybersec Phase-0 2026-05-13** — MIT 337 stars; **DNS server discovery (NOT subdomain enum)**; README has zero ethical-use guidance. Cybersec brief at `@cybersecurity-wiki/briefs/2026-05-13_pydns-scanner-adoption.md` with mandatory ethical-use addendum requirement. |
| **Threat-intel SaaS cluster — paid-tier evaluation** | 9-platform batch-Reject documented in `@concepts/threat-intel-saas-cluster.md`. Re-evaluate iff Cemini ever justifies paid threat-intel surface; out-of-scope for IP-sale-readiness. | **DEFERRED** |
| **PageIndex contradiction reconciliation** | K42 Doc 1 Adopt (long-form filings) vs 2026-05-05 NO-GO (wiki layer). Documented in `@entities/tools/pageindex.md` Dead Ends; no real conflict — different use cases. | **CLOSED** 2026-05-13 |

- **K43 ingest COMPLETE 2026-05-13** (evening): 5 sources across 3 distinct content domains — **Polymarket-tradecraft** (@AlterEgo_eth Gamma/CLOB API two-step flow + @de1lymoon three-formula synthesis Poisson/Shannon/Taleb) / **Cemini Phase-0 audit** (14-repo GitHub eval, 5 Adopt + 1 Steal-from + 1 Defer + 3 Reference + 4 Reject) / **K41 follow-on** (Weekly Wizdom #178 May 13 macro+positions + NL paper Behrouz et al. NeurIPS 2025). **7 new concept pages** synthesize the @de1lymoon quant trio: `poisson-edge-rare-events.md` + `shannon-entropy-kl-divergence-prediction-markets.md` + `taleb-fat-tails-barbell-prediction-markets.md` + `kelly-sizing-quarter.md` (universal sizing primitive) + `insider-detection-entropy-collapse.md` (defensive sub-signal, [TENTATIVE]) + `three-formula-system-polymarket-rare-events.md` (40/35/25 synthesis with `complete_rare_event_system()` reference impl) + `nested-learning.md` (osint stub → ccc-wiki primary). **13 new entity pages**: 2 Polymarket API entities (`polymarket-gamma-api.md` discovery layer + `polymarket-clob-api.md` execution layer) + 4 Adopt/Reference tools (bukosabino-ta, tradingview-mcp-atilaahmettaner, awesome-ai-agents-2026-zijian, awesome-systematic-trading-paperswithbacktest) + 7 new tickers (NNE, LIF, LAR, ZEC, NEAR, HYPE, HOME). **5 ticker pages updated** (ELVR + REA + BTC + SOL + Polymarket platform). **8 cross-wiki routes** — **largest cross-wiki routing event so far**, touching all 6 sibling wikis: ccc-wiki (3: NL primary + tolaria/multi-codex briefs) / cybersec (3: PYDNS-Scanner + pentest-ai-agents stubs + chekusu/mails brief) / image-gen (1: gracia.ai volumetric video) / 3d-printing (1: gracia.ai 3D mesh export sibling). **License posture observations**: 5 of 5 ADOPTs are MIT (continues IP-sale-readiness preference); AGPL-3.0 (tolaria) STEAL-FROM patterns only; PolyForm-Noncommercial + no-license repos auto-REJECT. **Same-source confirmation flag**: ELVR / LAR / REA appear on both Donny watchlist + WW newsletter — flagged as same originator, not independent confirmation. wiki_lint: K43-specific bidirectional gaps reduced to minor pre-existing wiki patterns. 5 raw sources SCPed to librarian; inbox now clean.

### K43 follow-ups (queue)

| Item | Action | Status |
|------|--------|--------|
| **Polymarket Gamma + CLOB integration** | Two-step flow (Gamma `events?slug=` → `clobTokenIds[0]=YES` → CLOB `POST /order`) now formalized as entity pages. Integration brief drafted at `briefs/2026-05-13_polymarket-gamma-clob-integration.md` (skill_audit 91/100 WARN — verdict GO incremental, ~2-3 day estimate, 7 risks documented, 7 operational gates). | **SHIPPED 2026-05-13** to `cemini-prod:/opt/cemini/briefs/2026-05-13_polymarket-gamma-clob-integration.md`; awaits server-Claude execution |
| **Three-formula synthesis backtest** | Cemini-side validation of `complete_rare_event_system()` 40/35/25 weighting on historical Polymarket rare-event markets. Verifies @de1lymoon's claimed mispricing on 5¢/1¢ contracts. | **PENDING** — pairs with hftbacktest infrastructure (K31 adopt) |
| **bukosabino/ta Phase-0 audit** | Phase-0 source audit caught **parallel-implementation conflict** with already-adopted `pandas-ta-classic` (identical 43-indicator set, identical API shape, zero novel coverage) PLUS stale-deps blocker (`pandas==1.3.5` + `numpy==1.21.5` EOL; fails on Python 3.12 and pandas 2.x). K43 source-doc ADOPT verdict was MIT-license + indicator-coverage filter only; Phase-0 caught the duplicate. | **NO-GO 2026-05-13** — entity page `@entities/tools/bukosabino-ta.md` updated with Phase-0 verdict table + Dead Ends entry; **no adoption brief** generated. `pandas-ta-classic` retained as canonical TA library. |
| **tradingview-mcp Phase-0 audit** | Phase-0 source audit confirmed **MIT license + 30 tools verified + active maintenance (commit 4h ago)** but caught **TradingView TOS redistribution as blocking gate** — `tradingview-screener` + `tradingview-ta` library licenses unaudited; commercial MCP-wrapper redistribution under TradingView ToU unknown. Existing prod brief `briefs/2026-05-10_tradingview-mcp-adoption.md` (GO-conditional) is now gated by this verdict. | **NO-GO pending TOS legal review 2026-05-13** — entity page `@entities/tools/tradingview-mcp-atilaahmettaner.md` updated with full Phase-0 audit + 6 gates to clear before reconsidering; **no new adoption brief** generated. |
| **Insider-detection 3σ backtest** | Single-source TENTATIVE heuristic from @de1lymoon. Backtest against historical Polymarket order books on known insider-trading cases (Trump-Macron, etc.). Defensive-signal only — stays out, doesn't enter. | **PENDING** — requires historical orderbook data |
| **Weekly Wizdom #178 third-source verification** | ELVR / LAR / REA same-source flag (Donny + WW = same originator). Need independent third source before treating critical-minerals thesis as confirmed beyond Massif/WW composite. | **DONE 2026-05-15** — thesis [CONFIRMED] via 4 independent Tier-1 sources (IEA / ADL / TCW / Allens); `critical-minerals-thesis.md maturity → validated`. Per-name in `ww-issue-178`: LAR EBITDA [CONFIRMED], ELVR placement [CONFIRMED], ELVR "A$150M convert" [RETRACTED], ELVR price-lifecycle [NEEDS VERIFICATION 2026-05-15]. REA Shiloh resource still unverified — did not surface in independent search. |
| **gracia.ai watch-list** | REFERENCE-ONLY both wikis. Watch for splat-to-mesh tooling maturity (NeRF2Mesh, splat2mesh, SuGaR). If a mature pipeline emerges, re-audit gracia.ai (or competitor) as a capture tool for 3D printing or as novel-view-synthesis for image-gen. | **TRACKING** |
| **`@briefs/2026-05-13_github-eval-cross-wiki-routes.md` brief** | Stage a distribution brief for the 14-repo audit + cross-wiki routes; currently the lint-flagged dangling related: was removed pending the brief being staged. Brief candidates: integration-priority ranking of the 5 ADOPTs + cross-wiki coordination summary. | **PENDING** — brief staging step |
| **Eval-github body @path cleanup** | `cross_wiki_route.py` auto-injected backlink lines at top of `eval-github-repos-2026-05-13.md` with wrong path prefix (`@target-wiki/concepts/...` while actual brief paths are `@target-wiki/briefs/...`). Cosmetic cleanup; not functionally broken. | **PENDING** — low-priority |
| **Brief filename double-dating** | `cross_wiki_route.py` creates briefs as `2026-05-13_<my-slug>.md` where my-slug already started with date, producing `2026-05-13_2026-05-13_*.md`. Affects all 5 K43 cross-route briefs consistently. Either fix script or accept convention. | **PENDING** — script-side cleanup |
| **NL paper deep-read on ccc-wiki side** | ccc-wiki nested-learning.md is stub; deep-read by ccc-wiki sessions when memory-architecture work resumes. OSINT-side reference is sufficient for current Cemini use. | **TRACKING** ccc-wiki |
| **`@concepts/three-formula-system-polymarket-rare-events.md` operational gate** | Synthesis concept identifies Cemini entry point under quarter-Kelly. Pairs with `@concepts/polymarket-bot-architecture.md` for execution layer. First-pilot candidate when Polymarket integration brief lands. | **PENDING** — depends on K30 Polymarket integration completion |

## Current state (end of 2026-05-12)

- **K40 cross-wiki ingest COMPLETE 2026-05-12**: 6 new sources + multi-wiki Gemini eval prompt v2 deliverable. Cross-wiki batches shipped to cybersec (17 tools + 1 concept), image-gen (4), SEO (5). 37 new OSINT entity stubs + 4 new OSINT concepts. **User-flagged v1 prompt limitation corrected**: v2 prompt routes URLs through 7-surface fit grid (Cemini financial / OSINT / Cybersec / Image-gen / SEO / 3D-printing / Workflow); ready for next eval batch. **NPM supply-chain defense brief staged to `cemini-prod:/opt/cemini/briefs/2026-05-12_npm-supply-chain-defense.md`** per user request; workspace `package.json` confirmed pinned to exact versions. Tier headlines from K40: **AutoTS** + **voicemode** + **hunk** + **veloxdb** + **anthropic-harness-design** Adopt (Phase-0 pending). **Anthropic Planner/Generator/Evaluator trinity adopted as CEMINI orchestrator architecture** (replaces ad-hoc LangGraph routing). New license-pattern catches: 3× no-LICENSE (Karma + multi-model-redteam + Claude-Code-Projects-Index) → mode #1 count climbing; CC-BY-NC-4.0 IP-sale poison pill (pastebar-app rejected); CC-BY-SA-4.0 added to catalog (claude-code-ultimate-guide acceptable for study-only). **New concept pages**: `ralph-autonomous-agent-pattern.md`, `polymarket-bot-architecture.md`, `agent-cost-routing-orchestra.md`, `npm-supply-chain-defense.md`, plus cybersec wiki `llm-vulnerability-discovery.md`.

### K40 follow-ups (HIGH PRIORITY queue)

| Item | Action | Status |
|------|--------|--------|
| **AutoTS Phase-0 audit** | Phase-0 source audit before FastMCP integration: license, GPU/MAPPO compat, dependency footprint vs Cemini's small Hetzner box | **DONE 2026-05-17 — CONDITIONAL-GO** — MIT confirmed; light 4-package core, real first-class MCP server; install via the `[mcp]` extra only (excludes TensorFlow). Not an RL framework (no MAPPO). |
| **voicemode laptop install** | Local Whisper.cpp + Kokoro voice I/O for Claude Code workflow | **DONE 2026-05-17 — GO** Phase-0 — MIT; bus-factor ~1 but tolerable (non-serving laptop tool, MIT fork escape hatch). Install pending user direction. |
| **hunk laptop install** | Offline diff/patch UI; reduces LLM context bloat | **DONE 2026-05-17 — GO** Phase-0 — MIT, 24 contributors, healthy; pre-1.0 beta, pin a known-good version. Install pending user direction. |
| **veloxdb laptop install** | Rust embedded KV for ingest pipeline caches | **DONE 2026-05-17 — CONDITIONAL-GO** Phase-0 — MIT; 667-crate SBOM clean (9 MPL-2.0 weak-copyleft only, no GPL); young repo + single-dev — validate before load-bearing use. |
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
| **HL funding Dune backtest** (`hl-funding-sniper` quick pipeline) — last **2026-05-27**, next due **2026-08-27** — track: `wiki/meta/hl-funding-backtest-cadence.md` | Quarterly; agent prompts when due; user-gated run (~10–15 min + Dune credits) |

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

## Done — 2026-05-30 World Cup Bot build + prod monitor deploy

- **OSS repo** — [cemini23/world-cup-bot](https://github.com/cemini23/world-cup-bot): modules 1–7, liquidity gate, go-live safety, alerts, rewards sync (split systemd unit), shadow-status with ledger path; `17708e1`; 128 tests; `deploy/systemd/` monitor + trading profiles.
- **Prod** — monitor profile on `cemini-prod` via `2026-05-29_wc-monitor-systemd-enable.md` (executed by server-Claude); unit refresh pending for K84 automation wave.
- **Wiki** — `entities/tools/world-cup-bot.md` validated; index + log updated.

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
