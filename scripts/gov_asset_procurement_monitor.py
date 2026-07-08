#!/usr/bin/env python3
"""Backward-compatible entrypoint — see scripts.intel.monitors.procurement."""
from scripts.intel.monitors.procurement import main

if __name__ == "__main__":
    raise SystemExit(main())
