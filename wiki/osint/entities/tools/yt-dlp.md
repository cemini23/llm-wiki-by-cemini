---
title: yt-dlp — feature-rich command-line media extractor
type: entity
tags: [entity, tool, media-extraction, osint, audio-visual-intelligence, adopted, k54]
keywords: [yt-dlp, youtube-dl-fork, media-downloader, unlicense, gplv3-binary-caveat, sponsorblock, osint-av-collection]
related:
  - sources/multi-wiki-tool-eval-26url-2026-05-19.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-19
updated: 2026-05-19
---

## Relations

- @sources/multi-wiki-tool-eval-26url-2026-05-19.md — K54 eval URL 19; the source that surfaced this tool
- @concepts/cemini-license-posture.md — yt-dlp is a clean case of the source-vs-binary license split

## Raw Concept

What prompted this page: K54 multi-wiki tool-eval URL 19, tier **Adopt**, primary fit OSINT wiki. yt-dlp is the de-facto-standard media extractor; this page records the verified facts and the one licensing subtlety that matters for Cemini adoption.

## Narrative

`yt-dlp/yt-dlp` — the **de-facto-standard command-line audio/video downloader**, the actively maintained successor to youtube-dl. Verified 2026-05-19 (GitHub API): **Unlicense** (per the GitHub API `spdx_id`), **163,135★**, pushed 2026-05-16, Python. Nightly release channel specifically maintained to counter upstream site API breakage and throttling; native SponsorBlock integration.

### OSINT relevance

For the OSINT wiki, yt-dlp is the raw audio-visual collection workhorse — pulling video/audio for transcription, threat-actor profiling, and feeding downstream pipelines. It reliably circumvents the throttling that cripples legacy extractors. (Cross-routed to the Image-gen wiki as well, where reliable audio extraction feeds TTS persona-ops training — see the K54 Image-gen brief.)

### The one license caveat — source vs. binary

The eval's licensing analysis here is correct and worth preserving: yt-dlp has a **split license posture**.
- The **source repository and PyPI source distributions** are governed by the permissive **Unlicense** — IP-sale-safe, no copyleft.
- The **pre-compiled binary executables** statically bundle GPLv3+ / ISC / MIT components. Those binaries carry **GPLv3+ encumbrance** — a copyleft poison pill if linked into the Cemini stack.

**Adoption rule**: Cemini compiles/installs yt-dlp strictly from the **Unlicense-protected source tarball** (`yt-dlp.tar.gz` / `pip install yt-dlp` from sdist). Never vendor or static-link the pre-built binary. This is a clean instance of the "read the actual license, distinguish source from distribution" discipline in @concepts/cemini-license-posture.md — the permissive grant covers the source, not the assembled binary.

### Verdict — Adopt (laptop-side / source-build only)

License-clean on the source path; mature beyond question (163k★, nightly releases). Adopt as an OSINT collection tool, source-build only. Low-stakes — a standalone CLI utility, not a stack dependency.

### Adoption status — installed on the laptop (2026-05-19)

Installed K54: `python3 -m pip install --no-binary :all: yt-dlp` — **yt-dlp 2026.3.17**, built from the PyPI source distribution (the `--no-binary :all:` flag forces building from the Unlicense source tarball; the GitHub PyInstaller release binaries — `yt-dlp.exe` / `yt-dlp_macos`, which carry the GPLv3+ static-link encumbrance — were deliberately *not* used). Smoke-tested: `python3 -m yt_dlp --version` → `2026.03.17`. Laptop-side curation/collection tool, consistent with the deployment boundary (a standalone CLI utility, not in any serving path). Re-install via the same source-only command on upgrade.

## Snippets

> "While the pre-compiled binary executables contain tightly bound GPLv3+ code (making those binaries absolute poison pills for the enterprise network), the raw Python source code repository and the PyPI source distributions are strictly governed by the highly permissive Unlicense." [Source: Tool Evaluation and Wiki Fit.docx — URL 19]
