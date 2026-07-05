#!/usr/bin/env python3
"""Backward-compatible entrypoint — see scripts.intel.monitors.jobs."""
from scripts.intel.monitors.jobs import main

if __name__ == "__main__":
    raise SystemExit(main())
