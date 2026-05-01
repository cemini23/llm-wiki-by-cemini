# Lessons

A running log of lessons learned while managing this workspace. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

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
