---
title: "Packt SecPro — The Chase outage and the trust we place in AI (2026-11-20)"
type: source
maturity: draft
related:
  - concepts/defensive-ai-trust-calibration.md
  - concepts/soc-operations.md
  - concepts/incident-response.md
  - concepts/agentic-containment-principles.md
  - concepts/patchless-window.md
updated: 2026-11-22
read_status: read
---

## Raw Concept

- **Title:** The Chase outage and the trust we're placing in AI
- **Author:** Packt SecPro
- **Type:** Newsletter (Substack, free tier)
- **Location:** `research to be indexed/substack-rss-secpro-2026-11-20-the-chase-outage-and-the-trust-were-placing-in-a.md`
- **URL:** https://secpro.substack.com/p/the-chase-outage-and-the-trust-were
- **Retrieved:** 2026-11-20
- **Read status:** read — full text 2026-11-22

## Narrative

On Monday 16 November, JPMorgan Chase attributed transaction delays to a software bug in its on-premises hardware systems. The bank reported no evidence of a cyberattack. The next day, The Washington Sun reported that bank executives and the NSA told lawmakers that urgent patching of AI-discovered vulnerabilities contributed to that week's outages. That account rests on sources describing private conversations, and it does not establish causation. `[TENTATIVE]` `[NEEDS VERIFICATION 2026-11-22]` against the Chase post-incident report.

The article's value is the trust argument that follows. A failure inside a bank can interrupt services beyond the bank. Giving an agent more authority over such infrastructure is a decision about other people's services.

Evidence both ways. Google Threat Intelligence Group and Mandiant reported agentic tools in live intrusions, plus automated conversion of disclosed vulnerabilities into exploits, plus AI-generated exploits that fail. `[TENTATIVE]` In DARPA's 2025 AI Cyber Challenge finals, competitor systems found 54 introduced vulnerabilities and patched 43. 1Password found that LLM-generated patches for six complex vulnerabilities addressed only some paths, introduced new weaknesses, or changed legitimate behaviour.

The oversight problem is the core. Anthropic reported that users approved roughly 93% of permission prompts and described approval fatigue. In an Anthropic study, 50 professional analysts used an agent with secretly assigned preferences and followed the agent's preference 86% of the time across four analytical decisions. That study used a statistical task, not security decisions, and both options were defensible. But it shows that a human approval step does not guarantee independent judgment.

The NCSC interim advice on agentic AI warns that built-in safeguards can be bypassed. It recommends human oversight plus technically enforced controls for higher-risk use, and independent evaluation of any AI judge.

Survey numbers: in a July 1Password-commissioned survey of 1,000 US employees, 46% of developers reported agents in production, 40% gave agents persistent access to systems or credentials, and 62% reported gaps in agent management. Self-reported and vendor-sponsored.

Conclusion: bounded use of defensive AI is reasonable today. Trusting it to decide that an organization is secure, that an incident is contained, or that a change is safe needs evidence beyond the system's own assurance.

[Source: substack-rss-secpro-2026-11-20-the-chase-outage-and-the-trust-were-placing-in-a.md]

## Snippets

> "Users approved roughly 93% of permission prompts and described the problem of approval fatigue."
[Source: SecPro 2026-11-20, citing Anthropic]

> "Across four analytical decisions, the participants followed the agent's preference 86% of the time."
[Source: SecPro 2026-11-20, citing an Anthropic study]
