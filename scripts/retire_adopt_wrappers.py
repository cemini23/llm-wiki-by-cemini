#!/usr/bin/env python3
"""Move adopt_k*_phase*.sh bodies to scripts/adopt-waves/; leave thin wrappers at old paths."""
from __future__ import annotations

import re
import stat
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
WAVES = SCRIPTS / "adopt-waves"

WRAPPER = """#!/usr/bin/env bash
# DEPRECATED — use: bash scripts/adopt.sh {wave} {phase}
exec "$(cd "$(dirname "$0")" && pwd)/adopt.sh" {wave} {phase}
"""


def wave_phase(name: str) -> tuple[str, str] | None:
    m = re.match(r"adopt_(.+)_phase(0|1)\.sh$", name)
    if not m:
        return None
    return m.group(1), f"phase{m.group(2)}"


def main() -> int:
    WAVES.mkdir(exist_ok=True)
    moved = wrapped = 0
    for src in sorted(SCRIPTS.glob("adopt_k*_phase*.sh")):
        wp = wave_phase(src.name)
        if not wp:
            continue
        wave, phase = wp
        dest = WAVES / src.name
        if not dest.exists():
            dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            dest.chmod(dest.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
            moved += 1
        src.write_text(WRAPPER.format(wave=wave, phase=phase), encoding="utf-8")
        src.chmod(src.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        wrapped += 1
    print(f"moved={moved} wrapped={wrapped} waves_dir={WAVES}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
