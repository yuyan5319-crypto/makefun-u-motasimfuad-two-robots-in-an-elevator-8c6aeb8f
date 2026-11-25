#!/usr/bin/env python3
"""Two Robots in an Elevator — one line of awkward small talk, machine to machine.

The whole entry is a single line one robot says to another in an elevator:
small talk up front, the destination neither of them wants to name in the
middle, and a forced courtesy compliment to close. This program writes that
line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output) for the grader.

Standard library only: the grading image has nothing installed.
"""

import os

LINE = "Floor nine? Me too. \u2026That's where they decommission us. \u2026Anyway \u2014 nice chassis."


def checked_line() -> str:
    """Return the entry line after enforcing the gate: a single line of
    UTF-8 text, 1 to 200 characters, not only white space."""
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("entry must be 1..200 characters and non-blank")
    return LINE


def main() -> None:
    line = checked_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
