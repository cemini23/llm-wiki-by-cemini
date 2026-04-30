---
title: "Piebald-AI/claude-code-system-prompts — Claude Code Internal System Prompts + 24 Builtin Tool Descriptions, Tracked Per-Version (MIT, JS, 9.7k★)"
type: source
tags: [github, claude-code, system-prompts, tool-descriptions, prompt-engineering, mit-license, gemini-dr-wave5b, steal-from-tier, fastmcp-tool-schemas, anthropic, prompt-extraction-pattern]
keywords: [claude-code-system-prompts, piebald-ai, 24-builtin-tools, plan-mode-prompt, explore-subagent, task-subagent, claude-md-utility-prompt, compact-prompt, statusline-prompt, magic-docs-prompt, webfetch-prompt, bash-cmd-prompt, security-review-prompt, agent-creation-prompt, per-version-tracking, claude-code-v2-1-123, fastmcp-tool-decorators, deepseek-v4-pro-think-xml-adherence, prompt-extraction-pattern]
clusters: [librarian-tooling, llm-agents, dev-tooling]
related:
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
  - sources/upstash-context7.md
  - sources/agentic-harness-engineering.md
  - sources/llms-corrupt-documents-laban-2026.md
  - concepts/llm-agent-systems.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - entities/infrastructure/deepseek-api.md
  - entities/frameworks/fastmcp.md
  - concepts/high-signal-paper-patterns.md
maturity: validated
read_status: read-skim
created: 2026-04-30
updated: 2026-04-30
---

## Relations

- @sources/gemini-dr-wave5b-osint-2026-04-30.md — Wave 5B canonical brief; URL 6 of the 18-URL evaluation; promoted to dedicated page from Steal-from verdict (highest star count of the wave at 9.7k)
- @sources/upstash-context7.md — Wave 4A Adopt sibling: context7 = "what does the API surface look like *now*" (external library docs); claude-code-system-prompts = "what does Claude Code's *internal* prompt look like *now*" (per-Claude-Code-version). Both target hallucination-prevention via grounding.
- @sources/agentic-harness-engineering.md — operationally paired: agentic-harness measures the prompt-engineering surface area for tool-using agents; this repo provides Claude Code's actual system-prompt content as ground truth for that surface area.
- @sources/llms-corrupt-documents-laban-2026.md — operationally paired: LLMs corrupt documents partly via prompt-misalignment; well-structured tool descriptions (extracted here) reduce input-side ambiguity that drives output-side corruption.
- @concepts/llm-agent-systems.md — cluster hub; the prompt-extraction-pattern is a content-vs-runtime distinction that complements the architectural patterns the hub indexes.
- @concepts/wiki-tooling-evaluation.md — adoption decision parent; Steal-from verdict with **prompt-extraction-pattern** as the crystallizing theme.
- @concepts/ip-sale-readiness.md — MIT root is clean. **But**: the underlying prompt text is Anthropic's intellectual property; the MIT license covers the JavaScript scraper, NOT the scraped content. Pre-adoption gate is legal review of "is incorporating Anthropic's prompt structures into Cemini's FastMCP tool schemas a derivative-work / TOS-conflict?" — likely fine for "structural inspiration" but not for "verbatim copy".
- @entities/infrastructure/deepseek-api.md — Cemini's brain. **Pre-adoption gate**: confirm DeepSeek-V4-Pro-Think strict adherence to heavy-XML-tagging structures (Claude-specific) before committing extracted schemas.
- @entities/frameworks/fastmcp.md — Cemini's ~130 custom FastMCP tool decorators are the Steal-from target — lift the Claude-Code prompt schemas, structurally adapt to FastMCP, gain consistency.

## Raw Concept

- **Original title**: "All parts of Claude Code's system prompt, 24 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact, statusline, magic docs, WebFetch, Bash cmd, security review, agent creation). Updated for each Claude Code version."
- **Author**: Piebald-AI organization (top contributors: mike1858, bl-ue, signadou, ddaanet — 4 total)
- **Repository**: https://github.com/Piebald-AI/claude-code-system-prompts
- **License**: MIT (file-level + repo-level confirmed via Exa `crawling_exa` 2026-04-30)
- **Primary language**: JavaScript (extraction-only)
- **Stars**: 9,684 (as of 2026-04-30) — strongest star signal of Wave 5B
- **Forks**: 1,722
- **Contributors**: 4
- **Created**: 2025-11-18
- **Last push**: 2026-04-29 (literal day-before-evaluation)
- **Releases**: **114** — one per Claude Code version
- **Latest release**: v2.1.123 (2026-04-29)
- **Topics**: claude-code, claude-code-system-prompts, system-prompts
- **Read status**: read-skim (README + license + repo metadata + release-cadence-tracking via `crawling_exa`; specific prompt-content read pending pre-extraction commit)
- **Discovered via**: User Wave 5B Gemini DR brief (2026-04-30)
- **Primary cluster**: librarian-tooling

## Narrative

### What it is

Piebald-AI's claude-code-system-prompts is a systematic extraction repository — a JavaScript scraper that pulls the internal system prompts, tool descriptions, sub-agent prompts, and utility prompts directly out of Anthropic's Claude Code CLI and version-tracks them as committed files in the repo. **Re-released per Claude Code version** (114 releases through v2.1.123 at evaluation date).

**What's inside**:

1. **24 builtin tool descriptions** — exact prompt schema for each of Claude Code's tools (Read, Write, Edit, Bash, Glob, Grep, etc.) including parameter descriptions, examples, when-to-use guidance.
2. **Sub-agent prompts** — Plan mode (715 tokens per docx), Explore subagent, Task subagent.
3. **Utility prompts** — CLAUDE.md handling, compact (context compression), statusline, magic docs, WebFetch, Bash cmd composition, security review, agent creation.
4. **Versioned** — each Claude Code release gets its own tagged commit, so historical prompt evolution is visible.

The JavaScript runtime that does the extraction is **irrelevant** — the value is the **prompt content** itself. This is a textbook **prompt-extraction-pattern** Steal-from candidate.

### Why this matters for Cemini

**Workflow — ✅ Yes-fit (high value)**:
- Cemini uses Claude Code for the laptop-side research workflow. Understanding Claude Code's internal system prompts directly improves how the solo developer crafts CLAUDE.md and skill instructions — knowing what assumptions Claude Code is already making lets the developer avoid redundant or contradictory directives.
- Plan mode's 715-token prompt is itself a study object — what does Anthropic consider essential planning context? That informs Cemini's own prompt-engineering decisions for non-Claude-Code agents.

**Cemini production stack — ✅ Steal-from**:
- Cemini exposes ~130 custom FastMCP tool decorators to its DeepSeek-V4-Flash brain. **The 24 builtin tool descriptions in this repo are reference schemas** — formatting syntax, parameter description style, when-to-use guidance. Lift the structural patterns, adapt to FastMCP, gain consistency with what an LLM is already trained to handle well.
- This is structural inspiration, not verbatim copy. Anthropic's prompt content is Anthropic's IP. The Steal-from is the *style* and *structure*, not the literal text.

**Wiki / Librarian server — ❌ No-fit**:
- CPX21 is markdown compilation + semantic search. Anthropic-CLI prompts have no role on it.

### Cross-paper / cross-tool synthesis

- **Pair with `@sources/upstash-context7.md`** (Wave 4A Adopt): context7 reduces *external-library* hallucination via grounded docs; this repo reduces *internal-tool* hallucination via grounded tool schemas. Together: agent's both inside-knowledge (own tools) and outside-knowledge (libraries) are grounded.
- **Pair with system_prompts_leaks** (Wave 5B URL 7 Reference-only, not promoted to dedicated page): Piebald is **narrower + version-tracked + Anthropic-only**; system_prompts_leaks is **broader + crowdsourced + cross-vendor**. Use Piebald for production-relevant Claude Code work; consult system_prompts_leaks via the Wave 5B brief for cross-vendor architectural inspiration.
- **Pair with `@sources/agentic-harness-engineering.md`**: AHE measures the harness surface area; this repo provides the actual Claude Code harness content as a comparison baseline.

### The prompt-extraction-pattern (the crystallizing theme)

Wave 5B surfaced this as a **content-vs-runtime distinction**:
- **The runtime** (JavaScript scraper) is uninteresting — anyone could write it.
- **The content** (extracted prompt text + tool descriptions + structures) is the high-value extract.

Mirrors the Wave 5A "**Steal-from-the-tokenizer-not-the-model**" pattern (Kronos): the *upstream* component (tokenization architecture for Kronos; prompt schemas here) is what's worth keeping. The *downstream* runtime (Kronos predictor disclaimed by authors; this repo's JS scraper) is irrelevant.

This pattern generalizes: **when evaluating a Steal-from candidate, separate "the thing the project produces" from "the code that produces it" — the produced artifact is usually the value**.

### Risks & open questions

1. **Extreme upstream volatility**. Claude Code is in beta with rapid iteration. v2.1.124 today is v2.1.130 next month. **Mitigation**: pin to a specific Claude Code version's prompts (e.g., v2.1.123 today) when extracting schemas. Re-sync when Cemini is willing to invest in re-validation.

2. **Anthropic IP boundary** [NEEDS VERIFICATION 2026-04-30] — the JavaScript scraper is MIT but the **scraped prompt content is Anthropic's IP**. Verbatim incorporation into Cemini's FastMCP tool schemas may constitute unauthorized derivative work or TOS violation. **Steal-from = structural inspiration only**, not verbatim copy. Pre-adoption legal review.

3. **DeepSeek-V4-Pro-Think XML adherence** [NEEDS VERIFICATION 2026-04-30] — Claude Code's prompts use heavy XML-style tagging (`<thinking>`, `<plan>`, `<tool_use>`, etc.) that's Claude-architecture-specific. Confirm DeepSeek-V4-Pro-Think correctly parses + adheres to the same patterns before committing schemas. If DeepSeek doesn't, the structural inspiration needs translation.

4. **No semver discipline** — Piebald's 114 releases follow Claude Code's versioning (which is also non-semver in practice). Pinning to a specific version requires accepting that "v2.1.123" doesn't have stability semantics.

5. **`security review` and `agent creation` prompts** are particularly interesting for Cemini — both are operational tasks Cemini's own pipeline may eventually want LLM assistance with. Worth specific attention during the deeper read.

### Cemini-side adoption assessment

**Decision**: **Steal-from for structural inspiration. Do not commit verbatim Anthropic prompt text into Cemini's codebase.**

Concrete next-steps:

1. **Read all 24 builtin tool descriptions** from a recent pinned version (e.g., v2.1.123). Catalog the structural patterns (parameter description style, when-to-use guidance, example formatting). ~3-4 hours.
2. **Audit Cemini's ~130 FastMCP tool decorators** for inconsistencies vs the structural patterns identified. ~2 hours.
3. **Refactor 5-10 highest-value FastMCP decorators** using the patterns as Cemini-bespoke style guide (rephrased, not copied). Validate that DeepSeek-V4-Pro-Think parses them correctly. ~1 day.
4. **If validation succeeds**: roll out the structural style to all decorators incrementally over the next quarter. ~ongoing.
5. **Monthly re-check** Piebald's latest version for new prompt sections (e.g., new sub-agents, new tools). Decide quarterly whether to re-sync structural style against the latest patterns.

License + IP-sale-readiness disposition: **structural inspiration is acceptable**; **verbatim copy of Anthropic prompts is not**. Legal review on the boundary is a one-time pre-adoption gate.

### Citation

> Piebald-AI. (2025). *claude-code-system-prompts — All parts of Claude Code's system prompt, tool descriptions, sub agent prompts, utility prompts. Updated for each Claude Code version*. v2.1.123. GitHub. https://github.com/Piebald-AI/claude-code-system-prompts (License: MIT [code]; underlying prompt content is Anthropic IP; retrieved 2026-04-30 via Exa `crawling_exa`)

## Snippets

> **The repo's identity statement**:
>
> "All parts of Claude Code's system prompt, 24 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact, statusline, magic docs, WebFetch, Bash cmd, security review, agent creation). Updated for each Claude Code version." [Source: github.com/Piebald-AI/claude-code-system-prompts repo description, retrieved 2026-04-30]

> **Wave 5B Steal-from rationale (URL 6 evaluation excerpt)**:
>
> "Steal-from. The JavaScript runtime architecture utilized to extract the prompts is irrelevant for deployment. However, the prompt structures themselves are invaluable. The highly optimized schemas, formatting syntax, and parameter descriptions for the 24 builtin tools must be directly lifted, structurally adapted, and integrated into Cemini's ~130 custom FastMCP tool decorators." [Source: another Evaluating Code for Trading & Wiki Stacks 4_30.docx URL 6]

> **Wave 5B risk caveat — upstream volatility (URL 6 evaluation excerpt)**:
>
> "A primary risk associated with relying on this repository is extreme upstream volatility. Claude Code operates in a beta state characterized by rapid, frequent development cycles. The specific prompt strings and logic flows scraped today (v2.1.124) will likely drift significantly or become entirely obsolete within weeks." [Source: another Evaluating Code for Trading & Wiki Stacks 4_30.docx URL 6]

> **Wave 5B integration vector for Cemini (URL 6 evaluation excerpt)**:
>
> "In evaluating the Workflow application, the concrete integration vector is profound. The prompts systematically extracted in this repository fundamentally dictate the behavior and boundaries of Claude Code. By rigorously studying the internal instructions for Plan mode (measuring 715 tokens) and the embedded Explore/Task sub-agent definitions, the solo developer gains complete operational understanding of the LLM-agent collaborator on the laptop." [Source: another Evaluating Code for Trading & Wiki Stacks 4_30.docx URL 6]
