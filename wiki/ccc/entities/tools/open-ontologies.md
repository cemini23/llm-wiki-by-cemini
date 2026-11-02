---
title: "open-ontologies — blast-radius planning and Lean-checkable proof certificates (MIT)"
type: entity
tags: [tool, ontology, knowledge-graph, verification, lean, atto, provenance]
keywords: [open ontologies, oo-cert, blast radius, asserted triples, derivations, owl, shacl, lean]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md"
  - "@osint-wiki/entities/tools/lexifina-global-law.md"
maturity: draft
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md, URL 18, **Extract** tier. Routed to Atto and family-tree.

The question this page answers: **can a proposed change to a knowledge graph be certified as sound before it is applied?**

## Narrative

### What it is

A Rust binary, **MIT**, that checks a planned change to a production ontology before it ships. It reports blast radius and risk, and it flags semantic changes that a text diff cannot show.

Reasoning support: OWL/RDFS, SHACL validation, custom rules (SWRL, RIF, Horn tables), satisfiability checks, conservative modules, and crosswalk certification. The MCP server gives Claude or Cursor 39 tools and 5 prompts.

### The workflow

Terraform-shaped: **plan → blast-radius report → apply / rollback.**

The blast-radius report is the part worth having. A text diff on a graph file shows which lines changed. It does not show which downstream conclusions become invalid. This does.

### The certificate

Two tab-separated files:

| File | Content |
|------|---------|
| `asserted.tsv` | The source claims. One triple per line: subject, predicate, object. |
| `derivations.tsv` | One line per inference step: rule, conclusion, premises. |

A separate **Lean checker** verifies the pair. It re-derives each conclusion under the named rule and confirms each premise is either asserted or concluded by an **earlier** line. Inference chains must be ordered.

The verdict distinguishes rule origin:

- Built-in rules → `entailed`.
- User-supplied rules → `entailed_under_supplied_rules`, because those rules are assumptions, not established facts.

`asserted.sha256` binds the certificate to the exact input bytes.

### Phase-0, 2026-11-01 — three findings

**1. The licence is MIT.** The report logged "NOT FOUND in public snippets (verify Cargo.toml and LICENSE)". The README states MIT. That doubt is cleared.

**2. Verification needs no network and no model.** An auditor needs the two files and a Lean build — core Lean, no Mathlib. "The tool streams nothing, and the tool calls no home server." That is the property that makes it usable inside the Atto boundary.

**3. Two caveats the report missed.**

- The digest binds to the **input bytes**, not to the state of the world. A valid certificate says the derivation is sound given those premises. It says nothing about whether the premises are true.
- **In the default in-memory storage mode, `load` followed by `reason` certifies nothing** and prints only a warning. Persistent storage mode is required for reuse across time. A pipeline that forgets this produces empty certificates that still look like successes.

### Fit with Atto — careful reading

The report pairs this with Atto to certify a proposed `truth.ged` mutation. That is the right shape, and the Atto hard ban on auto-merging `truth.ged` is preserved by it: the certificate supports a human decision, it does not replace one.

The honest limit: the certificate proves the **derivation** is valid, not the **conclusion** is true. For genealogy that distinction is decisive. A certificate can prove that "born in Comune X in 1884 implies Stato Civile archive A holds the record" follows from a stated rule. It cannot prove the birth year came from a real record.

So the value is narrower than "certify the family tree". It is: **certify each inference step, and list the asserted facts separately so a human can check those.**

### Status

Extract. MIT cleared. Set persistent storage mode. Keep asserted and inferred triples strictly separate.

## Snippets

> "`asserted.tsv`: the source claims, one triple per line (subject, predicate, object)." / "`derivations.tsv`: one line per inference step, in the order `rule`, `conclusion`, then the premises." [README, fetched 2026-11-01]

> "`{\"ok\":true,\"asserted\":3,\"derivations\":3,\"theorem\":\"OOCert.certificate_sound\"}`" [README, fetched 2026-11-01]

> "With the default in-memory mode, `load` followed by `reason` certifies nothing and prints only a warning." [README, fetched 2026-11-01]

> "MIT." — the whole licence statement. [README, fetched 2026-11-01]

## Dead Ends

- **Treating a valid certificate as proof the facts are true.** The digest binds input bytes. The premises are whatever you asserted.
- **Running in default in-memory mode and treating the output as a certificate.** Nothing is certified.
