---
title: "Offsec Harness Index — open-source offensive agent harnesses that ran in real operations"
type: entity
maturity: draft
related:
  - sources/newsletter-rss-tldrsec-2026-11-19-tldr-sec-355---cyber-chaos-monkey-offsec-harness.md
  - concepts/agentic-offensive-security-kill-chain.md
  - entities/tools/artex.md
  - entities/tools/cyberstrike.md
  - entities/tools/hexstrike-ai.md
  - entities/tools/pentest-ai-agents.md
updated: 2026-11-22
---

## Raw Concept

What prompted this page: the "Offsec Harness Index" link in tl;dr sec #355. The index itself was not fetched; this page records what the newsletter and the wiki already carry.

## Narrative

The Offsec Harness Index, by Daniel Miessler, tracks two things. First, open-source offensive AI agent harnesses that can be verified on GitHub. Second, which of them are known to have run in real operations. It is a tracking resource, not a tool.

It answers a recurring question for this wiki: which harness actually appears in intrusion reports, as distinct from which one has stars or a demo. The wiki already has entity pages for several candidates:

- @entities/tools/artex.md — reported in AWS intrusions.
- @entities/tools/cyberstrike.md — one of Elastic's five analyzed frameworks.
- @entities/tools/hexstrike-ai.md — one of Elastic's five.
- @entities/tools/pentest-ai-agents.md — AI pentest agent landscape.

**Elastic's five-framework set** (ARTEX, CyberStrikeAI, Cairn, PentAGI, HexStrike) is the closest published cross-section. Elastic found that none enforce authorization in code by default and three explicitly tell the model it is pre-authorized. That is a design finding, independent of the operator's intent.

**Use.** Treat the index as a candidate list for the lab's harness evaluation. A harness with a verified real-world run matters more than a benchmark score. Verify the claim against the cited report before you record it here.

**Open question.** The index was not read in this pass. Its inclusion criteria and update cadence are unverified.

[Source: newsletter-rss-tldrsec-2026-11-19-tldr-sec-355---cyber-chaos-monkey-offsec-harness.md]

## Snippets

> "An attempt to track the open-source offensive AI agent harnesses we can verify on GitHub, and to show which ones attackers are known to have run in real operations."
[Source: tl;dr sec #355]
