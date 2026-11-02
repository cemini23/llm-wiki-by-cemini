---
title: Multi-Wiki Link Revenue Evaluation v10.10 — batch C, 20 URLs (2026-11-02)
type: source
tags: [source, eval, tool-evaluation, revenue-lens]
keywords: [multi-wiki link evaluation, runtime v10.10, phase-0, tool triage, scrapling, kornia, unslop, tokeneconomizer]
related:
  - entities/tools/scrapling.md
  - entities/tools/kornia.md
  - entities/tools/openmed.md
  - entities/tools/unslop.md
  - entities/tools/tokeneconomizer.md
  - entities/tools/misakanet.md
  - entities/tools/boardui.md
  - entities/tools/agent-desktop.md
  - entities/tools/kronos.md
  - sources/arxiv-v10-10-batch-c-skipped-no-lane-2026-11-02.md
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md
maturity: draft
created: 2026-11-02
updated: 2026-11-02
read_status: read
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Cemini Multi-Wiki Link Evaluation — Gemini Deep Research RUNTIME (v10.10) |
| Type | Generated evaluation report, agent-authored and cited |
| Author | Cemini eval pipeline |
| Received | 2026-11-02 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki URL Revenue Evaluation 2026-11-02.docx` — **dated on archive**; the undated name already holds the batch-B docx |
| Duplicate check | `preingest_check.py` returns DUPLICATE on filename. It is a **filename collision, not a content match**: 50,448 bytes here against 3,090 KB for batch B, different sha256, different URLs. Same trap as the two `Multi-Wiki Link Revenue Evaluation` revisions in K295. |
| Batch | 20 URLs, none deferred |
| Lens | revenue plus project fit. Priority #1 Atto and Collectibles (co-equal), #2 GuruWatcher and Basgiath, #3 CeminiDFS, #4 CeminiParlays |

**Third batch to carry the v10.10 label**, after @sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md and @sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md. All 20 URLs are new; none repeat an earlier batch. The runtime version string appears not to advance between runs, so treat "v10.10" as a pipeline label, not a batch identity.

Batch theme: agent harness orchestration and cost control, computer vision and media pipelines, adaptive web scraping, financial time-series foundation models, local MoE serving, local PII NER, frontend polish, and game-studio agent workflows.

## Narrative

### Tier table

| # | Tool | Tier | Primary wiki | Project fit | License (verified) |
|---|------|------|--------------|-------------|--------------------|
| 1 | vercel-labs/agent-desktop | **Extract** | CCC | collectibles, atto | Apache-2.0 |
| 2 | D4Vinci/Scrapling | **Integrate** | CeminiSuite | collectibles | BSD-3-Clause |
| 3 | hyprwm/Hyprland | Pass | CCC | none | BSD-3-Clause |
| 4 | Donchitos/Claude-Code-Game-Studios | **Extract** | Game-dev, CCC | basgiath | MIT |
| 5 | FlashML-org/FreeToken | Watch | Cybersec | local-abliterated-lab | Apache-2.0 |
| 6 | pingdotgg/t3code | Context | CCC | none | MIT |
| 7 | kornia/kornia | **Integrate** | Image-gen | collectibles | Apache-2.0 |
| 8 | shiyu-coder/Kronos | Watch | OSINT | guruwatcher, xsp-killer | not stated |
| 9 | max-sixty/worktrunk | **Extract** | CCC | atto, collectibles | MIT OR Apache-2.0 |
| 10 | p-e-w/heretic | **Extract** | Cybersec | local-abliterated-lab | not found |
| 11 | thdxr/environment | Pass | CCC | none | not found |
| 12 | maziyarpanahi/openmed | **Extract** | OSINT | atto, family-tree | Apache-2.0 SDK, models differ |
| 13 | deepcoldy/botmux | Pass | CCC | none | MIT |
| 14 | Ikalus1988/MisakaNet | **Extract** | CCC | atto, collectibles | MIT |
| 15 | penso/herdr-gpui | Context | CCC | none | Apache-2.0 |
| 16 | ducha-aiki/kornia | UNAVAILABLE | Image-gen | none | n/a |
| 17 | Imagination-Studio (keys/Wasserman) | Watch | Image-gen | basgiath | Apache-2.0 |
| 18 | heydamir/unslop | **Integrate** | CCC, SEO | atto | CC-BY-4.0 |
| 19 | BoardUI/boardui | **Extract** | CCC | atto, collectibles | MIT, Pro tier commercial |
| 20 | microsoft/TokenEconomizer | **Integrate** | CCC | atto, collectibles | Apache-2.0 |

Tally: 4 Integrate, 7 Extract, 3 Watch, 2 Context, 3 Pass, 1 unavailable.

**This is the highest-action batch of the three.** The first two produced one Integrate between them.

### Phase-0, 2026-11-02

GitHub egress is denied in the session sandbox, so no clones. Checks used README and LICENSE files fetched from the raw content hosts. That confirms licence text and stated capability. It does not confirm commit depth, issue counts, or whether the code does what the README claims.

| Tool | Report claim | Phase-0 finding | Effect |
|------|--------------|-----------------|--------|
| Scrapling | "StealthyFetcher (automated Cloudflare Turnstile/Interstitial bypass and TLS/HTTP3 fingerprint spoofing)" drives the Integrate | BSD-3-Clause confirmed. The README states it "Can easily bypass all types of Cloudflare's Turnstile/Interstitial with automation" — and **describes no mechanism**. The project's own disclaimer says it is "for educational and research purposes only", requires users to "Always respect the terms of service of websites and robots.txt files", and leaves `robots_txt_obey` **opt-in, not default**. | The Integrate rests on a protection-bypass the vendor disclaims for the stated use. See the separate finding below. |
| kornia | "10x–70x faster eager, >100x with torch.compile" against OpenCV preprocessing | Apache-2.0 confirmed. The speed claim is for **batched tensors on a GPU**. The README states directly that **"OpenCV outperforms Kornia for single-image `uint8` CPU work."** Also: "No CI job covers CUDA or MPS half precision." | Card scanning processes **one image at a time**. At batch size 1 on macOS, the reported speedup does not apply. The value is in the *operators* — RANSAC homography, CLAHE, LightGlue matching — not in throughput. |
| TokenEconomizer | "cuts Claude Code and Codex token burn by 18.4%–30.9%" | Apache-2.0 confirmed. The README reports **cost**, not tokens: "18.4–30.9% lower mean cost" on SWE-Bench, 277 tasks across six repositories and five agent–model combinations, lower in all 30 cells. Web-Bench 16–21% lower. Pass@1 improved in 4 of 5 combinations. State lives in `~/.tokeneconomizer`. | Correct the metric: it is **cost reduction on SWE-Bench**, not a token-count reduction. The benchmark is software engineering, not this workflow. |
| unslop | Licence listed as CC-BY-4.0 | Confirmed CC-BY-4.0. Redistributing the **skill files** requires attribution to Damir Sokolovsky (@heydamir) with a link back. CSS and React edits to your own app are not affected. Installs to `~/.claude/skills/unslop`. | Attribution obligation applies only if the skill files are redistributed. It edits real source code and may offer to connect an image-generation service — it asks first. |
| openmed | "Apache-2.0 — permissive, cleanly avoids Atto's GPL vendor ban" | Repository exists on **`master`**, not `main` (the `main` raw URL 404s). 5.8k stars. **The SDK is Apache-2.0; the README states model and dataset licences differ**, with third-party notices in a NOTICE file. 42 PII language codes, **35 model-backed**. MLX runs "24–33× faster than CPU PyTorch". | The GPL-clearance claim holds for the **SDK only**. Check each model weight licence before bundling in an Atto kit. **Italian is not in the language list the fetch returned** — verify before planning on it. @entities/tools/openmed.md updated. |
| worktrunk | MIT OR Apache-2.0 | Confirmed. This closes the existing page's "licence unreported, never cloned" gap. | @ccc-wiki/entities/tools/worktrunk.md updated. |
| ducha-aiki/kornia | 404 | The report already marks it unavailable; canonical upstream is `kornia/kornia` (URL 7). | No action. |

### The Scrapling finding — read this before integrating

The report's Integrate is for one capability: getting past Cloudflare Turnstile and interstitial challenges on card-comp and population-report portals.

Three things are true at once:

1. **The capability is real and documented by its own project.** The README claims it plainly.
2. **The project disclaims this use.** "For educational and research purposes only", and respect robots.txt and site terms.
3. **The mechanism is not described.** The README says "with automation" and stops.

That third point is the practical problem. A capability that is claimed but not explained cannot be assessed for reliability or for what it does to the target site. It may break silently when the target changes.

**The recommendation belongs to the operator, not to this page.** Scrapling ships non-stealth fetchers — plain HTTP, a dynamic browser without evasion, adaptive parsing that survives layout changes. Those are ordinary scraping and carry no special question.

The StealthyFetcher path is different in kind: it defeats an access control the site owner put there deliberately. Whether to use it is a legal and business decision about the specific sites involved. It is not a technical decision, and this evaluation cannot make it.

**Do not route any of this to CeminiParlays.** The report already imposes a no-scrape contract there.

### The three combos worth running

1. **Scrapling (non-stealth) + kornia → Collectibles.** Ingestion and preprocessing. Kornia at batch size 1 is a question of operator quality, not speed.
2. **unslop + BoardUI → Atto.** BoardUI supplies accessible React Aria and Tailwind v4 components with an `AGENTS.md` and `llms.txt` rule set; unslop audits and removes generic AI styling. The report ties this to conversion on the kit and Access-share surfaces.
3. **worktrunk + MisakaNet + TokenEconomizer → CCC, Atto, Collectibles.** Parallel worktrees, local BM25 failure memory, and tool pruning. These three are the only items in the batch that change how the operator works rather than what a project does.

### Everything else

- **Watch.** FreeToken — blocked by 436 open issues and unverified NVFP4 and KV-cache stability on consumer hardware. Kronos — blocked by Qlib daily-equity assumptions, an unstated licence, and a demo pipeline stale since 2026-07-04. Imagination-Studio — blocked by 64–128 GB unified memory and 125–400 GB disk, plus a recent GPU thermal bug.
- **Context.** t3code (Effect RPC orchestration boundary, `evals/` harness for MCP tool-schema interpretation). herdr-gpui (GPUI multi-agent terminal splits).
- **Pass.** Hyprland (Linux Wayland), thdxr/environment (personal dotfiles), botmux (Feishu/Lark transport).

## Snippets

> "URL 2 (D4Vinci/Scrapling: hardens Cloudflare-protected eBay/130point/CardLadder/TCGplayer sold-comp and pop-report scraping + background XHR capture in /Users/claudiobarone/Projects/collectibles…)" — report, aggregate summary

> "Can easily bypass all types of Cloudflare's Turnstile/Interstitial with automation." — Scrapling README [fetched 2026-11-02]

> "This work is licensed under the BSD-3-Clause License." — Scrapling README [fetched 2026-11-02]

> "OpenCV outperforms Kornia for single-image `uint8` CPU work." — Kornia README [fetched 2026-11-02]

> "18.4–30.9% lower mean cost" on SWE-Bench, 277 tasks, lower in "all 30" repository × combination cells. — TokenEconomizer README [fetched 2026-11-02]

> "42 PII language codes, of which 35 are 'model-backed'". The SDK is Apache-2.0; "model and dataset licenses differ". — openmed README [fetched 2026-11-02]

## Dead Ends

- **Treating kornia's 10x–70x as a card-scanning speedup.** The claim is batched-GPU. At batch size 1 on macOS, the README says OpenCV wins.
- **Citing the token figure for TokenEconomizer.** The published number is cost, on SWE-Bench, not tokens.
- **Reading "Apache-2.0" on openmed as covering the model weights.** It covers the SDK. The README says model and dataset licences differ.
- **Assuming the v10.10 label means these URLs were seen before.** All 20 are new. Three separate batches share the label.
