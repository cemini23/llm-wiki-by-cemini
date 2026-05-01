---
title: Cryptographic audit trail
type: concept
tags: [concept, audit, cryptography, cemini-internal]
keywords: []
related:
  - concepts/nomotic-ai.md
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
  - concepts/defend-trade-secrets-act.md
  - sources/4-5-links.md
  - concepts/context-compression-resume-pattern.md
  - concepts/wiki-tooling-evaluation.md
  - sources/falkordb-graphrag-eval.md
  - sources/4-5-links-2.md
  - sources/3-26-link-re-3.md
  - sources/scaling-roadmap-research.md
  - sources/4-3-link-re-2.md
  - sources/wave-5-1-link-eval-stacks.md
maturity: validated
created: 2026-04-23
updated: 2026-04-28
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
- @concepts/defend-trade-secrets-act.md — K7-tail concept-promotion 2026-04-27 — sibling tamper-evident artifact pattern; the prescribed VCP/zkCA stack (this page) would supplement Git history as a cryptographically anchored secrecy-measure record satisfying DTSA's "reasonable measures to maintain secrecy" element under 18 U.S.C. § 1839
- @concepts/wiki-tooling-evaluation.md — 2026-04-28 synthesis: `llm-wiki-compiler`'s **confidence + `contradictedBy[]` per-page metadata** is a machine-readable analog to the inline `[CONFIRMED]` / `[TENTATIVE]` / `[NEEDS VERIFICATION]` / `[RETRACTED]` claim-tag system this concept page targets — complementary, not redundant; structured-metadata-on-pages + cryptographic-anchoring-of-claims serve different audit-trail layers
- @sources/falkordb-graphrag-eval.md — 2026-04-28 — graph databases enable schema-bound queries that vector-RAG cannot answer; cited GraphRAG benchmarks (3-4× better on cross-document reasoning) parallel the audit-trail story — provenance is a graph problem (chains of (claim, source, timestamp, signer) tuples), not a chunk problem. SSPL license blocks deployed-stack adoption; workspace-side experiment candidate only
- @sources/4-5-links.md — K8 deep-read 2026-04-28 — multi-topic Cemini-internal evaluation. The K8 doc's Synthesis section names the cryptographic audit trail explicitly as the **ex-post regulatory governance** mechanism that pairs with Pydantic v2 schemas + FastMCP tools (which provide ex-ante constraints). Reinforces the J-pass resolution: the deployed SHA-256 chain in `services/audit/chain.py` IS the substrate; the prescribed pymerkle/OpenTimestamps/VCP layers are separate forward-looking work
- @concepts/context-compression-resume-pattern.md — K8 promotion 2026-04-28 — adjacent state-persistence concern with intentional architectural distinction. The audit trail is *forward-only append-with-hash* (answers "what did the agent decide and when, immutably?"); cpr-pattern is *bidirectional save/load* (answers "where do we resume from after a crash?"). Both lean on PostgreSQL but solve different problems
- @sources/4-3-link-re-2.md — K14 deep-read 2026-05-01; three audit-trail reinforcements: OpenClaw centralized trust broker + non-lexical Pydantic v2 validation (Doc 3), ArchBench trajectory logging + set-based metrics → SHA-256 hashing (Doc 5), LDP structured provenance tracking with agent IDs + confidence scores + verification status (Doc 7). All Snippets-only.
- @sources/wave-5-1-link-eval-stacks.md — Wave 5.1 systems-architecture evaluation; hermes-a2a's HMAC security architecture surfaced as Steal-from hardening pattern for audit-trail layer

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
