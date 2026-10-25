---

title: "E2EE vault + zero-knowledge share — client PII delivery pattern for Atto Access Share"
type: concept
tags: [concept, e2ee, vault, atto, security, k237]
keywords: [end-to-end encryption, zero-knowledge links, Shamir recovery, Atto Access Share, client vault, AGPL isolate]
related:
  - entities/tools/ente.md
  - concepts/atto-local-first-threat-model.md
  - concepts/atto-genealogy-agent-kit.md
  - sources/eval-url-revenue-opportunity-2026-08-14.md
  - sources/arxiv-2608.12566-domus-2026-08-14.md
  - entities/tools/rachoon.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14


---

## Relations

- @entities/tools/ente.md — reference architecture (AGPL, pattern-only)
- @concepts/atto-local-first-threat-model.md — existing Atto vault/share threat model
- @concepts/atto-genealogy-agent-kit.md — what the vault ships (genealogy deliverables)
- @sources/eval-url-revenue-opportunity-2026-08-14.md — K237 eval source
- @sources/arxiv-2608.12566-domus-2026-08-14.md — house-history/archival-image content for the vault

## Raw Concept

What this page answers: how does an Atto client vault deliver sensitive civil-record PII (documents, dossiers, house-history evidence) to concierge clients and subscribers with **client-side encryption + zero-knowledge sharing**, so the server never sees plaintext and a compromise doesn't leak PII? Synthesized from **ente/ente** (K237 Extract) + the existing Atto local-first threat model + Domus house-history content.

## Narrative

Atto's recurring-revenue engine is the **Access Share subscription ($8–$20/mo MRR)** and the **concierge delivery (≥$2.5k)** — both require bulletproof client data privacy for Italian civil-record PII. The ente architecture supplies the reference pattern:

1. **Client-side encryption**: encrypt on the client, before upload; server stores ciphertext only. Multi-cloud object storage (S3/MinIO) is fine because data is encrypted.
2. **Zero-knowledge share links**: recipient gets a URL + key out-of-band; the share token is cryptographically derived, not a server-side ACL.
3. **Shamir Secret Sharing emergency recovery**: split the recovery secret across N shares so a lost device doesn't permanently destroy a concierge client's vault (the failure mode that kills trust).
4. **External audits**: ente's crypto/source are audited by Cure53, Symbolic Software, Fallible — Atto should budget for the same class of independent review before charging for privacy.

**AGPL isolate (hard rule):** ente is AGPL-3.0 — **no AGPL library may link into proprietary Atto distribution kits**. Clean-room pattern extraction only (key management, share-link UX, recovery flow, client-side crypto design). Do **not** put private Barone pedigree or living-person vitals into Atto fixtures or this wiki's git history.

Combo with **rachoon** (Gotenberg branded invoice/PDF engine) gives the full concierge loop: E2EE vault delivery + auto-invoicing. Combo with **Domus** (2608.12566) gives house-history/archival-image content that makes the vault a richer deliverable (III-worthy overlay registry, temporal address/occupancy records).

`[OPEN QUESTION 2026-08-14]` ente's cryptographic envelope in headless Node/Python workers (WebAssembly compatibility) — if Atto needs to open the vault headlessly.
