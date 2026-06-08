---
title: High-signal paper patterns — what makes an ingest worth doing
type: concept
tags: [ingest-rubric, paper-evaluation, source-selection, librarian-methodology, decision-rubric, applied-during-ingest]
keywords: [high-signal-paper, ingest-decision, source-selection, paper-evaluation-rubric, recipe, cemini-relevance, deployment-surface, license-poison-pill, exa-sweep, workflow-a, workflow-c, tier-2-proactive-search]
related:
  - sources/black-scholes-iv-explicit-schadner-2026.md
  - sources/pta-metric-anchoring-ssrn-4549819.md
  - sources/agentic-harness-engineering.md
  - sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md
  - sources/skillopt-executive-strategy-self-evolving-agent-skills-2026-05-30.md
  - sources/sia-self-improving-ai-harness-weight-updates-2026-05-30.md
  - sources/incompressible-knowledge-probes-li-2026.md
  - sources/lob-regime-detection-hiremath-2026.md
  - sources/moe-efficiency-leverage-tian-2026.md
  - sources/moe-surpass-dense-equal-resource-li-2026.md
  - sources/polymarket-informed-minority-gomezcram-2026.md
  - sources/training-free-grpo-cai-2025.md
  - sources/llms-corrupt-documents-laban-2026.md
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/gemini-dr-wave4b-osint-2026-04-29.md
  - sources/microsoft-qlib.md
  - sources/arxiv-agents-last-exam-2606.05405-2026-06-06.md
  - concepts/agents-last-exam-benchmark.md
  - sources/dune-analytics-mcp.md
  - sources/polymarket-predictions-mcp.md
  - sources/mercurialsolo-claudectl.md
  - sources/upstash-context7.md
  - sources/arxiv-alphaforgebench-2602-18481-2026-06-01.md
  - concepts/llm-alpha-factor-benchmarking.md
  - sources/last30days-skill-mvanhorn.md
  - sources/arxiv-epicure-food-embeddings-2605.22391.md
  - concepts/llm-augmented-entity-consolidation.md
  - sources/tradesdontlie-tradingview-mcp.md
  - sources/7onez-cti-expert.md
  - sources/spaceshift-sateais-api.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/llm-agent-systems.md
  - concepts/mcp-tool-marketplace.md
  - sources/thinking-with-visual-primitives-deepseek-2026.md
  - sources/platonic-representation-hypothesis-huh-2024.md
  - sources/sherry-ternary-quantization-tencent-2026.md
  - sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
  - sources/alash3al-stash.md
  - sources/shiyu-coder-kronos.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - sources/agriciDaniel-claude-obsidian.md
  - sources/piebald-claude-code-system-prompts.md
  - sweeps/2026-04-30.md
  - sources/situational-awareness-aschenbrenner.md
  - sources/blade-bayesian-listwise-alignment.md
  - sources/regime-conditioned-bo-evaluation.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/cemini-wiki-ingest-workflow.md
  - meta/daily-research-digest-cadence.md
  - sources/gemini-sci-research-2602-03837.md
created: 2026-04-29
updated: 2026-06-08
maturity: validated
---

## Relations

- @sources/black-scholes-iv-explicit-schadner-2026.md — Landing #1: refutes "BS-IV requires iteration"; closed-form math; CC BY 4.0; 223–235× empirical speedup. Quant-finance domain. Single-author.
- @sources/pta-metric-anchoring-ssrn-4549819.md — Landing #2: novel cross-sectional return predictor; TimescaleDB-shaped; promoted from K9 link-aggregate (not a direct user drop).
- @sources/agentic-harness-engineering.md — Landing #3: empirical methodology paper for LLM-agent harness evolution; 7-component decoupled substrate; +10.1pp transfer to deepseek-v4-flash; arXiv 2604.25850.
- @sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md — K105: physical-domain harness with flight-test oracle; steal patterns (skills/subagents/MCP); REFERENCE not Adopt.
- @sources/incompressible-knowledge-probes-li-2026.md — Landing #4: black-box parameter-estimator; deepseek-v4-* in calibration set; refutes Densing Law for factual capacity; single-author Pine AI; arXiv 2604.24827.
- @concepts/wiki-tooling-evaluation.md — sibling decision-record; Wave 1/2/3 ingest evaluation also used implicit criteria; this page makes them explicit.
- @concepts/cemini-wiki-ingest-workflow.md — daily digest + Tier 2/2.5 sweeps score candidates against this rubric
- @meta/daily-research-digest-cadence.md — Phase 1 morning discovery; references rubric in sweep next-steps
- @concepts/ip-sale-readiness.md — license poison-pill families A and B are the negative-signal half of this rubric.
- @concepts/llm-agent-systems.md — cluster hub for the LLM-agent landing area, where 2 of the 4 recent high-signal papers landed.
- @sources/situational-awareness-aschenbrenner.md — Aschenbrenner 2024 (165pp); landmark AGI-timeline essay ingested as Wave 5.1 source page; deep-read pending (first 10pp skimmed)
- @sources/blade-bayesian-listwise-alignment.md — K33 Landing: SIGIR '26 paper diagnosing two failure modes of static BoN listwise alignment + Bayesian fix. Methodologically rigorous (formal theorem + empirical validation), CC BY 4.0, direct Cemini surfaces (ranking tasks).
- @sources/regime-conditioned-bo-evaluation.md — K33 Landing: highest action-value of K33. Formal No-Free-Leaderboard proposition + PRS metric + REGIMEPLANNER + 79-condition GDSC2 case study. Direct fit to brief-audit gates and Conductor fitness function.
- @concepts/regime-conditioned-evaluation.md — K33 concept hub formalizing the regime-disclosure discipline; **applied-during-ingest** sibling rubric to this page (this rubric scores papers, regime-conditioned-evaluation scores claims about evaluation comparison).

## Raw Concept

**What prompted this page**: 2026-04-29, after a stretch where the user observed that the last 4 papers ingested (BSIV, PTA, AHE, IKP) "have mostly been very influential" and asked: how can we seek out specifically papers like these?

The recipe was implicit in those 4 landings. This page makes it explicit so:
1. The LLM (this agent in future sessions) consults the rubric during every ingest decision and during proactive Exa sweeps (Tier 2 of `@ROADMAP.md` proactive-search design).
2. The user can apply the rubric themselves when scanning arXiv RSS, GitHub trending, or other discovery channels.
3. Future divergence between "papers we like" and "papers we Reject" remains traceable to a written standard rather than implicit taste.

## Narrative

### The rubric — three filters, then quality + operational signals

Every candidate paper passes through three filters in order. If a candidate fails any filter, stop — don't ingest.

**Filter 1 — Format** *(hard requirement)*

| Required form | Examples that pass | Examples that fail |
|---|---|---|
| Research paper / preprint / academic working paper / SSRN paper / methodologically rigorous github project | arXiv preprint with DOI; SSRN paper with abstract; ICLR/NeurIPS conference paper; OpenReview submission; well-cited tech report | Marketing blog; Substack opinion piece; LinkedIn post; ChatGPT-generated summary; vendor press release; non-rigorous github README |

Note: rigorous github projects (e.g. `agentic-harness-engineering`, `langextract`) **can** pass Filter 1 if they ship with a paper or whitepaper-grade documentation. Pure vibes-coded repos do not.

**Filter 2 — Recency** *(hard requirement; window is the 30-day default for proactive search; loosens for retroactive discovery of older landmark papers)*

| Window | Treatment |
|---|---|
| Last 30 days | Default Tier-2 sweep window. Catches arXiv/SSRN late-month deadline clusters. |
| 30–90 days | Acceptable if Filter 3 hits hard (Cemini-domain overlap is direct + concrete deployment surface is obvious). |
| > 90 days | Only ingest as a retroactive discovery (cited by something we already have, or fills a known gap surfaced by `wiki_gap_detect.py`). |

The 4 recent landings were all within 14 days of arXiv submission. Recency mattered because the "interesting" / "surprising" content was novel.

**Filter 3 — Cemini-domain overlap** *(hard requirement; one or more)*

The candidate touches one of these surfaces in a non-trivial way:

| Cluster | Surface inside Cemini stack | Example landing |
|---|---|---|
| **Quant finance** | Options pricing (BS, IV, Greeks); cross-sectional alpha factors; market microstructure; portfolio strategy; RL for trading | BSIV (closed-form IV → Polars hot path) |
| **LLM agent infrastructure** | Harness engineering; MCP; orchestration substrates; multi-agent coordination; RAG architectures | AHE (7-component decoupled substrate → analyst orchestrator) |
| **LLM brain capacity / evaluation** | Anything that quantifies / calibrates / fingerprints DeepSeek family; MoE scaling; parameter estimation; knowledge capacity; hallucination patterns | IKP (deepseek-v4-* explicit in calibration set) |
| **Market infrastructure** | Prediction markets (Kalshi, Polymarket); event contract pricing; order-book microstructure; high-frequency execution | (none in recent 4 landings — open opportunity) |
| **Data infrastructure** | TimescaleDB / continuous aggregates; vector DBs; knowledge graphs; FTS5; column-store analytics | PTA (TimescaleDB continuous aggregate → adoption candidate) |
| **Audit / governance / IP** | Cryptographic audit trails; SBOM; license analysis; prescribed-vs-deployed verification | (gemini-dr-link-eval-2026-04-28 + ip-sale-readiness — methodology not a paper) |

A candidate that lands in two clusters at once is automatically more interesting (e.g. a paper bridging quant finance + LLM evaluation). Less domain-overlap → harder to justify ingest cost.

### Quality signals — more = better

Once a candidate passes the three filters, score it against these. ≥3 hits = strong candidate; ≥4 = ingest by default.

1. **Empirical results, not just position-paper framing**. R² values, confidence intervals, sample sizes (89 models, 96 dated checkpoints, 328 test cases). The recent 4 all had this.
2. **Comprehensive prior-work integration**. Cites 15+ relevant prior works. AHE cites 27 references; IKP cites 30+. Position papers ingested previously (Kim's `harness-4-5.md`, Maynard's `harness2-4-5.md`) cited fewer and were correctly graded `read-skim` not `read`.
3. **Code release at github** with verifiable license. Lowers adoption friction substantially. AHE / IKP / langextract all hit. Pure-math papers (BSIV) substitute reproducibility-via-formula.
4. **Reproducibility hooks**. Datasets named, methodology detailed, baseline implementations referenced. Allows side-channel verification without trusting the author.
5. **Refutes / advances a widely-held belief**. The "interesting" criterion. BSIV: "BS-IV requires iteration" → wrong. IKP: "Densing Law applies to all capability" → wrong for factual recall. AHE: "harness optimization = prompt tuning" → wrong; tools/middleware/memory carry the gain. PTA: "P-to-52w-high is anchoring noise" → wrong; it predicts cross-sectional returns. Refutation papers tend to be high-signal because the author had to do the work to refute the prior.
6. **Mathematical / algorithmic novelty distinct from training-recipe novelty**. The Densing Law is real for procedural capability; what makes IKP interesting is that it ISOLATES the part that doesn't compress. Training-recipe papers ("we trained X on Y and got Z%") are lower-signal than methodology / theory papers in our corpus because Cemini's brain comes from a vendor — we're consumers of training, not producers.

### Operational signals — the Cemini-deployment angle

Even a well-supported paper can be lower-signal if there's no clear deployment surface. Score these:

1. **Concrete deployment surface in the Cemini stack** (where in the codebase the paper's contribution would land). BSIV → `services/quant/iv_explicit.py`. IKP → daily 50-probe cron + hallucination-similarity drift detector. AHE → analyst-orchestrator harness substrate. PTA → TimescaleDB continuous aggregate.
2. **Quantifiable expected gain**. BSIV: 223–235× compute speedup measured. IKP: parameter-count visibility for vendor-independent procurement. AHE: +10.1pp pass@1 on deepseek-v4-flash measured. PTA: predicted cross-sectional return premium measured on prior datasets.
3. **Clear next-step**. After reading: "do a brief", "run a reproduction script", "license-gate the github code", etc. If the paper is just interesting-to-read with no actionable step, it's a Snippets-only candidate, not a full ingest.

### Negative signals — skip even when positive criteria met

| Signal | Action | Reasoning |
|---|---|---|
| License is GPL-3.0 / AGPL-3.0 / SSPL / ELv2 | **Skip code adoption**; paper-only ingest if methodology is recoverable | Poison-pill family A: copyleft. Spreads to derivative works, blocks IP-sale-readiness. See `@concepts/ip-sale-readiness.md`. |
| License is "NOASSERTION" or self-disclosed unauthorized derivative | **Reject entirely** | Poison-pill family B: vendor-IP-redistribution-without-authorization. See `@concepts/ip-sale-readiness.md`. (Worked example: openclaude.) |
| Single-author + extraordinary claims + no peer-reviewed track record | **Read-skim, not deep-read; never deploy without independent reproduction** | Single-author papers are higher variance; the 4 recent landings include 2 single-author (Schadner, Bojie Li) — both succeeded BUT both also had strong methodological grounding in cited peer-reviewed literature. The signal is "single author + sketchy citations + grandiose claim" → defer. |
| ≥50% overlap with existing wiki page | **Update existing page; do not create a new source** | Use `scripts/preingest_check.py` Step 0 of ingest workflow; if DUPLICATE / LIKELY → update existing instead. |
| Domain is NLP-only / vision-only / RL-only with no quant or agent angle | **Skip unless we have an explicit gap to fill** | Cemini's stack is OSINT + financial research, not a general-purpose ML lab. NLP-without-finance papers crowd the corpus. |
| Author is a research lab with closed-source preview only (no published paper, no code) | **Skip for now; revisit if an open paper drops** | Unable to verify claims, unable to deploy. (Anthropic / OpenAI / DeepMind blog posts often fall here.) |
| Vendor whitepaper / paid-content marketing piece | **Skip** | The wiki has standards. Even if the content is interesting, surfacing it from a `wiki/sources/<vendor>.md` file as if it were peer-reviewed inflates trust. If the technique is interesting, write it up as a `concepts/` page citing the vendor URL with `[TENTATIVE]`. |

### Workflow A status — ACTIVE as of 2026-04-29 (Path 1: session-driven)

User authorized Tier 2 promotion after the first manual Workflow A run surfaced 4 high-signal papers (`@sources/lob-regime-detection-hiremath-2026.md`, `@sources/moe-efficiency-leverage-tian-2026.md`, `@sources/moe-surpass-dense-equal-resource-li-2026.md`, `@sources/polymarket-informed-minority-gomezcram-2026.md`). The chosen automation tier:

- **Path 1 — Session-driven** (active): the LLM runs the 5 queries via the bundled Exa MCP plugin during a Claude Code session. Zero setup, zero new spend. The CLAUDE.md "Session-start ritual" subsection prompts the user weekly; `CronCreate` provides a Sunday 09:07 supplemental nudge. **Reports land at `wiki/sweeps/YYYY-MM-DD.md`** (commit them as wiki content; useful as a corpus of past candidate lists).
- **Path 2 — Bash + crontab + user Exa key** (ready, not activated): `scripts/weekly_arxiv_sweep.sh` is committed and ready. Activation requires the user to drop their own Exa API key at `~/.cemini/exa-api-key` and add the cron entry. Flip if Path 1's reliability becomes a friction.

Why Path 1 over Path 2: the Exa plugin's bundled credentials cannot be extracted for use by external bash scripts (verified 2026-04-29 — no API key found in `~/.claude/settings.json`, `~/.claude/plugins/cache/.../env.example` confirms users would need their own). Path 1 reuses the plugin's bundled spend; Path 2 doubles up on Exa subscriptions.

### Cluster-specific Exa-search query templates (Workflow A)

For weekly Tier-2 sweeps, these are the queries that have historically surfaced papers matching the rubric. Date-bounded to the last 14 days; category=`research paper` where possible.

```
"agent harness" OR "LLM agent evaluation" OR "agent orchestration framework" OR "agentic AI"
"options pricing" OR "implied volatility" OR "Greeks computation" OR "Black-Scholes"
"DeepSeek" OR "mixture of experts" OR "MoE scaling" OR "LLM parameter estimation"
"prediction market" OR "Kalshi" OR "Polymarket" OR "event contract pricing"
"reinforcement learning" "algorithmic trading" OR "portfolio optimization" OR "market making"
"multi-agent" "financial" OR "trading" OR "market microstructure"
"TimescaleDB" OR "continuous aggregate" OR "time-series database" "trading" OR "finance"
```

If a sweep returns ≤2 candidates passing Filter 1+2+3, drop two queries and add a fresh angle. If it returns ≥10 candidates passing all filters, the sweep has caught a deadline cluster (NeurIPS, ICLR, late-arXiv) and the user should be involved in selection.

### Application — how to score a candidate end-to-end

1. **Filter 1 (Format)**: drop or proceed.
2. **Filter 2 (Recency)**: drop or proceed.
3. **Filter 3 (Cemini-domain)**: drop or proceed.
4. **Quality signals**: count hits across the 6 above.
5. **Operational signals**: count hits across the 3.
6. **Negative signals**: any one is sufficient to skip.

Combined score, written as `Q/3 quality, O/3 operational, [Skip|Read-skim|Read|Reject]`:
- `≥3Q + ≥2O + no negatives` → **Read** (full ingest)
- `≥2Q + ≥2O + no negatives` → **Read-skim** (source page with shorter Narrative; revisit if cited 3+ times in subsequent ingests)
- `1Q + 1O + no negatives` → **Steal-from** (no source page; insights folded into existing concept pages with citation)
- `Negative signal → Reject` (with note in `concepts/ip-sale-readiness.md` if it's a license poison-pill)

### Worked examples

**Recent landings — what they scored against the rubric**:

| Paper | Q | O | Verdict | Notes |
|---|---|---|---|---|
| BSIV (Schadner) | 5/6 | 3/3 | Read (full + reproduction + brief) | Refutation + math + 223–235× empirical gain + brief shipped |
| PTA Metric | 4/6 | 3/3 | Read (cross-doc duplicate confirmation from K8) | Surfaced via K9 not direct user drop, but rubric retrofits cleanly |
| AHE (Lin et al) | 5/6 | 3/3 | Read | Refutation of prompt-only optimization + cross-model transfer + 6 bidir cross-links |
| IKP (Bojie Li) | 5/6 | 3/3 | Read | Refutation of Densing Law for factual + deepseek-v4-* calibration + silent-swap detector primitive |

**Worked Reject from Wave 3** (`gemini-dr-wave3-link-eval-2026-04-28.md`):

| Paper / project | Filter | Result |
|---|---|---|
| openclaude | Filter 1: ✓ Filter 2: ✓ Filter 3: ✓ | **REJECT** at Negative-signals: license is NOASSERTION + self-disclosed unauthorized derivative of Anthropic Claude Code. New poison-pill family B. |
| warp | Filter 1: ✓ Filter 2: ✓ Filter 3: ✓ | **REJECT** at Negative-signals: AGPL-3.0 license. Poison-pill family A. |

**What a Snippets-only landing looks like** (from K9, where the rubric scored Steal-from):

| Doc | Q | O | Verdict |
|---|---|---|---|
| ml-for-trading (book) | 2/6 | 1/3 | Steal-from — citation in `@concepts/quant-finance.md`, no source page; framework-obsolescence flag noted |

### Maintenance

This rubric is meta-content. Update it whenever:
1. A landing causes us to revise the criteria (e.g. a Read paper turns out to be a Reject post-deployment → criteria need tightening).
2. A new poison-pill family is identified (already happened: family B from openclaude).
3. The negative-signal table grows from observed misses (papers we ingested then later regretted).
4. A new domain joins the Cemini stack (e.g. if Cemini ever takes on social-media-OSINT, a new cluster row would land in Filter 3).

Track changes via the `updated:` field + `wiki/log.md` entries with `op = lint | rubric-update`.

## Snippets

> **The user observation that prompted this page**:
>
> "it seems like the last 2 or 3 papers i have submitted have mostly been very influential, how can we seek out specifically papers like these?" [Source: 2026-04-29 session]

> **Filter 3 hit-pattern from the 4 recent landings**:
>
> All 4 hit at least one Cemini-domain cluster directly. AHE and IKP both hit the LLM-agent-infrastructure surface where DeepSeek family is the brain. BSIV and PTA both hit quant-finance with concrete `services/quant/*` deployment slots. **No "interesting but tangential" papers landed.** The recipe holds: domain-overlap is non-negotiable.

> **The "refutation premium"**:
>
> 3 of 4 recent landings refute a widely-held belief (BSIV: "iteration is needed"; AHE: "prompt is the harness"; IKP: "Densing applies to all capability"). Refutation papers are higher-signal in our corpus because the author had to do the work to refute the prior, AND the refutation directly informs how we should architect the Cemini stack. Pure incremental-improvement papers ("X% better than baseline on benchmark Y") rarely land at full Read maturity.
