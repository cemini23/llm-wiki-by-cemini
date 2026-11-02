---
title: "lexifina/global-law — dated statutory corpora, Italy coverage starts 1947"
type: entity
tags: [tool, law, genealogy, mcp, atto, provenance]
keywords: [global-law, lexifina, statutory provenance, point-in-time law, italy, jure sanguinis, atto-mcp]
related:
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md
  - concepts/historical-jurisdiction-atlas.md
maturity: draft
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md, URL 18, **Extract** tier, routed to Atto and family-tree.

The question this page answers: **can Atto prove which Italian statute governed a birth, marriage, or naturalisation on a given date?**

## Narrative

### What it is

A git repository that interleaves the statute history of many jurisdictions into one timeline. Each provision is a file. Each law taking effect is a commit. A country with only publication sources gets no pinned submodule.

Two access surfaces matter:

- `tools/law.py` — a command-line reader.
- `tools/mcp_server.py` — a local stdio MCP server, read-only, zero network.

The report says the MCP server exposes 18 read-only tools: dated provision readings, diffs, word-level attribution, and change impact.

### The provenance model

Each corpus is one of three states, declared in `manifest.json`:

| State | Meaning |
|-------|---------|
| `in-force` | Dated official versions. |
| `replayed` | Rebuilt by applying each amending act. The `verification` field names which dates were checked. |
| `current-only` | Today's text only. No history. |

The repository ships `REPRODUCE.md`, which allows a hash-for-hash rebuild.

Git cannot store commit dates before 1970. The README states this limit directly. A historical event is therefore modelled as a commit whose content describes the event, not as a commit dated to it. Read the model that way, or the timeline misleads.

### Phase-0, 2026-11-01

GitHub egress is denied in the session sandbox, so no clone. Checks used `README.md` and `manifest.json` fetched from the raw content host.

| Question | Finding |
|----------|---------|
| Does an Italy corpus exist? | **Yes.** `italy/national/acts`, label "Italian law: the Constitution, every legge costituzionale, L. 300/1970…". |
| What period does it cover? | **From 1947-02-22 to 2026-06-23.** No earlier material. |
| Corpus state | Not declared in the manifest row. Two warnings on the record: `corpus.json lacks language (defaults are used)`, `corpus.json has no citation rule`. |
| Licence | `LICENSE.md` states CC0. The law text itself stays under each country repository's own terms. |

**The decisive finding.** The report asked for a check on "1865, 1912, and 1948" coverage and then routed the tool to Atto anyway. The corpus **starts at 1947-02-22**. The 1865 Civil Code and Law 555 of 1912 — the two instruments that actually govern most jure sanguinis claims — are absent.

So the value is narrower than the report states. The tool can establish the law from 1948 onward. It cannot establish pre-1948 Italian law, which is where the hard cases live.

### What to take

1. **The manifest schema.** A three-state corpus declaration (`in-force` / `replayed` / `current-only`) plus a `verification` field naming which dates were actually checked is a good contract. Atto should copy the *shape*, not the data.
2. **The read-only local stdio MCP server.** Zero network, read-only tools, one provision per file. This matches the Atto anti-exfiltration boundary.
3. **`REPRODUCE.md`.** A hash-verified rebuild recipe is the cheapest possible provenance claim.

### What not to take

- **The Italy data as a 1948-and-earlier source.** It does not cover that period.
- **The citation model.** The Italy corpus has no citation rule. Atto proofs need one.

### Status

Extract-tier, **partial fit**. Use as a schema and architecture reference for `atto-mcp`. Do not cite it in a concierge packet for a pre-1948 event.

## Snippets

> "Italian law: the Constitution, every legge costituzionale, L. 300/1970…" — `manifest.json`, Italy row, coverage begins `1947-02-22` [fetched 2026-11-01]

> "`in-force` (dated official versions)", "`replayed` (rebuilt by applying each amending act; its `verification` says which dates were checked)", "`current-only` (today's text only)" — README [fetched 2026-11-01]

> "Free to use: CC0. This repository is CC0." — README [fetched 2026-11-01]

## Dead Ends

- **Using the Italy corpus to date pre-1948 citizenship law.** Coverage begins 1947-02-22. The 1865 Civil Code and Law 555/1912 are outside it.
- **Reading commit timestamps as event dates.** Git cannot store dates before 1970. The commit describes the event; the timestamp does not date it.
