---
title: "Zero-Breach-Toolkit — offline spyware IOC scanner with coverage-gap reporting (Apache-2.0)"
type: entity
tags: [tool, forensics, spyware, ioc, offline, defensive, operator-opsec]
keywords: [zero breach toolkit, spyware ioc, pegasus, predator, graphite, candiru, mobile forensics, coverage gaps]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md"
maturity: draft
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md, URL 12, **Extract** tier. Routed to the local-abliterated / operator lab.

The question this page answers: **how do you check a host for spyware and report honestly on what you could not check?**

## Narrative

### What it is

`interplains/Zero-Breach-Toolkit`. **Apache-2.0.** 3 834 stars at the time of the report, with version 0.1.13 released 2026-11-01. The repository was created in late October 2026 and gained those stars within days.

An offline, read-only forensic scanner. It runs across Windows, macOS, Linux, Android device dumps, and iPhone backups. It looks for mercenary spyware indicators — Pegasus, Predator, Graphite, Candiru — across browser profiles, system logs, and file artifacts.

Design properties that matter:

- **Zero external packages.** The single-file release needs no install.
- **Zero admin rights.**
- **Network-isolated execution.** Indicator updates (`--update`) are a separate, explicit step and are decoupled from scanning.
- Runs as `python -X utf8 scan/zero-breach-toolkit.py`, or with `--phone "FOLDER"` for mobile backups.

### The output contract is the valuable part

The scanner reports in three parts:

1. What was found.
2. An **evidentiary strength grade**.
3. **What could not be checked.**

The third part is the one to copy into any forensic workflow. A scanner that reports only hits implies completeness it does not have. A scanner that enumerates its own blind spots states its real coverage. That is the difference between a tool an investigator can put in a report and a tool that manufactures false confidence.

### Limits

- **IOC matching cannot prove absence.** No hit means no known indicator matched. Novel spyware is by definition not in the indicator set.
- **The repository is days old.** A 6.3/10 code-health score is reported. Stars gained in days are not a security review.
- **Verify before running on a production host.** The report's condition, which is correct: check the PGP detached signatures — `zero-breach-toolkit.py.asc`, `SHA256SUMS.txt.asc`, `archivegenocide-signing-key.asc` — and read `scan/zero-breach-toolkit.py` before executing it on any host that matters.

### Scope

Authorized defensive work only. This is a host self-check for machines the operator controls, including the laptop that runs CeminiSuite and holds `~/AttoVault/`. It is not an offensive tool and has no offensive use here.

### Phase-0 status

**Not run at source level.** GitHub egress is denied in this session. The properties above come from the report's cited sources. The signature verification and source read in the previous bullet are the actual Phase-0, and they have not been done.

### Status

Extract, **pattern plus tool**. Nothing run, nothing installed.

## Snippets

> "Extracting its reproducible single-file release architecture and its mandatory 3-part output contract—grading evidentiary confidence and explicitly listing unverified surfaces ('what could not be checked')—into Cybersecurity wiki/briefs/ directly upgrades the local-abliterated-lab forensic workflow and reporting precision." — report, URL 12

> "IOC matching cannot prove absence of novel spyware." — report, URL 12 business risk

## Dead Ends

- **Treating a clean scan as proof the host is clean.** No known indicator matched. That is all it says.
- **Running it on a production host before verifying signatures and reading the source.** The repository is days old.
