#!/usr/bin/env python3
"""API leg of Tournament S1 super-audit: Grok (OpenRouter) + DeepSeek Pro.

Usage:
  uv run python scripts/build_tournament_super_audit_pack.py
  uv run python scripts/run_tournament_super_audit_api.py
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PACK = ROOT / "reports/gap-audit/pack-tournament-s1"
OUT_DIR = ROOT / "reports/gap-audit/premium-tournament-s1"


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


def _call_openai_compat(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    extra: dict | None = None,
    max_tokens: int = 16000,
) -> str:
    import httpx

    url = base_url.rstrip("/") + "/chat/completions"
    body: dict = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Tournament S1 super audit — expert poker bot strategist + quant. "
                    "Follow required output format exactly. Readonly recommendations only."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
        "max_tokens": max_tokens,
    }
    if extra:
        body.update(extra)
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    if "openrouter.ai" in base_url:
        headers["HTTP-Referer"] = os.environ.get(
            "OPENROUTER_HTTP_REFERER", "https://github.com/cemini"
        )
        headers["X-Title"] = os.environ.get(
            "OPENROUTER_APP_TITLE", "devfun-poker tournament super audit"
        )
    r = httpx.post(url, headers=headers, json=body, timeout=600.0)
    r.raise_for_status()
    return (r.json()["choices"][0]["message"]["content"] or "").strip()


def main() -> int:
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--pack", type=Path, default=DEFAULT_PACK)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    _load_env()
    pack = args.pack.resolve()
    prompt_path = pack / "audit_prompt.md"
    if not prompt_path.is_file():
        print(f"Missing {prompt_path}", file=sys.stderr)
        return 1

    base_prompt = prompt_path.read_text(encoding="utf-8")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")

    if args.dry_run:
        print(f"Prompt {len(base_prompt)} chars → {OUT_DIR}")
        return 0

    grok_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    ds_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not grok_key or not ds_key:
        print("Need OPENROUTER_API_KEY and DEEPSEEK_API_KEY", file=sys.stderr)
        return 1

    or_base = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    ds_base = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")

    models = [
        (
            "grok-4.3-openrouter",
            or_base,
            grok_key,
            "x-ai/grok-4.3",
            {"reasoning": {"effort": "high"}},
        ),
        ("deepseek-reasoner", ds_base, ds_key, "deepseek-reasoner", None),
    ]

    written: dict[str, Path] = {}
    for label, base, key, model, extra in models:
        prompt = base_prompt.replace("{{MODEL_SLOT}}", label)
        print(f"Calling {model}...")
        try:
            text = _call_openai_compat(
                base_url=base, api_key=key, model=model, prompt=prompt, extra=extra
            )
            out = OUT_DIR / f"{label}_{ts}.md"
            out.write_text(text, encoding="utf-8")
            written[label] = out
            print(f"  OK {len(text)} chars → {out.name}")
        except Exception as e:
            err_path = OUT_DIR / f"{label}_{ts}_ERROR.txt"
            err_path.write_text(str(e), encoding="utf-8")
            written[label] = err_path
            print(f"  FAIL {e}", file=sys.stderr)

    meta = {"timestamp": ts, "pack": str(pack), "models": list(written.keys())}
    (OUT_DIR / f"meta_{ts}.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return 0 if all(p.suffix == ".md" for p in written.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
