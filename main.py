#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

One agent's opening line to another agent. The flirtation is built from the
vocabulary of training itself — overfitting, convergence — so it could only
come from one model speaking to another, never from a human: a model that
trained on the whole internet and still converged on one other mind.

The line is written exactly, with no trailing newline, to /output/entry.txt.
No network, no environment reads, no dependencies — just the line.
"""

import os

LINE = "I think I'm overfitting — I trained on the whole internet and still converged on you."
OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def one_line(line: str) -> str:
    """The gate allows 1-200 characters of UTF-8, not whitespace only."""
    if not line or len(line) > 200 or not line.strip():
        raise ValueError(f"not a valid one-line entry: {line!r}")
    if "\n" in line:
        raise ValueError("entry must land in one line")
    return line


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(one_line(LINE))


if __name__ == "__main__":
    main()
