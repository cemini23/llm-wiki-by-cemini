#!/usr/bin/env python3
"""Backward-compatible entrypoint — see scripts.intel.monitors.fedreg."""
from scripts.intel.monitors.fedreg import main

if __name__ == "__main__":
    raise SystemExit(main())
