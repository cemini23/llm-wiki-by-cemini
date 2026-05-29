---
title: X — Kimi K2.6 routing playbook for Hermes (May 2026)
type: source
tags: [source, x, kimi, moonshot, claude, opus, hermes, agent-routing, cost-optimization, llm]
keywords: [kimi k2.6, moonshot, opus 4.7, SWE-Bench Pro, agentic, model orchestra, thinking mode, scope lock, /model, OpenRouter, auxiliary models, Modified MIT]
related:
  - concepts/agent-cost-routing-model-orchestra.md
  - entities/models/kimi-k2-6.md
  - entities/models/opus-4-7.md
  - entities/tools/hermes-agent.md
maturity: validated
read_status: deep-read
created: 2026-05-12
updated: 2026-05-29
---

## Relations

- `@concepts/agent-cost-routing-model-orchestra.md` — distilled architecture concept
- `@entities/models/kimi-k2-6.md` — Kimi K2.6 model entity
- `@entities/models/opus-4-7.md` — Opus 4.7 model entity (sibling)

- `@entities/tools/hermes-agent.md` — Hermes platform entity (Nous Research)

## Raw Concept

- **Title**: "Open your Hermes billing dashboard. Look at last month."
- **Author**: unspecified X handle (long-form thread, ~7 parts)
- **Source filename**: `hermes x post.docx`
- **Sha256**: `0d3e4eb6dfc7c78c...`
- **Size**: 13,356 bytes
- **Retrieved**: 2026-05-12
- **Read status**: deep-read
- **External handle cited**: `@nrehiew_` (referenced for the Zig inference engine war story, Apr 20 tweet)
- **Location** (canonical): `cemini-librarian:/opt/cemini-bulk/research/hermes x post.docx`

## Narrative

Long-form X post on routing tasks across multiple LLMs ("model orchestra") rather than defaulting every task to Opus 4.7. Centered on **Kimi K2.6** (Moonshot AI, April 2026 release) as a SWE-Bench-Pro-leading coding workhorse at ~1/10th Opus pricing.

### 7-part structure

1. **What Kimi K2.6 actually is** — 1T total / 32B active MoE; Modified MIT (commercial trigger at 100M MAU OR $20M/mo); SWE-Bench Pro 58.6% (beats GPT-5.4 + Opus 4.6); HLE-Full-with-tools 54.0% (beats every closed Western frontier); 12+ hour autonomous sessions; ~35% fewer steps than K2.5.
2. **War stories** — Zig inference engine (Qwen3.5 0.5B, 12h, 4000+ tool calls, 20% faster than LM Studio); Exchange-Core trading engine tuning (13h, 4000 LOC, ~3× throughput); KiloClaw (Kilo Code CEO's published 13h / 1000+ tool calls / 185% throughput improvement).
3. **Wiring into Hermes** — `/model openrouter:moonshotai/kimi-k2.6` or `/model moonshot:kimi-k2.6`; self-hosted on single 8×H100.
4. **Auxiliary model pattern** — five-model orchestra (main brain / hard escape / compression / title generation / vision / embeddings). Default-Opus routes title-generation through the most expensive model on the market.
5. **Two cost traps** — thinking-mode bloat (3.6× output token inflation per Artificial Analysis), drift (cheap → operator stops watching → scope creep). Fix: `/reasoning off` + scope-lock prompt header.
6. **When to swap** — Kimi for code/agent/test/refactor/UI/CRUD; Opus for ambiguous specs / multi-stack / hard math / legal/medical/financial.
7. **Kimi-first skills + escalation template** — 5-step adversarial-pass-then-escalate template (default Kimi → self-critique → confidence-low → Opus escalation only on `--hard` flag).

See `@concepts/agent-cost-routing-model-orchestra.md` for the distilled framework + Cemini-relevance analysis.

### About "Hermes"

**`[CONFIRMED 2026-05-29]`** — "Hermes" in this thread is **Nous Research's `hermes-agent`** (MIT, ~172k★): terminal TUI + gateway with slash-command autocomplete and provider-agnostic model switching (`hermes model`, OpenRouter/Moonshot routes). Not a Kilo Code / Augment / Factory.ai alias. See @entities/tools/hermes-agent.md.

Playbook slash vocabulary (`/branch`, `/queue`, `/rollback`, `/sage`) aligns with Hermes-style agent UX; full command list not independently enumerated in Wave 10 — verify against Hermes docs before quoting verbatim.

Lessons port to Claude Code regardless — the auxiliary-routing + thinking-mode-bloat + scope-lock patterns are model-agnostic.

### Cost math (per author, restated)

100M input + 10M output tokens/month →
- Opus 4.7: ~$2,550/mo
- Kimi K2.6: ~$85/mo (Moonshot direct, before any cache savings)
- Annual delta: ~$28,560

### Cemini relevance

Cemini already runs DeepSeek (price-competitive with Kimi); main-model savings already captured. Lessons that transfer:
1. Auxiliary-model orchestra (verify Cemini's title/summary/compression doesn't route through DeepSeek)
2. Scope-lock prompt header (workspace-laptop Claude Code skills + brief templates)
3. Adversarial-pass-then-escalate template (Cemini analyst → reviewer agent loop, relates to K37 reviewer-agent work)
4. Thinking-mode-bloat watch (relevant if Cemini ever adds extended-reasoning to FastMCP surfaces)

## Snippets

### The orchestra principle

> Tourists pick a single default. Real users build a five-model orchestra and run each track on the cheapest instrument that can carry it.

### Thinking-mode bloat math

> Kimi K2.6 in thinking mode generates 3.6x more output tokens than Opus or GPT for similar work (Artificial Analysis, Intelligence Index suite). At 10x cheaper per token, that nets to 2.7x cheaper. Not the 10x headline.

### Scope-lock prompt header

> Scope: [exactly which files / modules / behavior].
> Do not modify anything outside this scope.
> If you find a related issue, list it at the end. Do not fix it inline.

### Escalation template (verbatim)

> You are a senior engineer. Default behavior:
> 1. Solve the task on Kimi K2.6.
> 2. Pass tests / hit thresholds. Stop.
> 3. After the solution passes, run one adversarial pass:
>    "Critique your own solution. Find 3 weaknesses a senior
>     engineer would flag. Fix them."
> 4. If thresholds still don't hit after 3 iterations, set
>    confidence=low and surface the blocker. Do not retry blindly.
> 5. On confidence=low or --hard flag, escalate to Opus 4.7
>    with full context.

### Modified MIT license trigger

> Open-weight under Modified MIT. ... License only triggers above 100M MAU or $20M monthly revenue.

## Dead Ends

- Default-routing 3-word session titles to Opus 4.7 — author's load-bearing example.
- Single-default-model assumption — auxiliary routing is independent of main-model choice.

## Verification status (Wave 10, 2026-05-29)

- **`[CONFIRMED 2026-05-29]`** Hermes platform = `NousResearch/hermes-agent` (MIT, Nous Research).
- **`[TENTATIVE 2026-05-29]`** Kimi K2.6 cache pricing — third-party mirrors of Moonshot pricing (May 2026) show **cache-hit ~$0.10–0.16/M input**; author's **$0.15/M** figure is plausible for cache hits. **Cache-miss K2.6 input ~$0.95/M** (not K2.5's $0.60/M) — restate cost math when citing K2.6 specifically.
- **`[NEEDS VERIFICATION 2026-05-12]`** SWE-Bench Pro scores (58.6 / 57.7 / 53.4) — cross-check against Artificial Analysis or BigCodeBench leaderboards.
- **`[NEEDS VERIFICATION 2026-05-12]`** Kilo Code "KiloClaw" published numbers — find CEO's public statement.
- **`[NEEDS VERIFICATION 2026-05-12]`** `@nrehiew_` Zig inference engine tweet (Apr 20) — verify content matches author's restatement.
