#!/usr/bin/env python3
"""Fortune in a Pot.

Writes one kind, funny fortune for a houseplant on the windowsill,
at most 120 characters, to ``entry.txt`` under the output directory.

The grader runs this program with no network as
``python3 -P -s /bot/main.py`` and reads ``/output/entry.txt``; locally the
output directory can be overridden with ``MAKEFUN_OUTPUT_DIR``:

    MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt

The fortune is a fixed string on purpose: the run must be deterministic
(two runs, byte-identical output) and finish well inside the time budget.
Standard library only; no network, no clock, no randomness, no input.
"""

import os
from pathlib import Path

# One line, 115 characters, plain ASCII throughout: a fortune for the
# houseplant on the windowsill. Soon the morning sun finds its tallest
# leaf, and its keeper tells guests this windowsill has a favourite.
# ASCII-only keeps the character count and the byte count identical, so
# the 120-character gate holds either way.
FORTUNE = (
    "Soon the morning sun will find your tallest leaf, "
    "and your keeper will tell guests this windowsill has a favourite."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_NAME = "entry.txt"
MAX_CHARS = 120


def main() -> int:
    text = FORTUNE
    if not (1 <= len(text) <= MAX_CHARS) or not text.strip():
        raise SystemExit("fortune must be 1 to 120 non-blank characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("fortune must be a single line")
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    # Exactly the line, no trailing newline: the gate counts characters,
    # so nothing extra may ride along in the file.
    (out_dir / OUTPUT_NAME).write_text(text, encoding="utf-8", newline="")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
