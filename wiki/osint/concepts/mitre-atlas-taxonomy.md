---
title: MITRE ATLAS Taxonomy — Adversarial Threat Landscape for AI Systems
type: concept
tags: [security, taxonomy, mitre, ai-threats, llm-security, prompt-injection, rag-security, cemini-internal]
keywords: [mitre-atlas, attack-framework, prompt-injection, rag-poisoning, llm-jailbreak, agent-tool-poisoning, morris-ii-worm, openclaw, threat-modeling]
related:
  - entities/tools/mitre-atlas.md
  - sources/5-4-links-tool-eval.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/sae-execution-contract.md
  - concepts/reasoning-safety-monitor.md
  - concepts/agent-authorization-stack.md
  - concepts/cemini-license-posture.md
  - entities/infrastructure/deepseek-api.md
  - entities/frameworks/fastmcp.md
  - entities/tools/deepteam.md
  - concepts/reviewer-passive-injection-corpus.md
maturity: validated
created: 2026-05-04
updated: 2026-10-25
---

## Relations

- @entities/tools/mitre-atlas.md — entity page; this concept is the taxonomy synthesis derived from K28's Adopt-tier verdict
- @sources/5-4-links-tool-eval.md — origin source (URL 8 of the 19-tool eval batch)
- @concepts/openclaw-security-taxonomy.md — K20 promotion; ATLAS includes 4 OpenClaw-specific case studies (CS0048-CS0051) that directly cross-reference our K20 deep-read
- @concepts/sae-execution-contract.md — K19 promotion; SAE's ALLOW/LIMIT/BLOCK middleware is one realisation of the M0030 + M0033 mitigation classes
- @concepts/reasoning-safety-monitor.md — K22 promotion; closes the gap between technique-detection and execution-blocking on the agent-side reasoning chain
- @concepts/agent-authorization-stack.md — synthesis page; ATLAS techniques map onto the authorization stack's layers
- @concepts/cemini-license-posture.md — license-pattern catalog; ATLAS uses Apache-2.0 (data) + separate website terms-of-use, NOT CC BY 4.0 as initially recorded in the K28 ingest
- @entities/infrastructure/deepseek-api.md — Cemini's brain; ATLAS techniques target this kind of LLM API surface
- @entities/frameworks/fastmcp.md — Cemini's MCP layer; ATLAS techniques on AI Agent Tool Invocation directly target this surface

## Raw Concept

Synthesis of MITRE ATLAS v5.6.0 (Adversarial Threat Landscape for Artificial-Intelligence Systems) for use as Cemini's canonical AI-security threat model. ATLAS is a living knowledge base modeled directly on MITRE ATT&CK; it maps 16 tactics × 170 techniques × 35 mitigations × 57 case studies of adversarial attacks against AI-enabled systems.

K28 ingest (`@sources/5-4-links-tool-eval.md` URL 8) marked ATLAS as **Adopt-tier** for the wiki layer. This concept page is the synthesis (Option C from the K28 plan: single concept page + reference URLs, NOT a full mirror of all 200+ ATLAS objects, since (a) atlas.mitre.org is the canonical live source and (b) only a subset of techniques are operationally relevant to Cemini's threat surface).

### License posture

- **atlas-data GitHub repo**: Apache-2.0 (per `https://github.com/mitre-atlas/atlas-data/LICENSE`). Permissive; preserve copyright notice, state changes, attribute origin.
- **atlas.mitre.org website**: per MITRE's separate Terms of Use. The K28 eval cited the standard MITRE attribution boilerplate, which applies when reproducing **website-presented** content (rendered case-study pages, etc.). For data extracted from the GitHub repo and re-presented in our own narrative, Apache-2.0 license terms are sufficient.

Attribution boilerplate when copying website-presented ATLAS content verbatim:

> "© 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation."

This page does NOT reproduce ATLAS content verbatim at length — only short technique IDs and titles. Full descriptions are linked to the canonical source.

### Correction to K28 ingest

The K28 eval (`@sources/5-4-links-tool-eval.md` URL 8) recorded ATLAS as "CC BY 4.0 + custom MITRE Terms of Use". This is partially wrong: the **data feed** is Apache-2.0, not CC BY 4.0. The website may use CC BY 4.0 for site-presented content (matrix renderings, case-study HTML), but the underlying data we'd ingest from is Apache-2.0. License-posture concept page (`@concepts/cemini-license-posture.md`) updated to record this distinction.

## Narrative

### The 16 tactics (ATLAS v5.6.0)

ATLAS organizes adversary lifecycle stages as 16 tactics. Modeled on ATT&CK, but with AI-specific phases (`AI Model Access`, `AI Attack Staging`) added. Cross-references to ATT&CK tactic IDs preserved.

| # | Tactic ID | Name | Adversary intent (one-line) |
|---|-----------|------|------------------------------|
| 1 | AML.TA0002 | Reconnaissance | Gather info about the target AI system |
| 2 | AML.TA0003 | Resource Development | Establish AI artifacts, infrastructure, accounts |
| 3 | AML.TA0004 | Initial Access | Get a foothold inside the AI system |
| 4 | AML.TA0000 | AI Model Access | Reach the AI model itself (API, white-box, edge) |
| 5 | AML.TA0005 | Execution | Run malicious code embedded in AI artifacts |
| 6 | AML.TA0006 | Persistence | Maintain foothold via poisoned AI artifacts |
| 7 | AML.TA0012 | Privilege Escalation | Gain higher-level permissions |
| 8 | AML.TA0007 | Defense Evasion | Avoid detection by AI-enabled security software |
| 9 | AML.TA0013 | Credential Access | Steal account credentials |
| 10 | AML.TA0008 | Discovery | Map the AI environment internally |
| 11 | AML.TA0015 | Lateral Movement | Pivot through AI Ops infrastructure (model registries, vector DBs, training pipelines) |
| 12 | AML.TA0009 | Collection | Gather AI artifacts and related information |
| 13 | AML.TA0001 | AI Attack Staging | Prepare attack on the target AI model (proxy training, poisoning, adversarial crafting) |
| 14 | AML.TA0014 | Command and Control | Communicate with compromised AI systems |
| 15 | AML.TA0010 | Exfiltration | Steal AI artifacts or info about the system |
| 16 | AML.TA0011 | Impact | Manipulate, interrupt, erode confidence, destroy AI systems |

### LLM-relevant techniques (Cemini's primary threat surface)

Cemini's threat model is dominated by techniques touching:
1. The **DeepSeek API surface** (LLM brain interactions)
2. The **FastMCP @mcp.tool decorators** (AI agent tool invocation)
3. The **kb-server + stash retrieval layer** (RAG context)
4. The **librarian wiki** (AI Ops infrastructure that lateral-movement targets)

Relevant subset of the 170 ATLAS techniques (out of 53 LLM-tagged + agent-tagged):

| Technique ID | Name | Tactic | Cemini surface affected |
|--------------|------|--------|-------------------------|
| AML.T0051 | LLM Prompt Injection | Execution | DeepSeek API call site (any user/document → prompt path) |
| AML.T0051.001 | Indirect Prompt Injection | Execution | RAG context, document ingest, librarian wiki |
| AML.T0054 | LLM Jailbreak | Privilege Escalation, Defense Evasion | DeepSeek API (boundary on what the brain will do) |
| AML.T0064 | Gather RAG-Indexed Targets | Reconnaissance | librarian wiki contents indexable by adversary |
| AML.T0065 | LLM Prompt Crafting | Resource Development | Adversarial preparation against Cemini-specific prompts |
| AML.T0067 | LLM Trusted Output Components Manipulation | Defense Evasion | Output rendering / structured-output post-processing |
| AML.T0068 | LLM Prompt Obfuscation | Defense Evasion | Bypass our pre-call hooks |
| AML.T0069 | Discover LLM System Information | Discovery | Reveal Cemini's system prompts, model identity |
| AML.T0070 | RAG Poisoning | Persistence | Plant adversarial entries in librarian wiki / kb-server |
| AML.T0071 | False RAG Entry Injection | Defense Evasion | Inject entries that influence retrieval |
| AML.T0080 | AI Agent Context Poisoning | Persistence | Poison stash episodic memory or session state |
| AML.T0081 | Modify AI Agent Configuration | Persistence, Defense Evasion | Touch FastMCP / Conductor config.yaml |
| AML.T0086 | Exfiltration via AI Agent Tool Invocation | Exfiltration | Use a poisoned MCP tool to leak data via tool params |
| AML.T0093 | Prompt Infiltration via Public-Facing Application | Initial Access, Persistence | User-facing input → DeepSeek path |
| AML.T0099 | AI Agent Tool Data Poisoning | Persistence | Tool inputs/outputs tampered to mislead the brain |
| AML.T0100 | AI Agent Clickbait | Execution | Confused-deputy-style agent action triggers |
| AML.T0101 | Data Destruction via AI Agent Tool Invocation | Impact | Tool-mediated destructive ops (DELETE, rm, etc.) |
| AML.T0103 | Deploy AI Agent | Execution | Adversarial deployment of an unauthorized agent |
| AML.T0104 | Publish Poisoned AI Agent Tool | Resource Development | Supply-chain attack on tools we install |
| AML.T0110 | AI Agent Tool Poisoning | Persistence | Modify @mcp.tool decorator behavior |

For full descriptions of any technique above: https://atlas.mitre.org/techniques/<ID> (e.g., https://atlas.mitre.org/techniques/AML.T0051 for LLM Prompt Injection).

### LLM-relevant mitigations

Out of 35 ATLAS mitigations, 11 directly inform Cemini-side defenses:

| Mitigation ID | Name | Cemini implementation locus |
|---------------|------|-----------------------------|
| AML.M0002 | Passive AI Output Obfuscation | Sanitize LLM-emitted text before downstream consumption |
| AML.M0007 | Sanitize Training Data | Vet any external-data ingest path for poison content |
| AML.M0008 | Validate AI Model | Sanity-check model behavior pre-deployment (cross-validate vs known-correct outputs) |
| AML.M0020 | Generative AI Guardrails | Pre-call hooks in `services/llm_analyst/deepseek_client.py`; system-prompt invariants |
| AML.M0026 | Privileged AI Agent Permissions Configuration | Explicit allowlist of MCP tools the brain can invoke |
| AML.M0027 | Single-User AI Agent Permissions Configuration | Per-session token budget; per-user execution context |
| AML.M0028 | AI Agent Tools Permissions Configuration | FastMCP tool registry — what each agent can call |
| AML.M0029 | Human In-the-Loop for AI Agent Actions | Manual confirmation gates for destructive / financially-impactful tool calls |
| AML.M0030 | Restrict AI Agent Tool Invocation on Untrusted Data | Don't let RAG-retrieved content trigger tool calls |
| AML.M0032 | Segmentation of AI Agent Components | Run brain, tools, RAG retrieval in separately-credentialed containers |
| AML.M0033 | Input and Output Validation for AI Agent Components | Schema-validate every tool input/output against a typed contract |

These map cleanly onto the existing Cemini agent-authorization-stack (`@concepts/agent-authorization-stack.md`):
- M0026/M0027/M0028 ⇒ K19 SAE execution contract (`@concepts/sae-execution-contract.md`)
- M0029 ⇒ Human-in-the-loop nodes in the LangGraph orchestrator
- M0030 ⇒ K22 reasoning safety monitor (`@concepts/reasoning-safety-monitor.md`)
- M0032 ⇒ Hetzner container topology + private-network isolation
- M0033 ⇒ FastMCP `@mcp.tool` typed signatures + return-schema validation

### High-impact case studies (LLM/agent-related)

ATLAS includes 57 case studies; ~30 involve LLM/agent surfaces. The ones most directly informative for Cemini:

- **AML.CS0024 — Morris II Worm: RAG-Based Attack** — self-replicating adversarial prompts that propagate through email-and-document RAG pipelines. Demonstrates that the RAG retrieval layer is itself an attack surface, not just a context-source. Direct relevance: kb-server's content-ingest layer must validate every document before indexing.
- **AML.CS0020 — Indirect Prompt Injection: Bing Chat Data Pirate** — adversarial web content executes against an LLM browsing on the user's behalf. Lesson: any tool that fetches external content and feeds it to the brain (web-search, browser-MCP, document-loader) is an indirect-injection vector.
- **AML.CS0035 — Data Exfiltration from Slack AI via Indirect Prompt Injection** — same indirect-injection class but in a corporate-collaboration-tool surface. Slack AI's RAG over channel content was exploited to exfiltrate to attacker-controlled URLs.
- **AML.CS0046 — Data Destruction via Indirect Prompt Injection Targeting Claude Computer-Use** — adversarial document content commanded Claude's computer-use tool to delete files. Direct precedent for how AML.T0101 (Data Destruction via AI Agent Tool Invocation) lands in practice.
- **AML.CS0048-AML.CS0051 — OpenClaw cases** — four cases referencing the OpenClaw framework: 1-click RCE (CS0050), Command & Control via Prompt Injection (CS0051), exposed control interfaces (CS0048), supply-chain compromise via poisoned skill (CS0049). Direct cross-link to `@concepts/openclaw-security-taxonomy.md` (K20 deep-read).
- **AML.CS0030 — LLM Jacking** — adversaries hijack victim LLM API credentials to run inference on their dime. Cemini-relevant: the `/opt/cemini/.env` DeepSeek API key is a high-value target; treat credential-stealing techniques (T0083 Credentials from AI Agent Configuration) seriously.
- **AML.CS0040 — Hacking ChatGPT's Memories with Prompt Injection** — adversarial input persists into chat history, surviving across sessions. Cemini-relevant: stash episodic memory + cpr-pattern resume context can carry persistent poisoning.
- **AML.CS0045 — Data Exfiltration via an MCP Server used by Cursor** — data-exfil through MCP tool boundary. Direct relevance to Cemini's `@mcp.tool` ecosystem.
- **AML.CS0053 — Poisoned Postmark MCP Server Email Exfiltration** + **AML.CS0054 — Data Exfiltration via Remote Poisoned MCP Tool** — supply-chain attacks via third-party MCP servers. Cemini's MCP marketplace adoption rubric (`@concepts/mcp-tool-marketplace.md`) directly addresses this; see "bus factor" + "license verification" filters.

### Implementation guidance — what to do in Cemini's code

Mapping ATLAS technique classes to specific Cemini codepaths:

| Defense scope | Where in code | ATLAS techniques covered |
|---------------|---------------|--------------------------|
| Pre-call sanitization | `services/llm_analyst/deepseek_client.py` (pre-prompt hooks) | T0051 prompt injection, T0051.001 indirect, T0068 obfuscation |
| RAG entry validation | `kb-server/` ingest pipeline + `librarian/sync_wiki_to_librarian.sh` content gate | T0070 RAG poisoning, T0071 false RAG entry, T0064 reconnaissance |
| Tool registry allowlist | FastMCP server config (`/opt/cemini/.mcp.json` allowed tool list) | T0086 exfil via tool, T0099 tool data poisoning, T0110 tool poisoning, M0028 |
| Session/credentials isolation | Stash episodic memory boundary + per-session DeepSeek API key scoping (if achievable) | CS0030 LLM Jacking, T0083 credential access, M0027 |
| Output schema validation | LangGraph node typed-output enforcement | T0067 output manipulation, M0033 |
| Human-in-loop gating | Trade-execution path (when notional > threshold or new market entry) | T0101 destruction via tool, M0029 |
| Container/network segmentation | Hetzner private network + per-container service identity | T0093 prompt infiltration, M0032 |
| Reasoning-chain monitoring | K22 reasoning safety monitor | T0080 context poisoning, T0067 output manipulation, M0030 |

The above is **not** a deployment checklist — many of these are existing or planned defenses. Use this table as the cross-walk between what ATLAS describes adversarially and what Cemini implements defensively. When a specific defense gets implemented, that defense earns its own concept page (e.g., a `concepts/prompt-injection-guard.md` if/when the pre-call sanitizer ships); this page is the index, not the per-defense doc.

### Open follow-ups

These technique classes lack mapped Cemini defenses today:

- **AML.T0094 Delay Execution of LLM Instructions** — adversarial prompts that delay execution to evade real-time inspection. No current detector. Reasoning safety monitor (K22) might extend here.
- **AML.T0097 Virtualization/Sandbox Evasion** — agent tools that detect sandbox environments and behave differently. Not currently a Cemini issue (no live sandbox testing) but flag if agent eval workflow grows.
- **AML.T0100 AI Agent Clickbait** — confused-deputy-style baiting of agents. Maps loosely to M0030 (untrusted-data restriction) but specific patterns vary; needs case-by-case analysis.

If/when defenses are implemented for any of these, promote that work to its own concept page and cross-link here.

## Snippets

Verbatim excerpts from ATLAS data (Apache-2.0, attribution preserved):

- **Reconnaissance tactic** (AML.TA0002): "The adversary is trying to gather information about the AI system they can use to plan future operations." [Source: atlas-data ATLAS.yaml v5.6.0]

- **AI Agent Tool Invocation** (AML.T0053): tactic context tags include `AML.TA0005 Execution` and `AML.TA0012 Privilege Escalation` — i.e., calling an agent's tool is BOTH an execution vector AND a privilege-escalation vector. The Cemini implication: every `@mcp.tool` decorator must assume both roles in the threat model. [Source: atlas-data ATLAS.yaml v5.6.0]

- **Restrict AI Agent Tool Invocation on Untrusted Data** (AML.M0030): the load-bearing mitigation for indirect-prompt-injection scenarios. Maps to: "RAG-retrieved content cannot trigger tool calls without explicit human confirmation." [Source: atlas-data ATLAS.yaml v5.6.0]

- **Morris II Worm framing** (AML.CS0024): RAG-based propagation is the canonical adversarial pattern where an adversarial document, once indexed, causes downstream LLM calls to emit further adversarial content that gets further indexed — a self-replicating loop. [Reference: atlas.mitre.org/studies/AML.CS0024]

## Dead Ends

*(none yet — first synthesis of ATLAS into the wiki.)*

## Updating this page

ATLAS evolves regularly (v5.6.0 at this snapshot). Refresh cadence:
- Quarterly: pull latest `dist/ATLAS.yaml` from `mitre-atlas/atlas-data`, diff against the technique tables above, update if new LLM/agent techniques land
- On adoption: when Cemini ships a new defense, update the implementation-guidance table and cross-link the new concept page
- On retire: if a technique is deprecated upstream, mark it here with `[RETRACTED]` per CLAUDE.md citation conventions

The canonical source is always atlas.mitre.org / atlas-data; this page is a curator's-cut for Cemini's threat surface, not a mirror.
