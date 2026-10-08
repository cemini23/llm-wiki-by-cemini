---
title: "X post @savipww — Megabrain (Jev) & Six Grok Bots desk (2026-09-23)"
type: source
tags: [source, k286, trading, agents, jev, grok-bot, memecoins, typed-judgement]
keywords: [savipww, jev, typesafe, grok-bot, fomo, geckoterminal, dexscreener, noul, choice, score, typed-judgement, shadow-mode, kelly-desk]
related:
  - concepts/typed-judgement-desk-pattern.md
  - entities/tools/grok-bot.md
  - entities/tools/jev-mcp.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/typed-judgement-desk-pattern.md
- @entities/tools/grok-bot.md
- @entities/tools/jev-mcp.md

## Raw Concept

| Title | Megabrain (Jev) & Six Grok Bots That Already Made Me Six Figures (Setup Guide) |
| Author | @savipww (X) — "20 | deep into AI & Quant since 2022" |
| Type | Twitter Article (long-form) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/x-post-savipww-megabrain-jev-grok-bots-2026-09-23.md` |
| URL | https://x.com/savipww/status/2102720919185617314 |
| Retrieved | 2026-10-08 (via `opencli twitter article`) |
| Posted | 2026-09-23 · ~889 likes |
| Follow-on | The author's **original** six-bot guide (three weeks earlier) does the execution layer; this one adds the **judge** layer |
| read-status | read |

## Narrative

A **memecoin trading desk** built from **Jev** (typed judgement) and **six Grok Bot seats** (execution). The author claims six figures — **unverified, and this is a promotable setup guide with referral links** (FOMO venue, Telegram). Read it as a *pattern*, not a track record.

### The central move

> "every judgement on the desk is now a **typed number with a probability on it**, instead of prose my code had to parse."

**Jev** (TypeSafe) **does not generate text.** You send **state + typed questions**; it returns **typed answers with probabilities** in **70–500 ms**. The whole API is three question types:

- **`noul`** — an if (yes/no with a probability).
- **`choice`** — a switch (pick among options).
- **`score`** — a sort (rank candidates).

The design rule the author repeats:

> "**Code fetches, the model judges, code decides.** A seat that computes does not get a judge call. A seat that judges does not get a calculator."

Every number is computed **before** the call and passed in as a **field** — the model never does arithmetic.

### The pipeline

`collect.py` (SCAN + VET) gathers pools from **GeckoTerminal** (free, 10 calls/min), metrics from **FOMO** (session-scraped — FOMO has no public API), trade counts from **DexScreener**, and chain data (Solana / BSC / Robinhood). It builds the state → `judge.py` holds the **only** Jev key → `questions.py` holds every question, grouped into **sets** → `thresholds.py` + `filter.py` apply a **kill order** → **SOCIAL** (Grok Bot's X plugin *reads*; Jev *judges*) → `pick.py` (one `Choice` over the ≤10-token shortlist) → handoff to the six Grok Bot seats (**SIZE, FILLS, RISK**) → `book.py` (SQLite: one position at a time, plus a **rejection bench**) → `main.py` (the 15-minute cycle; `shadow=True` for a week).

### The four design ideas worth stealing

1. **Filter kill-order: facts kill before judgements.** `free_kill` (no network, runs on hundreds) → `trade_kill` (1 DexScreener call, on tens) → `chain_kill` (a GeckoTerminal slot) → `soft_kill` (a Jev call, on a handful). Plain comparisons (honeypot, authority-open) are code, **not** questions.
2. **Shadow mode + disagreement rows.** `shadow=True` logs one row per would-be trade with every answer, the model id, the rejection counters, **and what the old logic did with the same candidates**. "Read only the rows where the two disagree." The thresholds come from that review.
3. **A rejection bench.** A rejected token stays rejected — but **not for one fixed length**: a honeypot flag never becomes false, while "too early to tell" becomes tellable within the hour.
4. **Question sets, not single questions (the cost lever).** State is **charged once per call**; output is free. Splitting a set into one call per question costs **3–4×** for identical answers because the state is re-charged each time.

### The budget

**Under six cents a day.** Three dossiers per cycle → three tokens reach the judge → three calls each (market, chain, social) + one pick over survivors = **~10 calls at ~1,400 input tokens each**. The rate limit *is* the design: GeckoTerminal's 10/min gives 6 listing calls across 3 chains, leaving 3 dossier slots.

### The author's own caveat

> "**This is my setup, not your strategy!!!** Every threshold above is mine … Copy the shape, not the constants!"

Also: "A desk that trades every cycle is a desk with no filter." And the FOMO bearer lives ~1 hour, so the client must refresh from the browser at the top of every cycle.

### Why it matters here

This is the **clearest published statement of the typed-judgement desk pattern** — and it is the missing half of our own Grok Bot setup. We run Jev on the laptop (`jev-mcp`) and we run 19 Grok Bot charters; **no charter mentions Jev** (verified 2026-10-08: `grep jev` over `briefs/2026-09-01_grok-bot-charters.md` returns nothing). See @concepts/typed-judgement-desk-pattern.md.

**Replication caveat:** the trading half is **out of bounds** — our standing rule forbids **trading egress from the Grok Bot VM** (@concepts/grok-bot-operator-patterns.md). The **judgement half** is portable.

## Snippets

> "Jev does not generate text at all. You send it state and typed questions, it sends back typed answers with probabilities in 70 to 500ms." [Source: x-post-savipww-megabrain-jev-grok-bots-2026-09-23.md]

> "Code fetches, the model judges, code decides. A seat that computes does not get a judge call. A seat that judges does not get a calculator." [Source: x-post-savipww-megabrain-jev-grok-bots-2026-09-23.md]

> "Under six cents a day for every judgement the desk makes." [Source: x-post-savipww-megabrain-jev-grok-bots-2026-09-23.md]

> "This is my setup, not your strategy!!! … Copy the shape, not the constants!" [Source: x-post-savipww-megabrain-jev-grok-bots-2026-09-23.md]
