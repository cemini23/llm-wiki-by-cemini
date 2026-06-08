---
title: Hermes on-chain forensics skill bundle
type: concept
tags: [concept, hermes, onchain, wallet-forensics, skill-bundle, k78]
keywords: [forensics-bundle, nansen-tgm, dexscreener, tokenomist, cookie-mcp, tufte-report]
related:
  - sources/trading-posts-compilation-6-2026-05-29.md
  - concepts/x402-agent-micropayments-data-access.md
  - entities/tools/hermes-agent.md
  - concepts/polymarket-wallet-alpha-pipeline.md
  - entities/tools/dexscreener-mcp.md
maturity: draft
created: 2026-05-29
updated: 2026-06-08
---

## Relations

- @sources/trading-posts-compilation-6-2026-05-29.md — K78 Posts 3 + 5
- @concepts/x402-agent-micropayments-data-access.md — Nansen paid tier
- @entities/tools/hermes-agent.md — host runtime + skill bundling
- @concepts/polymarket-wallet-alpha-pipeline.md — complementary wallet-alpha stage
- @entities/tools/dexscreener-mcp.md — K106 Claude Desktop path (free API; no x402)

## Raw Concept

Reusable **Hermes skill bundle** that runs multi-source token/wallet diligence in one command (~45s–2min, ~$0.10/run per authors).

## Narrative

### Pipeline stages (K78 synthesis)

| Step | Tool | Cost (author) |
|------|------|----------------|
| Pool discovery | DexScreener | Free |
| Wallet forensics | Nansen TGM + balances (x402 / agentcash) | $0.03–0.07 |
| RPC checks | drpc.org (age, nonce, CEX deposits) | Free |
| Unlock calendar | Tokenomist | Free (author sub) |
| Sentiment | Cookie MCP (3 queries) | Free |
| Synthesis | Cross-reference matrix + HTML/Tufte report | — |

**BlockRun** cited as Nansen fallback. **Skill bundling** loads all skills atomically vs manual sequential invocation.

### Outputs claimed

- Top sellers / accumulators, net flows (24h/3d/7d/30d)
- Dump classification (investor, smart money, bot, institutional)
- Sentiment cross-check vs on-chain moves

### Cemini posture

- **Steal-from workflow**, not Hermes runtime adoption.
- Overlaps Parity/ColdMath-style wallet forensics (K61) but retail tooling stack.
- Verify Nansen x402 merchant terms + data freshness before prod brief.

## Snippets

> "/forensics-bundle token … Total time: 45 seconds to 2 minutes. Cost: ~0.10–0.35." [Source: Posts.docx K78 Post 3, @AlphaCartell — paraphrased]
