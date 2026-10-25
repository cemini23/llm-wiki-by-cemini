---
title: NPM supply-chain defense prompt (May 2026, TanStack-attack-era)
type: source
tags: [source, prompt, npm, bun, supply-chain, security, defense, tanstack]
keywords: [npm, bun, pnpm, min-release-age, minimum-release-age, save-exact, bunfig.toml, npmrc, lockfile, version pinning, tanstack]
related:
  - concepts/npm-supply-chain-defense.md
maturity: validated
read_status: deep-read
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- `@concepts/npm-supply-chain-defense.md` — distilled concept
- `briefs/2026-05-12_npm-supply-chain-defense-cemini.md` — application brief for Cemini prod (outside wiki/, staging-tracked)

## Raw Concept

- **Title**: "USE THE PROMPT BELOW IN CODEX/CC TO PROTECT YOUR SYSTEM AND CODEBASE FROM NPM SUPPLY CHAIN ATTACKS (LIKE TANSTACK TODAY)"
- **Source filename**: `NPM BUG DEFENSE PROMPT.docx`
- **Sha256**: `269b6e7e3d0d1128...`
- **Size**: 7,329 bytes
- **Retrieved**: 2026-05-12
- **Read status**: deep-read
- **Trigger event**: TanStack package compromise late 2026-05 (the source post calls it out as the contemporary attack)
- **Location** (canonical): `cemini-librarian:/opt/cemini-bulk/research/NPM BUG DEFENSE PROMPT.docx`

## Narrative

Short, actionable Codex/CC-runnable prompt with a 4-step procedure to harden a Node.js development environment against supply-chain attacks. Centered on a **7-day release-age cooldown** plus exact-version pinning plus lockfile-in-git. See `@concepts/npm-supply-chain-defense.md` for full distillation + Coverage limits.

### The 4 steps (verbatim)

1. **`~/.npmrc`** — keep every existing line, append `min-release-age=7`, `minimum-release-age=10080`, `save-exact=true`
2. **`~/.bunfig.toml`** (create if missing) — append `[install]` `minimumReleaseAge = 604800`
3. **Pin every dependency** in `package.json` — strip `^` and `~` from `dependencies`, `devDependencies`, `peerDependencies`. Exact versions only.
4. **Commit the lockfile to git** — `bun.lock` / `package-lock.json` / `pnpm-lock.yaml`

Reporting clause: "report: files changed, deps pinned, anything unexpected."

### Applied 2026-05-12 on workspace laptop

- `~/.npmrc` — 3 cooldown lines appended (prefix preserved)
- `~/.bunfig.toml` — newly created
- `OSINT WORKSPACE/package.json` — `agnix ^0.24.0` → `0.24.0` (1 dep pinned)
- Lockfile: workspace-gitignored already, step 4 N/A for this repo

### Brief staged for Cemini prod

`briefs/2026-05-12_npm-supply-chain-defense-cemini.md` — manual scp to `/opt/cemini/briefs/` per distribution rule; server-side Claude session executes with its own review loop.

### Cross-wiki relevance

This belongs in `@cybersecurity-wiki/concepts/` as a defensive-ops pattern. Cross-routed: `@cybersecurity-wiki/concepts/npm-supply-chain-defense.md` stub created.

## Snippets

### The rationale (verbatim)

> the cooldown makes every package manager refuse any version published in the last 7 days. attack chains usually only last a couple hours, but this protects you long term and for any future attacks... which at this rate will keep happening

### The procedure (verbatim, condensed)

> 1. edit ~/.npmrc. keep every existing line (auth tokens etc), append:
> min-release-age=7
> minimum-release-age=10080
> save-exact=true
>
> 2. edit ~/.bunfig.toml (create if missing). keep existing content, append:
> [install]
> minimumReleaseAge = 604800
>
> 3. in this project, open package.json and pin every dependency:
> strip ^ and ~ from every version under dependencies, devDependencies, and peerDependencies. exact versions only.
>
> 4. commit the lockfile (bun.lock / package-lock.json / pnpm-lock.yaml) so the resolved tree is locked in git. then report: files changed, deps pinned, anything unexpected.

## Dead Ends

- `save-exact=true` does NOT retroactively pin existing dependencies — only affects future `npm install <pkg>` invocations.
- Cooldown does NOT protect against direct `git clone && npm install` of a malicious repo (no registry involvement).
- Cooldown does NOT protect against slow-burn attacks past the 7-day window (xz-utils-style sleepers).

## NEEDS VERIFICATION

- `[OPEN QUESTION 2026-05-12]` TanStack compromise details — author references "LIKE TANSTACK TODAY" without specifying which package or attack vector. Useful to verify against TanStack security advisory + npm registry takedown logs for full attack reconstruction.
