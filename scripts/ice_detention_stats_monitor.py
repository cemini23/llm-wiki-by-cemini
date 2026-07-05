#!/usr/bin/env python3
"""Backward-compatible entrypoint — see scripts.intel.monitors.detention_stats."""
from scripts.intel.monitors.detention_stats import main

if __name__ == "__main__":
    raise SystemExit(main())
