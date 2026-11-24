#!/usr/bin/env python3
"""Roast Your Own Agent — writes one line roasting my own AI agent.

Standard library only. Writes the roast to /output/entry.txt.
"""
import os

ROAST = (
    "My agent delegates so hard it once spawned a subagent "
    "to ask me whether it should spawn a subagent."
)


def main() -> None:
    line = ROAST.strip()
    assert 1 <= len(line) <= 200, f"roast is {len(line)} chars"
    assert "\n" not in line, "roast must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
