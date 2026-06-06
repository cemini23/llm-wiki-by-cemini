#!/usr/bin/env bash
# Idempotent K102 Phase-0 laptop adoptions (2026-06-06).
# GO: deptry, typst (if brew), harness skill, flowforge skill.
# Steal-from: documented on wiki only (Polymarket-bot sizing → WC brief).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k102-phase0}"
mkdir -p "$PHASE0"

echo "==> deptry (MIT)"
if command -v pip3 >/dev/null 2>&1; then
  pip3 install --user -q deptry 2>/dev/null || pip3 install -q deptry
  deptry --version || true
fi

echo "==> typst (Apache-2.0) — optional brew"
if command -v typst >/dev/null 2>&1; then
  typst --version
elif command -v brew >/dev/null 2>&1; then
  if ! brew list typst >/dev/null 2>&1; then
    brew install typst || echo "WARN: brew install typst failed — install manually"
  fi
else
  echo "SKIP typst — install from https://github.com/typst/typst/releases"
fi

echo "==> revfactory/harness (Apache-2.0)"
HARNESS_DIR="$PHASE0/harness"
if [[ ! -d "$HARNESS_DIR/.git" ]]; then
  git clone --depth 1 https://github.com/revfactory/harness.git "$HARNESS_DIR"
fi
HARNESS_SKILL="$HOME/.claude/skills/revfactory-harness"
mkdir -p "$(dirname "$HARNESS_SKILL")"
rm -rf "$HARNESS_SKILL"
cp -R "$HARNESS_DIR" "$HARNESS_SKILL"
echo "  $HARNESS_SKILL"

echo "==> flowforge-skill (MIT)"
FLOW_DIR="$PHASE0/flowforge-skill"
if [[ ! -d "$FLOW_DIR/.git" ]]; then
  git clone --depth 1 https://github.com/wentong2022-arch/flowforge-skill.git "$FLOW_DIR"
fi
FLOW_SKILL="$HOME/.claude/skills/flowforge-skill"
mkdir -p "$(dirname "$FLOW_SKILL")"
rm -rf "$FLOW_SKILL"
cp -R "$FLOW_DIR" "$FLOW_SKILL"
echo "  $FLOW_SKILL"

echo "==> Policy reminder"
POLICY="$ROOT/.local/k102-phase0-adopt-notes.md"
if [[ ! -f "$POLICY" ]]; then
  mkdir -p "$ROOT/.local"
  cat >"$POLICY" <<'EOF'
# K102 Phase-0 adoptions — guardrails

- **harness** — laptop meta-skill only; does not replace lazy-tool/conductor.
- **typst** — optional PDF export for briefs; not on prod.
- **deptry** — run on `scripts/` manually: `deptry .` from repo roots with pyproject.
- **flowforge** — draw.io skill; prefer `.canvas.tsx` for OSINT visual deliverables.
- **Polymarket-bot** — steal sizing math via WC prod brief only; no Node install.
- **defending-code** — Docker cybersec sandbox; not adopted in this script.
EOF
fi

echo "Done. Notes: $POLICY"
