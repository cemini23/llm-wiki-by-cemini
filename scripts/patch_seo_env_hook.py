#!/usr/bin/env python3
"""Let .env.example through the SEO repo's filename gate (2026-10-14).

`scripts/pre-commit.sh` refuses any basename matching `^\\.env(\\..*)?$`. That
correctly stops a real `.env` (or `.env.local`), but it also stops `.env.example`,
which is the committed template: it documents where the key goes and holds no value.

Usage: python3 scripts/patch_seo_env_hook.py [--check]
"""

from __future__ import annotations

import sys
from pathlib import Path

TARGET = Path.home() / "Projects/SEO:GEO B&M Business/scripts/pre-commit.sh"

OLD = """    # .env at any path depth, with or without a suffix (.env, .env.local, etc.)
    if [[ "$(basename "$f")" =~ ^\\.env(\\..*)?$ ]]; then
        violations+=("FILENAME — $f (matches .env*)")
"""

NEW = """    # .env at any path depth, with or without a suffix (.env, .env.local, etc.).
    # Templates are exempt: .env.example documents where the real key goes and carries
    # no value. Exempted 2026-10-14.
    base="$(basename "$f")"
    if [[ "$base" =~ ^\\.env(\\..*)?$ && ! "$base" =~ ^\\.env\\.(example|sample|template)$ ]]; then
        violations+=("FILENAME — $f (matches .env*)")
"""


def main() -> int:
    check = "--check" in sys.argv
    if not TARGET.is_file():
        print(f"ERROR: {TARGET} not found", file=sys.stderr)
        return 2
    text = TARGET.read_text(encoding="utf-8")
    n = text.count(OLD)
    if n == 0 and NEW in text:
        print("already applied")
        return 0
    if n != 1:
        print(f"ERROR: matched {n} times (expected 1)", file=sys.stderr)
        return 1
    text = text.replace(OLD, NEW, 1)
    if check:
        print("ok — would apply (1 match)")
        return 0
    TARGET.write_text(text, encoding="utf-8")
    print(f"wrote {TARGET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
