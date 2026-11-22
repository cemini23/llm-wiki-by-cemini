---
title: "Cyber Chaos Monkey (CCM) — continuous adversarial testing of production"
type: entity
maturity: draft
related:
  - sources/newsletter-rss-tldrsec-2026-11-19-tldr-sec-355---cyber-chaos-monkey-offsec-harness.md
  - concepts/agentic-containment-principles.md
  - concepts/cyber-range-autonomous-incident-response-agents.md
  - concepts/agentic-offensive-security-kill-chain.md
  - entities/tools/defending-code-reference-harness.md
updated: 2026-11-22
---

## Raw Concept

What prompted this page: the tl;dr sec #355 summary of Shopify's Cyber Chaos Monkey (CCM). Source is the newsletter; the primary blog post was not read here.

## Narrative

Cyber Chaos Monkey is an AI agent system that continuously attacks Shopify production infrastructure. It uses live credentials, source code, threat intelligence, past reports, and infrastructure records. The goal is to find vulnerabilities before an external attacker does.

**Architecture.** Two components:

- **Discovery** — frontier cyber models identify candidate vulnerabilities.
- **Sandbox** — agents exploit the candidates with live requests, log analysis, and fuzzing.

**Safety design.** Four controls:

- Containerization of the executor.
- Egress controls.
- Credential proxies, so the agent never holds raw secrets.
- Two-person integrity, implemented as a separately aligned judge agent that monitors the executor and can kill it on a Rules-of-Engagement violation.

**Reported results.** Tens of thousands of offensive engagements, dozens of impactful findings, no outages. `[TENTATIVE]` `[NEEDS VERIFICATION 2026-11-22]` against the Shopify engineering post.

**What to copy for a lab.** The judge agent that can halt the executor is the transferable pattern. It is an external, separately aligned monitor, not a self-check. The credential proxy is the second pattern: the agent acts through a broker that scopes and logs each use.

**What not to assume.** The newsletter does not list detection coverage, false-positive handling, or how findings were triaged. Those are open questions before adoption.

[Source: newsletter-rss-tldrsec-2026-11-19-tldr-sec-355---cyber-chaos-monkey-offsec-harness.md]

## Snippets

> "A 'two-person integrity' approach where a separately-aligned judge agent monitors and can instantly kill the executor agent if it violates Rules of Engagement."
[Source: tl;dr sec #355]
