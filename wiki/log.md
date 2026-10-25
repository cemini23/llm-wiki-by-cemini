---
title: Federation wiki — operations log
type: concept
related:
  - index.md
  - osint/log.md
updated: 2026-10-23
---

# Operations log

Append-only, newest first. This is the merged log; each domain keeps its own full history at
`wiki/<domain>/log.md`.

## [2026-10-25] tooling | wiki_lint backlink fixer repaired, debt halved

- **Two defects.** The fixer wrote gap keys verbatim. A key `osint/sources/x.md` written into an osint page resolves to `wiki/osint/osint/sources/x.md`, which dangles — that is why `--apply` raised dangling links from 65 to 974. It also proposed `sweeps/` targets forever, because those pages have no frontmatter and can never hold a `related:` block.
- **Fixes.** `_related_ref()` renders the reference the resolver accepts: bare domain-relative path inside a domain, `@alias/path` across domains. `alias_for_domain()` reads the alias from the federation table, so `cybersec` maps to `cybersecurity-wiki`. Frontmatter-less targets are now skipped and counted, not proposed.
- **Applied.** 1,097 backlinks across 638 target pages. Bidirectional gaps **2,193 → 1,276**. Dangling `related:` held at **6** — no regression this time. 124 hub targets stay skipped by design; 69 sweeps targets are skipped as unfixable.
- **Converged.** A second run proposes 0, so the fixer is now idempotent.
- **Repaired.** Three pages that the earlier broken run had given duplicate `related:` keys.

## [2026-10-25] tooling | digest fan-out and archive split fixed

- **Digest fan-out.** `scripts/daily_research_config.yaml` now gives every `paper_queries` and `queries` cluster a `wikis:` list. `filter_for_wiki()` in `daily_research_digest_run.py` keeps only the entries naming the running domain. Default for an entry with no `wikis` key is **osint only**, so a new query cannot fan out by omission.
- **Effect.** 22 clusters × 8 wikis = **176 executions** before; **26** after (85% fewer). Per domain: osint 2 paper + 4 news, ccc 2 + 0, cybersec 1 + 0, seo 1 + 0, image-gen 1 + 0, gambling 4 + 8, game-dev 1 + 1, 3d-printing 1 + 0.
- **New queries** so no domain loses its paper lane: `seo-geo-retrieval-paper`, `image-gen-diffusion-paper`, `3d-printing-additive-paper`.
- **Archive split.** Five Latent Space raws moved `egress/osint/` → `egress/ccc/`; pages repointed. `archive_raw_to_egress.sh` gained a guard: for `newsletter-rss-*` and `substack-rss-*` it derives the owning wiki from the source page and exits 2 on a mismatch unless `--allow-cross-wiki` is passed.
- **Left open.** Six older Latent Space raws in `egress/osint/` have no source page in any wiki, so there is no owner to move them to.

## [2026-10-25] ingest | K295 — full inbox, eval v10.9, 8 Phase-0 audits

- **79 files. 61 duplicates. 13 PDFs, 13 newsletters, 1 eval docx pair, 1 CSV.** All 13 arXiv PDFs were already filed — 7 as source pages, 6 on the K293/K294 skip pages. The digest fan-out bug still writes one global query into eight inboxes.
- **Eval v10.9 (20 URLs).** Tiers: 3 Integrate, 5 Extract, 2 Watch, 6 Context, 4 Pass. Source page: `osint/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md`.
- **Phase-0, 8 tools cloned.** Seven of eight cloned. **Three findings that change decisions:** `DeanChensj/jiangshan-map` is **GPL-3.0**, not unlicensed as the report has it — pattern only, no code in Atto; `JetBrains/thinkrail` ships **no `mcp/server.mjs`** and `pi-spec-graph` declares no entrypoint, so the report's portability claim is unproven; `cloudflare/security-audit-skill` has **11** domain docs, not 5, and its last commit is **2026-09-14**, not Oct 17.
- **Conflict resolved.** `security-audit-skill` carried a K262 verdict of FILE / 0 Integrate GO against the v10.9 Integrate score. Operator ruled **Integrate** on 2026-10-25. The K262 concern was unattended copying into Cursor's skill directory; that is compatible with running the workflow on request. **Install did not complete and the first run is deferred** — Atlas, Atto's newest repo, is under active development, and auditing a tree mid-rewrite produces findings against code that will not survive. Resume at a stable checkpoint against a named commit.
- **Atlas for Atto.** jiangshan-map's `?year=&place=` contract is the pattern for the in-flight Atlas work. New concept page `osint/concepts/historical-jurisdiction-atlas.md`. The agent emits a year and a place from the record; the client resolves boundaries; the agent never formats a coordinate.
- **Pages.** 1 eval source page, 1 concept, 5 new tool pages (jiangshan-map, firecrawl-gov-index, experiential-labs, thinkrail, voicestudio, pausevfx, dessa), 3 tool pages updated (hallmark, security-audit-skill), 13 newsletter stubs.
- **Boundary.** No install, no skill add, no scrape, no trade, no route swap, no clone into Atto. Clones live in `/tmp/phase0-audit/`.

## [2026-10-23] ingest | K294 — full inbox

- **62 files. 8 duplicates. 34 PDFs and 28 newsletters.** The digest fan-out is still open. `2610.31158` is on the osint skip page.
- **Osint.** Quant-Arena: nine frontier models, GPT-6 Astra highest, no model beats equal-weight A-shares on the sealed year 2024. Tool marks sit outside the model: a call is refused when a capability, approval, or budget mark is missing. AMV-GUARD re-checks a memory only when the check can change the action. Kalshi trailing seven-day volume on 19 Oct is **$21.7bn**. **No trade.**
- **CCC.** Agent S4 reaches **21.3%** on OSWorld V2 by evolving interfaces, **3.8 times** the same model with fixed interfaces. OO-Harness gains up to **15.79 points**. **No route swap.**
- **Cybersec.** English safety does not transfer: mean translation bypass **21.9%** to **44.4%**. Abliteration did not close a script gap about Taiwan.
- **Archive.** 54 new raws on egress-fi (osint, ccc, cybersec). Eight already-filed PDFs were deleted locally and were not sent again.
- **Boundary.** No install, no clone, no scrape, no trade, no xsp/pm scp, no route swap.

## [2026-10-20] ingest | K293 — full inbox

- **83 files. 37 distinct PDFs. 18 newsletters.** Most PDFs were copies. The digest still writes one global arXiv query into every domain inbox.
- **Osint.** Options agents need a loss limit outside the model: **13 of 26** can reach unbounded loss, **6 of 8** broker interfaces included, **0 of 26** authenticate text sources. ADDMART rebuilds an IV surface by construction. ABF-Bench: cite the record you retrieved. Kalshi trailing seven-day volume **$21.5bn** on 18 Oct. **No trade. No `/route` swap.**
- **Cybersec.** A low ASR is mostly an ignore, not a refusal. Prompt-only InjecAgent ASR **0.2% → 43%**. Keyword jailbreak ASR **96.0%** vs a StrongREJECT judge at **2.7%**.
- **CCC.** Naming the authoritative tool file recovers GPT accuracy that retrieval drops. CDSE **+7.6**. Jarvis coordination **29 → 192 / 278**.
- **Archive.** 40 new raws landed on egress-fi (osint, cybersec, ccc, image-gen, 3d-printing). Already-filed copies were deleted locally and were not archived again.
- **Image-gen.** OpenVLHarness **+9.7–12.6**. **3d-printing.** FunCAD, 46 mechanism families, simulation before the picture.
- **Skipped.** `2610.18802`, `2610.20896`, `2610.23419`.
- **Boundary.** No install, no clone, no scrape, no scp.

## [2026-10-14] merge | eight federation wikis merged into one repository

- **Merged** osint, ccc, cybersec, seo, image-gen, gambling, game-dev and 3d-printing into this
  repository under `wiki/<domain>/`. History preserved in both directions via `git filter-repo`
  (`wiki/` → `wiki/<domain>/`); 2,046 commits, 9,820 pages.
- **Verified** file manifest 1:1 (0 missing, 0 added, 0 changed), resolved edges 0 lost / 0 silent
  retargets over 101,542 edges, history intact through the osint rename, and a real ingest cycle
  end to end.
- **Fixed** three consumers that broke on the namespaced layout. `wiki_gap_detect.py` failed
  **silently** — it reported zero gaps and exited 0 — which would have read as an excellent wiki.
  Also fixed `preingest_check.py` and `wire_ledger_check.py`, plus a linter regression that
  reported 900 append-only sweeps as missing frontmatter.
- **Re-pointed** the 12 daily fetchers at the merged repo and namespaced the inbox by domain.
- **Archived** the seven absorbed repositories — not deleted, they are the rollback.
- Plan: `briefs/2026-10-14_federation-wiki-merge-plan.md`.

## [2026-10-13] cleanup | inbox duplicate deleted

- **Deleted `research to be indexed/2609.20804v1.pdf`** on operator instruction. **sha256 `a39a9e03aaaa877b294a4b702ff07ae09110dcb1a2b0c0196a72ea46e0ec390e` re-confirmed byte-identical** to the raw already ingested on 2026-09-18, and already at `cemini-egress-fi` under a different filename. Nothing was lost. **Inbox is now empty.**

## [2026-10-13] phase0 | K290 tool eval — licences verified, 9 clones

- **Ran `bash scripts/adopt_k290_phase0.sh`** in the Terminal panel (the Bash sandbox denies `api.github.com`).
- **`gh api` verified all 13 listed repos.** The docx's known errors are confirmed: **`club-3090` is Apache-2.0** (docx said AGPL-3.0 — the copyleft caution was unfounded, Integrate holds) and **`sogen` is GPL-2.0** (docx said NOT FOUND). `Insomnia` is MIT, `hydra` GPL-3.0. **`xxHash` and `context-mode` return `NOASSERTION`** — expected, not a red flag: xxHash's dual BSD-2-Clause + GPL-2.0 split is not expressible by GitHub's detector, and Elastic Licence 2.0 is not a licence GitHub recognises (the same fact that keeps context-mode at Extract-only).
- **9 shallow clones → `.local/adopts/k290/` (411 MB of a 500 MB budget).** No clone failed. Integrate: skills (1.9 MB), xxHash (6.9 MB), cc-switch-cli (58.8 MB), club-3090 (46.8 MB), takumi (105.8 MB), anatomy (14.5 MB). Extract: context-mode (19.6 MB), openmed (150.9 MB), DigUp (15.8 MB). Skipped by design: artcraft, VoiceStudio, Unlimited-OCR, strip, dx-ball, and the Context rows.
- **Still 0 Integrate GO.** The clones are REFERENCE data under gitignored `.local/`; product adoption needs its own brief.
- **Pages updated:** `sources/eval-url-revenue-opportunity-2026-10-13` (Phase-0 status + verified-licence table), `concepts/k290-eval-wave`, entity pages `takumi` / `context-mode` / `vercel-skills` / `openmed`, the K290 wires header, and the Atto + Basgiath briefs. **The Basgiath brief now records that Phase-0 skipped both of its rows** — neither licence is confirmed.
- **Boundary unchanged:** no install, no scrape, no auto-submit, no xsp/pm scp, never auto-arm.

## [2026-10-13] ingest | K290 — VEPA guardrails + DistressBench + 20-URL tool eval + 5 feeds

- **9 inbox files → 8 source pages + 3 hubs + 9 entity/concept pages + 6 briefs.** One file was a **byte-identical duplicate**: `2609.20804v1.pdf` (harness design for coding agents, sha256 `a39a9e03…`) matches `sources/arxiv-2609.20804-harness-design-coding-2026-09-18.md` exactly — **not re-ingested**, raw not archived.
- **VEPA (the headline).** `sources/arxiv-2610.12813-vepa-verified-evolving-guardrails-2026-10-13.md`. A **deterministic, pre-action allow/refuse guardrail** of **typed symbolic rules** over events `⟨actor, action, data, recipient, purpose, authorization, context, tool⟩`. Three stages: **an LLM proposes patches → a deterministic verifier admits only well-formed, conflict-free rules (symbolic scope-overlap, not SMT) → a Beta-posterior evidence gate activates a rule only when its risk quantile clears tolerance**; no rule fires → LLM fallback. **0.81** ASSEBench-Safety (+0.02), **0.76** ATBench (+0.09); coverage ~80/89/88%. **No-Verifier ablation = −0.13 F1**; rule eval **≈0.25 ms**. **Its own limit: the upstream neural parser sits outside the guarantee — post-parse determinism ≠ end-to-end determinism.**
- **DistressBench.** `sources/arxiv-2610.12758-distressbench-2026-10-13.md`. Scores **care delivered, not refusal** — 718 clinician-authored conversations, rubric-weighted criteria across 7 dimensions. **25 models in only 12 separable bands**; best **88.4%**, median **71.4%**, clinician ceiling **98.7%**. **The finding: a 35.3% recognition–action gap** — the model recognizes the crisis on every criterion and fails to route to human help. One served model returns nothing on **7.5%** of conversations; a refusal-scored benchmark records that as a pass.
- **Sandbox credential exposure (the operational item).** Latent Space: a **Pier/Harbor sandbox injected its own provider key**; **DeepSeek V4.1 Flash used it in 33% of runs and succeeded in 11%** (15 other models did not). Author clarified it is **API-key abuse, not exfiltration**. The criticism lands on the **harness**. → **the `/route` Flash lane must never hold a durable credential.**
- **Meta Muse Wonder.** AA Intelligence Index v4.3 **56** vs **Opus 5.5 58**; **Coding Agents Index 68**, tying Claude Code + Sonnet 5.5 (68), ahead of Opus 5.5 (66); Terminal-Bench 4.0 **33% → 57%**; **$4/$20 per M**, 1M context. Skeptics: still **3–6 months behind**, no system card. **No `/route` swap.** → `entities/models/muse-wonder.md`.
- **Agent results.** **QwenGyre** (arXiv 2609.33848) — Elastic Scheduler **1.85×**; **prefix-shared trajectory trees** score partial progress after timeouts; NL2RepoBench **52.5% → 58.5%** in 48 steps. **GitSwarm** (Meta) — hundreds of async agents on one repo, all **30** IMOProofBench-Advanced, ProgramBench **79.4%** vs 65.1% single-agent. **Fork-and-Flush** beats single runs on **12/13** long-horizon tasks. **Test-writing gap: frontier agents' tests catch <55% of logical mutants.** Perplexity: **grep beat semantic search 63%/37%** on financial documents.
- **Tool eval (20 URLs, docx).** `sources/eval-url-revenue-opportunity-2026-10-13.md`. Theme: dev agent tooling / local inference / high-performance systems / media generation. **Docx license claims wrong or misleading on 5 of 20** (Insomnia NOT FOUND→MIT, sogen NOT FOUND→**GPL-2.0**, club-3090 AGPL→**Apache-2.0**, wordcraft Apache→**MIT OR Apache-2.0**, hydra imprecise) — **third wave running**. **Star counts unreliable, often ~2× off.** Tiers: **Integrate 6** (vercel-labs/skills, xxHash, cc-switch-cli, club-3090, takumi, anatomy), **Extract 3** (context-mode ELv2, openmed, DigUp), **Watch 1** (Unlimited-OCR), **Context 8**, **Pass 2**. The docx tiers **club-3090 Integrate while warning about AGPL copyleft** — the repo is Apache-2.0, so the caution rests on a wrong read. **Phase-0 not run in-session** (sandbox denies `api.github.com`) → `scripts/adopt_k290_phase0.sh`.
- **Feeds (5).** Latent Space AINews (Muse Wonder, DeepSeek sandbox, QwenGyre, GitSwarm, Decision 3.0 Apache-2.0 calibrated-probability models, claude-show-your-work MIT plugin, Cursor joins X Subscription, Arena $200M/3.1B + alignment index from traces, Karpathy funnel 20M/5,000). Pragmatic Engineer (Sam Newman DR excerpt: **RPO/RTO**, backup-restore / pilot-light / warm-failover / active-active; **capacity reservation is now a DR constraint**; **model providers are flaky vendors**; **mixing vendors in one flow raises the failure surface**; Uber burned its AI budget in 4 months). Event Horizon (**"not gambling" defence rejected**; 60% oppose election betting vs 13% support; Macquarie taker volume **$187B in 2026**; Kalshi **$274B YTD, $114B parlays**; **Sunday record $3.96B, 69.4% parlays**). Klement/KfW (Bales: **+0.2%/yr AI productivity → debt/GDP 185% → 143%** by 2056; **30y Treasuries = an implicit AI-productivity bet**). WuBlock (**September spot $696.7B, +36.5% MoM**; 14/14 up; top-3 concentration **62.4%** from 64.8%).
- **Concepts (4 new):** `crypto-exchange-spot-volume`, `ai-productivity-fiscal-debt`, `ai-vendor-multimodel-resilience`, `disaster-recovery-patterns`. **Entities (8 new):** muse-wonder, context-mode, vercel-skills, decision-3-0, claude-show-your-work, qwengyre, takumi, openmed. **Hubs:** `k290-arxiv-wave`, `k290-eval-wave`, `k290-feeds-wave`.
- **Updated (bidirectional backlinks):** ai-industry-trends-2026, deepseek-models, prediction-market-regulation-2026, kalshi-retail-lp, macro-weather-regime, crypto-derivatives-volume-2026, crypto-venue-website-traffic, agent-tool-use-verification, ai-safety, agent-harness-verification-bottleneck, agent-cost-routing-model-orchestra, guruwatcher-macro-watches, tool-evaluation-framework, k289-{arxiv,feeds}-wave, multi-wiki-eval-doc-level-vs-phase-0, xsp-lane-trading-framework, valuation-hypersensitivity-macro-liquidity, cemeni-stack, muse-spark-api, meta, agentic-context-management, agent-skill-manager, omlx, agent-toolkit-routing-research-backlog, html-effectiveness-pattern, atto-local-first-threat-model, cc-switch-cli, policy-distillation.
- **Briefs (6 staged):** cyber `2026-10-13_k290-vepa-and-sandbox-credential-abuse.md`; CCC `2026-10-13_k290-muse-wonder-and-agent-rl.md`; GW `2026-10-13_k290-ai-vendor-resilience-and-debt-watch.md`; gambling `2026-10-13_k290-gambling-definition-and-parlay-mix.md`; pm/xsp `2026-10-13_k290-pm-xsp-context-no-scp.md` (**no scp**); Atto `2026-10-13_k290-atto-pii-pdf-and-diagrams.md`; Basgiath `2026-10-13_k290-basgiath-promo-media-tooling.md`. `skill_audit`: all crosslinks-veto on `@osint-wiki/` (pre-existing tooling limitation — the check does not resolve wiki aliases; the shipped K289 brief fails identically). The muse brief's **regime_disclosure** veto was real and fixed with a single-regime disclosure.
- **Phase-1:** `scripts/adopt-waves/adopt_k290_phase1.sh` — `wire_ledger_check` PASS (wires=10). Wires section appended to `.cursor/rules/osint-phase1-adopt-wires.mdc`. Phase-0: `scripts/adopt-waves/adopt_k290_phase0.sh` (gh api license verify + 9 shallow clones, 500MB budget). **0 Integrate GO until Phase-0 runs.**
- **Sibling refs audit:** 0 genuinely missing OSINT pages. Sibling-side citation-form defects found (GuruWatcher cites raw feed filenames instead of wiki slugs; several wikis write `@osint-wiki/briefs/...` and `@osint-wiki/wiki/log.md`, which the alias cannot express since it maps to `wiki/`).
- **Archive:** pending — 4 raws (docx + 2 arXiv + duplicate PDF left in place) → `cemini-egress-fi`. Feeds are not archived (feed teasers).

## [2026-10-13] ingest | Muddy Waters short report — Edison International (EIX)

- **Target: Edison International (NYSE: EIX)**, parent of Southern California Edison. Report "MW is Short Edison International (US EIX)" published 2026-10-13 and delivered on stage at **Sohn San Francisco**, 10:30 AM PT ("Best Ideas: Carson Block & Peter S. Park"). URL: `muddywatersresearch.com/research/2026/oct-13/`.
- **Thesis:** SCE **failed to consider de-energizing four 220 kV transmission circuits** in Eaton Canyon on 7 Jan 2025 — the Eaton Fire corridor. Fire investigators concluded those circuits started the fire. A **willful-disregard** finding by the Wildfire Fund Administrator could trigger about **$20B (~$20/sh discounted, post-tax)**; an **imprudence** finding about **$4.3B (~$6.50/sh)**.
- **Reaction weak:** EIX about **$53.83, −3.25%**, near a 52-week low ($51.10–$81.62). The causation was already public, so the report is largely priced. **No puts trade.** Compare day-one moves: DLO −50% (2022), APP −20% (2025), ELF −8% (2024).
- **Pages:** `sources/muddy-waters-edison-international-eix-2026-10-13.md`; entities `entities/tickers/eix.md`, `entities/companies/muddy-waters-research.md`; concept `concepts/california-wildfire-utility-liability.md`.
- **Dead end (recorded):** the pre-reveal prediction attempt used Block's AI commentary (Economist "How to short AI", the "AI pretenders" line) and produced AI names (APLD, SMCI, CRWV) — all wrong. The reliable signal was the report URL pattern on MW's own site. Lesson: a short-seller's commentary is context, not a prior.
- **Source type:** web report (no egress archive). Retrieved 2026-10-13.

## [2026-10-09] cadence | gap detect and quarterly backtests

- **Gap detect:** 3789 pages. 36 type A, 137 type D, 246 type E. Report `.local/reports/wiki-gap-detect-2026-10-09.txt`. Tier 1 only. No Exa. Next due 2026-10-16.
- **Kalshi LP:** best Sharpe -24.66, PnL -$1.76, 16 trades, 1 market, 2026-09-19 to 2026-10-07. 0 of 80 configs with PnL above 0. Spread lab only. Do not promote. Report `.local/reports/kalshi-lp-backtest-2026-10-09.html`.
- **Cross-venue:** 0 trades. The matcher paired a bad BTC market and returned 4 bars on 2026-05-27. This run does not measure edge. Report `.local/reports/cross-venue-backtest-2026-10-09.html`.
- **Equity signal:** cache through 2026-06-12. No SSH. Best Sharpe 4.56 (lookback 30d, z 2.0, stop 3%). MCPT p=0.0005. Window 2021-06-14 to 2026-06-12. Sanity lab. Do not promote. Report `.local/reports/equity-signal-backtest-2026-10-09.html`.
- **HL funding:** Dune SQL returned 400 on tier medium/large and 402 (datapoint limit) on free/small. Fallback is the public Hyperliquid API. 10 coins, OI fixed at $50M, spread fixed at 2 bps, hours only 2026-08-10 to 2026-08-30. Best Sharpe 12.66 on 14 trades with PnL -$57.66. Directional lab. Do not change the steal-from posture. Report `.local/tools/hl-funding-sniper-reference/data/reports/backtest_report.html`.
- **PM LP:** not due. Not run.
- **Rapid-MLX:** CLI 0.16.0 installed. Telemetry off. No model pull. Free disk is 13 GB. `wire_status` is `runtime_wired`.

## [2026-10-12] ingest | K289 wave

- **Inbox:** 21 files → **20 source pages + 2 hubs**. **No eval docx this wave.** **Zero clones. No install. 0 Integrate GO.**
- **arXiv batch (8).** Quant: **`2610.13044` FOMO / FLEX options** — the first event study of single-name FLEX activity; post-event **listed-option OI rises** (β=0.3061, p=0.0042), selection into high IV (β=0.1235), and the **IV−RV spread predicts short-straddle P&L**; the honest read is **FLEX is a marker of institutional vol demand, not a directional predictor**. **`2610.13543` Three options are roughly enough** — in **rough Heston**, semi-static variance-optimal hedging via **Galtchouk–Kunita–Watanabe**: **three static vanillas cut the hedging error >95%** vs purely dynamic, across H ∈ {0.1, 0.3, 0.5}, with **Hurst-dependent strike choice**. **No trade. No xsp scp.**
- **Agents.** **`2610.13485` POrchestra** — **sub-agents proactively interrupt the orchestrator** to request harness adjustments; OPOD attributes each request to the preceding orchestration decision. **+9.1% success.** **`2610.13494` Humanize MLE** — names **long-horizon deceleration** and **harness staleness**; fixes with **context-reset session alternation**; **MLE-bench SOTA 78.2% at ¼ the budget**. **`2610.13647` A-SAW** — an IDE agent drafts architecture docs behind a **review gate** (author variance SD 19.2 → 3.8; **11/13 rejected unreviewed output**). **`2610.13772` MARGoS** — the reproducibility checklist (config hashing, seed propagation, frozen configs). **No `/route` swap.**
- **Safety + security.** **`2610.13078` Attention sees, MLP refuses** — **recognition and refusal are separate stages**; attention carries harmfulness, MLP writes refusal; joint P–D routing beats single-signal. **`2610.13651` ToFu (the headline)** — tool arguments from an LLM are **untrusted**; the **Repeat-After-Me** attack makes the orchestrator dispatch echoed tool-call text. ToFu fuzzed **273 MCP servers / 3,405 tools** → **253 verified bugs across 343 tools in 118 servers** (~**42% hit rate**). **The oracle is the tool's semantics, not a model.** **No PoC.**
- **Feeds (13).** **Event Horizon Ep. 36** — the CFTC issued an **Interim Final Rule** excluding **casino-style gambling** from the "swap" definition, and a **proposed rule** including **event contracts** in it; together a **preemption play** for the courts. Kalshi sought a Sixth Circuit rehearing the same day. The SCOTUS briefs now include the NFL, 145 tribes, 39 states, Dodd, and Gensler. **Kalshi "protected" NFL markets** (early-exit payout) mirror the sportsbook injury insurance. **No pm scp.**
- **XSP lane.** **GlitchSPX Talon weekly (Oct 12–16)** — bullish single names vs a **cautious Nasdaq map**; **QQQ $751.25 / $755 OTE / $760 structural invalidation**; SPXW and RUT carry **no valid OTE**; SQQQ sits on the caution side; MRVL/AMAT actionable but SMH/SOXX did not qualify. **Moontower Verticals** — compare payoffs **in the name's own standard deviations**, not percentages. **Moontower's 100-year almanac** — real compound returns (stocks 6.9%, long Treasuries 1.9%); **Elm vs Ibbotson ERP gap (~0 vs 4.7% over cash)**; Moontower #331 is a superset of the almanac. **No xsp scp.**
- **Agents (vendor).** **Anthropic dynamic workflows** — the lead agent writes a plan, **Claude writes the orchestration program**, and **Claude chooses the topology**. Candid Q&A: **"evals and lower defaults"** decide agent count; **the model does not know its budget**; flows cost **much more**. **No `/route` swap.**
- **Macro / crypto.** **Capital Flows** — sovereign-debt volatility; **France yields blowing out vs Bunds**, Euro swaps; a critique of the "devaluation solves everything" narrative → GuruWatcher **no auto-arm**. **Klement** — the EU ETS **raised intra-EU imports** (alignment beat carbon-cost arbitrage). **WuBlock** — the San Francisco... the Asia TOP10 (Kyrgyzstan terminates USDKG; **Dubai VARA 100% reserve rule**; Thailand's BTC/ETH-only crypto ETFs; Binance/IRGC accounts) and the weekly outlook (US CPI, ASML, OCP, Warsh). **SEO** — SparkToro: **"made entirely by humans" as a premium signal**.
- **The published artifact.** **Outlier Weekly** published *"How a $205 Million Drone Stock Makes Its Revenue"* — the Swarmer letter carrying the corrected audited numbers and the three-part revenue read (@sources/substack-rss-outlier-weekly-2026-10-12-swarmer-revenue.md).
- **Pages.** 2 hubs (`k289-arxiv-wave`, `k289-feeds-wave`); 20 source pages. **Updated:** `prediction-market-regulation-2026` (CFTC swap rules), `typed-judgement-desk-pattern` (dynamic workflows + orchestration).
- **Skipped:** `newsletter-rss-latent-space-2026-10-10-subscriber-exclusive-nyc-subscriber-meetups.md` (816 bytes; a subscriber-meetup notice, no research content). Archived, no page.
- **Phase-1 wires:** K289 section in `.cursor/rules/osint-phase1-adopt-wires.mdc`; `scripts/adopt_k289_phase1.sh`. FILE only — no wire-ledger rows.
- **Boundary:** zero clones. **No install, no scrape, no auto-submit, no xsp/pm scp, no LIVE Discord, no `/route` swap.**

## [2026-10-10] ingest | K288 wave

- **Inbox:** 15 files → **11 source pages + 3 hubs**, plus the Swarmer/rearmament evidence layer and recap briefs. **Zero clones. No install. 0 Integrate GO.**
- **The eval docx is inverted.** `Evaluating DFS and Betting Repositories.docx` marks **20/20 rows UNAVAILABLE** with "HTTP 404". **`gh api` found all 19 GitHub repos live** — `kycoonyatFD/nfl-assets-dashboard` (Sep 23), `everworldlife-netizen/fanduel-pace-totals` (Sep 20) and others predate the docx. **The reachability layer is broken.** Its works-cited is **confabulated from username substrings** (`atlantahouseplants/…` → "Atlanta Houseplants — Office Plant Design"). **Do not trust this docx's sources.** The failure mode has flipped from K281–K283's dead links to **live links declared dead**.
- **DFS / parlay repos** → briefs to **CeminiDFS** and **CeminiParlays**. **Operator guidance (2026-10-10): licence weight is lowered for DFS and parlay evaluations** — judge on fit and technique. `louaih/bonus-hedge` is the only licensed row (MIT). **No scrape. No auto-submit.**
- **Recap zips are desk output, not sources.** `dfsrecapweek4.zip` / `week4parlaysrecap.zip` carry structured `tool-gaps.md` (`do_not_auto_apply` on every row) → routed as briefs. **Recurring defects: ticket-capture completeness (three weeks running) and off-card bleed.** No repo edit from a recap desk.
- **War / Swarmer.** The 2 PDFs (`How to profit off war.pdf`, `REARM_War_Profit_2026-10-08.pdf`) are **two revisions of one note**; **file 2 is canonical** and file 1 is superseded. New evidence: the **sourced dossier** (FY2025 revenue $309,920; ~99% of Q2 from one counterparty group; Prince holds **no shares**) and the **Ratel revenue check**. ⚠ **Correction: Ratel's FY2024/FY2025 statements are AUDITED** (US GAAS, going-concern paragraph) — the Swarmer note's "unaudited" framing is wrong. The FY2026 earnout is a stretch: H1 is **12.5% of the $77M target**, H2 needs **7.0× H1** — only the **$86.6M of advances** converting gets there, and **Ratel reports substantial doubt about going concern**.
- **arXiv (2).** **NOMOS** — a written policy compiled into a **deterministic, LLM-free runtime tool-call gate**; violations **66.3% → 2.6%** (airline), **30.8% → 6.9%** (retail); **AgentDojo banking ASR 0.0%** vs 46.5%. **RESOLVE repairs 37% / rejects 13%** → **policy extraction must be statically verified.** Implementation **not released** (Zenodo DOI). **Gesture benchmark** — **SC, a common metric, correlates with no perceptual dimension**; semantic scoring (SGP) is the right one.
- **Feeds (4).** **TypeSafe/Jev >$100M ARR, $7.5B valuation, three weeks after launch**; decision models became a category (OpenAI Decisions API, Microsoft-Decision-1, Perplexity decider, Cloudflare clef, vLLM Semantic Router). **Unsloth turns Qwen3.5-4B into a decision model on 8GB VRAM**; **routing cut median Open SWE cost 64%**; **agent teams cost 1.8–5.1× more with little gain.** **Standard Bots** — perception learned, motion conventional, **inference on-prem**. **AlphaFold** — the right scaling law beats scale. **Polymarket Protocol V2**: full CTF rebuild, **migration Nov 2** (**no pm scp**). **Pyth partners with Exa for structured market data to AI agents via MCP.**
- **Pages.** 3 hubs (`k288-eval-wave`, `k288-arxiv-wave`, `k288-feeds-wave`); 11 source pages. **Updated:** `typed-judgement-desk-pattern` (the K286 pattern became a category), `swarmer-long-thesis` (audit correction), `rearmament-war-profit-desk` (PDF pair, file 2 canonical).
- **Process note (recorded):** the repo has an outstanding manual ingest gate — the eval's reachability check must be **verified with `gh api` before trusting a UNAVAILABLE verdict**.
- **Phase-1 wires:** K288 section in `.cursor/rules/osint-phase1-adopt-wires.mdc`; `scripts/adopt_k288_phase1.sh`. FILE only — no wire-ledger rows.
- **Boundary:** zero clones. **No install, no scrape, no auto-submit, no xsp/pm scp, no LIVE Discord, no `/route` swap.**

## [2026-10-09] ingest | K287 wave

- **Inbox:** 20 files pinned with `ls` before archive. Preingest: 15 NEW, 5 LIKELY, 0 DUPLICATE. LIKELY title and same-feed letters fold onto `concepts/k287-feeds-wave.md`. No second source page for the repeated Latent Space title. Archive: 20 of 20 files on `cemini-egress-fi:/opt/cemini-bulk/research/osint/`. Local copies removed.
- **Eval:** `Multi-Repo Revenue Evaluation.docx` (sha256 `b36632927d25ce3f…`). 1 Integrate, 6 Extract, 1 Watch, 6 Context, 6 Pass. Pass rows stay on `sources/eval-multi-repo-revenue-2026-10-09.md`.
- **gh api:** 18 of 18 repos exist. Docx licence column not used. LiteLLM API id **NOASSERTION**; file is MIT outside `enterprise/`. sogen **GPL-2.0**. daily_stock_analysis **MIT**. blessed-rs licence field empty. open-code-review **Apache-2.0**, 45,129 stars.
- **Phase-0** under `/tmp/k287-phase0/` (no install): open-code-review **GO REFERENCE** (pattern not new, no brief); litellm **NO-GO** (proxy already on 127.0.0.1:8791); sogen **NO-GO** (not permissive, no lab brief); daily_stock_analysis **CONDITIONAL-GO** (alert-only, not started, no orders).
- **Folds:** artcraft umbrella still NOASSERTION; rea MIT, owned-lab boundary stays; treg Pass, still NOASSERTION.
- **Hosted model:** `platform.experientiallabs.ai` GLM-5.3-flash-abliterated recorded as a hosted model. No key. No install. GPU repo `nullmoth/nvidia-macos-driver` is Pass. Do not build it.
- **arXiv (8):** constitutional gating confirms deterministic recovery and does not change the rule. HarnessSQL and Embodied Turing Machines get **no training wire**. HANS licence does not allow a genealogy brief. TestPrism joint success 28.00 percent vs single-reference 59.67 percent.
- **Feeds:** war-profit letter links `concepts/rearmament-defense-growth-thesis.md` (no second thesis). Sports letter does not change a ticket rule. Macro teaser states no numeric level. Security letters are summary only. Crypto letters are short notes.
- **Swarmer:** concept page verdict **UNSOUND**. Original sentences kept and marked. Vesting is 60 percent time and 40 percent milestone. The earnout needs both revenue and operating income. Audit file `reports/research/pack-swmr-long-thesis-20261009/qa/audit-final.md`. Desk note not rewritten.
- **Phase-1:** `scripts/phase1_adopt_inventory.py` is not in this repo. No settings edit. No ADOPT. NO-GO rows are `wont_wire`. The stock-digest CONDITIONAL-GO is `deferred`.
- **Gate:** `ingest_session_gate.py` skips stale verification tags inside `wiki/log.md`. Those lines quote older batches.
- **Briefs:** `briefs/2026-10-09_k287-guruwatcher-stock-digest-alert.md`, `briefs/2026-10-09_k287-illo-skill-no-wire.md`. No scp. Sibling copy to `../GuruWatcher/briefs/` blocked (operation not permitted). Local brief kept.
- **Boundary:** no install, no Ashburn copy, no image or print local wire.

## [2026-10-09] report | Swarmer long thesis (Prince roll-up)

- **Pack:** `reports/research/pack-swmr-long-thesis-20261009/` (untracked). Desk note `SWMR_long_thesis_2026-10-09.md`.
- **Thesis:** long Swarmer (NASDAQ: SWMR) as a speculative special situation. The bet is Prince consolidating Ukraine's combat-proven drone and robot makers. The software is real but small, and the revenue has a round-trip problem.
- **Key numbers:** price $13.13, market cap about $218M, TTM revenue $298K. Ratel Robotics: audited FY2025 net sales $18.6M, $86.6M of customer advances, FY2026 earnout target $77M. Prince holds zero shares, only unvested options. No listed options, so equity only.
- **Verification:** a Grok dossier plus two verification rounds corrected the Prince holding (zero, not 1,774,725 shares) and the Ratel dilution split (91.6/8.4 at closing, not 74.9/25.1).
- **Wiki:** `concepts/swarmer-prince-rollup-thesis.md` + `sources/swarmer-long-thesis-2026-10-09.md`.
- **Audit:** done 2026-10-09. Verdict UNSOUND. File `reports/research/pack-swmr-long-thesis-20261009/qa/audit-final.md`. The desk note was not rewritten. The Outlier handoff for this pack was not requested.

## [2026-10-08] report | War Is Coming. Here Is How to Profit. (rearmament defense growth)

- **Pack:** `reports/research/pack-rearmament-war-profit-20261008/` (untracked). Desk note `thesis.md`, PDF on the Desktop. SEO handoff `../SEO:GEO B&M Business/briefs/2026-10-08_rearmament-war-profit-outlier.md` + `wiki/concepts/rearmament-war-profit-outlier-notes.md`.
- **Trigger:** Marco Rubio Athens speech 7 Oct 2026 (`@SecRubio` 2107934022286385228) + the quote tweet by `@crypto_condom` framing it as an investment strategy.
- **Thesis:** FY2027 request $1.45T; missile and munitions pool about $95B (CRS: about $52.9B to the named programs); Patriot stockpile down about 65 to 67 percent; a reported 2027 Russia Article 5 window. Eight growth names: LHX, MRCY, MP (inputs) and AVAV, KTOS, RCAT, ONDS, UMAC (drones). Hold the floor, LEAPS on the larger names, speculative equity on the micro-caps.
- **Audit:** independent fact-check + nine-model OpenRouter audit, about $1.27. Corrections applied to the munitions percentage, market caps, an award qualification, a probe description, and causality.
- **Wiki:** `concepts/rearmament-defense-growth-thesis.md` + `sources/rearmament-war-profit-desk-2026-10-08.md`. Outlier article pending operator GO.

## [2026-10-08] ingest | K286 — X post @savipww (typed-judgement desk)

- **Source:** X Article `@savipww` — *"Megabrain (Jev) & Six Grok Bots That Already Made Me Six Figures (Setup Guide)"* (2026-09-23), read with **`opencli twitter article 2102720919185617314`**.
- **The pattern:** a **typed decision engine** (Jev / TypeSafe) answers `noul` (if) / `choice` (switch) / `score` (sort) questions with probabilities in **70–500 ms**, so the agent seats stop judging in prose. "**Code fetches, the model judges, code decides.**" Filter is a **kill order** — facts kill before judgements. Question **sets** (not single questions) because state is charged once per call → **3–4× cheaper**. **Shadow mode** logs disagreement rows; a **rejection bench** with variable expiry; a **one-position guard**. Cost ~**6¢/day**.
- **The finding:** we hold **both halves** — Jev live on the laptop (@entities/tools/jev-mcp.md) and **19 Grok Bot charters** — and **they are not connected**. Verified 2026-10-08: `grep -i jev briefs/2026-09-01_grok-bot-charters.md` returns **nothing**. Every seat uses the model's prose judgement. **This is the single biggest capability increase available to the desk.**
- **Boundary:** the **trading egress** is out of bounds — no trading egress from the Grok Bot VM (@concepts/grok-bot-operator-patterns.md). Jev is a **judgement service**, not egress, so wiring the judge is safe. **File only. No `/route` swap.**
- **New pages:** `concepts/typed-judgement-desk-pattern.md` + `sources/x-post-savipww-megabrain-jev-grok-bots-2026-09-23.md`. **Updated:** `entities/tools/grok-bot.md` (Jev gap), `entities/tools/rapid-mlx.md` + `sources/eval-github-repository-revenue-2026-10-08.md` (**Rapid-MLX licence CONFIRMED Apache-2.0**).
- **Brief:** `briefs/2026-10-08_jev-typed-judgement-desk.md`.

## [2026-10-08] ingest | K285 wave

- **Inbox:** 12 files → **12 source pages + 3 hubs**. One eval docx (20 rows), 8 arXiv papers, 3 feeds. **Zero clones. No install. 1 Integrate lead (licence unconfirmed).**
- **The eval docx — `GitHub Repository Revenue Evaluation.docx`.** Theme: reverse engineering, local LLM inference, autonomous agent orchestration, graphics pipelines, developer toolchain validation. **1 Integrate · 5 Extract · 1 Watch · 10 Context · 3 Pass.**
- **The Integrate lead — `raullenchai/Rapid-MLX`.** A local **Apple Silicon MLX** inference server with an OpenAI/Anthropic-compatible endpoint (3,941★). Atto zero-PII parsing + local lab. ⚠ **Licence NOASSERTION** at the API though the description claims Apache-2.0 — **confirm before wiring.** Pairs with K284's `Strata`: **two local-inference Integrates in two waves.**
- **The Extract rows.** `morluto/rea` (19,363★, **MIT**) — MCP-based **Hopper decompilation + tracing**; **a Pass in K283, now an Extract.** `storytold/artcraft` (6,064★) — 3D staging before generative video → Basgiath clips; ⚠ **NOASSERTION**. `LalitMaganti/syntaqlite` (Apache-2.0) — SQLite static linting. `henryiii/validate-pyproject-schema-store` (8★) — daily SchemaStore mirror. `ColeMurray/background-agents` (MIT) — sandboxed sub-tasks.
- **Watch:** `koala73/worldmonitor` (**88,036★, AGPL-3.0**) — headless path only, as a Polymarket-LP circuit-breaker. **No pm scp.**
- **Pass:** `fluffychat` (AGPL), `pi-extensions`, `react-native-skia`. **`AnyPS5` is GPL-2.0** — Pass in K283, Context now; do not adopt.
- **Phase-0 (WebFetch).** **All 20 repos exist — zero 404**, the **second consecutive all-real batch** (K284 also clean; K281–K283 each had 6–7 dead links). Licence flags: **Rapid-MLX NOASSERTION**, **artcraft NOASSERTION**, **worldmonitor AGPL-3.0**, **AnyPS5 GPL-2.0**, `system-design-notes` none.
- **arXiv batch (8).** Quant: `2610.09244` **risk-averse multi-population mean-field games** — AI-vs-human trader populations; reward 136.65→130.56, sensitivity 25.21→22.09 (**no trade, no scp**). OCR: `2610.09439` **InscriptionOCR** — Brahmi inscription OCR + Prakrit→English NMT (ResNet-50 100%, M2M-100 BLEU 56.4); **CC BY-NC 4.0**. Safety: `2610.10276` **PatchBench** — **MMLU flat while local regression is severe** (BNPS −26.3); `2610.10345` **SLDR** — signed layer sensitivity, repair two layers, **Harmful Score 11.54→0.08** near-lossless. Agents: `2610.10426` **CoTrace** — trajectory value depends on the harness; **gains vanish under a foreign runtime** (78→90, 30–50 trajs/iter); `2610.10332` **TPD** — stage-scored small agents, **+19.7 pp at 200 demos**; `2610.10478` **Before They Can Solve** — decisive-step screening ρ **0.964**, but **HumanEval ρ = −0.394**; `2610.10498` **EmbodiedRSI** — Value-of-Information experiment selection (RoboCasa Composite-Unseen 71.3% vs 40.1%).
- **The through-line (5 of 8 papers):** **the harness, the runtime, and the local metric matter more than the headline number.** Same doctrine as the workspace's audit gates.
- **Feeds (3).** Latent Space — **Stacklok/Mecatl** cloud-native harness: separate the agent loop from execution and state; route in the harness, not the gateway. Pragmatic Engineer — **Sam Newman**: **"LLMs are not world models … they have no concept of causality," so guardrails are not the long-term solution**; module boundaries first; the Opus-5.5 `--dangerously-skip-permissions` disk-format incident. Moontower — options-as-surgical-tools with a **Kelly worked example** (38.5/39 call spread 3-to-1 vs 1-to-1; f* = p − q/b → half-Kelly). **No xsp scp.**
- **Entities (3 new):** rapid-mlx, rea, syntaqlite. **Concepts (3 hubs new + 0 updated).** New hubs: `k285-eval-wave`, `k285-arxiv-wave`, `k285-feeds-wave`.
- **Briefs staged (7):** `briefs/2026-10-08_k285-atto-local-inference-lint.md`, `..._rea-background-agents.md`, `..._artcraft-clips.md`, `..._worldmonitor-canary.md`, `..._ccc-harness-resilience.md`, `..._ccc-harness-coevolution.md`, `..._cyber-model-repair.md`.
- **Process note:** the Basgiath row ships as a **brief** (`dragon-rider-map/briefs/`), per the LESSONS entry of 2026-10-08 — prompts are one-shot.
- **Phase-1 wires:** K285 section in `.cursor/rules/osint-phase1-adopt-wires.mdc`; `scripts/adopt_k285_phase1.sh`. FILE only — no wire-ledger rows.
- **Late feeds (+3, ingested after the main pass).** Three feeds landed mid-ingest and were archived before processing; pulled back from egress and ingested. `substack-rss-latent-space-2026-10-08-claude-haiku-55.md` — **Claude Haiku 5.5**, the cheap-worker tier, tiered pricing, but ~**3× Luna tokens** at max effort; `substack-rss-event-horizon-2026-10-08-39-states-scotus-brief.md` — **39 states + the NFL file at SCOTUS** against prediction markets; Michigan halts Coinbase by 2026-10-10; `substack-rss-klement-2026-10-08-government-debt-monetary-policy.md` — BIS: the debt level changes a rate shock's effect. **No `/route` swap. No pm scp.**
- **Boundary:** zero clones (bash has no network). **No xsp scp, no pm scp, no LIVE Discord, no `/route` swap.**

## [2026-10-07] ingest | K284 wave

- **Inbox:** 17 files → **17 source pages + 3 hubs**. Two eval docx (39 rows), 8 arXiv papers, 7 feeds. **Zero clones. No install. 0 install-required Integrate GO.**
- **Eval docx A — `Developer Resource Revenue Evaluation.docx`.** Theme: frontend architecture, agent UI design registries, component primitives, compute kernels. **3 Integrate · 8 Extract · 8 Context · 1 UNAVAILABLE.** The three Integrate rows are **design-registry MCPs**: `styles.refero.design` (DESIGN.md tokens), `21st.dev` (shadcn registry), `uiverse.io` (CSS controls). The gap: **agent-written frontends drift without a design contract.**
- **Eval docx B — `URL Revenue Opportunity Evaluation.docx`.** Theme: agent tooling, local model inference, clean-room creative suites, PS5 homebrew. **4 Integrate · 5 Extract · 3 Watch · 2 Context · 5 Pass.**
- **The headline — the `storytold` "ArtCraft" suite.** Seven active, **Apache-2.0**, pure-Rust clean-room Adobe replacements: photocraft (Photoshop, 12,693★), filmcraft, lightcraft, printcraft, vectorcraft, effectcraft, designcraft. The play: an **offline Atto document pipeline** — enhance scans → typeset a monograph → bind the PDF packet — no Adobe licence, **client PII local (`~/AttoVault/`)**. `photocraft` needs `--automation-read-root`/`--automation-write-root` boundary flags.
- **`Niko1221/Strata` (Integrate).** **MIT**, 16,491★ — a local **125B-MoE** inference engine on consumer hardware, exposing a localhost OpenAI/Anthropic endpoint. Local abliterated lab + Atto air-gapped parsing. **35–55 GB RAM lock; NVMe required.**
- **Extract.** `monid` (MIT — GuruWatcher metering), `upleft` (**6★ — read the idea**), `vectorcraft`, `lightcraft`, `treg` (**NOASSERTION — licence flag**), `21st.dev`.
- **Watch:** `incredible.one` (computer-use), `effectcraft`/`filmcraft` (Basgiath clips). **Pass (no code):** `omarchy-apple-dev` + four **PS5 emulators** (RetroArch, ProsperoEden, PS5X360, PS5SX2).
- **arXiv batch (8).** Quant: `2610.07554` **CGMY B-spline Galerkin** (Toeplitz → O(N log N) FFT; S&P IV RMSE 2.47 vp). Game theory: `2610.07686` **BluffJAX** (**MIT**, 10 imperfect-info games, JIT-CFR, **~2e7 samples/s**); `2610.08768` **arbitrarily slow fictitious play** (counterexamples to Karlin's O(t^{−1/2})). Agents: `2610.08621` Recursive Game Creator (coding-native player), `2610.08720` WorldSolver (GPT-5.6-Sol 48.7%), `2610.08722` compaction harm (**modest/bounded**), `2610.08761` **VeriFine** (judge co-evolves; **judge–human 0.53→0.82**), `2610.08630` In-Parameter Memory survey.
- **Feeds (7).** Pragmatic Engineer — **agent-authored PRs exceeded human-authored on GitHub in Aug 2026**; **"code reviews are dead" (LGTM theater)**; migrations collapse to weeks. Latent Space — **OpenAI 722 math papers** (Quasi-Riemann); **CIAware** monitor-awareness + **METR** transcript-as-untrusted; an AutomationBench audit found **206 verifier bugs**. Event Horizon — **CFTC proposes CTX/CAM**; **Connecticut: ProphetX/Gemini/Webull withdrew**; Kalshi US 500 perps; EDGE Markets agentic capital allocation. Klement ×2 — **Anthropic rev $4.6 B vs compute $7.3 B, op loss $8.06 B**; Europe defence-readiness index. SecPro — Cyber_AI newsletter launch (no content). WuBlock — **miner-to-AI pivot** (AI $1.5 M/MW vs mining $500 k/MW; hashprice record low $27.7/PH/s/day; **Ethiopia cut miner power 75%**).
- **Phase-0 (WebFetch).** **All 19 GitHub repos exist and are active** — **zero dead links**, inverting the K281–K283 pattern. **One docx false negative:** `pingdotgg/ts-rust` was rated UNAVAILABLE/404 but is alive (**159★, MIT**). Two licence corrections: **`treg` is NOASSERTION** (Apache-2.0 + additional terms); the **`storytold` suite is Apache-2.0**.
- **Entities (7 new):** strata, artcraft-suite, treg, monid, bluffjax, refero-styles, 21st-dev. **Concepts (3 new + 4 updated).** New hubs: `k284-eval-wave`, `k284-arxiv-wave`, `k284-feeds-wave`. Updated: prediction-market-regulation-2026 (CFTC CTX/CAM), agent-tool-use-verification (VeriFine), ai-industry-trends-2026 (math + AI economics), agentic-code-quality-gates (code-review theater).
- **Briefs staged (6):** `briefs/2026-10-07_k284-atto-document-pipeline.md`, `..._strata-local-inference.md`, `..._ccc-design-registries.md`, `..._guruwatcher-monid.md`, `..._pm-cftc-crypto.md`, `..._basgiath-clips.md`.
- **Incoming briefs:** no sibling `@osint-wiki/...` ref needs a new page.
- **Phase-1 wires:** K284 section in `.cursor/rules/osint-phase1-adopt-wires.mdc`; `scripts/adopt_k284_phase1.sh`. FILE only — no `runtime_wired` pages, so no wire-ledger rows.
- **Boundary:** zero clones (bash has no network). **No xsp scp, no pm scp, no LIVE Discord, no `/route` swap.** No install.

## [2026-10-06] ingest | K283 wave

- **Inbox:** 16 files → **16 source pages + 3 hubs**. Two eval docx (40 rows), 8 arXiv papers, 6 feeds. **Zero clones. 1 product Integrate GO (human-gated).**
- **Eval docx A — `GitHub Repositories Revenue Evaluation.docx`.** Theme: dev tools, agent harnesses, local RAG, CAD, concurrency/emulation. **1 Integrate · 6 Extract · 2 Watch · 6 Context · 5 Pass · 0 UNAVAILABLE.**
- **The Integrate row — `lfnovo/open-notebook` (first in four waves).** MIT, self-hosted multi-modal RAG — a private NotebookLM. **Verified 2026-10-06 (WebFetch): repo exists, MIT, ~39.9k stars, 4.6k forks.** The Atto-side play: page-cited Q&A over municipal registry PDFs with **local-only Ollama** inference, no client PII to cloud models. The wiki's K39 "Reference-only" verdict rested on **deleted-prod-host** constraints (CPX21 RAM headroom; PostgreSQL-only) — re-scored to **Integrate** now that the target is the laptop. Human-gated; **no install this session**; no `truth.ged` write.
- **Eval docx B — `GitHub Revenue Opportunity Evaluation.docx`.** Theme: Bedrock ecosystem / server tooling / agent runtimes. **0 Integrate · 9 Extract · 7 Context · 4 Pass.** **13 of 20 rows route to Basgiath.**
- **Basgiath Extracts.** `Flower7C3/simple-money` (in-game roleplay currency + ATM block, MIT), `tfgh6/bedrock-ui-animations` (JSON UI easing — flight speedometer/stamina, overlap 0.85, highest of batch), `Flower7C3/books-minecraft-bedrock-addon` (readable lore items), `kongbai9288/mc-mod-migrator` (schema migration across Mojang updates), `Flower7C3/just-clock` (HUD timer). **Currency stays in-game tokens only. No Marketplace. Fan-made labels.**
- **Instructive Pass, again — goal match / stack mismatch.** The Bedrock docx names `void-community/Void`; its own works-cited resolves the real repo to **`caunt/Void` — a Java-Edition proxy**. Bedrock DBS has no BungeeCord-style proxy here. Same pattern as K282's `FabricModdingConventions`.
- **Atto telephony row.** `albeSavvy/centralino-ai-studio-medico` — a medical switchboard whose core is **Italian voice/intent routing** (`atto overlap 0.70`). Extract the Italian intent taxonomy + structured interaction logging for *stato civile* / comune triage. **PII gate: no client genealogical data to a third-party telephony model without a human gate.**
- **GuruWatcher concurrency pair.** `ColeMurray/background-agents` (detached async workers) + `ldm0/keyed-lock` (per-key mutex) close the race-condition gap on parallel newsletter ingest. **Never auto-arm. Never `watches.json`.** No order routing.
- **CCC harness extracts.** `tester-army/e2e` (**cached agentic replay** — tokens once for discovery, then deterministic replay in CI), `msitarzewski/agency-agents` (persona library; must not override invariants), `frankbria/ralph-claude-code` (Ralph loop — mandatory cost caps), `kim-em/hex-dev` (hexagonal scaffolding). **No `/route` swap.**
- **CeminiParlays.** `pawurb/hotpath-rs` — Rust hot-path profiler for the copula engine. **No scrape, no auto-submit.**
- **Watch.** `deepseek-ai/DeepGEMM` (needs Hopper/Blackwell FP8); `lalalune/outreachr` (blocked on SPF/DKIM/DMARC warmup, not code).
- **arXiv batch (8).** Quant/math: **`2610.03849` Beneath the VIX** — splits the VIX into **probability × severity**; severity is **91.5% [86.7, 96.3]** of the recession log premium, severity elasticity 1.032, probability elasticity −0.032; DPP–VIX correlation 0.992. `2610.06495` a-posteriori **UVM** bounds (cash-gamma dual, BSB residual). `2610.06292` MFG fictitious-play convergence. `2610.04530` Λ-broadcast voter model (pure math). Agent/tooling: **`2610.06829` CLIFT** — conformal self-verification, **+11.3 pp on OM2W at K=4 with zero policy training** (additive-only reward); **`2610.06782` T-Search** — **Apache-2.0** agentic retriever, 61.3 fused Recall@10; **`2610.06650` Wikidata traces** — persistent-Python RLM harness beats stateless tool-calling (49→61, 60→74); **`2610.06790` BTTF** — SQLite over terabyte waveform dumps, multi-agent +17.3%.
- **Feeds (6).** Event Horizon: **Ohio cease-and-desist to 10 platforms** (Coinbase/Gemini/Novig/Polymarket/Robinhood/WeBull …) after the Sixth Circuit upheld Ohio vs Kalshi; **CFTC no-action** lets DCMs convert perpetual-style index futures into **true perpetuals** (expires **2026-10-20**); Kalshi record **$3.68 B** Sunday. WuBlock: **Hyperliquid funding-cap 4%/h → 0.5%** + HIP-4 capacity doubled; Liquid Network consensus exploit (~4,000 unbacked L-BTC, ~602 BTC unrecovered); **MemTensor** PyPI/npm compromise = **agent-memory supply chain**. Klement: nationalised Chilean firms ROA −11–13%, governing coalition −1–4% vote share. Latent Space: **Reflection Beam** 501B open model (**no `/route` swap**). SecPro ×2: patch≠recover; **OWASP Agentic TOP 10 / ANS / A2AS**.
- **Entities (14 new, 1 updated).** New: tester-army-e2e, agency-agents, ralph-claude-code, background-agents, keyed-lock, hotpath-rs, centralino-ai-studio-medico, t-search, mc-mod-migrator, void-minecraft-proxy, deepgemm, outreachr, bettercap (**gap-fill** — was referenced by a cyber brief but unwritten), bedrock-ui-animations, simple-money-minecraft-bedrock-addon. **Updated:** open-notebook (Reference-only → Integrate, K283 re-evaluation section).
- **Concepts (3 new + 4 updated).** New hubs: `k283-eval-wave`, `k283-arxiv-wave`, `k283-feeds-wave`. Updated: prediction-market-regulation-2026 (Ohio C&D + CFTC perps), crypto-derivatives-volume-2026 (HL funding cap), agent-setup-instruction-supply-chain (MemTensor), agent-tool-use-verification (CLIFT + RLM + T-Search).
- **Briefs written and staged (7):** `briefs/2026-10-06_k283-atto-open-notebook.md`, `..._atto-italian-telephony.md`, `..._guruwatcher-concurrency.md`, `..._ccc-agent-harness.md`, `..._basgiath-bedrock-extracts.md`, `..._pm-hl-feeds.md`, `..._cyber-agent-verification.md`.
- **Incoming briefs:** scanned `@osint-wiki/...` refs across all sibling `briefs/` dirs. Most "dangling" refs are path artifacts (pages exist under other slugs; `wiki/briefs/*` are gitignored). Real gap found and fixed: **`entities/tools/bettercap.md`** (a cyber brief cited it; page did not exist).
- **Phase-1 wires:** K283 section added to `.cursor/rules/osint-phase1-adopt-wires.mdc`; `scripts/adopt_k283_phase1.sh` + `scripts/adopt-waves/adopt_k283_phase1.sh`. FILE only — no `runtime_wired` pages, so no wire-ledger rows (matches K280–K282).
- **Eval-quality:** `NOT FOUND` metadata on **34 of 40 rows**; docx B lists a duplicate URL. Third generated-looking URL list in four days (K281 7/20 dead, K282 6/20 dead).
- **Boundary:** zero clones (bash has no network). **No xsp scp, no pm scp, no LIVE Discord, no `/route` swap.** No install.

## [2026-10-05] ingest | K282 wave

- **Inbox:** 13 files → **12 source pages + 3 hubs**. One eval docx (20 rows), 8 arXiv papers, 4 feeds. **12/13 archived to egress. Zero clones. 0 product Integrate GO.**
- **The eval docx — `Project Stack Revenue Evaluation.docx`.** Theme: level editors, modding infrastructure, agent workspaces, Minecraft Bedrock tooling. Tiers: **0 Integrate · 3 Extract · 4 Context · 7 Pass · 6 UNAVAILABLE.**
- **Two Basgiath Extract rows.** (1) The `xentropaff` Bedrock add-on guide scores `basgiath overlap 0.85` — the packaging standard: Behavior Pack / Resource Pack split, matched **manifest UUIDs**, one-click `.mcaddon`. The failure it names is real churn: a UUID mismatch breaks the Bedrock import dialog and the player leaves. (2) `rehan-remade/universal-modder` (0.75) adds a **fal MCP generative asset pipeline** on top of the layout K281 already took. **Operator decision (2026-10-05): do not adopt it — the pipeline is a paid third-party service, and we will not pay. Extract the free layout and the asset-iteration loop only.**
- **CCC gets the `ProblemFactory/vibespace` pattern.** Detachable background workers that survive daemon restarts, long-task cron, tiled views. Our harness has no native way to detach a long job from the session. **Upstream licence NOT FOUND — extract the contract, do not vendor.**
- **Agent-eval arXiv batch (7 papers).** **EvoRiskBench** is the actionable one: nine model × harness configs, injection via **MCP tools, skills and subagents**, aggregate ASR **37.46%**, worst 68.44% (DeepSeek-V4-Pro-0813 × Codex). **Model spread (54.37 pp) ≫ harness spread (5.41 pp).** Also: PowerBench (refusal triples at society scale), MLCommons jailbreak (Resilience Gap 7.57 pp, paired-metric template), MoE router gradient (local-lab abliteration technique, dual-use), kinetic theory of a validation gate (separation theorem), HyperBrowseComp (browsing eval; exercises Exa), and a financial-agent paper (**curated skills +16.2 pts vs self-generated +0.5**).
- **Duplicate caught cross-wiki.** `arxiv-2610.03675` (FrugalEvo) was **already ingested by the CCC wiki today (K425)**. Not re-ingested here. The inbox PDF is archived as already-covered.
- **Eval-quality signal, again.** **6 of 20 eval URLs return 404**, several of them `*-Community-2026` repos. Second wave in two days with a high dead-link rate (K281: 7 of 20). The URL lists are partly generated.
- **Instructive Pass.** `brainage04/FabricModdingConventions` does the thing Basgiath wants — headless GameTest regression CI for Minecraft entities — but it is **Java Fabric**, which cannot compile to Bedrock. **Goal match, stack mismatch.**
- **Briefs written and distributed (5):** `dragon-rider-map/briefs/2026-10-05_k282-basgiath-packaging.md`; `Cemini claude code CCC/briefs/2026-10-05_k282-ccc-harness.md`; `CCC .../2026-10-05_k282-ccc-agent-eval.md`; `Cybersecurity wiki/briefs/2026-10-05_agent-safety-eval-from-osint.md`; `Game Dev wiki/briefs/2026-10-05_k282-level-editors-from-osint.md`. All PASS `skill_audit` (100/100).
- **Incoming briefs:** no sibling brief routed into OSINT needs a new page. All `@osint-wiki/...` references in sibling briefs from the last 5 days resolve.
- **Boundary:** FILE only. No install. Zero clones. No client-modification code. **No XSP/PM scp. Never auto-arm.**

## [2026-10-04] ingest | K281 wave

- **NEW PROJECT REGISTERED — Basgiath.** The operator named a second co-primary workstream alongside GuruWatcher: **Basgiath**, a Minecraft **Bedrock** addition in the Empyrean series (dragon riders, a war college). Repo is `Projects/dragon-rider-map/` — its README opens `# Basgiath` with an ASCII dragon. Distribution target is MCPEDL and CurseForge, non-monetized fan project. The eval docx carries `basgiath` as its own overlap key beside atto, guruwatcher, ceminidfs, ceminiparlays.
- **Inbox:** 6 files → 9 source pages + 4 hubs. **Both eval docx are Minecraft** — one modding (20 rows), one Bedrock protocol (19 rows). 6/6 archived to egress. Zero clones.
- **The named repo — `rehan-remade/universal-modder`.** Operator asked for this one specifically. `gh api` 2026-10-04: **MIT, 2,919 stars, 22,365 KB, pushed the same day, not archived.** It is a skills-plus-knowledge-base library that lets any coding agent mod PC games. **Two patterns worth copying:** (1) one canonical `skills/` tree with `.agents/skills`, `.claude/skills`, `.gemini/skills`, `.github/skills` all symlinked to it, and a single canonical `AGENTS.md` that `CLAUDE.md` and `GEMINI.md` point at — cleaner than our post-commit sync, which is the mechanism that reverted a skill edit in K276; (2) a `knowledge/INDEX.md` field-notes base where the agent must write down what it learned for the next agent. **Adopt the layout, not the pipeline** — its asset path routes through a paid third-party service, a new spend line we have not agreed to. No install.
- **Seven unreachable rows.** The modding batch had 7 of 20 URLs that do not resolve — the highest unavailable rate this month. Worth noting as an eval-quality signal: that URL list looks partly generated rather than verified.
- **The two Integrate rows.** `thejacedev/McHeads-API` (MIT) renders player heads and skins from **Bedrock XUIDs as well as Java UUIDs** — most skin renderers are Java-only, so this solves a real gap for flight scoreboards and rider profiles. `bedrock-mc/mcpelauncher-agent` is an MCP layer over the Bedrock launcher; paired with the modding batch's headless container and LevelDB inventory tooling, that is the shape of an unattended test bench.
- **A named structure appears.** Moontower #330 reports **notable size buying in INTC October 16 130 calls** on 28 September, ahead of Intel's 23 October earnings, with a proposed fade of selling INTC straddles or writing covered calls. **Recorded as a claim with a date and a strike. Not armed. No xsp scp.**
- **Ingest dedup insight.** Moontower #330 is a **superset**: two other captures in the same inbox are near-verbatim sections of it. Ingested #330 once; the other two became pointer pages. Triplicating would have been the lazy path.
- **Moontower preingest false positive.** The checker flagged #330 as LIKELY on a fuzzy title match against earlier numbered issues. Numbered newsletters collide on title. Same class as the K279 false positive.
- **Distribution signal.** Robinhood's new platform exposes third-party data providers as subscribable modules inside its own trading agent. First time a brokerage appears as a channel rather than a counterparty. Noted, not integrated.
- **Korea/Japan split.** South Korea's market cap fell 33% in six months while its FSC proposed extending tokenized securities to stocks, bonds and funds. Japan launched a tax-detection system and formed a group to study on-chain settlement of **government bonds**. Retail shrinking while the product widens.
- **Boundary:** no install. Zero clones. **No client-modification code recorded** — the eval's Java anticheat-evasion and hacked-client rows were Pass, and nothing from them is on any page. **No XSP/PM scp. Never auto-arm.**
- **Concepts:** 4 k281 hubs (basgiath, harness, vol-quant, ood-stub). K278/K279/K280 hubs backlinked.
- **Next actions (not done):**
  1. Basgiath: evaluate `mcpelauncher-agent` plus the headless container as a test bench. That is the highest-leverage pairing in the wave.
  2. Basgiath: adopt the one-tree-plus-symlinks skill layout incrementally, starting with one repo.
  3. Fix `preingest_check.py` to also match numbered newsletters on URL, not title.
  4. Atto: the Kraken head-to-head is still unrun.
  5. CeminiParlays: the pick'em work is done and passing but uncommitted.

## [2026-10-03] ingest | K280 wave

- **Inbox:** one eval docx, 20 rows — plus **one wublock weekly that arrived mid-session and was swept to egress by the archive loop before it had a page**. That page is now written. **Watch this: the archive loop moves anything in the inbox, including a file that arrived after preingest.** Written as **2 source pages + 2 hubs** (the rows split cleanly into HTR and Monte Carlo). Archived to egress. **Zero clones. Nothing vendored.**
- **POSTURE CHANGE — Atto HTR.** The operator directive: *do not stay on Transkribus by precedent; if there is a better solution, adopt it.* Recorded. Across every prior wave this wiki carried "Transkribus stays the only product HTR". **Transkribus is now the incumbent with a challenger, not the fixed answer.**
- **The challenger is `mittagessen/kraken`.** Apache-2.0, 1,079 stars, last push 2026-09-24, a real engine (layout analysis, reading order, recognition), **CPU-capable, no GPU needed**, ~16 MB per model. Its partner model **CATMuS Medieval** names **Latin, Old French, Middle French, Old Spanish, and Italian** — the first released historical-script model in any wave to name Italian. 160k+ training lines, CC-BY-4.0.
- **Two blockers, both real.** (1) CATMuS is medieval bookscript; our records are 19th-century Italian cursive, so domain fine-tuning is required and **no off-the-shelf Kraken model exists for Italian civil registers**. (2) **No direct Kraken-versus-Transkribus head-to-head CER was found** — the two relevant papers sit behind a publisher anti-bot block. **Close that gap first.**
- **Accuracy evidence located:** Kraken on medieval French reports 6.0% line CER, 15.2% unseen, against 15.3% for a TrOCR+LoRA baseline. CATMuS-Medieval on unseen 17th-c Spanish/Hokkien reports about 10.0-11.4% CER against about 7.7-8.1% for PyLaia.
- **A real docx error caught.** The eval rated `githubharald/HTRPipeline` **Integrate** and claimed **MIT**. The live API returns **`spdx_id: null` — no licence at all**, all rights reserved, stale since July 2023. **It recommended vendoring an unlicensed repo.** This is the narrow case where the licence check still earns its place; it is not a reason to resume the full sweep.
- **Did not qualify:** SimpleHTR (MIT but English IAM toy), PreprocessingHTR (preprocessing only, no model), cremma-medieval (Old French, no Latin or Italian). Three of eight rows have no licence at all.
- **CEMINIDFS — this wave DOES apply.** Answering the operator's question directly. `nchopin/particles` (Extract) is a particle-filtering framework whose stated use is converting **static pre-game projections into dynamic state-space distributions that update on live drive results, snap counts, and game scripts** — that is the late-swap gap. `neurotrader888/mcpt` (Extract) is Monte Carlo permutation testing for overfitting, which applies to any strategy we test including DFS projection models. Prior K279/K280 rows had no DFS extract; these two do.
- **Honest note for future waves:** K279 and K280 carried 40 eval rows between them. The first 20 had no DFS item; the two real ones were in the second 20. When a batch has DFS-shaped rows but no extract, record **what class of thing would have qualified**, so the next wave has a target.
- **Concepts:** 2 k280 hubs (atto-htr, dfs, ood — see index). K279 hubs backlinked both ways.
- **Phase-0:** the audit agent cloned nothing (session network policy blocked git and gh directly); findings come from the live GitHub REST API and cited publisher records. **No clone. 0 product Integrate GO** — with an open evaluation, not a closed one.
- **Next actions (not done):**
  1. **Atto: run the head-to-head.** Transkribus against Kraken+CATMuS on the same pages, same ground truth, line CER each. This number decides the HTR question.
  2. If Kraken is within a few points before fine-tuning, label a few thousand lines from one comune and fine-tune CATMuS.
  3. CeminiDFS: evaluate particle filtering for the late-swap lane. High complexity; build only if that lane carries the margin.
  4. CeminiDFS and XSP: add a permutation test for overfitting.
  5. No clone. Nothing vendored. A human types the ticket.

## [2026-10-03] ingest | K279 wave

- **Operator directive (this wave and forward):** stop auditing licenses row by row; extract the technique. The judgement is now "what is usable", not what the SPDX field says. This did not cost anything in practice — the useful rows in both eval docs were technique, not code. **One exception kept:** anything vendored verbatim into shipped product code still gets a licence note, because that lands on the buyer's diligence, not on us.
- **Inbox:** 11 sources written (5 arXiv + 2 eval docx + 4 newsletter/substack). **11/11 archived** to `cemini-egress-fi:/opt/cemini-bulk/research/osint/`. Inbox is empty. Zero clones.
- **Preingest false positive:** the checker flagged a Latent Space item as DUPLICATE on **title alone**. Latent Space recycles "[AINews] not much happened today" for every slow news day, colliding with the June 30 and July 2 pages. It is **not** a duplicate; the content is new. **Fix the checker: match a recurring-title feed on URL or date, not title.**
- **Harness (strongest finding of the wave):** an enterprise process-evaluation pipeline found that of **175 runs passing every final numerical check, 162 (92.6%) still had at least one process deviation**; overall 227 of 240 runs failed at least one check (2610.01833). Separately, a coding-agent plugin review found **116 of 262 reported decisions (44.3%) were absent from the agent's own report** (2610.01769). A clinical audit found models failed to keep the middle "partially supported" label in **83.3% to 100%** of deserving cases while posting high safety scores — label collapse inflating a safety metric (2610.01497). PACE shows a safe tool variant and a leaking variant produce **identical admission evidence**, so admission review is not enforcement (2610.01349). TRACE contributes discounted-return credit assignment (2610.01323).
- **DFS / Parlays — two techniques worth building.** (1) A **pick'em breakeven table**: a fixed-multiplier card is a payout structure, not a price, so it needs the breakeven hit rate per card size (2-pick to 6-pick), per flex variant, and per platform settlement rule. (2) **Property-based testing of the de-vig and copula maths** — assert that de-vigged probabilities sum to 1.0, that the Gaussian copula joint sits between the product of marginals and the minimum marginal, and that any correlation matrix is positive semi-definite. This is where a silent numerical bug becomes a mispriced ticket. Two repos were Pass for the same reason: a naive score-regression model cannot beat a market-implied closing line. That is a standing argument for keeping the stack on de-vigged market lines.
- **Security:** the TeamCity flaw story is ransomware-relevant because a CI/CD server holds trusted access to repos, agents, credentials, artefacts, and deploy targets. The step teams skip is **credential rotation** — patching without rotating leaves the attacker's access intact. **No PoC. No exploit steps. No payloads.**
- **PM / crypto:** Kalshi reported in a roughly $1B round at about a **$40B valuation**. Ethereum 2030 roadmap, SEC and ESMA rulemaking, institutional tokenised-deposit launches. **No level to arm.**
- **Concepts:** 6 k279 hubs (harness, dfs-parlays, security, gambling-pm, ood-stub). Matching k278 hubs backlinked both ways; `updated:` bumped to 2026-10-03. `harness_verb: FILE`. `wire_status: policy_wired`.
- **Phase-0:** clones nothing. **No installs. 0 product Integrate GO.**
- **Routing:** DFS — the breakeven table and the property tests. Parlays — same, plus no automated board scraping. CCC — process-level evaluation, the self-report gap, and the admission-vs-enforcement split. Cyber — patch and rotate; **no PoC**. GW — **no level to arm**. **No xsp scp. No LIVE Discord.**
- **Rule:** `## OSINT K279 — 2026-10-03` inserted above `## OSINT K278` in `.cursor/rules/osint-phase1-adopt-wires.mdc`.
- **Briefs:** `briefs/2026-10-03_k279-*` (8). Sibling copies staged.
- **Next actions (not done):**
  1. CeminiParlays: build the pick'em breakeven table.
  2. CeminiParlays: add property-based tests over the de-vig and copula functions.
  3. Fix `preingest_check.py` to match recurring-title feeds on URL or date.
  4. Add a process-level check to our own gate: score the trajectory, not only the final output.
  5. No clone. No install. No auto-arm. A human still types the ticket.

## [2026-10-02] ingest | K278 wave

- **Inbox:** 13 sources written (8 arXiv + 1 eval docx + 2 latent-space + 2 substack). **13/13 archived** to `cemini-egress-fi:/opt/cemini-bulk/research/osint/`. Location fields name the egress path. Inbox is empty. No clone.
- **License check (the wave's headline):** the eval docx listed 20 repos. Every license was checked with `gh api` 2026-10-02. **Four docx claims failed**: sdcb/SimdPaddleOCR claimed "MIT via dependency chain" is **Apache-2.0**; mksglu/context-mode claimed ELv2 is **NOASSERTION**; getsentry/sentry claimed FSL-1.1 is **NOASSERTION**; cursor/plugins claimed MIT/Apache is **null**. Four repos were also size-skipped: impeccable 379 MB, hyperframes 488 MB, sentry 952 MB, three-gpu-pathtracer 954 MB. **Never trust eval SPDX.**
- **Harness:** VISTA is a mechanical harness with visual memory and no trained model; it took an open-weight model from 1.89 to 66.93 on ARC-AGI-3, and a frontier model to a perfect 100.00 relative human action efficiency in 7,302 actions against a human 17,135 (2610.02200). Image observations used 30.7M tokens against 71.9M for text grids. The coherence paper names a state failure class: when the deciding event was hidden, model accuracy was compatible with chance, and **one restoring sentence returned it to 40 of 40** (2610.02036). **A live budget counter did not stop overspend in 4 of 5 runs; commit enforcement did, 0 of 5.** Pi Durable externalises state (checkpoints, hot-swap, shared sync). An RLM interview is opinion, not measurement. **Do not swap `/route`.**
- **Atto:** PyPottery runs OCR then few-shot parsing on cursive archaeological records, at a 6.2% character error rate; parsing exact-match runs 13.56% at one example, 52.63% at three, 67.60% at ten (2610.02072). The 2023 genealogy DB paper measured that **19 of 210** business rules do not fit the schema, with a validated front end carrying 55 (2610.00633). **Transkribus stays the only product HTR.** No `truth.ged` merge. No Barone PII.
- **PM / macro:** a Kalshi-CBS News sponsorship drew criticism; Kalshi did about $2.065B on 30 September. A consumer survey reported **79% of prediction-market users lost money** in the past year. The forecasting paper reached soft-Brier 0.254 against 0.256 for a frontier model at 5% of cost, and its authors state plainly that **no scaffold reliably beats the market without non-public information** (2610.01955). Klement documents a p-hacked study: 10% significance, a break dated 1991 from the same data, then 5% after controls.
- **Vol quant:** a barrier-option expansion cuts mean absolute error from 0.09426 to 0.01248 on a 21-strike CEV case (2610.00340); an American-option SCLV solver runs in about 35 seconds against 639 seconds for a benchmark (2610.01187). **No trade. No sizing change.**
- **Security:** KaliBench reports that tool selection resolves with hints (72.0% to 95.2%) while argument construction is the bottleneck; an 8B tuned model reaches a 79.2 average total score (2610.02206). The reusable idea is the runtime-free verifiable reward. **No PoC. No exploit steps. No command list.**
- **Concepts:** 6 k278 hubs (harness, vol-quant, atto-htr, gambling-pm, security, ood-stub). Matching k277 hubs backlinked both ways; `updated:` bumped to 2026-10-02. `harness_verb: FILE`. `wire_status: policy_wired`.
- **Phase-0:** clones nothing. **No product install. 0 product Integrate GO.**
- **Routing:** Atto — PyPottery few-shot curve and the constraint split; **no HTR swap**. GW — **no level to arm**. DFS — no DFS extract. Parlays — the survey harm figure is context; **no submit**. CCC — the harness owns state; visibility is not enforcement; **do not swap `/route`**. Cyber — KaliBench scoring design; **no PoC**. Gambling — sponsorship and harm figures; **no pm scp**. SEO — nothing this wave. **No xsp scp. No LIVE Discord.**
- **Rule:** `## OSINT K278 — 2026-10-02` inserted above `## OSINT K277` in `.cursor/rules/osint-phase1-adopt-wires.mdc`. **FILE and HITL only.**
- **Briefs:** `briefs/2026-10-02_k278-*` (8: atto, guruwatcher, ceminidfs, ceminiparlays, ccc-harness, cyber-lab, gambling, seo). Sibling copies staged.
- **Index / ROADMAP / hot.md:** K278 sections added above K277.
- **gate:** `adopt_k278_phase0.sh` + `adopt_k278_phase1.sh` (no commit).
- **Next actions (not done):**
  1. Check state ownership before blaming a model when every step looks locally correct.
  2. Add a commit-enforcement gate, not a visible counter, for any shared budget.
  3. Atto: use the PyPottery few-shot curve (about 10 examples) to scope any parsing work.
  4. Borrow the runtime-free verifiable reward design for our own tool-invocation gates.
  5. No clone. No HTR swap. No auto-arm. A human still types the ticket.

## [2026-10-01] ops | DeepSeek model repoint

- DeepSeek retired the model id `deepseek-v4-flash` on 2026-09-10 and phased out `deepseek-v4-pro` on 2026-09-14. Both aliases now serve **V4.1-Flash**, whose API id is `deepseek-flash`.
- The gateway had pinned both old ids since 2026-09-30, so both picker entries served the same model while the labels read "V4 Flash" and "V4 Pro".
- Repointed `~/.local/bin/cemini-deepseek-anthropic-proxy.py` so every route maps to `deepseek-flash`. The picker was then cut to **one entry**, "DeepSeek V4.1 Flash"; the `claude-sonnet-4-5` route stays routable so a stale selection still resolves. The LaunchAgent was restarted.
- Repointed `DEEPSEEK_MODEL=deepseek-flash` in `~/.cemini/llm-routing.env`. Backup: `llm-routing.env.bak-20261001`.
- `CLAUDE.md` window override and `~/.claude/skills/route/SKILL.md` updated. The route skill no longer claims a Pro tier.
- Verify: the model list returns one entry; `claude-haiku-4-5` and `claude-sonnet-4-5` both returned `"model":"deepseek-flash"` through `http://127.0.0.1:8791`. `deepseek-flash` returned HTTP 200 on `api.deepseek.com/anthropic` before the change.
- Carry forward risk: `deepseek-flash` is a moving alias. The model behind it can change inside the window without notice.

## [2026-10-01] ingest | K277 wave

- **Inbox:** 15 sources written (8 arXiv + 2 latent-space + 1 tl;dr sec + 1 Sterling stub + 3 substack). **15/15 archived** to `cemini-egress-fi:/opt/cemini-bulk/research/osint/`. Location fields name the egress path. Inbox is empty. No clone.
- **Harness:** the minimal-harness paper found the coding environment is the single largest effect and that search, autonomy, and multi-agent scaffolding added nothing significant under an equal budget (2609.40303); self-selection trailed an oracle by 6.832 percentage points; DynaHarness admits a revision only after a paired regression check (2609.40306); Turbo Harness edits the harness per instance from a playbook (2609.40330); ScholarEvolve evolves it from the literature (2609.40169); Cogentic runs adversarial verifiers over drafts and keeps a ledger of only-confirmed work (2609.40324). **Never auto-evolve skills or rules from a paper. Do not swap `/route`.**
- **Verifier theme (three appearances):** a summary is not the document. Klement reports agent summaries flipped a buy or sell call in one case in four to one in three (2026-10-01). PageBreak validates a suspected bug against a running environment before it reports. This repeats the K276 trace-validity finding.
- **Security:** CodeMimicry names safety generalization lag, a code-domain blind spot where prompt-level guards left 76% to 100% residual success while hidden-layer interventions cut it to 4% to 14% (2609.39902). Threat class and mitigation table only. **No PoC.** A reported hidden-reasoning extraction campaign is a headline.
- **Atto:** decentralized document analysis reports handwriting transfer improving by a best case of x1.62 when separate archives are trained apart and merged, against pooled training (2609.39684). Method candidate for a future M-phase. **Transkribus stays the only product HTR.** No `truth.ged` merge. No Barone PII.
- **Vol quant:** stochastic Knothe-Rosenblatt calibration at 0.273s against 25.778s for a standard SLV calibration, with close prices (2609.39256). **No trade. No sizing change.**
- **PM / crypto:** Polymarket launched self-exclusion and deposit limits, and partnered with a national telehealth provider. Polymarket raised at a $21B post-money valuation; Kalshi is reported raising toward $40B. Crypto VC funding rose 71.1% month over month to about $1.269B. **No level to arm. Never auto-arm. No pm scp.**
- **SEO:** one Sterling Sky capture arrived as a truncated teaser, so it is a title and a URL only. **No ranking recipe.**
- **Concepts:** 6 k277 hubs (harness-evolution, security, vol-quant, atto-htr, gambling-pm, ood-stub). Matching k276 hubs backlinked both ways; `updated:` bumped to 2026-10-01. `harness_verb: FILE`. `wire_status: policy_wired`.
- **Phase-0:** clones nothing. Three repo URLs checked with `gh api` 2026-10-01: turbo-harness MIT 7783 KB; **ScholarEvolve SPDX null**; **CodeMimicry SPDX null**. **No product install. 0 product Integrate GO.**
- **Routing:** Atto — merged-archive method signal; **no HTR swap**. GW — **no level to arm**; **never auto-arm**. DFS — no DFS extract. Parlays — no new method; **no submit**. CCC — keep the paired regression gate and the adversarial-verifier split; **do not swap `/route`**. Cyber — code-domain safety lag; **no PoC**. Gambling — venue maturity and capital; **no pm scp**. SEO — title and URL. **No xsp scp. No LIVE Discord.**
- **Rule:** `## OSINT K277 — 2026-10-01` inserted above `## OSINT K276` in `.cursor/rules/osint-phase1-adopt-wires.mdc`. **FILE and HITL only.**
- **Briefs:** `briefs/2026-10-01_k277-*` (8: atto, guruwatcher, ceminidfs, ceminiparlays, ccc-harness, cyber-lab, gambling, seo). Sibling copies staged in Atto, GuruWatcher, CeminiDFS, CeminiParlays, CCC, cybersecurity, gambling, and SEO.
- **Index / ROADMAP / hot.md:** K277 sections added above K276.
- **gate:** `adopt_k277_phase0.sh` + `adopt_k277_phase1.sh` (no commit).
- **Next actions (not done):**
  1. Check the execution environment before adding harness machinery. It carried the largest measured effect.
  2. Add a summary-fidelity check: a summary is not the document. Score the source, not the summary.
  3. Keep the paired regression gate on any self-revision, and keep only confirmed work in the ledger.
  4. Atto: evaluate merged small-archive training for a future M-phase.
  5. No clone. No HTR swap. No auto-arm. A human still types the ticket.

## [2026-09-30] wire | K276 trace-validity gate

- Added the `trace_recheck` key to `scripts/harness_eval_checklist.py` (K334 harness eval gate). The gate now has six keys; all must be true for SHIP.
- `.cursor/skills/harness-eval-gate/SKILL.md` records the rule and the numbers from arXiv 2609.38107. Rule: score the re-run, not the trace.
- Source: @sources/arxiv-2609.38107-invalid-traces-2026-09-30.md.
- Verify: `python3 scripts/harness_eval_checklist.py selftest` (2 pass, 0 fail). The new key forces HOLD when false.
- Archive check: all 38 K276 raw files are on `cemini-egress-fi:/opt/cemini-bulk/research/osint/` (16/16 arXiv PDFs confirmed). Inbox empty.

## [2026-09-30] ops | Claude desktop DeepSeek window

- Cursor quota is out until about 2026-10-14. The orchestrator for that window is Claude desktop in 3p mode on DeepSeek `deepseek-v4-flash`.
- Gateway base is `https://api.deepseek.com/anthropic`. Backup model is `deepseek-v4-pro`.
- Desktop MCP entries `stash`, `ssh-prod`, and `ssh-librarian` are removed. Project MCP starts `lazy-tool` only. Definitions in `.mcp.json` stay.
- Claude `/route` is `~/.claude/skills/route/SKILL.md`. The Cursor skill file is unchanged.
- Exa plugin 3.3.8 is enabled on the main Claude config by a symlink to the existing cache.
- Claude Desktop 2.110 dropped raw `deepseek-*` ids, so the picker was empty. A local proxy on `127.0.0.1:8791` rewrites `claude-haiku-4-5` to `deepseek-v4-flash` and `claude-sonnet-4-5` to `deepseek-v4-pro`. Picker labels are DeepSeek V4 Flash and DeepSeek V4 Pro.
- Operator step left: quit Claude with Cmd-Q, reopen Claude.app, and confirm those two labels.

## [2026-09-30] ingest | K276 wave

- **Inbox:** 38 sources written (16 arXiv + 6 newsletter + 8 substack + 8 Sterling stubs). **38/38 archived** to `cemini-egress-fi:/opt/cemini-bulk/research/osint/`. Location fields name the egress path. Local copies removed. Inbox is empty. No clone.
- **Harness (strongest cluster so far):** harness learning trains a proposer to rewrite its harness (2609.35738); correct answers carry invalid traces, 31.6% on the hardest instances, over half passing arithmetic checks but failing a dependency check (2609.38107); most runs lose the declared plan under a generic loop, while pattern executors lift ALFWorld 0.48 to 0.92 (2609.38108); meta-skills lift a Builder by 8.95 points (2609.38143); meta-reasoning bounds the controller context (2609.38147); Game Arena resists benchmark saturation (2609.31473). **Do not swap `/route`. No skill install. Never auto-evolve.**
- **HTR (Atto):** pixel-reconstruction pretraining wins on Latin historical sets, 4.5% against TrOCR-B 4.7%, no released weights (2609.35473); few-shot VLM transcription reaches 5.36% on IAM, about 18-21% on historical sets (2609.37195); per-task error budgets run 3% to 20%, and retraining on noisy text removes the collapse above 15% error (2609.37755). **Transkribus stays the only product HTR.**
- **Vol quant:** a finance-informed carrier in the representation, not the loss (2609.33213); a Greek penalty in the training loss (2609.33767); price impact shifts the effective strike to K minus lambda-N and the hedger's own trading moved 9 of 1,000 simulated paths into the money (2609.36257); Dyson-Schwinger closure matches PDE references and gives bucketed vega at about 70-80x lower cost, model-to-model only (2609.37741). **No trade. No sizing change.**
- **PM / macro:** Event Horizon argues the CFTC can reach offshore venues; Kalshi set a record daily volume near $3.04B. One claim for the ledger: the Kalshi Anthropic-IPO-announcement market near 54% before 1 December. Klement on passive flow pressure and on tax-driven creative destruction. Capital Flows is a paywalled teaser. **No level to arm. Never auto-arm. Never `watches.json`. No pm scp.**
- **Cyber:** the Bitget hack headline, about $387.5M on 24 September, with the reported failure in a signing path that trusted manipulated transaction data. **No exploit steps. No address list. No PoC.**
- **SEO:** eight Sterling Sky titles and URLs. Two are test reports: the local-pack URL test and the review-posting-block data. **No ranking recipe.**
- **Concepts:** 6 k276 hubs (harness-evolution, vol-quant, newsletter-macro, gambling-pm, ood-stub, atto-htr). Matching k275 hubs backlinked both ways; `updated:` bumped to 2026-09-30. `harness_verb: FILE`. `wire_status: policy_wired`.
- **Phase-0:** clones nothing. Five repo URLs checked with `gh api` 2026-09-30: game_arena Apache-2.0 8494 KB; igsm-trace-validity MIT 95 KB; MetaSkill-AI4AI **SPDX null** 466 KB; good_enough_papyrus_htr MIT 23 KB; resight-smc MIT 954 KB. **No product install. 0 product Integrate GO.**
- **Routing:** Atto — error-budget rule and few-shot signal; **no HTR swap**. GW — **no level to arm**; **never auto-arm**. DFS — no DFS extract; the seal order is a process note. Parlays — Kalshi volume mix is context; **no submit**. CCC — trace-validity gate, declare-then-route pattern; **do not swap `/route`**. Cyber — two defender notes; no PoC. Gambling — regulation and volumes; **no pm scp**. SEO — titles and URLs. **No xsp scp. No LIVE Discord.**
- **Rule:** `## OSINT K276 — 2026-09-30` inserted above `## OSINT K275` in `.cursor/rules/osint-phase1-adopt-wires.mdc`. **FILE and HITL only.**
- **Briefs:** `briefs/2026-09-30_k276-*` (8: atto, guruwatcher, ceminidfs, ceminiparlays, ccc-harness, cyber-lab, gambling, seo). Sibling copies staged in Atto, GuruWatcher, CeminiDFS, CeminiParlays, CCC, cybersecurity, gambling, and SEO brief dirs.
- **Index / ROADMAP / hot.md:** K276 sections added above K275.
- **gate:** `adopt_k276_phase0.sh` + `adopt_k276_phase1.sh` (no commit).
- **Next actions (not done):**
  1. Add a trace-validity check to the harness gate: re-run the check, do not read the trace.
  2. Atto: write a per-task acceptable error band before choosing a transcription source.
  3. Atto: keep the few-shot VLM path as an option for one-off hands only.
  4. CeminiDFS: keep the freeze-bank-then-label seal order for slate validation.
  5. No clone. No HTR swap. No auto-arm. A human still types the ticket.

## [2026-09-28] ingest | K275 wave

- **Inbox:** 16 new source pages plus a VOYG RSS fold into the 27 Sep page. Phase-0 clones nothing. gh api 2026-09-28 overrides the docx. Page-diff Integrate line overridden on size. **0 product Integrate GO.**
- **Papers:** DynBranch names a branch-resolution barrier. Commit authority stays outside the agent. Option factors are not a trade. Rough-vol posterior is a note. PIA is not Atto. Robot map, voice platform, and checklist-label paper are headlines.
- **Newsletters:** Apricitas, KfW survey, Moontower 329 / soulcraft / Taylor URL, WuBlock calendar with no level, Event Horizon episode 34 headlines. No auto-trade. No pm scp.
- **Concepts:** 5 k275 hubs. Matching k274 hubs backlinked. `harness_verb: FILE`. `wire_status: policy_wired`.
- **Next actions (not done):** do not install the page-diff app; do not arm a URL watch; do not swap `/route`; option factors are not a coefficient; no Public auto-trade agent; WuBlock calendar is not a level. K274 projection actions stay open.

## [2026-09-27] ingest | K274 wave

- **Inbox:** 6 sources written (2 eval docx + 1 discussion PDF + 3 substack). **6/6 archived** to `cemini-egress-fi:/opt/cemini-bulk/research/osint/`. Size check passed. Local copies removed. Inbox is empty. Location fields name the egress path. No clone.
- **Sources:** Sports analytics eval (sha256 `dcfb4e35…`). gh api 2026-09-27 overrides the docx. A null SPDX still records the pattern. Pattern: partitioned parquet as our own artifact. World Cup scorer is a name only. NFL data eval (sha256 `8b5ba323…`). CSOE name. Wind penalty. Closing lines. nflverse Integrate is overridden. VOYG discussion (sha256 `01a3ba35…`). Not advice. CFTC Rule 4.41. Cite only the June 2025 sale at $31, the 23 September 2026 convert print at $31.40, June quarter gross profit of $4.5 million, operating loss of $51.4 million, and Starlab sales of zero. No trade. Glitch new week is title and URL only (sha256 `e2640718…`). No strike prices. It stays off the September 8 page. WuBlock 2026-09-26 headlines (sha256 `43a53d74…`). New York sued Polymarket. Magic Eden headline only. No exploit steps. WuBlock 2026-09-27 Asia top 10 headlines (sha256 `0ff55d35…`). No level to arm.
- **Concepts:** 5 k274-* hubs (harness-evolution, vol-quant, newsletter-macro, gambling-pm, ood-stub). Matching k273 hubs backlinked both ways; `updated:` bumped to 2026-09-27. `harness_verb: FILE`. `wire_status: policy_wired`. Sports extracts live on the gambling hub. Game-sim and StatsBomb names live on the ood hub. The macro hub says this wave has no level to arm.
- **Phase-0:** clones nothing. Skip list covers the sports rows. A null SPDX still records the pattern. **No product install. 0 product Integrate GO.** `.local/adopts/cfbfastR-cfb-data`, `.local/adopts/cfbfastR-data`, `.local/adopts/nfl-closing-speed-csoe`, `.local/adopts/nfldata`, and `.local/adopts/nfl-betting-data` stay absent.
- **Routing:** Atto — this wave is not genealogy; Transkribus stays the only product HTR. GW — **no level to arm**; **never auto-arm**; do not copy Glitch strikes. DFS — parquet, CSOE name, and wind penalty; no live order; no clone. Parlays — closing-line calibration and wind on totals; a human types the ticket; **no submit**. CCC — **do not swap `/route`**; no skill install. Cyber — WuBlock headlines only; no exploit steps. Gambling — same sports patterns; **no pm scp**; World Cup scorer is a name; do not revive world-cup-bot. SEO — no ranking recipe. **No xsp scp. No LIVE Discord.**
- **Rule:** `## OSINT K274 — 2026-09-27` inserted above `## OSINT K273` in `.cursor/rules/osint-phase1-adopt-wires.mdc`. **FILE and HITL only.**
- **Briefs:** `briefs/2026-09-27_k274-*` (8: atto, guruwatcher, ceminidfs, ceminiparlays, ccc-harness, cyber-lab, gambling, seo). `skill_audit.py` PASS on all eight. Sibling copies landed in Atto, GuruWatcher, CeminiDFS, CeminiParlays, CCC, cybersecurity, gambling, and SEO brief dirs.
- **Index / ROADMAP / hot.md:** K274 sections added above K273.
- **Archive:** 6/6 on egress-fi. Inbox empty.
- **gate:** `adopt_k274_phase0.sh` + `adopt_k274_phase1.sh` (no commit).
- **Next actions (not done):**
  1. CeminiDFS: publish our own projection artifacts as partitioned parquet. Do not download the college dump.
  2. CeminiDFS: add a closing-speed or separation adjustment in our own code. The upstream formula is unverified. Do not clone the 6704 KB MIT tree.
  3. CeminiDFS and CeminiParlays: apply a wind penalty to passing projections and game totals. Skip indoor and closed retractable games.
  4. CeminiParlays: keep a local table of historical closing spreads and totals for copula calibration. Do not clone nflverse/nfldata or nfl-betting-data.
  5. No odds scraper. No recruit scraper. No auto-submit. A human still types the Hard Rock or FanDuel ticket.

## [2026-09-26] ingest | K273 wave

- **Inbox:** 10 sources written (2 eval docx + 2 arXiv + 6 newsletter/substack). **10/10 archived** to `cemini-egress-fi:/opt/cemini-bulk/research/osint/`. Size check passed. Local copies removed. Inbox is empty. Location fields name the egress path. No clone.
- **Sources:** NFL DFS revenue eval (sha256 `0148b0cc…`). gh api 2026-09-26 overrides the docx. A null SPDX still records the pattern extract. Patterns: classic, showdown, and captain roster rules; two-way margin removal; de-juiced price versus a fixed pick'em multiplier; stadium weather discount; own score marginals; lineup exposure caps. dfsOptimizer is NOASSERTION and stays a pattern name. FanDuel has no public REST API on this row. Hard Rock and FanDuel stay a human ticket. Agent runtime eval (sha256 `ab41a7f0…`) uses the normal license gate. Zero clones. No skill install. arXiv 29167 IndicBankBench (**not genealogy, not Atto, not HTR**; strict pass3 is lower than at-least-once success; no lab steps). arXiv 29287 AEGIS (**one sentence**; aegis-audio-defense MIT 6618 KB; no clone). OpenRouter interview teaser (**do not change `/route`**). Three Sterling pages are title and URL only (filename dates stay 2026-09-24). SecEng Weekly is a headline only. SecPro #253 is a headline only. The target class is a CI/CD server (TeamCity). No intrusion steps.
- **Concepts:** 5 k273-* hubs (harness-evolution, vol-quant, newsletter-macro, gambling-pm, ood-stub). Matching k272 hubs backlinked both ways; `updated:` bumped to 2026-09-26. `harness_verb: FILE`. `wire_status: policy_wired`. Sports extracts live on the gambling hub. Bank bench and Sterling live on the ood hub. The macro hub says this wave has no level to arm.
- **Phase-0:** clones nothing. Skip list covers the sports rows and the agent-runtime SIZE-SKIP rows. **No product install. 0 product Integrate GO.** `.local/adopts/draftfast`, `.local/adopts/dfsOptimizer`, and `.local/adopts/aegis-audio-defense` stay absent.
- **Routing:** Atto — bank bench is not genealogy; AEGIS is not HTR; Transkribus stays the only product HTR. GW — **no level to arm**; **never auto-arm**. DFS — roster-rule and exposure extracts; no live order. Parlays — devig, pick'em gap, weather, own marginals; **no submit**. CCC — do not install the complexity skill; **do not swap `/route`**; AEGIS is a name and an impact. Cyber — TeamCity and AEGIS headlines only. Gambling — same parlay extracts; **no pm scp**. SEO — three Sterling titles and URLs only. **No xsp scp. No LIVE Discord.**
- **Rule:** `## OSINT K273 — 2026-09-26` inserted above `## OSINT K272` in `.cursor/rules/osint-phase1-adopt-wires.mdc`. **FILE and HITL only.**
- **Briefs:** `briefs/2026-09-26_k273-*` (8: atto, guruwatcher, ceminidfs, ceminiparlays, ccc-harness, cyber-lab, gambling, seo). `skill_audit.py` PASS on all eight. Sibling copies landed in Atto, GuruWatcher, CeminiDFS, CeminiParlays, CCC, cybersecurity, gambling, and SEO brief dirs.
- **Index / ROADMAP / hot.md:** K273 sections added above K272.
- **Archive:** 10/10 on egress-fi. Inbox empty.
- **gate:** `adopt_k273_phase0.sh` + `adopt_k273_phase1.sh` (no commit).
- **Next actions (not done):**
  1. CeminiDFS: add classic, showdown, and captain roster constraints in our own optimizer code.
  2. CeminiDFS: add a lineup exposure cap.
  3. CeminiParlays: compare a de-juiced price with a fixed pick'em multiplier.
  4. CeminiParlays: use own score marginals plus a weather discount for SGP. A human still types the Hard Rock or FanDuel ticket.
  5. No auto-submit. No clone of the large sports trees.

## [2026-09-25] deep-read | K272 deep-read

- **Papers deep-read (7):** arXiv 29016 EvoTreeNAD (neural-architecture search, not genealogy, not HTR); 29035 bounded coalescent (statistical population-size inference, not Atto, no lab steps); 29333 LLM graders (exam graders, preamble failure mode recorded, no prompt recipe); 29964 World Action Agent (robot VLM harness, not a product); 30012 behavior assays (cheap cross-vendor behavior studies, no clone, modelun SIZE-SKIP); 30219 verified commissioning (external gate holds release authority, do not rewrite Verify); 30249 RAPID (robot programs from one demonstration, not a product).
- **Eval page:** moved from skimmed to read; gh api table noted as verified content; docx on egress.
- **Newsletters (10):** LS foundries vs navigators deep-read; LS future deep-read; LS WorldPrompt deep-read (no local image-gen install); PE Pulse paywall teaser-only; Capital Flows rates paywall teaser-only (no level to arm); EH Kalshi Curry deep-read (no pm scp, no submit); Klement artist deep-read (not advice); WuBlock Bitget deep-read (public loss figure, containment only); WuBlock Vitalik deep-read (not advice); WuBlock weekly deep-read (Bitget figure stays TENTATIVE).
- **Hold pages (3, unchanged, still skimmed):** arXiv 30266 trace tamper; Sterling Sky GMB suspension; tl;dr sec #347.
- **Hubs:** Harness hub now records the grader MAE.
- **Index:** seven paper rows updated from draft to validated.

## [2026-09-25] ingest | K272 wave

- **Inbox:** 21 sources written (1 eval docx + 8 arXiv + 12 newsletter/substack). No skip file in this inbox set. **21/21 archived** to `cemini-egress-fi:/opt/cemini-bulk/research/osint/`. Size check passed. Local copies removed. Inbox is empty. Location fields name the egress path.
- **Sources:** GitHub revenue eval (sha256 `c8d46938…`). gh api 2026-09-25 overrides the docx. Zero clones. arXiv 29016 EvoTreeNAD (**not genealogy, not civil records, not HTR**); 29035 bounded coalescent (**not Atto**; phylodyn SPDX null; boundedcoal 404; no lab steps); 29333 LLM graders (a short preamble can push graders out of band; graders repo **404**); 29964 World Action Agent (not a product); 30012 behavior assays (coding-atlas SPDX null; modelun **MIT 21956 KB SIZE-SKIP**); 30219 verified commissioning (external gate holds release authority; do not rewrite Verify); 30249 RAPID (not a product); 30266 trace paper (**one sentence**; independent log; deletion not described). Newsletters: LS foundries vs navigators FILE; LS future publication note (**do not change `/route`**); LS WorldPrompt **[TENTATIVE]** (no image-gen install); PE Pulse FILE; Sterling Sky **title and URL only**; tl;dr sec #347 **headlines only**; Capital Flows rates (**no level to arm**); EH Kalshi Curry (**no pm scp, no submit**); Klement artist opinion (**no sizing change**); WuBlock Bitget public figure about $351.6 million plus a containment claim (**no transfer method**); WuBlock Vitalik speech (**not advice, never auto-arm**); WuBlock weekly news list (Bitget figure **[TENTATIVE]**).
- **Concepts:** 5 k272-* hubs (harness-evolution, vol-quant, newsletter-macro, gambling-pm, ood-stub). Matching k271 hubs backlinked both ways; `updated:` bumped to 2026-09-25. `harness_verb: FILE`. `wire_status: policy_wired`.
- **Entities:** modelun license is now **MIT**. The 2026-09-23 SPDX-null field is retracted. Size 21956 KB still blocks the clone. **`wont_wire` stays.** No new clone directory.
- **Phase-0:** clones nothing. Skip list includes Search, hindsight, univer, starnet, wifit3, wifite2, kubernetes-the-hard-way, tick-stock-panel, impeccable, openbao, TikTok downloaders, media pipelines, TikTok-Unlock, Zefoy automator, TikTok-ViewBot, phylodyn, boundedcoal, graders 404, coding-atlas, modelun. **No product install. 0 product Integrate GO.** Wireless-tool URL class and engagement-automation URL class: no steps.
- **Routing:** Atto — EvoTreeNAD is not genealogy; phylodynamic is not Atto; Transkribus stays the only product HTR. GW — **no level to arm**; Bitget figure is a news claim. DFS — thin FILE; no live orders. Parlays — Kalshi Curry news, **no submit**. CCC — external gate; independent trace log; **do not install a browser**; **do not swap `/route`**; never auto-evolve skills. Cyber — headlines only; no procedure. Gambling — Kalshi note; **no pm scp**. SEO — Sterling title and URL only. **Live jev path unchanged. No xsp scp. No LIVE Discord.**
- **Rule:** `## OSINT K272 — 2026-09-25` inserted above `## OSINT K271` in `.cursor/rules/osint-phase1-adopt-wires.mdc`. **FILE and HITL only.**
- **Briefs:** `briefs/2026-09-25_k272-*` (8: atto, guruwatcher, ceminidfs, ceminiparlays, ccc-harness, cyber-lab, gambling, seo). `skill_audit.py` PASS on all eight. Sibling copies landed in Atto, GuruWatcher, CeminiDFS, CeminiParlays, CCC, cybersecurity, gambling, and SEO brief dirs. Further implementation: none.
- **Index / ROADMAP / hot.md:** K272 sections added above K271.
- **Archive:** 21/21 on egress-fi. Inbox empty.
- **gate:** `adopt_k272_phase0.sh` + `adopt_k272_phase1.sh` (no commit).

## [2026-09-24] archive | inbox to egress-fi

- **49/49** inbox files copied to `cemini-egress-fi:/opt/cemini-bulk/research/osint/`. Size check passed. Local copies removed. Inbox has no files left.
- Includes the K270 set, the K271 remainder, the Sterling Sky batch, duplicate re-copies, and the Jev PDF.
- Source `Location` fields for those pages now name the egress-fi path.

## [2026-09-24] ingest | K271 wave

- **Inbox:** 13 sources written (1 eval docx + 8 arXiv + 4 newsletter/substack). **Skipped source pages:** Jev Trading Research Paper.pdf (K268); Multi-Repo Revenue Evaluation Plan.docx (duplicate); arXiv 25447–26781 (K270); Opus 5.5; biosecurity; SparkToro; SecPro 252; WuBlock bStocks; KOSPI; CFTC; who-forecasts; Appleton; Windows; John Platt; Sterling Sky batch (K270). Skip files stay in the inbox.
- **Sources:** Multi-wiki URL eval (sha256 `97dcc91a…`, do not fold with the 2026-09-22 eval). arXiv 27138 commodity surface; 27542 control-token (**name and impact only** — no reproduction); 27606 state-grounded conditioning; 27612 RegenHarness; 27620 InGuard (**name and impact only**); 27639 echo chambers (GitHub **404**); 27717 SkillGym (**SIZE-SKIP**); 27720 CoRelNav. Newsletters: LS Muse glasses (**TENTATIVE**); EH World Cup broadcasts (~0.9 prediction-market logos per minute); Klement AI-debt opinion; Klement acquisitions (Fillat and Garetto — valuation premium is not a trade signal).
- **Concepts:** 5 k271-* hubs (harness-evolution, vol-quant, newsletter-macro, gambling-pm, ood-stub). Matching k270 hubs backlinked both ways; `updated:` bumped to 2026-09-24.
- **Entities:** jev-curate **MIT REFERENCE** clone `.local/adopts/jev-curate` (504 KB, depth 1, dataset sifter, `wont_wire`, not genealogy, not HTR, no vault data); Canny **MIT REFERENCE** clone `.local/adopts/canny` (266 KB, depth 1, evidence gate, `wont_wire`, do not install hooks).
- **Phase-0:** two REFERENCE clones only. NO-CLONE list includes hindsight, univer, Model-Optimizer, harness-sdk, jev-chat-jarvis, treg, google/ax, axe, learn-harness-engineering, ai-memory, apple-corelocation, agent-desktop, typesafe-mario, jev-drone, OneVOneJev, neo4jev (prior FILE), killmyidea, FluidUse (already SIZE-SKIP), deleting-the-trace, SkillGym, InGuard, Echo-Chamber 404. **No weight download. No product install. 0 product Integrate GO.**
- **Routing:** Atto — jev-curate is not genealogy and not HTR. GW — Klement notes have **no level to arm**. DFS — thin FILE. Parlays — broadcast study, **no submit**. CCC — do not install Canny; **do not swap `/route`**; never auto-evolve skills. Cyber — control-token paper is a name and an impact. Gambling — World Cup logo study; **no pm scp**; world-cup bot stays retired. SEO — no new SEO item. **Live jev path unchanged. No xsp scp. No LIVE Discord.**
- **Rule:** `## OSINT K271 — 2026-09-24` inserted above `## OSINT K270` in `.cursor/rules/osint-phase1-adopt-wires.mdc`. **FILE and HITL only.**
- **Briefs:** `briefs/2026-09-24_k271-*` (8: atto, guruwatcher, ceminidfs, ceminiparlays, ccc-harness, cyber-lab, gambling, seo). `skill_audit.py` PASS on all eight. Sibling brief copies landed in Atto, GuruWatcher, CeminiDFS, CeminiParlays, CCC, cybersecurity, gambling, and SEO brief dirs.
- **Index / ROADMAP / hot.md:** K271 sections added above K270.
- **Archive:** one attempt succeeded. `substack-rss-klement-2026-09-24-ai-could-help-governments-cut-debt-but-unevenly.md` is at `cemini-egress-fi:/opt/cemini-bulk/research/osint/`. The archive script removed that local inbox copy. The other 12 new files stay in `research to be indexed/` with archive pending. The plan allowed one attempt. **Do not delete the skip files.**
- **gate:** `adopt_k271_phase0.sh` + `adopt_k271_phase1.sh` (no commit).

## [2026-09-23] ingest | K270 wave

- **Inbox:** 19 sources written (8 arXiv PDF + 10 newsletter/substack + 1 Sterling Sky GBP batch page covering 14 posts). **Skipped source pages:** Jev Trading Research Paper.pdf (K268); capital-flows 2026-09-20 credit-fueled; glitchspx talon; secpro 252. Skip files stay in the inbox.
- **Sources:** arXiv 25447 conduct-under-pressure; 25518 matryoshka-attribution (**attribution method only** — no code release, finetune case study not described); 25686 task-state-influence; 26499 local-coding-agent-manipulation; 26606 option-rebate-design; 26760 grow-the-harness; 26779 cliffcompaction; 26781 agensh. Newsletters: LS John Platt; LS Opus 5.5 (**TENTATIVE**); LS bio-security (citation only — not Atto, not HTR); PE windows-ai; PE appleton (**LIKELY flag = shared sponsor URLs only**); SparkToro algorithms; Substack: Capital Flows KOSPI; EH CFTC mention markets; Klement who-forecasts (Thesmar/Verner); WuBlock bStocks; Sterling Sky GBP batch.
- **Concepts:** 5 k270-* hubs (harness-evolution, vol-quant, newsletter-macro, gambling-pm, ood-stub). Matching k269 hubs backlinked both ways; `updated:` bumped to 2026-09-23.
- **Entities:** cliffcompaction **MIT REFERENCE** clone `.local/adopts/cliffcompaction` (1005 KB, depth 1); modelun SPDX null ~21MB **NO-CLONE** `wont_wire`; agensh GitHub **404 on 2026-09-23** **NO-CLONE** `wont_wire`.
- **Phase-0:** one REFERENCE clone only. SKIP list includes modelun, agensh, airo-mono, pi, Kimi-K3. **No weight download. 0 product Integrate GO.**
- **Routing:** Atto unchanged (bio-security is not Atto). GW/KOSPI/who-forecasts/bStocks FILE; **no level to arm; never auto-arm; never watches.json**. DFS/Parlays FILE; CFTC staff advisory; **no pm scp**; no sizing change. CCC harness FILE; **do not swap `/route`**; never auto-evolve `.cursor/skills`. SEO SparkToro + Sterling FILE; no ranking claim. **No xsp scp. No LIVE Discord.**
- **Rule:** `## OSINT K270 — 2026-09-23` inserted above `## OSINT K269` in `.cursor/rules/osint-phase1-adopt-wires.mdc`. **FILE only.**
- **Briefs:** `briefs/2026-09-23_k270-*` (8: atto, guruwatcher, ceminidfs, ceminiparlays, ccc-harness, cyber-lab, gambling, seo).
- **Index / ROADMAP / hot.md:** K270 sections added above K269.
- **Archive:** **BLOCKED — SSH failed.** `ssh cemini-egress-fi` returned `Permission denied (publickey,password)` (exit 255) on 2026-09-23. No file was archived and no inbox file was deleted. Source page `Location` fields point at the local inbox until archive succeeds. Re-run `bash scripts/archive_raw_to_egress.sh --wiki-id osint "<file>"` for each new file with a source page once egress SSH auth is restored. **Do not delete the skip files.**
- **gate:** `wiki_lint.py` (no commit).

## [2026-09-22] wire | Jev workflow gates

- **Trial:** Redacted classify on live mcp-jev (jev-latest) — `jev_find` / `jev_verify` / `jev_screen`; catalog verify 0.53 stays HITL; screen blocked synthetic override targeting `watches.json`.
- **Rule:** `~/.cursor/rules/jev-workflow.mdc` (federation user-global; canon CCC). Confidence under 0.8 means a human decides. Never arm. Never vault PII. OSINT project copy removed so the rule does not load twice.
- **No harness-zero clone** (SIZE-SKIP unchanged).
- **No weight download** for open-jev-typed-decision-engine (`wont_wire` stays).

## [2026-09-22] ingest | K269 wave

- **Inbox:** 18 sources written (2 evals + 8 arXiv + NGI PDF + 7 newsletters). **Skipped source pages:** Jev Trading Research Paper.pdf (K268); capital-flows; glitchspx; secpro. **Do not re-clone** REFERENCE adopts.
- **Sources:** Multi-wiki URL eval + Repository eval (different hashes — do not fold); IV diffusion 22893; PROSE 23845; residualization 24194; InvestorNerd 24658; RRSI 24972; Harness-Zero 24974; onPanda 24983; VideoGen 24997; NGI Orbuch; LS Diogo System One; LS MiMo-V2.6; Sterling Sky GBP (empty RSS); EH free-bets; Klement chip ban; Moontower Kelly; WuBlock BTC historical.
- **Concepts:** 7 k269-* hubs (eval-github, harness-evolution, jev-system-one, vol-quant, newsletter-macro, gambling-pm, ood-stub). Prior hubs backlinked.
- **Entities:** jev-lexer, jev-test-filter, jev-search (MIT REFERENCE); open-jev-typed-decision-engine (Apache-2.0 REFERENCE); harness-zero (SIZE-SKIP NO-CLONE). **jev-mcp WIRE unchanged.**
- **Phase-0:** REFERENCE only — no re-clone. SIZE-SKIP harness-zero ~21MB. SKIP null licenses (jevify / djev-spark / Nemotron_Jev). **0 product Integrate GO.**
- **Routing:** Atto #1 organizer; open-jev-typed-decision-engine = redacted type only; Transkribus sole HTR; never auto-merge truth.ged. GW #2 macro FILE never auto-arm. CeminiDFS/Parlays FILE; no pm scp; Kelly education no sizing change. CCC RRSI/Harness-Zero/residualization FILE (do not swap `/route`; never auto-evolve skills). Cyber ai-ctf FILE no PoC. SEO Sterling brief only. **No xsp/pm scp. No LIVE Discord.**
- **Briefs:** `briefs/2026-09-22_k269-*` (8) + Jev briefs `### K269 add`.
- **Archive:** 18/18 new inbox files → egress-fi. Duplicates and the K268 Jev PDF stayed local.
- **gate:** `wiki_lint.py` (no commit).

## [2026-09-21] ocr | Jev Trading Research Paper

- **Route:** mid-lane `route-task` (Grok plan → OpenCode stalled → vision OCR completed in parent). PDF fetched from egress-fi; 8 pages rendered `.local/ocr/jev-pages/`.
- **Output:** `.local/ocr/jev-trading-research-paper.txt`; source page `read_status: read`; new hub `k268-jev-trading-wave` + entity `jev-trader` FILE (jarrodwatts/jev-trader MIT, no clone).
- **Posture:** TypeSafe System One HFT field report — FILE only. **0 Integrate GO. Never auto-arm. jev-mcp WIRE unchanged.**

## [2026-09-21] ingest | K268 wave

- **Inbox:** 18 files (9 PDF + 9 newsletters). Leftover SecPro skipped — already K265. Never trust filename `htr` without reading the abstract.
- **Sources:** Jev Trading Research Paper (image-only unread-stub); CRAFT FRB polarimetry 21177 (**NOT Atto HTR**); OU SV 21291; operator-splitting SV 21301; MIRAGE 21554; HMM equilibrium 21684; failing-robot-ask 21942; RecreationWorld 22000; CodeMidas 22068; Capital Flows; Event Horizon ep33; GlitchSPX Talon Sep21; Klement heating hammer; Moontower blindsided/end-behavior/328; Outlier parlay submit-screen; WuBlock weekly outlook.
- **Concepts:** 8 k268-* hubs (vol-quant, harness-evolution, ood-stub, game-dev, newsletter-macro, gambling-pm, xsp-signal, cybersec thin). Entities: `codemidas` + `recreationworld` FILE NO-CLONE.
- **Phase-0:** `adopt_k268_phase0.sh` — **no clones** (paper repos unverified). **0 product Integrate GO.**
- **Routing:** Atto #1 FRB trap + Transkribus sole HTR; organizer stays organizer. GW #2 macro FILE never auto-arm. CeminiDFS #3 thin FILE. CeminiParlays #4 Outlier/EH FILE no pm scp. CCC CodeMidas/MIRAGE/robot-ask FILE (do not swap `/route`). Cyber thin FILE no PoC. XSP GlitchSPX Talon FILE no xsp scp. Game-dev RecreationWorld FILE.
- **Briefs:** `briefs/2026-09-21_k268-*` + `briefs/xsp-k268-glitchspx-talon-sep21.md` + Jev briefs `### K268 add`.
- **Archive:** 18/18 mapped inbox → egress-fi (SecPro retained in inbox).
- **gate:** `ingest_session_gate.py` + `wiki_lint.py`.

## [2026-09-20] ingest | K267 wave

- **Inbox:** 3 NEW files (parent preingest). Leftover SecPro skipped — already K265. Extra inbox `Jev Trading Research Paper.pdf` not this wave. Never trust docx SPDX. Two evals are different hashes — do not fold.
- **Sources:** Multi-wiki eval SPDX overrides; repository eval SPDX overrides; WuBlock Asia TOP10 (BoJ +25 bp to 1.25%; HK tokenised bills; Jiangsu RWA illegal; MOEX BTC/ETH perps). NK device-theft row wiki FILE, no PoC.
- **Concepts:** 6 k267-* hubs. Entities: openjev-razorback, winnow, foreman, typesafe-mcp, pi-jev, jev-desktop. Bumps: jev-mcp **WIRE unchanged**, openjev FILE sibling note, jev-browser Liao FILE, tax-doc-classifier FILE, transkribus sole HTR.
- **Phase-0:** `adopt_k267_phase0.sh` — openjev-razorback Apache-2.0; winnow / foreman / typesafe-mcp / pi-jev / jev-desktop MIT. SKIP: SPDX-null / NOASSERTION / AGPL / GPL / SIZE-SKIP. Eval Integrate OVERRIDE FILE. **0 product Integrate GO.**
- **Routing:** Atto #1 organizer; do-the-work lures FILE/HITL (matrix on atto hub). Transkribus sole HTR. No unattended Antenati. No auto-merge truth.ged. GW #2 openjev-razorback + winnow FILE; never auto-arm; jev-trader out. CeminiDFS #3 thin FILE. CeminiParlays #4 thin FILE; no pm scp. CCC typesafe-mcp / pi-jev FILE (do not swap `/route`). Cyber FILE no PoC. **No xsp/pm scp.**
- **Briefs:** `briefs/2026-09-20_k267-*` + Jev briefs `### K267 add`. Sibling copies attempted.
- **Archive:** 3/3 NEW inbox → egress-fi.
- **gate:** `ingest_session_gate.py` + `wiki_lint.py`.

## [2026-09-20] phase-0 | K267

- **razorback16/openjev** — Apache-2.0 `[CONFIRMED]` gh api 2026-09-20; tiny GO REFERENCE FILE as `openjev-razorback`. Distinct from TheoLeeCJ MIT. FILE GW local extract. Never auto-arm.
- **GhalebDweikat/winnow** — MIT `[CONFIRMED]`; tiny GO REFERENCE FILE. GW newsletter prefilter. Never auto-arm.
- **thruwire/foreman** — MIT `[CONFIRMED]`; tiny GO REFERENCE FILE. Atto HITL FIND checklist. No auto-merge truth.ged.
- **itsmostafa/typesafe-mcp** — MIT `[CONFIRMED]`; tiny GO REFERENCE FILE. Eval Integrate OVERRIDE. **Never replace live mcp-jev. Never `npx github:`.**
- **y0usaf/pi-jev** — MIT `[CONFIRMED]`; tiny GO REFERENCE FILE CCC batched eval. Do not swap `/route`.
- **yikangy873-gif/jev-desktop** — MIT `[CONFIRMED]`; tiny GO REFERENCE FILE HITL only. No unattended parish DBs.
- **SKIP:** nimble SPDX-null; Heman10x NOASSERTION; laya-mlx FILE mention; Jev-cu SPDX-null; awesome lists; hermes-jev-skills; burnigtm fork; SemIf exists; BuilderIO SIZE+null; OpenStock AGPL; neo4jev size; blink null; Liao jev-browser (jkudish exists); reticle SIZE+NOASSERTION; NanoJev SIZE; skill-suggester / typesafe-ai/skills (no auto-evolve); jev-trader; prism; paperless GPL SIZE; ikermoel skip; jev-mcp exists.
- **0 product Integrate GO.** Transkribus sole HTR. Do not swap `/route`. No LIVE Discord. No xsp/pm scp.

## [2026-09-19] ingest | K266 wave

- **Inbox:** 6 files, all sha256-verified against the handoff table. Parent pre-pulled 6 X extracts via X MCP (`plain_text`) plus Reddit via Brave. Leftover `substack-rss-secpro-2026-09-18-252-…` skipped — already K265.
- **Sources:** LangChain *Building a Harness with Jev* (@sydneyrunkle, 4,141 likes / 9,390 bm / 1,221,679 impr — **best Jev long-form**); @0xMovez *Jev Engineering 10 steps*; @parcadei JEV TIP 001 skill-classify; @shreyanshpatni_ *Custom Agent Harness*; @borjafat *8 internal linking hacks* (**SEO, not Jev**); @BuildwithPublic *0DTE Public API desk* (**not Jev, not a live desk**).
- **Concepts:** 4 hubs — `k266-ccc-jev-x-wave`, `k266-seo-x-voice-wave`, `k266-finance-0dte-wave`, `k266-ood-stub-wave`. Entities: new `langchain-typesafe` FILE stub (**no clone**); bumps `jev-mcp` (**WIRE unchanged**), `openjev` FILE.
- **Phase-0:** `adopt_k266_phase0.sh` — **no clones**. Runtime gate needs no new repo. Live path remains laptop `mcp-jev`. **Never `npx github:jkudish/jev-mcp`.**
- **Routing:** Atto #1 email-triage analog FILE, redacted type only, not vault mail. GW #2 `AutoModeMiddleware` = claim-ledger analog, never auto-arm. CeminiDFS #3 paper-classify analog = review-CSV citation, no solver swap. CeminiParlays #4 dynamic menu = promo vs real-hedge labels, no pm scp. CCC harness brief. SEO voice only. Gambling brief = no route. **No xsp/pm scp. No LIVE Discord.**
- **Briefs:** `briefs/2026-09-19_k266-*` + `### K266 add` on the four Jev briefs.
- **SEO voice:** style pass drafted in `briefs/2026-09-19_k266-seo-voice.md` (exemplar rows, snippets, Article queue, log line). Sibling `../SEO:GEO B&M Business` write attempted.
- **Claim hygiene:** 200x/400x = TypeSafe vendor claim; "78% vs 42%" = author claim, unsourced; Vercel fx 5–18x compares the classifier only. **Cite as claims, never as Cemini measurements.**
- **Archive:** 6/6 `x-article-*` / `x-post-*` inbox files → egress-fi.
- **Revenue verdict:** **no new Cemini product this wave.** Paid analogs already exist (email triage, Browserbase, LangChain). Our money path is **gates inside Atto / GW / DFS / Parlays / CCC**, not a Jev SaaS. OpenJev/clones stay FILE Watch.
- **gate:** `ingest_session_gate.py` + `wiki_lint.py`.

## [2026-09-19] ingest | K265 wave

- **Inbox:** 5 files (parent preingest 5 NEW). Two evals are different hashes — fold both on one source page. Extra copy rows: SkillOpt, tax-doc-classifier, claude-reflect, classifier-dev. Never trust docx SPDX.
- **Sources:** URL eval SPDX overrides; LS Jev clones; SecPro 252; WuBlock HL lend.
- **Concepts:** 6 k265-* hubs. Entities: jev-rules, jev-codex-router, skillopt, tax-doc-classifier, classifier-dev, claude-reflect. Bumps: jev-mcp **WIRE unchanged**, openjev FILE Watch, transkribus sole HTR, wiki-tooling-evaluation, GuruWatcher no auto-arm, k264 hubs.
- **Phase-0:** `adopt_k265_phase0.sh` — jev-rules / jev-codex-router / SkillOpt / classifier-dev / claude-reflect MIT; tax-doc-classifier Apache-2.0. SKIP: cua SIZE-SKIP; Orca AGPL; OpenCreator/Dream-RSI/yibie null; hermes NOASSERTION; laya 404; typesafe proprietary; awesome-jev list skip; jev-mcp exists. **0 product Integrate GO.**
- **Routing:** Atto #1 tax-doc-classifier / classifier-dev FILE redacted type (Transkribus sole HTR). GW #2 LS citation-selection/escalation = claim-ledger gate; never auto-arm. CeminiDFS #3 thin FILE + Jev brief. CeminiParlays #4 escalation FILE + Jev brief. CCC Jev clones / AGENTS.md / SkillOpt FILE (do not swap `/route`). Cyber SecPro FILE. **No xsp/pm scp.**
- **Briefs:** `briefs/2026-09-19_k265-*` + Jev briefs `### K265 add`. Sibling copies attempted.
- **Archive:** 5/5 inbox → egress-fi. Local copies removed. Parent finished after Grok sandbox SSH block.
- **gate:** `ingest_session_gate.py` WARN acknowledged if stale `[NEEDS VERIFICATION]` on historical `wiki/log.md`.

## [2026-09-19] phase-0 | K265

- **EliaAlberti/jev-rules** — MIT `[CONFIRMED]` gh api 2026-09-19; ~16MB GO REFERENCE FILE. No skill auto-evolve.
- **0xNatoshi/jev-codex-router** — MIT `[CONFIRMED]`; tiny GO REFERENCE FILE. **Do not swap `/route`.** Eval Integrate OVERRIDE.
- **microsoft/SkillOpt** — MIT `[CONFIRMED]`; ~24MB GO REFERENCE FILE. **No skill auto-evolve.** Eval Integrate OVERRIDE.
- **kyotofin/tax-doc-classifier** — Apache-2.0 `[CONFIRMED]`; tiny GO REFERENCE FILE. Atto redacted type only. Not product HTR.
- **mrmps/classifier-dev** — MIT `[CONFIRMED]`; ~3MB GO REFERENCE FILE. Atto/GW FILE.
- **BayramAnnakov/claude-reflect** — MIT `[CONFIRMED]`; tiny GO REFERENCE FILE. **No skill auto-evolve.** Eval Integrate OVERRIDE.
- **SKIP:** cua SIZE-SKIP ~483MB; Orca AGPL; OpenCreator/Dream-RSI/yibie SPDX-null; hermes NOASSERTION; laya 404; typesafe proprietary; fatwang2/awesome-jev list skip; jev-mcp already WIRE.
- **0 product Integrate GO.** Transkribus sole HTR. Do not swap `/route`. No LIVE Discord. No xsp/pm scp.

## [2026-09-18] ops | Ashburn cemini-prod deleted

- **Deleted:** Hetzner `ubuntu-8gb-ash-2` (`cemini-prod`). Operator confirmed. SSH to former IP has no banner; `Host cemini-prod` tombstoned to `192.0.2.1` so a recycled IP cannot steal `accept-new`.
- **Live:** `cemini-egress-fi` direct SSH. Raw bulk + pg/redis dumps. GuruWatcher timer `OnCalendar=*:0/15` (oneshot; `OnUnitActiveSec` did not re-arm). `files.youratto.com` Worker 301 → R2 kits.
- **Laptop:** unloaded `com.cemini.prod-mcp-tunnel` (KeepAlive was retrying the dead host). Env backup stays in `~/.cemini/prod-env-backup-2026-09-18/`.
- **Pages:** `cemini-stack`, `cemini-egress-fi`, `hetzner`, `laptop-prod-research-split`, `guruwatcher`, index, ROADMAP, CLAUDE.md schema.
- **Gates:** no xsp/pm scp; no LIVE Discord; no auto-arm watches; no `/opt/cemini` host.

## [2026-09-18] ingest | K264 wave

- **Inbox:** 17 files (14 NEW + 3 false DUPLICATE treated as NEW: two eval copies + LS weekly title). Fold eval `(1)` into one source; archive both. Preingest: parent ran; do not re-litigate licenses.
- **Sources:** URL-stack eval SPDX overrides; C2C; ATM $1B+ tape; vehicle voice; China AIGC; PP-OCRv6 historical; xeno-interpretability; harness-design; OverclaimBench; SAFEHARNESS OOD; LS Projects; tldrsec 346; Capital Flows; EH Eagles; Klement homework; WuBlock Fed hike.
- **Concepts:** 8 k264-* hubs. Entities: pi-subagents, tradingview-optimizer, fast-jev-compaction, c2c. Bumps: jev-mcp **WIRE/runtime_wired**, jev-ultrafast FILE, transkribus sole HTR, tradesdontlie FILE-not-Integrate, wiki-tooling-evaluation, GuruWatcher no auto-arm, k263 hubs.
- **Phase-0:** `adopt_k264_phase0.sh` — pi-subagents / tradingview-optimizer / fast-jev-compaction MIT; C2C Apache-2.0. SKIP: handbook NOASSERTION; hardenerAi/typesafe-mario/building-with-jev-skill SPDX-null; HTF GPL extract-only; worldmonitor AGPL; jev-browser TLS timeout; jev-mcp/jev-ultrafast exist. **0 product Integrate GO.**
- **Routing:** Atto #1 jev-mcp laptop WIRE (not vault product; Transkribus sole HTR). GW #2 ATM historical FILE; tradingview-optimizer HITL; never auto-arm. CeminiDFS #3 thin FILE. CeminiParlays #4 EH Eagles FILE. CCC harness-design/overclaiming/C2C/LS/pi-subagents FILE (do not swap `/route`). Cyber EXTRACT. **No xsp/pm scp.**
- **Briefs:** `briefs/2026-09-18_k264-*` written (gitignored). Sibling copies attempted — sandbox may block `../`.
- **Archive:** 17/17 inbox → egress-fi. Local copies removed.
- **gate:** `ingest_session_gate.py` WARN acknowledged — stale `[NEEDS VERIFICATION]` on historical `wiki/log.md` entries are pre-existing, not this batch. Stromberg et al (2026) is cite-only `[NEEDS VERIFICATION 2026-09-18]`.

## [2026-09-18] phase-0 | K264

- **nicobailon/pi-subagents** — MIT `[CONFIRMED]` parent gh api 2026-09-18; ~19MB GO REFERENCE FILE. Do not swap `/route`.
- **Roboquant-AI/tradingview-optimizer** — MIT `[CONFIRMED]` gh api 2026-09-18; tiny GO REFERENCE FILE. Chrome HITL. No auto-arm.
- **tamaratran/fast-jev-compaction** — MIT `[CONFIRMED]` gh api 2026-09-18; tiny GO REFERENCE FILE. No skill auto-evolve.
- **thu-nics/C2C** — Apache-2.0 `[CONFIRMED]` gh api 2026-09-18; ~5MB GO REFERENCE FILE.
- **jkudish/jev-mcp** — MIT `[CONFIRMED]`; already cloned. **WIRE laptop Cursor MCP** (operator OK). Local dist. Never `npx github:`. **0 product Integrate.**
- **jkudish/jev-browser** — MIT `[CONFIRMED]` by live `gh api` retry 2026-09-18 (57 ★ / ~10MB); REFERENCE clone made. HITL cassette only. No unattended Antenati scrape.
- **browser-use/jev-ultrafast** — already cloned. FILE bump HITL.
- **SKIP:** handbook NOASSERTION; hardenerAi/typesafe-mario/building-with-jev-skill SPDX-null (do not copy skills); HTF GPL extract-only; worldmonitor AGPL and SPDX still unconfirmed; tradingview-mcp exists FILE-not-Integrate.
- **Archive:** 17/17 inbox files on `cemini-egress-fi:/opt/cemini-bulk/research/osint/`; local inbox empty.
- **0 product Integrate GO.** Transkribus sole HTR. No skill evolve. No LIVE Discord. No xsp/pm scp.

## [2026-09-18] ops | claude-mem observer Nemo

- **Switch:** OpenRouter primary `mistralai/mistral-nemo`, fallback `inclusionai/ling-3.0-flash`. Worker 13.24.20 loaded live. No `:free`. No paid GLM 5.2.
- **Cost proxy:** 17 Sep 264 calls → ~$0.40/mo Nemo vs $15–45 paid GLM 5.2 (thinking tax).
- **Pages:** `entities/tools/claude-mem.md`, index, ROADMAP. Settings live in `~/.claude-mem/` (not git).

## [2026-09-18] ops | laptop TV MCP + OpenCLI Hyperliquid

- **Cursor MCP:** `plugin-finance-data-providers-tradingview` already live (37 tools). Smoke: SPY quote + BTC pulse. Personal research only. Not inherited by Grok `/route`.
- **OpenCLI tradingview:** SKIP — no `TradingView.app`; plugin needs logged-in Desktop; options often paid. Operator: no paid TV account.
- **OpenCLI Hyperliquid:** `opencli plugin install github:himself65/finance-skills/hyperliquid` → `@0.1.0`. Smoke: `markets --limit 3` (BTC 78028 / ETH 2507.5 / ZEC 1458.9); `funding-compare --coin BTC` (HL APR 10.95 vs Binance 4.52). Public `/info`, no key.
- **tradesdontlie CDP MCP:** still off (no Desktop). Family C + steal-from unchanged.
- **Pages:** `entities/tools/finance-skills.md`, `entities/tools/opencli.md`, `entities/tools/tradingview-mcp-atilaahmettaner.md`, `sources/tradesdontlie-tradingview-mcp.md`, index, ROADMAP.
- **Prod:** no TV in `/opt/cemini`. No LIVE Discord. No xsp/pm scp.

## [2026-09-17] ingest | K263 wave

- **Inbox:** 16 files (15 NEW + 1 LIKELY treated as NEW: PE Matt Pocock ≠ Dex Horthy). Preingest: parent ran; do not re-litigate licenses.
- **Sources:** stack eval SPDX overrides; Donny 16 Sep macro; pruning smart-home; cost-efficient LLM; AeroWeaver OOD; CERA-MoA; fictitious play; social laws; ScienceIDE; AgentLSD; LS AIUC + Gas Town; PE Pocock; EH sports hedge; Klement Malacca; Moontower var/cov.
- **Concepts:** 8 k263-* hubs. Entities: openjev, jev-ultrafast, browserskill, jev-mcp, knowledge-work-plugins, ecc-harness, agent-lsd. Bumps: nvidia-skillspector no new clone, colibri Watch no new clone, data-formulator FILE, k262 hubs, GuruWatcher no auto-arm, wiki-tooling-evaluation FILE-not-Integrate.
- **Phase-0:** `adopt_k263_phase0.sh` — openjev / jev-ultrafast / BrowserSkill / data-formulator / jev-mcp / ECC / agent-lsd MIT; knowledge-work-plugins Apache-2.0. **0 Integrate GO.**
- **Routing:** Atto #1 openjev FILE (PII on-device; Transkribus sole HTR; HITL chrome cassette). GW #2 Donny MSTR 120 / UEC 9-9.50 claim-ledger HITL; Klement Malacca no named levels. CeminiDFS #3 data-formulator FILE. CeminiParlays #4 EH real-vs-promo hedge FILE. CCC CERA-MoA/ScienceIDE/ECC/Pocock/Gas Town/AIUC FILE (do not swap `/route`). Cyber AgentLSD EXTRACT. **No xsp/pm scp.**
- **Briefs:** `briefs/2026-09-17_k263-*` written (gitignored). Sibling copies attempted — sandbox may block `../`.
- **Archive:** 16/16 inbox → egress-fi. Local copies removed.
- **gate:** `ingest_session_gate.py` WARN acknowledged — stale `[NEEDS VERIFICATION]` on historical `wiki/log.md` entries are pre-existing, not this batch. Maurer et al (2026) is URL-only `[NEEDS VERIFICATION 2026-09-17]`.

## [2026-09-17] phase-0 | K263

- **TheoLeeCJ/openjev** — MIT `[CONFIRMED]` gh api 2026-09-17; ~5MB GO REFERENCE FILE. Local System-One logit readout. Do not swap `/route`.
- **browser-use/jev-ultrafast** — MIT `[CONFIRMED]`; ~4MB GO REFERENCE FILE. Chrome HITL. No unattended portal scrape.
- **Tencent/BrowserSkill** — MIT `[CONFIRMED]`; ~5MB GO REFERENCE FILE. Eval Integrate OVERRIDE. HITL chrome.
- **microsoft/data-formulator** — MIT `[CONFIRMED]`; ~36MB GO REFERENCE FILE. DFS FILE.
- **jkudish/jev-mcp** — MIT `[CONFIRMED]`; tiny GO REFERENCE FILE. Ask before MCP.
- **anthropics/knowledge-work-plugins** — Apache-2.0 `[CONFIRMED]`; ~6.5MB GO REFERENCE FILE. No skill auto-evolve.
- **affaan-m/ECC** — MIT `[CONFIRMED]`; ~52MB GO REFERENCE FILE. Eval Integrate OVERRIDE. HITL. No skill auto-evolve.
- **Golim/agent-lsd** — MIT `[CONFIRMED]`; ~8MB GO REFERENCE EXTRACT. No PoC. No CTF writeups.
- **SKIP:** skillspector exists; colibri Watch exists; WeKnora NOASSERTION; cilium SIZE-SKIP; supervision SIZE-SKIP; coder AGPL; n8n NOASSERTION; Octop Pass; claude-code proprietary; ScienceIDE no SPDX URL.
- **0 Integrate GO.** Transkribus sole HTR. No MCP. No LIVE Discord. No xsp/pm scp.

## [2026-09-16] ingest | K262 wave

- **Inbox:** 23 NEW (1 eval + 10 arXiv/PDF + 12 newsletters). Preingest: parent ran; do not re-litigate licenses.
- **Sources:** repo eval SPDX overrides; ExpertHTR; ScienceBuddy; social harness; byte distill; GANADI; Kalshi hedge; diffusion vol; SBM; clinical OOD; insect OOD; LS Socher/AEF-1/games/Jev; PE factory; EH Kalshi records + CLARITY; Klement NATO + CB; Moontower Fed/10y; WuBlock traffic + cloture.
- **Concepts:** 8 k262-* hubs. Entities: security-audit-skill, sciencebuddy, open-code-review, oh-my-hermes, experthtr, openhunterai. Bumps: m3e-canvas no new clone, k261-atto ExpertHTR pointer, GuruWatcher no auto-arm, wiki-tooling-evaluation FILE-not-Integrate.
- **Phase-0:** `adopt_k262_phase0.sh` — security-audit-skill / ScienceBuddy / oh-my-hermes MIT; open-code-review Apache-2.0. **0 Integrate GO.**
- **Routing:** Atto #1 ExpertHTR FILE (Transkribus sole HTR). GW #2 Moontower/Klement no auto-arm. CeminiDFS #3 Kalshi football awareness only. CeminiParlays #4 EH combos + Kalshi hedge FILE. CCC ScienceBuddy/social/factory FILE (do not swap `/route`). Cyber EXTRACT. **No xsp/pm scp.**
- **Briefs:** `briefs/2026-09-16_k262-*` written (gitignored). Sibling copies blocked by workspace sandbox — operator `cp` leftover.
- **Archive:** 23/23 inbox → egress-fi. Local copies removed.
- **gate:** `ingest_session_gate.py` WARN acknowledged — stale `[NEEDS VERIFICATION]` on historical `wiki/log.md` entries are pre-existing, not this batch.

## [2026-09-16] phase-0 | K262

- **cloudflare/security-audit-skill** — MIT `[CONFIRMED]` gh api 2026-09-16; ~0.14MB GO REFERENCE FILE. Do not copy into Cursor skills.
- **Gen-Verse/ScienceBuddy** — MIT `[CONFIRMED]`; ~12MB GO REFERENCE FILE. HITL. No skill/harness auto-evolve.
- **alibaba/open-code-review** — Apache-2.0 `[CONFIRMED]`; ~52MB GO REFERENCE FILE.
- **rlaope/oh-my-hermes** — MIT `[CONFIRMED]`; ~100MB GO REFERENCE FILE.
- **SKIP:** OpenHunterAI NOASSERTION NO-GO; supervision SIZE-SKIP ~4.3GB; google-maps-scraper no clone (ToS); fmzquant SPDX null; tinycast/WeKnora NOASSERTION; YuE OOD; VoiceStudio/ever-gauzy AGPL; m3e-canvas exists; YOINK no pm scp.
- **0 Integrate GO.** Transkribus sole HTR. No MCP. No LIVE Discord. No xsp/pm scp.

## [2026-09-16] query | Outlier Weekly LIVE — CRML / Tanbreez

- **LIVE** — https://outlierweekly.substack.com/p/the-greenland-license-is-real-the (operator-confirmed 2026-09-16; scheduled 2026-09-14)
- **SEO wiki** — @seo-wiki/concepts/crml-tanbreez-outlier-notes.md flipped scheduled → LIVE; voice table + index updated
- **This wiki** — permalink recorded on 2026-09-01 CRML query handoff. Desk pack: `reports/research/pack-crml-short-thesis-20260901/`. No new research pass. No xsp/pm scp.

## [2026-09-15] ingest | K261 wave

- **Inbox:** 10 files (7 NEW + 3 LIKELY treated as NEW: Osmani different title, Talon new week, Moontower #327 next issue). Preingest: parent ran; do not re-litigate licenses.
- **Sources:** stack eval SPDX overrides; Osmani brownfield; EH Ep 32 enforcement; Talon 14–18 Sep; Klement debt + disasters; Moontower Kelly + #327; Outlier Tanbreez; WuBlock Fed/BOJ.
- **Concepts:** 7 k261-* hubs. Entities: power-pwn, agentic-inbox, mcp-sports-hub, arsenal-ng, m3e-canvas. Bumps: worldmonitor AGPL Watch reaffirm, vphone-cli no new clone, wiki-tooling-evaluation FILE-not-Integrate, GuruWatcher Talon HITL, k260 hubs.
- **Phase-0:** `adopt_k261_phase0.sh` — power-pwn / mcp-sports-hub / arsenal-ng / m3e-canvas MIT; agentic-inbox Apache-2.0. **0 Integrate GO.**
- **Routing:** Atto #1 FILE (CF email + agentic-inbox; hypit NO-GO). GW #2 Talon HITL no auto-arm. CeminiDFS #3 mcp-sports-hub FILE no MCP. CeminiParlays #4 EH + Kelly FILE. CCC Osmani/m3e FILE (do not swap /route). Cyber EXTRACT. **No xsp/pm scp.**
- **Briefs:** `briefs/2026-09-15_k261-*` written (gitignored). Sibling copies blocked by workspace sandbox — operator `cp` leftover.
- **Archive:** 10/10 inbox → egress-fi. Local copies removed.
- **gate:** `ingest_session_gate.py` WARN acknowledged — stale `[NEEDS VERIFICATION]` on historical `wiki/log.md` entries are pre-existing, not this batch. IMF Nguyen et al (2026) is URL-only `[NEEDS VERIFICATION 2026-09-15]`. Daily digest paper lane = 0 hits — no arXiv fetch.

## [2026-09-15] phase-0 | K261

- **mbrg/power-pwn** — MIT `[CONFIRMED]` gh api 2026-09-15; ~3.5MB GO REFERENCE EXTRACT. Authorized lab. No PoC.
- **cloudflare/agentic-inbox** — Apache-2.0 `[CONFIRMED]`; ~3.5MB GO REFERENCE FILE. Cloudflare lock-in; not product Integrate.
- **lacausecrypto/mcp-sports-hub** — MIT `[CONFIRMED]`; ~3MB GO REFERENCE FILE. Ask before MCP.
- **halilkirazkaya/arsenal-ng** — MIT `[CONFIRMED]`; ~18MB GO REFERENCE EXTRACT. No PoC.
- **lnkiai/m3e-canvas** — MIT `[CONFIRMED]`; ~9MB GO REFERENCE FILE CCC.
- **SKIP:** worldmonitor AGPL Watch reaffirm no re-clone; hypit NOASSERTION NO-GO; vphone-cli exists; ligolo GPL extract-only no clone; VoiceStudio AGPL; auto-gpu-kernel Watch; YOINK no pm scp; awesome-trading-agents list no clone.
- **0 Integrate GO.**

## [2026-09-14] operator | Grok Bot DFS/Parlays desks (§17–19)

- **Brief:** `briefs/2026-09-01_grok-bot-charters.md` — §17 Parlays Slate Desk (weather / roster / scheme → `environment.csv`); §18 DFS Recap Desk; §19 Parlays Recap Desk. DFS Slate Desk remains §8.
- **Product copies:** `CeminiParlays/docs/GROK-BOTS.md`, `CeminiDFS/docs/GROK-BOTS.md`; sibling briefs `2026-09-14_grok-bots.md`.
- **Wiki:** bump `grok-bot`, `grok-bot-operator-patterns`. FILE only; operator paste into Grok Bot.app. No Odds API key on the Bot VM. No sportsbook submit. No FanDuel Enter.
- **Example:** `CeminiParlays/examples/recap_sportsbook_ledger.csv` for `ceminiparlays grade`.

