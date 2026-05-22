---
title: "Polymarket-Near-Resolution-Bot — late-stage CLOB mid-price scanner (gamma-trade-lab, MIT)"
type: entity
tags: [entity, tool, polymarket, clob, near-resolution, adopt-eligible, mit, python, k55-2]
keywords: [polymarket-near-resolution-bot, gamma-trade-lab, clob-mid-pricing, late-stage-execution, binary-outcome-scanner, mit-license]
related:
  - sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-clob-api.md
  - concepts/polymarket-bot-architecture.md
  - concepts/prediction-market-statistical-arbitrage.md
maturity: validated
created: 2026-05-21
updated: 2026-05-22
---

## Relations

- @sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md — discovery source (K55 batch URL 5, the only Adopt)
- @entities/platforms/polymarket.md — execution venue
- @entities/tools/polymarket-clob-api.md — depends on this API surface for mid-price reads
- @concepts/polymarket-bot-architecture.md — slots into the "execution layer" role for late-stage market exploitation
- @concepts/prediction-market-statistical-arbitrage.md — late-resolution mid-price divergence is a specific arbitrage substrate

## Raw Concept

What prompted this page: K55-2 Tool Eval (URL 5) was the single Adopt tier verdict across 50 evaluated repos. MIT-licensed, Python, 9★, last commit 2026-05-21 (24-hour activity), 0 open issues. Functionally narrow — scans CLOB mid-pricing for heavily-favored binary outcomes near expiration — but the niche is genuine and does not duplicate any existing Cemini wiki entity.

## Narrative

### What it is

- **Repo**: `github.com/gamma-trade-lab/Polymarket-Near-Resolution-Bot`
- **License**: MIT (verified per K55 Tool Eval)
- **Stack**: Python (post claims "Python 9" — likely a tooling artifact; standard Python 3.x assumed pending Phase-0 audit)
- **Maturity**: 9★, 0 issues, last push 2026-05-21 (the same day as the Gemini DR eval — very current)
- **Capability**: Polls Polymarket's Central Limit Order Book (CLOB) for binary markets nearing resolution where mid-price reflects strong directional skew. Targets the **late-stage execution slice** that other Polymarket bots in the wiki (which focus on entry-time or mid-trajectory arbitrage) do not specifically address.

### Why Cemini cares

- **Fills a gap** in the existing Polymarket bot stack: most catalogued bots target market-making (LP-rewards farming), cross-venue arbitrage (Polymarket↔Kalshi), or directional entry. None specifically target the **near-resolution late-stage** window where mid-prices on heavy favorites can briefly mispricing relative to settlement certainty.
- **MIT license** clears IP-sale compliance immediately. No license-verification spot-check needed (already verified by the eval, contrast with the 31 Reject entries).
- **Tiny codebase** — Phase-0 audit cost is low; full code review possible in <1 hour.

### What we have not verified yet

- **Phase-0 audit not run.** Before any adoption into `/opt/cemini/`, the standard Phase-0 protocol applies: clone to `/tmp/polymarket-near-resolution-bot-audit/`, verify in-file LICENSE, check dependencies (especially any web3 wallet code that could exfiltrate keys), confirm the README matches the code, look for the wiki-tooling-class failure mode (hardcoded paths, environment assumptions).
- **"Heavily favored" threshold** is not specified in the eval — could be 90¢, 95¢, 99¢. Different thresholds imply very different operational profiles (95¢ markets resolve cleanly; 99¢ markets may have liquidity issues for any meaningful position size).
- **No record of operator deployment** beyond the repo author. With 9 stars, this is a micro-repo with no community validation.

### Phase-0 audit (2026-05-22)

Clone: `/tmp/k57-phase0-2026-05-22/gamma-trade-lab_Polymarket-Near-Resolution-Bot/`

| Gate | Verdict |
|------|---------|
| G1 License | **PASS** — MIT in `pyproject.toml` + LICENSE |
| G2 README honesty | **PASS** — tail-risk, no auto-redeem, Gamma `endDate` ≠ oracle |
| G3 Code surface | **PASS** — small `near_bot/` package; `DRY_RUN=1` default |
| G4 Client version | **WARN** — pins `py-clob-client==0.28.0` (pre-v2); align with prod client policy |
| G5 Maturity | **WARN** — ~9★, single maintainer |

**Verdict: CONDITIONAL-GO** — **steal-from** scanner filters (certainty mid, spread caps, complement sanity band). **NO** live wallet deployment until redemption ops + settlement-mechanics checks per `@concepts/cme-settlement-mechanics-for-prediction-markets.md`.

Thresholds are **env-parameterized** (`NEAR_CERTAINTY_MID_MIN`, `NEAR_BUY_USDC`, etc.) [CONFIRMED from README].

### Cemini posture

- **Tier: CONDITIONAL-GO** (Phase-0 complete). Reference patterns only for prod until redemption + oracle alignment scoped.
- **Routing**: server-side evaluation; not librarian.

## Snippets

> "This repository fulfills a critical algorithmic requirement for the Cemini financial suite, explicitly providing Python 9 logic to scan Central Limit Order Book (CLOB) mid-pricing for heavily favored binary outcomes nearing expiration on Polymarket." [Source: tool-evaluation-50urls-2026-05-21.docx — URL 5 reasoning]

> "Highly active micro-repository featuring commits within the last 24 hours, focusing strictly on granular, late-stage prediction market states with 9 community stars." [Source: tool-evaluation-50urls-2026-05-21.docx — URL 5 maturity signal]
