#!/usr/bin/env python3
"""Patch laptop ~/.hermes/config.yaml — same aux/alias/reasoning discipline as librarian."""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patch_hermes_librarian_models import MODEL_ALIASES, patch_aux_block  # noqa: E402

import re


def main() -> None:
    p = pathlib.Path.home() / ".hermes" / "config.yaml"
    if not p.exists():
        raise SystemExit(f"missing {p}")
    text = p.read_text()

    text = re.sub(
        r"(?m)^  reasoning_effort: medium",
        "  reasoning_effort: low",
        text,
        count=1,
    )
    for aux_key in ("title_generation", "compression"):
        if f"  {aux_key}:" in text:
            text = patch_aux_block(text, aux_key)

    if "model_aliases:" not in text:
        text = text.rstrip() + "\n\n" + MODEL_ALIASES
    else:
        text = re.sub(
            r"(?ms)^model_aliases:.*?(?=^\S|\Z)",
            MODEL_ALIASES,
            text,
            count=1,
        )

    p.write_text(text)
    print(f"patched {p}")


if __name__ == "__main__":
    main()
