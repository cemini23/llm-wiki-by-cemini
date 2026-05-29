---
title: Gemini Deep Research — Evaluating GitHub Repos for Trading Stack (2026-05-12, 23 URLs)
type: source
tags: [source, gemini-deep-research, link-evaluation, tool-audit, claude-code, ip-sale-ready, cemini-stack, librarian-stack, workflow]
keywords: [gemini deep research, tool audit, link evaluation, awesome-ralph, AutoTS, voicemode, hunk, veloxdb, claude-code-ultimate-guide, supertonic, codegraph-rust, trellis, ai-marketing-skills, mac-code]
related:
  - sources/evaluating-project-links-systems-2-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/ralph-autonomous-agent-pattern.md
  - entities/tools/pastebar-app.md
  - entities/tools/hunk.md
  - entities/tools/ai-marketing-skills.md
  - entities/tools/claude-code-ultimate-guide.md
  - entities/tools/autots.md
  - entities/tools/trellis.md
  - entities/tools/veloxdb.md
  - entities/tools/taskexplorer.md
  - entities/tools/how-to-train-your-gpt.md
  - entities/tools/website-downloader.md
  - entities/tools/claude-code-projects-index.md
  - entities/tools/awesome-ralph.md
  - entities/tools/jetbrains-air.md
  - entities/tools/awesome-ai-extensions.md
  - entities/tools/voicemode.md
  - entities/tools/vizpilot-ai.md
  - entities/tools/awesome-gpt-super-prompting.md
  - entities/tools/codegraph-rust.md
  - entities/tools/whisper-money.md
  - entities/tools/supertonic.md
maturity: validated
read_status: deep-read
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- `@sources/evaluating-project-links-systems-2-2026-05-12.md` — Doc 2 (sibling Gemini eval, 26 URLs)
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — refined multi-wiki prompt drafted from these two evaluations
- `@concepts/tool-evaluation-framework.md` — three-surface methodology this brief uses
- `@concepts/cemini-license-posture.md` — license reject-list referenced throughout
- `@concepts/ralph-autonomous-agent-pattern.md` — concept extracted from URL 1

## Raw Concept

- **Title**: Cemini Stack & Wiki Stack — Link Evaluation Brief
- **Authoring tool**: Gemini Deep Research (Google)
- **Source filename**: `Evaluating GitHub Repos for Trading Stack.docx`
- **Sha256**: `668920663391ba15...`
- **Size**: 3,099,575 bytes
- **Retrieved**: 2026-05-12
- **Evaluation prompt**: The Cemini three-surface eval prompt (cemini production stack / librarian wiki server / workflow). Lacks cross-wiki dimensions for cybersec / image-gen / seo / 3d-printing — drove false-NO-GO verdicts on cybersec-relevant tools; addressed in `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md`.
- **Read status**: deep-read (all 23 URLs extracted into structured inventory; entity stubs created for each)
- **Location** (canonical): `cemini-librarian:/opt/cemini-bulk/research/Evaluating GitHub Repos for Trading Stack.docx`

## Narrative

23-URL deep-research evaluation. 3 URLs UNAVAILABLE (designer-skills, oh-my-hermes, diffpane — likely retrieval mismatch or repo deletion). 20 evaluable URLs. Recommendation distribution:

- **Adopt: 4** (AutoTS, veloxdb, voicemode, hunk)
- **Steal-from: 4** (awesome-ralph, ai-marketing-skills, claude-code-ultimate-guide, plus partial cross-doc overlap)
- **Defer: 2** (supertonic, JetBrains Air)
- **Reference-only: 5** (Website-downloader, codegraph-rust, Claude-Code-Projects-Index, how-to-train-your-gpt, awesome-ai-extensions)
- **Reject: 5** (PasteBarApp, TaskExplorer, VizPilot_AI, whisper-money, trellis, Awesome_GPT_Super_Prompting)

### Headline calls

**Highest-confidence Adopt**: **AutoTS** ([URL 9](https://github.com/winedarksea/AutoTS)) — MIT, 1.4k stars, won M6 2023 financial forecasting competition, MCP-compatible, scikit-learn idioms. Direct Cemini integration target for the analyst-node prediction layer.

**Highest-confidence workflow Adopts** (laptop-side, not Cemini-prod):
- **voicemode** ([URL 19](https://github.com/mbailey/voicemode)) — MIT, Whisper.cpp + Kokoro, Core ML accelerated on M-series Mac, MCP-native bidirectional voice for Claude Code.
- **hunk** ([URL 20](https://github.com/modem-dev/hunk)) — MIT, TUI diff viewer specialized for AI-generated multi-file changes, Pierre diffs + inline AI annotations.
- **veloxdb** ([URL 16](https://github.com/abeni16/veloxdb)) — MIT, native Tauri+Rust PostgreSQL client with macOS Keychain + SSH-tunnel + ER diagrammer. Ideal Cemini PG admin tool.

**Critical Steal-from**:
- **awesome-ralph** ([URL 1](https://github.com/snwfdhmp/awesome-ralph)) — MIT. The Ralph pattern: file-based memory (`prd.json` + `progress.txt`), segregated `PROMPT_plan.md` / `PROMPT_build.md`, fresh-context loops. See `@concepts/ralph-autonomous-agent-pattern.md` for distilled methodology.
- **claude-code-ultimate-guide** ([URL 17](https://github.com/FlorianBruniaux/claude-code-ultimate-guide)) — CC-BY-SA-4.0, 4.3k stars. 24,000-line guide with 7-module learning path, 181 templates, embedded MCP search server. **Significant cybersec content** (28 CVE catalog + 655 malicious-skill-pattern threat database) — cross-routed to `@cybersecurity-wiki/`.

**Critical Rejects (poison-pill licenses)**:
- **PasteBarApp** ([URL 2](https://github.com/PasteBar/PasteBarApp)) — CC BY-NC 4.0. Non-commercial license = IP-sale poison pill. Reject (4th catalog mode #1 contributor extension).
- **whisper-money** ([URL 10](https://github.com/whisper-money/whisper-money)) — CC BY-NC 4.0. Same poison pill.
- **trellis** ([URL 12](https://github.com/mindfold-ai/trellis)) — AGPL-3.0. Catastrophic IP-sale rejection.
- **Awesome_GPT_Super_Prompting** ([URL 14](https://github.com/CyberAlbSecOP/Awesome_GPT_Super_Prompting)) — GPL-3.0 + adversarial nature violates enterprise API ToS. Reject for OSINT use; cross-routed to cybersec for adversarial AI study.

### Full per-URL inventory (23 URLs)

See entity stubs in `wiki/entities/tools/` for each URL — frontmatter carries `gemini_eval_doc1_url: N` and `phase_0_verdict: …` tags.

| # | Title | License | Tier | Cemini / Wiki / Workflow | Cross-wiki |
|---|---|---|---|---|---|
| 1 | awesome-ralph | MIT | Steal-from | ❌ / ⚠️ / ✅ | — |
| 2 | PasteBarApp | CC BY-NC 4.0 | **Reject** | ❌ / ❌ / ❌ | — |
| 3 | Website-downloader | MIT | Reference-only | ❌ / ⚠️ / ✅ | seo, cybersec |
| 4 | supertonic | MIT (code) + OpenRAIL-M (weights) | Defer | ⚠️ / ✅ / ✅ | image-gen, seo |
| 5 | codegraph-rust | MIT | Reference-only | ❌ / ❌ / ✅ | cybersec |
| 6 | designer-skills | UNAVAILABLE | — | — | — |
| 7 | TaskExplorer | GPL-3.0 | Reject | ❌ / ❌ / ❌ | cybersec |
| 8 | VizPilot_AI | Apache-2.0 | Reject | ❌ / ❌ / ❌ | — |
| 9 | **AutoTS** | **MIT** | **Adopt** | ✅ / ❌ / ✅ | — |
| 10 | whisper-money | CC BY-NC 4.0 | Reject | ❌ / ❌ / ❌ | — |
| 11 | oh-my-hermes | UNAVAILABLE | — | — | — |
| 12 | trellis | AGPL-3.0 | Reject | ❌ / ❌ / ❌ | — |
| 13 | ai-marketing-skills | MIT | Steal-from | ❌ / ❌ / ✅ | seo |
| 14 | Awesome_GPT_Super_Prompting | GPL-3.0 | Reject | ❌ / ❌ / ❌ | cybersec, image-gen |
| 15 | JetBrains Air | proprietary | Defer | ❌ / ❌ / ⚠️ | — |
| 16 | **veloxdb** | **MIT** | **Adopt** | ❌ / ❌ / ✅ | — |
| 17 | claude-code-ultimate-guide | CC-BY-SA-4.0 | Steal-from | ❌ / ❌ / ✅ | cybersec |
| 18 | Claude-Code-Projects-Index | **NOT FOUND** | Reference-only | ❌ / ❌ / ✅ | — |
| 19 | **voicemode** | **MIT** | **Adopt** | ❌ / ❌ / ✅ | image-gen |
| 20 | **hunk** | **MIT** | **Adopt** | ❌ / ❌ / ✅ | — |
| 21 | diffpane | UNAVAILABLE | — | — | — |
| 22 | how-to-train-your-gpt | MIT | Reference-only | ❌ / ❌ / ❌ | image-gen |
| 23 | awesome-ai-extensions | CC0-1.0 | Reference-only | ❌ / ❌ / ❌ | seo |

### Aggregate patterns (vs prior K39 audit findings)

- **No-LICENSE catalog mode #1 occurrence**: 1 new finding (Claude-Code-Projects-Index, URL 18 — popular-looking project with deployed Vercel site, no LICENSE file). Adds to K39 running total (currently 8+ post-gabagool).
- **Mischaracterization risk**: The prompt's three-surface frame (Cemini-prod / librarian-server / workflow) generated FALSE-NO-GO verdicts on cybersec-relevant tools (Awesome_GPT_Super_Prompting jailbreak corpus, TaskExplorer Windows kernel introspection, codegraph-rust tree-sitter + vector hybrid). All would have surfaced as relevant if the prompt had had cybersec-wiki as a target surface. See `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` for the corrective prompt.
- **License posture wins**: 4 hard Rejects on AGPL/CC-BY-NC/GPL/CC-BY-SA — the prompt's reject-list is doing its job.

### What lands as workspace action

- **Adopt now** (laptop-side): voicemode, hunk, veloxdb — file follow-up ROADMAP items.
- **Adopt now** (Cemini-prod): AutoTS — file as analyst-node prediction-layer brief.
- **Steal-from concepts** (laptop-side): Ralph pattern (`@concepts/ralph-autonomous-agent-pattern.md` written), ai-marketing-skills SKILL.md schema + PII sanitizer hook (cross-routed to SEO wiki), claude-code-ultimate-guide TDD prompt structures + CVE database (cross-routed to cybersec-wiki).

## Snippets

### URL 9 (AutoTS, the headline Cemini Adopt)

> Adopt — verified financial forecasting pedigree (won M6 2023 forecasting competition), MCP-native integration surface, scikit-learn API idioms. AutoTS provides immediate Cemini integration via the analyst-node prediction layer.

### URL 1 (awesome-ralph)

> Rather than relying on continuous context windows that degrade over time, the methodology isolates iterations, granting each agent loop a fresh computational context. The system manages state and project memory exclusively through persistent file structures, specifically utilizing Git history, a progress.txt ledger, and a structured prd.json file to track user stories and task completion statuses.

### URL 14 (Awesome_GPT_Super_Prompting, Reject for OSINT but cybersec-relevant)

> The repository operates as a curated directory of jailbreaks, leaked system prompts, prompt injection techniques for GPT-4o/Claude 3.5/DeepSeek R1, with GPL-3.0 copyleft. Adversarial nature violates enterprise API ToS; risks API key bans on the production DeepSeek account.

## Dead Ends

- Three URLs UNAVAILABLE (designer-skills, oh-my-hermes, diffpane) — retrieval engine returned mismatched results or repo inaccessible. Re-attempt with direct GitHub clone if any become priority.
- Prompt-level limitation: three-surface frame missed cybersec / image-gen / seo / 3d-printing relevance for ~6 URLs. Already addressed in the corrective prompt for future evals.

## NEEDS VERIFICATION

- `[CONFIRMED 2026-05-29]` AutoTS M6 competition placement — maintainer paper `docs/catlin_m6_paper.tex` documents **investment decision challenge win**; see @entities/tools/autots.md.
- `[NEEDS VERIFICATION 2026-05-12]` voicemode + hunk star counts and last-commit dates — Gemini eval cited 1.2k / 3.8k stars; spot-check before adoption.
- `[NEEDS VERIFICATION 2026-05-12]` claude-code-ultimate-guide CC-BY-SA-4.0 license — Share-Alike copyleft creates derivation risk; confirm whether "Steal-from" path is "copy ideas, not code" or "fork the repo." The former is fine, the latter triggers SA.
