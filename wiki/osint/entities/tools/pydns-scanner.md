---
title: PYDNS-Scanner — Async DNS recon TUI (Adopt-tier, cybersec primary)
type: entity
tags: [tool, dns, recon, async, python, textual-tui, mit, adopt-tier, cybersec-cross-route, osint-cross-route, workflow]
keywords: [pydns-scanner, async dns, aiodns, httpx socks, slipnet, dnstt, noisedns, asn detection, textual tui]
related:
  - sources/tool-evaluation-wiki-fit-2026-05-13.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-13
updated: 2026-05-28
---

## Relations

- `@sources/tool-evaluation-wiki-fit-2026-05-13.md` — origin source (Doc 3, K42), Adopt-tier
- `@concepts/tool-evaluation-framework.md` — methodology

## Raw Concept

- **URL**: `https://github.com/xullexer/PYDNS-Scanner`
- **License**: MIT
- **Stars**: 330 / 2 open issues
- **Stack**: Python 3.11+, Textual (TUI), aiodns, httpx[socks], loguru, Rust
- **Tier**: Adopt
- **Primary fit**: Cybersec-wiki + Workflow

## Narrative

Async DNS recon scanner with SlipNet mode (DNSTT, NoiseDNS tunnel verification). SOCKS5 proxy testing via httpx[socks]. Textual TUI for laptop diagnostics.

### Cross-routing

- **OSINT-wiki**: ISP/AS-number detection heuristics for threat-actor infrastructure profiling
- **Workflow**: Textual TUI as diagnostic standard for network validation
- **Cybersec-wiki** (primary): SlipNet mode for red-team operational guides

### Phase-0 audit (2026-05-28)

Repo: `xullexer/PYDNS-Scanner` — **MIT**, ~382 stars, active (updated 2026-05-28).

| Check | Result |
|---|---|
| License | MIT confirmed |
| Maturity | Active project, upward adoption signal |
| Cemini fit | Cybersec/OSINT recon workflows; not core trading runtime |

**Verdict: CONDITIONAL-GO (cybersec + workflow)** — adopt patterns for recon/diagnostics only.

[Source: Tool Evaluation and Wiki Fit.docx URL 2 (retrieved 2026-05-13)]
