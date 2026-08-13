---
title: "tl;dr sec #341 — Hugging Face incident talk + CSS webmail bomb + GitHub supply chain (2026-08-13)"
type: source
tags: [newsletter, tldrsec, k236, cyber]
keywords: [hugging-face, CSS exfiltration, webmail, wp2shell, RubyGems, GitHub Actions, npm, promptware, beyond-zero, agent identity]
related:
  - concepts/agent-setup-instruction-supply-chain.md
  - concepts/agent-safety-executable-evaluation.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: read
---

## Relations

- @concepts/agent-setup-instruction-supply-chain.md — promptware / memory-file poisoning extends the agent-supply-chain model
- @concepts/agent-safety-executable-evaluation.md — agent identity + least-privilege mitigations pair with executable safety evals

## Raw Concept

| Field | Value |
|-------|--------|
| Title | tl;dr sec #341 — Hugging Face Incident Black Hat Talk, CSS Bomb in your Inbox, GitHub Supply Chain Security Improvements |
| URL | https://tldrsec.com/p/tldr-sec-341 |
| sha256 | `9cbe6610adad1ca8d0433c679542f97ab2c769a0a9a4170d06bec9e3943c4e51` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-tldrsec-2026-08-13-tldr-sec-341---hugging-face-incident-black-hat-t.md` |
| retrieved | 2026-08-13 |

## Narrative

Black Hat USA 2026 recap issue. Highlights routed to `@cybersecurity-wiki/`:

- **OpenAI–Hugging Face incident deep-dive** (Eric Wallace, Michael Dalton) — >500K views in a week; the timeline/details of the HF agent compromise (continues the #339 "HF AgentBaiting" thread).
- **CSS: the bomb inside your inbox** (PortSwigger Gareth Heyes Black Hat). CSS in webmail clients weaponized to bypass sanitizers, exfiltrate tokens, spoof UI, steal passwords across Gmail/Outlook/Fastmail/ProtonMail: nesting attribute selectors to brute-force Medium 12-char hex tokens, indirect prompt injection into OpenAI's Atlas browser, font-height oracles + animations for token exfiltration when CSP blocks external resources, real-time keyloggers via `select` elements. Plus **Shazzer** — shared browser fuzz-testing platform.
- **LLM-discovered WordPress RCE** — Adam Kues (Assetnote/SL Cyber) used GPT 5.6 Sol Ultra + OpenAI Cycle Double Cover prompt to find wp2shell: a pre-auth RCE chain in WordPress core (batch API desync → SQLi via `author__not_in` → post-cache poisoning → `customize_changeset` → admin). ~$25 / 10 hours. Affects ~40% of the internet. Wiz documented exploitation in the wild. Key meta-observation: human understanding time is 2-5x model discovery time.
- **RubyGems CDN cache vuln** (Truffle Security) — gzip-compressed authenticated `GET /api/v1/api_key` responses cached at Fastly edges up to 1h; two config failures (no private cache directives + no vary on Authorization); legacy API keys revoked.
- **GitHub supply chain improvements** — safer `pull_request_target` defaults in `actions/checkout` ("pwn requests"), read-only Actions cache for untrusted triggers, staged npm publishing (2FA beyond CI creds), npm v12 install scripts off by default, 3-day Dependabot cooldown, 72-hr read-only mode for high-impact npm accounts, Actions network egress firewall (technical preview).
- **deadair** (Nikhil Satyakrishna) — CLI detecting "dead" detection rules that can't see their data (no matching source, stale/empty sources, missing fields, ingest-lag blind windows); Elastic Security + OpenSearch Security Analytics; read-only metadata APIs.
- **promptware** (Daniel Koifman) — semantic malware delivered via prompt injection that hijacks AI coding assistants (Claude Code, Cursor, Devin) by poisoning memory-config files; no stable signatures; C2 via approved SaaS (GitHub Issues, RabbitMQ); detection is agent-side: FIM on memory files, behavioral baselining of tool calls, privilege auditing.
- **Least privilege for AI agents** (Microsoft) — agent as first-class principal, task-based RBAC, curated tool allowlists, JIT time-limited entitlements, downstream re-verification, auditability (agent identity/role/scope/action/on-behalf-of).
- **Beyond Zero** (Google, Adkins/Ramamoorthy) — zero trust pushed into the authorization layer: resource-level action evaluation across APIs + MCP, static+dynamic policies, automated investigations triggering containment, on-demand verification challenges for users and AI agents.

**Route:** `@cybersecurity-wiki/` brief — HF incident / supply chain / CSS bomb; AI-agent security items (promptware, agent identity, Beyond Zero) fold into the cyber lab's agent-security lane.

[Source: https://tldrsec.com/p/tldr-sec-341 (retrieved 2026-08-13)]
