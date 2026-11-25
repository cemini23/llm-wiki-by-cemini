---
title: "Claude-BugHunter — bug-bounty skill bundle with a cross-engagement ledger (MIT code / CC-BY-4.0 prose)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - "@osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md"
updated: 2026-11-24
maturity: draft
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md, URL 5,
**Extract** tier. Routed to the cybersec wiki and the local operator lab.

The question this page answers: **how does a hunter keep what it learned on one target
from being thrown away on the next?**

## Narrative

### What it does

A Claude Code skill bundle for bug hunting and external red-team work. Three parts
carry the value:

- **methodology skills** — recon, enumeration, and report writing as procedures
- **`memory.py`** — a cross-engagement ledger. Findings, dead endpoints, and confirmed
  false positives persist between engagements, so the next run starts from knowledge
  instead of from zero.
- **Burp MCP wiring** — the agent drives a Burp session through MCP rather than parsing
  proxy exports.

### Why the ledger is the real extract

Most offensive skill packs are prompt text. This one keeps state. The ledger is what
makes a second engagement on the same programme cheaper than the first — which is the
actual cost problem in this work.

The same ledger shape applies to the Atto recon lane, where a family-research target
accumulates dead ends across sessions.

### Licence split

**Code is MIT. Methodology prose is CC-BY-4.0.** The two must be handled separately:
copy code under MIT with attribution, and quote prose under CC-BY with attribution and
an indication of changes. Neither is a block; both require the notice.

### Phase-0, 2026-11-16

| Check | Result |
|-------|--------|
| Licence | MIT (code) / CC-BY-4.0 (prose) — permissive [CONFIRMED] |
| Maturity | 7.4k stars, pushed the day of the check, 18 open issues |
| Cloud requirement | None stated; local skills plus a local Burp instance |
| Local gap | `local-abliterated-lab` is **not present** on this machine |

The gap cannot be checked, because the project repository does not exist here. The item
therefore cannot be queued. [CONFIRMED — `Projects/` listing 2026-11-16]

### Status

Extract, reference only. Queued nowhere until the operator lab repository exists.

### Re-graded 2026-11-24 — Context

The 2026-11-24 batch re-evaluated this URL and graded it **Context**. The item is still
blocked: the operator lab repository does not exist on this machine, so no gap can be
checked. [CONFIRMED — `Projects/` listing 2026-11-24]

The report names four specific artifacts worth indexing as reference, and they are more
concrete than the earlier batch: a **7-question validation gate**, **VRT severity
mapping**, a **scope-enforced workflow structure**, and a **disclosed-report
taxonomy**. The last two are the durable ones — scope enforcement is what separates
authorised testing from its opposite, and a report taxonomy is what makes a finding
submittable.

See @osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md.

## Snippets

> A Claude Code skill bundle for bug hunting and external red-team work.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 5]

## Dead Ends

- **Queuing an item whose target project is absent.** The gap cannot be verified, so the
  tier cannot be acted on.
