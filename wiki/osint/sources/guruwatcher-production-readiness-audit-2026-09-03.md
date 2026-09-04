---
title: GuruWatcher production-readiness audit (2026-09-03)
type: source
tags: [source, audit, guruwatcher, production-readiness, stripe]
keywords: [GuruWatcher, GW-01, github-invite, IMAP, newest-wins, Stripe]
related:
  - concepts/guruwatcher-newsletter-claim-ledger.md
maturity: draft
created: 2026-09-04
updated: 2026-09-04
read_status: read
---

## Relations

- @concepts/guruwatcher-newsletter-claim-ledger.md — newest-wins / claim extract
- Brief home: `../GuruWatcher/briefs/2026-09-04_gw-prod-audit.md`

## Raw Concept

| Field | Value |
|-------|--------|
| Title | GuruWatcher Production Readiness Audit |
| Type | code and test audit |
| Date | 2026-09-03 (America/New_York) |
| Repo | GuruWatcher `kevin-testing` / `fc996de7c91d` |
| Release | 0.1.7 |
| Filename | `production-readiness-audit-2026-09-03.pdf` |
| sha256 | `23de69d8f590e39f…` |
| Verdict | **NO-GO** |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` (post-archive) |

## Narrative

27 defects: 8 High, 15 Medium, 4 Low. 0 Critical. 487 tests passed, 6 failed on Windows/Python 3.14. 82% statement coverage. No known vuln in the currently resolved runtime set. No high-confidence live secret in the tracked tree.

**Release blockers that matter for alert-only Discord:**

- **GW-01** — one paid Stripe Checkout Session can invite unlimited GitHub logins (GET mutation). Mock: 20 usernames, one session, 20 invites.
- **GW-02** — Control Panel IMAP dotenv is `source`d in Docker as root. Passwords become shell.
- **GW-03** — `os.WNOHANG` crashes Windows start/status/stop.
- **GW-04** — default adapter `file_drop` silently drops configured IMAP.
- **GW-05** — `published_at` / RFC 5322 Date discarded; stale mail revives; newest-wins breaks.
- **GW-06** — HTML regex deletes `VIX < 20` comparison operators.
- **GW-07** — DOTALL regex binds a level to the wrong instrument across a newline.
- **GW-08** — per-source profiles are written and never read at extract time.

Do not promote 0.1.7 until the eight High findings have regression tests. No live Stripe/GitHub/Discord/IMAP mutations were performed.

## Snippets

> Disposition: NO-GO for production release

> The most urgent defect is an authorization design flaw in the Cloudflare GitHub-invite endpoint: one paid Stripe Checkout Session can be replayed indefinitely to invite arbitrary GitHub accounts into the private repository.

[Source: production-readiness-audit-2026-09-03.pdf]
