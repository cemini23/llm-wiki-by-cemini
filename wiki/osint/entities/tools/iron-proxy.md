---
title: Iron Proxy — policy egress proxy and request firewall
type: entity
tags: [entity, tool, proxy, egress-control, apache-2.0, cybersec-fit, k68, k233]
keywords: [iron-proxy, egress, oauth, jwt, request firewall, policy enforcement, mitm, ssrf]
related:
  - sources/multi-wiki-tool-eval-22url-2026-05-26.md
  - sources/eval-url-revenue-opportunity-2026-08-12.md
maturity: draft
created: 2026-05-26
updated: 2026-08-12
---

## Relations

- @sources/multi-wiki-tool-eval-22url-2026-05-26.md — K68 source
- @sources/eval-url-revenue-opportunity-2026-08-12.md — K233 20-URL eval, Integrate tier

## Raw Concept

Repository: `paradigmxyz/iron-proxy` (Apache-2.0, 596★, ~3.3MB, active 2026-08-10; release/Docker identity `ironsh/iron-proxy`). Go single-binary MITM egress proxy + built-in DNS server. Default-deny at the network boundary; boundary secret injection (workloads use proxy tokens, real creds swapped at egress); upstream IP deny list (SSRF/DNS-rebinding / IMDS protection for `169.254.169.254`, `fd00:ec2::254`, `fd20:ce::254`); per-request structured JSON audit trail; WebSocket/SSE streaming; explicit proxy (HTTP/HTTPS/SOCKS5) support; optional PostgreSQL MITM proxy with `SET ROLE` + RLS for per-tenant isolation (needs PgBouncer `pool_mode=session`).

## Narrative

**Verdict: GO Integrate (cyber local-abliterated-lab).** K68 flagged Adopt-eligible (cybersec); K233 Phase-0 confirms GO. Deploy as the mandatory egress gateway for LLM-driven authorized pentest/agent scripts: a compromised or hijacked agent sandbox exfiltrates only worthless proxy tokens, never real credentials. Single YAML config + single binary keeps ops friction low. Fuse local DNS denial for IMDS.

Risk: on-the-fly CA generation/injection can break TLS handshakes for legacy non-SNI tools — verify against the lab's older pentest tooling before default-on. Docs at docs.iron.sh.

[Source: paradigmxyz/iron-proxy README (retrieved 2026-08-12)]
