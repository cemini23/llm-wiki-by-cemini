---
title: syncthing — Decentralized cryptographic file sync (Adopt-tier, MPL-2.0)
type: entity
tags: [tool, file-sync, decentralized, cryptographic, mpl-2-0, adopt-tier, workflow, osint-cross-route]
keywords: [syncthing, file synchronization, mpl-2.0, ecdsa, decentralized, local-first, threat-intel replication]
related:
  - sources/multi-wiki-link-eval-prompt-2026-05-13.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-13
updated: 2026-05-28
---

## Relations

- `@sources/multi-wiki-link-eval-prompt-2026-05-13.md` — origin source (Doc 2, K42), Adopt-tier
- `@concepts/tool-evaluation-framework.md` — methodology

## Raw Concept

- **URL**: `https://github.com/syncthing/syncthing`
- **License**: MPL-2.0
- **Stars**: 84k / 369 open issues
- **Stack**: Go (84.5%), HTML, JavaScript
- **Version**: v2.1.0 (May 2026)
- **Tier**: Adopt
- **Primary fit**: Workflow

## Narrative

Continuous decentralized file synchronization with cryptographic primitives. ECDSA-signed upgrades. Cross-platform host network mode.

### Cemini use case

Replicate Claude Code configurations + local MCP server artifacts + Markdown databases across multiple analyst laptops. Cross-routed to OSINT-wiki for decentralized threat-intel dataset replication.

### Phase-0 audit (2026-05-28)

Repo: `syncthing/syncthing` — **MPL-2.0**, ~85k★, mature Go project with extensive tests.

**Verdict: CONDITIONAL-GO (workflow)** — acceptable for decentralized laptop config sync; MPL-2.0 is weak copyleft (file-level). Avoid modifying and distributing forked syncthing binaries inside proprietary deliverables without legal review.

[Source: Multi-Wiki Link Evaluation Prompt.docx URL 36 (retrieved 2026-05-13)]
