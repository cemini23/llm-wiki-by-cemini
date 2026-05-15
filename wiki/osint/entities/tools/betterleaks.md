---
title: "Betterleaks — Secret Detection with CEL Filtering (Aikido Security)"
type: entity
tags: [entity, tool, security, secret-detection, pre-ip-sale, go, adopt]
keywords: [betterleaks, secret-detection, cel-filtering, nltk-false-positive, gitleaks-successor, pre-ip-sale-audit, credential-scanning]
related:
  - sources/multi-wiki-tool-evaluation-v3.md
  - concepts/npm-supply-chain-defense.md

maturity: validated
created: 2026-05-15
updated: 2026-05-15
---

## Relations

- @sources/multi-wiki-tool-evaluation-v3.md — K45 source evaluation (Adopt tier, WARN 82)
- @concepts/npm-supply-chain-defense.md — secret scanning is the detection layer for supply-chain defense


## Raw Concept

From the K44 multi-wiki tool evaluation (Gemini Deep Research v3, "Tool Evaluation for Cemini Wiki Integration.docx"). Listed as highest-priority Adopt item for pre-IP-sale codebase audit. Betterleaks is a Go-based secret detection tool built by the Gitleaks creator, maintained by Aikido Security. Key differentiators from Gitleaks: CEL-based contextual rule filtering (more expressive than Gitleaks' `[[allowlist]]`), secrets validation via async HTTP requests from within CEL rules, and natural-language false-positive reduction using an embedded NLTK words corpus (marketed as "Token Efficiency filtering").

## Narrative

### Phase-0 source audit (2026-05-15)

**Repository**: `betterleaks/betterleaks` (GitHub)
**License**: MIT (confirmed — Zachary Rice copyright, standard MIT text in LICENSE file)
**Stars**: 944 (as of 2026-05-15)
**Forks**: 59
**Open Issues**: 39
**Created**: 2026-02-03 (~3.5 months old)
**Last Commit**: 2026-05-11 (4 days ago — active maintenance)
**Maintainer**: Aikido Security (commercial backing) + Zachary Rice (original Gitleaks author)

| Gate | Check | Result |
|------|-------|--------|
| G1 | License verification | **PASS** — MIT, clean IP-sale surface |
| G2 | Star/fork ratio | **PASS** — 944★ / 59 forks = 16:1, healthy for 3.5-month-old security tool |
| G3 | Commit cadence | **PASS** — 133 commits, active weekly cadence since creation |
| G4 | Dependencies audit | **PASS** — Go modules, clean `go.mod` (28 direct deps, no GPL/AGPL contamination) |
| G5 | CEL filtering claims | **PASS** — `celenv/` directory contains full CEL environment with custom bindings for HTTP validation, AWS, crypto, JSON, time; `filter.go` + `prefilter.go` confirm the architecture |
| G6 | BPE / natural-language false-positive reduction | **CONDITIONAL-GO** — Uses embedded NLTK words corpus (`words/words.txt.gz`, ~58k English words) not true BPE tokenization. Checks detected strings against dictionary word ratio; non-word strings (high entropy) flagged as likely secrets. Serves same purpose but marketing overstates sophistication. Effective for false-positive reduction, just not BPE. |
| G7 | Architecture | **PASS** — Clean Go structure: `detect/` (engine), `sources/` (git/filesystem/github scanners), `report/` (output), `config/` (rule definitions). Extensible rule format in TOML. |

**Verdict: GO** — Phase-0 confirms betterleaks is a credible secret-detection tool suitable for pre-IP-sale codebase scanning. G6 (BPE claim) is marketing puffery — it's NLTK dictionary-based filtering, which is simpler but effective. This does not block adoption.

### Adoption plan (3-phase)

1. **Pre-IP-sale scan** (immediate, ~2 hours): Install betterleaks via Homebrew (`brew install betterleaks`), run against all Cemini repos + OSINT workspace, review findings, remediate any true positives
2. **CI/CD integration** (post-IP-sale): GitHub Actions pre-commit hook via `.pre-commit-hooks.yaml`
3. **Sister-wiki deployment** (optional): Roll out across cybersec-wiki, ccc-wiki repos as part of standard toolchain

### Key differentiators vs Gitleaks

| Feature | Gitleaks | Betterleaks |
|---------|----------|-------------|
| Rule filtering | `[[allowlist]]` (regex + path + commit) | CEL expressions (Turing-complete, context-aware) |
| Secret validation | None (static only) | Async HTTP validation from within CEL rules |
| False-positive reduction | Stopwords only | NLTK words corpus (58k English words) |
| Scan sources | Git, filesystem, stdin | Git, filesystem, GitHub org/user/PR, stdin |
| Performance | ahocorasick + re2 | ahocorasick + re2 + parallelized sources |

### Architecture notes (Steal-from potential)

The CEL environment (`celenv/`) is the most architecturally novel component — custom CEL bindings for AWS, HTTP, JSON, and cryptographic operations that allow rules to express complex conditional logic. This pattern is reusable beyond secret detection: any rule engine that needs context-aware filtering could adopt the CEL-environment approach. The `celenv/bindings_filter.go` and `celenv/filter.go` files are the primary extraction targets.

The NLTK-words approach (embedded compressed wordlist with lazy singleton loading) is a lightweight pattern for false-positive reduction that could be ported to other detection pipelines.

## Snippets

> "Betterleaks is a tool for finding secrets like passwords and API keys." [Source: betterleaks README.md, retrieved 2026-05-15]

> "CEL-based filtering: Write contextual rule filters that evaluate fragment (data chunks) attributes (like git author, commit message, and file path) and finding data to reduce false positives." [Source: betterleaks README.md, retrieved 2026-05-15]

> "Token Efficiency filtering: Filter out natural language false positives by using BPE tokenization to measure how 'rare' or non-human a string is." [Source: betterleaks README.md — NOTE: actual implementation uses NLTK words corpus, not BPE tokenization; marketing overstates technical sophistication]

## Dead Ends

- **Waiting for Gitleaks to add CEL filtering** — Gitleaks development has slowed; betterleaks is the successor by the same author. Waiting would mean deferring the pre-IP-sale scan indefinitely.
- **Building a custom secret scanner** — 3+ weeks of engineering for a worse result. Betterleaks has 944★ community validation, Aikido commercial backing, and a rule ecosystem Gitleaks never built. Build-vs-buy strongly favors buy here.
