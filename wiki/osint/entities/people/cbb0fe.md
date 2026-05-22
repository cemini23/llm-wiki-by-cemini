---
title: "@Cbb0fe (CBB) — 2020-2021 Uniswap+BSC mempool sniper, +$50M reported"
type: entity
tags: [entity, person, x-creator, mev, dex-sniping, mempool, uniswap, bsc, ethereum, historical-narrative, k55-2]
keywords: [cbb0fe, cbb, uniswap-sniping, bsc-sniping, mempool-monitoring, anti-snipe-measures, infura-nova, polkastarter-snipes]
related:
  - sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md
  - concepts/dex-mempool-sniping-2020-2021.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
---

## Relations

- @sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md — Post 5 source ("How We Made +$50M Sniping Shitcoins On DEXs")
- @concepts/dex-mempool-sniping-2020-2021.md — historical concept page synthesized from this post

## Raw Concept

Pseudonymous X creator (signing as "CBB") publishing a first-person memoir of the 2020-2021 mempool-sniping era on Uniswap and BSC. K55-2 ingest source — Post 5 is the foundational narrative source for the `dex-mempool-sniping-2020-2021` concept page (history-of-MEV reference).

## Narrative

### Handle

- X / Twitter: **@Cbb0fe**
- Signed as "CBB" at post close
- Operated as a two-person team with his brother (university IT teacher, learned Solidity in days before Aug 2020)

### Stated background

- Both brothers French; brother resigned university post December 2020 after sniping became full-time
- Moved to Dubai January 2021 to operate full-time
- Started with ~$40K combined portfolio, no Solidity knowledge, no blockchain understanding (per his account)

### Operation arc (as documented in K55-2 Post 5)

| Period | Activity |
|--------|----------|
| Aug 2020 | First snipes: $YMPL (60 ETH profit), $VIDYA (159 ETH), $POLS (6-figures), naive Add-Liquidity-then-buy approach (1 block late) |
| Sep 2020 | Upgraded to mempool monitoring; $CHADS +675 ETH, $FRONTIER +800 ETH, $LINA, $CHARTEX → 2300 ETH in 6 days |
| Sep 18 2020 | Uniswap UNI airdrop — claims "mid 6-figures" across the eligible test wallets |
| Dec 2020 - Feb 2021 | Polkastarter era; SpiderDAO +$500K via UI-bypass + listing snipe |
| Feb-May 2021 | BSC explosion; $KPAD +8300 BNB (~$2M in 1 hour), $COOK +3000 BNB, $MATTER +2000 BNB; AWS infra at $40-60K/mo |
| Aug 2021 | $EVN whitelist accident — blacklisted wallets randomly whitelisted, +$6M from dumping accumulated supply |
| Total | "+200 shitcoins on +10 chains", +$50M reported |

### Technical contributions (as claimed)

- **First (in his telling) to implement** the "for 1 ETH, buy as many tokens as possible up to limit Y" buy-pattern (instead of fixed token-target)
- **Pair-agnostic snipe contract** (ETH / USDT / USDC listing pair)
- **Multi-region AWS latency benchmarking** → North Virginia identified as optimal (Infura-driven MetaMask infrastructure clusters there)
- **Loop contract** to bypass per-tx buy limits
- **"Slave" contracts** — main contract spawns sub-contracts each below per-wallet buy limit
- **150-200 globally-distributed BSC nodes**, each emitting 10 txs per snipe attempt
- **"Suicide snipe"** — auto-sell 4 blocks after a no-limit buy to liquidate everyone sniping after
- **Atomic list-and-buy** contract for BSC launchpads with public listing-tx execution

### Why Cemini cares

- **Not a current-strategy source.** Mempool sniping at 2020-2021 magnitude is effectively closed (Flashbots, private mempools, MEV-share). The era documented is historical.
- **Foundational MEV history.** First-person operational detail about latency-edge engineering (AWS NoVA, geographic node fanning), anti-snipe arms-race iteration (loop → slave contracts → atomic list-buy), and exit timing (mid-2021 saturation, not regulatory).
- **Generalizable operational lessons** — geographic infrastructure as first-class strategic variable; smart-contract innovation per anti-defense iteration; anti-snipe defenses as moat for sophisticated snipers. These patterns generalize to any future MEV-adjacent or DEX-execution-edge strategy.

### Caveats

- **All PnL figures are self-reported** — no on-chain corroboration cited, no wallet addresses, no third-party verification.
- Specific snipe-by-snipe figures (`$KPAD +8300 BNB`, `$CHADS +675 ETH`) should be treated as `[TENTATIVE]` until / unless paired with on-chain data.
- **Architecture descriptions are independently corroborated** by the broader 2020-2021 MEV literature (Flashbots research, Daian et al. "Flash Boys 2.0", various postmortems). The mechanics — public mempool monitoring, Infura/NoVA latency edge, BSC random-tx-ordering — are `[CONFIRMED]` even if his specific operation isn't.
- Memoir is self-published; brother's identity and university affiliation undisclosed.
- The "EVN whitelist accident" story (+$6M out of nowhere) is suspicious-on-its-face but plausible given known DeFi smart-contract bugs in that period.
