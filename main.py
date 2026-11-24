"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line, 108 characters, inside the 140-character
# gate: a robot vacuum's excuse for missing a spot, told in its own
# voice, rooted in its cliff sensor and its map.
# Revision note: the punchline turns on the vacuum's own hardware —
# the cliff sensor, not a generic apology — so the line reads as the
# machine keeping a straight face, as the judge brief asks.
import os

TEXT = (
    "My cliff sensor mistook the rug's shadow for a staircase, so I "
    "backed off. I don't fall downstairs for dust."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
