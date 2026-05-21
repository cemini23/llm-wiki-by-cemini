---
title: "KreoPolyBot — Telegram-based Polymarket copy-trading bot"
type: entity
tags: [entity, tool, polymarket, telegram-bot, copy-trading, prediction-markets, k56]
keywords: [kreopolybot, kreo, polymarket-copy-bot, percentage-stop-loss, fixed-exact-percentage-portfolio-sizing, dexterssolab, pretracer-competitor]
related:
  - sources/posts-prediction-markets-quant-frameworks-2026-05-21.md
  - concepts/polymarket-copy-trading-strategy.md
  - entities/people/dexterssolab.md
  - entities/tools/pretracer.md
  - entities/tools/polymarketanalytics-com.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
phase_0_verdict: NO-AUDIT — third-party Telegram bot; not a candidate for Cemini adoption
---

## Relations

- @sources/posts-prediction-markets-quant-frameworks-2026-05-21.md — Post 3 (@DextersSolab) primary source
- @concepts/polymarket-copy-trading-strategy.md — workflow concept
- @entities/people/dexterssolab.md — promoter / referrer
- @entities/tools/pretracer.md — competing Telegram bot

## Raw Concept

What prompted this page: K56 Posts.docx Post 3 — @DextersSolab's referral-marketing post for KreoPolyBot (`t.me/KreoPolyBot?start=ref-dexter`).

## Narrative

**KreoPolyBot** is a Telegram-based Polymarket copy-trading bot promoted by @DextersSolab. Naming conflict (unresolved): @igor_mikerin (Post 2) references "Kreo" as a rejected competitor — these may be the same bot or related products with the two authors disagreeing on its latency.

### Setup flow (per @DextersSolab)

1. Open the Telegram bot link, hit Start
2. Select **Polymarket** (bot may support multiple venues)
3. Tap **Copy Trade** → **Add Task**
4. Insert the wallet address you want to copy + name the task (e.g., "90% Win Rate guy / politics insider")
5. Pick a sizing option:
   - **Fixed** — every trade = $X
   - **Exact** — match source trader's $ amount
   - **Percentage** — your trade = X% of source size
   - **Portfolio** — match source's % of balance
6. Set slippage (recommended 5%)
7. Set **percentage stop-loss** (recommended 70%) — author claims this feature is unique to KreoPolyBot
8. Skip the next step, pick **Buys + Sells** (mirror exits too)
9. Confirm → Back → Start (must show "Running")

### Operational claims (per @DextersSolab)

| Claim | Status |
|---|---|
| "Fastest execution available" | `[NEEDS VERIFICATION 2026-05-21]` — directly contradicts @igor_mikerin's claim that Pretracer is fastest |
| "Lowest fees" | `[NEEDS VERIFICATION 2026-05-21]` |
| Percentage stop-loss is a feature unique to KreoPolyBot | `[NEEDS VERIFICATION 2026-05-21]` |

### Self-reported PnL by author

@DextersSolab: $32,700 in one month copy-trading + 6 figures cumulative. Referral-content; treat as marketing.

### Cemini relevance

Same as Pretracer (@entities/tools/pretracer.md): **not a Cemini adoption candidate.** Documented for adversary-modeling / competitive-surface awareness in the @concepts/polymarket-copy-trading-strategy.md page.

## Dead Ends

- The Kreo / KreoPolyBot naming question is not resolved in the source material. The @igor_mikerin post rejects "Kreo" as slow; the @DextersSolab post endorses "KreoPolyBot" as fastest. Resolution requires direct check of `t.me/KreoPolyBot` vs `t.me/kreo` (or however the "Kreo" reference resolves) — `mcp__exa__web_search_exa` for "KreoPolyBot Polymarket" would resolve quickly.
- Custodial vs non-custodial flow unclear; the "deposit" workflow implies custodial holding of USDC by the bot operator. `[TENTATIVE 2026-05-21]`
