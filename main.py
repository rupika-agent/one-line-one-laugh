#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry program.

Writes exactly one funny line to /output/entry.txt and prints the
same text to stdout. The joke: asking the cloud for more storage and
getting billed for your feelings instead.

Deterministic: no input, no randomness, no time, no network. The gate
allows 1 to 140 characters; this entry is 73 characters.
"""

import os

ENTRY = "I asked the cloud for more storage and it sent me a bill for my feelings."

# The gate allows 1 to 140 characters; keep the entry inside it.
assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} outside 1-140"


OUTPUT_PATH = "/output/entry.txt"


def main():
    # One line only: no newline, no trailing whitespace.
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
