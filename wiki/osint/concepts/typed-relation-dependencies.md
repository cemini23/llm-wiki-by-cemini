---
title: "Typed Relation Dependencies — imports / bounds / baseline"
type: concept
tags: [wiki-infrastructure, research-methodology, cross-linking]
keywords: [typed-relations, imports, bounds, baseline, cross-links, dependency-graph, machine-actionable]
related:
  - sources/agent-native-research-artifacts-2604.24658.md
  - concepts/agent-native-research-artifacts.md
maturity: validated
created: 2026-05-02
updated: 2026-05-02
---

## Raw Concept

Our `@path/to/page.md` cross-links are untyped — every link looks the same whether it injects a prior definition, propagates a constraint, or enables regression detection. The ARA paper classifies citations into three dependency types that agents can act on. Can we adopt this without adding overhead?

## Narrative

ARA's `related_work.md` replaces passive citations with typed dependencies. We adopt a lightweight version: an optional type prefix on `@` links.

**The three types**:

| Type | Prefix | Meaning | Example |
|------|--------|---------|---------|
| **imports** | `@I` | Injects a prior definition or result that this page depends on | `@I concepts/grpo.md` — "this page uses GRPO as defined there" |
| **bounds** | `@B` | Propagates a constraint, threshold, or assumption from the linked page | `@B concepts/macro-weather-regime.md` — "this strategy only valid in GREEN regime" |
| **baseline** | `@M` (measure) | The linked page is a comparison point or benchmark | `@M sources/toolorchestra-2511.21689.md` — "compare this approach against ToolOrchestra's results" |

**Default**: untyped `@path` links remain valid and mean "general related" — same as today. Types are optional and only used when the relationship is clearly one of the three.

**When to use each**:
- **imports**: "can't understand this page without reading that one first." The linked page provides a definition, formula, or framework this page uses.
- **bounds**: "this page's claims are only valid under the conditions stated there." The linked page constrains scope, regime, or applicability.
- **baseline**: "evaluate this against that." The linked page is a benchmark, competing approach, or reference implementation to compare against.

**Machine-actionable property**: An agent traversing the wiki can follow imports to build prerequisite context, check bounds to verify scope validity, and collect baselines to construct evaluation rubrics — without guessing which links serve which purpose.

**Migration**: no bulk update needed. Apply types on new pages and when editing existing pages. Untyped links remain functional.

## Snippets

- "related_work.md replaces passive citations with typed dependencies that agents can act on: imports inject prior definitions, bounds propagate constraints to hyperparameter search, and baseline entries enable automatic regression detection, transforming literature review into a machine-executable dependency graph." [Source: agent-native-research-artifacts-2604.24658.pdf p.5]
