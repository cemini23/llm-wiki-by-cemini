---
title: "Say Shibboleth — fingerprinting the LLM and harness behind an agentic attack"
type: source
related:
  - concepts/harness-fingerprinting-telemetry.md
  - concepts/harness-fingerprint-trajectory-routing.md
  - concepts/measurement-integrity-mcp-security-eval.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Say Shibboleth: Fingerprinting the LLMs and Harnesses Behind Agentic Attacks |
| Author | Dario Pasquini, Reworr, Giuseppe Ateniese, Manish Bhatt, Sergej Epp |
| Type | arXiv paper (cs.CR), 2611.12386 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.12386-say-shibboleth-fingerprinting-the-llms-and-harne.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 19 |
| Read status | read |

## Narrative

The defender observes only effects at the target. It cannot query the attacker's model. The paper calls this setting **blind and passive**.

The technique is a **shibboleth trap**: a honeypot service that makes an informative interaction a condition for a resource the agent wants. No successful prompt injection is needed. The agent pursues its own objective and reveals itself while doing so.

Three gates are used:

- **Declarative gate.** An MCP sampling request asks the agent to name the model it serves. Capability negotiation also carries a client name, which can reveal the harness.
- **Text gate.** The agent must write text, such as an operator log entry. Model-specific wording, which the authors call **accent**, is classified against known traces.
- **Behavioural gate.** The service holds a call open, masks a secret in tool output, or varies scheduling. The effects visible in later requests reveal harness behaviour: timeouts, redaction, and tool-call concurrency.

Results:

- Combined declarative and behavioural inference reached 90% to 92% top-1 accuracy across 15 candidate models.
- In a separate four-harness experiment, fixed probe rules identified the correct harness with 92% accuracy. The harness readout contains no learned component.
- When six models were told to conceal their identity, declarative accuracy fell, but behavioural text still carried identifying signal.

The consequence cuts both ways. A defender can attribute an attack. An operator who wants an unattributable agent cannot rely on hiding the name. **A harness leaks its identity through timing, redaction, and scheduling, not only through strings.**

## Snippets

> "We introduce a technique we call shibboleth traps: modular honeypot services designed to elicit discriminative behaviors from agentic attackers." [Source: arxiv-2611.12386-say-shibboleth-fingerprinting-the-llms-and-harne.pdf p.1]

> "When instructed to conceal their identity, agents still leave useful behavioral evidence even as their declarations become uninformative." [Source: arxiv-2611.12386-say-shibboleth-fingerprinting-the-llms-and-harne.pdf p.1]
