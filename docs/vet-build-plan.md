# vet — Build Plan (v0.1.0)

## Goal

Ship a **stdlib-only**, **domain-neutral** static auditor for agent artifacts. First consumer: skills and briefs before they leave a repo or ship to prod.

## Non-goals (v0.1)

- LLM dynamic audit (`--llm-mode`) — stays in private `skill_audit.py`; avoids API keys in public default path
- Cross-format skill conversion
- Hosted service / SaaS

## Architecture

```
src/vet/
  __init__.py          # version
  __main__.py          # python -m vet
  cli.py               # argparse, exit codes
  models.py            # CheckResult, AuditReport
  engine.py            # parse, assemble, score, verdict
  report.py            # text + JSON render
  profiles.py          # profile → check list
  checks/
    _regex.py          # shared patterns
    sections.py
    crosslinks.py
    citations.py
    freshness.py
    prose.py
    frontmatter.py
    regime.py          # optional, brief profile
    adoption.py        # completeness, risk, phasing, claim-evidence, abstract
    skillmd.py
```

## Profiles

| Profile | Use case | Checks |
|---------|----------|--------|
| `brief` | Tool-adoption / design briefs | All 12 static checks from skill_audit v0.4 |
| `skillmd` | Anthropic SKILL.md / Cursor skills | Frontmatter required fields, body non-empty, name slug, description length |
| `minimal` | Any markdown agent doc | sections (soft), crosslinks, citations, freshness, prose, frontmatter |

## CLI

```bash
vet PATH [--profile brief|skillmd|minimal]
vet PATH --json
vet PATH --strict          # warnings → REJECT
vet PATH --root .          # crosslink resolution root
vet PATH --link-dir wiki   # extra dirs (repeatable)
vet PATH --nv-age-days 30
```

Exit codes: `0=PASS`, `1=WARN`, `2=REJECT`, `3=ERROR`

## Config / resolution

- `VET_ROOT` env or `--root` (default: cwd)
- `--link-dir` adds search paths for `@path/to/file.md` (default: `[root, root/wiki]` if wiki exists)
- No secrets, no network calls

## Tests

Fixtures under `tests/fixtures/`:

- `pass_brief.md`, `fail_missing_target.md`, `fail_dangling_link.md`
- `pass_skillmd/SKILL.md`, `fail_skillmd_no_description/SKILL.md`
- Regression: regime disclosure veto, adoption brief heuristics

Run: `pytest` + `ruff check`

## CI

GitHub Actions: Python 3.11–3.12, pytest, ruff

## Release checklist

- [x] No API keys, SSH hosts, `.local`, prod paths in tree
- [x] Secret-pattern scan clean
- [x] README: install, profiles, GitHub Action snippet, attribution (MedSkillAudit lineage)
- [x] LICENSE MIT
- [x] Push to https://github.com/cemini23/vet (public, v0.1.0)

Local clone: `/Users/claudiobarone/Desktop/projects/vet`

## OSINT integration

`scripts/skill_audit.py` delegates static checks to `vet` when the CLI is on PATH (`--no-vet` forces inline fallback). `--llm-mode` dynamic audit remains workspace-local.

## Post-v0.1 (workspace integration)

- OSINT `scripts/skill_audit.py` can thin-wrap `vet --profile brief` or stay forked until validated
- ROADMAP entry when published
