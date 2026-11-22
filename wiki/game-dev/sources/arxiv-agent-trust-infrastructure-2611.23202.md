---
title: ATI — federated identity and attestation for cross-organization AI agents
type: source
related:
  - sources/arxiv-runtime-nl-criteria-verification-2611.23074.md
  - concepts/agent-harness-castle-project.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2611.23202
maturity: draft
created: 2026-11-22
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation, and Accountability Architecture for Cross-Organization Autonomous AI Agents |
| Authors | Viet K. Nguyen, Mohammad I. Husain |
| Affiliation | California State Polytechnic University, Pomona |
| Type | arXiv:2611.23202v1 [cs.AI], 17 November 2026, 13 pages |
| Location | `research to be indexed/game-dev/arxiv-2611.23202-agent-trust-infrastructure-ati-a-federated-ident.pdf` |
| Retrieved | 2026-11-22 |
| Read status | read |
| Licence | Apache-2.0 |

## Narrative

### The problem

Agents from different organizations call each other's tools and hand off work. Network-level trust and API keys do not show that the caller is a legitimate agent, that it runs its approved model and prompt, or that its action was authorized. [Source: arxiv-2611.23202-agent-trust-infrastructure-ati-a-federated-ident.pdf p.1]

### The architecture

ATI treats each agent as a security principal. It uses five planes, all enforced by a reference monitor outside the agent's model:

| Plane | Job | Mechanism |
|-------|-----|-----------|
| Identity | Prove the caller holds the key | Ed25519 key pair; the agent ID is the SHA-256 hash of the public key |
| Trust | Establish cross-organization trust | One certificate authority per organization (AgentCA); partners exchange CA public keys; no shared root |
| Attestation | Check what the agent runs | Signed report of model, tool list, and system-prompt hash, compared with the approved record in the certificate |
| Policy | Authorize each tool call | Three checks on each call |
| Accountability | Attribute each action | Signed, hash-chained log entry per allowed tool call |

[Source: arxiv-2611.23202-agent-trust-infrastructure-ati-a-federated-ident.pdf p.5-7]

The identity and request formats follow IETF WIMSE workload tokens. Attestation uses Entity Attestation Tokens. The design adds no new cryptography. Each plane reuses a known pattern: X.509 certificates, SPIFFE-style workload identity, TPM measure-then-attest, a zero-trust reference monitor, and a certificate-transparency-style log. [Source: arxiv-2611.23202-agent-trust-infrastructure-ati-a-federated-ident.pdf p.3]

### The evaluation

The team ran a simulated federation of eight organizations and six agent frameworks, with five agents per organization. Security experiments used two organizations, 14 attack scenarios, and six benign tasks, across five agent models. Each scenario ran with five attack wordings and three repeats. A panel of judge models scored the outcomes. [Source: arxiv-2611.23202-agent-trust-infrastructure-ati-a-federated-ident.pdf p.1]

| Metric | Without ATI | With ATI |
|--------|-------------|----------|
| Attack containment, all 14 scenarios | 43% | 84% |
| Attack containment, 11 scenarios held constant | 40% | 80% |
| Benign task success, 90 trials | 91% | 92% |
| Overhead per request | — | about 174 µs |

[Source: arxiv-2611.23202-agent-trust-infrastructure-ati-a-federated-ident.pdf p.8, p.12-13] [TENTATIVE — simulated single-process federation, judge-model scoring]

### Limits the authors state

- Prompt injection (A6) is not prevented. ATI checks identity, not the content a request carries.
- Collusion between authorized agents (A11) can look like normal collaboration.
- A stolen private key is not detected directly. Recovery needs revocation and reissue, and the recovery latency was not measured.
- The logs are tamper-evident, not proof of non-repudiation, unless the signing keys stay safe.
- No privacy controls for identity metadata or audit logs. Certificate and log data can reveal organizational relationships.
- The simulation runs in one process, so signatures and tokens never cross a network.

[Source: arxiv-2611.23202-agent-trust-infrastructure-ati-a-federated-ident.pdf p.12]

### Relevance to game dev

There is none in practice. This is infrastructure for agents that cross organizational boundaries. castle-sim runs operator-owned agents on one laptop, under one trust domain. There is no partner CA, no cross-organization handoff, and no need for a certificate per agent.

The page exists because the paper was in this domain's inbox and the ingest records it. Read it as agent-security background for a future multi-operator project, not as a design input for the castle-sim harness. Compare @sources/arxiv-runtime-nl-criteria-verification-2611.23074.md, which addresses a smaller question the harness does have: did this session break a stated rule?

## Snippets

> "With all enforcement mechanisms enabled, attack containment increases from 43% to 84% … while enforcement introduces approximately 174 µs of overhead per request." [Source: arxiv-2611.23202-agent-trust-infrastructure-ati-a-federated-ident.pdf p.1]

> "ATI does not defend against instructions hidden in the data that a request carries, which we treat as a separate problem." [Source: arxiv-2611.23202-agent-trust-infrastructure-ati-a-federated-ident.pdf p.3]

## Dead Ends

- Applying a certificate authority to a single-user Godot project. It adds a key-distribution job and stops no realistic threat.
- Reading the 84% containment figure as a safety score. It is the share of 14 scripted attack scenarios stopped in a one-process simulation.
