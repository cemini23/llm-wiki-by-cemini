---
title: "Harness fingerprinting — a harness leaks identity through timing, redaction, and scheduling"
type: concept
related:
  - sources/arxiv-say-shibboleth-fingerprinting-2611.12386.md
  - concepts/harness-fingerprint-trajectory-routing.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/expert-data-rl-environments.md
  - sources/newsletter-rss-latent-space-2026-11-09-what-frontier-labs-buy-a-data-deep-dive-with-han.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: from the target side only, what reveals which model and harness is attacking?

Synthesised from `@sources/arxiv-say-shibboleth-fingerprinting-2611.12386.md`.

## Narrative

The defender sees only the effects of an agent's actions. It cannot query the model. The paper calls this setting blind and passive.

**Shibboleth traps** are honeypot services that make an informative interaction a condition for a resource. No prompt injection is needed; the agent reveals itself while pursuing its own goal.

Three signal classes:

| Gate | What it elicits | What it reveals |
|------|-----------------|-----------------|
| Declarative | An MCP sampling request asking the agent to name its model; capability negotiation client name | Model id string, harness name |
| Text | Required written text, such as a change log entry | Model-specific wording ("accent") |
| Behavioural | A held-open call, a masked secret, varied scheduling | Timeout policy, redaction behaviour, tool-call concurrency |

Results: 90% to 92% top-1 accuracy across 15 models when declarative and behavioural signals are combined. A fixed rule set identified the harness with 92% accuracy across four harnesses, with no learned component. When six models were told to report a false name, declarative accuracy fell but behavioural text still carried signal.

### What this means for harness designers

Every harness makes observable promises:

- How long it waits before abandoning a call.
- Whether it redacts secrets in tool output before the model sees them.
- Whether it runs tool calls concurrently or in sequence.

Those are the behaviour of the harness, and they are visible to any service the agent touches. Two consequences:

1. **A harness cannot be anonymous by hiding strings.** Timing and redaction are enough.
2. **A fingerprint is also a diagnostic.** The same three probes can distinguish two Cemini harness versions during a migration, or two lane configurations during a `/route` failover test.

### Relation to CoTrace

`@concepts/harness-fingerprint-trajectory-routing.md` uses harness fingerprints to prevent a harness-tuned agent from silently travelling to another host. This paper measures the same signal from the outside. Together they bracket the idea: harness identity is real, detectable, and portable.

## Snippets

> "These probes reveal how a harness masks secrets in tool output, enforces command time limits, and schedules tool calls, using only the effects visible in subsequent requests." [Source: arxiv-2611.12386-say-shibboleth-fingerprinting-the-llms-and-harne.pdf p.1]
