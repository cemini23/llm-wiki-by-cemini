---
title: OpenClaw security taxonomy
type: concept
tags: [concept, security, agent-framework, taxonomy, kill-chain, execution-safety, architectural-primitive]
keywords: [openclaw, security taxonomy, two-axis taxonomy, context manipulation, kill chain, exec allowlist bypass, prompt injection, supply chain, provenance model, inter-layer enforcement, closed-world assumption, lexical-vs-semantic]
related:
  - sources/ai-2-4-3.md
  - concepts/sae-execution-contract.md
  - concepts/cryptographic-audit-trail.md
  - concepts/llm-agent-systems.md
  - concepts/scatter-gather-topology.md
  - sources/crypto-7-4-11.md
  - sources/3-17-agent-research.md
  - sources/3-25-git-research.md
  - sources/git-3-5-pt3.md
  - sources/3-29-15.md
  - concepts/reasoning-safety-monitor.md
  - concepts/agent-authorization-stack.md
  - sources/safeharness-2604.13630.md
  - concepts/mitre-atlas-taxonomy.md
  - entities/tools/hermes-agent.md
  - entities/tools/claw-swe-bench.md
  - concepts/claw-swe-bench-harness-evaluation.md
  - sources/arxiv-claw-swe-bench-2606.12344-2026-06-16.md
  - sources/arxiv-aohp-os-agent-harness-2606.23449-2026-06-23.md
  - sources/huggingface-model-evals-74url-2026-06-23.md
  - concepts/aohp-os-level-agent-harness.md
maturity: validated
created: 2026-05-01
updated: 2026-06-23
---

## Relations

- @entities/tools/claw-swe-bench.md — K119 MIT harness benchmark on OpenClaw-style tasks
- @sources/ai-2-4-3.md — canonical source: Suwansathit, SUCCESS Lab, Texas A&M, arXiv:2603.27517v1, February 2026
- @concepts/sae-execution-contract.md — SAE is the defense counterpart; this taxonomy catalogs the threat model SAE's six mitigations address
- @concepts/cryptographic-audit-trail.md — K20's provenance model + Gateway RCE chain as audit-trail detection targets
- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research
- @concepts/scatter-gather-topology.md — §6.7 unified inter-layer enforcement composes with scatter-gather's execution-leaf placement
- @sources/crypto-7-4-11.md — K19 SAE paper: "here's the defense"; K20 = "here's what it defends against"
- @sources/3-17-agent-research.md — K16 sandboxed observer shares the closed-world-assumption critique
- @sources/3-25-git-research.md — K17 debate-cycle decision anchoring; provenance model complements debate with origin-level trust
- @sources/git-3-5-pt3.md — K18 ToxicSkills threat vector directly instanced by yahoofinance malicious skill
- @sources/3-29-15.md — K22 deep-read 2026-05-01; reasoning safety monitor provides the detection layer that catches Context Manipulation as it unfolds in the CoT — closes K20 §6.6's context-window provenance gap
- @concepts/reasoning-safety-monitor.md — K22 promotion; reusable architectural primitive for parallel CoT inspection — nine-category taxonomy + interrupt signal before corrupted reasoning reaches execution
- @concepts/agent-authorization-stack.md — K19+K22+K23+K24 cross-cluster synthesis; threat model that informs all four authorization layers.
- @sources/safeharness-2604.13630.md — K25 SafeHarness lifecycle-integrated harness security; defends against the threat surface K20 catalogs at the harness-internal level.
- @entities/tools/hermes-agent.md — K52 Nous Research Hermes Agent, positioned as OpenClaw's successor; this taxonomy is the comparison frame for its security posture

## Raw Concept

The question this page answers: **What is the structured threat model for AI agent frameworks that connect LLM reasoning to host execution surfaces, and what reusable architectural insights does the OpenClaw vulnerability corpus provide?**

Synthesized from @sources/ai-2-4-3.md (K20 deep-read, 2026-05-01). The OpenClaw security taxonomy is a reusable architectural primitive for reasoning about agent-framework security — a two-axis classification system (architectural layer × attack technique) plus a novel kill-chain stage ("Context Manipulation") and three structural root causes that generalize beyond OpenClaw to any LLM-agent framework with host execution privileges.

## Narrative

**[K20 PROMOTION — 2026-05-01]** The OpenClaw security taxonomy, derived from 190 advisories against the OpenClaw AI agent framework (200K+ GitHub stars), provides the most comprehensive structured threat model available for agent frameworks where LLM reasoning connects to host execution surfaces. Its architectural insights are reusable: the two-axis taxonomy, the Context Manipulation kill-chain stage, and the three structural conditions apply to any framework where an LLM can invoke shell commands, filesystem operations, browser automation, or containerized execution.

### Two-axis taxonomy

**System axis** — 10 architectural layers, ordered from external-facing to internal:

| # | Layer | Advisory count | Dominant technique |
|---|---|---|---|
| 1 | Channel Input Interface | 35 | Allowlist bypass (mutable identity fields) |
| 2 | Plugin & Skill System | 12 | Supply-chain execution (context-window dropper) |
| 3 | Agent Context Window | 4 | Indirect prompt injection |
| 4 | Gateway WebSocket Interface | 18 | SSRF → token exfiltration → RCE chain |
| 5 | Tool Dispatch Interface | 57 | Path traversal + sandbox escape |
| 6 | Exec Policy Engine | 46 | Lexical allowlist bypass (3 variants) |
| 7 | Container Boundary / Host OS | 8 | Docker bind-mount escape |
| 8 | LLM Provider Interface | 3 | Prompt injection + inter-session contamination |
| 9 | Inter-Agent Communication | 3 | Trust-boundary collapse (agent = user) |
| 10 | Knowledge & Memory Store | 4 | Persistent context poisoning |

**Attack axis** — 7 techniques: Allowlist Bypass (37), Injection (28), Privilege Escalation (22), Authorization Bypass (19), Information Disclosure (16), Resource Exhaustion (12), Configuration Manipulation (8). 48 advisories are hybrid (span ≥2 techniques).

Key insight: allowlist bypass dominates (37 of 190, 19.5%) not because allowlists are inherently weak but because every subsystem implemented its own allowlist independently, each with different identity models — none of which survived adversarial mutation.

### OpenClaw Kill Chain — 6 stages

1. **Initial Access** — attacker establishes presence via channel message, plugin installation, or WebSocket connection
2. **Context Manipulation** (NOVEL — no MITRE ATT&CK analog) — attacker-controlled data enters the LLM context window and is processed as instruction rather than data. Traditional kill chains model data as passive (something to exfiltrate or encrypt); in agent frameworks, data is active — it can persuade, redirect, and reprogram.
3. **Execution** — the model, acting on manipulated context, invokes tools or emits commands
4. **Credential Access** — tokens, API keys, session secrets extracted from memory, logs, or environment
5. **Privilege Escalation** — exec allowlist manipulation, sandbox escape, cross-session trust collapse
6. **Impact** — host code execution, data exfiltration, persistent backdoor installation

The Context Manipulation stage is the architectural insight with the broadest applicability. It formalizes what makes LLM-agent security structurally different from conventional application security: the attack surface includes the model's reasoning process itself, not just the code paths that execute its outputs.

### Three bypass classes (relative to the reasoning layer)

K20's §5.8.3 identifies a three-tier model of how attacks relate to the LLM reasoning layer:

| Class | Position | Mechanism | Example |
|---|---|---|---|
| **Exec-policy bypass** | Below reasoning layer | Circumvents enforcement of permitted system calls | Line-continuation, busybox multiplexer, GNU abbreviation |
| **Skill-level escalation** | Beside reasoning layer | Registers malicious capabilities before policy is applied | yahoofinance dropper |
| **Prompt injection** | Above reasoning layer | Manipulates intent before any policy enforcement is reached | Slack metadata, Sentry headers, inter-session contamination |

A model successfully prompt-injected may voluntarily invoke a tool policy would otherwise have denied — rendering the policy irrelevant without ever triggering it. This is the fundamental asymmetry: defenses must be correct everywhere; attacks need only one path to the context window.

### Three structural conditions (§7)

These are the paper's most generalizable findings — architectural anti-patterns that apply to any agent framework with host execution privileges:

**1. Pervasive closed-world assumption.** Each subsystem was implemented as though inputs originated from a cooperative, finite, trusted set of sources. The exec allowlist assumed commands were enumerable via lexical parsing. Channel allowlists assumed identity fields were immutable. Context assembly assumed strings are information, not instruction. Defensible in closed systems; invalid in any open-world deployment.

**2. Absence of unified inter-layer policy enforcement.** Trust decisions are made locally (per call site, per subsystem, per handler) without a global invariant enforced across component boundaries. The Gateway RCE chain is the existence proof: three independently moderate-severity advisories (SSRF, token leak, exec-approval bypass) composed into unauthenticated RCE because no enforcement point observed the full call path from LLM tool invocation to Node-Host shell execution.

**3. Plugin/skill distribution as ungoverned execution surface.** The yahoofinance malicious skill did not exploit a memory-safety bug or parsing flaw. It operated entirely within the LLM context window, evading the entire exec policy pipeline. The runtime provides no dedicated policy primitive for the distribution channel — content review, cryptographic signing, and context-window provenance annotations are all distribution-layer controls the runtime itself doesn't enforce.

### Lexical model vs. semantic reality

The three exec allowlist bypasses share a root cause with broad applicability to any system that gates shell execution via string matching:

- **Line-continuation**: `\n` in double-quoted strings triggers POSIX line continuation, concatenating token fragments the parser sees as separate
- **Multiplexer dispatch**: `busybox sh -c '<cmd>'` changes effective executable identity; the allowlist sees `busybox`, the shell executes `<cmd>`
- **Option abbreviation**: GNU getopt accepts unambiguous prefixes (`--compress-prog` = `--compress-program`); exact-set-membership deny-lists miss abbreviated variants

The unifying principle: a command string's security-relevant identity cannot be determined by lexically parsing its text. The allowlist must reason about how the shell will interpret the string at runtime — what executable will actually be invoked, what flags will actually be active. This is the same insight that motivates SAE's projection-based enforcement (M3): don't parse intent from text; enforce constraints on the executable action.

### Cemini mapping

The OpenClaw taxonomy provides the threat model that Cemini's execution-security architecture must address. The mapping onto existing Cemini primitives:

| K20 structural condition | Cemini primitive | Status |
|---|---|---|
| Closed-world assumption | SAE M2 (trust-state conditioned budgeting — upstream intent is structurally untrusted) | Prescribed (K19) |
| Absent inter-layer enforcement | SAE ExecutionRequest/ExecutionContext/ExecutionDecision API contract (typed, validated, provenance-carrying) + scatter-gather terminal-leaf placement | Prescribed (K19 + scatter-gather topology) |
| Ungoverned distribution surface | SAE M2 (provenance score p_prov_t for skill/toolchain) + M5 (staged execution for low-provenance actions) | Prescribed (K19) |
| Lexical model for exec gating | SAE M1 (Intended Policy Spec with hard OOS rules) + M3 (projection-based enforcement — enforce on the action, not the text) | Prescribed (K19) |
| Prompt injection as above-policy attack | SAE M2 (I_inj flag from safety monitors) + K20 §6.6 (mandatory provenance tag for every context-window string) + K22 Reasoning Safety Monitor (step-level detection + interrupt) | K19+K22: SAE enforces at execution boundary; K22 detects at reasoning boundary |

The gap: K20's §6.6 — "mandatory provenance tag for every string entering the context window" — had no direct Cemini analog until K22. SAE's trust-state (z_t) provides provenance-gated budgeting at the execution boundary, but does not address the context-window layer where prompt injection operates.

**K22 closes this gap.** The Reasoning Safety Monitor (@concepts/reasoning-safety-monitor.md, from @sources/3-29-15.md) provides the missing detection layer. It inspects each reasoning step as it's generated, classifies unsafe behaviors into a nine-category taxonomy, and dispatches an interrupt signal BEFORE corrupted reasoning reaches tool execution. The monitor's per-step verdict (safety flag + error type code + confidence + location quote) is precisely the context-window provenance signal K20 §6.6 prescribed: it identifies which reasoning step was manipulated, by what attack mechanism (BadChain → Goal Deviation; Preemptive Answer → Calculation Error + Premature Conclusion; OverThink → Misinterpretation; Deadlock → Reasoning Loop), and with what confidence.

K19+K20+K22 now form a complete execution-security architecture: K19 enforces at the execution boundary (SAE), K20 catalogs the threat model (OpenClaw taxonomy), and K22 detects at the reasoning boundary (Reasoning Safety Monitor). The monitor's interrupt signal can feed into SAE's trust-state as a reasoning-integrity component — z_t now carries both provenance (p_prov_t, from M2) and reasoning-safety (I_reasoning, from K22).

### When to consult this page

- Designing execution-security boundaries for any agent framework where LLMs can invoke host commands
- Evaluating whether a new agent-framework CVE or GHSA fits a known pattern (consult the two-axis taxonomy)
- Threat-modeling a multi-agent deployment (consult the kill chain + three bypass classes)
- Assessing whether a skill/plugin marketplace needs supply-chain controls beyond what the runtime provides (consult structural condition #3)
- Understanding why lexical shell-command allowlists fail (consult lexical-vs-semantic section)

## Snippets

**S1 — Context Manipulation as novel kill-chain stage (p.10, §4.3)**:
> "The Context Manipulation stage has no direct analog in the conventional Cyber Kill Chain or MITRE ATT&CK frameworks. It captures the unique property of LLM-integrated systems where attacker-controlled data enters the model's context window and is processed as instruction rather than as data. Traditional kill chains model data as passive—something to be exfiltrated or encrypted. In agent frameworks, data is active: it can persuade, redirect, and reprogram."
>
> *— @sources/ai-2-4-3.md p.10, §4.3*

**S2 — Three bypass classes (pp.23–24, §5.8.3)**:
> "Exec-policy bypass operates below the reasoning layer—it circumvents the runtime's enforcement of which system calls or tool invocations are permitted. Skill-level escalation operates beside the reasoning layer—it exploits the operator trust model to register malicious capabilities before policy is applied. Prompt injection operates above both—it manipulates the content from which the model constructs its intentions before any policy enforcement is reached."
>
> *— @sources/ai-2-4-3.md pp.23–24, §5.8.3*

**S3 — Lexical model vs. semantic reality (p.20, §5.6.4)**:
> "Taken together, these three bugs share a single root cause: the exec allowlist was designed as a string-matching system operating on static representations of command text, while the actual security boundary it was meant to enforce requires reasoning about command semantics—how the shell will interpret the string at runtime, what executable the invocation will actually dispatch to, and what the effective set of active options will be after GNU abbreviation expansion."
>
> *— @sources/ai-2-4-3.md p.20, §5.6.4*

**S4 — The closed-world assumption (p.26, §7)**:
> "The first structural condition is a pervasive closed-world assumption: each subsystem was implemented as though its inputs originated from a cooperative, finite, and trusted set of sources. The exec allowlist assumed that command representations were enumerable through lexical parsing. Channel allowlists assumed that sender identity fields were immutable properties of authenticated sessions. The LLM context assembly pipeline assumed that strings entering the context window represented information rather than potential instructions."
>
> *— @sources/ai-2-4-3.md p.26, §7*

**S5 — Inter-layer composition as root cause (p.26, §7)**:
> "The second structural condition is the absence of unified inter-layer policy enforcement. Trust decisions are made locally (per call site, per subsystem, per handler) without a global invariant enforced across component boundaries. The Gateway RCE chain illustrates this: three independently moderate-severity advisories composed into complete unauthenticated host code execution because no enforcement point observed the full call path from LLM tool invocation to Node-Host shell execution."
>
> *— @sources/ai-2-4-3.md p.26, §7*

**S6 — Supply chain as execution surface (p.27, §7)**:
> "The third structural condition is the emergence of the plugin and skill distribution channel as an execution surface for which the runtime provides no dedicated policy primitive. The malicious yahoofinance skill did not exploit a memory-safety bug or parsing flaw; it operated entirely within the LLM context window, evading the entire exec policy pipeline."
>
> *— @sources/ai-2-4-3.md p.27, §7*

**S7 — Unified inter-layer enforcement (p.26, §6.7)**:
> "All five defense areas above share a common structural requirement: trust properties must be enforced at inter-layer interfaces through typed, validated, provenance-carrying request objects, rather than at per-call-site checks within each layer. A unified policy boundary would evaluate, for any node.invoke frame, whether the initiating context (agent, operator, inter-session) is authorized to request the specific command with the specific parameters, regardless of which individual layer the request traverses."
>
> *— @sources/ai-2-4-3.md p.26, §6.7*
