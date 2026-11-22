#!/usr/bin/env bash
# cemini-managed-hook-installer
#
# Install the tracked git hook(s) from scripts/hooks/ into .git/hooks/.
# Idempotent: rerun safely after a fresh clone or if .git/hooks is cleared.
#
# Usage:
#   bash scripts/install_git_hooks.sh           # install / refresh
#   bash scripts/install_git_hooks.sh --check   # report status; exit 1 if missing
#   bash scripts/install_git_hooks.sh --force   # overwrite a foreign hook
#
# The installer refuses to overwrite an existing hook that was not written by
# this workspace (no `# cemini-managed-hook` marker) unless --force is passed.

set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
SOURCE_DIR="$ROOT/scripts/hooks"
TARGET_DIR="$ROOT/.git/hooks"
MARKER="# cemini-managed-hook"

check_only=0
force=0
for arg in "$@"; do
    case "$arg" in
        --check) check_only=1 ;;
        --force) force=1 ;;
        -h|--help)
            sed -n '2,17p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
            exit 0
            ;;
        *)
            echo "Error: unknown argument: $arg" >&2
            exit 2
            ;;
    esac
done

if [[ ! -d "$TARGET_DIR" ]]; then
    echo "Error: $TARGET_DIR does not exist. Are you inside a git working tree?" >&2
    exit 1
fi

hooks=(pre-commit)
missing=0

for hook in "${hooks[@]}"; do
    source_path="$SOURCE_DIR/$hook"
    target="$TARGET_DIR/$hook"

    if [[ ! -f "$source_path" ]]; then
        echo "Error: tracked hook source missing: $source_path" >&2
        exit 1
    fi

    if (( check_only )); then
        if [[ -f "$target" ]] && grep -qF "$MARKER" "$target"; then
            echo "installed: $target"
        else
            echo "NOT installed: $target"
            missing=1
        fi
        continue
    fi

    if [[ -e "$target" ]] && ! grep -qF "$MARKER" "$target"; then
        if (( force )); then
            echo "overwriting foreign hook (--force): $target"
        else
            echo "Error: $target exists and is not cemini-managed." >&2
            echo "       Rerun with --force to overwrite it." >&2
            exit 1
        fi
    fi

    cp "$source_path" "$target"
    chmod +x "$target"
    echo "installed: $target"
done

if (( check_only )); then
    exit "$missing"
fi

exit 0
