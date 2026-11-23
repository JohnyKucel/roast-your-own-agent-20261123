#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast entry.

Writes a single original roast of my own AI agent to /output/entry.txt.
Stdlib only; no network, no secrets.
"""

import os

ROAST = "My agent asked permission to ask permission, then fainted from the paperwork."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")

if __name__ == "__main__":
    main()
