---
title: NPM supply-chain defense — release-age cooldown pattern
type: concept
tags: [concept, security, npm, supply-chain, bun, package-manager, ip-sale-ready]
keywords: [npm, supply-chain attack, min-release-age, minimum-release-age, bunfig, tanstack, save-exact, version pinning, lockfile]
related:
  - sources/npm-supply-chain-defense-prompt-2026-05.md
  - concepts/cemini-license-posture.md
  - entities/tools/betterleaks.md
  - "@cybersecurity-wiki/concepts/npm-supply-chain-defense.md"
  - entities/tools/no-mistakes.md
maturity: validated
created: 2026-05-12
updated: 2026-10-25
---

## Relations

- `@sources/npm-supply-chain-defense-prompt-2026-05.md` — original prompt
- `@concepts/cemini-license-posture.md` — sibling supply-chain hygiene concept (license-level)
- `@cybersecurity-wiki/concepts/npm-supply-chain-defense.md` — cybersec-side defensive-ops counterpart
- `briefs/2026-05-12_npm-supply-chain-defense-cemini.md` — application brief for Cemini (outside wiki/, staging-tracked)

## Raw Concept

Trigger: TanStack package compromise late 2026-05 (per source prompt). The defense pattern — a 7-day release-age cooldown — was widely circulated as a quick, recoverable mitigation that does not require auditing every dependency.

## Narrative

### The attack window

Modern npm/yarn/pnpm/bun supply-chain attacks follow a recurring shape:

1. Attacker compromises maintainer credential (phished, leaked token, malicious-PR-merged-by-distracted-maintainer).
2. Attacker publishes a malicious version of a popular package — often a patch bump (`x.y.z+1`) so semver-range installs (`^x.y.z`, `~x.y.z`) auto-pull it.
3. Within hours, CI pipelines + dev `npm install` invocations + cron-updated containers pull the malicious version. Payload runs.
4. Detection: somewhere between minutes (security tooling firing) and days (after damage). npm registry typically takes the package down within 24-48h.

The defense pattern blocks step 3 specifically: refuse to install any package published within the last 7 days. The attack window typically closes in under 24h; a 7-day cooldown survives with substantial margin.

### The four-step recipe (per source prompt)

1. **`~/.npmrc`** — preserve existing lines, append:
   ```
   min-release-age=7
   minimum-release-age=10080
   save-exact=true
   ```
   `min-release-age` (days) is the newer npm 11+ form; `minimum-release-age` (minutes, 10080 = 7 days) handles older CLI versions. `save-exact` strips `^` / `~` on `npm install <pkg>`, writing exact versions.

2. **`~/.bunfig.toml`** — create if missing:
   ```toml
   [install]
   minimumReleaseAge = 604800
   ```
   604800 seconds = 7 days. Bun-specific.

3. **Pin every dependency** in `package.json` — strip `^` and `~` from `dependencies`, `devDependencies`, `peerDependencies`. Exact versions only.

4. **Commit the lockfile to git** — `bun.lock` / `package-lock.json` / `pnpm-lock.yaml`. Locks the resolved transitive tree, not just direct deps.

### Escape hatch

When a brand-new patch is genuinely needed (vulnerability fix shipped today), override per-invocation:

```bash
npm install <pkg>@<exact-version> --min-release-age=0
bun add <pkg>@<exact-version> --minimum-release-age=0
```

Default-deny + per-call override is the right ergonomic. Don't disable globally.

### Coverage limits — what this doesn't catch

- Slow-burn attacks where malicious payload sits dormant past the 7-day window. The 2024 `xz-utils` backdoor is a non-npm but adjacent example — 2+ year sleeper.
- Compromised dependencies you already have pinned (no install happens, no cooldown applied — but you wouldn't pull the malicious version either, because pinning).
- Build-time / postinstall scripts in already-resolved versions.
- IDE extension supply-chain attacks (VSCode marketplace, JetBrains plugins) — different ecosystem.
- Direct `git clone && npm install` of a malicious repo (no registry involvement).

**Conclusion**: This raises the bar against the most common vector (registry-published-then-pulled patch). Layer with: SBOMs, periodic `npm audit` review, lockfile-diff review on dependency bumps, minimum-maintainer-trust scoring (e.g. `socket.dev`).

### Applied 2026-05-12 on cemini-workspace-laptop

- `~/.npmrc` — three cooldown lines appended (prefix preserved)
- `~/.bunfig.toml` — newly created with `minimumReleaseAge = 604800`
- `OSINT WORKSPACE/package.json` — `agnix ^0.24.0 → 0.24.0` (only dep; package-lock.json is workspace-gitignored, so step 4 N/A here)

For Cemini prod server: see `briefs/2026-05-12_npm-supply-chain-defense-cemini.md` — staged 2026-05-12 for manual scp + server-side execution.

### Cross-wiki relevance

- **Cybersec-wiki** (`@cybersecurity-wiki/concepts/npm-supply-chain-defense.md`): npm supply-chain is a recurring CVE source; the defensive-ops counterpart of this page lives in that wiki's defensive cluster. Cross-link is bidirectional.

## Snippets

From source prompt:
> the cooldown makes every package manager refuse any version published in the last 7 days. attack chains usually only last a couple hours, but this protects you long term and for any future attacks... which at this rate will keep happening

## Dead Ends

- `save-exact=true` does NOT retroactively pin existing dependencies in `package.json`. It only affects future `npm install <pkg>` invocations. Step 3 (manual `^` / `~` strip) is required for existing entries.
- `min-release-age` is a flag, not a registry-side enforcement — a malicious actor running their own private registry could ignore it. Trust boundary: assumes you're pulling from npmjs.com or a trusted mirror.
