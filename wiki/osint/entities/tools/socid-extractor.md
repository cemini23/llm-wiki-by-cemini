---
title: "socid-extractor — cross-platform social-account identifier extraction"
type: entity
tags: [tool, osint, social-media-intelligence, entity-resolution, scraping, adopt, locally-installed, k49]
keywords: [socid-extractor, soxoj, stable-internal-identifiers, gaia-id, facebook-uid, instagram-pk, 130-platforms, http-only, no-headless-browser, entity-resolution, mit-license]
related:
  - sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md
  - entities/tools/fingerprint-suite.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
phase_0_verdict: "GO 2026-05-16 — repo HEAD/v0.0.28 is clean MIT; clean permissive deps; no supply-chain red flags. Remediation done: cemini-librarian upgraded to v0.0.28 (MIT line) 2026-05-16. Residual (benign): laptop pinned at v0.0.27 (GPL-3.0) — laptop Python is 3.9.6, v0.0.28 requires >=3.10; laptop is the curation workspace (no serving path, never redistributes), so GPL on an imported library there carries no copyleft risk. Upgrade the laptop install when a Python 3.10+ is available."
---

## Relations

- @sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — evaluated in the v3-iteration eval (Adopt tier, OSINT primary fit)
- @entities/tools/fingerprint-suite.md — sibling OSINT-collection tooling; fingerprint-suite supplies stealth, socid-extractor supplies entity extraction
- @cybersecurity-wiki/concepts/osint-for-cybersecurity.md — cross-wiki: stable-identifier extraction enables threat-actor correlation across platform redesigns

## Raw Concept

Promoted from the 2026-05-16 "Tool Evaluation and Wiki Fit v3 Iteration" 46-repo eval. Tier: **Adopt**. Primary fit: OSINT-wiki. Cross-route: cybersecurity-wiki (OSINT-for-cybersecurity / threat-actor correlation). **Adopted locally** this ingest.

- URL: https://github.com/soxoj/socid-extractor
- License: **MIT at repo HEAD / v0.0.28** (relicense commit c73f79e, 2026-04-03, PR #222) — but the **locally-installed v0.0.27 is GPL-3.0**. See Phase-0 Audit (2026-05-16).
- Stars / last commit / open issues: 976 / 2026-05-14 / 1 (audit 2026-05-16; eval claimed 975 / 2026-04-09 / 1 — eval's "last commit" was stale, repo is more active than reported)
- Stack: Python (3.10+; CI tests 3.10–3.14)

## Narrative

**socid-extractor** is a Python library that resolves a persistent OSINT friction point: **entity continuity across constantly-evolving social-media architectures**. It operates entirely via standard HTTP requests — no headless browser, no compute overhead — and parses structured data from **130+ platforms** into normalized ontologies (standardizing fields like `fullname`, `created_at`).

Its core innovation is extraction of **stable internal identifiers** — Google **GAIA IDs**, Facebook **UIDs**, Instagram **`pk`** values. These immutable IDs let analysts track a target continuously even when usernames change or a platform redesigns its frontend DOM. Output normalization means unstructured social intelligence can pipe directly into a database for cross-referencing.

**Cemini fit**: directly serves the OSINT-wiki / librarian kb-server workflow — pure-Python, no browser latency, ingests and normalizes public profile data programmatically. The stable-identifier extraction is the tracking primitive for threat-actor financial profiling (cross-routed to cybersec). MIT clears the IP sale.

**Adoption (2026-05-16)**: installed via `pip` on the laptop (`~/tools/`) and on cemini-librarian — a workspace/curation-side OSINT tool, consistent with the deployment boundary (curation tooling on laptop+librarian; financial tooling on cemini-prod).

- `[OPEN QUESTION 2026-05-16]` Parser resilience against emerging anti-scraping defenses (e.g. Cloudflare Turnstile on TikTok). (Partially addressed below — active upstream maintenance is the mitigation, but per-platform resilience is still untested without execution.)

## Phase-0 Audit (2026-05-16)

Clone-and-inspect audit per CLAUDE.md § "Phase-0 audit pattern". Repo cloned to `/tmp/socid-extractor-audit/` (shallow, depth 50). No execution. This is a **retroactive** Phase-0 — v0.0.27 was already pip-installed on the laptop (`~/tools/`) and on cemini-librarian in K49.

**License — PASS at HEAD, with a version caveat.** Repo HEAD and tag **v0.0.28** carry a clean, standard `MIT License` file (`Copyright (c) 2019-2026 Soxoj`) and `pyproject.toml` declares `license = "MIT"`. The relicense is real: commit `c73f79e` "License change to MIT (#222)", dated 2026-04-03. **Caveat:** the project was **GPL-3.0** before that. Tag `v0.0.27` ships a full GNU GPL v3 LICENSE file and `setup.py` with `license='GPL-3.0'`. The locally-installed package is **0.0.27**, and `pip show socid-extractor` on this laptop confirms `License: GPL-3.0`. So the eval's "MIT (per report)" is correct *for the current repo* but **does not match the bits actually installed on the librarian**. SPDX: HEAD declares `license = "MIT"` (SPDX expression form) in `pyproject.toml`; the standalone LICENSE file is the canonical MIT text.

**Dependency license scan — clean.** Three runtime deps only (`requirements.txt` / `pyproject.toml`): `requests` (Apache-2.0), `python-dateutil` (Apache-2.0 / BSD dual), `beautifulsoup4` (MIT). All permissive, zero copyleft transitive contamination. Test-only deps (`pytest`, `pytest-rerunfailures`, `pytest-xdist`) are MIT and not shipped.

**Supply-chain red flags — none.** No `setup.py` at HEAD (PEP 517 `pyproject.toml` + `setuptools.build_meta`); no `cmdclass` / custom post-install hooks; no `os.system` / `subprocess` / network calls in `pyproject.toml`, `setup.cfg`, `run.py`, or `revision.py`. `revision.py` is a dev helper, not a build hook. Clean PyPI-sourced build. Dependabot is active on test deps.

**Tool-class failure mode (parser staleness vs anti-scraping) — well mitigated.** For an OSINT scraper the killer is parsers rotting against site redesigns. socid-extractor is actively maintained against exactly this: last commit 2026-05-14 (two days before audit — eval's "2026-04-09" was already stale), recent CHANGELOG entries are continuous parser fixes (Medium RSS, Substack, Calendly, Discourse, Vimeo, GitHub/GitLab, Virgool). The `pytest.ini_options` markers (`github_failed`, `rate_limited`, `requires_cookies`) show the maintainer explicitly tracks anti-bot / captcha breakage. Only 1 open issue. Healthy multi-contributor cadence (Soxoj + dependabot + outside PRs).

**Comparison vs existing Cemini coverage.** Sibling `@entities/tools/fingerprint-suite.md` supplies stealth/anti-detection; socid-extractor supplies the complementary stable-identifier extraction layer. No overlap with existing Cemini tooling — it fills a genuine gap.

**Verdict — GO** (was CONDITIONAL-GO; remediation done 2026-05-16). Tool is clean, actively maintained, no supply-chain concerns, permissively licensed at HEAD. The audit's open condition — v0.0.27 being GPL-3.0 — was acted on the same day:

- **cemini-librarian — CLEARED.** Upgraded `/opt/socid-extractor-venv` to **v0.0.28** (MIT line). The librarian sits adjacent to the raw-source canon; it is now on a clean MIT install.
- **Laptop — residual, benign.** The laptop runs system Python **3.9.6**; socid-extractor **v0.0.28 requires Python ≥3.10**, so the laptop install stays pinned at **v0.0.27 (GPL-3.0)** until a Python 3.10+ interpreter is added. This is not a real copyleft risk: the laptop is the curation workspace — not in any serving path, powered off when idle, and the library is *imported*, never modified or redistributed. GPL-3.0 copyleft does not bite a private internal library import. Upgrade opportunistically when a newer Python lands on the laptop.

Net: GO. The IP-sale-relevant machine (librarian) is on clean MIT; the laptop residual is documented and benign.

## Snippets

> "The core innovation is its extraction of 'stable internal identifiers' — such as Google GAIA IDs, Facebook UIDs, and Instagram pk values ... These immutable identifiers allow OSINT analysts to track threat actors continuously, even when the target attempts to evade detection by altering usernames." [Source: Tool Evaluation and Wiki Fit Analysis.docx — URL 10]
