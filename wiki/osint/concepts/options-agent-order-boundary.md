---
title: Options-agent order boundary — loss limits outside the model
type: concept
related:
  - sources/arxiv-options-agent-safeguards-2610.24289-2026-10-20.md
  - sources/arxiv-certified-execution-harness-2610.31376-2026-10-23.md
  - sources/arxiv-amv-guard-2610.31446-2026-10-23.md
  - concepts/k293-osint-wave.md
  - concepts/k294-osint-wave.md
maturity: draft
updated: 2026-10-23
---

## Raw Concept

What this page answers: where must a check sit before an LLM agent is allowed to send an options order? From the K293 measurement of shipped broker and open-source options agents (arXiv 2610.24289).

## Narrative

An options order can keep the named direction and the named strategy and still change the loss by an order of magnitude. The paper's own example is a bull put spread that risks about $400 per contract. Drop the protective leg and the same direction is an uncovered put that can lose about $9,900. An equities risk check that watches buy versus sell does not see that change.

The measurement of 26 systems, including every broker-native agent interface in the sample:

| Check | Result |
|---|---|
| Systems that can place orders | 22 of 26 |
| Pre-trade limit enforced outside the model | 10 of those 22 |
| Mandatory human step | absent on 17 of 26 |
| Unbounded loss reachable | 13 of 26, including 6 of 8 broker interfaces |
| Text-source authentication or market-data cross-check | 0 of 26 |

The rule for this workspace: do not let a model send an options order. Put a loss limit, a leg-count check, and a human step on the order path, outside the model. Indirect text that the agent reads is an untrusted input. **No trade. No auto-arm. No pm scp.**

[TENTATIVE] single paper, arXiv 2610.24289, read 2026-10-20. The counts are the authors' screen of public repos and broker docs, not a Cemini audit.

**K294 (2026-10-23).** A tool call needs the same kind of outside check. The certified harness refuses the call when a capability, approval, or budget mark is missing. AMV-GUARD re-checks a memory only when the check can change the action. @sources/arxiv-certified-execution-harness-2610.31376-2026-10-23.md @sources/arxiv-amv-guard-2610.31446-2026-10-23.md
