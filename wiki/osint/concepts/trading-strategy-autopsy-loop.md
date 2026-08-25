---
title: "Trading strategy autopsy loop — loss → diagnosis → rewrite → re-test"
type: concept
tags: [concept, trading, loop-engineering, eval, prediction-markets]
keywords: [autopsy, self-improving, backtest, adversarial, maker-checker, retrospective]
related:
  - sources/x-article-antpalkin-self-improving-ai-trading-machine-2026-08-06.md
  - concepts/practical-loop-engineering.md
  - concepts/agent-steering-action-boundary.md
  - entities/people/antpalkin-cvxv666.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- @sources/x-article-antpalkin-self-improving-ai-trading-machine-2026-08-06.md — antpalkin X Article (2026-08-06)
- @concepts/practical-loop-engineering.md — /goal, /loop, worker ≠ verifier
- @concepts/agent-steering-action-boundary.md — HITL on LIVE/money paths (K239)
- @entities/people/antpalkin-cvxv666.md — public advocate of the pattern

## Raw Concept

What this page answers: how **retrospective trade autopsy** feeds an agent loop that rewrites strategy code and re-runs tests — and where that pattern breaks when eval ≠ live market.

## Narrative

**Pattern (antpalkin / public X thread, 2026-08-06):**

```
closed trades / backtest loss
    → structured autopsy (where, why, which rule failed)
    → agent rewrites strategy code or parameters
    → re-run test (no human edit)
    → repeat until metric improves or cap hit
```

Variants in the wild:

| Variant | Eval signal | Risk |
|---------|-------------|------|
| Weekly SSH autopsy + NotebookLM cross-ref (copy-trade bots) | Real journal + book RAG | Human still approves deploy |
| Adversarial maker/checker (Polymarket) | Peer agent breaks thesis | Checker must be independent |
| Pure backtest autopsy loop | Simulator PnL | **Simulator gap** — strategies that exploit backtest slippage die live |

**Design steals for Cemini:**

1. **Retrospective before predictive** — traders trust "why did THIS trade lose" more than "what to buy next"; autopsy is the onboarding path to automation (calibration reps).
2. **Worker ≠ verifier** — the agent that writes the autopsy should not be the sole agent that approves LIVE deploy; pairs @concepts/practical-loop-engineering.md.
3. **Eval honesty** — if the loop optimizes a backtest with no adversarial flow, it will overfit the simulator (same shape as RL sim-to-real failure). Prefer evals that match deployment boundary where possible.
4. **HITL default on money** — autopsy → rewrite → **paper re-test** can run unattended; **LIVE order egress** stays SteerBench hold unless operator confirms (K239).

**Cross-wiki:** wagering UX and PM/Kalshi consumer angle → `@gambling-wiki`. CeminiSuite prod bots → `@osint-wiki` entities/tools, not duplicated here.

## Snippets

> Instead of getting deleted, it reads its own autopsy, finds the exact place it bled, rewrites its own code, and runs the test again.

[Source: @sources/x-article-antpalkin-self-improving-ai-trading-machine-2026-08-06.md — X preview metadata]
