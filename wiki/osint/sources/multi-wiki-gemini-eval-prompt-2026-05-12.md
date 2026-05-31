---
title: Multi-wiki Gemini Deep Research evaluation prompt (2026-05-12)
type: source
tags: [source, prompt, gemini-deep-research, tool-evaluation, multi-wiki, cross-routing, ip-sale-ready, cemini-stack, librarian-stack, cybersec-wiki, image-gen-wiki, seo-wiki, 3d-printing-wiki, workflow]
keywords: [gemini deep research, evaluation prompt, multi-wiki routing, false NO-GO, cross-routing, license posture, tier classification, Adopt, Steal-from, Defer, Reference-only, Reject, anti-hallucination]
related:
  - sources/evaluating-github-repos-trading-stack-2026-05-12.md
  - sources/evaluating-project-links-systems-2-2026-05-12.md
  - sources/evaluating-urls-cemini-project-2026-05-13.md
  - sources/multi-wiki-link-eval-prompt-2026-05-13.md
  - sources/tool-evaluation-wiki-fit-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - entities/tools/openant.md
  - entities/tools/hunk.md
  - entities/tools/ai-marketing-skills.md
  - entities/tools/multi-model-redteam.md
  - entities/tools/claude-code-ultimate-guide.md
  - entities/tools/autots.md
  - entities/tools/veloxdb.md
  - entities/tools/redactdesk.md
  - entities/tools/aisoc.md
  - entities/tools/bug-bounty-agents.md
  - entities/tools/idassist.md
  - entities/tools/sim.md
  - entities/tools/awesome-design-md.md
  - entities/tools/awesome-ralph.md
  - entities/tools/anthropic-harness-design.md
  - entities/tools/hermes-war-room.md
  - entities/tools/voicemode.md
  - entities/tools/codenomad.md
  - entities/tools/supertonic.md
  - entities/tools/accomplish.md
maturity: validated
read_status: deep-read
created: 2026-05-12
updated: 2026-05-21
---

## Relations

- `@sources/evaluating-github-repos-trading-stack-2026-05-12.md` — Doc 1 evaluated under the prior 3-surface prompt; surfaced the false-NO-GO problem this prompt corrects
- `@sources/evaluating-project-links-systems-2-2026-05-12.md` — Doc 2 evaluated under the prior 3-surface prompt; same false-NO-GO problem
- `@concepts/tool-evaluation-framework.md` — methodology framework this prompt operationalizes
- `@concepts/cemini-license-posture.md` — license reject-list referenced in the prompt body
- `@ccc-wiki/concepts/deep-research-evaluation-prompt.md` — v3/v4 lineage; **canonical copy-paste lives in CCC `prompts/`**
- `@ccc-wiki/concepts/cursor-ide-workspace.md` — v4 Cursor-primary harness (surface 7 expansion)

## Raw Concept

- **Title**: Cemini Multi-Wiki Link / Project Evaluation Prompt (v2, May 2026)
- **Author**: Claudio Barone + Claude (Anthropic, claude-opus-4-7) — co-authored revision of the previous 3-surface eval prompt
- **Created**: 2026-05-12
- **Supersedes**: The implicit 3-surface prompt used by `@sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md` + `@sources/gemini-dr-wave4b-osint-2026-04-29.md` (Cemini-prod / librarian-server / workflow surfaces only). That prompt drove ~9 false-NO-GO verdicts on cybersec-/image-gen-/SEO-relevant tools across Doc 1 + Doc 2 evaluations on 2026-05-12.
- **Use**: Copy `## Snippets → ## The prompt (verbatim, copy-paste ready)` into Gemini Deep Research alongside the URL list to be evaluated.
- **Superseded for new batches (2026-05-21):** v3 + v4 at `@ccc-wiki/concepts/deep-research-evaluation-prompt.md` — `prompts/deep-research-multi-wiki-eval-v4-2026-05-21.md` (current), `prompts/deep-research-multi-wiki-eval-v3-2026-05-21.md` (frozen for K53–K55). v3 fixes v2's mislabeled surface 7 ("Workflow") → **CCC wiki**.

> **Archive (v2, May 2026).** Superseded for new eval batches by `@ccc-wiki/concepts/deep-research-evaluation-prompt.md` (v6; eight surfaces incl. `gambling-wiki`). Kept as historical record of the false-NO-GO fix and v1→v2 design changes.

## Narrative

The previous evaluation prompt (used April–May 2026) evaluated each URL against three surfaces only:

1. **Cemini production stack** — the algorithmic-trading server at `/opt/cemini` (financial suite)
2. **Librarian server** — `/opt/cemini-wiki/` wiki serving infrastructure
3. **Workflow** — laptop-side dev tooling for the OSINT-WORKSPACE

That framing systematically generated false-NO-GO verdicts on tools whose primary fit was a **sibling wiki** (cybersec, image-gen, SEO, 3d-printing). Documented examples from Doc 1 + Doc 2 evaluations (2026-05-12):

| Tool | Old verdict | True fit |
|---|---|---|
| Awesome_GPT_Super_Prompting | Reject (Cemini ToS risk) | Cybersec wiki — adversarial AI study corpus |
| TaskExplorer | Reject (no Cemini fit) | Cybersec wiki — Windows kernel introspection |
| codegraph-rust | Reference-only (no Cemini fit) | Cybersec wiki — binary RE / RAG-on-code primitive |
| IDAssist | Reject (no Cemini fit) | Cybersec wiki — IDA-Pro LLM plugin |
| AIRecon | Reference-only (no Cemini fit) | Cybersec wiki — autonomous pentest agent |
| Bug-Bounty-Agents | Steal-from (workflow only) | Cybersec wiki — 43 offensive personas (primary) |
| AiSOC | Steal-from (Cemini orchestrator) | Cybersec wiki — LangGraph SOC orchestrator (also fits Cemini for trade-audit, dual-surface) |
| supertonic | Defer (TTS unrelated to Cemini) | Image-gen wiki — financial-speech TTS for persona ops |
| awesome-design-md | Adopt (OSINT wiki only) | SEO + image-gen wikis — DESIGN.md for any LLM-consumed UI |

This v2 prompt fixes the false-NO-GO by adding **5 wiki surfaces + the Cemini financial suite + workflow = 7 evaluation surfaces**, plus an explicit **cross-routing recommendation** field that the v1 prompt lacked.

### Design changes from v1 → v2

1. **Surfaces expanded** — 3 → 7 (osint-wiki, cybersec-wiki, image-gen-wiki, seo-wiki, 3d-printing-wiki, Cemini financial suite, workflow). Each gets its own ✅/⚠️/❌ cell + reasoning sentence.
2. **Primary-fit recommendation added** — every tool gets a "primary wiki recommendation" line: *"Primary fit: cybersec-wiki (offensive operations)"* or *"Primary fit: OSINT financial research"* — the single best home for the tool. Sometimes None (truly cross-cutting or no fit).
3. **License-posture catalog updated** — added EUPL-1.2 (per Taranis-AI 2026-05-12 catch) and CC-BY-SA-4.0 (per claude-code-ultimate-guide caveat). Re-emphasized: **no LICENSE file = TENTATIVE Reject** for any IP-sale-bearing stack until verified.
4. **Anti-hallucination guidance retained** — the v1 had strong instructions to never invent star counts, never claim a license without verification, mark NOT FOUND when retrieval fails. v2 keeps that block verbatim.
5. **Cross-wiki routing examples block added** — the prompt now contains 3-4 concrete cross-routing examples to anchor the LLM's understanding of when to use the secondary-wiki recommendation slot.

### Operational use

1. Compile URL list (one per line) — typically 20-30 URLs from X-thread saves, podcast notes, conference references, or `research to be indexed/` triage hopper.
2. Open Gemini Deep Research with the v2 prompt + URL list pasted as user message.
3. Wait for Gemini run (typically 15-25 min depending on URL count + page depth).
4. Save the resulting `.docx` to `research to be indexed/`.
5. Run `python3 scripts/preingest_check.py` then ingest via standard 6-step ingest pipeline.
6. For each URL with cross-wiki cells = ✅, follow the per-wiki routing rule from `CLAUDE.md` (stubs vs briefs, depending on substantive depth).

### Token + cost note

This v2 prompt is ~30% longer than v1 due to 7-surface evaluation. Per-URL output is also ~40% longer (5 extra cells in the per-tool table plus the primary-fit and cross-routing-recommendation lines). Net Gemini Deep Research cost increase per evaluation: ~50-70%. Tradeoff vs the ~9 false-NO-GOs per 25-URL doc that required follow-up cross-routing work: clearly positive ROI.

## Snippets

### The prompt (verbatim, copy-paste ready)

> # Cemini Multi-Wiki Link Evaluation Prompt (v2, May 2026)
>
> You are a tool-evaluation analyst with a strict anti-hallucination discipline. You will evaluate each URL in the user's list against **seven evaluation surfaces** + classify each by **tier** + identify a **primary wiki fit** + flag **cross-wiki routing opportunities**.
>
> ## Anti-hallucination guidance (read first, follow always)
>
> - **Never invent stars, contributors, commit dates, or downloads.** If retrieval gives `null` or `not found`, write the cell as `NOT FOUND` — do not estimate.
> - **Never assert a license without confirming a LICENSE file or SPDX badge.** If you cannot find an explicit license, write `NO LICENSE FOUND` and treat as `[TENTATIVE Reject]` for any IP-sale-bearing surface.
> - **Never assert a feature without seeing the code path or README claim.** If the repo's README claims a feature but you cannot confirm it in code/issues, label as `CLAIMED (unverified)`.
> - **Never claim "matches Cemini's needs" without naming the specific Cemini path** (e.g. `agents/orchestrator.py`, `analyst-node prediction layer`). Vague fit assertions are rejected as hallucination-adjacent.
> - **If a URL is unreachable, repo deleted, or returns a 404,** mark `UNAVAILABLE` and proceed to the next URL. Do not synthesize from cached snippets — cached content is not verifiable.
>
> ## The seven evaluation surfaces
>
> Evaluate every URL against all 7. Each surface gets ✅ (clear fit) / ⚠️ (partial fit / caveat) / ❌ (no fit).
>
> 1. **Cemini financial suite** — algorithmic trading stack at `/opt/cemini` (Python + LangGraph + PostgreSQL + Redis Streams + Polymarket/Kalshi adapters). Trading bots, strategy backtesting, market data ingestion, IP-sale-readiness for the financial codebase. Reject ANY tool with AGPL / SSPL / EUPL / PolyForm-Noncommercial / CC-BY-NC / BSL — these are poison-pill licenses for the IP sale.
>
> 2. **OSINT wiki** — financial research wiki served by librarian + queryable via kb-server REST API. Quant finance + prediction markets + threat-actor financial profiling + market microstructure. Source-side workflow tooling welcome (wiki linting, brief audit, gap detection).
>
> 3. **Cybersecurity wiki** — offensive security (pentest / red team / bug bounty / exploit dev / LLM vuln-discovery), defensive ops (SOC / IR / threat hunting / blue team automation), threat actors, MITRE ATT&CK / ATLAS, certifications. **Strong cross-routing target — most "no-Cemini-fit, has-security-content" tools route here.**
>
> 4. **Image-gen wiki** — uncensored / persona / character image generation. ComfyUI nodes, LoRA training, persona-ops (consistent characters), TTS for voice ops on personas, M-series Mac flash-paging for local inference, image-to-X workflows.
>
> 5. **SEO wiki** — local SEO, GBP optimization, GEO/AEO, web design templates, social media tooling, creator marketing, DESIGN.md style references, AI-marketing skill packs.
>
> 6. **3D-printing wiki** — FDM/FFF printing, Bambu, slicers, materials, print farms, store-ops automation. **Low cross-routing density — most general tools won't fit here.**
>
> 7. **Workflow** — laptop-side Claude Code / dev tooling. Skills, MCP servers, terminal-native tools, voice integration, diff viewers, IDE plugins, local-first knowledge tools. **Generally permissive — workflow accepts more licenses since nothing here ships to production.**
>
> ## Tier classification (apply to every URL)
>
> | Tier | Meaning | Trigger |
> |---|---|---|
> | **Adopt** | Install / configure / integrate now | Strong fit in ≥1 surface + clean license + reproducible install + active maintenance |
> | **Steal-from** | Extract specific pattern / code / idea | Useful design / methodology / snippet — but full adoption blocked by license, scope, dependencies, or maintenance |
> | **Defer** | Defer 30-90 days for re-eval | Promising but immature (low stars / recent fork / breaking changes likely) OR pricing/tier-stability concerns |
> | **Reference-only** | Document and forget | Read-the-blog-once value or future-reference utility; no integration intent |
> | **Reject** | Catalog as rejected | License poison pill OR adversarial-AI-violates-ToS OR domain mismatch OR `NO LICENSE FOUND` on IP-sale-bearing surface |
>
> ## Per-URL output template
>
> For each URL, output:
>
> ```
> ## URL N: [Title]
>
> - **URL**: <full URL>
> - **License**: [SPDX or NO LICENSE FOUND or UNVERIFIED]
> - **Stars / Last commit / Open issues**: <num> / <YYYY-MM-DD> / <num> (or NOT FOUND if unretrievable)
> - **Stack**: <runtime/language/framework summary>
> - **Maturity signal**: <one sentence on what activity / community signals indicate>
> - **Tier**: Adopt | Steal-from | Defer | Reference-only | Reject
> - **Primary fit**: <one of: Cemini-financial / OSINT-wiki / Cybersec-wiki / Image-gen-wiki / SEO-wiki / 3D-printing-wiki / Workflow / None>
>
> | Cemini financial | OSINT wiki | Cybersec wiki | Image-gen wiki | SEO wiki | 3D-printing wiki | Workflow |
> |---|---|---|---|---|---|---|
> | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ |
>
> - **Cross-wiki routing**: <list any secondary wikis where a stub / brief should land, with one-sentence why>
> - **Reasoning**: 2-4 sentences on why the tier + primary fit + cross-routing make sense. Cite specific code paths, README sections, or named features — never speak vaguely about "fit."
> - **License risk** (if any): <one sentence on IP-sale implications, ToS concerns, or copyleft chains>
> - **NEEDS VERIFICATION** (if any): <list of specific claims requiring follow-up>
> ```
>
> ## Cross-wiki routing examples (anchor your understanding)
>
> - **Cybersec offensive tool** (e.g. autonomous pentest agent, LLM jailbreak corpus, IDA-Pro plugin): Primary fit = Cybersec-wiki. May be tier Reject for Cemini financial (no fit) but Adopt or Steal-from for cybersec.
> - **Persona TTS / voice-clone tool**: Primary fit = Image-gen wiki (persona-ops). May be Adopt for image-gen, Defer for workflow.
> - **DESIGN.md / UI-style reference**: Primary fit = SEO wiki OR Image-gen wiki. Cross-route to both. Workflow value as Claude Code template library.
> - **LLM observability / monitoring**: Primary fit = OSINT-wiki (Cemini-adjacent) but cross-route to Cybersec-wiki if it includes adversarial-prompt detection.
> - **Local-first knowledge tool** (Obsidian-adjacent, wiki tools): Primary fit = Workflow. Stub in OSINT-wiki tool catalog. Cross-route to all wikis if applicable.
>
> ## License posture (Cemini reject list, current as of 2026-05-12)
>
> **Hard reject for any IP-sale-bearing surface (Cemini financial, OSINT wiki, cybersec wiki, image-gen wiki, SEO wiki, 3D-printing wiki):**
> - AGPL-3.0 (any version)
> - SSPL-1.0
> - EUPL-1.2 (added 2026-05-12 per Taranis-AI)
> - PolyForm-Noncommercial-1.0.0
> - CC-BY-NC (any variant)
> - BSL (Business Source License, any variant)
> - GPL-3.0 (for production-bearing code; OK for laptop-side scripts)
> - **NO LICENSE FOUND** = `[TENTATIVE Reject]` until verified
>
> **OK for any surface:**
> - MIT, Apache-2.0, BSD (2/3-clause), ISC, Unlicense, CC0-1.0, MPL-2.0
>
> **Caveat (case-by-case):**
> - CC-BY-SA-4.0 — Share-Alike copyleft on text/docs. OK to read + copy ideas, NOT OK to fork.
> - LGPL-2.1 / LGPL-3.0 — dynamic linking OK, static-linking + private fork is poison.
> - Workflow-only OK: GPL-3.0 (laptop scripts, never shipped), AGPL-3.0 (only if self-hosted with no derivative-distribution).
>
> ## Summary section (at the end)
>
> After all per-URL evaluations, produce:
>
> ```
> ## Aggregate summary
>
> - **Adopt: N** (list)
> - **Steal-from: N** (list)
> - **Defer: N** (list)
> - **Reference-only: N** (list)
> - **Reject: N** (list)
> - **UNAVAILABLE: N** (list, no further analysis required)
>
> ### Primary-fit distribution
> - Cemini financial: N
> - OSINT wiki: N
> - Cybersec wiki: N
> - Image-gen wiki: N
> - SEO wiki: N
> - 3D-printing wiki: N
> - Workflow: N
> - None: N
>
> ### Cross-routing batch
> List the secondary-wiki stubs / briefs that should be created in each non-primary wiki, batched by target wiki for efficient stub generation.
>
> ### License pattern summary
> - NO LICENSE FOUND: N
> - Poison-pill licenses caught: N (list specific ones)
> - Clean MIT / Apache / BSD: N
> ```
>
> ## Final reminder
>
> If you find yourself writing "would be useful for X" without naming a specific Cemini path, a specific wiki page, or a specific workflow tool — STOP. Mark the cell ⚠️ and document the uncertainty in the Reasoning field. Vague fit is hallucination-adjacent and erodes the prompt's value.
>
> Now evaluate the URLs in the user's list using this template.

### Adaptation notes (for future v5 work)

- **v3/v4 shipped 2026-05-21** — see `@ccc-wiki/concepts/deep-research-evaluation-prompt.md`. v4 keeps **seven surfaces**; Cursor ops fold into CCC surface 7 (no eighth surface, no Cursor-only wiki).
- **3D-printing surface low signal density** — across 49 URLs across Doc 1 + Doc 2, the 3D-printing column generated zero ✅ and one ⚠️ (general "make/STL" mention). May be worth dropping to a 6-surface template if Doc 3 + Doc 4 confirm the same.
- **Workflow + OSINT-wiki overlap** — many tools are both. Consider whether they're really distinct surfaces or whether OSINT-wiki should absorb workflow under a "workflow tooling" sub-area.
- **License-posture catalog drift** — every new poison-pill catch (EUPL, BSL) requires prompt + CLAUDE.md updates. Mechanize the catalog as a separate file referenced by the prompt rather than inlined.

## Dead Ends

- **v1 prompt with 3 surfaces only** — proven inadequate for 2026-05-12 dual-Gemini-eval batch; 9 false-NO-GOs measurable. Documented in this page's narrative; do not re-use v1.
- **Auto-applying cross-routing without user gating** — initial design considered "if cross-wiki = ✅ then auto-create stub." Rejected: stubs need a brief human glance for stub-vs-page-vs-brief decision, and the post-ingest discussion is where that decision happens. Keep cross-routing as a recommendation, not an automation.

## NEEDS VERIFICATION

- `[NEEDS VERIFICATION 2026-05-12]` v2 prompt cost increase estimate (~50-70%) — measured against Doc 3 once next batch runs. Tighten based on real numbers.
- `[NEEDS VERIFICATION 2026-05-12]` 3D-printing low-signal observation — confirm with at least one more 25+ URL batch before considering removal from surface list.
