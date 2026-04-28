---
title: "emtwiki.endusergeek.com — deployed Karpathy-pattern wiki for EMT-Basic certification (San Juan College / NM EMS Bureau aligned)"
type: source
tags: [deployed-example, karpathy-pattern, knowledge-base, emt-curriculum, high-stakes-domain, reference-only]
clusters: [llm-agents]
keywords: [emtwiki, endusergeek, emt-basic, nremt, nm-ems-bureau, san-juan-college, deployed-wiki-example]
related:
  - concepts/wiki-tooling-evaluation.md
  - sources/wastedcode-memex.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/llm-wiki.md
maturity: validated
read_status: read
created: 2026-04-28
updated: 2026-04-28
---

## Relations

- @concepts/wiki-tooling-evaluation.md — synthesis page; cited as **reference-only deployed example** demonstrating the pattern is mature for high-stakes domains
- @sources/wastedcode-memex.md — same `endusergeek.com` host pattern (likely same author isingh); plausibly built with `memex`; cross-link kept lightweight without confirming since adoption analysis doesn't depend on it
- @sources/atomicmemory-llm-wiki-compiler.md — alternative tool that could produce this kind of wiki; both point at the same Karpathy-pattern endpoint
- @sources/llm-wiki.md — the Karpathy gist this wiki visibly implements

## Raw Concept

- **Original title**: EMT-B Wiki — *San Juan College EMT-B Program — New Mexico*
- **Author**: Unknown (likely associated with isingh / endusergeek.com — same host pattern as `wastedcode/memex`)
- **Type**: Deployed knowledge-base wiki (web URL, not a tool/repo)
- **URL**: https://emtwiki.endusergeek.com/
- **Retrieved**: 2026-04-28 (via Exa `crawling_exa`)
- **Last updated**: 2026-04-05
- **Domain**: EMT-Basic certification curriculum, NREMT psychomotor + cognitive exam content, NM EMS Bureau protocols (September 2022)
- **Read status**: read (browsed full index and structural shape; not deep-read into individual articles)

## Narrative

emtwiki.endusergeek.com is **a deployed example** of a Karpathy-pattern wiki at production scale in a high-stakes domain (EMT-Basic certification — life-or-death-level accuracy required, NREMT and state-EMS-bureau alignment auditable). It is *not* a tool to evaluate for adoption; it is a **proof-of-concept** that the Karpathy pattern, as implemented by tools like memex / llm-wiki-compiler / kb-server, is mature enough to support real curricula without breaking down.

**Why this matters for the wiki-tooling-evaluation decision:**
1. **Existence of deployed examples raises the floor on "is this pattern production-ready?"** Yes — at least in pedagogical / certification-curriculum domains.
2. **The structural shape is recognizable**: hierarchical sections (Foundations / Core Concepts / Airway / Patient Assessment / Pharmacology / Medical / Trauma / Special Populations / NREMT Skills / Operations / Practice Drills), per-topic articles linked from index, quick-reference table mapping findings → interventions, source-files manifest at the bottom. This is exactly the index/concept/source/log shape our schema codifies — confirming the pattern is convergent across implementations.
3. **Curriculum-as-code framing** ("This wiki is designed as a curriculum, not a reference manual") parallels the workspace's "librarian, not just notes" framing — a wiki that reads top-to-bottom is a different artifact than a wiki that's only ever queried by symbol-grep.

**Structural inventory** (what an example deployed wiki looks like in this style):

- **9 hierarchical sections** with table-of-contents-style navigation: Assessments / Pharmacology / Procedures / Medical Emergencies / Trauma / Special Populations / Operations / Practice Drills / Quick Reference
- **Per-section article tables** with `Article | Drug/Skill/Topic | Key Concept` columns — same shape as our `wiki/index.md` but section-scoped
- **Quick-Reference: Assessment Finding → Intervention** table at the bottom — a curated cross-section index that would be hand-built on a normal wiki but is the kind of "compounding query saved as a wiki page" that llm-wiki-compiler's `--save` flag automates
- **Source Files manifest** at the bottom listing the raw protocol PDFs + supplemental markdown + NREMT skill checklists that fed the wiki — explicit provenance, exactly the source-attribution pattern our `wiki/sources/` carries

**5-step patient assessment sequence** is the curriculum's structural backbone — every intervention article links back to a finding in the assessment sequence. This is the same "bidirectional cross-reference is the value" pattern Vannevar Bush named (cited in `sources/wastedcode-memex.md`) and that our `related:` discipline enforces via lint.

**Pharmacology table** as a worked example of the entity-page pattern:

| Article | Drug | Key Indication |
|---|---|---|
| oxygen | Oxygen | Hypoxia, respiratory distress, chest pain, shock, trauma |
| oral-glucose | Oral glucose | Altered mental status in known diabetic who can swallow |
| aspirin | Aspirin (ASA) | Suspected ACS / cardiac chest pain |
| epinephrine-auto-injector | Epinephrine (EpiPen) | Anaphylaxis with systemic involvement |
| activated-charcoal | Activated charcoal | Certain ingested poisons within 1 hour (check NM protocol) |

This is structurally identical to our `wiki/entities/tickers/` pattern (per-entity article + cross-link + key facts in tabular form). The pattern transfers across domains.

**No tooling fingerprint visible from the rendered wiki** — could be memex, mkdocs, Hugo, custom static-site-generator, plain Obsidian + a static publisher, or any of several Karpathy-pattern tools. The renderer choice is invisible to the user; the *structure* (which is the load-bearing artifact) is the same regardless. This is **good news for adoption**: any tool we pick produces a result that's recognizable as "this kind of wiki," not lock-in to a specific tool's idiosyncratic output format.

**Practice Drills** section deserves a callout: scenario-based drills set in San Juan County applying multiple curriculum sections together. These are the equivalent of our `briefs/` pattern — distilled application-of-multiple-pages output filed back into the wiki. Same structural innovation (compounding query → saved page) the llm-wiki-compiler `--save` flag implements.

## Snippets

### S1 — Curriculum-as-code framing (homepage)

> "This wiki is designed as a curriculum, not a reference manual. Start at the top and work through each section in order. Each section builds on the one before it."

### S2 — 5-step assessment as structural backbone (Assessments section)

> "The five-step patient assessment sequence is the backbone of every patient contact. Every intervention connects back to a finding in this sequence."

### S3 — Source-files manifest (bottom of homepage)

> "raw/protocols/nm-sop-guidelines-treatment-2022.pdf — NM EMS Treatment Guidelines (September 2022) / raw/supplemental/patient-assessment-sequence.md — Full 5-step assessment sequence / raw/supplemental/emt-b-pharmacology.md — EMT-B scope medications / raw/nremt/psychomotor-skills.md — NREMT psychomotor skill station checklists"

[Direct provenance: `raw/` directory in the source tree, mirroring our `wiki/sources/` discipline.]

### S4 — Quick-reference cross-section table (homepage, "Quick Reference: Assessment Finding → Intervention")

> "Absent/inadequate breathing → bvm-ventilation / SpO2 <94% or respiratory distress → oxygen-administration (NRB at 10–15 LPM) / No pulse + not breathing → cardiac-arrest-aed / Major external bleeding → bleeding-control-shock (direct pressure or tourniquet) / Altered LOC + known diabetic + can swallow → oral-glucose / Chest pain, possible ACS → aspirin + oxygen-administration / Anaphylaxis (systemic signs) → epinephrine-auto-injector + oxygen-administration / High MOI, supine patient → spinal-immobilization-supine [...]"

[Worked example of compounding-query-as-saved-page: a hand-curated finding→intervention map that aggregates information from 15+ underlying articles into a single quick-reference table. The kind of artifact `llmwiki query --save` would produce automatically over time.]
