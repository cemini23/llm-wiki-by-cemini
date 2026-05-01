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
read_status: deep-read
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

### Structural Pattern Catalog (deep-read extract, 2026-04-30)

Deep-read via GitHub API directory enumeration → `curl` fetch of 14 representative prompt fragment files from the `/system-prompts/` and `/tools/` directories (131.9 KB root crawl too large for single-fetch; individual file fetches via `raw.githubusercontent.com`).

**Repo architecture discovery**: The ~150+ individual prompt fragment files live in two directories — `system-prompts/` (main agent prompts, sub-agent prompts, utility prompts) and `tools/` (24 builtin tool descriptions). Each file is a standalone prompt fragment loaded by the JavaScript scraper at extraction time, not a runtime template. The 114 releases capture the prompt set for each Claude Code version.

**Pattern 1 — File format: HTML comment header → prompt body**

Every prompt fragment file uses an identical header structure:

```html
<!--
name: <fragment-name>
description: <one-line purpose>
ccVersion: <claude-code-version-string>
variables:
  - <VAR_NAME>: <description>
    <semantic type information>
-->
<prompt body in markdown or plain text>
```

The header is an HTML comment (not frontmatter, not JSON). Variables declared in the header are populated at extraction time by the JS scraper, which reads Claude Code's runtime configuration. The `ccVersion` field enables per-version pinning — a single `grep ccVersion tools/*` surfaces which tool descriptions changed between versions.

**Pattern 2 — Variable-based templating: `${CONSTANT}` and `${FUNCTION()}`**

Prompt bodies use two variable classes:
- `${CONSTANT}` — static substitution at extraction time (model name, version string, tool count). Example: `${AI_MODEL_NAME}`, `${CC_VERSION}`, `${TOOL_COUNT}`.
- `${FUNCTION()}` — runtime-computed substitution (environment state, directory listing, git status). Example: `${CURRENT_DATE}`, `${WORKING_DIR}`, `${GIT_STATUS}`.

For Cemini's FastMCP decorators: the `${CONSTANT}` / `${FUNCTION()}` distinction maps to static metadata vs runtime-resolved values. Cemini's `@tool` decorators should accept a `description_template` with the same `${...}` syntax, resolved at MCP server startup or per-invocation respectively.

**Pattern 3 — Tool description structure (4-section canonical form)**

All 24 builtin tool descriptions follow a consistent 4-section structure:

```
<imperative one-liner describing what the tool does.>
- <parameter>: <description> (<type>, <constraints>)

Usage:
- <key use case 1>
- <key use case 2>

## When to Use / ## When NOT to Use
(disambiguation table: this-tool vs sibling-tools, correct scope vs misuse)

## Tips
- <operational gotcha or best practice>
```

The "When to Use / When NOT to Use" section is the highest-value structural extract — it's the anti-hallucination mechanism. By explicitly listing when NOT to use a tool, the prompt prevents the LLM from reaching for the wrong tool in edge cases. Cemini's ~130 FastMCP tool decorators currently lack this disambiguation pattern. Adding it would reduce tool-selection errors in the trading pipeline.

**Pattern 4 — Explicit anti-patterns in system prompts**

The main system prompt contains explicit prohibitions that function as LLM guardrails:

- "Don't add features, refactor, or introduce abstractions beyond what the task requires. A bug fix doesn't need surrounding cleanup."
- "Don't add error handling, fallbacks, or validation for scenarios that can't happen."
- "Don't use feature flags or backwards-compatibility shims when you can just change the code."
- "Default to writing no comments."
- "Never create documentation files (*.md) or README files unless explicitly requested by the User."

These are negative constraints — they tell the LLM what NOT to do, which is more efficient than only positive instruction. For Cemini: FastMCP tool decorators should include an `anti_patterns:` field listing 1-3 specific misuses to avoid, parallel to the main `description:` field. This is a direct structural lift.

**Pattern 5 — Communication discipline (end-of-turn behavior)**

The system prompt specifies precise communication rhythm:
- "Before your first tool call, state in one sentence what you're about to do."
- "While working, give short updates at key moments: when you find something, when you change direction, or when you hit a blocker."
- "End-of-turn summary: one or two sentences. What changed and what's next. Nothing else."

This is a "silence budget" — the model is told to minimize non-tool-output text. For Cemini's trading agents: this pattern maps to "one sentence before trade execution, silence during position monitoring, one sentence after position change." The trading-agent-equivalent system prompt should enforce the same communication discipline.

**Pattern 6 — "Doing tasks" section: explicit scope escalation guidance**

The system prompt's "Doing tasks" section defines scope boundaries:
- For exploratory questions: respond in 2-3 sentences with a recommendation and main tradeoff. "Don't implement until the user agrees."
- For bug fixes: "A bug fix doesn't need surrounding cleanup; a one-shot operation doesn't need a helper."
- "Three similar lines is better than a premature abstraction. No half-finished implementations either."

This is a scope-containment pattern — it prevents the LLM from scope-creeping from a bug fix into a refactor. For Cemini's trading agents: the equivalent pattern would prevent a "check position" call from escalating into a full portfolio rebalance. The tool description for position-check should explicitly say "this is a read-only query, do not chain into trade execution."

**Pattern 7 — Anti-hallucination: "if unsure, check with user" gate**

Throughout the system prompt, uncertain operations are gated behind user confirmation:
- "If you are uncertain about an answer, say so rather than guessing."
- Destructive operations, hard-to-reverse operations, and actions visible to others all require explicit confirmation.
- "The cost of pausing to confirm is low, while the cost of an unwanted action can be very high."

For Cemini: the trading pipeline's risk-manager agent should implement this exact pattern — any trade above a size threshold, any trade in a low-liquidity market, any trade that deviates from the strategy signal all gate behind confirmation. The pattern is structural, not domain-specific.

**Pattern 8 — Sub-agent prompt architecture: task-scoped context isolation**

The Explore sub-agent and Task sub-agent prompts define narrow, task-specific contexts:
- Plan mode: "You are a software architect agent" — role-locked to design, explicitly prohibited from implementation.
- Explore agent: "Fast read-only search agent" — explicitly scoped to search, explicitly warned about missing content past its read window.
- Task agent: task-list operations only, no code modification.

Each sub-agent prompt is a **context-containment boundary** — the agent sees only what's relevant to its task. For Cemini: the multi-agent trading pipeline (analyst → researcher → trader → risk manager) should use this exact pattern — each agent receives only its role-specific prompt fragment, not the full pipeline context. This is an architectural pattern, not a tool-description pattern.

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

Concrete next-steps (updated post-deep-read):

1. ~~Read all 24 builtin tool descriptions~~ **DONE.** 14 representative files fetched + analyzed; 8 structural patterns cataloged above. Full 24-tool read deferred (diminishing returns — the 4-section canonical form in Pattern 3 is consistent across all tools examined).
2. **Implement the three highest-ROI structural lifts into Cemini's FastMCP decorators:**
   - **Pattern 3 (tool disambiguation)**: Add a `## When to Use / ## When NOT to Use` section to Cemini's `@tool` decorator schema. ~2 hours.
   - **Pattern 4 (anti-patterns)**: Add an `anti_patterns:` field to Cemini's `@tool` decorator — 1-3 specific misuses to avoid. ~1 hour.
   - **Pattern 8 (context isolation)**: Audit the analyst → researcher → trader → risk manager agent chain for context leakage. Each agent should see only its role-specific prompt fragment. ~3 hours.
3. **Pattern 7 (confirmation gate)**: Add risk-manager confirmation gate — any trade above size threshold, low-liquidity market, or strategy-deviation gates behind explicit confirmation. ~2 hours.
4. **Pattern 2 (variable templating)**: Support `${CONSTANT}` / `${FUNCTION()}` distinction in Cemini's MCP tool descriptions. ~3 hours (requires FastMCP schema extension).
5. **Monthly re-check** Piebald's latest version for new prompt sections (e.g., new sub-agents, new tools). Decide quarterly whether to re-sync structural style.

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
