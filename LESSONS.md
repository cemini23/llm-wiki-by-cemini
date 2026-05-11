# Lessons

A running log of lessons learned while managing this workspace. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

---

## 2026-05-11 — Phase-0 audit catches eval-brief mischaracterization (meta-pattern)

Five Phase-0 audits across K28, K30, and K38 have now rejected credible-looking Adopt-tier verdicts because the eval brief mischaracterized the tool's actual function. The pattern is consistent enough to be worth naming: **eval briefs are synthesized from README marketing + GitHub topic tags, not from reading entry-point code**. The DR sweep that generates them sees the surface a maintainer wants to present; Phase-0 sees what the code actually does. When those diverge, the brief loses.

The 5 catches:

| K | Tool | Eval-brief framing | Phase-0 reality |
|---|------|--------------------|-----------------|
| K28 | SwarmVault | Wiki-tooling candidate | Hardcoded flat-layout — doesn't support nested wikis |
| K30 | PageIndex | Wiki retrieval upgrade | Single-file API + agentic cost + lost graph/metadata |
| K30 | Claude-OSINT | Skill merge for curator | Wrong domain — red-team OSINT, not curator workflow |
| K38 | 9router | "Lean compress-then-forward proxy, ~65% token reduction" | Private Next.js 16 + React 19 dashboard (monaco-editor + recharts + sql.js); README's real claim is 20-40%; Family-C OAuth-grafted free tiers = TOS landmine |
| K38 | guild | "Local-first search MCP / Ollama replacement on CPX21" | Agent-coordination substrate with quest/lore/oath/brief primitives; retrieval is internal to its lore archive, not a drop-in for wiki-markdown serving |

The three mischaracterization shapes worth naming because Phase-0 keeps catching them:

1. **Marketing claim vs measured reality** — README/landing-page perf claim doesn't match the repo's actual measurement (9router's 65% headline vs 20-40% in-repo claim).
2. **Framework vs application** — tool framed as a focused library, repo is actually a full product (9router as "lean proxy" vs full dashboard with bundled integrations). `"private": true` in package.json is the smoking gun for this shape.
3. **Wrong-primitive** — tool framed by surface-level category match (MCP server, retrieval engine) when the actual primitives serve a different problem (guild's quest/lore/oath/brief is task-coordination, not document-retrieval).

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
