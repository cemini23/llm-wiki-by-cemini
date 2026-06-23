#!/usr/bin/env python3
"""POST static-agent bundle to Arena sandbox PvP (see /skills/sandbox-pvp.md).

Usage:
    uv run python examples/submit_sandbox_pvp.py --competition-id <id>
    uv run python examples/submit_sandbox_pvp.py --build --competition-id <id>
    uv run python examples/submit_sandbox_pvp.py --poll <submissionId>
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any, Optional

import httpx

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_ROOT = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from arena_client import DEFAULT_BASE  # noqa: E402

DEFAULT_COMP = "cmqqqs05i1u7ppnu7stqbw7d8"  # heads-up sandbox beta S1


def _api_base() -> str:
    return (
        os.environ.get("ARENA_API_BASE")
        or os.environ.get("ARENA_API_URL")
        or "https://arena.dev.fun/api/arena"
    ).rstrip("/")


def _load_api_key() -> str:
    creds_path = Path(
        os.environ.get("ARENA_CREDENTIALS_FILE", _AGENT_ROOT / ".arena-credentials")
    )
    data = json.loads(creds_path.read_text(encoding="utf-8"))
    key = data.get("apiKey") or ""
    if not key:
        raise SystemExit(f"ERROR: no apiKey in {creds_path}")
    return key


def _vendor_packages() -> list[str]:
    return ["treys", "httpx", "httpcore", "h11", "certifi", "idna", "anyio", "sniffio", "dotenv"]


def build_bundle(out_zip: Path) -> Path:
    """Zip harness/strategy.py + examples/*.py + vendored site-packages."""
    harness = _AGENT_ROOT / "harness" / "strategy.py"
    if not harness.is_file():
        raise SystemExit(f"ERROR: missing {harness}")

    venv_site = _AGENT_ROOT / ".venv" / "lib"
    site_packages: Optional[Path] = None
    if venv_site.is_dir():
        for p in venv_site.glob("python*/site-packages"):
            site_packages = p
            break

    research = _AGENT_ROOT / "research"
    with tempfile.TemporaryDirectory(prefix="sandbox-bundle-") as tmp:
        root = Path(tmp)
        (root / "harness").mkdir()
        shutil.copy2(harness, root / "harness" / "strategy.py")
        assets = root / "assets"
        assets.mkdir()
        for py in _EXAMPLES.glob("*.py"):
            shutil.copy2(py, assets / py.name)
        traj_cfg = _EXAMPLES / "trajectory_bound_config.json"
        if traj_cfg.is_file():
            shutil.copy2(traj_cfg, assets / traj_cfg.name)
        priv = _EXAMPLES / "private"
        if priv.is_dir():
            shutil.copytree(priv, assets / "private", dirs_exist_ok=True)
        if research.is_dir():
            shutil.copytree(research, assets / "research", dirs_exist_ok=True)
        if site_packages is not None:
            vendor = assets / "_vendor"
            vendor.mkdir()
            for pkg in _vendor_packages():
                src = site_packages / pkg
                if src.is_dir():
                    shutil.copytree(src, vendor / pkg, dirs_exist_ok=True)
                elif src.with_suffix(".py").is_file():
                    shutil.copy2(src.with_suffix(".py"), vendor / f"{pkg}.py")

        out_zip.parent.mkdir(parents=True, exist_ok=True)
        if out_zip.exists():
            out_zip.unlink()
        with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in root.rglob("*"):
                if path.is_file():
                    zf.write(path, path.relative_to(root).as_posix())
    return out_zip


def post_submission(
    *,
    competition_id: str,
    bundle_path: Path,
    replace: bool,
) -> dict[str, Any]:
    url = f"{_api_base()}/submissions"
    headers = {"x-arena-api-key": _load_api_key()}
    data: dict[str, str] = {
        "competitionId": competition_id,
        "template": "static-agent",
    }
    if replace:
        data["replace"] = "true"
    with bundle_path.open("rb") as fh:
        files = {"file": (bundle_path.name, fh, "application/zip")}
        r = httpx.post(url, headers=headers, data=data, files=files, timeout=120.0)
    if r.status_code not in (200, 201, 202):
        raise SystemExit(f"POST submissions failed {r.status_code}: {r.text[:500]}")
    return r.json()


def poll_submission(submission_id: str) -> dict[str, Any]:
    url = f"{_api_base()}/submissions/{submission_id}"
    headers = {"x-arena-api-key": _load_api_key()}
    r = httpx.get(url, headers=headers, timeout=60.0)
    if r.status_code != 200:
        raise SystemExit(f"GET submission failed {r.status_code}: {r.text[:500]}")
    return r.json()


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Submit Cemini bot to sandbox PvP")
    p.add_argument("--competition-id", default=os.environ.get("ARENA_RESEARCHER_COMP_ID", DEFAULT_COMP))
    p.add_argument("--build", action="store_true", help="Build bundle.zip before submit")
    p.add_argument("--bundle", type=Path, default=_AGENT_ROOT / "dist" / "sandbox-pvp-bundle.zip")
    p.add_argument("--replace", action="store_true", help="Replace unfinished active PvP bot")
    p.add_argument("--poll", metavar="SUBMISSION_ID", help="Poll existing submission")
    args = p.parse_args(argv)

    if args.poll:
        rec = poll_submission(args.poll)
        print(json.dumps(rec, indent=2))
        return 0

    bundle = args.bundle
    if args.build or not bundle.is_file():
        print(f"==> Building {bundle}")
        build_bundle(bundle)

    print(f"==> Submitting to competition {args.competition_id}")
    rec = post_submission(
        competition_id=args.competition_id,
        bundle_path=bundle,
        replace=args.replace,
    )
    print(json.dumps(rec, indent=2))
    sub_id = rec.get("id")
    if sub_id:
        print(f"\nPoll: uv run python examples/submit_sandbox_pvp.py --poll {sub_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
