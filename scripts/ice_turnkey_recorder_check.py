#!/usr/bin/env python3
"""Backward-compatible entrypoint — see scripts.intel.monitors.recorder."""
from scripts.intel.monitors.recorder import main

if __name__ == "__main__":
    raise SystemExit(main())
