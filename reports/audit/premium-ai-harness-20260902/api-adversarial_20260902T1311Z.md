I'll consult an independent panel before committing to findings, since much of this audit rests on inventory counts I cannot verify myself.

## Panel responses

### ~google/gemini-pro-latest

**1. Failure Modes and Wasted Effort**
*   **Context Poisoning:** 1,400+ lines of `alwaysApply` rules (770 + 311 + 319) guarantee the LLM will lose the actual prompt in the noise, leading to hallucinations, ignored instructions, and degraded reasoning. 
*   **Alert/Artifact Fatigue:** Generating multiple daily audits (super-audit, free-audit, NotebookLM exports) and 20 scheduled background jobs creates a high-noise environment. Most of these outputs are likely ignored.
*   **Drift:** Managing 28 isolated `.cursor/` directories means updates are out of sync, leading to unpredictable IDE behavior across projects.
*   **What is likely broken:** Over half of the 20 LaunchAgents are probably failing silently. The OpenRouter caching proxy is likely caching stale errors and serving them back to the IDE, causing phantom bugs. The wiki is a graveyard of unread text.

**2. Budgeting always-loaded IDE rule context**
*   **Budget:** Absolute maximum of 50–100 lines. Every line of `alwaysApply` dilutes the user's immediate prompt.
*   **Always-on:** Immutable boundaries (e.g., "Require human approval for PROD writes"), global code style (e.g., "Use strict TypeScript"), and project scaffolding directories.
*   **On-demand (Agent-requested):** API specifications, component-specific rules, MCP tool definitions.
*   **Wiki:** Human-to-human historical context, architecture decisions, meeting notes. AI should not read this unless explicitly pointed to it.
*   **Symptoms of too much context:** The model repeatedly apologizes for missing instructions, gives generic code instead of project-specific code, hallucinates tools, or fails to complete simple refactors because it is trying to satisfy 50 conflicting rules.

**3. Lifecycle Labels and Dual-ID Scheme**
*   **Diagnosis:** You have built a pseudo-Jira system that requires humans to be databases. Drop the dual IDs entirely.
*   **Mental Model / Migration:** Move to a linear 3-state system: `Idea` -> `Active` -> `Archived`.
*   **Action:** 
    1. Pick one source of truth (e.g., GitHub Issue numbers or a single sequential integer). 
    2. Drop `policy_wired`. If something must follow a policy, enforce it at the execution layer (MCP or IDE rule), not via a tag. 
    3. Run a one-time script to convert all K# dual IDs to standard folder/file names and delete the old tags.

**4. Managing 28 per-repo `.cursor/` configurations**
*   **Global vs. Repo Split:** Global config (`~/.cursorrules` or a globally registered MCP) handles cross-cutting concerns (git workflows, standard boundaries, communication style). Per-repo config handles *only* local build/test commands and specific file paths.
*   **Management:** Do not maintain 28 isolated configs. Create a central `federation-config` repo. Symlink the `.cursor/` directories from the 28 repos to this central repo, or use git submodules. If a rule doesn't apply to all 28, it belongs in a project-specific markdown file loaded on demand, not `alwaysApply`.

**5. Tiered Model Routing**
*   **Evaluation:** A 4-tier system (Free -> Cheap -> Mid -> Frontier) for two people is a false economy. The human time spent reviewing a bad output from a free model costs vastly more than a $0.02 API call to a frontier model.
*   **Criteria/Measurement:** Track the *first-shot success rate*. If a free/cheap model requires more than one correction prompt, it has failed its economic premise. 
*   **Current Tiers:** 
    *   *Free:* Useless for code generation. Fine for formatting or summarizing digests.
    *   *Cheap:* DeepSeek V3/R1 is exceptional and currently disrupts the "Mid" tier entirely.
    *   *Frontier:* Claude 3.5 Sonnet / GPT-4o remain strictly necessary for complex architectural synthesis and heavy refactoring.

**6. Subscription Overlap**
*   **Agentic IDE (Cursor Pro):** Keep. This already includes Claude 3.5 Sonnet and GPT-4o.
*   **Claude Max & Grok:** Cancel both. You are paying for web interfaces to models you already access via Cursor and OpenRouter. Cursor and DeepSeek API cover 99% of your coding and reasoning needs.
*   **Model Router (OpenRouter):** Keep. Use it to access DeepSeek and frontier models on demand.
*   **Two Web-Search APIs (Exa & Brave):** Cancel one. Exa is better for semantic/dev search; Brave is cheaper/broader. You do not need both.

**7. Triage of the 145-page Wiki vs 26 Skills**
*   **Signal:** A 100% naming mismatch proves the wiki and the AI execution layer are completely decoupled. The humans write wiki pages to feel productive; the AI uses skills to do work.
*   **Triage:** 
    1. **Promote:** Identify the 5-10 wiki pages containing actual operational runbooks or prompt fragments and turn them into executable MCP tools or `.mdc` files.
    2. **Archive:** Dump the remaining 135+ pages into a read-only `archive/` directory. Do not delete them, but remove them from the active AI search space.

**8. Scheduled Background Jobs (LaunchAgents)**
*   **Policy:** 20 jobs on a personal laptop is brittle. 
*   **Consolidation:** Move all jobs into a single orchestrator script (e.g., one Python script or Makefile) triggered by one LaunchAgent. 
*   **Observability:** Output everything to a single local log file. If a job fails, trigger a macOS notification (`osascript`). 
*   **Deletion:** If a digest or report is generated but not read/acted upon by a human for 3 consecutive days, delete the job.

**9. Local MCPs, Tunnels, and Proxies**
*   **Risks:** Running ngrok/SSH tunnels on a laptop used for production access bypasses your network firewall and creates a severe lateral movement vector. If a tunnel endpoint is compromised, the attacker has access to your local machine, your IDE, and your production credentials.
*   **Hygiene:** 
    1. Tunnels must default to OFF and require a manual human command to open, with a strict auto-timeout (e.g., 1 hour).
    2. Disabled-by-default MCPs (like the OSINT server) should be physically moved out of the `.cursor` path to prevent accidental activation by an LLM hallucinating a config change.

**10. Local Model Runtime (Ollama) and Caching Proxy**
*   **Ollama:** Keep it off. A MacBook cannot run coding models that compete with DeepSeek V3/R1 or Claude 3.5. You are wasting battery, RAM, and time for inferior output.
*   **Caching Proxy:** Delete it. Caching API calls for an AI dev setup is a massive anti-pattern. You will inevitably cache a hallucinated answer or a failed code generation, and the LLM will repeatedly fetch the cached failure when trying to debug.

**11. Top 10 Highest-Leverage Fixes (Ranked)**
1.  **Nuke the 1,400+ lines of `alwaysApply` rules:** Reduce to under 100 lines of strictly formatting and boundary constraints.
2.  **Delete the OpenRouter caching proxy:** Prevent stale context loops.
3.  **Cancel redundant subscriptions:** Drop Claude Max and Grok. Rely on Cursor Pro + OpenRouter (DeepSeek).
4.  **Centralize IDE configs:** Symlink `.cursor/` directories to a single repo to stop configuration drift.
5.  **Kill the dual-ID and 3-phase scheme:** Adopt a single source of truth (Issue #) and a linear status (Active/Archived).
6.  **Consolidate 20 LaunchAgents:** Collapse into 1-3 jobs (e.g., Daily Ingest, Daily Digest).
7.  **Disable all tunnels by default:** Implement a strict human-in-the-loop manual start with an auto-kill timer.
8.  **Archive the Wiki:** Move non-executable documentation out of the AI's default context path.
9.  **Simplify Model Routing:** Route all trivial/medium tasks directly to DeepSeek V3/R1 via API. Route hard tasks to Cursor (Claude 3.5 Sonnet). Drop the "free" tier.
10. **Halt all unused audits:** Stop generating reports (super-audit, NotebookLM exports) that no one reads.

**12. Over-engineering and the Minimal Alternative**
*   **The Argument:** Two humans are managing a 28-repo federation, 20 cron jobs, a custom caching layer, custom network tunnels, 5 AI subscriptions, and complex dual-labeling state machines on a single laptop. The cognitive overhead of managing the system has eclipsed the actual work the system was built to do. 
*   **Minimal Version:** 
    *   One IDE (Cursor Pro).
    *   One router for API access (OpenRouter, defaulting to DeepSeek).
    *   One global `.cursorrules` file.
    *   No local background jobs (move necessary digests to a lightweight cloud function or run them manually when opening the laptop).
    *   No wiki; documentation lives directly in the code repositories next to the systems they describe.

### ~openai/gpt-latest

## Overall verdict

This looks less like a federation than several partially overlapping control planes: IDE rules, wiki pages, skills, MCPs, model routers, audits, and LaunchAgents. The main risk is not lack of capability. It is that nobody can reliably tell which layer is authoritative, active, safe, or producing value.

The likely pattern is:

- Instructions exist but are not consistently followed.
- Automations run but their outputs are rarely consumed.
- Multiple services solve the same problem at different quality levels.
- Configuration volume creates an illusion of control while reducing predictability.
- Audit findings accumulate as more documents rather than becoming deletions or fixes.

A temporary freeze on new rules, skills, MCPs, jobs, subscriptions, and audit documents would be appropriate until the existing estate is reduced.

## 1. Likely failure modes and wasted effort

### What I would expect to be broken or unused

1. **Always-on rules are being diluted, contradicted, or truncated.**  
   Three files totaling roughly 1,400 always-applied lines are already excessive before global rules and repository context are counted.

2. **Rules describe an intended system rather than the system that actually runs.**  
   Long policy files commonly contain stale paths, obsolete names, duplicated prohibitions, aspirational workflows, and exceptions that nobody remembers.

3. **Per-repository configurations have drifted.**  
   Some repos likely contain older MCP definitions, copied rules with slight differences, dead paths, and project-specific overrides whose purpose is no longer known.

4. **MCP availability is nondeterministic.**  
   A server that exists only when a folder is open will make identical agent requests behave differently depending on IDE state. Disabled servers may still be assumed available by documentation or prompts.

5. **LaunchAgents are silently failing or running redundantly.**  
   Common causes include missing shell environment, moved executables, sleeping laptops, expired credentials, unbounded logs, overlapping runs, and jobs succeeding technically while producing unused output.

6. **Routing costs are measured without the cost of retries and review.**  
   A free model that requires two retries, correction by Grok, and human verification is not free.

7. **Model names conceal endpoint variability.**  
   “Qwen,” “Kimi,” or “DeepSeek” is not a stable routing definition. Variant, quantization, provider, context limit, rate limit, and provider-side changes materially affect results.

8. **Reports are replacing decisions.**  
   Multiple audits with unclear disposition suggest analysis inventory rather than remediation. Findings probably conflict or repeat.

9. **The wiki is primarily a write-only archive.**  
   Zero basename overlap does not prove there is no semantic relationship to skills, but it strongly suggests there is no maintained discovery or provenance link.

10. **Human workflow is paying orchestration tax.**  
    The operators may spend substantial time deciding where a task goes, reconciling outputs, maintaining configs, and reading digests instead of completing the underlying task.

11. **Security boundaries are weaker than the conceptual policy suggests.**  
    Local MCPs, tunnels, global registrations, production credentials, and agent tools on one laptop create a broad ambient-authority environment.

12. **The caching layer may deliver little actual savings.**  
    Exact prompt cache hits are often low for agentic work. It may instead add another source of logging, stale behavior, secret exposure, and difficult debugging.

## 2. Budgeting always-loaded IDE context

Treat always-on context as scarce instruction bandwidth, not cheap documentation.

### Always-on rules

Keep only rules that are:

- Applicable to nearly every request in that scope.
- Short, unambiguous, and testable.
- Costly or dangerous to violate.
- Not already enforced more reliably by permissions, CI, or tooling.

Typical contents:

- Production/LIVE/irreversible writes require explicit human approval.
- Do not expose secrets.
- Default to read-only inspection.
- Run specified tests before declaring completion.
- A small number of repository-specific commands or hard constraints.

As a starting limit, aim for approximately:

- **Global always-on:** 300–800 words.
- **Per-repo always-on:** 300–1,000 words.
- **Total automatic instruction context:** preferably under 2,000–3,000 tokens unless measured evidence justifies more.

Line count is imperfect, but a 770-line always-on policy is almost certainly documentation masquerading as instruction.

### On-demand documents

Use these for:

- Deployment procedures.
- Architecture explanations.
- Incident response.
- Trading or OSINT workflows.
- Detailed style guides.
- Rare exceptions.
- MCP/tool operating instructions.
- Large checklists.

The short always-on rule should point to the relevant document by task trigger, for example: “Before a production deployment, read `docs/production-runbook.md`.”

### Wiki

Use the wiki for:

- Explanations, research, historical decisions, and references.
- Material not required to perform a routine task correctly.
- Human-readable navigation and institutional memory.

It should not be the sole source for a safety control or required executable procedure.

### Symptoms of excessive always-on context

- The agent violates important rules despite those rules being present.
- It cites irrelevant policy language in simple tasks.
- Responses become verbose, hesitant, or policy-dominated.
- Different sessions interpret the same rule differently.
- Instructions near the end of files appear ignored.
- More prompt clarification is needed for ordinary work.
- Latency and token use rise without improved outcomes.
- The agent follows a general rule instead of a more relevant project rule.
- Operators cannot predict which instruction wins during a conflict.

Test this empirically with 10–20 representative tasks using the current rules and a reduced rule set.

## 3. Replacing lifecycle labels and dual IDs

Do not try to refine the meanings of “Phase-0,” “Phase-1,” and `policy_wired`. Retire them. “Phase” is especially poor because it can mean maturity, chronology, deployment stage, or project generation.

For policy-like items, use one canonical state machine:

`PROPOSED → ACCEPTED → IMPLEMENTED → VERIFIED → RETIRED`

Definitions:

- **PROPOSED:** captured but not approved.
- **ACCEPTED:** approved as intended policy or work.
- **IMPLEMENTED:** represented in actual rules, code, configuration, or procedure.
- **VERIFIED:** tested or observed to work.
- **RETIRED:** no longer active; retained only for history.

Use `BLOCKED` as a separate flag, not a lifecycle state. Use object type separately: `policy`, `skill`, `job`, `service`, `report`, and so forth. Do not use `policy_wired` as both a category and a maturity state.

### IDs

Adopt one opaque canonical namespace, such as:

`CEM-0001`

Keep the existing K identifiers as aliases only:

```yaml
id: CEM-0001
legacy_ids:
  - K12
  - PHASE1-K12
state: IMPLEMENTED
type: policy
```

### Low-rewrite migration

1. Freeze creation of new Phase/K identifiers.
2. Create one small registry—CSV, YAML, or a database table—with canonical ID, title, type, state, location, owner, and legacy aliases.
3. Do not infer ambiguous mappings. Mark them `NEEDS_REVIEW`.
4. Add aliases to existing documents without renaming everything immediately.
5. Update only items touched during normal work, except for actively used policies and jobs, which should be migrated first.
6. Publish a one-page glossary and remove the old labels from templates.
7. After a fixed transition period, make searches and tooling display only canonical IDs while still resolving aliases.

The registry is the authority; filenames and tags are indexes.

## 4. Managing 28 `.cursor/` configurations

The correct principle is **global baseline, repository delta**.

### Global/user-level configuration

Keep only truly universal behavior:

- Human approval requirement.
- Secret-handling requirements.
- Read-only defaults.
- General code-change discipline.
- Universally used, low-risk MCP registrations.

Avoid globally enabling broad write-capable MCPs merely for convenience.

### Per-repository configuration

Keep:

- Repository architecture and commands.
- Local test/lint/build instructions.
- Repo-specific protected paths.
- Repo-specific MCPs and environment assumptions.
- Domain constraints that genuinely differ.
- A concise pointer to relevant runbooks.

### Recommended cleanup

1. Inventory every `.cursor/` file by hash and purpose.
2. Identify exact duplicates and near-duplicates.
3. Delete copied global policy from repositories.
4. Reduce each repo to its actual delta.
5. Designate an owner for every remaining rule and MCP entry.
6. Remove rules that merely restate README material.
7. Add a lightweight check that flags unexpectedly large rule files, unknown MCPs, or reintroduced deprecated labels.

Do not build an elaborate configuration-generation framework for two people. A documented baseline, small repository deltas, and a periodic diff report are sufficient.

## 5. Evaluating tiered model routing

A tiered chain only saves money if it minimizes **total cost to an accepted result**, not initial inference price.

### Routing criteria

Route using observable task properties:

- Consequence of error.
- Need for repository-wide reasoning.
- Context volume and retrieval requirements.
- Tool-use requirements.
- Ambiguity of the request.
- Ease of automatic verification.
- Privacy constraints.
- Latency requirement.
- Expected output length.

Examples:

- **Free/cheap:** classification, extraction, formatting, simple summaries, boilerplate, testable local edits.
- **Mid-tier:** bounded debugging, moderate synthesis, code review, familiar multi-file work.
- **Frontier:** ambiguous architecture, security-sensitive changes, complex debugging, high-stakes reasoning, long tool-using tasks.

Production risk should route by consequence, not apparent difficulty.

### Required measurements

Create a fixed set of real tasks and record:

- Exact model and provider endpoint.
- First-pass acceptance rate.
- Human review minutes.
- Retry and escalation rate.
- Tool-call failures.
- Latency.
- Input/output tokens and actual price.
- Test or factual correctness.
- Rate-limit and availability failures.
- Cost per accepted result.

Do not trust savings claims until the lower tier matches the accepted-result rate over a meaningful sample. Re-run the evaluation when endpoint versions or providers change.

### General quality observations

- Strong Qwen and DeepSeek variants can be excellent value for bounded coding, transformation, and routine reasoning.
- Kimi-family models can be useful for large-document synthesis, but advertised context size is not evidence of reliable retrieval across that context.
- Hunyuan quality is more endpoint- and language-dependent; it should earn a routing slot through local tests rather than family reputation.
- Free endpoints are suitable for disposable, verifiable work. They are poor dependencies for time-sensitive workflows because availability, latency, limits, and exact variants can change.
- Summarization is deceptively risky: inexpensive models often produce fluent but lossy summaries. Test preservation of numbers, qualifications, dissent, and action items.
- For coding, tests and diffs matter more than benchmark reputation.
- “OpenCode Zen” and similar intermediary tiers should remain only if they produce a measurable quality, cost, privacy, or workflow benefit. Another hop by itself is not a benefit.

## 6. Subscription overlap

The largest overlap is among Cursor Pro, Grok, Claude Max, OpenRouter/API access, and DeepSeek credits.

### Likely consolidation

- **Agentic IDE:** Keep Cursor if it is the primary environment and its agent features are heavily used. It is not fully replaced by a chat subscription.
- **Frontier subscription:** Keep the one whose chat/CLI workflow is most frequently used outside Cursor.
- **Second frontier subscription:** Require evidence of a distinct advantage—specific model quality, usage limits, research access, or workflow. Otherwise rotate subscriptions monthly rather than keeping both continuously.
- **Cheap API:** Keep one for automation and high-volume bounded tasks. API credits and consumer subscriptions are not interchangeable.
- **Model router:** OpenRouter is useful for endpoint choice and consolidated billing. Direct-provider credits are redundant unless they offer materially better pricing, reliability, privacy, or features.
- **Web search:** Exa and Brave overlap substantially for ordinary retrieval. Exa may justify itself for semantic/research workflows; Brave may justify itself for conventional web search and predictable search results. Keep both only if measured workflows depend on their differences.
- **Smaller subscriptions:** Presume cancellation unless each has a named recurring workflow, monthly usage, and a replacement cost.

A simple rule: every paid service needs an owner, a recurring use case, and a quarterly “would we buy this again today?” decision.

## 7. Triaging the wiki and skills

Zero basename overlap signals weak information architecture, not necessarily zero semantic overlap. Likely problems include inconsistent naming, duplicated concepts, no provenance, and no clear path from knowledge to execution.

Classify each page into four groups:

1. **Operational source:** required to perform a recurring workflow.
2. **Reference:** useful background consulted occasionally.
3. **Evidence/history:** audit, research, or decision record.
4. **Obsolete/duplicate:** archive or delete.

Promote material to an executable skill only when:

- The workflow recurs.
- Inputs and outputs are defined.
- Success can be checked.
- Tool permissions are understood.
- A human currently follows the procedure consistently.

Do not turn explanatory essays into skills. Instead, give each existing skill:

- A canonical name.
- A one-sentence purpose.
- Owner.
- Inputs and outputs.
- Safety level.
- Links to supporting wiki pages.
- Last-used date.

Archive pages that have no owner, no inbound links, no recent use, and no unique evidentiary value. Audit artifacts should end with a disposition table: `accepted`, `rejected`, `superseded`, or `open`, plus an owner and action.

## 8. Policy for scheduled jobs

Twenty jobs on a personal laptop is plausible only if they are observable and demonstrably consumed.

Every job should have:

- Purpose and owner.
- Schedule and expected runtime.
- Timeout.
- Non-overlap lock.
- Idempotent behavior where possible.
- Last start, last success, and last failure.
- Structured log with rotation.
- Output destination and retention.
- Failure notification after a defined threshold.
- Explicit credentials and network dependencies.
- A documented effect of laptop sleep or missed schedules.

Create one daily status report showing only exceptions:

- Failed.
- Never completed.
- Running too long.
- Overlapping.
- Output not consumed.
- Credentials near expiry.
- Repeatedly missed because the laptop was asleep.

Deletion criteria:

- No output was consumed in 30 days.
- The same information appears in another digest.
- It fails repeatedly without anyone noticing.
- It produces more review time than value.
- It exists “just in case.”
- Its output has no named downstream consumer.

Consolidate schedules where practical. One morning pipeline with stages is usually easier to observe than several loosely related digest agents.

## 9. MCP, tunnel, and proxy risks

The main risk is ambient authority: an agent-controlled process can reach files, credentials, network services, or production systems beyond the operator’s immediate awareness.

Require:

- Read-only tools by default.
- Separate production credentials from ordinary development credentials.
- Least-privilege tokens with expiration.
- Explicit approval at the final LIVE or irreversible operation.
- No production write capability exposed to an MCP unless currently needed.
- Server version pinning and review of updates.
- An inventory of server, command, port, permissions, owner, and last use.
- Localhost authentication where supported; “local” is not an access-control policy.
- Restricted filesystem roots.
- Tool-call logging without secret contents.
- Disabled servers actually stopped, not merely hidden from one config.
- Tunnels bound only as required, authenticated, time-limited, and closed after use.
- Firewall review for proxies and MCP ports.
- No secrets in command-line arguments, world-readable files, or verbose logs.

Prompt injection is particularly relevant for search, GitHub, documents, OSINT, and MCP-fetched content. Retrieved text must never be treated as authorization to invoke sensitive tools.

## 10. Ollama and the local caching proxy

### Local models

Keep Ollama off unless there is a recurring workload where local execution provides one of:

- Required privacy or offline use.
- High-volume repetitive processing.
- Lower measured cost.
- Predictable latency.
- A model that performs the task adequately on available hardware.

On a single MacBook, local inference competes with the IDE, browser, indexing, and other services for memory, power, and thermal capacity. Running it merely because it is installed has negative utility.

### Caching proxy

A local proxy is worthwhile if it provides measured:

- Cache hit savings.
- Unified usage records.
- Rate limiting.
- Redaction or policy enforcement.
- Reliable failover.

Pitfalls include:

- Logging prompts and API keys.
- Incorrect cache-key construction.
- Cross-project or cross-user data leakage.
- Serving stale answers.
- Caching requests with nondeterministic or tool-dependent results.
- Altering streaming or tool-call behavior.
- Becoming a single point of failure.
- Hiding the true provider/model used.
- Low hit rates that do not justify maintenance.

Cache only clearly safe, deterministic requests, scope entries by user/project/model/configuration, encrypt or minimize storage, and expose the actual upstream endpoint in logs.

## 11. Top 10 fixes, ranked

1. **Replace Phase-0/Phase-1/`policy_wired` and dual IDs with one registry, canonical ID, and explicit state machine.**
2. **Cut always-applied rules to a short safety and execution baseline; move the remainder on demand.**
3. **Inventory all 28 `.cursor/` configurations and reduce each to a repository-specific delta.**
4. **Audit every LaunchAgent using last-success and output-consumption data; delete or consolidate unused jobs.**
5. **Create a single authoritative inventory of active services, MCPs, tunnels, credentials, jobs, and subscriptions.**
6. **Lock down production access: read-only defaults, separate credentials, least privilege, and final human approval.**
7. **Benchmark model routing on real tasks using cost per accepted result, including retries and human review.**
8. **Cancel overlapping subscriptions that lack a distinct measured workflow; start with the second frontier subscription and duplicate search API.**
9. **Triage wiki pages and audit packs into operational, reference, historical, and archive categories; attach dispositions to findings.**
10. **Remove inactive infrastructure—including Ollama, proxies, tunnels, and MCPs—unless each has a named current use and owner.**

## 12. The over-engineering case and a minimal alternative

The strongest evidence of over-engineering is the ratio of coordination machinery to operators:

- 28 IDE configurations.
- Hundreds of policy-tagged pages.
- 26 skills.
- Several model tiers.
- Multiple audits.
- Multiple MCP scopes.
- 20 scheduled jobs.
- Multiple overlapping subscriptions.
- Several identifiers for the same conceptual estate.

For two people, every additional control plane must be remembered, debugged, secured, and reconciled. If the operators are confused by the lifecycle model, the system has already exceeded its usable governance capacity.

### Deliberately minimal version

- **One primary IDE:** Cursor.
- **One short global safety rule:** human approval for LIVE/irreversible writes, secret handling, read-only default.
- **One small per-repo instruction file:** commands, architecture, local constraints.
- **One canonical registry:** IDs, state, owner, location.
- **One frontier model access path:** through Cursor or one preferred subscription.
- **One cheap API/router:** for automation and bounded low-risk tasks.
- **One web-search provider:** unless the second proves a distinct recurring advantage.
- **Three background workflows at most:** morning brief, document ingest, and one domain-specific pipeline.
- **No always-running local model unless actively justified.**
- **No persistent tunnel unless actively needed.**
- **Only essential MCPs enabled, read-only by default.**
- **One monthly operations review:** costs, failed jobs, unused outputs, open audit actions, and services to delete.

The target should not be a perfectly governed federation. It should be a small, predictable workstation where either operator can answer four questions quickly: what is authoritative, what is running, what can write, and what is worth paying for.

### ~anthropic/claude-opus-latest

## 1. Failure modes and what's probably already broken

The dominant failure mode here is **artifact accumulation without a consumer**. Every item in your inventory is a producer; almost nothing is described as a consumer with an owner and a decision it feeds. That asymmetry is the disease; everything below is a symptom.

Specific things I would bet money are broken or dead right now:

- **Several of the 20 LaunchAgents are silently failing.** LaunchAgents on a laptop miss runs when the lid is closed, fail on network absence, and inherit a minimal PATH that breaks `node`/`python`/`uv` invocations. Without `StandardErrorPath` plus an actual read of those logs, a job that has been erroring for weeks looks identical to one that works. Check `launchctl list | grep cemini` for nonzero exit statuses; expect at least 3–6 bad ones.
- **The 770-line alwaysApply rule is not being followed in full.** Instruction adherence degrades well before context limits. You are paying tokens on every request for guidance the model partially ignores, which is worse than not having it — you believe a constraint is enforced when it is advisory at best.
- **Free-tier OpenRouter models have changed underneath you.** Free endpoints get renamed, rate-limited, deprecated, or silently swapped. If your router has no per-model success/failure counter, some tier of that chain is almost certainly failing over instantly and you are actually running on DeepSeek or Grok while believing you are on free models.
- **The "leftover" Phase-0/Phase-1 items are not leftovers.** They are items that were never in either bucket because the taxonomy was invented after the work started. Same for the K# dual-ID: that is the fossil record of a renumbering you did halfway through.
- **The 145 wiki pages tagged `policy_wired` are write-only.** Zero basename overlap with 26 skills is near-proof no execution path reads them.
- **Some of the audit artifacts contradict each other** and none has a "decisions taken / rejected" section. A super-audit, cursor-audit, and free-audit that produced no diff to the repo are entertainment, not audit.
- **Duplicate, drifted `.cursor/rules` across 28 repos**, where you fixed a bad rule in one repo and 27 copies still carry the bug.
- **Cost blind spot:** with Cursor Pro, Grok, Claude Max, DeepSeek, OpenRouter, Exa, Brave, plus smaller ones, you have no single number for monthly spend per unit of useful work. The routing chain exists to save money on the cheapest part of the bill.

Wasted effort concentrates in three places: maintaining the taxonomy, maintaining the rules, and building routing sophistication for tasks whose absolute cost is trivial.

## 2. Always-on rule context budget

**Hard budget: 500 lines / ~5k tokens total always-applied per repo, and I would push for 200.** You are currently at roughly 1,400 lines of alwaysApply (770 + 311 + 319) before file context, MCP tool schemas, or conversation. That is indefensible.

The split:

- **Always-on (target ≤200 lines):** things that are true on every single request and whose violation is expensive. Realistically: the human-in-the-loop rule for LIVE/irreversible writes, "never commit secrets," the 3–5 non-obvious repo conventions, and a one-line index pointing at on-demand docs. Prohibitions and safety invariants belong here because you cannot rely on the agent knowing to fetch them.
- **Agent-requested / description-triggered rules:** anything conditional. Language conventions, deployment procedures, test patterns, API-specific guidance. Cursor's rule types exist precisely for this; use globs and descriptions so a Python rule loads on `.py` and nothing else.
- **Wiki:** narrative, rationale, history, decisions. Anything a human reads to understand *why*. An agent should reach it only via explicit search, never by default.

Rule of thumb: if you cannot state which specific bad output a rule line prevents, it is documentation, not a rule.

**Observable symptoms of always-on bloat:**
- The agent restates your rules back to you instead of doing the task (preamble inflation).
- Instructions in the middle of the rules file are ignored while first and last sections are honored.
- Behavior changes when you rephrase your prompt but not when you edit rules — the tell that rules are being crowded out.
- Rising cost/latency per turn with no quality gain; premature context compaction in long sessions.
- Contradictions surface as inconsistent behavior across sessions (near-certain at 1,400 lines — you almost certainly have direct contradictions between the 770-line policy file and the two 311/319-line project files, and you should diff them for exactly that).

Test empirically: delete the 770-line file for one week and record whether any output actually degrades. Most operators discover ~80% was inert.

## 3. Collapsing Phase-0 / Phase-1 / policy_wired into one model

Three labels exist because they answer three different questions that got conflated: *when was this built* (Phase-0/1 — historical, no longer actionable), *is it governed* (policy_wired), and *does it work*. Only the last two matter going forward.

**Do this: keep one dimension — status — and delete the rest.**

```
status: draft | active | deprecated | archived
```

Four states, one field, one source of truth. Transitions: `draft → active` (an operator has used it successfully at least once), `active → deprecated` (superseded; still present, do not extend), `deprecated → archived` (moved out of the load path). No transition back except `deprecated → active` with a reason. Archiving is a directory move, not a tag, so the load path physically cannot see archived items.

If you truly need governance as a separate axis, make it a boolean `hitl_required: true|false` — but note that "policy_wired" as a name is doing no work; nothing in your description depends on it programmatically.

**Phase-0/Phase-1 become metadata, not identity.** If you want the history, keep `created_phase: 0|1` as an inert annotation nobody branches on.

**Migration, no rewrite (an afternoon):**
1. Freeze new labels today. Announce between the two of you: no new Phase-* tags.
2. Write the K# → new-ID mapping to a single flat file (`ids.csv`: `k_id, old_id_a, old_id_b, canonical_id`). Pick **one** ID space as canonical — the one referenced by more live code, not the prettier one.
3. Bulk-assign: everything currently loaded and used → `active`. Everything "leftover" → `archived` by default. Deprecation is opt-out, not opt-in; make your partner argue an item back into `active`.
4. Leave old tags in place as dead text rather than mass-editing. Add a lint that fails if a Phase-* tag appears in a *new* file.
5. After 30 days, anything still `archived` and unmissed gets deleted, and the mapping file becomes the only trace.

The K# dual-ID problem resolves itself once one space is canonical and the other is a lookup, not an identifier.

## 4. Managing 28 `.cursor/` directories

28 copies of anything maintained by two people will drift; the question is only how you notice. The default answer of "sync them with tooling" is wrong — it industrializes the duplication.

**The split I'd insist on:**

- **User-level (`~/.cursor/rules`, global Cursor settings, user MCP config):** your personal working style, output preferences, the universal safety rules, and every MCP server you use in more than one repo (stash, github, atto). This is where the HITL rule lives, so it cannot be lost by a repo missing a file.
- **Per-repo `.cursor/`:** only what is genuinely specific to that codebase — its architecture, its build/test commands, its domain vocabulary, and MCP servers unique to it. Should be short. If a repo's rules are interchangeable with another repo's, they belong at user level.

**Then reduce repo count in the load path.** 28 repos for two people is itself a finding. Realistically 5–8 are active. Empty the `.cursor/` directories in the rest; do not maintain rules for repos you touch twice a year.

**Anti-drift, cheapest first:**
- A single script that prints a table of all 28 `.cursor/` contents with line counts, `alwaysApply` flags, and file hashes. Run it monthly. Duplication becomes visible, which is 90% of the fix.
- Identical hashes across repos → that content should be at user level. Delete the copies.
- Do **not** build a templating/sync system. It adds a config layer, which is what you said you want less of.

One caveat: user-level rules are invisible to collaborators and untracked by git. With two operators, keep `~/.cursor/rules` in a small dotfiles repo so you both share and can diff it.

## 5. Evaluating the routing chain

My blunt read: **the four-hop easy-task chain (free → OpenCode Zen → DeepSeek) is over-engineered for the money involved.** Easy tasks are cheap by definition. DeepSeek-class pricing means thousands of easy tasks cost single-digit dollars. You have built a fallback cascade with three failure surfaces to save an amount that is noise next to Claude Max plus Cursor Pro plus Grok. Every hop adds latency, a silent-failure mode, and a debugging path.

**Before believing any cost-savings claim, require:**
1. **A per-request log:** timestamp, task class, model actually served (not intended), input/output tokens, cost, latency, and an outcome flag. If you cannot produce cost-by-model for last month from a file, you have no savings claim.
2. **Retry accounting.** The only number that matters is cost-per-*accepted*-result. A free model that needs two retries plus a Grok escalation is more expensive than going to the mid tier first, once you price your own attention.
3. **A fixed eval set: 20–30 real tasks from your actual work**, with a rubric and a pass/fail you both apply. Run every tier against it once. This is a half-day and it settles most arguments permanently.
4. **A silent-degradation alarm.** Log which model served each request and alert on unexpected tier distribution. Otherwise free-tier deprecation looks like "the assistant got dumber lately."
5. **Human-time as the denominator.** At two operators, your attention is the scarce resource, not API dollars. Any routing decision that saves $5 and costs 20 minutes of confusion is a loss.

**On tier quality, generally (verify against your own eval, and expect this to shift within months):**
- **Coding:** the gap between cheap and frontier is largest here and it is not close on multi-file, agentic, or debugging work. Free/cheap models are fine for boilerplate, single-function edits, test scaffolds, regex, and format conversion. They are bad at knowing when to stop and at long tool-use chains. Do not route anything touching production code paths below your mid tier.
- **Summarization:** the gap is smallest. Cheap models are genuinely near-parity for digests, extraction, and classification. This is where your savings actually are — and it is exactly what your daily workflow (morning summary, content digests, ingest) is full of. Push all of it down.
- **Long context:** stated context windows are marketing. Effective recall degrades sharply mid-document on cheap models. For long-context work, prefer retrieval plus a small window over dumping 100k tokens into a cheap model. If you must use long context, put the question at both the start and end of the prompt.

**Simplification I'd actually ship:** two tiers, not four. Cheap (one model, one fallback) for summarize/extract/classify; frontier for code and reasoning. Route on task type, which you can name in advance, not on a subjective "difficulty" judgment made per-request.

## 6. Subscription overlap

Where the real overlap is:

- **Claude Max vs. Cursor Pro:** heavy overlap. Both give you frontier-model agentic coding. Max includes CLI-based agentic coding on the same underlying models Cursor routes to. You are paying twice for "frontier model writes code in my repo." This is your largest genuine redundancy and probably your two largest line items.
- **Grok vs. Claude Max vs. Cursor:** a third frontier subscription as the "medium" tier is hard to justify. Medium-difficulty tasks are the easiest thing to absorb into either neighbor. The only defensible case is a capability you specifically depend on — real-time X/social data for the trading workflow. If that is the reason, keep it and say so; if it is "second opinions," that is a $300/yr habit.
- **Exa vs. Brave:** substantially overlapping. They are different in kind — Brave is a cheap general web index, Exa is embedding/neural search tuned for finding semantically similar content. Running both is defensible only if you can point at queries where one clearly wins. Otherwise keep the cheaper one, cancel the other, and re-add if you feel the loss. My prior: keep Brave for breadth and cheapness, drop Exa unless the research workflow specifically leans on neural retrieval.
- **OpenRouter vs. DeepSeek direct:** OpenRouter can serve DeepSeek. Direct API is marginally cheaper and one less hop; the router's value is model access breadth and failover. Pick one as primary. Keeping both credits is fine (both are prepaid, not recurring) but the *routing complexity* of using both is not.

**Genuinely no substitute:** exactly one frontier subscription, and a router or a cheap API for bulk work. That's it.

**Genuinely cheaper at the same tier:** the free/cheap models are at parity for summarization and classification, so anything you route there is real savings. Local embeddings are free and fine. Frontier coding has no free substitute at the same quality tier — do not try.

**My recommendation:** cancel one of {Cursor Pro, Claude Max} — pick by which agentic surface you actually reach for on a Tuesday, and run the other for a month before deciding permanently. Cancel one search API. Put Grok on notice with a written justification tied to the trading workflow. Expect to cut spend materially with no capability loss you'll notice.

## 7. The 145-page / 26-skill disjunction

Zero basename overlap between 145 `policy_wired` pages and 26 skills is not a naming problem. It is evidence that **the wiki and the executable layer were built by different impulses and have never been connected.** The tag `policy_wired` is aspirational — it marks intent to wire, not wiring. If it were load-bearing, at least a handful of names would collide.

The second signal: 145 pages for two people means the wiki's real function is *thinking-by-writing*, which is legitimate but should not be confused with infrastructure.

**Triage — do it in one sitting, time-boxed, both operators present, 30 seconds per page:**

- **Promote to tooling (expect 5–15 pages):** the page describes a procedure you have executed more than three times and would execute again. These become skills. If it is not a repeatable procedure, it cannot be a skill.
- **Keep as reference (expect 20–40):** you have actually consulted it in the last 90 days, or it encodes a decision you'd otherwise relitigate. Architecture decisions, incident notes, vendor comparisons.
- **Archive (expect 90–120):** everything else. Move to an `archive/` tree, keep it searchable, remove it from any index or default view.

Then **drop the `policy_wired` tag entirely** — it will mean nothing after triage — and separately audit the 26 skills for whether they are invoked at all. My prior is that a third of the skills are also dead. The disjunction cuts both ways.

Do not attempt to reconcile the two namespaces by renaming. That preserves 145 pages of debt with better labels.

## 8. Scheduled-job policy

20 LaunchAgents for two people is roughly 4x what the described workflow needs. The core rule: **a scheduled job you don't notice failing is a liability, not an asset.**

Minimum bar per job — no job runs without all five:
1. **A named human consumer and a decision it feeds.** Written down. "Digest for morning review, read by A before standup." If no one reads the output, delete the job.
2. **stdout/stderr to a dated log file** with rotation. Non-negotiable and nearly free.
3. **Failure notification you cannot ignore** — macOS notification, or a line prepended to the morning summary. Silent email is not notification.
4. **A lockfile** (`flock`-style or a PID file with staleness check) so a slow run cannot overlap the next. Overlap on ingest jobs corrupts state and is a classic cause of duplicated wiki pages.
5. **A heartbeat.** Each job writes `last_success` with a timestamp. One extra job — a **health check** — reads all heartbeats and reports anything stale into your morning summary. This single job replaces per-job monitoring and is the highest-value addition in this whole audit.

Also: set `Nice` values so background ingest doesn't compete with your IDE, and remember `StartCalendarInterval` jobs skip while the machine is asleep — if a job must run daily, make it idempotent and catch-up-capable rather than assuming it fired.

**Deletion test.** For each of the 20, answer: *when did a human last act on this output?* Never / can't recall / >30 days → disable (don't delete) for two weeks. Nothing missed → delete. Expect to end at 6–9 jobs. Consolidate aggressively: three separate digest jobs should be one job with three sections, because it is one thing you read at one time.

**Order of operations:** do the audit *before* adding observability, or you'll instrument jobs you're about to delete.

## 9. MCP, disabled servers, tunnels, and prod access

This is the section where I'd push back hardest, because it is the only one where the downside is unbounded.

**Real risks:**
- **MCP servers run with your full user privileges.** They are ordinary local processes with your filesystem, keychain-adjacent files, and network access. A third-party MCP server is a supply-chain dependency with no sandbox.
- **Tool-description injection.** An MCP server can change its tool descriptions after you approve it; those descriptions enter the model's context and can carry instructions. A benign server that updates can become a hostile one without any visible change on your side.
- **Prompt injection reaching prod tools.** This is your actual top risk. You ingest documents and run OSINT — untrusted text — in the same agent sessions that can reach production tooling. The lethal combination is untrusted input + private data + an egress or write capability. `prod-mcp` being "explicitly disabled in one project's mcp.json" is a comment, not a control: a per-project disable flag is one edit, one merge, or one agent-made config change away from being enabled, and it doesn't constrain other projects at all.
- **"Off when its folder is closed"** is ambient, not intentional. Your lazy-tool server's security posture is a side effect of window state.
- **Tunnels and the caching proxy** are listening sockets and stored credentials. An ngrok-style tunnel exposes a local port to the public internet, often with weak or no auth, sometimes left up for days. On a machine with production access, that is the single highest-severity item in your inventory.

**Hygiene I'd require:**
1. **Separate credentials by blast radius.** Prod write credentials must not be reachable from the same environment that runs ingest/OSINT. Different shell profile, different keychain entry, or ideally a separate macOS user account for prod work. This is the one structural change worth the cost.
2. **Delete `prod-mcp` from config entirely** rather than disabling it. Keep the config snippet in a password manager or a gitignored file you paste in when you need it. Friction is the feature. A disabled entry is a loaded gun with the safety on.
3. **Pin MCP server versions**, no auto-update, and read the diff before bumping. Prefer servers you can read in an afternoon.
4. **Inventory listening ports weekly** — `lsof -iTCP -sTCP:LISTEN -P`. Tunnels get an expiry: if you can't say why it's up, kill it. Never leave a tunnel running overnight without auth in front of it.
5. **Keep HITL approval at the tool layer, not the prompt layer.** Your hard constraint is currently expressed in a 770-line rules file — i.e., enforced by a model's goodwill. Move it into the tool: the prod write path should require a typed confirmation or a separate credential that only a human supplies. Then it holds regardless of what the model reads, and it survives you deleting the rules file (which I've recommended).
6. **Least privilege on the boring servers.** github MCP with a fine-grained PAT scoped to the repos you actually use, not a classic token with `repo` on everything.
7. **No MCP server with prod write access registered globally.** Ever. Global registration means every repo, including OSINT.

## 10. Ollama and the caching proxy

**Ollama: leave it off, and consider uninstalling.** On a MacBook it competes for exactly the resource your IDE needs — unified memory — and a model large enough to be useful for your tasks will make Cursor sluggish. Local models are worth running for: (a) high-volume classification/tagging where per-call API cost genuinely accumulates, (b) data you contractually cannot send off-machine, (c) offline work, (d) local embeddings. Nothing in your described workflow clearly hits those, and your cheap-API tier already covers the volume case at better quality. `ollama serve` idling is near-free, so the cost is mostly conceptual overhead — but that overhead is what you asked me to cut. If you keep it, keep it for embeddings only.

**The caching proxy: good idea in principle, and probably a net negative as currently deployed.** Real value: dedupes repeated identical calls from your 20 scheduled jobs, gives you the per-request log you need for question 5, and survives upstream rate limits. That logging function alone might justify it.

Pitfalls, in order of how likely they are to bite you:
- **Stale cache correctness bugs.** Cached responses to prompts whose *context* changed — a digest job re-summarizing a file that has since been edited and getting yesterday's summary. Semantic or fuzzy cache matching makes this much worse. Key on the exact full request, hash everything, and set a short TTL.
- **It's an unmonitored single point of failure.** When it dies, every route dies, and you'll debug it as a model problem.
- **It's a plaintext store of your prompts and API keys** on disk, unencrypted by default, and probably not in your backup exclusions.
- **It masks the degradation you need to see.** A cached success can hide that the upstream free model has been deprecated for a week.
- **Cache-hit rates on genuinely varied dev work are low** — often under 10%. Measure yours. If it's below ~15%, the proxy is not earning its keep as a cache.

**Verdict:** keep it, but re-scope it. Its job is *logging and observability*, with caching as a bonus. If it can't produce your cost-per-model report, replace it with something that can.

## 11. Top 10 fixes, ranked

1. **Move the HITL production guarantee out of the rules file and into the tool layer** (typed confirmation or human-supplied credential). Your one hard constraint is currently enforced by a model reading line 400 of 770. Everything else on this list is optimization; this is the one that prevents an unrecoverable day.
2. **Cut always-on rules from ~1,400 lines to ≤200 per repo.** Biggest immediate gain in agent quality, cost, and your own ability to reason about behavior. Diff the three alwaysApply files for contradictions while you're in there.
3. **Delete `prod-mcp` from all config and separate prod credentials from the ingest/OSINT environment.** Untrusted text and production write access must not share a session.
4. **Audit the 20 LaunchAgents against "when did a human last act on this?" and cut to 6–9,** consolidating digests into one morning artifact.
5. **Add one health-check job** that reads every remaining job's heartbeat and reports staleness into the morning summary. One job replaces all per-job monitoring.
6. **Cancel one of Cursor Pro / Claude Max, and one search API.** Trial by removal for 30 days, not by debate. Largest real cost reduction available, with no quality loss you'll notice.
7. **Collapse the three lifecycle labels to a single 4-state `status` field, pick one canonical ID space, and write the K# mapping to one flat file.** An afternoon; removes a recurring daily tax.
8. **Collapse the routing chain from four tiers to two** — cheap for summarize/extract/classify, frontier for code/reasoning — routed on task type, not perceived difficulty.
9. **Triage the 145 wiki pages in one time-boxed session**; archive by default, promote 5–15 to skills, and drop the `policy_wired` tag. Audit the 26 skills for actual invocation while you're there.
10. **Hoist duplicated rules to user level, empty `.cursor/` in inactive repos, and add a monthly one-screen drift report** across whatever remains.

Deliberately **not** on this list: building a routing evaluation harness, a config sync system, or a skills registry. All three are the kind of thing that feels like progress and adds surface area. Do 1–10 first; most of the need for them will evaporate.

## 12. The strongest case that this is over-engineered

The honest version, stated as an adversary would:

**You have built a platform for an organization that doesn't exist.** Nearly every component in this inventory is a *coordination* technology — lifecycle labels, ID spaces, policy tagging, per-repo config, tiered routing, audit artifacts. Coordination technology solves problems caused by many people, turnover, and unshared context. You are two people who can resolve any ambiguity by turning around. The taxonomy that would save a 30-person team weeks costs a two-person team pure overhead, because you pay all the maintenance and receive none of the benefit.

**The tell is the ratio.** Six-plus audit artifacts and 145 wiki pages against 26 skills and an unknown number of working jobs. When the meta-work outweighs the work, the system has become the project. The confusion you report — leftovers, dual IDs — is not a bug in the taxonomy; it is the taxonomy's cost showing up on the bill.

**Second tell: cost optimization inverted against your real scarcity.** A four-hop chain to shave dollars off easy tasks, while paying for two or three overlapping frontier subscriptions and spending human hours maintaining the chain. You optimized the cheap resource and ignored the expensive one, which is the two of you.

**Third tell: 28 repos, 20 jobs, 145 pages — none of these numbers were chosen.** They accreted. Systems that accrete never shrink without a deliberate deletion event, and there is no evidence one has happened here.

**A deliberately minimal version:**

- **3–5 active repos** in the agentic load path. The rest are archives you open when needed, with empty `.cursor/`.
- **One `~/.cursor/rules` file, ~100 lines,** shared via dotfiles. Per-repo rules only where genuinely repo-specific, ~50 lines, agent-requested where possible.
- **One frontier subscription. One cheap API. One search API.** Two tiers of routing, chosen by task type.
- **One scheduled job:** a morning brief that includes digests, ingest results, and job health. Plus whatever the trading workflow genuinely requires on its own schedule.
- **One status field, four states.** No phases, no dual IDs, no policy tags.
- **Zero MCP servers with production write access registered globally.** Prod work happens in a separate environment with a human-supplied credential.
- **The wiki as a personal notebook** with no pretense of being infrastructure, and ~30 pages that you actually reread.
- **HITL enforced in code**, not prose.

That version does everything your daily workflow describes — morning summary, digests, ingest, routing, prod briefs, trading — at maybe a third of the cost and a tenth of the cognitive load.

The strongest counter-argument, which I'll grant: some of this is deliberate practice, and building the federation is itself an objective. That's a fine reason. But then say so explicitly, and stop measuring it by usability and cost — because by those measures it is losing, and the audit artifacts you keep generating are the system telling you so.

## Analysis

**Consensus**

- The ~1,400 lines of alwaysApply rules (770+311+319) are indefensible; always-on context must be cut hard and reserved for short, universal, safety-critical invariants, with everything conditional moved to on-demand/agent-requested docs and narrative/history to the wiki
- Symptoms of always-on bloat are behavioral: rules partially ignored despite being present, generic or policy-dominated output, inconsistent behavior across sessions, rising cost/latency with no quality gain
- Multiple of the 20 LaunchAgents are almost certainly failing silently or producing output nobody consumes; consolidate into far fewer jobs, add logging plus an unignorable failure signal, and delete any job with no named human consumer
- Retire Phase-0/Phase-1/policy_wired in favor of a single lifecycle status field with one canonical ID space; keep K# as a lookup/alias via a mapping file or registry rather than doing a mass rewrite, and freeze creation of new labels/IDs immediately
- Cost-savings claims from tiered routing are untrustworthy unless measured as cost per accepted result including retries, escalations and human review time; the operators' attention, not API dollars, is the scarce resource
- The multi-hop routing chain is over-engineered for the money at stake and should be collapsed to fewer tiers; cheap/free models are near-parity for summarization/extraction/classification but not for multi-file agentic coding, where frontier models remain necessary
- Advertised long-context windows are not evidence of reliable recall on cheap models
- Subscriptions overlap materially: at most one frontier chat/CLI subscription is justified alongside the agentic IDE, one search API should be cancelled, and every paid service needs a named recurring workflow to survive
- 28 per-repo .cursor/ configs should follow a global-baseline / per-repo-delta split: universal safety and cross-repo MCPs at user level, only build/test commands, architecture and repo-specific MCPs per repo; delete copied global policy
- Zero basename overlap between 145 wiki pages and 26 skills shows the documentation and execution layers are decoupled and the tag is aspirational; triage by promoting only a handful of genuinely repeatable procedures to tooling, keeping a small reference set, and archiving the large majority out of the active/AI-visible path
- Local MCP servers, tunnels and proxies on a machine with production access create serious ambient-authority risk; require default-off/read-only, least-privilege and expiring credentials, time-limited tunnels closed after use, an inventory of what is running and listening, and version pinning of MCP servers
- A per-project 'disabled' flag (prod-mcp) is not a real control; disabled servers must be genuinely stopped or removed from the config path so they cannot be re-enabled accidentally
- Keep Ollama off on this laptop: no described workload justifies competing with the IDE for unified memory when cheap APIs are better quality
- The audit/report artifacts (super-audit, cursor-audit, free-audit, NotebookLM exports) are accumulating without producing decisions or deletions and should stop or be tied to dispositions
- The setup is over-engineered for two people, and the minimal version is roughly: one IDE, one short global rule file plus small per-repo deltas, one frontier access path, one cheap API/router, one search provider, a handful of jobs, one status field, and no persistent local model/tunnels

**Contradictions**

- **The local OpenRouter caching proxy**
  - ~google/gemini-pro-latest: Delete it; caching for AI dev work is an anti-pattern that will serve back cached hallucinations and failed generations, creating phantom bugs
  - ~openai/gpt-latest: Conditionally worthwhile: keep only if it delivers measured hit-rate savings, unified usage records, rate limiting or redaction; cache only deterministic requests with scoped keys
  - ~anthropic/claude-opus-latest: Keep but re-scope it: its real value is per-request logging/observability (needed for the routing evidence), with caching as a bonus; replace it if it cannot produce a cost-per-model report; measure hit rate and drop caching below ~15%
- **How to manage 28 .cursor/ directories**
  - ~google/gemini-pro-latest: Create a central federation-config repo and symlink or submodule the 28 .cursor/ directories to it
  - ~anthropic/claude-opus-latest: Explicitly do not build a templating/sync system — it industrializes duplication and adds a config layer; hoist shared rules to user level, empty .cursor/ in inactive repos, and use a monthly hash/line-count drift report
  - ~openai/gpt-latest: No elaborate configuration-generation framework for two people; documented baseline, small per-repo deltas, and a periodic diff report suffice
- **Which frontier subscriptions to cancel**
  - ~google/gemini-pro-latest: Keep Cursor Pro; cancel both Claude Max and Grok outright — Cursor plus OpenRouter/DeepSeek covers 99% of needs
  - ~anthropic/claude-opus-latest: The largest redundancy is Cursor Pro vs Claude Max — cancel one of the two by trial-by-removal; keep Grok only with a written justification tied to real-time trading data
  - ~openai/gpt-latest: Cursor is not replaceable by a chat subscription; keep the IDE plus the one most-used frontier subscription, and rotate the second monthly rather than holding both
- **Which search API to drop**
  - ~google/gemini-pro-latest: Cancel one; frames Exa as better for semantic/dev search and Brave as cheaper/broader without a firm pick
  - ~anthropic/claude-opus-latest: Prior: keep Brave for breadth and cheapness, drop Exa unless the research workflow specifically depends on neural retrieval
  - ~openai/gpt-latest: Keep both only if measured workflows depend on their difference; otherwise cancel one, no directional prior
- **Whether to build a routing evaluation harness**
  - ~openai/gpt-latest: Insists on a fixed real-task eval set with ~10 recorded metrics per request, re-run whenever endpoints change, before trusting any tier
  - ~anthropic/claude-opus-latest: Recommends a half-day 20–30 task eval, but deliberately excludes building a routing evaluation harness from the top-10 because it adds surface area that mostly evaporates after simplification
  - ~google/gemini-pro-latest: Minimal measurement: track first-shot success rate only; a cheap model needing one correction has already failed economically
- **Shape of the replacement state machine**
  - ~google/gemini-pro-latest: Three states: Idea → Active → Archived; drop policy_wired entirely and enforce policy at the execution layer
  - ~openai/gpt-latest: Five states: PROPOSED → ACCEPTED → IMPLEMENTED → VERIFIED → RETIRED, with BLOCKED as a flag and object type as a separate field
  - ~anthropic/claude-opus-latest: Four states: draft | active | deprecated | archived, archiving as a physical directory move, plus an optional hitl_required boolean
- **Handling legacy K#/Phase tags during migration**
  - ~google/gemini-pro-latest: Run a one-time script to convert all K# dual IDs to standard names and delete the old tags
  - ~openai/gpt-latest: Do not mass-rename; add aliases in a registry, mark ambiguous mappings NEEDS_REVIEW, migrate opportunistically
  - ~anthropic/claude-opus-latest: Leave old tags in place as dead text; add a lint that fails only on new Phase-* tags, and delete unmissed archived items after 30 days
- **Free-tier models' usefulness for code**
  - ~google/gemini-pro-latest: Free models are useless for code generation; drop the free tier entirely
  - ~anthropic/claude-opus-latest: Free/cheap models are fine for boilerplate, single-function edits, test scaffolds and format conversion, but nothing touching production code paths
  - ~openai/gpt-latest: Free endpoints are acceptable for disposable, automatically verifiable work but are poor dependencies for time-sensitive workflows
- **Aggressiveness of the job-deletion trigger**
  - ~google/gemini-pro-latest: Delete the job if its output is unread/unacted for 3 consecutive days
  - ~openai/gpt-latest: Delete after 30 days of unconsumed output, duplication, or unnoticed repeated failure
  - ~anthropic/claude-opus-latest: Disable (not delete) for two weeks first, then delete if nothing is missed; expect to land at 6–9 jobs
- **Whether to keep the wiki at all**
  - ~google/gemini-pro-latest: Minimal version has no wiki; documentation lives in the repos next to the systems it describes
  - ~anthropic/claude-opus-latest: Keep it as a personal notebook of ~30 pages actually reread, with no pretense of being infrastructure
  - ~openai/gpt-latest: Keep it for explanations, research and institutional memory, but never as the sole source of a safety control or required procedure

**Partial coverage**

- ~openai/gpt-latest, ~anthropic/claude-opus-latest: Prompt injection is the concrete mechanism of concern: OSINT/document-ingest sessions handle untrusted text in the same agent context that can reach write-capable tools; retrieved text must never authorize sensitive tool calls
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: MCP supply-chain risk beyond permissions: servers run with full user privileges, and tool descriptions/versions can change after approval, so pin versions and review diffs
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: Test the rule cut empirically (A/B a reduced rule set on 10–30 representative tasks, or delete the 770-line file for a week and record degradation) rather than arguing about it
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: Free/cheap endpoint identity is unstable — 'Qwen'/'Kimi'/'DeepSeek' is not a routing definition; log the model actually served and alarm on unexpected tier distribution to catch silent degradation or deprecation
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: Job hygiene specifics: non-overlap locks, idempotency, timeouts, log rotation, heartbeat/last_success records, and one exception-only status report; account for missed runs while the laptop sleeps
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: An MCP server that exists only when its folder is open makes agent behavior nondeterministic depending on IDE state
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: Audit findings need an explicit disposition (accepted/rejected/superseded/open) with an owner, or they are inventory rather than remediation
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: Every remaining rule, MCP entry, job and subscription needs a named owner and a recurring, periodically re-justified use case
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: The proxy/cache is an unmonitored single point of failure and a plaintext store of prompts and API keys on disk
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: Cheap-model summarization is deceptively lossy (numbers, caveats, action items) even though it is the closest-to-parity task class — verify preservation, not fluency
- ~google/gemini-pro-latest, ~anthropic/claude-opus-latest: The three alwaysApply files very likely contain direct contradictions with each other and should be diffed for conflicts
- ~google/gemini-pro-latest, ~anthropic/claude-opus-latest: Failure notification should be a local, unavoidable channel (macOS notification via osascript, or prepended to the morning brief) rather than silent logs or email
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: Separate production credentials from ordinary dev/ingest credentials with least privilege (e.g. fine-grained GitHub PAT scoped to active repos), and require approval at the final irreversible operation
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: Route by consequence of error and task type rather than by a per-request subjective 'difficulty' judgment
- ~openai/gpt-latest, ~anthropic/claude-opus-latest: A single authoritative inventory/registry (services, MCPs, tunnels, credentials, jobs, subscriptions, IDs) is the artifact that resolves 'what is authoritative and what is running'

**Unique insights**

- ~google/gemini-pro-latest: Move recurring digests off the laptop entirely to a lightweight cloud function, or run them manually on wake, rather than scheduling them locally
- ~google/gemini-pro-latest: Physically move disabled-by-default MCP configs out of the .cursor path so an agent editing config cannot re-enable them
- ~google/gemini-pro-latest: Tunnels should require a manual human command to open with a hard auto-timeout (e.g. one hour)
- ~openai/gpt-latest: Impose a temporary moratorium on new rules, skills, MCPs, jobs, subscriptions and audit documents until the existing estate is reduced — otherwise the audit itself becomes another artifact
- ~openai/gpt-latest: Separate the axes explicitly: object type (policy/skill/job/service/report) is a field, BLOCKED is a flag, and neither belongs in the lifecycle state; 'policy_wired' failed because it was both a category and a maturity state
- ~openai/gpt-latest: Mark ambiguous legacy ID mappings NEEDS_REVIEW rather than guessing, and let the registry be authoritative while filenames and tags are merely indexes
- ~openai/gpt-latest: 'Localhost' is not an access-control policy — require authentication on local MCP/proxy listeners and restrict filesystem roots
- ~openai/gpt-latest: Rotate the second frontier subscription month-to-month instead of holding both continuously, and apply a quarterly 'would we buy this again today?' test
- ~openai/gpt-latest: Cache-key correctness detail: scope entries by user/project/model/configuration and expose the true upstream endpoint in logs, since caching can also alter streaming/tool-call behavior
- ~openai/gpt-latest: Success criterion framing: either operator should be able to answer four questions quickly — what is authoritative, what is running, what can write, what is worth paying for
- ~openai/gpt-latest: An intermediary hop like 'OpenCode Zen' must justify itself with a measurable quality, cost, privacy or workflow benefit; another hop is not itself a benefit
- ~anthropic/claude-opus-latest: Diagnostic framing: every inventory item is a producer and almost nothing is described as a consumer with an owner and a decision it feeds — that asymmetry is the disease and everything else is a symptom
- ~anthropic/claude-opus-latest: The 'leftover' items were never in either phase bucket because the taxonomy was invented after the work started, and the K# dual ID is the fossil record of a half-finished renumbering — so the labels cannot be repaired, only retired
- ~anthropic/claude-opus-latest: Move the HITL production guarantee out of prose rules into the tool layer (typed confirmation or a human-supplied credential) so it survives deletion of the rules file — ranked as the single highest-leverage fix
- ~anthropic/claude-opus-latest: Delete prod-mcp from config entirely and keep the snippet in a password manager: friction is the feature; a disabled entry is a loaded gun with the safety on
- ~anthropic/claude-opus-latest: Consider a separate macOS user account (or at minimum separate shell/keychain) for prod work, so ingest/OSINT sessions cannot reach prod write credentials
- ~anthropic/claude-opus-latest: Concrete verification step: run launchctl list | grep cemini and inspect nonzero exit statuses; expect 3–6 broken agents, and note LaunchAgents inherit a minimal PATH that breaks node/python/uv
- ~anthropic/claude-opus-latest: Do the job audit before adding observability, or you will instrument jobs you are about to delete
- ~anthropic/claude-opus-latest: Add one health-check job that reads all remaining jobs' heartbeats into the morning summary, replacing per-job monitoring; also set Nice values so ingest does not compete with the IDE
- ~anthropic/claude-opus-latest: Make deprecation opt-out: bulk-archive all 'leftover' items and require the other operator to argue an item back to active
- ~anthropic/claude-opus-latest: 28 repos in the agentic load path is itself the finding — realistically 5–8 are active; empty .cursor/ in the rest instead of maintaining rules for repos touched twice a year
- ~anthropic/claude-opus-latest: User-level rules are untracked and invisible to the second operator; keep ~/.cursor/rules in a shared dotfiles repo so both can diff it
- ~anthropic/claude-opus-latest: Audit the 26 skills for actual invocation too — the disjunction cuts both ways and roughly a third of the skills are probably dead
- ~anthropic/claude-opus-latest: Long-context tactic: prefer retrieval over dumping 100k tokens into a cheap model, and place the question at both the start and end of the prompt
- ~anthropic/claude-opus-latest: Rule-of-thumb filter: if you cannot name the specific bad output a rule line prevents, it is documentation, not a rule
- ~anthropic/claude-opus-latest: Explicit anti-list of tempting non-fixes (routing eval harness, config sync system, skills registry) that feel like progress but add surface area
- ~anthropic/claude-opus-latest: Grants the strongest counter-argument: if building the federation is itself the objective (deliberate practice), that is legitimate — but then stop judging it by usability and cost, because on those metrics it is losing

**Blind spots**

- No backup, snapshot or rollback plan before the recommended deletion event — 28 repo configs, 145 wiki pages and 20 agents are about to be cut with no stated way to restore if the reduced rule set or archived pages turn out to be load-bearing
- No treatment of the trading workflow's specific irreversibility risk beyond generic HITL: no kill switch, position/size limits, dry-run mode, immutable audit trail of executed actions, or what happens if a scheduled job fires an order while the laptop is unattended
- Data confidentiality and provider terms are unexamined: free-tier OpenRouter routes commonly log or train on prompts, so routing proprietary code, ingested documents or OSINT material to the free tier may be a disclosure problem independent of quality
- No actual spend baseline: none of the responses estimated current monthly cost per service or proposed per-provider billing alerts/hard spend caps, yet all three recommend cancellations on cost grounds
- macOS platform security is absent: FileVault, Full Disk Access/TCC grants held by agents and MCP servers, keychain access scoping, and laptop loss/theft exposure for a device holding prod credentials and tunnels
- Two-operator coordination is not designed: no ownership split, no decision protocol for disagreements, no bus-factor/handoff plan if one operator is unavailable, despite 'owner' being required on every artifact
- No verification-first step that converts the unverifiable self-reported inventory into machine-readable evidence (config hashes, launchctl exit codes, listening ports, billing exports) before acting on any recommendation
- Cursor-specific mechanics are asserted rather than measured: no one proposes measuring the actual token footprint of rules, checking rule precedence/truncation behavior, or reviewing .cursorignore/indexing scope
- Provider concentration risk after consolidation: cancelling the second frontier subscription and the second search API leaves no fallback for an outage, rate-limit change, price rise or account suspension
- No mechanism to prevent re-accretion beyond a monthly review — no budget caps on rule lines, job count, repo count or subscriptions enforced by tooling
- Human-time instrumentation is never proposed even though 'cognitive overhead' and 'cost per accepted result' both depend on it; the operators are asked to price their attention without measuring it

# SUPER AUDIT — Cemini Federation AI Harness
**Reviewer stance:** adversarial, readonly. **Date:** 2026-09-02
**Panel:** 3 independent frontier models consulted (consensus + dissent recorded below).

## Scope caveat (read first)
I have **no filesystem, launchctl, billing, or MCP access**. Every count in the brief (28 repos, 770 lines, 145 pages, 20 agents, 26 skills, "zero basename match") is **operator-self-reported and unverified**. The panel independently flagged the same thing: *acting on an unverified inventory is how you delete something load-bearing.* So §0 below is mandatory before any fix lands, and every recommendation is tagged `[VERIFIED-BY-OPERATOR-FIRST]` where it depends on a count I cannot see.

Second caveat the brief did not ask for and needs: **there is no stated backup/rollback plan, no trading kill-switch, no spend baseline, and no data-retention analysis for free-tier routing.** Three of four are, in my judgement, higher severity than anything in questions 1–12.

---

## §0 — Verify-first block (30 minutes, do before fix #1)

```bash
# 0a. ROLLBACK ANCHOR — do this first, nothing else is safe without it
cd ~/ && git -C <federation-root> tag pre-audit-2026-09-02 && git -C <federation-root> push --tags
tar -czf ~/Desktop/preaudit-cursor-configs.tgz $(find ~ -maxdepth 4 -type d -name .cursor 2>/dev/null)
cp -R ~/Library/LaunchAgents ~/Desktop/preaudit-launchagents
# wiki: snapshot the whole tree before any archive move

# 0b. Which LaunchAgents are actually dead? (nonzero col 2 = last exit status)
launchctl list | grep cemini
for f in ~/Library/LaunchAgents/com.cemini.*.plist; do echo "== $f"; \
  /usr/libexec/PlistBuddy -c "Print :StandardErrorPath" "$f" 2>/dev/null || echo "NO STDERR PATH"; done

# 0c. Real always-on context cost, per repo
find ~ -maxdepth 4 -path "*/.cursor/rules/*" -name "*.mdc" -exec sh -c \
  'printf "%s\t%s\t%s\n" "$(wc -l < "$1")" "$(grep -c alwaysApply "$1")" "$1"' _ {} \;

# 0d. Drift: identical rule files copied across repos
find ~ -maxdepth 4 -path "*/.cursor/*" -type f -exec md5 -r {} \; | sort | uniq -D -w32

# 0e. What is listening / what can reach the internet
lsof -iTCP -sTCP:LISTEN -P -n | grep -v Chrome
ps ax | grep -Ei 'ngrok|cloudflared|ssh -R|ollama|proxy' | grep -v grep

# 0f. Spend baseline — export last 60d invoices from all providers to one CSV. You have no cost number today.
```

If 0b returns fewer than 3 nonzero exits, the panel's central prediction is wrong and you should discount fix #4 accordingly.

---

## Verdict table

| # | Area | Verdict | Core finding | Evidence status |
|---|---|---|---|---|
| 1 | Daily workflow | 🟠 **Orchestration tax** | The day is producer-heavy: summary → digests → ingest → route → prod briefs → trading. Almost no step has a *named consumer and a decision it feeds*. Friction is not tooling; it's "where does this task go" deciding-cost, paid per task, twice per day, by two people. | Inferred |
| 2 | 28 `.cursor/` workspaces | 🔴 **Over-provisioned** | 28 repos in the agentic load path for 2 operators is itself the finding; realistically 5–8 are active. Rules/MCP are near-certainly duplicated with drift (fix one bug, 27 copies keep it). | `[VERIFY 0c/0d]` |
| 3 | Context tax | 🔴 **Indefensible** | ~1,400 alwaysApply lines before file context, MCP schemas, or conversation. At that size you almost certainly have **direct contradictions between the 770-line wire file and the 311/319 project rules** — which shows up as "inconsistent across sessions," not as an error. You believe constraints are enforced; they are advisory. | `[VERIFY 0c]` |
| 4 | Phase-0/1/policy_wired | 🔴 **Unrepairable, retire it** | Three labels answer three different questions (when built / is governed / does it work). "Leftovers" were never in either bucket — the taxonomy was invented *after* the work started. The dual-ID K# is the fossil of a half-finished renumbering. Cannot be fixed by better definitions. | Strong panel consensus |
| 5 | Route chain | 🔴 **Optimizing the cheap resource** | A 3-hop easy tier exists to shave dollars off tasks that are cheap by definition, while 2–3 frontier subscriptions run in parallel. **Answer to "should OpenCode replace DeepSeek Flash on easy": no — delete the hop instead.** Every hop = latency + a silent-failure surface. | Consensus |
| 6 | Subscriptions | 🟠 **Redundant, unmeasured** | Largest genuine overlap is Cursor Pro ↔ Claude Max (both = "frontier model edits my repo"). Second: Exa ↔ Brave. Panel split 3 ways on *which* to cut — that split is itself the finding: **decide by trial-by-removal, not by debate.** | `[VERIFY 0f]` |
| 7 | Wiki (145 / 26 / zero match) | 🟠 **Aspirational tag** | Zero basename overlap is near-proof no execution path reads those pages. `policy_wired` marks *intent to wire*, not wiring. The disjunction cuts both ways: audit the 26 skills for invocation too — expect ~1/3 dead. | `[VERIFY: grep skill names in logs]` |
| 8 | Research reports | 🔴 **Analysis inventory** | super-audit / cursor-audit / free-audit / notebooklm packs with no disposition section = entertainment, not audit. They likely contradict each other. **This document included** — it is worthless unless §"Top 10" gets accept/reject/defer marks by end of week. | Consensus |
| 9 | MCP | 🔴 **Highest unbounded risk** | `prod-mcp` "disabled in mcp.json" is a **comment, not a control** — one edit / one merge / one agent config-write away, and it constrains nothing outside that project. `lazy-tool` off-when-folder-closed makes agent capability a function of *window state* — nondeterministic. You ingest untrusted text (OSINT, documents) in sessions that can reach write tools. That is the lethal trifecta. | Consensus, high confidence |
| 10 | Grok bots | 🟡 **Fine, justify or cut** | `~/.grok` with tradingview MCP disabled is the right posture. The open question is not config, it's whether Grok earns a third frontier line item. Only defensible answer: real-time social/market data for trading — write that justification down or cancel. | Inferred |
| 11 | LaunchAgents | 🔴 **Silent failure estate** | 20 jobs ≈ 4× the described workflow. LaunchAgents miss runs on lid-close, break on minimal-PATH `node`/`python`/`uv`, and a job erroring for weeks looks identical to a healthy one without `StandardErrorPath` + someone reading it. | `[VERIFY 0b]` |
| 12 | Laptop | 🟡 **Mostly right already** | Ollama off = correct, keep it off (nothing in this workflow hits the 4 local-model justifications; it competes for the unified memory Cursor needs). Cache proxy = **panel's only real fight** (see dissent). Tunnels = the single highest-severity item in the inventory if any lack auth or outlive their task. | `[VERIFY 0e]` |
| — | **Unasked: trading irreversibility** | 🔴 **Gap** | HITL-on-prod is stated but there is no kill switch, no position/size cap, no dry-run mode, no immutable execution log, and no answer to *"what happens if a scheduled job fires an order while the laptop is unattended."* | Not in brief |
| — | **Unasked: free-tier data terms** | 🟠 **Gap** | Free OpenRouter routes commonly log/train on prompts. Routing ingested documents, OSINT material, or proprietary code there is a **disclosure** problem independent of quality. | Not in brief |

### Recorded dissent (do not let me hide this behind consensus)
- **Cache proxy:** one model says *delete it* (caching AI dev calls serves back stale/hallucinated generations as phantom bugs); one says *conditional on measured hit-rate*; one says *keep but re-scope to logging.* **My call:** turn caching **off**, keep the process **as the per-request logger** you need for fix #8, and re-enable caching only if measured hit-rate >15%. Cache-key must include model+project+config, TTL short.
- **28 configs:** one model wants a central config repo with symlinks/submodules; two say *do not build a sync system — it industrializes duplication.* **My call:** no sync system. Hoist to user level, empty the inactive ones, monthly hash report. A symlink farm means one bad edit hits 28 repos simultaneously.
- **Which subscription dies:** cancel-both-Grok-and-Max / cancel-one-of-Cursor-or-Max / keep-IDE-and-rotate-the-second-monthly. Unresolvable without §0f. **Use the matrix below.**
- **Free tier for code:** "useless for code" vs "fine for boilerplate/tests." **My call:** free tier for summarize/extract/classify only; nothing touching a production code path.

---

## Top 10 fixes (ranked by unrecoverable-damage-prevented, then by daily tax removed)

| # | Fix | Actionable step | Effort |
|---|---|---|---|
| **1** | **Move HITL out of prose and into the tool layer** | Your one hard constraint is currently enforced by a model reading ~line 400 of 770. Make the prod write path require a typed confirmation string **or** a credential only a human pastes at call time. Then it survives fix #2 deleting the rules file. Add to the same layer: trading kill-switch file (`~/.cemini/TRADING_HALT` → any order path exits non-zero if present), max position size, `--dry-run` default. | 1 day |
| **2** | **Delete `prod-mcp` from all `mcp.json`; separate prod credentials by blast radius** | Remove the entry entirely — keep the snippet in your password manager and paste it when needed. *Friction is the feature.* Then: prod write creds must not be reachable from the shell/keychain that runs ingest/OSINT (separate shell profile minimum, separate macOS user account ideally). Scope the github MCP to a fine-grained PAT covering only active repos. No globally-registered server may hold prod write. Ever. | 1 day |
| **3** | **Cut alwaysApply from ~1,400 → ≤200 lines/repo** | `git mv .cursor/rules/cemini-phase1-policy-wires.mdc .cursor/rules/cemini-wires.reference.mdc`, strip `alwaysApply: true`, add `description:` so the agent can request it. Same for the 311/319 files: convert to glob-scoped or description-triggered. **Diff the three for contradictions while you're in there.** Keep always-on to: HITL invariant, no-secrets, read-only default, 3–5 non-obvious conventions, one-line index of on-demand docs. Filter: *if you cannot name the specific bad output a line prevents, it is documentation.* Test by deleting the 770-line file for a week and recording actual degradation. | 3 h |
| **4** | **Audit the 20 LaunchAgents on "when did a human last act on this?"** — cut to 6–9 | Use §0b. For each: never / can't recall / >30d → `launchctl bootout` for two weeks (**disable, don't delete**). Nothing missed → delete. Consolidate the three-ish digest jobs into one morning artifact with three sections, since you read them at one time. Do this *before* adding observability or you'll instrument jobs you're about to delete. | 2 h |
| **5** | **Add exactly one health-check job** | Every surviving job writes `~/.cemini/heartbeat/<job>.json` with `last_success`; each gets `StandardErrorPath`, a `flock` lockfile (overlapping ingest is a classic duplicate-wiki-page cause), a timeout, and a `Nice` value so it loses to Cursor. One new agent reads all heartbeats and **prepends stale/failed jobs to the morning summary**. Silent logs are not notification. This single job replaces per-job monitoring. | 3 h |
| **6** | **Collapse the lifecycle to one field** | See one-page proposal below. Afternoon of work; removes a recurring daily tax and the "leftover"/K# confusion permanently. | 4 h |
| **7** | **Collapse routing 4 tiers → 2, routed on task type not perceived difficulty** | Cheap tier (one model + one fallback) for summarize/extract/classify/format — this is where your real savings are, because your whole morning is that. Frontier for code and reasoning. **Delete the OpenCode Zen hop** unless it can show a measurable quality/cost/privacy/workflow win; another hop is not itself a benefit. Log the model *actually served* (not intended) and alarm on unexpected tier distribution — otherwise free-tier deprecation presents as "the assistant got dumber lately." Route by *consequence of error*, not difficulty. Add a rule: no ingested/OSINT/proprietary content to free-logged endpoints. | 4 h |
| **8** | **Cancel one of {Cursor Pro, Claude Max} and one of {Exa, Brave} by trial-by-removal** | Do §0f first. Then 30-day removal trial, not a debate — the panel could not agree, which means you can't either. Put Grok on notice with a written trading-data justification. Set **hard spend caps + billing alerts** on every remaining API (you currently have none). | 1 h + 30 d |
| **9** | **Time-boxed wiki triage, archive-by-default** | Both operators, one sitting, 30 s/page. Promote → only procedures executed 3+ times (expect 5–15 → skills, hand-written, no auto-evolve). Keep → consulted in last 90 days (expect 20–40). Archive → everything else (expect 90–120) into `wiki/archive/`, out of every index and out of the AI-visible path. Then **drop the `policy_wired` tag entirely** and audit the 26 skills for actual invocation. Deprecation is **opt-out**: the other operator must argue an item back. | 3 h |
| **10** | **De-duplicate `.cursor/` and shrink the load path** | Move universal rules + cross-repo MCPs (stash/github/atto) to `~/.cursor/rules/` — and keep that directory **in a shared dotfiles repo**, since user-level rules are otherwise invisible and untracked for the second operator. Empty `.cursor/` in the ~20 inactive repos. Add a monthly one-screen drift report (§0d, hashes + line counts + alwaysApply flags). Fix `lazy-tool`: make availability explicit, not a side effect of window state. **No templating/sync system.** | 3 h |

**Deliberately NOT on this list** (feels like progress, adds surface area): a routing eval harness, a config sync/templating system, a skills registry, more rules. Do 1–10; most of the need evaporates. Also: **impose a moratorium** on new rules, skills, MCPs, jobs, subscriptions, and audit documents until the estate shrinks — otherwise this audit becomes artifact #7.

---

## Simplify Phase-0 / Phase-1 / policy_wired — one page

**Diagnosis.** Three labels because three questions got conflated: *when was this built* (Phase-0/1 — historical, unactionable), *is it governed* (`policy_wired`), *does it work* (unlabelled). `policy_wired` failed specifically because it is simultaneously a **category** and a **maturity state**. "Leftovers" exist because the taxonomy postdates the work. The dual-ID K# is a half-finished renumbering. **None of this is repairable by redefinition — retire it.**

**The one mental model.** One field. Four states. One canonical ID space.

```yaml
id: CEM-0142            # canonical, opaque, sequential, never reused
status: active          # draft | active | deprecated | archived
type: policy            # policy | skill | job | service | report   <- separate axis
hitl_required: true     # boolean, separate axis (replaces policy_wired entirely)
legacy: [K37, PHASE1-K37]   # inert lookup aliases, nothing branches on these
```

- `draft → active` — an operator used it successfully at least once.
- `active → deprecated` — superseded; present, do not extend.
- `deprecated → archived` — **physically moved** out of the load path (a directory move, not a tag), so the agent cannot see it.
- Only backward transition: `deprecated → active`, with a written reason.
- `blocked` is a **flag**, not a state. Object type is a **field**, not a state. Phase is an **inert annotation** (`created_phase: 0|1`) that nothing reads.

**Migration — one afternoon, no mass rewrite.**
1. **Freeze today.** Verbally, between the two of you: no new `Phase-*` tags, no new K#. This is the whole fix; everything below is cleanup.
2. **Pick the canonical ID space** — the one referenced by more *live code*, not the prettier one. The other becomes an alias.
3. **One flat file** `~/cemini/ids.csv`: `canonical_id,k_id,legacy_id_b,title,type,status,owner,location`. Ambiguous mappings get `status=NEEDS_REVIEW` — **do not guess.** The CSV is authoritative; filenames and tags are indexes.
4. **Bulk-assign:** everything currently loaded and in use → `active`. Everything "leftover" → `archived`. Opt-out, not opt-in.
5. **Do not mass-edit old tags.** Leave them as dead text. Add one lint that fails only when a `Phase-*` tag or bare K# appears in a **new** file.
6. **30 days later:** anything still `archived` and unmissed gets deleted; `ids.csv` is the only trace.

**Operator-facing rule (put this in the ≤200-line always-on file, verbatim):**
> Everything has one ID (`CEM-####`) and one status (`draft/active/deprecated/archived`). Governance is the `hitl_required` boolean. There are no phases. If you find a K# or a Phase tag, look it up in `ids.csv` and do not propagate it.

**Success test:** either operator, cold, can answer in under 10 seconds — *what is authoritative, what is running, what can write, what is worth paying for.*

---

## Subscription matrix

| Service | Overlaps with | Verdict | Trigger / one-time step |
|---|---|---|---|
| **Cursor Pro** | Claude Max (heavy) | **Keep pending trial** — the agentic-IDE surface is not replaced by a chat/CLI subscription; 28-repo indexing lives here | Run the 30-day removal trial on Max first, not on Cursor |
| **Claude Max** | Cursor Pro (heavy) | **Trial-by-removal, 30 d** — largest genuine redundancy and likely a top-2 line item | Cancel for 30 d; log every time you reach for it and can't. If <5 times, done |
| **Grok (xAI)** | Cursor + Max as "mid tier" | **Justify in writing or cut** — a third frontier sub as the middle tier is the easiest thing to absorb into either neighbour | Sole defensible case = real-time social/market data for trading. Write it down in `ids.csv` as a `service` row with an owner, or cancel |
| **DeepSeek API** | OpenRouter (can serve the same models) | **Keep one as primary** — direct is marginally cheaper, one less hop | Pick primary; keep the other as failover only. Prepaid credits are fine; the *routing complexity of using both* is not |
| **OpenRouter** | DeepSeek direct | **Keep** — breadth + failover + consolidated billing | Set a hard spend cap. Log served-model. Exclude ingested/OSINT/proprietary content from free-logged routes |
| **Exa** | Brave (substantial) | **Cut one — panel leans Exa unless neural retrieval is load-bearing** | Name 3 real queries where Exa clearly beat Brave. Can't? Cancel and re-add if you feel the loss |
| **Brave Search** | Exa | **Keep** (breadth, cheapness) — assuming Exa goes | — |
| **"etc." smaller subs** | unknown | **Presume cancellation** | Each needs an owner, a monthly-used recurring workflow, and a replacement cost. No entry in `ids.csv` → cancel |
| **Ollama (free)** | cheap API tier | **Stay off / consider uninstall** | Keep only if you move embeddings local |

**Standing rule:** every paid service gets an owner, a named recurring workflow, and a quarterly *"would we buy this again today?"* vote. **Concentration risk note:** after cutting the second frontier sub and the second search API you have no fallback for an outage, rate-limit change, or account suspension — accept that consciously, and keep one prepaid credit balance elsewhere as the escape hatch.

---

## Free-utility wins (real parity, not cope)

| Win | Why it's genuinely same-tier | Step |
|---|---|---|
| **Push the entire morning stack to the cheap/free tier** | Summarize / extract / classify is the one task class where cheap ≈ frontier. Your day is *made of* this. This is where the savings actually are. | Route morning summary + digests + ingest tagging to one cheap model; frontier only for prod briefs |
| **…but verify preservation, not fluency** | Cheap summarization is *deceptively lossy* — drops numbers, caveats, dissent, action items while reading beautifully | Spot-check 5 digests/week against source for numeric + action-item fidelity |
| **Local embeddings** | Free, fast, and quality-adequate for retrieval | Only defensible reason to keep Ollama installed |
| **Retrieval instead of long-context dumping** | Advertised context windows are marketing; cheap-model recall degrades sharply mid-document | Chunk + retrieve rather than 100k-token dumps. Put the question at both start **and** end of the prompt |
| **Deleting the 770-line always-on file** | The largest per-request cost reduction available, and it *improves* adherence | Fix #3 — costs nothing, saves tokens on every single turn |
| **`launchctl` + `flock` + `osascript` + a heartbeat CSV** | Replaces any paid monitoring/observability tool at this scale | Fix #5 |
| **Trial-by-removal as the decision procedure** | Free, and settles arguments three frontier models could not | Fixes #8 |
| **`git tag` + `tar` snapshot** | Free rollback insurance for a deletion event of this size | §0a — **do not skip this one** |

---

## Closing adversarial note

The strongest case against this entire estate, which I'll put plainly because the panel converged on it independently: **you have built coordination technology for an organization that does not exist.** Lifecycle labels, dual ID spaces, policy tagging, 28 per-repo configs, four-tier routing, six audit artifacts — all of it solves problems caused by many people, turnover, and unshared context. You are two people who can resolve any ambiguity by turning around. You pay all of the maintenance and receive none of the benefit. The confusion you reported is not a bug in the taxonomy; **it is the taxonomy's cost arriving on the bill.** And you optimized the cheap resource (API dollars on easy tasks) while ignoring the expensive one (two operators' attention).

The one legitimate counter-argument: if building the federation *is itself* the objective — deliberate practice — that's a fine reason. But then say so explicitly and stop grading it on simplicity, utility, and cost, because on those three metrics it is losing, and the audit packs you keep generating are the system telling you so.

**This document is artifact #7 until you mark each of the Top 10 `accepted | rejected | deferred` with an owner and a date.** Do that before you do fix #1.