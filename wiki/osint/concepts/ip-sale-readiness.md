---
title: IP-sale-readiness
type: concept
tags: [concept, cemini-internal, m-and-a, strategy]
keywords: []
related:
  - sources/3-10-algorithmic-trading-ip-sale-audit.md
  - sources/3-10-cryptographic-research.md
  - sources/3-18-crypto-integration-technical-audit.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - sources/3-19-telegram-discord-research.md
  - sources/forex-research-3-18.md
  - sources/trading-playbook-research.md
  - concepts/cryptographic-audit-trail.md
  - concepts/replacement-cost-valuation.md
  - concepts/publishers-exclusion.md
  - concepts/irc-1235-capital-gains-safe-harbor.md
  - concepts/milestone-ledger.md
  - entities/infrastructure/hetzner.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/nautilustrader.md
  - entities/frameworks/pydantic-v2.md
  - entities/components/kelly-cvar-risk-engine.md
  - concepts/sbom.md
  - concepts/macro-weather-regime.md
  - concepts/game-of-attrition-doctrine.md
  - entities/platforms/alpaca.md
  - entities/platforms/hyperliquid.md
  - entities/platforms/kalshi.md
  - entities/infrastructure/deepseek-api.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-10-algorithmic-trading-ip-sale-audit.md
- @sources/3-10-cryptographic-research.md
- @sources/3-18-crypto-integration-technical-audit.md
- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-19-langgraph-scatter-gather-financial-analysis.md
- @sources/3-19-telegram-discord-research.md
- @sources/forex-research-3-18.md
- @sources/trading-playbook-research.md
- @concepts/cryptographic-audit-trail.md
- @concepts/replacement-cost-valuation.md
- @concepts/publishers-exclusion.md
- @concepts/irc-1235-capital-gains-safe-harbor.md
- @concepts/milestone-ledger.md
- @entities/infrastructure/hetzner.md
- @entities/frameworks/langgraph.md
- @entities/frameworks/nautilustrader.md
- @entities/frameworks/pydantic-v2.md
- @entities/components/kelly-cvar-risk-engine.md
- @concepts/sbom.md
- @concepts/macro-weather-regime.md
- @concepts/game-of-attrition-doctrine.md
- @entities/platforms/alpaca.md
- @entities/platforms/hyperliquid.md
- @entities/platforms/kalshi.md

## Raw Concept

Synthesized across 10 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[TENTATIVE — 2026-04-24 Track C audit]** The overall readiness narrative is partial: components 1, 2, 4 are *in-progress* (real but incomplete); component 5 (milestone ledger) is `[RETRACTED]` as claimed — the ledger does not exist in any form (see @concepts/milestone-ledger.md). Component 3's pg_tamperlog / pymerkle / OpenTimestamps / VCP sub-claims are `[RETRACTED]` (see @concepts/cryptographic-audit-trail.md); the underlying SHA-256 hash chain does exist. The SBOM sub-claim in component 4 is `[RETRACTED]` (see @concepts/sbom.md). Component 6 is `[CONFIRMED] doc-only`. Gap memo: `briefs/track-c-walk-results.md`. Outstanding tickets: **P0** milestone-ledger, **P1** SBOM + CVaR-gate + skill-vetting + audit-trail clarification.

**IP-sale-readiness** is the cross-cutting posture that frames every
architecture choice in the 10 most-recent Cemini-internal research docs.
The thesis: the Cemini Financial Suite is being built not as a lifestyle
prop-trading shop but as an acquisition target for a proprietary trading
firm, fintech, or systematic hedge fund looking to buy a turnkey
multi-asset platform.

### Core readiness components
1. **Reproducibility** `[CONFIRMED 2026-04-24]` — one docker-compose on commodity CPU hardware
   reproduces the whole stack. No GPUs, no hyperscaler lock-in, no
   vendor SaaS without a zero-cost local fallback. *Evidence: `docker-compose.yml` + 6 sub-compose files + 18 Dockerfiles in `/opt/cemini/`.*
2. **Typed everything** `[TENTATIVE 2026-04-24]` — Pydantic v2 at every boundary, OpenAPI
   spec generated from code, LangGraph state schemas serialized.
   *Partial: `cemini_contracts/` has Pydantic v2 models; LangGraph state in `agents/orchestrator.py` uses `TypedDict`, not Pydantic. Not every boundary is typed.*
3. **Audit trail** `[TENTATIVE 2026-04-24]` — `[RETRACTED]` sub-claims: ~~pg_tamperlog → pymerkle → OpenTimestamps →
   VeritasChain Protocol Silver Tier~~. Every LLM reasoning trace,
   every order, every position change is cryptographically anchored.
   *Real: `audit_hash_chain` DB table + triggers, `core/merkle.py`, `shared/audit_trail/`. Custom SHA-256 chain, not RFC 6962 pymerkle, not externally anchored. See @concepts/cryptographic-audit-trail.md.*
4. **Test posture** `[TENTATIVE 2026-04-24]` — Ruff + Semgrep + Trivy + ~~Schemathesis +
   Hypothesis + mutmut~~ `[RETRACTED sub-claims]`, all wired into CI, all producing artifacts
   the acquirer inherits. *Partial: Ruff + Trivy FS scan in `.github/workflows/deploy.yml` (Step 34d). Schemathesis + Hypothesis + mutmut have 0 hits in the repo. SBOM generation is retracted — see @concepts/sbom.md.*
5. **Milestone ledger** `[RETRACTED 2026-04-24]` — ~~each feature shipped is recorded against
   an explicit milestone so the acquirer reads a linear narrative
   from initial commit to the current code, not a pile of disjoint
   PRs.~~ *The ledger does not exist (no table, no JSONL, no YAML). `docs/ROADMAP.md` is a weak substitute with no schema-version / SBOM-hash / Merkle-root anchoring. This is the P0 ticket and the single most-load-bearing gap in the acquirer narrative. See @concepts/milestone-ledger.md.*
6. **Tax + legal structure** `[CONFIRMED 2026-04-24] doc-only` — Florida single-member LLC with IRC
   §1235 capital-gains safe harbor on IP transfer; asset-purchase
   agreement template with earnout tiers pre-drafted. *APA deliverable; no engineering milestone. See @concepts/irc-1235-capital-gains-safe-harbor.md + @concepts/publishers-exclusion.md.*

### Deal-killer ledger
Specific items tracked separately because they'd torpedo the sale if
undiscovered in due diligence: CCXT venue-adapter license ambiguities,
Finnhub commercial license per-entity restrictions, Telegram-channel
alt-data (publisher's-exclusion candidate), any GPL-contaminated
dependency, any model weight whose license forbids commercial
re-distribution, and any personal data persisted without a clear
retention schedule.

## Snippets

*(populate as source stubs are deep-read.)*
