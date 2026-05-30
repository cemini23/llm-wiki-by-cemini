#!/usr/bin/env bash
# setup_obsidian_vault.sh — Obsidian graph layer over git wiki/ (K84 gap close).
#
# Copies versioned vault chrome into wiki/.obsidian/ (gitignored). Canonical
# content remains wiki/*.md in git; Obsidian is read/review + graph only.
#
# Usage:
#   bash scripts/setup_obsidian_vault.sh
#   bash scripts/setup_obsidian_vault.sh --open   # launch Obsidian app

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WIKI="$ROOT/wiki"
TEMPLATE="$ROOT/scripts/obsidian-vault-template"
OBSIDIAN_DIR="$WIKI/.obsidian"
OPEN=false
[[ "${1:-}" == "--open" ]] && OPEN=true

if [[ ! -d "$WIKI" ]]; then
  echo "ERROR: wiki/ not found at $WIKI" >&2
  exit 1
fi

mkdir -p "$OBSIDIAN_DIR"
for f in app.json graph.json core-plugins.json; do
  cp "$TEMPLATE/$f" "$OBSIDIAN_DIR/$f"
done

# Workspace pointer (optional — helps Obsidian remember vault name)
cat > "$OBSIDIAN_DIR/workspace-mobile.json" <<'EOF'
{}
EOF

echo "Obsidian vault ready: $WIKI"
echo "  Graph view: enable 'Show orphans' (configured in graph.json)"
echo "  Wikilinks: use [[page-slug]] in body OR keep @path/ syntax for git canon"
echo "  Pre-commit ritual: open Graph → filter orphans → cross-check wiki_lint.py"

if [[ "$OPEN" == true ]]; then
  if [[ -d "/Applications/Obsidian.app" ]]; then
    open -a Obsidian "$WIKI"
  else
    echo "Obsidian.app not found — install from https://obsidian.md then re-run with --open"
  fi
fi
