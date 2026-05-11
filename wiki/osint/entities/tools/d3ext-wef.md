---
title: "WEF — Wi-Fi Exploitation Framework (D3Ext)"
type: entity
tags: [tool, wifi-offensive, out-of-scope, reject, k38]
keywords: [d3ext, wef, reject, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 21)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/D3Ext/WEF`
- **Tier (per source brief)**: **Reject**
- **License**: Offensive security; out-of-scope regardless of license

## Narrative

Bash-script framework for offensive WPA/WPA2/WPA3/WPS/WEP analysis + active exploitation. Wraps aircrack-ng, hcxdumptool, hostapd. DoS via 802.11 management frames, PMKID capture, offline brute-force.

### Integration vector

**Reject** — complete domain mismatch with Cemini. Wi-Fi offensive security is orthogonal to trading + wiki operational objectives.

### Risks

Bash scripts requiring root + offensive Wi-Fi tools = security posture disaster. Outside scope, outside trust boundary.

[Source: Link Evaluation Brief Trading Stack.docx, URL 21]
