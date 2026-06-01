# Lessons

A running log of lessons learned while managing this workspace. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

---

## 2026-06-01 — New Polymarket order-path repos must inherit CeminiSuite CLOB V2 stack on day one

World Cup Bot shipped with **`py-clob-client` V1** in `[live]` while CeminiSuite and the OSINT wiki already pinned **`py-clob-client-v2`** (Apr 2026 cutover). Shadow Phase 1 on **cemini-prod** (`DRY_RUN=true`) never POSTed orders, so preflight reported PASS and Bugbot/architect passes missed it until **egress-fi** ran the first live `plan` → `order_version_mismatch`.

**Why the gates failed:**
- Preflight checked V1 import until patched.
- Bugbot = static diff review (exports, kill-switch, etc.) — not cross-repo dependency parity.
- `/obsidian-architect` closed Bugbot items; no “match CeminiSuite Polymarket stack” checklist item.
- `LESSONS.md` had no CLOB V2 line to trigger on “double-check lessons.”

**Fix shipped:** `7054500` V2 migration + `check_clob_v2_import.py` + preflight `py_clob_client_v2` when `DRY_RUN=false`; egress live plan verified 2026-06-01.

*Apply*: Any new repo with Polymarket **order POST** must (1) declare `py-clob-client-v2` in `[live]`, (2) pass `check_clob_v2_import.py` in CI, (3) run one **`DRY_RUN=false` plan smoke** on non-US egress before shadow/live sign-off — not only monitor dry-run. **Checklist (architect hub):** `@osint-wiki/projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md`. Cross-check `@concepts/polymarket-retail-trading-discipline.md` and `CeminiSuite/services/polymarket_clob_v2_adapter.py` before calling a bot “launch ready.”

---

## 2026-05-13 — OpenSpec produces well-tested code but doesn't validate spec-vs-production alignment

K42 OpenSpec adoption pilot, Phase-2: 4 of 5 sprints landed (Sprints 1-4, 105/105 tests pass, harmfulness-audit gate verified end-to-end against the bundled policy). At the Sprint 5 (rollout) gate, a read-only SSH probe of the actual production Conductor at `cemini-librarian:/opt/cemini/conductor/` surfaced the operational truth: **the production `ToolOrchestrator` dispatches only `kb_search` + `stash_recall` — both read-only.** None of the 8 Polymarket tools that the K37 spec + bundled `policy.yaml` enumerate (`place_order`, `withdraw`, `close_position`, `cancel_order`, `submit_research_query`, plus quote tools) exist in production yet.

Sprint 5 was decided as **DEFERRED**, not deployed. Deploying middleware that classifies every existing tool as `skip-review` would be dead infrastructure plus a confidence trap (a future dev reading "K37 reviewer-agent v2 is in production" would reasonably infer trading is gated when no gate path is firing). K37 code stays at `conductor/reviewer/` as the pilot deliverable; OpenSpec change `reviewer-agent-selective-trigger` gets a `DEFERRED.md` with the re-open trigger documented; tasks 5.1-5.5 are explicitly marked deferred with reason.

**The methodology gap**: spec-driven development as practiced in OpenSpec is **internally** rigorous — the proposal/design/specs/tasks artifact bundle validates first-try, code lands deterministic against the locked spec, tests pass on the first run. None of that **externally** validates that the tool surface enumerated in the spec exists in production. The Phase-1 + Phase-2 pilot succeeded on its load-bearing measurement objective (Opus vs Sonnet 4.6 comparative author quality + spec→code determinism) AND simultaneously shipped a fully-tested middleware for a hypothetical tool surface. Both facts are true.

The spec was authored against the K37 concept doc, which describes a **future-state** trading integration. The OpenSpec workflow does not have a hook for "verify the production code already exposes the tool surface this spec claims to gate." A hypothetical 5th artifact `grounding.md` (or a `## Production reality check` section in `design.md`) might close this — TBD whether it's worth introducing without a second instance.

**Three sub-lessons compound:**

1. **Specs need a grounding check before any "land behind feature flag" task.** The cheap version: every OpenSpec change with a Sprint that wires into a runtime path MUST include a 1-line `## Production reality check` section listing the actual import path + the actual tool/function the middleware hooks. The check is one `ssh ls /opt/.../module.py` + one `grep <hook_function>` — same shape as Phase-0 audits.
2. **Pilot-deliverable status is a valid terminal state.** Sprints 1-4 are not wasted: they're a tested + reviewable + re-openable design artifact for when the Polymarket surface lands. The OpenSpec change directory + the `conductor/reviewer/` source directory together ARE the artifact; they need to stay intact, not be deleted. The `DEFERRED.md` documents the re-open trigger so the next reader doesn't redo the design work.
3. **The OpenSpec pilot's own measurement objective succeeded independently.** Opus 4.7 and Sonnet 4.6 both produced first-try-validating bundles; Sonnet matched Opus on artifact validation while diverging on a single safety-semantic choice (missing-confidence handling) that surfaced through normal review. That is **the** load-bearing finding for adopting OpenSpec across other Cemini workstreams. The Polymarket-mismatch is orthogonal — it's a gap in *how we author specs*, not in OpenSpec itself.

*Apply*: From now on, any OpenSpec change with a runtime-wiring task (the equivalent of K37's Task 1.3 / Sprint 5.x) gets a `## Production reality check` line in `design.md` that names the target import path + hook function in the actually-running code, verified via a read-only SSH probe before the proposal is accepted. If the target doesn't exist yet, the change must explicitly state "pre-positioning infrastructure for future tool surface X" and call it out at the proposal stage rather than discovering it at deployment time. See `openspec/changes/reviewer-agent-selective-trigger/DEFERRED.md` for the K37 re-open trigger documenting what production state would unblock this work.

---

## 2026-05-13 — Cemini adopts SKILL.md frontmatter spec internally (spec-only, not catalog)

K42 follow-up landed: `briefs/2026-05-13_agent-skills-spec-decision.md` recommended Axis A (adopt the SKILL.md spec format) but explicitly reject Axis B (catalog content dependency). The K42 eval cited `package-security-check` skill was removed from the `instructa/agent-skills` HEAD on 2026-05-12 — 12 days between evaluation and removal. **Catalog churn is too fast to depend on.**

The spec itself is portable: plain markdown + YAML frontmatter with `name`, `description`, `license`, `metadata.author`, `metadata.version`, `disable-model-invocation` fields. Body is markdown protocol after a `---` divider, then optionally a `# Project documentation` section for humans. Cemini's existing `~/.claude/skills/tech-debt-audit.md` was already 80% compliant; 3-field frontmatter upgrade (license + metadata.author + metadata.version) brought it to 100%. No body changes; backwards-compatible.

**Cemini's spec stance (pinned to 2026-05-13 snapshot)**:
- We adopt the SKILL.md frontmatter format for internal skills going forward
- We do NOT depend on agent-skills catalog content (or any external skill catalog)
- We pin to this spec snapshot; revisit annually for instructa/Anthropic drift
- `scripts/skill_audit.py --mode skillmd` extension is deferred; not blocking for adoption

*Apply*: New Cemini skills authored from 2026-05-13 forward use the SKILL.md frontmatter. Existing skills get retrofitted opportunistically when touched. See `briefs/2026-05-13_skillmd-compliance-tech-debt-audit.md` for the field-by-field compliance template.

---

## 2026-05-12 — K39 Phase-0 batch surfaced 7th mischaracterization catch + no-LICENSE pattern hits 5 occurrences

K39's 5-tool RED-FLAG audit batch closed today with 0 GO / 1 CONDITIONAL-GO / 4 NO-GO-or-REJECT. Three meta-lessons compound.

**1. Eval-brief OAuth-grafting pattern (meridian) is now confirmed as a *recurring* family, not a one-off (K38 9router was occurrence #1).** Meridian's `src/proxy/tokenRefresh.ts:30` reads `~/.claude/.credentials.json` and the macOS Keychain `Claude Code-credentials` service directly; calls `https://platform.claude.com/v1/oauth/token` with hardcoded `OAUTH_CLIENT_ID = "9d1c250a-e61b-44d9-88ed-5944d1962f5e"` (Claude Code's own client ID being reused); and `oauthUsage.ts:26-27` hits private undocumented `api.anthropic.com/api/oauth/usage` with `anthropic-beta: oauth-2025-04-20`. README's load-bearing disclaimer ("No OAuth interception. No binary patches. No hacks. Just pure, documented SDK calls.") is **directly contradicted by the code**. Same Family-C TOS landmine that killed 9router, and same eval-brief "Adopt — Workflow only" framing missed it both times. **Apply**: any third-party tool advertising "use your Claude Max subscription with [other-tool]" should be Phase-0 audited at the `tokenRefresh.ts`-equivalent source file before adoption — the marketing claim and the code routinely disagree.

**2. Mischaracterization aggregate now 7 catches (K28+K30+K30+K38+K38+K38+K39).** The pattern fires across project sizes (single-dev to 32K★), license types, and tool categories. The K28 SwarmVault catch (flat-layout disease) is structurally different from the K38 9router catch (TOS landmine), which is structurally different from the K39 deepseek-tui catch (scope-creep on legitimate-tool). Three distinct sub-modes:
   - **a. Scope-creep** (deepseek-tui, obscura, K28 SwarmVault) — eval brief recommends wholesale workflow/prod-stack replacement based on partial fit + memory/speed claims alone; tool is fine but the rec is reckless.
   - **b. TOS landmine** (meridian, 9router) — OAuth-grafting / credential reuse pattern; the tool's mechanism violates vendor TOS, eval brief misses it.
   - **c. Caveat-then-Adopt internal inconsistency** (mac-code) — brief itself flags blocking risk (SSD wear), then recommends Adopt anyway. Self-contradictory recommendation.
   These three sub-modes need different audit attention. Scope-creep audits compare against existing stack coverage; TOS-landmine audits read auth-code path directly; caveat-then-Adopt audits enforce internal consistency between brief's Risk section and Recommendation section.

**3. No-LICENSE-file pattern now at 5 occurrences in 4 K-cycles (K36/K38×2/K39×2).** K39 alone surfaced 2 of the 5 (meridian + mac-code). Both had README badges/footers claiming MIT directly contradicted by `gh api repos/<owner>/<repo> --jq '.license.spdx_id'` = null. The check is one `gh api` call. Failure mode = adopting the README's license claim as ground truth without API verification. **Apply**: `scripts/skill_audit.py` Phase-0 brief-audit could grow a `--license-verify` flag that runs the `gh api` check on every github.com URL in a brief and flags mismatches. Currently every Phase-0 audit does this manually; automating eliminates the human-skip failure mode entirely.

*Apply summary*: Phase-0 audit discipline keeps shipping value (7-of-7 high-stakes blocks now have post-audit verdicts that diverge meaningfully from the eval-brief recommendation). The cost is 10-30 min per tool. The savings, on the meridian case alone, is "Anthropic credential revocation + IP-sale ToS-history scar." Worth the time every cycle.

---

## 2026-05-11 — No-LICENSE-file in popular repos (3rd occurrence; treat README claim as unbacked)

Three K-series ingest passes have now surfaced the same pattern: a GitHub repo with prominent README MIT/Apache claim but **no actual LICENSE file in the repo**. Under default copyright, this means "all rights reserved" — the README's license assertion is legally unenforceable absent a written grant. Star count and maintainer prominence do not change this.

The 3 catches:

| K | Tool | Stars | README claim | Repo reality |
|---|------|-------|--------------|--------------|
| K36 | `finance-skills` (claude-plugins-official) | popular skill marketplace plugin | MIT | No LICENSE file; [upstream issue #64](https://github.com/claude-plugins-official/finance-skills/issues/64) filed 2026-05-10 (still open) |
| K38 | `Readme.skill` (study8677) | 68★ / single-author / 25-day-old | "协议 — MIT" (Chinese README footer) | No LICENSE file |
| K38 | `AI-Trader` (HKUDS) | **16,123★** / dual English+Chinese README | MIT | No LICENSE file; root listing has only `.env.example, .gitignore, README.md, README_ZH.md, assets, docs, …` — zero LICENSE/COPYING; GitHub `license` API returns null |

The K38 AI-Trader case is the most striking: 16k stars, dual-README professionalism, active 6-month project. The visible markers all suggest a mature MIT-licensed codebase. The Phase-0 minimum — fetch `repos/<owner>/<repo>` from the GitHub API, check the `license` field — surfaces the gap in seconds. Without that check, a Steal-from extraction proceeds under a false license-clean assumption.

This is **not** a niche-repo pattern. It cuts across:
- Skill/plugin marketplaces (finance-skills)
- Single-author early-stage tools (Readme.skill)
- Major academic-org production codebases (HKUDS, the lab that publishes RAG papers)

Operationally, the no-LICENSE-file pattern interacts with the Cemini IP-sale-readiness posture: a clean-room reimplementation built from a no-LICENSE source has weaker provenance defense than one built from an explicitly-MIT-licensed source. The copyright-default analysis would land the same way (no copying allowed without a grant), but in litigation, the defending party has to show clean-room separation rather than pointing at a license grant. Higher friction.

*Apply:*

1. **Add `gh api repos/<owner>/<repo> --jq '.license.spdx_id'` to the Phase-0 license-verification step** — never trust the README's license claim alone. If the API returns `null`, treat as `NO-LICENSE-FILE` regardless of README content. This is the cheapest possible check (one HTTP call) and catches 100% of this pattern.
2. **Downgrade Steal-from verdicts to "pseudocode-only pattern extraction" when LICENSE is missing** — the source can be read as a design reference, but no direct code copy / derivative translation. Clean-room reimplementation only. Pattern recorded in `wiki/entities/tools/ai-trader-hkuds.md` and `wiki/entities/tools/readme-skill.md`. Tag entity pages with `license-gap` for aggregation.
3. **File upstream GitHub issue** requesting the repo add a LICENSE file matching their README claim. Low-cost (one issue per finding), creates a paper trail, and 1 in N maintainers will actually fix it. The finance-skills issue #64 is the template — short, polite, references the README MIT claim directly.
4. **Do not bump `maturity: validated` for a no-LICENSE-file entity until at least the pseudocode-only constraint is documented in the page body.** Otherwise the validated tag implies license clearance that doesn't exist.

---

## 2026-05-11 — Phase-0 audit catches eval-brief mischaracterization (meta-pattern)

Six Phase-0 audits across K28, K30, and K38 have now rejected credible-looking Adopt-tier verdicts because the eval brief mischaracterized the tool's actual function. The pattern is consistent enough to be worth naming: **eval briefs are synthesized from README marketing + GitHub topic tags, not from reading entry-point code**. The DR sweep that generates them sees the surface a maintainer wants to present; Phase-0 sees what the code actually does. When those diverge, the brief loses.

**K38 base rate signal**: 3 of the last 4 K38 Adopt-tier verdicts (9router, guild, Readme.skill = 75%) were mischaracterized. This isn't tail risk — it's the modal failure mode for current DR-generated eval briefs, especially on small/young/non-English-primary repos.

The 6 catches:

| K | Tool | Eval-brief framing | Phase-0 reality |
|---|------|--------------------|-----------------|
| K28 | SwarmVault | Wiki-tooling candidate | Hardcoded flat-layout — doesn't support nested wikis |
| K30 | PageIndex | Wiki retrieval upgrade | Single-file API + agentic cost + lost graph/metadata |
| K30 | Claude-OSINT | Skill merge for curator | Wrong domain — red-team OSINT, not curator workflow |
| K38 | 9router | "Lean compress-then-forward proxy, ~65% token reduction" | Private Next.js 16 + React 19 dashboard (monaco-editor + recharts + sql.js); README's real claim is 20-40%; Family-C OAuth-grafted free tiers = TOS landmine |
| K38 | guild | "Local-first search MCP / Ollama replacement on CPX21" | Agent-coordination substrate with quest/lore/oath/brief primitives; retrieval is internal to its lore archive, not a drop-in for wiki-markdown serving |
| K38 | Readme.skill | "Agent skill for repo-stats auto-gen / augments wiki-curation toolchain" | Personal Claude/Codex-usage **profile** generator (Chinese-language Markdown + SVG poster across 10 dimensions of individual developer style). Zero wiki-curation surface. DR sweep evidently read English README.en.md keywords and missed the Chinese README's actual audience (developers sharing AI-native work portfolios) |

The three mischaracterization shapes worth naming because Phase-0 keeps catching them:

1. **Marketing claim vs measured reality** — README/landing-page perf claim doesn't match the repo's actual measurement (9router's 65% headline vs 20-40% in-repo claim).
2. **Framework vs application** — tool framed as a focused library, repo is actually a full product (9router as "lean proxy" vs full dashboard with bundled integrations). `"private": true` in package.json is the smoking gun for this shape.
3. **Wrong-primitive** — tool framed by surface-level category match (MCP server, retrieval engine, skill catalog) when the actual primitives serve a different problem (guild's quest/lore/oath/brief is task-coordination, not document-retrieval; Readme.skill's 10-dimension developer profile is personal-portfolio, not repo-stats).
4. **Non-English-primary repo** — Readme.skill specifically. Repo README is Chinese; the English README.en.md is a thin keyword stub. DR sweeps default to the English-language surface and miss the actual audience/purpose documented in the primary-language README. Worth checking the repo's `README*.md` set explicitly before trusting an eval-brief framing on any non-English-domiciled project.

The Phase-0 minimum that catches all three: read `package.json`/`Cargo.toml`/`go.mod` for `"private": true` and dependency bloat signals; read the primary entry-point (`cmd/main.go`, `src/index.ts`, etc.) for the actual primitives; cross-check the README's measured perf number against the eval brief's quoted number.

Cost asymmetry favors the audit: ~30 min Phase-0 prevents 2-4 hours of misaligned implementation. ROI is still favorable when the verdict is GO — you ship with confidence rather than discovering the framing gap mid-integration.

*Apply:*
1. **Never adopt an eval-brief Adopt verdict without Phase-0 unless the tool is from a known-trusted vendor** (official MCP servers, established maintainers we've audited before). The 5 catches are all from less-known repos where the README is the only signal the DR sweep has.
2. **When chartering the next DR sweep, ask it to quote the primary entry-point function names + counts** alongside README snippets. A brief that says "9router exposes 4 proxy functions: compress(), forward(), …" gives Phase-0 a fast sanity-check; a brief that only says "9router is a token-compressing proxy" does not.
3. **Tag entity pages with `eval-brief-mischaracterization`** when this pattern fires. The K38 entries already do this — see [`wiki/entities/tools/9router.md`](wiki/entities/tools/9router.md) and [`wiki/entities/tools/guild-mcp.md`](wiki/entities/tools/guild-mcp.md). Aggregating the tag over time gives the next eval-brief audit a head-start (which sources tend to mischaracterize? which tool classes?).

---

## 2026-05-11 — Claim-evidence anchoring: dedup by canonical value, anchor within ±240 chars

`skill_audit.py` v0.4 calibration surfaced an over-counting bug in the claim-evidence detector. The naive pass treated every textual occurrence of a claim as a distinct claim — so an adoption brief mentioning "MIT license" four times across different sections registered as 4 claims, of which only the first had a nearby `VERIFIED 2026-05-10` anchor → score 1/4 = 25% anchored, even though the claim was fully evidenced. The audit then flagged a clean brief as under-evidenced and recommended rework.

The fix has two parts:

1. **Dedup by `(label, canonical_value)`** — lowercased, whitespace-collapsed, hyphen-stripped. "MIT", "MIT license", "mit-licensed" all canonicalize to `(license, mit)` and count once. Same for version strings (`v0.4.2` ≡ `0.4.2`), star counts (`12k` ≡ `12000`), commit recency (`last commit 2026-05-09` ≡ `commit: 2026-05-09`).
2. **Anchor window ±240 chars** — a claim is anchored if **any** of its occurrences sit within ±240 characters of a verification token. Tokens: `VERIFIED YYYY-MM-DD`, `Phase-0 audit`, `[Source: ...]`, `[NEEDS VERIFICATION ...]`, `[CONFIRMED]` / `[TENTATIVE]` / `[RETRACTED]`. 240 chars ≈ one prose paragraph, which is the natural unit at which a writer pins evidence to a claim — wider windows leak across topics; narrower windows miss claims mentioned at the start of a paragraph with the citation at the end.

The combined effect: the 4-MIT-mentions brief now registers as 1 anchored claim (the first occurrence is within the window of the `VERIFIED` tag) and audits clean. Repeated mentions don't penalize you, but the first mention must be anchored.

*Apply:* when writing an adoption brief or entity-page synthesis, place the verification anchor near the **first** occurrence of each unique claim. Subsequent mentions are free. Don't sprinkle `VERIFIED` tags throughout — it wastes prose and doesn't move the audit score. When reviewing a brief that audits as under-anchored, look for unique-claim-without-nearby-anchor before assuming the brief actually lacks evidence; the more common failure is anchor-placement (claim in §1, citation in §4) rather than missing-citation.

---

## 2026-05-10 — Two-layer memory: `hot.md` is curated state, `claude-mem` is passive observation

Installed `claude-mem` v13.0.1 (Apache-2.0, K35 GO) at the laptop level today. It's a Bun/SQLite/ChromaDB worker that observes Claude Code tool calls + file edits and injects top-N semantically-relevant observations on `SessionStart`. This adds a **second memory layer** alongside the existing `hot.md` discipline, and the two must not be conflated:

| Layer | Source of truth for | Update cadence | Reliability |
|-------|---------------------|----------------|-------------|
| `hot.md` | **Curated intentional state** — open decisions, next-step pointers, K-series position, sprint mode | End of every session (LLM rewrites it) | High — user-reviewed |
| `claude-mem` | **Passive observation memory** — what files were read, what commands ran, what was tried | Continuous (worker daemon) | Medium — semantic recall, not curated |
| `ROADMAP.md` | **Active workstream truth** — DONE log, decisions, pending workstreams | After significant operations | High — committed to git |

When the three disagree, hierarchy is `ROADMAP.md` > `hot.md` > `claude-mem`. Treat claude-mem injections as advisory ("we may have looked at X before") and confirm against the curated layers before acting. Claude-mem is most useful for the "did we already try this?" question that `hot.md` won't capture because the user didn't think it worth recording.

Critical sanity gate: the default `CLAUDE_MEM_SEMANTIC_INJECT_LIMIT=5` cap is what makes this safe to leave running. If you ever raise it past ~20, recheck the token-budget impact at session start. Lazy injection (`SEMANTIC_INJECT=false` default) means observations only surface on user-prompt relevance match, not blanket dump.

*Apply:* when `claude-mem` injects a "you did X" hint that contradicts `hot.md`, trust `hot.md`. When it surfaces an incidental observation that `hot.md` doesn't mention, log it forward into `hot.md` if it materially affects the next session. Never let claude-mem decide a workflow question on its own.

---

## 2026-05-01 — The schema is a synthesis of two design patterns, not invented from scratch

The workspace schema (CLAUDE.md) was synthesized from two primary sources found in the raw research corpus, not designed from first principles:

- **Karpathy's LLM Wiki** (raw source on librarian: `cemini-librarian:/opt/cemini-bulk/research/llm-wiki.md`; mirror at `wiki/sources/llm-wiki.md`) — contributed the three-layer architecture (raw / wiki / schema), `index.md` + `log.md` navigation, ingest/query/lint operations, and the "persistent compounding artifact" philosophy.
- **ByteRover Context Tree** (raw source on librarian: `cemini-librarian:/opt/cemini-bulk/research/llm re 4:3.pdf`) — contributed hierarchical `Domain > Topic > Subtopic > Entry` organization, explicit `@path` relations, YAML frontmatter with lifecycle metadata, ADD/UPDATE/UPSERT/MERGE/DELETE primitives with `reason` audit trail, and OOD signaling.

Both sources predate the workspace. The schema lives in CLAUDE.md (operational) rather than here because it's referenced every session; this entry captures the *why* behind the design, not the rules themselves.

*Apply:* when uncertain about wiki structure, defer to those two source documents. They're the root pattern authorities; CLAUDE.md is the derived implementation.

---

## 2026-04-24 — Research-doc aspirational architectures ≠ deployed infrastructure

Third time the wiki incorrectly claimed DeepSeek-R1-14B on Ollama runs on the Hetzner server. Third correction from the user ("we have gone through this before"). The failure mode is always the same: a research PDF in `research for cemini/` proposes an architecture; the source-stub page faithfully summarizes the proposal; a later entity/concept page synthesizes from the source summary and quietly promotes "X is proposed" into "X is deployed"; a still-later page cites that entity page as if it were verified production state. The error compounds because entity pages are treated as ground truth once they exist.

Evidence that settled it this time: `du -sh ~/.ollama` → not found, `OLLAMA_MODELS` empty, no ollama binary, no LLM-inference Python deps in the `cemini_mcp` container requirements.txt. None of it matched the confident wiki claims.

*Apply:*
1. **Mark source provenance explicitly.** When an entity page is synthesized purely from research-doc proposals (no server-side verification), its `## Raw Concept` section should say so. Phrase like *"This page reflects the architecture proposed by @sources/X and @sources/Y; it has NOT been verified against the deployed Cemini stack."* Block the synthesis from reading as ground truth.
2. **Never carry infra claims forward without a direct-evidence gate.** Before any concept/entity page says "Cemini uses X" (present tense, as production fact), there must be a `[Source: <server path/command/output>]` citation — not just another wiki page. A wiki-to-wiki citation chain is a hallucination amplifier.
3. **Retract in place, don't delete.** Per CLAUDE.md's `[RETRACTED]` rule, keep the page with `maturity: retracted`, preserve the retracted-claim-of-record, and annotate the inline claims on every page that inherited the bad synthesis. Future sessions will still encounter the retraction log and won't re-create the pages.
4. **When the user says "we've gone through this before," treat it as a durable-fact signal.** Add a MEMORY.md equivalent pointer (see `retracted_dri.md` as the template pattern). Don't just fix the page for this session.

---

## 2026-04-23 — The library had the answer; search it before designing

When asked to design the workspace's indexing/organization structure, the reflex was to work from external references (Karpathy's LLM Wiki gist). Running a keyword scan over the 242 existing PDFs turned up `llm re 4:3.pdf` (the ByteRover paper) — which specifies a hierarchical, file-based, markdown-only knowledge structure that's almost exactly what we needed, with far more implementation detail than the Karpathy doc. The final schema is a synthesis of the two, grounded in concrete patterns rather than one-source theory.

*Apply:* before designing anything non-trivial, keyword-scan the local library first. The library is big enough to hide directly relevant material under opaque filenames. Use `pypdf` + regex (see `/tmp/pdf_scan.py` as a template) to sweep fast — scanning 147 PDFs takes under two minutes.

---

## 2026-04-23 — PDF filenames are dates, not topics
The 242 PDFs in `research for cemini/` are named by the date they were downloaded (e.g. `3:29 15.pdf`), not by subject. You cannot locate material by filename alone — you need keyword search over content, or an index we build ourselves.

*Apply:* don't assume a filename reveals topic. When a specific subject is needed, keyword-search the corpus. Build the index progressively — each time a PDF is read, capture its real title + topic + a one-line summary into an index file so the next read is faster. The goal is that every PDF eventually has a row in the index, even if unread.

---

## 2026-04-23 — The server has dev, this laptop has research
When setting up the workspace the assumption was that OSINT research lived on the Hetzner server alongside the dev stack, and we planned to rsync it down. In reality the server has only code and raw data feeds (GDELT, EDGAR, X harvests); the long-form research PDFs already live here in `research for cemini/`. We skipped the rsync step.

*Apply:* when looking for research material, start here. Use the server for ticker lists, raw feeds, and dev references — not for curated research. Never modify the server's `CLAUDE.md` from this workspace.
