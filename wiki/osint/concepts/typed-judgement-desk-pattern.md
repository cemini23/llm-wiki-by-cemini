---
title: Typed-judgement desk pattern — a decision engine inside an agent desk
type: concept
tags: [concept, agents, harness, jev, grok-bot, decision-engine, typed-judgement, k286]
keywords: [typed-judgement, jev, typesafe, noul, choice, score, kill-order, shadow-mode, rejection-bench, question-sets, grok-bot]
related:
  - sources/x-post-savipww-megabrain-jev-grok-bots-2026-09-23.md
  - entities/tools/jev-mcp.md
  - entities/tools/grok-bot.md
  - concepts/grok-bot-operator-patterns.md
  - concepts/agent-tool-use-verification.md
  - concepts/agent-harness-verification-bottleneck.md
  - sources/substack-rss-latent-space-2026-10-10-typesafe-jev-100m-arr.md
  - concepts/k288-feeds-wave.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- @sources/x-post-savipww-megabrain-jev-grok-bots-2026-09-23.md — the published instance (memecoin desk)
- @entities/tools/jev-mcp.md — our live Jev wiring (laptop)
- @entities/tools/grok-bot.md — the execution lane
- @concepts/grok-bot-operator-patterns.md — our charter synthesis and constraints
- @concepts/agent-tool-use-verification.md — the verifier is a first-class object
- @concepts/agent-harness-verification-bottleneck.md — where the desk can be trusted

## Raw Concept

What this page answers: how do you put a **typed decision engine** inside an agent desk so the agents stop judging in prose? Synthesized from the `@savipww` Jev + Grok Bot guide and our own Jev/Grok Bot pages.

## Narrative

### The pattern in one line

**Code fetches. The engine judges. Code decides.** The agents neither fetch their own facts nor decide the final action — they fill seats around a **typed judgement call**.

### Why "typed" matters

A text model asked to judge returns prose the caller must parse, and prose has no contract. A **typed** engine returns a structured answer with a **probability**, in a fixed schema, in tens of milliseconds:

- **`noul`** — an if: a yes/no with a probability.
- **`choice`** — a switch: pick one of N options (up to 255).
- **`score`** — a sort: rank candidates.

The caller reads a **number**, applies a **threshold**, and writes no parser. This is the same distinction as an API returning a string versus returning an integer.

### The four design rules

1. **Arithmetic stays in code.** Every number is computed before the call and passed in as a field. The engine never does maths; it only judges. This is what removes the model's own opinion from the loop.
2. **Facts kill before judgements do.** The filter is a **kill order**, cheapest first:
   - `free_kill` — no network, runs on hundreds (fields already in hand).
   - `trade_kill` — one external call, runs on tens.
   - `chain_kill` — one rate-limited call, runs on a few.
   - `soft_kill` — one judgement call, runs on a handful.
   Plain comparisons (a honeypot flag, an authority-open flag) are **code, not questions**.
3. **Question sets, not single questions.** State is **charged once per call**; output is free. Grouping questions into a set is **3–4× cheaper** than one call per question, for the same answers.
4. **Shadow mode with disagreement rows.** Run in shadow; log one row per would-be action with every answer, the model id, the rejection counters, and **what the old logic did with the same inputs**. Read only the rows where the two **disagree** — that is where the thresholds come from.

### The state the desk must remember

- **One action at a time.** A guard, or the desk accumulates positions nobody sized.
- **A rejection bench, with variable expiry.** A rejected candidate stays rejected — but not for a fixed length. A hard flag never becomes false; "too early to tell" becomes tellable within the hour.

### Where this fits our stack

We already hold **both halves**: Jev on the laptop (@entities/tools/jev-mcp.md) and 19 Grok Bot charters (@concepts/grok-bot-operator-patterns.md). **They are not connected.** Verified 2026-10-08: no charter mentions Jev.

| Desk half | Us today | The pattern |
|-----------|----------|-------------|
| Fetch | Bot plugins + laptop CLIs | code fetches; the model never fetches |
| **Judge** | **the Bot judges in prose** | **a typed engine judges (noul/choice/score)** |
| Decide | the Bot | code applies the threshold |
| Remember | per-desk files | one-position guard + rejection bench |

**The gap is the judge row.** Our seats take the model's prose opinion; the pattern replaces it with a typed probability.

### What is reusable and what is not

**Reusable:** the whole shape — typed judgement, kill order, question sets, shadow mode, the rejection bench.

**Not reusable, and out of bounds:**
- The **trading egress**. Our standing rule forbids **trading egress from the Grok Bot VM** (@concepts/grok-bot-operator-patterns.md). The desk here executes on a memecoin venue; ours must not.
- The **constants.** "Copy the shape, not the constants" — the thresholds are the author's, tuned on his risk tolerance.
- The **track record.** Six figures is unverified, and the post carries referral links.

### Safe places to apply it here

1. **GuruWatcher claim extraction** — `noul` on "is this a claim or a level?", `score` over candidate watches. Alert-only, no egress.
2. **Parlays / DFS analysis** — `score` over legs; the operator still types the ticket.
3. **XSP signal triage** — `score` over setups; no order.
4. **Eval and audit gates** — `noul` on "does this change meet the success criteria?" — the same shape as the wiki's own audit verdicts.

All four are **advisory**. The engine advises; code decides; a human submits.

### Boundary

FILE only. **No trading egress from any agent VM.** **No `/route` swap** — the engine is a judgement service, not a model router. No key in git.

## K288 — the pattern became an industry category (2026-10-10)

Two days after this page was written, the pattern became a **product category**.

**TypeSafe/Jev: >$100M ARR, $7.5B valuation, three weeks after launch.** In the same week: an **OpenAI Decisions API** (probability / pick / score, $0.10/M input, no output charge), **Microsoft-Decision-1**, **Perplexity `pplx-decider-v1.1-27b`** (94.5% Decision Bench, $0.017/1K), **Cloudflare `clef`** (`clef-flash` cheaper than Jev), **Liquid `d1`**, and **vLLM Semantic Router Decision 2.0** (multiple questions, per-option probabilities, one pass).

**The recipe is now portable.** **Unsloth** turns **Qwen3.5-4B into a decision model on 8GB VRAM**; a Qwen3.5-0.8B walkthrough reports **37% → 65% in 60 steps (~10 min on 4GB)**. You do not need the vendor API to run the desk.

**The economics are now measured.** LangChain reports that **routing each task to the cheapest adequate model cut median Open SWE cost per task by 64%.** The `noul`/`choice`/`score` split is exactly that routing, moved inside the desk.

**Two cautions from the same wave.** Decision models **still struggle on consistency and complex decisions** (early Microsoft-Decision-1 evaluation). And **agent teams cost 1.8–5.1× more** for little gain (Vals AI: only Sol at medium effort improved, +7.3; Opus's sequential waves showed no significant gain). **The judge is worth it; a bigger team of judges is not.**

[Source: @sources/substack-rss-latent-space-2026-10-10-typesafe-jev-100m-arr.md]
