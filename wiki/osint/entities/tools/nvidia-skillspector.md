---
title: "NVIDIA SkillSpector — agent skill security scanner"
type: entity
tags: [tool, adopt-candidate, cybersec, mcp, skill-audit, k88, phase-0-complete]
keywords: [skillspector, nvidia, langgraph, supply-chain, prompt-injection, skill-audit, osv]
related:
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - "@cybersecurity-wiki/entities/tools/nvidia-skillspector.md"
maturity: validated
created: 2026-05-31
updated: 2026-05-31
phase_0_verdict: CONDITIONAL-GO 2026-05-31 — Apache-2.0 verified; static scan PASS; wire `--no-llm` into laptop preingest only; not on PyPI; Python 3.12+; do not deploy on librarian until air-gap OSV probe
adoption_status: PHASE-0-COMPLETE 2026-05-31
---

## Relations

- @sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md — K88 v5 Adopt (primary fit cybersec-wiki)
- @concepts/tool-evaluation-framework.md — Phase-0 complete
- @concepts/cemini-license-posture.md — Apache-2.0 IP-sale-safe
- @cybersecurity-wiki/entities/tools/nvidia-skillspector.md — cybersec-wiki mirror (user session)

## Raw Concept

- **Repo**: `github.com/nvidia/skillspector`
- **License**: Apache-2.0 `[CONFIRMED 2026-05-31]` — `LICENSE` file + GitHub API SPDX
- **Prompted by**: K88 multi-wiki eval — supply-chain scanning for Claude skill repos before kb-server ingest
- **PyPI**: **not published** (2026-05-31) — install from Git source only

## Narrative

LangGraph-based scanner for MCP/agent skill directories — 64 static patterns (prompt injection, exfiltration, supply chain, MCP tool poisoning, YARA, AST taint) plus optional LLM semantic pass. **Fills a real gap:** OSINT `scripts/skill_audit.py` is prose/checklist-only today; SkillSpector adds executable static analysis before skill install or wiki routing.

### Phase-0 audit (2026-05-31)

Repo cloned to `/tmp/ph0-skillspector/`; maturity via `gh api`.

#### License — claim vs actual

| Claim (K88 eval) | Actual |
|------------------|--------|
| Adopt, Apache-2.0 | **Apache-2.0 CONFIRMED** — root `LICENSE`, SPDX via `gh api`, NVIDIA copyright headers in source |

IP-sale-safe for integration into preingest tooling.

#### Maturity — observed

| Metric | Observed | Note |
|--------|----------|------|
| Stars | **429** | Strong launch traction |
| Forks | 31 | Healthy |
| Open issues | 3 | Low |
| Created | **2026-03-21** | ~10 weeks old at audit — young but NVIDIA-backed |
| Last push | **2026-05-18** | Active |
| Version | **2.0.0** (pyproject) | Classifier: **Alpha** |
| Source files | 51 Python modules | Substantive scanner, not a stub |
| PyPI | **Absent** | `pip install skillspector` fails — source/`uv` install only |

Young repo with credible engineering (tests, SARIF output, OSV client, YARA rules). Bus factor is NVIDIA org, not a solo maintainer pump-and-dump.

#### Failure-mode probe — skill-scanner class

**1. Hardcoded layout?** No — accepts Git URL, zip, directory, or single `SKILL.md`. Compatible with `.claude/skills/` and marketplace skill trees.

**2. LLM dependency trap.** Default CLI path **requires** an LLM API key (`OPENAI_API_KEY` or provider-specific). Without it, scan **errors** unless `--no-llm` is passed. **Integration must use static-only mode** for CI/preingest; LLM semantic pass is opt-in with explicit key policy.

**3. OSV / air-gap behavior.** `[CONFIRMED 2026-05-31]` — `osv_client.py` queries `api.osv.dev` with 10s timeout; on failure logs warning and falls back to a **small static CVE list** (`_FALLBACK_VULNERABLE_PYPI` / `_FALLBACK_VULNERABLE_NPM`). SC4 supply-chain coverage degrades gracefully offline — not a hard blocker for librarian subnet, but live OSV is strictly better. Probe on `cemini-librarian` still recommended before any server-side install.

**4. Dependency footprint.** Editable install on laptop Python 3.12.5 → **~228 MB venv** (langgraph stack, yara-python, httpx, openai SDK). Heavy for a pre-commit hook; acceptable as an **on-demand preingest subprocess**, not a always-on daemon.

**5. Python version.** `requires-python >= 3.12` — laptop 3.12.5 PASS; verify prod/librarian Python before any server-side use.

**6. Programmatic API.** `skillspector.graph` exposes compiled LangGraph; CLI wrapper is thin. Practical integration: `skillspector scan <path> --no-llm --format json` from `preingest_check.py` or a new `scripts/skill_supply_scan.py`.

#### Live probe (2026-05-31)

```bash
skillspector scan ".claude/skills/kb-retriever" --no-llm --format json
```

Result: **risk score 0 / SAFE**, ~1 s elapsed, 8 components scanned, 0 issues. Static path works without network LLM.

#### Comparison vs existing Cemini coverage

| Surface | Overlap |
|---------|---------|
| `scripts/skill_audit.py` | **Complementary** — SkillSpector adds static malware/pattern detection; keep skill_audit for brief prose gates |
| `scripts/preingest_check.py` | **Extension point** — duplicate detection today; no supply-chain scan |
| kb-server / conductor | No overlap — different layer |
| Cybersec offensive skills | Methodology vs tooling — SkillSpector is install-time gate, not engagement tradecraft |

### Decision — CONDITIONAL-GO

Wire **static-only** SkillSpector into **laptop preingest** (new skill drops, finance-skills marketplace updates, cross-wiki skill imports). Conditions:

1. **`--no-llm` always** in automated pipeline unless operator explicitly opts into semantic pass with API key.
2. **Isolated venv** (`python3.12 -m venv .local/skillspector-venv`) — do not pollute global Claude Code Python.
3. **Not on librarian/prod** until air-gap OSV fallback probed on subnet (`ssh cemini-librarian` one-shot scan).
4. **Not on PyPI** — pin Git SHA in install docs; re-audit on upstream releases.
5. **Cybersec-wiki** owns expanded entity narrative + MCP exposure policy (authorized research boundary).

### Integration sketch (next brief, not shipped)

```bash
skillspector scan "$SKILL_PATH" --no-llm --format json --output /tmp/skillspector.json
# Gate: risk_assessment.severity != LOW → human review before ingest
```

## Snippets

> "Queries the OSV.dev batch API … Falls back to a small static list when the API is unreachable (network error, timeout, air-gapped environment)." [Source: nvidia/skillspector `osv_client.py` module docstring, cloned 2026-05-31]

> "Use `--no-llm` to skip LLM analysis and run static checks only." [Source: nvidia/skillspector CLI help, 2026-05-31]
