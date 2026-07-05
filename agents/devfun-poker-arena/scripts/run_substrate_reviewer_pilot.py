#!/usr/bin/env python3
"""K146 pilot — small-model reviewer on projected topology (Gemma-class via OpenRouter).

Usage:
  uv run python scripts/prepare_substrate_reviewer_pack.py
  uv run python scripts/run_substrate_reviewer_pilot.py
  uv run python scripts/run_substrate_reviewer_pilot.py --dry-run
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PACK = ROOT / "reports/substrate-reviewer/pack"
OUT_DIR = ROOT / "reports/substrate-reviewer/pilot"
DEFAULT_MODEL = "google/gemma-3-27b-it"


def _load_env() -> None:
    for p in (
        Path.home() / ".cemini" / "llm-routing.env",
        Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/.env"),
        ROOT / ".env",
    ):
        if not p.is_file():
            continue
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v


def _call_openrouter(*, api_key: str, model: str, prompt: str) -> str:
    import httpx

    url = "https://openrouter.ai/api/v1/chat/completions"
    body = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Expert Python poker-bot harness reviewer. "
                    "Topology-only audit — cite symbol names from the pack."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
        "max_tokens": 4000,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": os.environ.get("OPENROUTER_HTTP_REFERER", "https://github.com/cemini"),
        "X-Title": os.environ.get("OPENROUTER_APP_TITLE", "devfun-poker substrate pilot"),
    }
    r = httpx.post(url, headers=headers, json=body, timeout=180.0)
    r.raise_for_status()
    return (r.json()["choices"][0]["message"]["content"] or "").strip()


def main() -> int:
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--pack", type=Path, default=DEFAULT_PACK)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--model", default=os.environ.get("CEMINI_SUBSTRATE_REVIEWER_MODEL", DEFAULT_MODEL))
    args = p.parse_args()

    pack = args.pack.resolve()
    prompt_path = pack / "review_prompt.md"
    if not prompt_path.is_file():
        print(f"Missing {prompt_path} — run prepare_substrate_reviewer_pack.py first", file=sys.stderr)
        return 1

    prompt = prompt_path.read_text(encoding="utf-8")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")

    if args.dry_run:
        out = OUT_DIR / f"dry_run_{ts}.md"
        out.write_text(f"# Dry run — prompt only ({len(prompt)} chars)\n\n{prompt[:8000]}\n", encoding="utf-8")
        print(json.dumps({"dry_run": True, "prompt_chars": len(prompt), "out": str(out)}, indent=2))
        return 0

    _load_env()
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not key:
        print("OPENROUTER_API_KEY missing — use --dry-run or set key in ~/.cemini/llm-routing.env", file=sys.stderr)
        return 1

    print(f"Calling {args.model}...")
    try:
        text = _call_openrouter(api_key=key, model=args.model, prompt=prompt)
    except Exception as e:
        err = OUT_DIR / f"error_{ts}.txt"
        err.write_text(str(e), encoding="utf-8")
        print(f"FAIL: {e}", file=sys.stderr)
        return 1

    out = OUT_DIR / f"review_{ts}.md"
    out.write_text(text + "\n", encoding="utf-8")
    meta = {"timestamp": ts, "model": args.model, "pack": str(pack), "out": str(out), "chars": len(text)}
    (OUT_DIR / f"meta_{ts}.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
