---
title: "Sports-prediction consensus agent — multi-source analytical consensus as Polymarket entry signal"
type: concept
tags: [concept, polymarket, sports-trading, consensus-signal, claude-agent, firecrawl, kelly-sizing, k55]
keywords: [sports-consensus-agent, firecrawl-scraping, claude-sonnet-extraction, tier-weighted-sources, consensus-strength, edge-gate-7pp, kelly-fraction-conservative, 6pct-hard-cap, stacyonchain, centpro-bot, 5-source-analytics, polymarket-sports-trading]
related:
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - concepts/ai-assisted-trading-workflow.md
  - concepts/polymarket-bot-architecture.md
  - concepts/kelly-sizing-quarter.md
  - entities/people/stacyonchain.md
  - entities/tools/centpro.md
  - entities/tools/firecrawl.md
  - entities/platforms/polymarket.md
  - concepts/agentic-time-machine-forecasting-eval.md
  - sources/arxiv-agentic-time-machine-2606.21013-2026-06-23.md
  - sources/youtube-kalshi-bots-batch-2026-05-29.md
  - entities/tools/momentum-odds.md
  - entities/platforms/kalshi.md
  - entities/tools/polygnosis.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
maturity: validated
created: 2026-05-20
updated: 2026-06-23
clusters: [polymarket, agents, sports]
---

## Relations

- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — Post 4 (@stacyonchain) primary source
- @concepts/ai-assisted-trading-workflow.md — this concept extends the AI-assisted preparation layer with a research-and-consensus agent
- @concepts/polymarket-bot-architecture.md — Step 4 (entry sizing + risk caps) inherits from the broader bot architecture
- @concepts/kelly-sizing-quarter.md — Kelly fraction reference; this concept uses a conservative 0.12-0.20 fraction
- @entities/people/stacyonchain.md — author
- @entities/tools/centpro.md — the commercial productized form the author sells; the recipe in this concept is the open architecture
- @entities/tools/firecrawl.md — the scraping layer used to feed the agent
- @sources/youtube-kalshi-bots-batch-2026-05-29.md — K80 Beast Sports + MomentumOdds videos
- @entities/tools/momentum-odds.md — commercial 60+ sportsbook signal feed (webhook executor pattern)
- @entities/platforms/kalshi.md — Kalshi sports totals/moneylines as execution venue

## Raw Concept

What prompted this page: K55 Posts.docx Post 4 — @stacyonchain's "How to Build a Claude Agent for Sport Predictions." Documents a multi-source consensus-as-signal architecture that's directly applicable to sports markets on Polymarket. Promoted alongside a paid productized version (centpro.bot, K55 multi-wiki tool eval URL 4 — Reject), but the architecture itself is the useful artifact and is openly described.

## Narrative

### Thesis

A single analyst saying "Team A wins 65-35" is approximately noise. **Five independent analytical sources** — different platforms, different methodologies, no financial relationship — all converging on the same directional view is signal worth acting on. The agent's job is to find that consensus automatically across the published sports-analytics universe, score how strong and aligned it is, and **flag only entries that cross a threshold**.

The agent does *not* try to predict outcomes. It synthesizes consensus from the published outputs of people who do.

### Architecture — 4 stages

```
SOURCES → [stage 1: scrape via Firecrawl] → raw articles
       → [stage 2: per-article extraction via Claude] → structured signals (JSON)
       → [stage 3: cross-source consensus via Claude] → consensus envelope
       → [stage 4: entry evaluator] → SKIP / ENTER (YES/NO, size)
```

#### Stage 1 — Data layer (Firecrawl)

JS-rendering scraper required because most sports-analytics platforms render via SPA frameworks. Curated source list with **tier weights**:

| Tier | Sources |
|---|---|
| 1 (most credible) | OptaAnalytics, FBref, Understat, WhoScored |
| 2 | SofaScore |

Tier represents *editorial / methodological credibility* — an Opta statistical model carries more weight than a fan-blog form table. Each scrape pulls `max_results=2` per source per match, trimmed to 2,000 chars/article for token efficiency.

#### Stage 2 — Per-article signal extraction

Claude Sonnet 4.5, one call per article. **The critical constraint**: "Do not add your own analysis. Extract only what is written." The prompt asks for:

```json
{
  "favored_team": "<team_a|team_b|neutral>",
  "confidence": 0.0,         // analyst's expressed confidence
  "primary_factors": [],     // max 3 factors cited
  "risk_factors": [],        // injuries, weather, lineup issues
  "stated_probability": null // or float if explicit
}
```

This is pure extraction, not inference. The agent is faster + more consistent than a human, but not smarter; it is reading what *humans* concluded.

#### Stage 3 — Consensus synthesis

Single Claude call ingesting all per-source signals. Computes:

```json
{
  "consensus_team": "<...>",
  "consensus_strength": 0.0-1.0,
  "weighted_probability": 0.0-1.0,
  "source_count": int,
  "dissenting_count": int,
  "shared_risks": [],
  "signal_quality": "strong|moderate|weak|skip"
}
```

**Signal-quality rules** (from the @stacyonchain post):
- **Strong**: strength ≥ 0.72, ≥5 sources, ≤1 dissent
- **Moderate**: strength ≥ 0.60, ≥3 sources
- **Weak / skip**: everything else

#### Stage 4 — Entry evaluator (gates + Kelly)

```python
def evaluate_entry(consensus, polymarket_price, bankroll):
    # Gate 1: signal quality
    if consensus["signal_quality"] not in ["strong", "moderate"]:
        return SKIP("insufficient consensus")

    p_agent = consensus["weighted_probability"]
    edge = p_agent - polymarket_price

    # Gate 2: minimum edge threshold
    if abs(edge) < 0.07:
        return SKIP("edge below 7pp")

    # Gate 3: Kelly sizing
    b = (1 - polymarket_price) / polymarket_price
    f_raw = (p_agent * b - (1 - p_agent)) / b

    # Conservative fraction
    fraction = 0.20 if consensus["signal_quality"] == "strong" else 0.12
    size = min(bankroll * f_raw * fraction, bankroll * 0.06)  # 6% hard cap

    return ENTER(side, size, edge, ...)
```

Three independent gates:
- **Signal-quality gate** (Stage 3 must produce strong or moderate).
- **Minimum-edge gate** (`|p_agent − market| ≥ 7pp`).
- **Kelly + hard cap** (`min(kelly × fraction, 0.06 × bankroll)`).

The 6% hard cap is **non-negotiable regardless of how strong the consensus looks**. Consensus is not outcome certainty — 6 analysts agreeing on expected goals doesn't prevent a 90th-minute set-piece goal for the other team. Tail risk is real on every individual match.

### Author's reported findings (single-source [TENTATIVE])

- Strong consensus signals (strength ≥ 0.72, ≥6 sources aligned) appear on **~15-20%** of matches analyzed. The remaining 80-85% are filtered out as weak consensus or active disagreement. **The filtering is the point.**
- **Consensus strength predicts better than consensus direction.** Six sources at 0.78 strength favoring the underdog outperforms four sources at 0.61 strength favoring the favorite. The count + tightness of independent convergence matters more than which side.
- Operational cost: **<$30/month** in API + scraping credits for the entire system. Cheap to run.

### Limitations

- Works only on **publicly published** analysis. The agent has no edge over participants with insider information (private lineups, locker-room reports). It's a **systematic research layer**, not an information-edge engine.
- Tier weights are subjective and the author's specific tier-1 list (Opta, FBref, Understat, WhoScored, SofaScore) is football-specific. Generalizing to NBA, NFL, MLB requires re-curating the source list with sport-specific tier weights.
- The agent's "consensus" is only as independent as the sources actually are. If FBref and Understat are both citing the same underlying xG model, that's not 2 independent sources — it's 1 model + 1 reframing. **Source-independence audit** should be done as part of source-list curation, not assumed.

### Cemini fit

**Cemini-relevant — adjacent to existing Polymarket workstreams**.

Current Cemini Polymarket coverage is heavy on weather + UpDown + arb (3-4 concept pages). Sports markets are a major Polymarket category not yet explicitly covered. This architecture maps cleanly onto a Cemini Polymarket sports adapter:
- **Sources**: the curated tier-weighted source list is portable; the scraper layer (Firecrawl) is already a candidate tool to adopt — see `@entities/tools/firecrawl.md`.
- **Claude extraction stage**: matches Cemini's existing analyst-node pattern; signal extraction is a per-article LLM call with structured JSON output.
- **Consensus stage**: lightweight; one LLM call per match.
- **Entry stage**: gates + Kelly + hard cap pattern is identical to other Cemini strategies; just plug in different parameters.

**Estimated build effort** (rough): low — most of the components already exist in the Cemini stack; the work is source-list curation + per-sport tier-weighting + sport-specific scraping rules + the sports-market discovery layer on top of Polymarket Gamma API.

**Caveat on the @stacyonchain promotion**: the author promotes `centpro.bot` (15/50 spots, $49/mo subscription, closed-source Windows binary) as the productized form. **CentPRO is Rejected** (K55 tool eval URL 4 — see `@entities/tools/centpro.md`). The recipe in this concept is the open architecture; the bot for sale is the gated implementation. The recipe is useful regardless.

### K80 — sportsbook line vs prediction-market line [TENTATIVE]

Two K80 YouTube videos describe a **simpler cousin** of full multi-source consensus:

| Pattern | Source | Mechanism |
|---------|--------|-----------|
| **Totals divergence** | Beast Sports Picks (`iF6ZWEbkxzM`) | Scraper compares Kalshi/Polymarket O/U line (e.g. 202) vs sportsbook consensus (e.g. 217) — buy PM line when implied win rate high vs book anchor |
| **Sportsbook correlation feed** | MomentumOdds + Odds channel (`qPRY5ws3h60`) | SaaS aggregates 60+ books → webhook → local Kalshi bot |

Architecturally this is **Stage 3 collapsed**: an external vendor already computed consensus; the bot only maps game → Kalshi ticker + sizes the bet. Same entry gates (edge threshold, exposure cap) apply. Cross-venue: Kalshi and Polymarket both listed for NBA/college totals in Beast Sports demo.

## Snippets

> "A single analyst saying 'Team A wins this 65-35' means relatively little. Five independent sources — different platforms, different methodologies, no financial relationship to each other — all converging on the same directional view? That's signal worth acting on." [Source: Posts.docx — Post 4, @stacyonchain]

> "Do not add your own analysis. Extract only what is written. Output JSON only: {favored_team, confidence, primary_factors, risk_factors, stated_probability}." [Source: Posts.docx — Post 4, @stacyonchain]

> "The most useful thing I learned: consensus strength predicts better than consensus direction. Six sources aligned at 0.78 strength favoring the underdog outperforms four sources at 0.61 strength favoring the favorite." [Source: Posts.docx — Post 4, @stacyonchain]

> "The 6% hard cap per position is non-negotiable regardless of how strong the consensus looks. Analytical consensus is not outcome certainty — six analysts agreeing on expected goals doesn't prevent a 90th-minute set piece goal for the other team." [Source: Posts.docx — Post 4, @stacyonchain]

> "Strong consensus signals — strength above 0.72, six or more sources aligned — appeared on roughly 15–20% of matches analyzed. The remaining 80-85% either produced weak consensus or direct disagreement across sources. That filtering is the point." [Source: Posts.docx — Post 4, @stacyonchain]
