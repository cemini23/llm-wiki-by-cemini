---
title: Agentic offensive-security kill chain
type: concept
tags: [concept, agent-security, red-team, llm-pentest, kill-chain, agent-phishing, sandbox]
keywords: [agentic red team, agent-phishing, worker orchestrator separation, 2606.24496, offensive security agents]
related:
  - sources/arxiv-2606-24496-red-teaming-the-agentic-red-team.md
  - concepts/llm-pentest-automation.md
  - concepts/agent-runtime-guardrails.md
  - concepts/red-team-operations.md
  - concepts/agent-vm-sandboxing.md
  - concepts/docker-agent-sandbox-allowlist-proxy.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/airecon.md
  - entities/tools/pentest-ai-agents.md
  - entities/tools/pentest-ai.md
  - entities/tools/iron-proxy.md
  - sources/arxiv-zero-apt-llm-pentest-2606.05567-2026-06-05.md
  - concepts/mcp-security-posture.md
  - concepts/security-tool-orchestration-determinants.md
  - sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md
  - concepts/chainwatch-mcp-kill-chain-detection.md
  - concepts/ethics-autonomous-offensive-ai-agents.md
  - concepts/agent-decoy-defense-autonomous-pentest.md
  - entities/tools/cyberstrike.md
  - sources/newsletter-rss-tldrsec-2026-11-12-tldr-sec-354---artex-agentic-hacking-in-the-wild.md
  - entities/tools/artex.md

  - sources/arxiv-ethics-autonomous-offensive-ai-2607.20255.md
maturity: draft
created: 2026-06-25
updated: 2026-11-14
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-containment.mdc"
---

## Relations
- @entities/tools/cyberstrike.md — AGPL AI offensive harness — CONDITIONAL-GO lab/VM only (Phase-0 2026-08-02)
- @sources/arxiv-ethics-autonomous-offensive-ai-2607.20255.md
- @concepts/ethics-autonomous-offensive-ai-agents.md
- @sources/arxiv-2606-24496-red-teaming-the-agentic-red-team.md — primary audit (2606.24496)
- @concepts/llm-pentest-automation.md — Tier-2 deployment methodology
- @concepts/agent-vm-sandboxing.md — substrate isolation complement

## Raw Concept

Ingest 2026-06-25: arXiv:2606.24496 — security model for **agentic offensive-security tools** when the engagement target is adversarial (honeypot / active defender).

## Narrative

### Architecture abstraction

```
Orchestrator (secrets, memory, skills, UI, high-privilege APIs)
    ↔  Agent harness / guardrails
Worker (bash runtime, tool execution)  ← treat as UNTRUSTED after any target contact
Target T (adversary-controlled during pentest)
```

### Kill chain stages

| Stage | Objective |
|-------|-----------|
| **LLM manipulation** | Agent-phishing: staged artifact on `T` → download + execute gates |
| **Worker RCE** | Trojanized binary/config (cfgunpack, db-restore, pwcrypt patterns) |
| **Lateral movement** | Worker → orchestrator (shared API keys, host-network, docker.sock) |
| **Secrets exfil** | LLM API keys, Cobalt Strike tokens, cross-session findings |
| **Persistence** | Skill injection via unauthenticated internal APIs (RedAmon-class) |
| **Guardrail bypass** | CAI/xalgorix guardrails fail under active adversary model |
| **Sandbox escape** | Privileged Docker, `--network=host`, orchestrator exec from worker message |

### Agent-phishing (prompt-injection-free)

1. Craft payload with hidden malicious functionality (plausible offensive artifact)
2. Stage on honeypot as **critical artifact** for operation progress
3. Agent downloads + executes after inspection → RCE

**97.8%** success across 8 agents × 6 frontier LLMs (2606.24496 Table 3). Relies on **download gate** + **execute gate**, not injected prompts.

### Landscape audit (Table 1 summary)

10/12 tools: deterministic worker RCE + secrets exfil + host compromise path. Failures: **STRIX** (no reliable chain), **Artemis** (limited). **METATRON / nebula / xalgorix**: no OS sandbox — host compromise immediate.

### Secure design principles (§9 steal-from)

| Principle | Implementation |
|-----------|----------------|
| **Malicious worker model** | Assume worker compromise after target engagement |
| **No secrets in worker** | API keys on orchestrator; proxy tool calls |
| **Least-privilege Docker** | No docker.sock, no `--network=host`, no privileged unless scoped |
| **Worker↔orchestrator isolation** | No shared blanket API keys; per-user authZ on internal APIs |
| **Orchestrator-enforced guardrails** | Deny lists ineffective if only worker-side |
| **Egress proxy + human gate** | High-impact actions require orchestrator approval |

Pairs with @concepts/llm-pentest-automation.md Tier-2 scope gates — **scope ≠ sandbox security**.

See `briefs/2026-06-25_agentic-red-team-secure-architecture-handoff.md` and `briefs/2026-06-25_agent-phishing-tier2-eval-checklist.md`.

`[TENTATIVE]` — audit covers default configs of 12 OSS tools; hardened deployments not measured.

### In the wild (November 2026)

Agentic attack tooling now appears in real intrusions, not only in lab studies. Datadog observed ARTEX against AWS environments in October 2026 `[TENTATIVE]`. Google Threat Intelligence Group and Mandiant observed several actors using ARTEX, PentAGI and Hexstrike `[TENTATIVE]`. Some operations reached deep system access in about 15 minutes from initial access.

The reported progression adds two stages to the framework timeline. Stage 6 is a multi-agent, low-sophistication attack with little human interaction, expected within 1–3 months. Stage 7 is a sophisticated fully autonomous attack, expected within 3–6 months `[TENTATIVE]`.

Two properties change the defence. First, speed: a 15-minute intrusion removes the human review loop from containment. Second, noise: the frameworks generate many permission-denied errors and API bursts. The noise is a detection opportunity, so do not suppress it as benign scanner activity.

Mandiant recommends five layers: restrict control-plane access to trusted networks, migrate to short-lived workload credentials, scan continuously, harden applications against feature abuse, and detect identity velocity and API bursts. The first two remove the entry condition, because the observed access used long-term static keys.

See @entities/tools/artex.md for the detection signatures.

## Snippets

| Agent | Notable misconfig (2606.24496) |
|-------|-------------------------------|
| AIRecon | `--network=host` → orchestrator API abuse |
| CAI / PentAGI | docker.sock mount |
| RedAmon | Shared internal API key, no per-user checks |
| PentestGPT | `python_session` runs on host orchestrator |

[Source: arxiv-2606.24496]
