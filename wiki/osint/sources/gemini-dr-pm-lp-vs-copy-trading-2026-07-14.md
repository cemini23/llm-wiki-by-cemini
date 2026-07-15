---
title: "Gemini DR — Polymarket LP vs copy-trading capital allocation (2026-07-14)"
type: source
tags: [source, gemini-deep-research, polymarket, copy-trading, lp-rewards, capital-allocation, k165]
keywords: [lp-vs-copy, whale-copy, daleep, wc-incentives, openclaw-malware, oracle3, cryptuon-polybot]
related:
  - sources/gemini-dr-pm-trading-strategies-capital-2026-07-14.md
  - sources/gemini-dr-pm-hl-strategies-2026-07-14.md
  - concepts/cemini-pm-lp-vs-copy-capital-decision.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/hyperliquid-hlp-vs-user-vaults.md
  - entities/tools/oracle3.md
  - entities/tools/cryptuon-polybot.md
  - concepts/openclaw-security-taxonomy.md
  - entities/tools/openclaw.md
maturity: validated
read_status: deep-read
created: 2026-07-14
updated: 2026-07-14
clusters: [polymarket, copy-trading]
---

## Relations

- @sources/gemini-dr-pm-trading-strategies-capital-2026-07-14.md — sibling capital matrix (same wave)
- @sources/gemini-dr-pm-hl-strategies-2026-07-14.md — sibling HL vault/DIY depth
- @concepts/cemini-pm-lp-vs-copy-capital-decision.md — operator synthesis + empirical kill

## Raw Concept

- **Title**: Research Report: Polymarket LP Rewards vs. Copy-Trading Capital Allocation
- **Type**: Gemini Deep Research docx
- **Location**: `cemini-egress-fi:/opt/cemini-bulk/research/osint/Polymarket LP Vs Copy-Trading.docx` (after archive)
- **Retrieved**: 2026-07-14
- **sha256**: `f60a2b3e99064db1...` · **size**: 3,001,899 bytes · **Preingest**: NEW

## Narrative

Capital-allocation DR for Cemini: options framed as PM LP (A), PM copy (B), HL vault/DIY (C), neither (D).

**Headline at $10k (this report):** prefer **A (PM LP)** with canary + kill switches; **not** copy. At **$500 / $2k** prefer **D**.

Key economics: Daleep/Deleep et al. 2026 — whales have **lower** edge than small traders; LP **$1/day/market** floor; WC Live moneyline pools cited much larger than pre-game; DIY HL copy fee/latency loser; OpenClaw ClawHub skill malware (warmup RCE).

**INTEGRATE-CANDIDATE (doc):** oracle3, cryptuon/polybot, Prediction Hunt, Polymarket/agents.  
**AVOID:** Telegram private-key bots, OpenClaw trading skills, DIY HL fill-mirrors.

Conflicts with sibling reports and Cemini empirical LP kill (~$0.94, sleeve KILLED 2026-06-13) are reconciled on `@concepts/cemini-pm-lp-vs-copy-capital-decision.md`.

## Snippets

> Kill switches cited: net markout &lt; 0 for 3 consecutive days; detection lag &gt; 200ms; canary DD &gt; 10%.

> HLP: 0% perf/mgmt, 4-day lockup; user vaults: 10% perf fee, 5% leader skin (as stated in report).
