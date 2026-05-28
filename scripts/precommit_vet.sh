#!/usr/bin/env bash
# Pre-commit hook: vet changed skills/briefs (requires `vet` on PATH).
set -euo pipefail
if ! command -v vet >/dev/null 2>&1; then
  echo "precommit_vet: install vet — pip install git+https://github.com/cemini23/vet.git"
  exit 1
fi
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
for f in "$@"; do
  case "$f" in
    */SKILL.md|*.cursor/skills/*/SKILL.md)
      vet "$f" --profile skillmd --strict
      ;;
    briefs/*)
      vet "$f" --profile brief --strict --root .
      ;;
    *)
      vet "$f" --profile minimal --strict
      ;;
  esac
done
