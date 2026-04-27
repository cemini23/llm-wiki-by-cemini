---
title: "Immutable Explainability: Fuzzy Logic and Blockchain for Verifiable Affective AI"
type: source
tags: [pdf, crypto, xai, affective-computing, fuzzy-logic, blockchain-anchoring, ssi, sepolia, hash-anchoring, proof-of-concept]
clusters: [crypto]
related:
  - concepts/crypto-asset-taxonomy.md
maturity: validated
read_status: read
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @concepts/crypto-asset-taxonomy.md — functional taxonomy of the 7 crypto-native watchlist assets

## Raw Concept

- **Original title**: Immutable Explainability: Fuzzy Logic and Blockchain for Verifiable Affective AI
- **Author(s)**: Marcelo Fransoy, Alejandro Hossian, Hernán Merlino
- **Affiliation**: Grupo GEMIS.BA — Universidad Tecnológica Nacional, Facultad Regional Buenos Aires (UTN FRBA), Argentina (academic, master's-thesis-adjacent)
- **Type**: PDF (preprint / workshop paper; source code released on GitHub)
- **Location**: research for cemini/agent 3 4:4.pdf
- **Length**: 13p (+ references)
- **Retrieved**: 2026-04-23 (download date)
- **Publication date**: 2025 (workshop presentation at WICC 2025; tied to in-preparation master's thesis by Fransoy at UTN FRBA)
- **Read status**: read
- **Primary cluster**: crypto
- **All clusters**: crypto

## Narrative

Academic proof-of-concept paper from an Argentine university group proposing **Immutable Explainability** — a pairing of an interpretable inference engine (Mamdani-type fuzzy logic) with public-blockchain hash anchoring (Sepolia testnet) for audit trails of affective-AI decisions. The target domain is Spanish-language voice emotion recognition; the motivating problems are twofold: (a) affective AI is usually a black box, and (b) when the provider owns the audit log, neither users nor regulators can trust that log hasn't been edited. The proposed architecture decouples explanation generation (fuzzy rules produce a readable trace of which rules fired and at what strength) from explanation integrity (hash of the redacted trace is anchored on a public chain), and reserves Self-Sovereign Identity (DIDs/VCs) as future work.

The system is a six-subsystem vertical slice: Whisper ASR → text-emotion module (lemmatization, negation, intensifier handling via spaCy `es_core_news_sm`) + audio-emotion module (RMS/ZCR/optional MFCC → arousal, SNR for ASR-confidence penalization) → Mamdani fuzzy fusion engine (IF–THEN rules over `asr_confidence × valence × arousal` → convex-combination weight `w_text ∈ [0,1]`) → orchestrator/API → auditing + blockchain anchoring. Each inference persists a `fusion_details` record (inputs, fired rules with firing strengths, output sets, centroid-defuzzified `w_text`), PII-redacts it, SHA-256 hashes it to a `txid`, and asynchronously submits the `txid` to a smart contract on Sepolia. Verification script `verify-txid-anchorage.py` lets a third party recompute the hash from the off-chain JSON and match it against the on-chain record. Evaluation on Spanish MEACorpus 2023 (5,129 samples): fuzzy fusion achieves weighted F1 = 0.429 vs linear fusion 0.408, text-only 0.396, audio-only 0.213; the fuzzy engine corrects 168 errors that linear fusion makes, 287 that the text module misses, and 162 where both baselines fail. Headline accuracy is modest because heuristic classifiers are deliberately weak — the authors state the goal is architectural validation, not a SOTA benchmark, with neural backends (BETO/RoBERTa-es for text, Wav2Vec2/HuBERT for audio) deferred to future work.

Who should care: this is a **clean, honest proof-of-concept** — unlike many "blockchain + AI" papers, the authors clearly delimit what anchoring does (integrity of an already-generated trace, proof of existence) and does not do (doesn't prove the model executed correctly, doesn't store the explanation itself, doesn't implement SSI). Gas analysis is concrete (~47k gas/event → ≈USD 8.08/anchor on Ethereum L1 at 50 gwei / ETH $3,445; L2 or Merkle-aggregation proposed for production) rather than handwaved. Cryptography is elementary (SHA-256 + a trivial `store_txid` smart contract) and the blockchain role is genuinely minimal — this is *crypto-adjacent* in the sense that the entire on-chain layer could be replaced by a transparency log (Sigsum/CT) or signed timestamping without losing the core contribution, which is the Mamdani-engine XAI trace. The paper acknowledges this directly. Cluster fit: `crypto` works if the cluster is "cryptography / blockchain uses in AI pipelines" rather than "web3 / tokens / DeFi" — there is no token, no consensus work, no smart-contract logic beyond a hash-write. Flag: **academic-honest-POC**, **applied-crypto / not web3**, **master's-thesis-tier rigor** (modest scale, well-documented, reproducible with Docker + public GitHub repo at `fransoymarcelo/immutable-explainability-heuristic-model`).

## Key findings

- **Immutable Explainability architecture**: Mamdani fuzzy inference engine (white-box, per-inference trace of fired rules + firing strengths) + SHA-256 hashing of redacted trace + on-chain anchoring of `txid` via a minimal smart contract on Sepolia testnet. Readable audit trace lives off-chain (planned: encrypted, user-controlled via IPFS / personal data vault).
- **Fuzzy fusion rule base**: convex-combination weight `w_text` produced by IF–THEN rules over `(asr_confidence, valence, arousal)` with triangular/trapezoidal membership functions, min t-norm / max s-norm, max aggregation, centroid defuzzification. Explicit modality-gating: low ASR confidence → lower `w_text`. Fallback to linear fusion if fuzzy engine fails.
- **Empirical evaluation (Spanish MEACorpus 2023, 5,129 samples, real Whisper ASR)**: weighted F1 fuzzy fusion 0.429 > linear fusion 0.408 > text-only 0.396 > audio-only 0.213. Fuzzy corrects 168 linear-fusion errors, 287 text-module errors, and 162 cases where both baselines fail. Macro F1 and macro recall show modest or mixed gains — text-only retains slight advantage on majority-class recall.
- **Gas / cost analysis**: `store_txid` consumes ~47,000 gas/event; on Ethereum L1 at 50 gwei + ETH $3,445 that is ≈USD 8.08/anchor; Sepolia testnet is free. Production strategy: migrate to L2 (Polygon, Arbitrum) or Merkle-aggregate hundreds of events into a single root (< USD 0.01/event marginal cost). Anchoring runs async so user-perceived latency is ~0 ms; end-to-end pipeline latency ≈4.0 s dominated by Whisper ASR.
- **Honest scope**: authors explicitly acknowledge the blockchain anchors proof-of-existence only, not proof of correct model execution; zk-SNARK / ZK-attestation is flagged as future alternative. SSI / DID / VC ecosystem is future work. Heuristic classifiers are a deliberately weak baseline for neural-backend replacement (BETO/RoBERTa-es, Wav2Vec2/HuBERT).
- **Crypto-cluster relevance**: limited but genuine. Uses a public-chain anchor as root of trust; gas/cost/L2 discussion is concrete. No tokens, no DeFi, no consensus work. The on-chain component could be swapped for a transparency log without altering the main contribution.

## Snippets

- **Abstract** — "We introduce the concept of Immutable Explainability, an architecture designed to address both challenges simultaneously. Our approach combines an interpretable inference engine—implemented through fuzzy logic to produce a transparent trace of each decision—with a cryptographic anchoring mechanism that records this trace on a blockchain, ensuring that it is tamper-evident and independently verifiable." — thesis statement.
- **§4.7 (fusion)** — "Probs_final = w_text · Probs_text + (1 − w_text) · Probs_audio, where w_text ∈ [0,1] is determined by a Mamdani-type fuzzy inference engine that takes as inputs ASR confidence, arousal, and valence." — core fusion rule, with `w_text` as the fuzzy output.
- **§4.13 (decentralized auditing)** — "Each pipeline execution generates a redacted event (stored_event) and computes its cryptographic hash (txid = SHA-256(...)). This txid is anchored in a smart contract deployed on a public blockchain (Sepolia Testnet)." — anchoring mechanism.
- **§4.13 (scope disclosure)** — "The blockchain guarantees only the integrity and the proof of existence of the explanation; it does not store the explanation itself. Verification requires the off-chain holder of the data (e.g., the user) to voluntarily present it so that its hash can be compared to the on-chain record." — honest limit statement.
- **§5.4 (results, Table 2)** — Fuzzy Fusion: weighted F1 0.429, weighted recall 0.438 vs Linear Fusion 0.408 / 0.425; Text Only 0.396 / 0.424; Audio Only 0.213 / 0.297 on Spanish MEACorpus 2023 (5,129 samples). Fuzzy engine corrects 168 linear-fusion errors, 287 text-module errors, 162 dual-baseline failures.
- **§5.7 (gas)** — "The hash-write operation (store_txid) in the smart contract consumes ~47,000 gas units per event. … Mainnet Projection (Layer 1): assuming a 50 gwei gas price and ETH at USD 3,445, the per-anchor cost is ≈ USD 8.08 … For large-scale deployment, the design considers migrating to Layer-2 networks (Polygon, Arbitrum) or using Merkle aggregation … marginal cost to negligible levels (< USD 0.01 per event)." — cost analysis and L2/Merkle scalability plan.
- **§7.1 (conclusions)** — "The pipeline achieves 43.8% recall and 0.429 weighted F1 with real Whisper transcriptions. This is not an upper bound—only the baseline that neural models must surpass under the same conditions." — authors' framing of their own numbers as heuristic baseline rather than SOTA claim.
