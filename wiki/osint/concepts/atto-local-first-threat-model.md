---
title: Atto local-first threat model — vault, MCP, share
type: concept
tags: [concept, genealogy, atto, security, threat-model, mcp, k185, draft]
keywords: [AttoVault, AES-256-GCM, SSN strip, Cloudflare Access, min-release-age, suggest-only, STRIDE]
related:
  - sources/gemini-atto-threat-model-2026-07-22.md
  - concepts/atto-macos-gtm-gumroad.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/openclaw-security-taxonomy.md
  - sources/gemini-atto-macos-gtm-2026-07-22.md
maturity: draft
created: 2026-07-22
updated: 2026-07-22
---

## Relations

- @sources/gemini-atto-threat-model-2026-07-22.md — primary DR (K185)
- @concepts/atto-macos-gtm-gumroad.md — buyer-facing privacy FAQ source
- @concepts/gpuology-genealogy-agent-kit.md — vault / share / MCP product surfaces
- @concepts/openclaw-security-taxonomy.md — Context Manipulation / tool-call parallels for MCP
- @sources/gemini-atto-macos-gtm-2026-07-22.md — companion GTM claims

## Raw Concept

Defensive checklist for Atto as a **local-first genealogy app**: what breaks when the threat is the endpoint, the supply chain, or a poisoned intake document — not a multi-tenant SaaS breach.

## Narrative

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

Align implementations with `../atto/SECURITY.md`. CVE / worm / Cloudflare-default claims in the DR need primary-doc check before HARD requirements. [NEEDS VERIFICATION 2026-07-22]
