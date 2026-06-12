---
title: "CloddsBot — Multi-Agent Trading Terminal"
type: entity
tags: [tool, trading-bot, multi-agent, nodejs, steal-from, k38]
keywords: [cloddsbot, steal-from, three-surface-eval]
related:
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - entities/tools/gabagool.md
maturity: validated
created: 2026-05-11
updated: 2026-06-12
license_verified: MIT
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 9)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context
- `@entities/tools/gabagool.md` — sibling Polymarket arb bot pattern (K39, 2nd occurrence)

## Raw Concept

- **Repo / URL**: `github.com/alsk1992/CloddsBot`
- **Tier (per source brief)**: **Steal-from**
- **License** [VERIFIED 2026-05-11]: **MIT** (clean for pattern extraction per Cemini license posture). Maturity: 254★ / last push 2026-05-08 / ~3.5 months old.

## Narrative

Self-hosted AI-driven algorithmic trading terminal. Anthropic Claude primary + 8 LLM providers. 4 specialized agents: market analysis, alerts, execution. Native Web3: Solana DeFi, EVM, Hyperliquid, Binance perps. Node.js runtime.

### Integration vector

Steal-from: port to Python the **multi-agent routing logic**, **risk-engine math**, **prediction-market integrations**, **MCP tool schemas**. Do NOT adopt Node.js runtime (mismatch with Cemini Python stack).

### Risks

TypeScript→Python translation of async order execution is high-risk for financial losses if mistranslated. Massive scope (21 messaging platforms, multiple blockchains) — extract narrowly.

[Source: Link Evaluation Brief Trading Stack.docx, URL 9]

### Phase-0 reaffirm (K103, 2026-06-07)

Clone: `/tmp/k103-phase0-audit/CloddsBot`. **CONDITIONAL-GO steal-from** — MIT; ~327★; M2M settlement patterns for WC module 4 reference only; no Node prod install.

### K113 reaffirm (2026-06-12)

Eval URL 11 — **world-cup-bot overlap:** Solana DEX + Meteora DBC patterns absent from WC advance module 4 fill handler. License re-verified **MIT** (`gh api`); eval erroneously claimed null license. Steal-only; see `@sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md`.

### Phase-0 clone audit (2026-05-28)

Clone: `/tmp/k73-phase0-batch2/CloddsBot` (supplements 2026-05-11 license verification)

| Check | Result |
|-------|--------|
| License | **MIT** (`LICENSE` present) |
| Maturity | ~295★, large Node/TS surface (~600 files) |
| Runtime | Multi-agent terminal spanning many venues/chains — scope far beyond PM/Kalshi |
| Extraction | Steal routing/risk/MCP schema ideas only; **do not** port Node runtime into Cemini Python stack |

**Verdict: CONDITIONAL-GO (steal-from)** — same posture as prior eval; not a deployable cemini-prod service.

