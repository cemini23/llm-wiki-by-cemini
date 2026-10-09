---
title: "Multi-repo revenue evaluation — 20 rows: agent tooling, gateways, feeds (2026-10-09)"
type: source
tags: [source, k287, eval, gateway, agent-tooling, licence-audit]
keywords: [k287, litellm, open-code-review, sogen, daily-stock-analysis, artcraft, rea, lingbot-map]
related:
  - concepts/k287-arxiv-wave.md
  - concepts/k287-feeds-wave.md
  - concepts/active-project-research-routing.md
  - entities/tools/open-code-review.md
  - entities/tools/litellm.md
  - entities/tools/sogen.md
  - entities/tools/daily-stock-analysis.md
  - entities/tools/artcraft-suite.md
  - entities/tools/rea.md
  - entities/tools/treg.md
  - entities/tools/lingbot-map.md
  - entities/tools/magpie.md
  - entities/tools/aleapp.md
  - entities/tools/cc-switch-cli.md
  - entities/tools/blessed-rs.md
  - entities/tools/rakazo.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
read_status: read
---

## Relations

- @concepts/k287-arxiv-wave.md
- @concepts/k287-feeds-wave.md
- @concepts/active-project-research-routing.md
- @entities/tools/litellm.md — gateway Phase-0 verdict NO-GO
- @entities/tools/open-code-review.md — pattern already on file
- @entities/tools/sogen.md — GPL-2.0 NO-GO
- @entities/tools/daily-stock-analysis.md — alert-only, not started

## Raw Concept

| File | `Multi-Repo Revenue Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Repo Revenue Evaluation.docx` |
| Retrieved | 2026-10-09 |
| Dual-ID | **OSINT K287** |
| sha256 | `b36632927d25ce3fa82c00503dbe6374cfced83d6e1c86f40a2d83bfa20ca1f3` |
| Rows | 20 URLs |
| Theme | Developer agent tooling, spatial 3D, binary reverse engineering, financial analytics, hosted inference |

## Narrative

A 20-row eval. The docx licence column is not evidence. Every GitHub row was checked with `gh api` on 2026-10-09. All 18 repositories exist. No row is a missing repo.

### Tier spread (docx)

| Tier | Count | Rows |
|------|-------|------|
| Integrate | 1 | litellm |
| Extract | 6 | open-code-review, artcraft, rea, sogen, daily_stock_analysis, hosted GLM |
| Watch | 1 | lingbot-map |
| Context | 6 | magpie, ALEAPP, cc-switch-cli, blessed-rs, rakazo, illo-skill |
| Pass | 6 | SwiftUI-Agent-Skill, hiring-without-whiteboards, awesome-paseo-plugins, treg, nvidia-macos-driver, marketing URL |

Pass rows stay on this page. They do not get stubs.

### Phase-0 (new Integrate and Extract)

Clones sit under `/tmp/k287-phase0/`. Nothing was installed.

| Repo | gh api | Stars | Last push | Verdict |
|------|--------|-------|-----------|---------|
| `alibaba/open-code-review` | Apache-2.0 | 45,129 | 2026-10-08 | **GO REFERENCE**. Pattern is not new. No brief. |
| `BerriAI/litellm` | NOASSERTION | 60,615 | 2026-10-09 | **NO-GO**. Second gateway. |
| `momo5502/sogen` | GPL-2.0 | 3,659 | 2026-10-09 | **NO-GO**. Licence is not permissive. No lab brief. |
| `ZhuLinsen/daily_stock_analysis` | MIT | 66,099 | 2026-10-05 | **CONDITIONAL-GO**. Alert-only. Needs a yes. Not started. |

`open-code-review` was already **GO REFERENCE** in K262, with `wire_status: wont_wire`. The hybrid pattern is a deterministic filter, then an LLM comment. That pattern is already on @entities/tools/open-code-review.md. K287 refreshes the star count. It does not add a brief.

LiteLLM file text is MIT outside `enterprise/`. The API id stays NOASSERTION because of that split. The policy note is on @entities/tools/litellm.md. A local proxy already listens on 127.0.0.1 port 8791. Do not add a second gateway.

sogen `LICENSE` is GNU GPL version 2. A lab brief is allowed only for a permissive licence. This row has no lab brief.

`daily_stock_analysis` pushes a decision dashboard to chat apps. The README has no broker and no order call. The dashboard still prints buy and sell points. Those points are not orders. The watch is not armed.

### Folds

| Repo | This batch | Prior page |
|------|------------|------------|
| `storytold/artcraft` | Extract, already audited | @entities/tools/artcraft-suite.md. Umbrella repo is **NOASSERTION**, 11,194 stars, pushed 2026-10-09. The seven app repos stay Apache-2.0 from K284. |
| `morluto/rea` | Extract, already audited | @entities/tools/rea.md. **MIT**, 43,530 stars, pushed 2026-10-09. Owned-lab boundary stays. |
| `superdesigndev/treg` | Pass | @entities/tools/treg.md. **NOASSERTION**, 4,932 stars, pushed 2026-10-09. No wire. |

### Watch

`Robbyant/lingbot-map` is **Apache-2.0**, 17,662 stars, pushed 2026-10-06. Stub only. The stack wants CUDA, PyTorch, and Kaolin. That is not a laptop wire. See @entities/tools/lingbot-map.md.

### Context stubs

| Repo | Licence | Stars | Last push |
|------|---------|-------|-----------|
| `yetone/magpie` | MIT | 7,422 | 2026-10-09 |
| `abrignoni/ALEAPP` | MIT | 979 | 2026-10-09 |
| `SaladDay/cc-switch-cli` | MIT | 5,245 | 2026-10-07 |
| `nicoburns/blessed-rs` | none | 1,620 | 2026-08-03 |
| `elie222/rakazo` | Apache-2.0 | 3,576 | 2026-10-09 |

`blessed-rs` docx claimed MIT or Apache-2.0. The API licence field is empty. No install.

`tmchow/illo-skill` is Context. **MIT**, 389 stars, pushed 2026-09-21. Brief only. No local wire. No image-generation install. No entity page.

ALEAPP is not installed. It is a different repo from iLEAPP.

`cc-switch-cli` is not the Rust proxy on @entities/tools/cc-switch.md.

### Pass rows (no stubs)

| Repo or URL | Licence | Stars | Last push | Note |
|-------------|---------|-------|-----------|------|
| `twostraws/SwiftUI-Agent-Skill` | MIT | 5,383 | 2026-10-07 | No Swift in the active stacks. |
| `poteto/hiring-without-whiteboards` | MIT | 52,504 | 2026-09-24 | Hiring list. No code fit. |
| `omercnet/awesome-paseo-plugins` | CC0-1.0 | 59 | 2026-09-22 | Plugin list. |
| `superdesigndev/treg` | NOASSERTION | 4,932 | 2026-10-09 | Fold. See above. |
| `nullmoth/nvidia-macos-driver` | NOASSERTION | 1,823 | 2026-10-09 | GPU repo. Pass. Do not build it. |
| `thefoundation.limestonedigital.com/ai-transformation-operations` | n/a | n/a | n/a | Marketing URL. Pass. |

### Hosted model

`https://platform.experientiallabs.ai/models/glm-5.3-flash-abliterated` is a **hosted model**. The docx called it Extract. Record only. No key. No install. It is not a local weight.

### Phase-1

`scripts/phase1_adopt_inventory.py` is not in this repo. No settings file was edited. No ADOPT row. No new policy bullet. NO-GO rows are `wont_wire`. The daily-stock CONDITIONAL-GO is `deferred` and is not started. `open-code-review` stays `wont_wire` from K262.

### Boundary

No install. No second gateway. No GPU build. No image-generation wire. No order from the stock digest. No scp.

## Snippets

> "Tier: Integrate" for BerriAI/litellm. [Source: Multi-Repo Revenue Evaluation.docx]

> "A local proxy already listens on 127.0.0.1 port 8791. Default NO-GO for a second gateway." [Source: K287 operator order, 2026-10-09]
