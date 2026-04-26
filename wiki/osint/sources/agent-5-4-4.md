---
title: Constant-Size Cryptographic Evidence Structures for Regulated AI Workflows
type: source
tags: [pdf, crypto, applied-cryptography, audit-trails, hash-and-sign, regulated-ai, merkle-trees, game-based-proofs, cluster-partial-misfit]
clusters: [crypto]
related:
  - concepts/crypto-asset-taxonomy.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @concepts/crypto-asset-taxonomy.md — functional taxonomy of the 7 crypto-native watchlist assets

## Raw Concept

- **Original title**: Constant-Size Cryptographic Evidence Structures for Regulated AI Workflows
- **Author(s)**: Leo Kao (sole author)
- **Affiliation**: Codebat Technologies Inc. (industry, regulated-AI / clinical compliance vendor)
- **Type**: PDF (arXiv preprint)
- **Location**: research for cemini/agent 5 4:4.pdf
- **Length**: 16p
- **Retrieved**: 2026-04-23 (download date)
- **Publication date**: 10 February 2026 (v2 on arXiv:2511.17118v2 [cs.CR]; v1 November 2025)
- **Read status**: read
- **Primary cluster**: crypto
- **All clusters**: crypto (see cluster note)

## Narrative

Single-author applied-cryptography paper proposing a **constant-size evidence structure** abstraction for audit trails in regulated AI workflows (clinical trials, medical decision support, pharmaceutical manufacturing, financial compliance). Each audit event is committed to a fixed k-tuple of λ-bit hash-field outputs plus a signature: `ev = (f₀, …, f_{k-1}) = (H(ϕ₀(E)), …, H(ϕ_{k-1}(E)))` with `σ = Sign_sk(ev)`. Fields encode context commitments, I/O hashes, environment/TEE attestation digests, and audit-chain links. The core claim is that fixed-size evidence removes metadata-length leakage, gives uniform per-event verification cost (Θ(k) hash ops + 1 signature verify), and composes cleanly with hash-chain and Merkle-tree anchoring plus optional TEE attestation.

Security is developed formally via three game-based experiments with tight reductions: **evidence binding** (a single ev cannot validate two distinct events — reduction to collision resistance of H, advantage bound k·Adv_CR), **tamper detection** (forgery of evidence on unqueried events — reduction to EUF-CMA signatures + collision resistance), and **non-equivocation** (two distinct hash-chains cannot share a tip — reduction to collision resistance, bound n·Adv_CR). Proofs are correct in sketch (standard hash-and-sign / Merkle-chain arguments) and the paper acknowledges the static-key-compromise limitation, leaving adaptive corruption and UC composability as future work. Prototype is in Rust with a 256-bit hash and Ed-curve signatures; reports 3.5×10⁴ events/s single-threaded generation, 2.8×10⁵ events/s on 16 cores, 4.0×10⁵ events/s GPU batch verification at batch size 10⁶. Hardware is "mid-range discrete GPU (8GB VRAM)" with hash/signature choice unnamed — so treat the benchmarks as indicative, not reproducible.

Who should care: this is **applied cryptography**, not cryptocurrency. The paper's "blockchain" mentions are restricted to noting that the Link output (hash-chain tip or Merkle root) *could* be anchored to an external ledger or transparency log (Certificate Transparency, Sigsum, Bitcoin cited as examples); no tokenomics, no smart-contract logic, no consensus. Clinical-trial/pharma/HIPAA/FDA/EU-AI-Act/Sarbanes-Oxley regulatory framing is the real motivation. Industry affiliation (Codebat Technologies) is disclosed, and the paper admits "certain implementation details are covered by patent applications by Codebat Technologies Inc." — so treat the "industry-wide standard" framing as vendor-aligned. The cryptographic core is solid and standard-recipe (classic hash-and-sign; nothing novel cryptographically), and the value is primarily the clean abstraction + regulatory framing. Flag: **applied-crypto / not web3**, **vendor-adjacent** (patent-pending), **cluster-partial-misfit** for a `crypto` cluster that is otherwise web3-flavored. If the cluster is "cryptography-generally" this fits; if the cluster is "cryptocurrency", move it or retag `applied-cryptography`.

## Key findings

- **Abstraction**: evidence item = k fixed-length hash fields + one signature, `ev = (H(ϕ₀(E)), …, H(ϕ_{k-1}(E)))`, `σ = Sign_sk(ev)`. Fields bind context, inputs, outputs, environment/TEE attestation, and audit-chain links. k ≈ 8–12 recommended in practice.
- **Security theorems (Thm 5.4–5.6)**: evidence binding ≤ k·Adv_CR(H); tamper detection ≤ k·Adv_CR(H) + Adv_EUF-CMA(Sig); non-equivocation ≤ n·Adv_CR(H). Proofs via standard hash-collision / EUF-CMA reductions against static-key adversary.
- **Complexity**: Θ(k) hash ops + 1 sign for Generate; Θ(k) hash ops + 1 verify for Verify; chain Link is O(n); Merkle Link is O(n). Representation size is exactly k·λ bits, independent of event content.
- **Prototype microbenchmarks** (Rust, 256-bit hash, Ed-curve sig, 16-core server + mid-range GPU): 3.5×10⁴ events/s single-thread Generate (28.4 µs/event), 2.8×10⁵ events/s 16-core (5.7 µs/event), batch Verify 2.5×10⁵/s CPU @ 10⁵ batch / 4.0×10⁵/s GPU @ 10⁶ batch.
- **Regulatory scope**: paper anchors use-cases to HIPAA, 21 CFR Part 11 (FDA electronic records), EU AI Act (Regulation 2024/1689), and Sarbanes-Oxley — not to crypto/financial regulation per se.
- **Crypto-cluster relevance**: minimal. Blockchain/ledger references are three sentences total (Link anchors *could* use Certificate Transparency, Sigsum, or a blockchain). No tokens, no consensus, no smart contracts. Author/affiliation has patent-pending IP; treat "standards-body" framing as vendor-influenced.

## Snippets

- **Abstract** — "This paper introduces constant-size cryptographic evidence structures, a general abstraction for representing verifiable audit evidence for AI workflows in regulated environments. Each evidence item is a fixed-size tuple of cryptographic fields…" — thesis statement.
- **§4 (construction)** — "Generate(pp, sk, E): for each i ∈ I, mᵢ ← ϕᵢ(E); fᵢ ← H(mᵢ); ev ← (f₀, …, f_{k-1}); σ ← Sign_sk(ev); return (ev, σ)." — core algorithm.
- **§5.2 (security)** — "Adv^Bind_{Π,A}(λ) ≤ k · Adv^CR_{H,B}(λ)." Theorem 5.4 bound; k is the number of evidence fields. Reduction loses a factor of k via guessing the colliding index.
- **§6.4 (TEE composition)** — "If events are generated inside TEEs [Intel SGX, ARM TrustZone], the encoding functions ϕᵢ can be defined to include attestation outputs or environment identifiers. For example, one field might be H(measurement ∥ config)."
- **§7.3 (prototype)** — "single-threaded 3.5×10⁴ events/s, 28.4 µs/event; multi-threaded (16 cores) 2.8×10⁵ events/s, 5.7 µs/event." — headline generation throughput.
- **§10 (limitations / industrial disclosure)** — "Certain implementation details are covered by patent applications by Codebat Technologies Inc.; the present paper concentrates on the abstract construction and its security/performance properties." — vendor-IP flag.
