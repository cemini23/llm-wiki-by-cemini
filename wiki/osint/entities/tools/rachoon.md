---
title: "Rachoon — self-hosted invoicing / PDF engine (Gotenberg billing for Atto)"
type: entity
tags: [tool, invoicing, billing, atto, pdf, agpl, k237]
keywords: [Rachoon, Gotenberg, Nunjucks, AdonisJS, Nuxt, invoices, PDF generation, self-hosted billing]
related:
  - sources/eval-url-revenue-opportunity-2026-08-14.md
  - concepts/e2ee-vault-share.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-14.md — K237 eval batch (Extract, Atto billing)
- @concepts/e2ee-vault-share.md — vault + automated branded-agreement combo

## Raw Concept

What prompted this page: K237 eval tiers rachoon as **Extract** for Atto Concierge billing — automated branded PDF retainers + payment tracking. Verified via gh api: **AGPL-3.0** (matches docx), 3.9MB → cloned as reference to `.local/adopts/rachoon` (8MB).

## Narrative

Self-hosted invoicing platform (Nuxt.js frontend, AdonisJS backend, PostgreSQL, Docker-ready). Core pattern worth extracting: **Gotenberg PDF engine + Nunjucks templating** for professional, branded, multi-currency/tax invoices, offers, payment tracking, and dashboard insights.

### Steal-for-Atto (AGPL isolate — pattern only)

- **Gotenberg PDF compilation** as a self-hosted replacement for SaaS billing tools ($30–$60/mo savings): standardize branded invoice / retainer / agreement generation for ≥$2.5k concierge engagements and $499–$899 kit sales.
- **Nunjucks template customization** for branded document styling.
- **Multi-currency + tax support** — international clients seeking Italian citizenship records.
- **AGPL isolate**: pattern + Docker orchestration extraction only; **no upstream code embedding in proprietary Atto deliverables** (same discipline as ente).
- Business risk: client billing records need isolated DB backups to prevent invoice-data corruption.

**Brief:** folded into Atto `2026-08-14_k237-ente-e2ee-vault.md` (E2EE vault + branded billing combo). Tier: `[TENTATIVE]`.
