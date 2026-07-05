#!/usr/bin/env python3
"""Build K146 substrate reviewer pack (topology + audit JSON, no full source bodies)."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_CLI = ROOT / "scripts" / "docs_cli.py"
DEFAULT_OUT = ROOT / "reports/substrate-reviewer/pack"
HU_GUARD_SYMBOLS = (
    "_hu_wide_open_hand",
    "_hu_ladder_bb_defend",
    "_hero_set_vulnerable_on_four_straight",
    "_board_four_in_straight_window",
    "_board_four_to_flush",
    "_preflop_pot_committed_should_call",
)


def _run_docs_cli(*args: str) -> str:
    cmd = [sys.executable, str(DOCS_CLI), *args]
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr or proc.stdout or f"docs_cli failed: {args}")
    return proc.stdout


def _hu_guard_block() -> str:
    lines = []
    for sym in HU_GUARD_SYMBOLS:
        try:
            out = _run_docs_cli("symbol", "examples/cemini_decide.py", sym)
            lines.append(out.strip())
            lines.append("")
        except RuntimeError:
            lines.append(f"MISSING: {sym}")
            lines.append("")
    return "\n".join(lines).strip()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = p.parse_args(argv)

    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    audit_dir = out / "substrate"
    subprocess.run(
        [sys.executable, str(DOCS_CLI), "audit", "--out-dir", str(audit_dir)],
        cwd=ROOT,
        check=True,
    )
    audit = json.loads((audit_dir / "substrate_audit.json").read_text(encoding="utf-8"))
    topology = (audit_dir / "substrate_topology.txt").read_text(encoding="utf-8")
    hu_guards = _hu_guard_block()

    template = (ROOT / "prompts" / "substrate_reviewer_pilot.md").read_text(encoding="utf-8")
    prompt = (
        template.replace("{{MODEL_SLOT}}", "pack")
        .replace("{substrate_audit}", json.dumps(
            {k: v for k, v in audit.items() if k != "topology"}, indent=2,
        ))
        .replace("{topology}", topology[:12000])
        .replace("{hu_guards}", hu_guards)
    )
    (out / "review_prompt.md").write_text(prompt, encoding="utf-8")
    (out / "hu_guards.txt").write_text(hu_guards + "\n", encoding="utf-8")

    meta = {
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "gate_pass": audit.get("gate_pass"),
        "prompt_chars": len(prompt),
        "hu_guards_checked": len(HU_GUARD_SYMBOLS),
    }
    (out / "manifest.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return 0 if audit.get("gate_pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
