---
title: git-rewind — AI-Powered Git State Briefing CLI (Rust)
type: entity
tags: [tool, dev-workflow, git-utility, rust, openai-compatible, adopt-tier, laptop-only]
keywords: [git-rewind, rust-cli, ai-git-briefing, openai-api-base-override, workflow-utility, deepseek-compatible]
related:
  - sources/5-5-moarrr-tool-eval.md
  - entities/tools/codegraph.md
  - entities/tools/leaf.md
  - entities/tools/ttok.md
  - entities/infrastructure/deepseek-api.md
maturity: draft
created: 2026-05-05
updated: 2026-05-06
---

## Relations

- @sources/5-5-moarrr-tool-eval.md — origin source: K31 Gemini DR eval URL 3, **Adopt** tier
- @entities/tools/codegraph.md — companion laptop-side workflow utility (token-efficient AST indexer); both serve Claude Code dev sessions
- @entities/tools/leaf.md — companion laptop-side terminal markdown viewer; same workflow tier
- @entities/tools/ttok.md — companion token-counter; ttok measures any text payload, git-rewind's `rewind estimate` measures the repo-state payload specifically
- @entities/infrastructure/deepseek-api.md — git-rewind supports any OpenAI-compatible endpoint via `OPENAI_API_BASE` override; DeepSeek API is OpenAI-compatible, so git-rewind can reuse Cemini's existing DeepSeek key

## Raw Concept

AI-powered command-line interface developed in Rust. Evaluates the current state of a Git repository and provides a **natural-language briefing** to the developer. Reads branch histories, recent commits, working-tree state. Identified as **Adopt-tier** in the K31 Gemini DR eval (`@sources/5-5-moarrr-tool-eval.md` URL 3).

**Important correction to K31 eval framing**: the eval emphasized Ollama-only local operation. Verified 2026-05-06: git-rewind actually supports **any OpenAI-compatible endpoint** via `OPENAI_API_BASE` env-var override (confirmed in upstream README). This means it works equally well with Ollama (local), DeepSeek API (Cemini's existing brain), Groq, Gemini, OpenAI — privacy-friendly path is preserved (you choose the endpoint).

## Narrative

- **URL**: `https://github.com/Chronos778/git-rewind` ✓ verified 2026-05-06
- **License**: **MIT per `Cargo.toml` metadata** but **NO LICENSE file in repo** (verified 2026-05-06 via gh API). This is a soft-license-intent signal, not a hardened legal artifact. CONDITIONAL for IP-sale-readiness; ACCEPTABLE for laptop-only dev tool. Filed upstream as [issue #2](https://github.com/Chronos778/git-rewind/issues/2) 2026-05-06; not blocking.
- **Stack**: Rust binary (pre-built releases for `x86_64-apple-darwin`, `aarch64-apple-darwin`, Linux variants, Windows)
- **LLM integration**: Multi-provider via `OPENAI_API_BASE` env-var; supports Groq > Gemini > OpenAI (priority order with cost-discipline framing) + any OpenAI-compatible endpoint (Ollama, DeepSeek, vLLM, etc.)
- **Maintainer / maturity**: `Chronos778`, 16★, 0 issues, created 2026-05-02, last push 2026-05-05. **Very young + small.** Pin version aggressively; treat as low-stakes Adopt with bus-factor caveat.
- **Latest version**: 1.1.4 (verified 2026-05-06)

### Why Adopt for laptop-side workflow

Per K31 eval recommendation: install locally on the primary macOS laptop. Synergizes with the existing Karpathy LLM Wiki-pattern workflow without exposing proprietary research or codebase to external LLM providers.

Use cases:
- "What did I touch last in this branch?" — natural-language summary of recent activity
- Pre-commit context check before authoring a commit message
- Cross-session resume — synergizes with `hot.md` session-state cache

### Integration with existing laptop tooling

Cemini's laptop already has:
- **codegraph** v0.7.3 (K28 Adopt) — AST indexing for Claude Code
- **leaf** v1.18.2 (K28 Adopt) — terminal markdown viewer
- **Ollama** runtime (local LLM substrate; deployed on librarian, available via SSH tunnel from laptop)

git-rewind plugs into the same workflow tier. All three are local-only, Ollama-compatible, no server-side ops impact.

### Install — verified 2026-05-06

Three distribution paths exist (per upstream README):

1. **Auto-install script** (preferred — no Rust toolchain needed):
   ```bash
   curl -fsSL https://raw.githubusercontent.com/Chronos778/git-rewind/main/install.sh | bash
   ```
   ⚠ **Known bug 2026-05-06**: upstream `install.sh` checksum-verification step references a `.sha256` URL that returns 404 for the latest release. The script parses the 404 body ("Not Found") as the expected checksum, fails comparison, exits. **Workaround used**: manually downloaded the binary tarball from the release page and extracted to `~/.local/bin/`. Filed upstream as [issue #1](https://github.com/Chronos778/git-rewind/issues/1) 2026-05-06; not blocking.
2. **Cargo install** (requires Rust toolchain — Cemini laptop doesn't have one per K28 leaf decision):
   ```bash
   cargo install git-rewind
   ```
3. **Manual pre-compiled binary** (fallback used 2026-05-06):
   ```bash
   curl -fsSL -o /tmp/rewind.tar.gz \
     https://github.com/Chronos778/git-rewind/releases/download/v1.1.4/rewind-aarch64-apple-darwin.tar.gz
   tar -xzf /tmp/rewind.tar.gz -C ~/.local/bin
   chmod +x ~/.local/bin/rewind
   rewind --version  # → git-rewind 1.1.4
   ```

### Configure for DeepSeek (Cemini's existing brain)

Per the upstream README, `OPENAI_API_BASE` overrides the API endpoint. DeepSeek API is OpenAI-compatible (per `@entities/infrastructure/deepseek-api.md`), so the existing Cemini DeepSeek key works:

```bash
# Add to ~/.zshrc or shell profile:
export OPENAI_API_BASE="https://api.deepseek.com/v1"
export OPENAI_API_KEY="<existing DeepSeek key>"
export OPENAI_MODEL="deepseek-v4-flash"  # or deepseek-v4-pro for deeper analysis
```

OR use Groq/Gemini for free-tier laptop dev (rewind prioritizes Groq > Gemini > OpenAI when multiple keys are set).

OR use Ollama via SSH tunnel from librarian (port 11434):
```bash
export OPENAI_API_BASE="http://localhost:11434/v1"
export OPENAI_API_KEY="ignore"  # pragma: allowlist secret  (literal placeholder; Ollama ignores key)
```

### Open questions — resolved 2026-05-06

- ✓ Exact GitHub URL: `Chronos778/git-rewind`
- ✓ License: MIT per Cargo.toml; NO LICENSE file (CONDITIONAL — laptop-acceptable)
- ✓ Distribution: install.sh / cargo / pre-built binary (use binary path on laptop)
- ✓ Star count: 16; created 2026-05-02; last push 2026-05-05; v1.1.4
- ⚠ Bus factor: single maintainer, very young project — pin version, treat as low-stakes Adopt
- ✓ Ollama compatibility: confirmed via `OPENAI_API_BASE` override; reuses Cemini's existing DeepSeek key trivially

### Adoption status — laptop INSTALLED 2026-05-06

- Binary at `~/.local/bin/rewind` (chmod +x verified)
- `rewind --version` → `git-rewind 1.1.4`
- `rewind --dry-run` works without API key (raw git state output verified on this repo)
- `rewind estimate` works without API key (returns token count for current repo state)
- API-backed commands (default `rewind`, `rewind commit`, `rewind ask`) require API key configuration via `rewind config set <provider> <key>` or env vars — **deferred to user** (provider/cost-discipline choice)
- Cemini-prod-side: NOT installed. git-rewind is a developer-workflow tool, not a production-stack component.

## Snippets

- **Scope framing** (K31 eval): "Artificial Intelligence-powered command-line interface developed in Rust that evaluates the current state of a Git repository and provides a natural-language briefing to the developer. Operating directly within the local repository, it reads branch histories, recent commit[s, working-tree state]." [Source: 5_5 moarrr links.docx URL 3]

- **Recommendation tier (privacy-friendly framing)**: "Adopt. The developer should install the utility locally on the primary macOS laptop to enhance the workflow sequence. Because the architecture supports local Ollama instances, it synergizes perfectly with the existing Karpathy LLM Wiki-pattern workflow without exposing proprietary research or codeba[se]." [Source: 5_5 moarrr links.docx URL 3]
