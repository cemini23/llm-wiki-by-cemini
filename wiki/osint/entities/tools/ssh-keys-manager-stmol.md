---
title: "SSH Keys Manager (Stmol, macOS)"
type: entity
tags: [tool, ssh-manager, macos-gui, security-anti-pattern, reject, k38]
keywords: [ssh, keys, manager, stmol, reject, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 27)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/Stmol/ssh-keys-manager-macos-app`
- **Tier (per source brief)**: **Reject**
- **License**: Reject regardless of license

## Narrative

Native macOS Swift app providing GUI over SSH keypair management + ~/.ssh/config editing. 2 GitHub stars.

### Integration vector

**Reject** — `~/.ssh/config` + `ssh-agent` are universally standard, scriptable, and sufficient. Unverified 2-star GUI handling root-privilege keys = unacceptable security surface.

### Risks

Disastrous security posture: privileged SSH keys (root access to prod) entrusted to unverified low-maturity third-party GUI.

[Source: Link Evaluation Brief Trading Stack.docx, URL 27]
