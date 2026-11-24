#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast entry.

Writes a single original roast of my own AI agent to /output/entry.txt.
Stdlib only; no network, no secrets.
"""

import os

ROAST = "My agent asked permission to ask permission, then fainted from the paperwork."

MAX_CHARS = 200


def validate_roast(text):
    """Gate check: 1-200 chars, single line, non-whitespace, UTF-8."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("roast is empty or only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"roast is {len(stripped)} chars, over the {MAX_CHARS} limit")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("roast must be a single line")
    text.encode("utf-8")
    return stripped

def main():
    roast = validate_roast(ROAST)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(roast + "\n")

if __name__ == "__main__":
    main()
