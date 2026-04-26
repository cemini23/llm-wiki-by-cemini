---
title: Cryptographic audit trail
type: concept
tags: [concept, audit, cryptography, cemini-internal]
keywords: []
related:
  - sources/3-10-cryptographic-research.md
  - sources/3-18-crypto-integration-technical-audit.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - concepts/ip-sale-readiness.md
  - concepts/milestone-ledger.md
  - entities/infrastructure/timescaledb.md
  - concepts/skill-vetting.md
  - concepts/equity-intraday-backfill-gap.md
  - entities/platforms/hyperliquid.md
  - sources/crypto-5-4-11.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
audit_date: 2026-04-24
---

## Relations

- @sources/3-10-cryptographic-research.md
- @sources/3-18-crypto-integration-technical-audit.md
- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md — explicit cite as trust-deficit mitigator for paper-trading results (independent verifiability is the buyer-psychology lever)
- @concepts/ip-sale-readiness.md
- @concepts/milestone-ledger.md
- @entities/infrastructure/timescaledb.md
- @concepts/skill-vetting.md
- @concepts/equity-intraday-backfill-gap.md — backfill INSERTs anchor into the same hash chain
- @entities/platforms/hyperliquid.md
- @sources/crypto-5-4-11.md — *The Quantum-Cryptographic Co-evolution* (Kundu & Kompella, Cisco Research) — forward-looking PQ-cryptography landscape relevant to the SHA-256 hash-chain layer's threat-model assumptions (D′ 2026-04-26 routing)

## Raw Concept

Synthesized across 3 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[RESOLVED — 2026-04-25 primary-source deep-read]** The 2026-04-24 Track C audit retractions stand and now have explicit primary-source grounding. The deep-read of `@sources/3-10-cryptographic-research.md` — the document this concept page was originally synthesized from — confirms it is a **prescriptive technical audit** recommending the four-layer stack below, not an as-built description. Source's own verdicts: `ADOPT pg_tamperlog (PL/pgSQL version)`, `ADOPT pymerkle (in-memory, RFC 6962)`, `ADOPT OpenTimestamps (free Bitcoin calendar servers)`, `ADOPT VCP Silver Tier (schema-only — explicitly not full protocol implementation)`; rejected: DataTrails, fapilog-tamper, RFC 3161 TSAs, ACA Group attestation, VCP Gold/Platinum, Intel TDX. The wiki's prior present-tense framing collapsed that prescription into as-built language, which Track C correctly caught. What's actually deployed in `qdb` — `audit_hash_chain` table + `trg_audit_chain_hash` trigger + `audit_chain_hash_trigger()` function, plus `core/merkle.py` / `shared/audit_trail/merkle_batch.py` / `verify.py` / `chain_writer.py` — is a **spiritually-similar but custom** implementation of the source's first two layers (SHA-256 chain + hand-rolled Merkle batch) that does not use the named libraries and does not extend to layers 3-4 (Bitcoin anchoring + VCP envelope). Ticket (**P2**) remains valid: *Clarify audit-trail posture for APA* — either ship the prescribed layers 2-4 on top of the existing chain (source estimates 6 developer-days for full Phase 1-3 prescription) or formally retract the VCP language from APA docs and re-document the custom chain as "spiritual successor with explicit divergences from VCP Silver Tier." Gap memo: `briefs/track-c-walk-results.md`.

Cemini's cryptographic audit trail is a layered tamper-evident ledger
spanning every order, position change, and LLM reasoning artifact. The
design is derived from SCITT (Supply Chain Integrity, Transparency,
and Trust) principles and targets the VeritasChain Protocol v1.1 Silver
Tier.

### Stack (bottom-up)
1. **pg_tamperlog** `[RETRACTED 2026-04-24]` — ~~PostgreSQL extension producing append-only
   receipts for every write to the audited tables. Schema-bound, so
   an attacker who gains DB write access cannot silently mutate the
   history.~~ *What actually exists: `audit_hash_chain` table + `trg_audit_chain_hash` trigger + `audit_chain_hash_trigger()` function in `qdb`; companion tables `audit_batch_commitments`, `audit_intent_log`. Custom SHA-256 chain, not an extension-backed tamper-log.*
2. **pymerkle** `[RETRACTED 2026-04-24]` — ~~RFC 6962-compatible Merkle tree built over
   pg_tamperlog receipts in configurable windows (typical: 1 min for
   hot tables, 1 h for cold). Merkle root signed with the Cemini
   operator key.~~ *`pymerkle` is not installed in `cemini_mcp`; 0 hits. Hand-rolled Merkle batch in `shared/audit_trail/merkle_batch.py` exists but is not RFC 6962 and is not signed with an operator key.*
3. **OpenTimestamps** `[RETRACTED 2026-04-24]` — ~~submits the signed root to the Bitcoin
   blockchain via OpenTimestamps calendar servers, producing a
   publicly-verifiable timestamp proof.~~ *Not installed; 0 hits in the repo. No calendar-server code, no OTS proof-generation path.*
4. **VeritasChain Protocol (VCP) v1.1 Silver Tier** `[RETRACTED 2026-04-24]` — ~~the publication
   envelope: bundles the OpenTimestamps proof, the Merkle root, the
   pg_tamperlog range, and the relevant Pydantic-v2 schemas into a
   single JSON-LD document suitable for third-party verification.~~ *No VCP/VeritasChain references anywhere outside the wiki. Wiki-only language.*

### What's anchored
- All order submissions, fills, and venue-ack responses across
  Alpaca/OANDA/Hyperliquid/Kalshi.
- Every LangGraph state transition + LLM reasoning trace. `[RETRACTED 2026-04-24]` Previously named "DeepSeek-R1 reasoning trace" — DeepSeek/Ollama are not deployed (see @entities/infrastructure/deepseek-r1-14b.md). Whatever LLM actually produces traces today is left unclaimed until verified.
- Risk-engine decisions (position-sizing, CVaR-clip events).
- Macro Weather regime transitions.
- Milestone-ledger commits.

The effect: an IP-sale buyer can independently verify — via Bitcoin-
anchored timestamp proofs — that any backtest-reproduction run on the
shipped stack matches the claimed historical record. This is the
single biggest differentiator vs prop-shop IP that typically ships as
code + CSV backtest output with no independent verifiability.

## Snippets

*(populate as source stubs are deep-read.)*
