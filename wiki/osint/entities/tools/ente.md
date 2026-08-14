---

title: "Ente — end-to-end encrypted cloud (E2EE vault for Atto Access Share)"
type: entity
tags: [tool, e2ee, vault, encryption, atto, k237]
keywords: [Ente, end-to-end encryption, zero-knowledge, Shamir, Access Share, AttoVault, AGPL]
related:
  - sources/eval-url-revenue-opportunity-2026-08-14.md
  - concepts/e2ee-vault-share.md
  - concepts/atto-local-first-threat-model.md
  - sources/arxiv-2608.12566-domus-2026-08-14.md
  - concepts/atto-genealogy-agent-kit.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14

---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-14.md — K237 eval batch (Extract, Atto)
- @concepts/e2ee-vault-share.md — E2EE vault/share pattern → Atto Access Share
- @concepts/atto-local-first-threat-model.md — existing Atto vault/share threat model
- @sources/arxiv-2608.12566-domus-2026-08-14.md — house-history + archival images → vault combo

## Raw Concept

What prompted this page: K237 eval (docx) tiers ente as **Extract** for Atto's Access Share subscription ($8–$20/mo MRR) — zero-knowledge client vault delivery. Verified via gh api: **AGPL-3.0**, 721MB (size-skip clone → README/docs only).

## Narrative

**Ente** is a fully open-source, end-to-end encrypted platform for storing data without trusting the service provider. Three apps: **Ente Photos** (Google/Apple Photos alternative), **Ente Locker** (safe space for important documents + credentials, free ≤100 items), **Ente Auth** (2FA alternative to deprecated Authy). Cryptography + source audited by **Cure53, Symbolic Software, Fallible**. AGPL-3.0 monorepo (Dart/Flutter clients, Go/Rust server, Swift/Kotlin), multi-cloud object storage (S3/MinIO), self-hostable.

### Steal-for-Atto (E2EE vault + Access Share)

- **Client-side encryption + zero-knowledge link generation** for secure client vault distribution — no server-side plaintext exposure of PII.
- **Shamir Secret Sharing emergency recovery** — concierge clients need foolproof recovery to avoid permanent data loss.
- **Access Share model**: ente's private sharing pattern maps onto Atto's $8–$20/mo Access Share tier — the recurring-revenue engine.
- **AGPL isolate**: **no AGPL library may link into proprietary Atto distribution kits** — clean-room pattern extraction only (client-side crypto design, key management, share-link UX, recovery flow). Do not put private Barone pedigree in Atto fixtures.

### Phase-0

- License: AGPL-3.0 (verified via gh api, matches docx).
- Size: 721MB > 500MB → **no clone**. README/docs-only reference.
- **NEEDS VERIFICATION 2026-08-14**: WebAssembly compatibility of ente's cryptographic envelope in headless Node/Python workers (per eval docx).
