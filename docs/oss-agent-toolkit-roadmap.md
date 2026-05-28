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
| **1** | [vet](https://github.com/cemini23/vet) | **v0.2.0** — Action, examples, PyPI workflow | Static veto-gate audit |
| **2** | [phase0](https://github.com/cemini23/phase0) | **v0.2.0** — Action, PyPI workflow | Third-party tool adoption audits |
| **3** | [wikilint](https://github.com/cemini23/wikilint) | **v0.1.0** — new | Wiki orphans, backlinks, dangling @paths |
| **4** | [agent-toolkit-demo](https://github.com/cemini23/agent-toolkit-demo) | **live CI template** | Forkable repo wiring all three tools |
| **5** | [ara-schema](https://github.com/cemini23/ara-schema) | **v0.1.0** | Wiki page format spec (structure only) |
| — | eval-skeptic | Merged into phase0 `verify-eval` | — |

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

## Visibility playbook (updated — posts underperformed)

Distribution shift from one-off posts → **forkable CI template**:

1. **[agent-toolkit-demo](https://github.com/cemini23/agent-toolkit-demo)** — fork + green/red CI badges
2. **GitHub Marketplace-style Actions** on each repo (`action.yml`)
3. **PyPI** — trusted publishing workflows shipped; `docs/PYPI.md` in each repo (human: create PyPI projects + publishers)
4. **awesome-agent-skills** — PR opened listing vet / phase0 / wikilint / demo under Development and Testing
5. **OSINT pre-commit** — `vet` on SKILL.md + briefs; `wikilint` on `wiki/` changes

## ara-schema

Published at [cemini23/ara-schema](https://github.com/cemini23/ara-schema) — frontmatter, sections, citation/confidence tags; no Cemini content.

## Monetization preserved

| Open layer | Closed layer |
|------------|--------------|
| Audit/lint/eval tooling | Execution stack + prod MCP |
| Schema + methodology | Trading signals + strategies |
| Community trust | CeminiSuite institutional sale, newsletter |
