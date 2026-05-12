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
  - sources/3-29-research-6.md
  - concepts/agent-identity-protocol.md
  - sources/3-17-agent-research.md
  - sources/3-25-git-research.md
  - sources/git-3-5-pt3.md
  - sources/crypto-7-4-11.md
  - concepts/sae-execution-contract.md
  - sources/ai-2-4-3.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/agent-authorization-stack.md
  - concepts/agent-trajectory-triage-signals.md
  - sources/signals-trajectory-triage.md
maturity: validated
created: 2026-04-23
updated: 2026-05-11
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
- @sources/3-29-research-6.md — K15 deep-read 2026-05-01; Paper 5 (AIP/IBCT) promoted to @concepts/agent-identity-protocol.md — IBCT completion blocks map onto the existing SHA-256 chain, adding agent-to-agent authorization provenance
- @concepts/agent-identity-protocol.md — K15 promotion 2026-05-01; IBCT provides the ex-ante authorization layer (who can execute what) that pairs with this page's ex-post immutability layer (what happened, immutably recorded)
- @sources/3-17-agent-research.md — K16 deep-read 2026-05-01; abliterated-model sandbox pattern (observation-only, zero execution authority) + deterministic auditable execution (Gap 4) reinforce the audit-trail security boundary
- @sources/3-25-git-research.md — K17 deep-read 2026-05-01; agentic decision anchoring: each debate cycle's structured JSON state artifact → SHA-256 hash → pymerkle tree → OpenTimestamps, linking linguistic reasoning inextricably to TorchRL execution command
- @sources/git-3-5-pt3.md — K18 deep-read 2026-05-01; convx conversation-level anchoring (SHA-256 fingerprinting + automated secret redaction → Git) completes three-level provenance chain: engineering provenance → decision rationale → execution record
- @sources/crypto-7-4-11.md — K19 deep-read 2026-05-01; SAE execution-level audit anchoring (M6): every ExecutionDecision emits structured audit record (matched rule, enforced budgets, effective action, trust-state snapshot). Replay-deterministic — same stream + config = same decision trace. Fills gap between decision rationale and execution record
- @concepts/sae-execution-contract.md — K19 promotion 2026-05-01; provenance chain extended to four levels: engineering provenance (convx) → decision rationale (K17 debate-cycle) → execution authorization (SAE ALLOW/LIMIT/BLOCK audit records) → execution record (trade-level Merkle)
- @sources/ai-2-4-3.md — K20 deep-read 2026-05-01; Gateway RCE chain as composition-detection target + input provenance model as fifth anchoring dimension
- @concepts/openclaw-security-taxonomy.md — K20 promotion 2026-05-01; Context Manipulation kill-chain stage + three structural conditions; the provenance model (input-provenance.ts) as context-assembly-layer audit primitive
- @concepts/agent-authorization-stack.md — K19+K22+K23+K24 cross-cluster synthesis; every authorization decision across all four layers is immutably logged.

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

**IBCT extension (K15, 2026-05-01)**: @concepts/agent-identity-protocol.md adds the ex-ante authorization layer that pairs with this page's ex-post immutability. The existing SHA-256 chain records *what happened*; IBCT completion blocks record *who authorized it under what constraints*. Together they provide a complete cryptographic provenance chain from agent debate consensus → delegated authorization → tool execution → immutable record. See the IBCT concept page for the Biscuit-token-based verifiable delegation protocol.

**Sandboxed Observer pattern (K16, 2026-05-01)**: K16 prescribes deploying an abliterated (uncensored) LLM strictly within an observation-only pipeline — the model parses raw SEC EDGAR filings and volatile social sentiment, but its outputs flow exclusively to PostgreSQL/JSONL logs for future TorchRL training. It has zero mechanical ability to interface with the EMS signal router or the kill switch. This is a security-boundary pattern: the LLM is a sensor, not an actor. The audit trail captures all observer outputs (ex-post immutability), while the sandbox enforces that no observer output can become an execution trigger (ex-ante constraint). Together with the IBCT extension, this establishes a three-layer security model: (1) IBCT authorizes *who* can execute; (2) the sandbox constrains *what* the observer can influence; (3) the audit trail records *what happened* immutably.

**Agentic Decision Anchoring (K17, 2026-05-01)**: K17 extends the audit trail's anchoring scope from trade execution to agent debate consensus. After each Generator-Evaluator debate cycle, the structured JSON state artifact (containing the thesis, evaluation metrics, and consensus decision) is SHA-256 hashed. The hash is inserted into the Merkle tree, linking the DeepSeek model's linguistic reasoning inextricably to the numerical output in the Polars feature dataframe and the subsequent TorchRL execution command. The root is periodically stamped via OpenTimestamps. Because inference is prescribed as entirely local (Ollama on Hetzner), there are no external API logs to rely upon or obscure — the entire reasoning and execution apparatus is mathematically sealed. This extends the audit trail from *what was executed* (trade-level) to *why it was decided* (debate-cycle-level), providing a complete provenance chain that an institutional acquirer's forensic audit can replay: agent debate → consensus reasoning → feature vector → TorchRL execution → order routing.

**Conversation-level anchoring via convx (K18, 2026-05-01)**: K18 (Resource 5 — pascalwhoop/convx) extends the audit trail's scope further upstream, to the AI-assisted engineering process itself. convx provides SHA-256 fingerprinting of AI conversation sessions (Claude Code, Cursor, Codex), ensuring execution idempotency — only sessions containing novel modifications are processed. Critically, it performs automated secret redaction prior to Git archival, replacing sensitive tokens and API keys with secure placeholders. This addresses a gap in the existing audit trail: the existing chain covers *what the agents decided* (K17, debate-cycle-level) and *what executed* (trade-level), but not *how the codebase itself evolved through AI-assisted development*. convx anchors the engineering provenance — an acquirer's due diligence team can replay the full AI-assisted development history, verifying that the Logit-Space pricing logic was rigorously constructed rather than hallucinated. The three anchoring levels now form a complete chain: **engineering provenance** (convx, Git-archived AI sessions) → **decision rationale** (K17, debate-cycle JSON artifacts) → **execution record** (trade-level, SHA-256 → Merkle tree → OpenTimestamps).

**SAE execution-level audit anchoring (K19, 2026-05-01)**: @sources/crypto-7-4-11.md adds a fourth anchoring layer at the execution boundary: SAE's M6 auditability mandate. Every ExecutionDecision emits a structured audit record containing: matched rule (which policy predicate fired), enforced budgets (leverage/notional/rate/slippage caps), effective action (the post-projection action that reached the executor), and a full state snapshot including trust signals (provenance score, capability risk, injection alert flag). Critically, SAE audit records are **replay-deterministic**: given the same replay stream and config, the same decision trace is regenerated bit-for-bit. This extends the provenance chain to four levels: **engineering provenance** (convx, Git-archived AI sessions) → **decision rationale** (K17, debate-cycle JSON artifacts) → **execution authorization** (SAE, ALLOW/LIMIT/BLOCK audit records with trust-state snapshot) → **execution record** (trade-level, SHA-256 → Merkle tree → OpenTimestamps). The SAE layer fills the gap between *what was decided* and *what was actually submitted to the exchange* — without it, an auditor cannot distinguish "the agent decided to go long" from "a compromised skill submitted 5× leverage through a manipulated prompt."

**K20 provenance model + Gateway RCE chain (2026-05-01)**: @sources/ai-2-4-3.md and @concepts/openclaw-security-taxonomy.md add two audit-trail-relevant primitives:

1. **Gateway RCE chain as composition-detection target**: K20's 3-stage Gateway→RCE chain (gatewayUrl SSRF → token exfiltration → node.invoke exec approval bypass) is the canonical example of a multi-stage attack where no single audit record captures the full chain. Three independently moderate-severity advisories composed into unauthenticated RCE because no enforcement point observed the full call path. The audit trail's replay-deterministic property (SAE M6) is the detection mechanism: given the full ExecutionRequest→Decision trace, an auditor can reconstruct the chain and identify that the SSRF'd token was subsequently used to authorize an exec-approval mutation. Without cross-layer audit records, the three stages appear as unrelated events.

2. **Input provenance as fifth anchoring dimension**: K20's inter-session contamination fix (GHSA-w5c7) introduces a structured `InputProvenance` type with three values: `external_user`, `inter_session`, `internal_system`. This is a **context-assembly-layer provenance model** that complements the four existing audit-trail layers. Where SAE records *what was executed and under what trust state*, input provenance records *where the instruction came from*. The generalization proposed in K20 §6.6 — "mandatory provenance tag for every string entering the context window" — would add a fifth anchoring dimension to Cemini's provenance chain: **instruction provenance** (who/what originated each string the model sees) → engineering provenance → decision rationale → execution authorization → execution record. This is not yet prescribed for Cemini but is the natural next layer.

## Snippets

*(populate as source stubs are deep-read.)*
