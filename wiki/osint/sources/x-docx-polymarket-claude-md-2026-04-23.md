---
title: "X.docx — Polymarket Weather Bot Technical Breakdown + 12-Rule CLAUDE.md Template (X-thread compilation, late April 2026)"
type: source
tags: [x-thread-compilation, polymarket-weather-trading, gamma-api, claude-md-template, claude-code-prompting, karpathy, forrest-chang, agent-orchestration, k41]
keywords: [alteregoeth-weather-bot, gamma-api-events-slug, gamma-api-markets, polymarket-temperature-bins, regex-bin-parsing, sentinel-values-edge-buckets, claude-md-12-rule-template, karpathy-4-rules, forrest-chang, mnilax, simplicity-first, surgical-changes, goal-driven-execution, token-budget-30000, checkpoint-discipline, fail-loud-rule, model-judgment-only-rule, convention-over-novelty]
related:
  - entities/people/alteregoeth.md
  - entities/people/mnilax.md
  - entities/people/forrest-chang.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/claude-md-12-rule-template.md
  - concepts/polymarket-market-making-architectures.md
  - sources/x2-docx-polymarket-theparuchh-2026.md
maturity: draft
read_status: read
created: 2026-05-13
updated: 2026-05-13
clusters: [prediction-markets, llm-agents, methodology]
---

## Relations

- @entities/people/alteregoeth.md — author of Section 1 (Polymarket weather-bot Gamma API technical breakdown)
- @entities/people/mnilax.md — author of Section 2 (12-rule CLAUDE.md template article)
- @entities/people/forrest-chang.md — author of the original 4-rule CLAUDE.md template Mnilax extends to 12; original repo claimed at 120k stars in May 2026
- @concepts/polymarket-weather-trading-strategy.md — concept page housing both the @AlterEgo_eth and @theparuchh approaches as a single strategy family
- @concepts/claude-md-12-rule-template.md — concept page housing Mnilax's 12-rule expansion of Karpathy → Forrest Chang template
- @concepts/polymarket-market-making-architectures.md — sibling architectural pattern; weather-bot is a Polymarket-specific-domain instance of broader market-making patterns
- @sources/x2-docx-polymarket-theparuchh-2026.md — companion source; @theparuchh deeper guide to same weather-bot strategy class

## Raw Concept

- **Title**: untitled X-thread compilation (two unrelated long-form X posts pasted into a single .docx)
- **File**: X.docx
- **Length**: ~49,707 chars (after XML strip)
- **Source platform**: x.com (Twitter); thread quotes
- **Date**: late April 2026 (Section 1 references May 15 forecast example; Section 2 references "May 2026 Claude Code ecosystem")
- **PDF location (post-scp)**: `cemini-librarian:/opt/cemini-bulk/research/X-polymarket-claude-md-2026-04-23.docx`
- **sha256**: `db7f050dbaf7ad5b...` (preingest verdict: NEW)
- **Size**: 31,947 bytes
- **Read status**: read (full document, both sections)
- **Discovered via**: user drop into `research to be indexed/` 2026-05-12

## Narrative

### Section 1 — @AlterEgo_eth Polymarket weather-bot Gamma API breakdown

Technical decomposition of a Polymarket weather-trading bot using **only two Gamma API endpoints**:

1. **Slug construction pattern**: `highest-temperature-in-{city}-on-{month}-{day}-{year}` (e.g. `highest-temperature-in-seoul-on-may-15-2026`). This is the canonical Polymarket slug shape for daily-city high-temperature markets and lets the bot find the exact event without iterating through all events.

2. **Endpoint #1 — Event-by-slug**: `GET https://gamma-api.polymarket.com/events?slug={slug}` returns an array of events; first element contains all markets for that event (one market per temperature bin: market_id + question text + price).

3. **Bin parsing**: question text like `"Will the high temperature in Seoul be between 22-23°C on May 15?"` or `"28°C or higher"` / `"15°C or below"`. Regex extracts lower/upper bin boundaries. **Edge buckets**: sentinel values `-999` (lower) and `999` (upper) for "or below" / "or higher" buckets.

4. **Endpoint #2 — Market price**: `GET https://gamma-api.polymarket.com/markets/{market_id}` returns `outcomePrices` as a JSON string with two prices (YES, NO). `prices[0]` = YES price = market-implied probability.

5. **No auth required on either endpoint** — both are public.

This is the **clean technical breakdown** of the strategy that @theparuchh in the companion source describes the *operational guide* for.

### Section 2 — @Mnilax 12-Rule CLAUDE.md Template

Forrest Chang took Andrej Karpathy's late-January-2026 thread complaining about Claude code-writing failures, packaged the complaints into 4 behavioral rules in a single CLAUDE.md, dropped on GitHub. **Repo grew to 5,828 stars first day, 60,000 bookmarks in 2 weeks, 120,000 stars by May 2026** — claimed fastest-growing single-file repo of 2026.

Mnilax tested the 4 rules over 30 codebases / 6 weeks, found mistakes dropped from ~40% to ~3% on tasks that played to their strengths. **But template was built to fix code-writing mistakes from January 2026; May 2026 ecosystem has new problems** — agent fights, hook cascades, skill loading conflicts, multi-step workflows breaking across sessions. Mnilax added 8 more rules.

#### Karpathy → Forrest Chang original 4 rules

| # | Rule | Core idea |
|---|------|-----------|
| 1 | Think Before Coding | No silent assumptions; state what you're assuming; surface tradeoffs; push back when simpler approach exists |
| 2 | Simplicity First | Minimum code that solves the problem; no speculative features; no abstractions for single-use code |
| 3 | Surgical Changes | Touch only what you must; don't "improve" adjacent code; don't refactor what isn't broken |
| 4 | Goal-Driven Execution | Define success criteria; loop until verified; tell Claude what success looks like, not what steps to follow |

#### Mnilax 8 added rules (May 2026 agent orchestration)

| # | Rule | Headline |
|---|------|----------|
| 5 | Use model only for judgment calls | Use LLM for classification/drafting/summarization/extraction; **do NOT** use for routing/retries/status-code handling/deterministic transforms |
| 6 | Hard token budgets, no exceptions | Per-task 4,000 tokens; per-session 30,000 tokens. If approaching budget, summarize and start fresh. **Surfacing the breach > silently overrunning** |
| 7 | Surface conflicts, don't average them | If two existing patterns contradict, **pick one** (more recent/more tested), explain why, flag the other. "Average" code is the worst code |
| 8 | Read before you write | Read file's exports, immediate caller, shared utilities before adding. "Looks orthogonal to me" = most dangerous phrase |
| 9 | Tests verify intent, not just behavior | Every test must encode **why** the behavior matters. Test that can't fail when business logic changes = function is wrong |
| 10 | Checkpoint after every significant step | Multi-step task: summarize done / verified / left. Don't continue from a state you can't describe back |
| 11 | Convention beats novelty | Match codebase conventions even if you disagree. Disagreement is a separate conversation. Conformance > taste. |
| 12 | Fail visibly, not silently | "Migration completed" wrong if 30 records skipped silently. Default to surfacing uncertainty, not hiding it. |

Empirical claim (Mnilax): tracking 50 representative tasks across 30 codebases for 6 weeks across three configurations (Karpathy 4 / Mnilax 12 / no template) showed mistake rate of 41% → 3%, compliance 78% → 76%. Going from 4 → 12 rules **added almost no compliance overhead** but cut mistake rate by 8 additional points because new rules cover failure modes original 4 didn't address.

Claimed gap-areas where Karpathy 4 silently break:
1. Long-running agent tasks (no budget/checkpoint/fail-loud)
2. Multi-codebase consistency (no rule for picking among styles)
3. Test quality (treats "tests pass" as success without meaningfulness check)
4. Production vs prototype (Simplicity First overfires on early-stage code)

Mnilax tested more than 12 rules: at 14+ rules, compliance dropped 76% → 52%. The 200-line ceiling for CLAUDE.md effectiveness held.

### Cemini relevance

- **Section 1 is operational gold for Cemini's Polymarket work**: the slug pattern + two-endpoint API + bin-regex + sentinel values is implementation-ready for adding Polymarket-weather-market coverage to Cemini's prediction-market stack. Pair with @sources/x2-docx-polymarket-theparuchh-2026.md for the operational guide (weather-station coordinates, bias-correction parameter, entry windows).
- **Section 2 is direct guidance for Cemini's own CLAUDE.md hygiene**: Cemini's CLAUDE.md is 322 lines as of K41 ingest (well over the 200-line ceiling Mnilax warns about). Rule 5 (model judgment only) + Rule 10 (checkpoint discipline) + Rule 12 (fail loud) are particularly relevant to Cemini's agent stack.
- **Cross-source corroboration**: Mnilax's Rule 10 (checkpoint discipline) is the operational sibling of @sources/llms-get-lost-multi-turn-laban-2025.md's measured failure mode (39% multi-turn perf drop, premature-commitment mechanism). One paper measures the failure, one X-thread prescribes the discipline.
- **Author signal posture**:
  - @AlterEgo_eth — verified technical content; specific endpoints + auth-free claims independently verifiable
  - @Mnilax — empirical claims (30 codebases / 6 weeks / 41% → 3% mistake rate) are author-asserted; not independently reproducible without the testing harness. Treat compliance numbers as illustrative not measured.
  - Forrest Chang — original 4-rule repo **`[CONFIRMED 2026-05-29]`** — `forrestchang/andrej-karpathy-skills` ~130k+★ (see @entities/people/forrest-chang.md); 60k bookmarks / "fastest single-file repo" remain `[TENTATIVE]`.
  - Andrej Karpathy — January 2026 X thread is the upstream source; not in this document, only second-hand description

## Snippets

> "Polymarket names events using a standard pattern. For each city and date the bot builds a slug like this: highest-temperature-in-{city}-on-{month}-{day}-{year}. Example: highest-temperature-in-seoul-on-may-15-2026" [Source: X.docx Section 1, @AlterEgo_eth]

> "Edge buckets get sentinel values: -999 for the lower boundary of 'or below' and 999 for the upper boundary of 'or higher'" [Source: X.docx Section 1, @AlterEgo_eth]

> "Rule 5 — Use Claude for: classification, drafting, summarization, extraction from unstructured text. Do NOT use Claude for: routing, retries, status-code handling, deterministic transforms." [Source: X.docx Section 2, @Mnilax]

> "Rule 12 — Fail loud: If you can't be sure something worked, say so explicitly. 'Migration completed' is wrong if 30 records were skipped silently. 'Tests pass' is wrong if you skipped any. 'Feature works' is wrong if you didn't verify the edge case I asked about. Default to surfacing uncertainty, not hiding it." [Source: X.docx Section 2, @Mnilax]

## Dead Ends

- Did NOT verify "fastest single-file repo of 2026" claim; star count **`[CONFIRMED 2026-05-29]`** via @entities/people/forrest-chang.md (~130k+★).
- Did NOT verify Karpathy's January 2026 X thread directly; the thread content is described second-hand by Mnilax
- Mnilax's empirical-comparison numbers (41% → 3% mistake rate, 78% → 76% compliance over 30 codebases / 6 weeks) are **author-asserted**, not in any published methodology document Cemini has visibility on. Treat as illustrative.
