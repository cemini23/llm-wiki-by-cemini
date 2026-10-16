---
title: K292 osint wave — feeds, tool eval, and the inbox fan-out defect (Oct 2026)
type: source-hub
tags: [k292, osint, feeds, tool-eval, eval, defects]
keywords: [fan-out, daily digest, CEMINI_WIKI_ID, paper queries, BeTINN, TheoPhysEval, Librarian Agents, leantoken, Kalshi share, Goolsbee]
related:
  - sources/k292-osint-feeds-2026-10-16.md
  - sources/eval-url-multi-wiki-repository-2026-10-16.md
  - sources/arxiv-betinn-2610.19254-2026-10-16.md
  - sources/arxiv-theophyseval-2610.16733-2026-10-16.md
  - sources/arxiv-librarian-agents-2610.22273-2026-10-16.md
  - concepts/anticipatory-workspace-curation.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
wire_status: policy_wired
---

## Relations

- @sources/k292-osint-feeds-2026-10-16.md
- @sources/eval-url-multi-wiki-repository-2026-10-16.md
- @sources/arxiv-betinn-2610.19254-2026-10-16.md
- @sources/arxiv-theophyseval-2610.16733-2026-10-16.md
- @sources/arxiv-librarian-agents-2610.22273-2026-10-16.md
- @concepts/anticipatory-workspace-curation.md

## Raw Concept

**OSINT K292 wave, 2026-10-16.** 142 inbox files, but **only 22 distinct new sources**. Three osint source pages, one hub, one new concept. **Two arXiv papers were skipped as having no relevance** — see below. **No install. No trade. No scrape. No xsp/pm scp.**

## Narrative

### 1. DEFECT — the daily digest fans the same arXiv papers into all eight inboxes

**142 inbox files. 22 distinct new sources.**

The 16 arXiv PDFs in this drop are **byte-identical across all eight domain inboxes**. `scripts/daily_research_fetch.py` writes to `research to be indexed/<domain>/`, keyed on `CEMINI_WIKI_ID`, and there are **eight per-domain LaunchAgents** — but **`paper_queries` in `daily_research_config.yaml` is one global list.**

So eight scheduled runs execute the same queries and each fetches the same PDFs into its own namespace. The fetcher's docstring half-predicts this (*"Without it eight scheduled runs drop into one directory"*), but the namespace prevents **collisions**, not **duplication**.

**K291 confirms this is new.** That wave added 27 source pages and **no arXiv ID landed in more than one domain**. This wave would have produced 128 duplicate pages — 16 papers × 8 domains — of which 64 were already ingested.

**Two candidate fixes:** scope `paper_queries` per domain, or have the fetcher skip a paper another domain inbox already holds. **Not yet fixed.**

### 2. BeTINN — accurate prices do not imply accurate greeks

`arXiv 2610.19254`. A Heston physics-informed surrogate, and a measurement argument worth more than the architecture: **validation physics loss is informative but does not determine differential fidelity.** Accurate values coexist with localized Δ/Γ errors, concentrated near maturity at the KΓ peak and at low moneyness. Reference bars: PINN 0.00857 normalized price MAE, DeepONet 0.00974, a DeepSVM re-implementation 0.1258. **No code released — read and cite.** → `@sources/arxiv-betinn-2610.19254-2026-10-16.md`

### 3. TheoPhysEval — the memorisation signal

`arXiv 2610.16733`. 50 unpublished theoretical-physics problems, two harness tracks: **realistic** (web + tools) and **isolated** (local only). Pass rates 98% down to 42% across five agents at about **$2.33 per problem** for the winner. **Accuracy barely moves when web access is denied**, which the authors read as significant literature memorisation. **Run the same eval with and without retrieval — the delta is a memorisation estimate.** The paper's own caveat matters: Latent Space reported the benchmark's authors **confirming several reference solutions were wrong**. → `@sources/arxiv-theophyseval-2610.16733-2026-10-16.md`

### 4. Librarian Agents — the paper that names what this wiki is

`arXiv 2610.22273` (Stanford/CMU). Agents navigate filesystems well but are **rarely trained to build reusable workspaces for future use** — and the paper cites Claude Code as the harness where that asymmetry lives. A builder agent rewrites a flat corpus into hierarchical files plus reference links, trained with GRPO against a frozen answerer, rewarded by **answerability probes every 8 turns**. **+33 points** on BrowseComp-Plus, **+31** zero-shot on BRIGHT, **33.8% fewer tokens per correct answer**. Build costs ~179K tokens; the break-even is roughly **20 queries**. → `@concepts/anticipatory-workspace-curation.md`

### 5. Feeds — the numbers that matter

- **Kalshi holds 78% of trailing seven-day prediction-market notional.** $20.18bn against Polymarket US's $2.97bn. **Strip parlays and Kalshi still did $6.8bn — more than every other venue combined, parlays included.** Parlays are 64.2% of Kalshi volume and half of Polymarket US. → `@concepts/kalshi-retail-lp.md`
- **Google now bars prediction-market ads in Connecticut, Michigan, Nevada, New York and Ohio**, and has written the category into its main ads policy.
- **Consumer sentiment has stopped predicting spending** (Goolsbee, Chicago Fed). **53% of Michigan households cite higher prices as why they are worse off, against 7% in 2019.** CPI is 3.7% but the **price level is ~30% above January 2020**.
- **Bubble cohorts lose.** IT workers who joined during the 1990s tech bubble earned 5-10% more at the peak, and **7-8% less than comparable peers fifteen years after it**. → `@concepts/ai-productivity-fiscal-debt.md`
- **Joy of Destruction games: one in three people take money from another player for no personal gain, no knowledge and no reputational effect**, and take about 30%.
- **Crypto venue traffic +11.41% MoM** to 150.73m visits; **OKX now 22.0% against Binance's 23.0%**, with OKX's top visitor origin the USA. → `@concepts/crypto-venue-website-traffic.md`

### 6. Tool eval — both Integrate rows have no licence

`Integrate 2 · Extract 6 · Watch 1 · Context 5 · Pass 6 · UNAVAILABLE 0`. **Both Integrate rows (`morluto/leantoken`, `morluto/flameox`) are marked licence NOT FOUND**, and the docx's own friction note says to verify the morluto SPDX strings before redistribution. **An Integrate decision on an unread licence.** The on-topic core is small: the morluto MCP cluster, `xerj`, `parallel-cc` and Cap. → `@sources/eval-url-multi-wiki-repository-2026-10-16.md`

### 7. Skipped, and why

**Two papers were deliberately not ingested.** `arXiv 2610.18802` (branching explosion of Brownian Fleming-Viot systems) and `arXiv 2610.20896` (the Q-process for mother-dependent multitype branching) are **pure probability theory with no method, number, model or caveat usable in any lane of this federation**. Writing pages for them would be manufacturing relevance. `2610.18802` was already skipped once, in K291, for the same reason.

## Snippets

> Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time [Source: arXiv 2610.22273, abstract]

> Over the trailing seven days, Kalshi has done $6.8 billion in volume outside of parlays, which is more than all volume (parlays included) at all other exchanges combined. [Source: https://nexteventhorizon.substack.com/p/wide-chasm-between-kalshi-and-field (retrieved 2026-10-16)]

> People live in levels, not rates. [Source: https://kyla.substack.com/p/chicago-fed-president-austan-goolsbee-b24 (retrieved 2026-10-15)]
