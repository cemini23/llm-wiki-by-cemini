---
title: "drift — Zero-Config Encrypted File Transfer (Rust)"
type: entity
tags: [tool, file-transfer, encryption, websocket, rust, workflow, k39, adopt-tier]
keywords: [drift, encrypted file transfer, scp replacement, x25519, chacha20-poly1305, workflow]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 1)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL** (per source brief): `github.com/aeroxy/drift`
- **Tier (per source brief)**: **Adopt** (Workflow only)
- **License** (per source brief): MIT
- **Stack**: Rust 1.82+, single static binary, WebSocket, X25519 + ChaCha20-Poly1305, HTML/Web UI
- **Maturity** (per source brief): v0.4.0 May 2026; author describes as "still very early"

## Narrative

Single-binary Rust file-transfer utility — WebSocket-routed (NAT-friendly), end-to-end encrypted, no SSH keys or cloud buckets required. Eval brief proposes adoption strictly for shipping briefs/ laptop → Hetzner production.

### Integration vector

**Adopt — Workflow only**. Replaces manual `scp` for brief shipping. Single-developer-laptop daemon, port-restricted to developer static IP via UFW.

### Risks

1. **Single-dev bus-factor** (aeroxy is sole maintainer). If abandoned, upstream WebSocket / crypto vulnerabilities will go unpatched.
2. **Non-standard open port** on production Hetzner — institutional acquirers flag these in due diligence; must be heavily documented as authorized developer ingress.
3. **No delta transfer** — disqualifies for wiki sync (rsync over SSH retained for `wiki/`).
4. **Workflow overlap**: Cemini already uses scp; drift's primary win is "no SSH-key management" — minor productivity gain.

### NEEDS VERIFICATION

- GitHub stars / contributor count / issue activity (eval brief lacked exact numbers)
- Resident memory consumption when idle
- License file actually present in repo (Phase-0 to confirm)

### Phase-0 audit status

Not yet performed. Defer install pending. Low-priority audit (Adopt scope is narrow, low-risk).

[Source: Evaluating Project Links for Stacks.docx URL 1; retrieved 2026-05-11]
