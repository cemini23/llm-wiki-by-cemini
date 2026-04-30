---
title: "7onez/cti-expert — Cyber Threat Intelligence & OSINT Skill for Claude Code (Python, MIT + Ethical Use Addendum, 78★)"
type: source
tags: [github, claude-code-skill, osint, cyber-threat-intelligence, agentflow-dag, mit-with-ethical-addendum, family-c-adjacent, gemini-dr-wave4-osint, workflow-adopt]
keywords: [cti-expert, 7onez, hieu-ngo, cyber-threat-intelligence, osint-skill, agentflow-dag-execution, aead-methodology, acquire-enrich-assess-deliver, 67-commands, 35-techniques, maigret, sherlock, holehe, h8mail, scrapling, stix-2-1, ioc-export, lateral-pivot-expansion, ethical-use-addendum-restriction]
clusters: [llm-agents, osint, dev-tooling]
related:
  - sources/gemini-dr-wave4b-osint-2026-04-29.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
maturity: validated
read_status: read-skim
created: 2026-04-30
updated: 2026-04-30
---

## Relations

- @sources/gemini-dr-wave4b-osint-2026-04-29.md — Wave 4B URL 9 Adopt; promoted to dedicated source 2026-04-30. Strongest Wave 4B Adopt for laptop Workflow; defines the candidate `concepts/osint-event-driven-analysis.md` extension space for Cemini.
- @concepts/wiki-tooling-evaluation.md — Wave 4 evaluation parent
- @concepts/ip-sale-readiness.md — **MIT base license + Ethical Use Addendum is borderline-adjacent to Family C** (constraints attached to clean-license code that may affect deployment); not exact Family C (which is third-party-data-provider-TOS), but the pattern of "MIT-plus-restrictions" warrants scrutiny. The addendum restricts use to "legal research, corporate security investigations, and authorized testing" — Cemini's use case (corporate intelligence for ticker research) likely falls within scope, but acquirer due-diligence may need explicit confirmation.
- @concepts/high-signal-paper-patterns.md — rubric: 78 stars + 1 contributor + 67+ commands across 35+ techniques + STIX 2.1 export = "competent solo project with a defined methodology"; bus-factor caveat applies (single contributor)

## Raw Concept

- **URL**: https://github.com/7onez/cti-expert
- **Type**: Open-source Claude Code skill / Agent toolkit
- **License**: **MIT + Ethical Use Addendum**. GitHub aggregator shows: License: **Other (NOASSERTION)** because of the addendum text. README clarifies: "MIT License + Ethical Use Addendum. You are free to use, modify, and distribute this skill under the MIT license, provided that you include original attribution, comply with the ethical use guidelines above, and clearly mark any derivatives."
- **Stars / Forks (Exa-verified 2026-04-30)**: 78 ★ / 10 forks
- **Stack**: Python 83.4% / Shell 16.6%
- **Org**: 7onez (Hieu Ngo, solo author)
- **Created**: 2026-04-06; **Last push**: 2026-04-19 (active for ~13 days)
- **Topics**: claude-code, claude-code-skill, cti, cyber-threat-intelligence, digital-forensics, investigation, osint, reconnaissance, security, threat-intelligence
- **Discovered via**: Gemini DR Wave 4B 2026-04-29 (URL 9); promoted 2026-04-30
- **Read status**: read-skim (Exa-fetched README + Gemini brief)

## Narrative

### What it is

A specialized **Claude Code skill** that transforms the generic Claude LLM into a trained **cyber-threat-intelligence (CTI) and OSINT analyst**. Provides 67+ commands across 35-38 reconnaissance techniques. No API keys required for core functionality (optional: Wigle, VirusTotal, URLScan.io for enhanced access).

**Methodology**: AEAD — **Acquire / Enrich / Assess / Deliver** — the agent autonomously executes a structured intelligence pipeline.

**Architecture**: an **AgentFlow engine** does **Directed Acyclic Graph (DAG)-based execution**. Lateral pivot expansions iteratively map infrastructure: starting from a target person/domain/wallet, the agent traverses to affiliated networks. Outputs:
- Markdown dossiers (routable to Obsidian vault)
- Microsoft Word documents
- **STIX 2.1 standardized IOC exports** (Indicators of Compromise — interoperable with security platforms)
- Auto-generated network topology diagrams

Wraps third-party Python OSINT tools: **maigret** (username enumeration), **sherlock** (social media), **holehe** (email), **h8mail** (breach data), **Scrapling** (adaptive web parsing).

### Why Cemini-relevant

**Workflow Adopt for the laptop-side OSINT extension space**. Per the Gemini brief: "drastically augments the existing Claude Code and Obsidian workflow by immediately providing the agent with 67 native OSINT execution pathways. The resulting STIX 2.1 formatted IOC exports and comprehensively synthesized markdown dossiers can be routed directly into the Obsidian vault."

**Cemini-stack scope: ❌ NOT for cemini-prod**. The Gemini brief is explicit: "the architecture is fundamentally a complex wrapper designed to translate human chat intent into orchestrated CLI tool executions. The Cemini production system leverages LangGraph for deterministic, programmatic state orchestration. Attempting to retroactively adapt these interactive CLI skills into headless LangGraph nodes is incredibly inefficient."

### Future Cemini extension surface

cti-expert defines the **candidate `concepts/osint-event-driven-analysis.md`** extension space. If Cemini ever takes on event-driven OSINT (e.g., flagging cybersecurity events that affect ticker watchlists — exchange hacks, ransomware incidents on listed companies, supply-chain breaches), this skill is the natural starting point.

For now: laptop-side use during research that touches OSINT-shaped questions (e.g., investigating a fintech startup's domain for technical-due-diligence signals).

### The Ethical Use Addendum — should we worry?

The README states: "MIT License + Ethical Use Addendum. You are free to use, modify, and distribute this skill under the MIT license, provided that you include original attribution, comply with the ethical use guidelines above, and clearly mark any derivatives."

The "ethical use guidelines": **explicitly prohibits deployment for doxxing, stalking, unauthorized monitoring, or harassment**. Use is restricted to "legal research, corporate security investigations, and authorized testing."

**Cemini's use case** (corporate intelligence for ticker research) **fits within the addendum's allowed scope**, but acquirer due-diligence may want explicit legal-review confirmation. Per `@concepts/ip-sale-readiness.md` Family C framing: this is **MIT-plus-restrictions**, not strict Family C (Family C is third-party-TOS via clean-license code; this is direct restrictions in the project's own license addendum). It's borderline — call it **Family C-adjacent**: the LICENSE has constraints, but they're constraints the project itself imposes (not a third party's).

For laptop-side Workflow use: the constraints are easy to honor (we're not doing doxxing/stalking). For Cemini production deployment: would require an acquirer-friendly explicit-scope statement that Cemini's use stays within the addendum's allowed categories.

### Risks & open questions

1. **Dependency sprawl** — 30+ third-party Python OSINT tools (maigret, sherlock, holehe, h8mail, etc.). Each is independently maintained; any one breaking causes a cti-expert command to fail (potentially silently, leaving incomplete intelligence profiles).
2. **DOM/anti-bot drift** — most underlying tools scrape against platform DOMs that frequently change. Per Gemini brief: "If a target platform updates its DOM structure or authentication flow, the underlying tool will break." Pre-adoption: install + run the full smoke test before relying on the skill in time-sensitive research.
3. **Scrapling Cloudflare bypass** [NEEDS VERIFICATION 2026-04-30] — per Gemini brief, the Scrapling implementation needs review for "modern capabilities necessary to bypass advanced Cloudflare or equivalent anti-bot protections, as raw web scraping without proxy rotation has become notoriously fragile."
4. **Ethical Use Addendum at acquirer DD** — if Cemini is ever sold, the acquirer's IP team will see this addendum on a clone of the skill. Cemini should pre-write a position-paper documenting the Cemini-internal-use scope alignment with the addendum's allowed categories.
5. **Vietnamese localization in README** — the README has substantial Vietnamese-language sections. Useful to know for due-diligence transparency; doesn't change adoption decision but worth noting.
6. **Bus-factor** — solo author "Hieu Ngo"; if abandoned, fork-and-maintain pattern.

### Cemini-side adoption assessment

**Decision: Adopt for laptop Workflow** — gates the future Cemini extension to event-driven OSINT analysis. Concrete next-steps:

1. License audit ✅ done (MIT + Ethical Use Addendum; verified)
2. **Install on the laptop**: `~/.claude/skills/cti-expert/` per Gemini's recommended path. ~10 min
3. **Smoke-test the underlying tool dependencies** (maigret, sherlock, holehe, etc.) — install all required deps; run a small test investigation against a known target (e.g., self-investigation of own domain). ~30 min
4. **Document the addendum alignment** — write `wiki/concepts/osint-event-driven-analysis.md` (eventually) with explicit framing: Cemini's use is "corporate security investigations and authorized testing" per the addendum's allowed scope.
5. **Use during ad-hoc research** — when ticker research touches questions that benefit from OSINT (domain investigations, founder background, infrastructure analysis), invoke cti-expert. Outputs route into Obsidian vault as Markdown dossiers.

### Citation

> Ngo, H. (7onez). (2026). *CTI Expert — Cyber Threat Intelligence & OSINT Analysis Skill for Claude Code*. https://github.com/7onez/cti-expert (MIT License + Ethical Use Addendum; v2.2/v2.3; 78 stars; created 2026-04-06)

## Snippets

> **Mission framing (from README)**:
>
> "Transform Claude into a trained intelligence analyst — 67+ commands, 38 techniques, zero API keys required for core functionality. A Claude Code skill that transforms Claude into a trained cyber threat intelligence and open-source intelligence analyst." [Source: https://github.com/7onez/cti-expert README, retrieved 2026-04-30 via Exa]

> **License + Ethical Use Addendum (from README)**:
>
> "MIT License + Ethical Use Addendum. You are free to use, modify, and distribute this skill under the MIT license, provided that you include original attribution, comply with the ethical use guidelines above, and clearly mark any derivatives. See LICENSE for full text." [Source: https://github.com/7onez/cti-expert README, retrieved 2026-04-30 via Exa]

> **Methodology framing (per Gemini DR brief Wave 4B URL 9)**:
>
> "It effectively transforms the generalized Claude LLM into a highly trained intelligence analyst capable of autonomously executing a rigorous 'AEAD' (Acquire, Enrich, Assess, Deliver) methodology. The framework acts as an orchestration layer, seamlessly integrating a multitude of third-party Python OSINT tools (including maigret, sherlock, holehe, and the Scrapling library for adaptive web parsing) alongside standard Unix networking utilities. Utilizing its internal AgentFlow engine, the agent can perform parallel pivot expansions—iteratively mapping infrastructure by moving laterally from a target person, domain, or cryptocurrency wallet to affiliated networks." [Source: another Link Evaluation for Trading and Wiki Stacks 4_29.docx URL 9 evaluation]
