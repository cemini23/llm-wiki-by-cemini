---
title: Atto local-first threat model — vault, MCP, share
type: concept
tags: [concept, genealogy, atto, security, threat-model, mcp, k185, draft]
keywords: [AttoVault, AES-256-GCM, SSN strip, Cloudflare Access, min-release-age, suggest-only, STRIDE]
related:
  - sources/substack-rss-secpro-2026-07-24-244-uk-cyber.md
  - entities/tools/visa-vulnerability-agentic-harness.md
  - entities/tools/ego-lite.md
  - concepts/youratto-lean-conversion-page.md
  - concepts/youratto-brand-identity.md
  - sources/gemini-atto-landing-demo-production-2026-07-23.md
  - sources/gemini-atto-threat-model-2026-07-22.md
  - concepts/atto-macos-gtm-gumroad.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/italian-citizenship-youtube-soft-flags.md
  - sources/gemini-atto-macos-gtm-2026-07-22.md
  - sources/atto-commercial-migration-plan-2026-07-23.md
  - sources/software-licensing-architecture-research-2026-07-23.md
  - entities/tools/license-guard-rs.md
  - entities/tools/opencli.md
  - entities/tools/ente.md
  - concepts/e2ee-vault-share.md
  - sources/atto-production-readiness-audit-2026-09-02.md
  - entities/tools/openmed.md
maturity: draft
created: 2026-07-22
updated: 2026-09-04
---

## Relations

- @sources/atto-production-readiness-audit-2026-09-02.md — 2 Sep Windows audit; ATTO-007 raw `--file` can leave loopback
- @entities/tools/opencli.md — K197 backlink
- @entities/tools/openmed.md

- @sources/substack-rss-secpro-2026-07-24-244-uk-cyber.md — identity lesson

- @entities/tools/visa-vulnerability-agentic-harness.md — K195 Extract

- @entities/tools/ego-lite.md — K195 session isolation required

- @concepts/youratto-brand-identity.md — folio / AttoVault metaphor; no vault-lock overclaim in mark
- @concepts/youratto-lean-conversion-page.md — K192 lean page trust copy must match controls

- @sources/gemini-atto-landing-demo-production-2026-07-23.md — K192 demo claims vs controls

- @entities/tools/license-guard-rs.md — K191

- @sources/atto-commercial-migration-plan-2026-07-23.md — K191 soft-gate offline

- @sources/gemini-atto-threat-model-2026-07-22.md — primary DR (K185)
- @concepts/atto-macos-gtm-gumroad.md — buyer-facing privacy FAQ source
- @concepts/gpuology-genealogy-agent-kit.md — vault / share / MCP product surfaces
- @concepts/openclaw-security-taxonomy.md — Context Manipulation / tool-call parallels for MCP
- @concepts/italian-citizenship-youtube-soft-flags.md — appointment proofs in vault; strip before LLM
- @sources/gemini-atto-macos-gtm-2026-07-22.md — companion GTM claims

## Raw Concept

Defensive checklist for Atto as a **local-first genealogy app**: what breaks when the threat is the endpoint, the supply chain, or a poisoned intake document — not a multi-tenant SaaS breach.

## Narrative

3 Sep Windows production audit (`c8a9ac2c6a56`) is **NOT READY**. ATTO-007: assist `--base` / `ATTO_OMLX_BASE` can send a raw `--file` off loopback without the strip-safe pack. Treat that as a local-first miss, not a feature.

### Actors (local-first set)

| Actor | Motivation | Primary asset at risk |
|-------|------------|------------------------|
| Snooping relative | Family secrets | Unlocked vault / screen |
| Device thief | Hardware / identity theft | Unencrypted vault at rest |
| Supply-chain attacker | Creds → backdoored builds | npm/uv lifecycle hooks |
| MCP / prompt injector | Tool abuse via poisoned intake | Vault key, GEDCOM exfil |
| Inadvertent user | Misconfig / paste-to-ChatGPT | Living-person PII on public web |

### Must-have (v1)

| Domain | Control |
|--------|---------|
| Crypto | AES-256-GCM on `~/AttoVault/`; passphrase UX ≥15 chars / spaces OK |
| Privacy | Exclude SSN / `_PRIV` / IDNO from Topola export; regex-strip 9-digit patterns before LLM |
| AI / MCP | Human Approve shows untruncated command; rotating approval tokens (no static passthrough) |
| Share | Cloudflare Access **fail-closed** on custom domain + `*.pages.dev` |
| Supply chain | `min-release-age=7d`, lockfile install, `--ignore-scripts` in CI |

### Explicitly out of scope (indie)

- Full GDPR DPA/DSAR program (household / controller framing — verify before EU ads)
- Immutable crypto audit of every UI click (attacker owns the disk)

### User-facing FAQ spine

- Data stays on disk unless user publishes share or opts into AI suggest  
- Full SSN never sent to LLMs (strip → fixture)  
- Family site fail-closed + allowlist — not public by default  
- AI suggest-only; Approve required for tree writes  

Align implementations with `../atto/SECURITY.md`. CVE / worm / Cloudflare-default claims in the DR need primary-doc check before HARD requirements. [OPEN QUESTION 2026-07-22]
