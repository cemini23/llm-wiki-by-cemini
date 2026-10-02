---
title: "Enforcing database constraints with MS VBA and SQL Server (2610.00633)"
type: source
tags: [source, k278, atto, genealogy, database]
keywords: [k278, constraints, vba, genealogy-db, FILE]
related:
  - concepts/k278-atto-htr-wave.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
read_status: skimmed
---

## Relations

- @concepts/k278-atto-htr-wave.md

## Raw Concept

| File | `arxiv-2610.00633-on-enforcing-database-constraints-using-ms-vba-e.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.00633-on-enforcing-database-constraints-using-ms-vba-e.pdf` |
| Archive | egress-fi 2026-10-02 |
| Retrieved | 2026-10-02 |
| sha256 | `13ccfe3cc4135bfa088d056b587714b87e9f31cfff9075a0a1007cd505054010` |
| Dual-ID | **OSINT K278** |
| arXiv | 2610.00633 |
| Author | Diana Christina Mancas |
| Venue | ICDD 2023, Sibiu, Romania |

## Narrative

A method paper about constraints a database engine cannot enforce on its own.

The author gives a pseudo-code algorithm that maps each unenforceable business rule to a form or control event procedure, using MS VBA against SQL Server. The case study is a genealogy application called GENEALOGIES.

The numbers are the interesting part, because they quantify how much of a genealogy domain will not fit in the schema.

| Measure | Count |
|---------|-------|
| Business rules in the sub-universe | 210 |
| Relational rules (six RDM types) | 172 |
| Non-relational rules (four MDM categories) | 38 |
| Rules SQL Server cannot enforce | **19** |
| Rules the VBA front end enforces | 55 (17 relational + 38 non-relational) |

Two rules are coded as examples. One bounds a lifespan. The other requires spouses to be alive together for at least one day.

The author admits the limits. Only two constraints are shown, for paper length. Uniqueness on binary picture objects cannot be enforced this way either, because the VBA variant type cannot hold objects that large; two of the four such constraints stay unenforced. Portability to other engines is asserted, not demonstrated.

This is a 2023 conference paper, not new work.

Result for Atto: the durable idea is the split. A relational schema carries the rules it can. A validated front end carries the rest. That is the same shape as the Atto human-gated truth layer. The GENEALOGIES rule inventory is a useful checklist of the constraint classes a genealogy store usually needs. It is a pattern note, not an install. No code URL. No clone.
