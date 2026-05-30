---
title: "Gemini DR — WC 2026 per-team LP safety assessments (Spain / Brazil / Morocco)"
type: source
tags: [source, gemini-deep-research, world-cup-2026, lp-safety, polymarket, k84, time-volatile]
keywords: [advance-to-knockout, bilateral-quoting, extreme-bound, skip, reduce, human-review, pre-tournament-friendly]
related:
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - concepts/world-cup-advance-market-bot-v1.md
  - entities/tools/world-cup-bot.md
  - sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md
  - sources/gemini-wc2026-group-b-lp-analysis-2026-05-29.md
  - sources/trading-posts-compilation-k84-2026-05-30.md
maturity: draft
read_status: deep-read
created: 2026-05-30
updated: 2026-05-30
---

## Relations

- @concepts/polymarket-sports-lp-operating-rules.md — extreme-bound + bilateral rules these reports stress-test
- @concepts/world-cup-2026-group-conviction-matrix.md — team-level safety verdicts folded into matrix (K84)
- @entities/tools/world-cup-bot.md — `conviction.yaml` should consume verdicts; **re-run before kickoff**
- @sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md — reward-farming vs conviction framing (K82/K83)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Three Gemini Deep Research LP safety reports (per-team advance markets) |
| **Author** | Gemini Deep Research (prompt family: WC bot LP safety — **predates public world-cup-bot v4 module map**) |
| **Type** | docx × 3 |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/` — `FIFA World Cup LP Safety Assessment.docx` (Spain), `FIFA World Cup LP Safety Assessment copy.docx` (Morocco), `Brazil World Cup Market Safety Assessment.docx` |
| **Retrieved** | 2026-05-30 |
| **Read status** | deep-read |
| **Volatility** | **[NEEDS VERIFICATION 2026-06-06]** — squad injuries, friendlies (Jun 4–8), and order books will move materially before Group C/H open (~Jun 13). Treat all microstructure numbers as **snapshots**, not config constants. |

## Narrative

Batch of **team-specific** Polymarket “advance to knockout” LP safety reports generated ~May 30, 2026. All three markets sit at **extreme upper bounds** (mid ≥ ~90¢), triggering **bilateral quoting** and toxic-flow exposure under the bot’s GTC + 60s fill-to-exit + 10h pre-kickoff cancel constraints.

### Executive verdict table (May 30 snapshot)

| Team | Group | Verdict | Mid (snapshot) | Primary risk driver |
|------|-------|---------|----------------|---------------------|
| **Spain** | H | **skip** | ~90¢+ | Yamal hamstring + unprotected Jun 4/8 friendlies; rewards-only economics at skew |
| **Brazil** | C | **reduce** | 95.5¢ (94/97) | Neymar Grade-2 calf tear (72h); widen spreads / cut size |
| **Morocco** | C | **human_review** | assumed ≥90¢ | Aguerd injury cluster; book depth unknown — manual gate before quote |

### Shared structural findings [CONFIRMED across 3 reports]

1. **Rewards-only at ≥90¢** — spread capture is negligible vs adverse selection from injury/news flow.
2. **Bilateral requirement** — simultaneous YES/NO posts increase pick-off surface when informed traders react to RFEF/medical wires faster than the bot’s 60s exit loop.
3. **Pre-tournament friendlies** — Spain (Iraq Jun 4, Peru Jun 8) flagged as unprotected high-severity flow events; monitor API latency during those windows.
4. **Order book depth** — all three reports explicitly refuse USD liquidity estimates; **runtime Gamma/CLOB only** (aligns with world-cup-bot design).

### Bot / config implications

- Map verdicts → `config/conviction.yaml` tiers: `skip` | `reduce` | `human_review` (not yet in v3 seeds for these three teams — **K84 follow-up on prod**).
- Do **not** bake May 30 mids into public docs for Issue 3 (2026-06-03); cite methodology + monitor triggers instead.
- Re-run Gemini DR safety prompt **weekly** through tournament window or on RFEF/FIFA medical bulletins.

## Snippets

> "Verdict — skip … deploying quoting capital on this specific market is structurally flawed." [Source: FIFA World Cup LP Safety Assessment.docx — Spain]

> "Verdict — reduce … systematically reduce quoting size and widen spreads to the maximum allowable parameters." [Source: Brazil World Cup Market Safety Assessment.docx]

> "Verdict — human_review … order book depth unknown — do not estimate USD liquidity." [Source: FIFA World Cup LP Safety Assessment copy.docx — Morocco]
