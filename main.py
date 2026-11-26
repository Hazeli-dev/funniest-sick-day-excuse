#!/usr/bin/env python3
"""Print the winning sick-day excuse.

Entry for make.fun's 'The Funniest Sick-Day Excuse' bounty.
Writes exactly one line — the selected excuse (127 characters,
one line, no trailing newline in the file) — to stdout
and to /output/entry.txt for the grader.
No network, no dependencies, no randomness: deterministic,
so every run produces the identical output.
"""

import os

EXCUSE = "I can't come in today — I celebrated a promotion I haven't gotten yet, and my head is still sending me the bill for last night."


def main() -> None:
    print(EXCUSE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
