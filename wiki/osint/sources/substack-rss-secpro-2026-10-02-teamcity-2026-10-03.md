---
title: "SecPro #254 — TeamCity ransomware and dev-infrastructure value (2026-10-02)"
type: source
tags: [source, k279, security, infra, no-poc]
keywords: [k279, teamcity, cve-2026-63077, ci-cd, mitigation]
related:
  - concepts/k279-security-wave.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
read_status: skimmed
---

## Relations

- @concepts/k279-security-wave.md

## Raw Concept

| File | `substack-rss-secpro-2026-10-02-254-teamcity-ransomware-and-the-new-value-of-dev.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-secpro-2026-10-02-254-teamcity-ransomware-and-the-new-value-of-dev.md` |
| Archive | egress-fi 2026-10-03 |
| URL | https://secpro.substack.com/p/254-teamcity-ransomware-and-the-new |
| Retrieved | 2026-10-03 |
| Dual-ID | **OSINT K279** |
| sha256 | `0006ae392f4a7bb8384b534ddacf8f56502626f8463999b83c90fd74fb0f14e6` |

## Narrative

A CI/CD vulnerability story with a clear defensive lesson. Tool names, patch levels, and mitigations only. **No exploit steps.**

JetBrains disclosed a critical unauthenticated remote-code-execution flaw in TeamCity On-Premises in July 2026. The cause class is unsafe deserialisation in the build-agent polling protocol. CISA added it to the known-exploited list on 5 August, and on 24 September identified it as exploited by ransomware groups.

The reason it is ransomware-relevant rather than a data-theft target: **a CI/CD server holds trusted access to repositories, build agents, credentials, artefact stores, and deployment systems.** Compromising it gives a path to everything downstream.

| Measure | Value |
|---------|-------|
| Severity | CVSS 9.8 |
| Fixed in | 2025.11.7 and 2026.1.3 |
| Internet-exposed vulnerable servers shortly after disclosure | about 700 |
| By late September | just over 160 |

### The mitigation, as stated

Patch TeamCity On-Premises to one of the two fixed versions, or apply the vendor's security patch plugin if an upgrade cannot be done immediately. TeamCity Cloud users need no action.

Detection indicators named: log entries for a conversion exception and a forbidden-class exception in the server log, plus unauthorised build agents whose names begin with a specific prefix.

The broader takeaways: check internet exposure, investigate the host, **rotate credentials**, map downstream access, and reduce privilege.

### Why this is on the wiki

Two reasons. First, the `rotation` step is the one teams skip — the server's credentials are the actual prize, so patching without rotating leaves the attacker in. Second, the shape generalises: any trusted automation host that reaches repositories and deploy targets is a high-value target, and our own runners are in that class.

No exploit steps, no payload, and no procedure on this page. FILE only. **No PoC.**
