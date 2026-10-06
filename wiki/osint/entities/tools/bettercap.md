---
title: "bettercap — network attack / MITM framework (reference)"
type: entity
tags: [tool, cybersecurity, offensive, mitm, reference]
keywords: [bettercap, mitm, network-attack, wifi, ble, go, arp-spoof, reference]
related:
  - concepts/local-abliterated-llm-pentest-stack.md
  - sources/eval-github-repo-revenue-evaluation-2026-07-29.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @concepts/local-abliterated-llm-pentest-stack.md — authorized-lab context
- @sources/eval-github-repo-revenue-evaluation-2026-07-29.md — where bettercap was first evaluated

## Raw Concept

- **Repo:** `github.com/bettercap/bettercap`
- **Type:** Network attack / MITM framework (Go)
- **Referenced by:** `../Cybersecurity wiki/briefs/2026-08-03_k219-appsec-llm-protocol.md` — the citation pointed here and the page did not exist

## Narrative

**bettercap** is a widely used, actively maintained framework for network reconnaissance and man-in-the-middle attacks — Wi-Fi (deauth, evil-twin), BLE, Ethernet (ARP/DNS spoof), and HTTP/HTTPS proxying and script injection. Written in Go, with a scriptable caplet system.

### Why it matters here

Cited from the cybersecurity wiki's K219 appsec/LLM-protocol brief. It is **reference material for the authorized local abliterated/cyber lab** — useful for testing agentic tooling against a hostile-network model.

### Boundary

**Authorized-lab only.** No PoC in the wiki; no unattended use against third-party networks. Live capture and spoofing on networks the operator does not own is out of scope.

[Source: gap-fill from `../Cybersecurity wiki/briefs/2026-08-03_k219-appsec-llm-protocol.md`; created 2026-10-06]
