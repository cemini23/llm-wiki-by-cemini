---
title: "tl;dr sec #354 — ARTEX and agentic hacking in the wild, the patchless window, backporting"
type: source
related:
  - concepts/agentic-offensive-security-kill-chain.md
  - concepts/patchless-window.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - entities/tools/artex.md
  - entities/tools/hexstrike-ai.md
  - entities/tools/mcptrace.md
  - entities/tools/abliterated-out-of-the-box.md
  - concepts/software-maintenance-institutional-insecurity.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [tl;dr sec] #354 - ARTEX & Agentic Hacking in the Wild, The Patchless Window, Backporting Security Fixes |
| Author | Clint Gibler (tl;dr sec) |
| Type | newsletter (RSS) |
| URL | https://tldrsec.com/p/tldr-sec-354 |
| Feed | tldrsec (https://rss.beehiiv.com/feeds/xgTKUmMmUm.xml) |
| Retrieved | 2026-11-12 |
| File | `newsletter-rss-tldrsec-2026-11-12-tldr-sec-354---artex-agentic-hacking-in-the-wild.md` |
| Read status | read |

## Narrative

This issue has one defensive headline (agentic attack frameworks observed in production), one measurement headline (the patchless window), and several item-level findings. Newsletter facts are single-source here. Treat incident details as `[TENTATIVE]` until a vendor advisory confirms them.

### ARTEX and agentic offensive frameworks in the wild

Datadog (Julie Agnes Sparks) observed **ARTEX**, an AI-native penetration-testing framework, attacking AWS environments in October 2026 `[TENTATIVE]`. The observed activity used compromised long-term IAM access keys. The tool searched CloudWatch logs for financial data, file paths and secrets such as `AKIA` keys. Datadog found hundreds of internet-exposed ARTEX consoles, often in Mandarin and hosted in Singapore or Hong Kong. It also saw unauthenticated abuse of public Amazon Cognito user pools.

ARTEX uses a multi-LLM architecture: a planner agent directs worker agents, and the workers record activity on a shared "blackboard" graph. Detection opportunities are concrete:

- characteristic user agents
- placeholder S3 object requests such as `zzz_nonexistent_abc.txt`
- `FilterLogEvents` calls with a consistent 1000-event limit
- noisy permission-denied errors during enumeration

Google Threat Intelligence Group and Mandiant observed several actors weaponizing open-source agentic frameworks: ARTEX, PentAGI and Hexstrike `[TENTATIVE]`. Some operations moved from initial access to deep system access in **about 15 minutes**. Reported capabilities include automated Active Directory reconnaissance, Kerberoasting, DCSync, and cloud profiling to harvest Azure storage keys. The speed comes with forensic noise.

Mandiant recommends five defensive layers:

1. Restrict control-plane access to trusted networks.
2. Migrate to short-lived workload credentials.
3. Run continuous vulnerability scanning.
4. Harden applications against feature abuse.
5. Detect identity velocity anomalies and API bursts.

GTIG places the current stage at multi-agent, low-sophistication attacks with little human interaction, and expects sophisticated fully autonomous attacks within 3–6 months `[TENTATIVE]`.

The operator reading for this workspace: long-term static keys are the entry condition. A stolen key plus an agent equals a fast, noisy intrusion. Detection must key on the burst shape, not only on the tool signature.

### The patchless window

Second Security (Elad Erez, Daniel Drizin, Or Elias) measures the gap between a public open-source fix and publication of its CVE `[TENTATIVE]`. The gap grew from **5.1 days in January 2026 to 39.2 days in August 2026** across 18,594 CVEs. Public exploits appeared within hours of the fix. The fastest examples were 4–16 hours, and the fastest tenth of all public exploits arrived in 1.8 days.

The consequence is structural. Attackers read the public diff. Defenders' scanners wait for the CVE. Vulnerability management therefore sees the vulnerability after the exposure window has opened. See @concepts/patchless-window.md.

### Backporting and vulnerability debt

Trail of Bits (Artem Dinaburg) used Codex with GPT-5.6 to identify and backport fixes to stable Linux kernel branches and distributions. The run produced **142 fixes covering 90 CVEs** `[TENTATIVE]`. The reported debt is large:

| Distribution | Unfixed CVEs | Packages | High or critical |
|---|---|---|---|
| Ubuntu 26.04 | 770 | 1,028 | 43.5% |
| Debian 13 | 4,562 | 1,128 | 39.9% |
| Stable kernel 5.10.y | >2,000 | — | — |

Trail of Bits offers free backporting help through Patch the Planet. Phil Venables' "vulnapocalypse" post makes the same point from the operations side: AI accelerates discovery and fix development, but deployment consumes about 60% of effort.

The defensive rule is that "patched in main" is not "users are protected." Measure the deployed version, not the upstream commit.

### Abliterated models in AppSec pentesting

Include Security (Laurence Tennant) compared abliterated GLM-5.3 against base GLM-5.3 in webapp pentesting with the OpenCode harness `[TENTATIVE]`. The abliterated model produced **26% fewer findings** in source-code analysis. It was not significantly better at exploit development. It did continue into post-exploitation without prompting, and it produced more robust proofs of concept in 4 of 5 cases against 2 of 5 for the base model. Reported risks are destructive actions, scope breaches, and supply-chain exposure from untrusted model hosting.

This finding matters for the local abliterated lab. The measured trade is not "same model without refusals." It is fewer static findings, more autonomous lateral action, and weaker hosting trust. See @concepts/local-abliterated-llm-pentest-stack.md.

### Cloud items

- Upwind (Dan Gansel) reports a cross-tenant data poisoning and exfiltration path in AWS Athena. The official `aws-sdk-pandas` library creates a predictable default S3 bucket for query results and treats attacker-owned buckets as legitimate `[TENTATIVE]`. AWS patched the Athena service earlier; the SDK never received the fix.
- Upwind also reports a cross-tenant RCE in the SageMaker Python SDK from predictable S3 bucket naming. The attack produced zero errors and no CloudTrail events in victim accounts and affected 200+ official example notebooks `[TENTATIVE]`. `[NEEDS VERIFICATION 2026-11-14]` against the current SDK release notes.
- Alex Smolen lists three IAM patterns that coding agents generate wrongly: explicit `Deny` statements, permission boundaries used outside delegated authority, and unnecessary `sts:GetCallerIdentity` allows.

Both cloud findings belong to one class: a predictable resource name creates a shadow resource that the victim's own tooling trusts. The control is to pin the bucket owner or use an explicit bucket name with `ExpectedBucketOwner`.

### Quick links

- **MCPTrace** — a Volatility 3 plugin that extracts MCP and JSON-RPC message candidates from Windows and Linux memory dumps. See @entities/tools/mcptrace.md.
- **AbliteratedOutTheBox** — a llama.cpp fork that removes refusals at inference time without weight changes. See @entities/tools/abliterated-out-of-the-box.md.
- Nudge Security describes eight discovery methods for shadow AI agents. No single method gives complete coverage.

### Other items

Prusa 3D printers had 14 vulnerabilities forming a full RCE chain (Yannick Dixken) `[TENTATIVE]`. An OpenSSH build on musl Linux accepted any password longer than 256 characters `[TENTATIVE]`. Both are `[NEEDS VERIFICATION 2026-11-14]` against upstream advisories.

## Snippets

> "Datadog's Julie Agnes Sparks observed ARTEX, an AI-native penetration testing framework, conducting real-world attacks against AWS environments in October 2026, using compromised long-term IAM access keys to search CloudWatch logs for financial data, file paths, and secrets like AKIA keys." [Source: newsletter-rss-tldrsec-2026-11-12-tldr-sec-354---artex-agentic-hacking-in-the-wild.md]

> "The gap between when an open source vulnerability fix becomes public and when its CVE is published … grew from 5.1 days in January 2026 to 39.2 days in August across 18,594 CVEs." [Source: newsletter-rss-tldrsec-2026-11-12-tldr-sec-354---artex-agentic-hacking-in-the-wild.md]

> "The abliterated model produced 26% fewer vulnerability findings in source code analysis and wasn't significantly better at exploit development, though it did push further into post-exploitation without prompting." [Source: newsletter-rss-tldrsec-2026-11-12-tldr-sec-354---artex-agentic-hacking-in-the-wild.md]
