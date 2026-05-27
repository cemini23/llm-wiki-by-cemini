# OSS Agent Toolkit — Roadmap

Saved 2026-05-27 from strategy session. Two public repos ship first; others are sequenced follow-ons.

## IP boundary

| Safe to open-source | Keep closed |
|---------------------|-------------|
| Lint/audit tooling, schemas, methodology | Trading strategies, Polymarket bot logic |
| Phase-0 checklists, license-skeptic patterns | Prod briefs, `/opt/cemini` wiring |
| Wiki page format spec (structure, not content) | Rare-event methodology (newsletter / institutional) |
| Anonymized eval failure stats | Conductor synthesis, raw ingested sources |

Rule: **ship the librarian's ruler, not the library's contents.**

## Repo sequence

| Priority | Repo | Status | Purpose |
|----------|------|--------|---------|
| **1** | [vet](https://github.com/cemini23/vet) | **Shipped v0.1.0** | Static veto-gate audit for skills, briefs, agent prompts |
| **2** | [phase0](https://github.com/cemini23/phase0) | **Shipped v0.1.0** | CLI for third-party tool adoption audits (two-gate pattern) |
| 3 | wikilint | Planned | Generalize `wiki_lint.py` — bidirectional links, orphans, stale tags |
| 4 | eval-skeptic | Planned | Verify LLM tool-eval license claims via `gh api` |
| 5 | ara-schema | Planned | Agent Research Archive page format spec only |

## Deferred / skip

| Idea | Verdict |
|------|---------|
| Cross-skill converter (Cursor ↔ Claude ↔ Codex) | Defer — format drift, low moat |
| Kimi-style swarm for Claude/Cursor | Skip — red ocean |
| Full conductor/kb-server OSS | Skip — too close to prod brain |
| NotebookLM bridge | Keep internal |

## vet (repo 1)

Extract and generalize `scripts/skill_audit.py`:

- **Profiles:** `brief` (12 static checks), `skillmd` (Anthropic SKILL.md frontmatter), `minimal` (portable subset)
- **Veto gates:** Operational Stability + Scientific Integrity (MedSkillAudit lineage)
- **Stdlib-only** core; no API keys in default path
- **GitHub Action** for CI on skills/briefs
- **Origin:** battle-tested on 100+ Cemini briefs (internal); public tool is domain-neutral

Build plan: `docs/vet-build-plan.md`

## phase0 (repo 2 — after vet)

Codify doc-level eval → Phase-0 source audit:

```bash
phase0 audit https://github.com/foo/bar --class mcp-server
```

Tool-class checklists: MCP server, wiki-tool, skill library, OAuth proxy, etc.

Launch content: blog post with anonymized stats (40% doc-level Adopts failed Phase-0; license eval false-negative rate).

## Visibility playbook

1. Ship `vet` + README case study (no Cemini alpha)
2. Ship `phase0` + HN/Show HN post with eval failure stats
3. Optional: `wikilint` if wiki/CI angle resonates

Brand neutrally on repos; mention Cemini only as case study in About/README.

## Monetization preserved

| Open layer | Closed layer |
|------------|--------------|
| Audit/lint/eval tooling | Execution stack + prod MCP |
| Schema + methodology | Trading signals + strategies |
| Community trust | CeminiSuite institutional sale, newsletter |
