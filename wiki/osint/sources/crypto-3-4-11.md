---
title: Merkle Tree Certificate Post-Quantum PKI for Kubernetes and Cloud-Native 5G/B5G Core
type: source
tags: [pdf, infrastructure, post-quantum, pki, kubernetes, merkle-tree, tls, 5g]
clusters: [infrastructure]
related:
  - entities/infrastructure/hetzner.md
maturity: validated
read_status: read-skim
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @entities/infrastructure/hetzner.md — Cemini server infrastructure host

## Raw Concept

- **Original title**: Merkle Tree Certificate Post-Quantum PKI for Kubernetes and Cloud-Native 5G/B5G Core
- **Author(s)**: Unspecified in metadata captured
- **Type**: PDF
- **Location**: research for cemini/crypto 3 4:11.pdf
- **Length**: 29p
- **Retrieved**: 2026-04-23
- **Read status**: read-skim (preview + title only — full PDF not re-read in this pass)
- **Primary cluster**: infrastructure
- **All clusters**: infrastructure

## Narrative

Post-quantum cryptography infrastructure paper applying Merkle Tree Certificate (MTC) constructions to Kubernetes and 5G/B5G core networks. Core motivating observation: ML-DSA-65 signatures are 3,309 bytes and public keys 1,952 bytes — over 50× Ed25519 — which compounds badly in mTLS-heavy environments where thousands of inter-component connections authenticate continuously. The MTC construction reduces this per-connection overhead by batching attestations into a tree and shipping compact proofs rather than full certificate chains.

Honest assessment: this is a specialist systems-crypto paper. The problem is real (PQC signature bloat in K8s/5G mesh) and the solution family (MTC) is mainstream research, but evaluating the specific contribution requires the full paper. 29 pages suggests substantive work rather than a position paper.

Relevance to Cemini: tangential but non-trivial. The Cemini stack is Dockerized on Hetzner with a "crypto" tag here driven by post-quantum rather than blockchain/assets — note the naming collision. If/when Cemini adopts Kubernetes or any mesh with mTLS, PQC migration becomes material; until then this is background reading. The home cluster (infrastructure) fits appropriately; "crypto" in the all_clusters sense is not about financial crypto.

## Key findings

- ML-DSA-65 is >50× larger than Ed25519 in signature and key size; cumulative impact is the core problem statement.
- Merkle Tree Certificates compress per-connection authentication cost via tree-structured attestations.
- Target deployments: Kubernetes control planes, 5G Core networks — both feature many-to-many mTLS topologies.
- Note: "crypto" here means cryptography (PQC), NOT cryptocurrency. The home_cluster infrastructure is correct.

## Snippets

- **p.1** — "Post-quantum signature schemes such as ML-DSA-65 produce signatures of 3,309 bytes and public keys of 1,952 bytes, which are over 50× larger than classical Ed25519. In TLS-authenticated environments like Kubernetes control planes and 5G Core networks, where every inter-component connection is mutually au- thenticated, this overhead compounds across thousands[...]" — Concrete bloat numbers motivate the MTC approach.
