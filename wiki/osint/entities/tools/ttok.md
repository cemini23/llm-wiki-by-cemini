---
title: ttok — Token-Counting CLI Utility (Simon Willison)
type: entity
tags: [tool, token-counting, cli-utility, cost-discipline, adopt-tier, universal-install, simon-willison]
keywords: [ttok, simonw, token-count, llm-cost-discipline, pre-call-audit, brief-token-estimation]
related:
  - sources/5-5-moarrr-tool-eval.md
  - entities/tools/codegraph.md
  - entities/tools/git-rewind.md
maturity: validated
created: 2026-05-05
updated: 2026-05-08
---

## Relations

- @sources/5-5-moarrr-tool-eval.md — origin source: K31 Gemini DR eval URL 19, **Adopt** tier
- @entities/tools/codegraph.md — companion laptop-side workflow tool (token efficiency via AST indexing); ttok complements by measuring the savings
- @entities/tools/git-rewind.md — companion K31 laptop adoption; ttok measures any text payload, git-rewind's `rewind estimate` measures repo-state token count specifically

## Raw Concept

Ultra-lightweight Python CLI utility by Simon Willison. Single-purpose: **audit, count, and truncate text payloads against specific LLM token limits**. Identified as **Adopt-tier** in the K31 Gemini DR eval (`@sources/5-5-moarrr-tool-eval.md` URL 19).

## Narrative

- **URL**: github.com/simonw/ttok ✓ verified 2026-05-06
- **License**: **Apache-2.0** ✓ verified 2026-05-06 via gh API (matches Simon Willison's standard pattern)
- **Stack**: Python, depends on `tiktoken` (OpenAI tokenizer)
- **Distribution**: `pip install ttok` ✓ verified — installs cleanly via `pip3 install --user`
- **Maintainer**: Simon Willison (high reliability + active maintenance, per his track record across `llm`, `datasette`, `sqlite-utils`, etc.)
- **Stars**: 391 (verified 2026-05-06)
- **Last push upstream**: 2024-05-02 — older but stable; the tokenizer-counting problem doesn't drift much

### Laptop install verified 2026-05-06

```bash
pip3 install --user ttok
# Installs at: ~/Library/Python/3.9/bin/ttok
# Symlinked into: ~/.local/bin/ttok (which is on PATH per npm-prefix convention)

ttok --version  # → ttok, version 0.3
echo "test" | ttok  # → token count
```

Smoke tests (2026-05-06):
- `cat briefs/2026-05-06_hftbacktest-adoption.md | ttok` → **3619 tokens**
- `cat briefs/2026-05-06_guidance-ai-adoption.md | ttok` → **3336 tokens**

Both K31 briefs fit in any reasonable LLM context window. Token counting works correctly via OpenAI's tiktoken library; for DeepSeek-specific counts, manual ~5% adjustment per K-series ingest discipline (DeepSeek tokenizer is tiktoken-compatible but with slightly different boundary behavior on edge cases).

### Cemini-prod install verified 2026-05-08

```bash
pip3 install ttok==0.3
# Installs: ttok 0.3 + tiktoken 0.12.0
# Warning: click dep emits UserWarning about duplicate --tokens param; cosmetic, non-blocking

ttok --version  # → ttok, version 0.3
echo "test" | ttok  # → 3 tokens
echo "The quick brown fox jumps over the lazy dog" | ttok  # → 10 tokens
```

Pinned in `/opt/cemini/requirements.txt`:
```
ttok==0.3  # K31 token-counting CLI (Simon Willison, Apache-2.0)
```

Smoke tests on prod (2026-05-08): output matches expected token counts; CLI functional.

### Why Adopt (universally)

Per K31 eval recommendation: install **universally across the Cemini backend Python environment AND the local macOS developer workstation**. Single-purpose, virtually nonexistent architectural risk.

Use cases for Cemini:

| Use case | Why ttok helps |
|---|---|
| Pre-call token budget audit in DeepSeek wrappers | Verify a prompt fits in the context window before issuing the call (avoids truncation surprises) |
| Brief-staging token estimation | When a brief at `briefs/<file>.md` will be fed to a downstream agent, estimate tokens before scp; pair with `scripts/skill_audit.py` |
| Conductor cost discipline | The audit-trail Phase 1+5 brief (`@briefs/2026-05-05_conductor-audit-trail-phase1.md`) computes per-query cost; ttok provides the input-token half of that |
| Wiki-page token-budget audits | Long source pages (e.g., the 37 KB Kalshi llms.txt page at `@concepts/kalshi-api-reference.md`) — verify they're chunkable for kb-server retrieval |
| K-series ingest discipline | When evaluating whether a paper deep-read fits in DeepSeek's context, count tokens first |

### Integration

```bash
# Laptop install (workspace-side)
pip install ttok

# Pre-call audit example
cat briefs/2026-05-05_polymarket-stack-adoption.md | ttok        # token count
cat briefs/2026-05-05_polymarket-stack-adoption.md | ttok -t 100000  # truncate to 100k

# Cemini-prod side
# Add to /opt/cemini/Pipfile or pyproject.toml
# Use in pre-call hooks in services/llm_analyst/deepseek_client.py
```

### Open questions — resolved 2026-05-08

- ~~License confirmation~~ → ✓ Apache-2.0 verified 2026-05-06
- ~~Cemini-prod-side install~~ → ✓ Installed + smoke-tested 2026-05-08
- ~~Latest version~~ → ttok 0.3, tiktoken 0.12.0; deps minimal
- Tokenizer compatibility — ttok defaults to OpenAI's tiktoken; DeepSeek tokenizer is tiktoken-compatible at the boundary level (verified empirically in K-series ingest discipline; minor edge-case drift acceptable)
- Phase 2: wire into `deepseek_client.py` pre-call audit hook + `AuditEntry.token_count` (per `@briefs/2026-05-05_conductor-audit-trail-phase1.md` Phase 1+5)

### Adoption status

- **Laptop**: ✓ INSTALLED 2026-05-06 (`pip3 install --user ttok` + symlink to `~/.local/bin/ttok`)
- **Cemini-prod**: ✓ INSTALLED 2026-05-08 (`pip3 install ttok==0.3` + pinned in `requirements.txt`)
- **Phase 2 pre-call hook**: pending — wire `count_tokens_via_ttok()` into `deepseek_client.py` + `AuditEntry.token_count`

## Snippets

- **Scope framing** (K31 eval): "Ultra-lightweight, dedicated Python utility engineered exclusively to audit, count, and truncate text payloads against specific LLM token limits." [Source: 5_5 moarrr links.docx URL 19]

- **Recommendation tier**: "Adopt. The software must be installed universally across the Cemini backend Python environment and the local macOS developer workstation. Its single-purpose, highly refined design creates massive operational utility with virtually nonexistent architectural risk." [Source: 5_5 moarrr links.docx URL 19]
